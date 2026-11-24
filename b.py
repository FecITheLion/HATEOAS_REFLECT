import ast
import copy
import json
import math
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, quote, urlparse
from urllib.request import Request, urlopen

INSPECT_HOST = "http://127.0.0.1:8001"
MUTATE_HOST = "http://127.0.0.1:8002"
STATE_FILE = "mutate_state.json"

DEFAULT_SCRIPT = [
    "candidate = 3",
    "largest_prime = 2",
    "fib_candidate = 2",
    "largest_fib = 1",
    "if candidate % 2 != 0:",
    "    largest_prime = candidate",
    "candidate = candidate + 1",
    "fib_candidate = fib_candidate + 1",
]

SAFE_BUILTINS = {
    "abs": abs,
    "min": min,
    "max": max,
    "len": len,
    "range": range,
    "int": int,
    "bool": bool,
    "True": True,
    "False": False,
}


def default_state() -> dict:
    return {
        "largest_prime": 2,
        "candidate": 3,
        "largest_fib": 1,
        "fib_candidate": 2,
        "schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}},
        "document": {"count": "3"},
        "script": list(DEFAULT_SCRIPT),
        "script_version": 1,
        "last_mode": "init",
        "last_actor": "mutate",
        "reading_peer": False,
        "saved_at": None,
    }


STATE = default_state()


def is_prime(n: int) -> bool:
    if not isinstance(n, int) or isinstance(n, bool) or n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = math.isqrt(n)
    d = 5
    while d <= limit:
        if n % d == 0 or n % (d + 2) == 0:
            return False
        d += 6
    return True


def next_prime_after(n: int) -> int:
    cur = max(2, int(n) + 1)
    while not is_prime(cur):
        cur += 1
    return cur


def is_fibonacci(n: int) -> bool:
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        return False
    if n in (0, 1):
        return True
    for term in (5 * n * n + 4, 5 * n * n - 4):
        root = math.isqrt(term)
        if root * root == term:
            return True
    return False


def next_fib_after(n: int) -> int:
    cur = max(1, int(n) + 1)
    while not is_fibonacci(cur):
        cur += 1
    return cur


def analyze_script(lines: list[str]) -> dict:
    source = "\n".join(lines)
    syntax_ok = True
    syntax_error = None
    assigned_vars: list[str] = []
    try:
        tree = ast.parse(source or "pass")
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id not in assigned_vars:
                        assigned_vars.append(target.id)
    except SyntaxError as exc:
        syntax_ok = False
        syntax_error = f"line {exc.lineno}: {exc.msg}"
    return {
        "line_count": len(lines),
        "syntax_ok": syntax_ok,
        "syntax_error": syntax_error,
        "assigned_vars": assigned_vars,
        "lines": lines,
    }


def execute_script_lines(lines: list[str], actor: str = "mutate") -> dict:
    source = "\n".join(lines) if lines else "pass"
    ns: dict = {
        "__builtins__": SAFE_BUILTINS,
        "largest_prime": STATE["largest_prime"],
        "candidate": STATE["candidate"],
        "largest_fib": STATE["largest_fib"],
        "fib_candidate": STATE["fib_candidate"],
    }
    exec_ok = True
    exec_error = None

    try:
        compiled = compile(source, "<hateoas_script>", "exec")
        exec(compiled, ns, ns)
    except Exception as exc:
        exec_ok = False
        exec_error = f"{type(exc).__name__}: {exc}"

    updated_vars: dict[str, int] = {}
    if exec_ok:
        cand_val = ns.get("candidate")
        if isinstance(cand_val, int) and not isinstance(cand_val, bool):
            STATE["candidate"] = cand_val
            updated_vars["candidate"] = cand_val
            if is_prime(cand_val) and cand_val > STATE["largest_prime"]:
                STATE["largest_prime"] = cand_val
                updated_vars["largest_prime"] = cand_val

        lp_val = ns.get("largest_prime")
        if isinstance(lp_val, int) and not isinstance(lp_val, bool) and lp_val >= 2:
            STATE["largest_prime"] = lp_val
            updated_vars["largest_prime"] = lp_val
            if STATE["candidate"] <= lp_val:
                STATE["candidate"] = lp_val + 1
                updated_vars["candidate"] = STATE["candidate"]

        fc_val = ns.get("fib_candidate")
        if isinstance(fc_val, int) and not isinstance(fc_val, bool):
            STATE["fib_candidate"] = fc_val
            updated_vars["fib_candidate"] = fc_val
            if is_fibonacci(fc_val) and fc_val > STATE["largest_fib"]:
                STATE["largest_fib"] = fc_val
                updated_vars["largest_fib"] = fc_val

        lf_val = ns.get("largest_fib")
        if isinstance(lf_val, int) and not isinstance(lf_val, bool) and lf_val >= 1:
            STATE["largest_fib"] = lf_val
            updated_vars["largest_fib"] = lf_val
            if STATE["fib_candidate"] <= lf_val:
                STATE["fib_candidate"] = lf_val + 1
                updated_vars["fib_candidate"] = STATE["fib_candidate"]

        STATE["last_mode"] = "script:exec"
        STATE["last_actor"] = actor

    exported_ns = {
        k: v
        for k, v in ns.items()
        if k != "__builtins__" and isinstance(v, (int, float, str, bool, list, dict))
    }

    return {
        "exec_ok": exec_ok,
        "exec_error": exec_error,
        "script_version": STATE["script_version"],
        "updated_vars": updated_vars,
        "locals_snapshot": exported_ns,
        "state": {
            "largest_prime": STATE["largest_prime"],
            "candidate": STATE["candidate"],
            "largest_fib": STATE["largest_fib"],
            "fib_candidate": STATE["fib_candidate"],
            "last_mode": STATE["last_mode"],
            "last_actor": STATE["last_actor"],
        },
    }


def mutate_script_lines(
    lines: list[str],
    op: str,
    line_text: str | None = None,
    var_name: str | None = None,
    val_text: str | None = None,
    index: int | None = None,
) -> tuple[list[str], str]:
    updated = list(lines)
    if op == "reset_script":
        return list(DEFAULT_SCRIPT), "reset_script"
    if op == "append_step":
        step = line_text if line_text else f"step_fib = {next_fib_after(STATE['largest_fib'])}"
        updated.append(step)
        return updated, f"append_step:{step}"
    if op == "set_var":
        var = var_name or "fib_candidate"
        val = val_text if val_text is not None else str(next_fib_after(STATE["largest_fib"]))
        assignment = f"{var} = {val}"
        replaced = False
        for i, existing in enumerate(updated):
            stripped = existing.lstrip()
            if stripped.startswith(f"{var} =") or stripped.startswith(f"{var}="):
                indent = existing[: len(existing) - len(stripped)]
                updated[i] = f"{indent}{assignment}"
                replaced = True
                break
        if not replaced:
            updated.append(assignment)
        return updated, f"set_var:{assignment}"
    if op == "replace_line" and index is not None and 0 <= index < len(updated):
        existing = updated[index]
        indent = existing[: len(existing) - len(existing.lstrip())]
        new_code = line_text if line_text is not None else f"# mutated line {index}"
        updated[index] = f"{indent}{new_code}"
        return updated, f"replace_line:{index}"
    if op == "toggle_step" and index is not None and 0 <= index < len(updated):
        existing = updated[index]
        stripped = existing.lstrip()
        indent = existing[: len(existing) - len(stripped)]
        if stripped.startswith("# "):
            updated[index] = f"{indent}{stripped[2:]}"
            return updated, f"uncomment:{index}"
        if stripped.startswith("#"):
            updated[index] = f"{indent}{stripped[1:]}"
            return updated, f"uncomment:{index}"
        updated[index] = f"{indent}# {stripped}"
        return updated, f"comment:{index}"
    fallback_line = line_text if line_text else f"# hop_fib = {STATE['fib_candidate']}"
    updated.append(fallback_line)
    return updated, f"append_fallback:{fallback_line}"


def _parse_value(raw: str):
    low = raw.strip().lower()
    if low == "true":
        return True
    if low == "false":
        return False
    if low in ("null", "none"):
        return None
    try:
        return int(raw)
    except ValueError:
        pass
    try:
        return float(raw)
    except ValueError:
        pass
    try:
        return json.loads(raw)
    except Exception:
        return raw


def set_property(prop: str, raw_val: str, actor: str = "mutate") -> dict:
    parsed_val = _parse_value(raw_val)
    if prop == "largest_prime" and isinstance(parsed_val, int):
        STATE["largest_prime"] = parsed_val
        if STATE["candidate"] <= parsed_val:
            STATE["candidate"] = parsed_val + 1
    elif prop == "candidate" and isinstance(parsed_val, int):
        STATE["candidate"] = parsed_val
    elif prop == "largest_fib" and isinstance(parsed_val, int):
        STATE["largest_fib"] = parsed_val
        if STATE["fib_candidate"] <= parsed_val:
            STATE["fib_candidate"] = parsed_val + 1
    elif prop == "fib_candidate" and isinstance(parsed_val, int):
        STATE["fib_candidate"] = parsed_val
    else:
        STATE[prop] = parsed_val
    if prop == "script":
        STATE["script_version"] = STATE.get("script_version", 1) + 1
    STATE["last_actor"] = actor
    STATE["last_mode"] = f"set:{prop}"
    return {"property": prop, "value": STATE.get(prop)}


def save_state_to_disk() -> dict:
    snapshot = copy.deepcopy(STATE)
    snapshot["reading_peer"] = False
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(snapshot, f, indent=2)
    STATE["saved_at"] = STATE_FILE
    return {"saved": True, "file": STATE_FILE, "state": snapshot}


def reset_state_data() -> dict:
    fresh = default_state()
    STATE.clear()
    STATE.update(fresh)
    if os.path.exists(STATE_FILE):
        try:
            os.remove(STATE_FILE)
        except OSError:
            pass
    return {"reset": True, "state": copy.deepcopy(STATE)}


def get_property_options(prop: str | None = None) -> dict:
    lp = STATE["largest_prime"]
    cand = STATE["candidate"]
    lf = STATE["largest_fib"]
    fcand = STATE["fib_candidate"]
    catalog = {
        "largest_prime": [2, 3, 5, 7, 11, lp, next_prime_after(lp)],
        "candidate": [cand, cand + 1, next_prime_after(cand - 1)],
        "largest_fib": [1, 2, 3, 5, 8, 13, lf, next_fib_after(lf)],
        "fib_candidate": [fcand, fcand + 1, next_fib_after(fcand - 1)],
        "script": [
            list(DEFAULT_SCRIPT),
            list(DEFAULT_SCRIPT) + [f"next_p = {next_prime_after(lp)}", f"next_f = {next_fib_after(lf)}"],
            ["fib_candidate = 8", "largest_fib = 8"],
        ],
        "script_op": ["append_step", "set_var", "replace_line", "toggle_step", "reset_script"],
    }
    if prop:
        return {
            "property": prop,
            "current_value": STATE.get(prop),
            "options": catalog.get(prop, [STATE.get(prop), None, True, False, 0, ""]),
            "available_properties": list(catalog.keys()),
        }
    return {
        "available_properties": list(catalog.keys()),
        "current_values": {k: STATE.get(k) for k in catalog if k in STATE},
        "options_by_property": catalog,
    }


def call_url(url: str, method: str = "GET", reader: str = "mutate") -> dict:
    STATE["reading_peer"] = True
    try:
        req = Request(url, data=None, headers={"X-Reader": reader}, method=method)
        with urlopen(req, timeout=3.0) as resp:
            return json.loads(resp.read().decode("utf-8"))
    finally:
        STATE["reading_peer"] = False


def _script_links(reader: str = "client") -> dict:
    nxt_prime = next_prime_after(STATE["largest_prime"])
    nxt_fib = next_fib_after(STATE["largest_fib"])
    return {
        "self": {"href": f"{MUTATE_HOST}/script?reader={reader}", "method": "GET"},
        "exec_script_here": {"href": f"{MUTATE_HOST}/script/exec?reader={reader}", "method": "POST"},
        "peer_exec_script": {"href": f"{INSPECT_HOST}/script/exec?reader=mutate", "method": "POST"},
        "peer_inspect_script": {"href": f"{INSPECT_HOST}/script/inspect?reader=mutate", "method": "GET"},
        "mutate_append_step": {
            "href": f"{MUTATE_HOST}/script/mutate?op=append_step&line={quote(f'fib_hit = {nxt_fib}')}&reader={reader}",
            "method": "POST",
        },
        "mutate_set_var": {
            "href": f"{MUTATE_HOST}/script/mutate?op=set_var&var=fib_candidate&val={nxt_fib}&reader={reader}",
            "method": "POST",
        },
        "mutate_set_prime_var": {
            "href": f"{MUTATE_HOST}/script/mutate?op=set_var&var=candidate&val={nxt_prime}&reader={reader}",
            "method": "POST",
        },
        "peer_base": {"href": f"{INSPECT_HOST}/?reader=mutate", "method": "GET"},
    }


def _two_way_links(reader: str = "client", prop: str = "largest_fib", val: str = "8") -> dict:
    q_prop = quote(str(prop))
    q_val = quote(str(val))
    fc = STATE["fib_candidate"]
    cand = STATE["candidate"]
    nxt_fib = next_fib_after(STATE["largest_fib"])
    nxt_prime = next_prime_after(STATE["largest_prime"])
    return {
        "self": {"href": f"{MUTATE_HOST}/?reader={reader}", "method": "GET"},
        "peer_base": {"href": f"{INSPECT_HOST}/?reader=mutate", "method": "GET"},
        "peer_state": {"href": f"{INSPECT_HOST}/peer?reader=mutate", "method": "GET"},
        "inspect_prime": {"href": f"{INSPECT_HOST}/inspect?n={cand}&reader=mutate", "method": "GET"},
        "inspect_fib": {"href": f"{INSPECT_HOST}/fib?n={fc}&reader=mutate", "method": "GET"},
        "peer_fib": {"href": f"{INSPECT_HOST}/fib?n={fc}&reader=mutate", "method": "GET"},
        "script": {"href": f"{MUTATE_HOST}/script?reader={reader}", "method": "GET"},
        "exec_script": {"href": f"{MUTATE_HOST}/script/exec?reader={reader}", "method": "POST"},
        "peer_exec_script": {"href": f"{INSPECT_HOST}/script/exec?reader=mutate", "method": "POST"},
        "peer_script": {"href": f"{INSPECT_HOST}/script?reader=mutate", "method": "GET"},
        "peer_inspect_script": {"href": f"{INSPECT_HOST}/script/inspect?reader=mutate", "method": "GET"},
        "options": {"href": f"{MUTATE_HOST}/options?prop={q_prop}", "method": "GET"},
        "peer_options": {"href": f"{INSPECT_HOST}/options?prop={q_prop}&reader=mutate", "method": "GET"},
        "set_value": {"href": f"{MUTATE_HOST}/set?prop={q_prop}&val={q_val}", "method": "POST"},
        "peer_set_value": {"href": f"{INSPECT_HOST}/set?prop={q_prop}&val={q_val}&reader=mutate", "method": "POST"},
        "step_prime": {"href": f"{MUTATE_HOST}/act?mode=step-prime&val={nxt_prime}&reader={reader}", "method": "POST"},
        "step_fib": {"href": f"{MUTATE_HOST}/act?mode=step-fib&val={nxt_fib}&reader={reader}", "method": "POST"},
        "save_state": {"href": f"{MUTATE_HOST}/save?reader={reader}", "method": "POST"},
        "peer_save_state": {"href": f"{INSPECT_HOST}/save?reader=mutate", "method": "POST"},
        "reset_state": {"href": f"{MUTATE_HOST}/reset?reader={reader}", "method": "POST"},
        "peer_reset_state": {"href": f"{INSPECT_HOST}/reset?reader=mutate", "method": "POST"},
        "peer_callback": {"href": f"{INSPECT_HOST}/callback?from=mutate&trigger=post", "method": "POST"},
        "peer_loop": {"href": f"{INSPECT_HOST}/loop?hops=5", "method": "GET"},
    }


def _callback_response_for_post(trigger_action: str, post_summary: dict, reader: str = "mutate") -> dict:
    peer_state = {}
    try:
        peer_state = call_url(f"{INSPECT_HOST}/peer", method="GET", reader="mutate")
    except Exception:
        peer_state = {}

    for k in ("largest_prime", "candidate", "largest_fib", "fib_candidate", "script", "script_version", "last_mode"):
        if k in peer_state and peer_state[k] is not None:
            STATE[k] = peer_state[k]

    observed_mode = peer_state.get("last_mode", trigger_action)
    if observed_mode == "step-prime" or "prime" in trigger_action:
        nxt_val = str(next_fib_after(STATE["largest_fib"]))
        script_url = f"{MUTATE_HOST}/script/mutate?op=set_var&var=fib_candidate&val={quote(nxt_val)}&reader=mutate"
        next_rel = "step_fib"
        next_prop = "largest_fib"
        reason = "Callback read Inspect state after prime step, mutated script fib_candidate, and instructs Fibonacci step."
    else:
        nxt_val = str(next_prime_after(STATE["largest_prime"]))
        script_url = f"{MUTATE_HOST}/script/mutate?op=set_var&var=candidate&val={quote(nxt_val)}&reader=mutate"
        next_rel = "step_prime"
        next_prop = "largest_prime"
        reason = "Callback read Inspect state, mutated script candidate, and instructs prime step."

    script_post_output = None
    try:
        script_post_output = call_url(script_url, method="POST", reader="mutate")
    except Exception as exc:
        script_post_output = {"error": str(exc)}

    instruction = {
        "rel": next_rel,
        "method": "POST",
        "href": f"{MUTATE_HOST}/act?mode={'step-fib' if next_rel == 'step_fib' else 'step-prime'}&val={nxt_val}&reader=mutate",
        "reason": reason,
    }

    output_to_post = {
        "status": "completed_callback_and_script_mutation",
        "trigger_action": trigger_action,
        "post_result": post_summary,
        "read_peer_state_endpoint": f"{INSPECT_HOST}/peer",
        "script_mutate_endpoint": script_url,
        "script_mutation_output": script_post_output,
        "state": {
            "largest_prime": STATE["largest_prime"],
            "candidate": STATE["candidate"],
            "largest_fib": STATE["largest_fib"],
            "fib_candidate": STATE["fib_candidate"],
            "script": STATE["script"],
            "script_version": STATE["script_version"],
        },
    }

    return {
        "from": "mutate",
        "role": "callback_responder",
        "reader": reader,
        "callback_flow": "POST -> B HATEOAS -> GET A STATE -> POST /script/mutate (no body) -> OUTPUT TO POST",
        "observed_peer_state": peer_state,
        "output_to_post": output_to_post,
        "response_to_post": output_to_post,
        "next_instruction": instruction,
        "recommended_rel": next_rel,
        "_links": _two_way_links(reader=reader, prop=next_prop, val=nxt_val),
    }


def mutate_and_decide(explicit_mode: str | None = None, explicit_val: str | None = None, reader: str = "client") -> dict:
    insp = {}
    try:
        insp = call_url(f"{INSPECT_HOST}/?reader=mutate", method="GET", reader="mutate")
    except Exception:
        insp = {}

    prime_info = insp.get("prime_check", {})
    if prime_info.get("largest_prime") is not None:
        STATE["largest_prime"] = prime_info["largest_prime"]
    if prime_info.get("n") is not None:
        STATE["candidate"] = prime_info["n"]

    fib_info = insp.get("fib_check", {})
    if fib_info.get("largest_fib") is not None:
        STATE["largest_fib"] = fib_info["largest_fib"]
    if fib_info.get("n") is not None:
        STATE["fib_candidate"] = fib_info["n"]

    policy = insp.get("policy", "")
    if explicit_mode:
        mode = explicit_mode
    elif policy == "after_prime_step_advance_fib":
        mode = "step-fib"
    elif policy == "after_fib_step_advance_prime":
        mode = "step-prime"
    else:
        mode = "step-fib"

    if mode == "step-prime":
        n = int(explicit_val) if explicit_val is not None else STATE["candidate"]
        if is_prime(n) and n > STATE["largest_prime"]:
            STATE["largest_prime"] = n
        STATE["candidate"] = n + 1
        suggest_prop, suggest_val = "largest_prime", str(next_prime_after(STATE["largest_prime"]))
    elif mode == "step-fib":
        fn = int(explicit_val) if explicit_val is not None else STATE["fib_candidate"]
        if is_fibonacci(fn) and fn > STATE["largest_fib"]:
            STATE["largest_fib"] = fn
        STATE["fib_candidate"] = fn + 1
        suggest_prop, suggest_val = "largest_fib", str(next_fib_after(STATE["largest_fib"]))
    else:
        suggest_prop, suggest_val = "fib_candidate", str(next_fib_after(STATE["largest_fib"]))

    STATE["last_mode"] = mode
    STATE["last_actor"] = reader

    return {
        "from": "mutate",
        "reader": reader,
        "post_body_required": False,
        "chosen_mode": mode,
        "based_on_inspect_policy": policy,
        "state": copy.deepcopy(STATE),
        "callback_href": f"{INSPECT_HOST}/callback?from=mutate&trigger={quote(mode)}",
        "callback_method": "POST",
        "recommended_rel": "peer_callback",
        "_links": _two_way_links(reader=reader, prop=suggest_prop, val=suggest_val),
    }


def run_auto_loop(max_hops: int = 6) -> dict:
    trace = []
    current_doc = call_url(f"{INSPECT_HOST}/?reader=mutate", method="GET", reader="mutate")
    trace.append({"hop": 1, "target": f"{INSPECT_HOST}/?reader=mutate", "method": "GET", "response": current_doc})

    visited_rels = set()
    for hop in range(2, max_hops + 1):
        rec_rel = current_doc.get("recommended_rel")
        links = current_doc.get("_links", {})
        if not rec_rel or rec_rel not in links or rec_rel in visited_rels:
            break
        visited_rels.add(rec_rel)
        link = links[rec_rel]
        href = link["href"]
        method = link.get("method", "GET").upper()
        current_doc = call_url(href, method=method, reader="mutate")
        trace.append({"hop": hop, "rel": rec_rel, "target": href, "method": method, "response": current_doc})

    return {
        "initiator": "mutate",
        "first_target": f"{INSPECT_HOST}/",
        "hops_executed": len(trace),
        "state": copy.deepcopy(STATE),
        "trace": trace,
    }


class MutateHandler(BaseHTTPRequestHandler):
    def _send_json(self, payload: dict, status: int = 200):
        body = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urlparse(self.path)
        qs = parse_qs(parsed.query)
        reader = qs.get("reader", ["inspect" if self.headers.get("X-Reader") == "inspect" else "client"])[0]
        prop = qs.get("prop", [None])[0]
        hops = int(qs.get("hops", ["6"])[0])
        n_val = int(qs["n"][0]) if "n" in qs else None

        if parsed.path == "/peer":
            self._send_json({
                "largest_prime": STATE["largest_prime"],
                "candidate": STATE["candidate"],
                "largest_fib": STATE["largest_fib"],
                "fib_candidate": STATE["fib_candidate"],
                "schema": STATE["schema"],
                "document": STATE["document"],
                "script": STATE["script"],
                "script_version": STATE["script_version"],
                "last_mode": STATE["last_mode"],
                "last_actor": STATE["last_actor"],
                "reading_peer": STATE["reading_peer"],
                "saved_at": STATE["saved_at"],
            })
        elif parsed.path == "/fib":
            insp_fib = {}
            try:
                insp_fib = call_url(f"{INSPECT_HOST}/fib?reader=mutate", method="GET", reader="mutate")
            except Exception:
                insp_fib = {}
            fn = STATE["fib_candidate"] if n_val is None else n_val
            fib_flag = is_fibonacci(fn)
            should_step = qs.get("step", ["false"])[0].lower() in ("1", "true", "yes")
            if should_step:
                if fib_flag and fn > STATE["largest_fib"]:
                    STATE["largest_fib"] = fn
                STATE["fib_candidate"] = fn + 1
                STATE["last_mode"] = "step-fib"
                STATE["last_actor"] = reader
            self._send_json({
                "from": "mutate",
                "reader": reader,
                "action": "step_fib" if should_step else "inspect_fib",
                "fib_check": {
                    "n": fn,
                    "is_fibonacci": fib_flag,
                    "largest_fib": STATE["largest_fib"],
                    "next_fib_candidate": STATE["fib_candidate"],
                    "saw_inspect_fib": (insp_fib or {}).get("fib_check"),
                },
                "recommended_rel": "peer_callback" if should_step else "step_fib",
                "_links": _two_way_links(reader=reader, prop="largest_fib", val=str(next_fib_after(STATE["largest_fib"]))),
            })
        elif parsed.path == "/script/exec":
            exec_res = execute_script_lines(STATE["script"], actor=reader)
            self._send_json({
                "from": "mutate",
                "reader": reader,
                "action": "exec_script",
                **exec_res,
                "recommended_rel": "peer_callback",
                "_links": _script_links(reader=reader),
            })
        elif parsed.path in ("/script", "/script/inspect"):
            analysis = analyze_script(STATE["script"])
            self._send_json({
                "from": "mutate",
                "reader": reader,
                "action": "inspect_script" if parsed.path == "/script/inspect" else "traverse_script",
                "script_version": STATE["script_version"],
                "analysis": analysis,
                "recommended_rel": "peer_callback",
                "_links": _script_links(reader=reader),
            })
        elif parsed.path == "/options":
            self._send_json({
                "from": "mutate",
                "reader": reader,
                **get_property_options(prop=prop),
                "recommended_rel": "set_value",
                "_links": _two_way_links(reader=reader, prop=prop or "largest_fib", val=str(next_fib_after(STATE["largest_fib"]))),
            })
        elif parsed.path == "/loop":
            self._send_json(run_auto_loop(max_hops=hops))
        elif parsed.path in ("/", "/inspect"):
            self._send_json(mutate_and_decide(reader=reader))
        else:
            self._send_json({"error": "Not found"}, status=404)

    def do_POST(self):
        parsed = urlparse(self.path)
        qs = parse_qs(parsed.query)
        reader = qs.get("reader", ["client"])[0]
        trigger_action = qs.get("trigger", [parsed.path])[0]

        if parsed.path == "/callback":
            self._send_json(_callback_response_for_post(trigger_action=trigger_action, post_summary={"path": parsed.path}, reader=reader))
            return

        if parsed.path == "/script/exec":
            exec_res = execute_script_lines(STATE["script"], actor=reader)
            self._send_json({
                "from": "mutate",
                "reader": reader,
                "post_body_required": False,
                "action": "exec_script",
                "post_result": exec_res,
                **exec_res,
                "callback_href": f"{INSPECT_HOST}/callback?from=mutate&trigger=script:exec",
                "callback_method": "POST",
                "recommended_rel": "peer_callback",
                "_links": _script_links(reader=reader),
            })
            return

        if parsed.path == "/fib":
            fn = int(qs["n"][0]) if "n" in qs else STATE["fib_candidate"]
            fib_flag = is_fibonacci(fn)
            if fib_flag and fn > STATE["largest_fib"]:
                STATE["largest_fib"] = fn
            STATE["fib_candidate"] = fn + 1
            STATE["last_mode"] = "step-fib"
            STATE["last_actor"] = reader
            self._send_json({
                "from": "mutate",
                "reader": reader,
                "post_body_required": False,
                "post_result": {"action": "step_fib", "n": fn, "is_fibonacci": fib_flag, "largest_fib": STATE["largest_fib"]},
                "callback_href": f"{INSPECT_HOST}/callback?from=mutate&trigger=fib",
                "callback_method": "POST",
                "recommended_rel": "peer_callback",
                "_links": _two_way_links(reader=reader, prop="largest_fib", val=str(next_fib_after(STATE["largest_fib"]))),
            })
            return

        if parsed.path == "/script/mutate":
            op = qs.get("op", ["append_step"])[0]
            line_text = qs.get("line", [None])[0]
            var_name = qs.get("var", [None])[0]
            val_text = qs.get("val", [None])[0]
            idx_raw = qs.get("index", [None])[0]
            idx = int(idx_raw) if idx_raw is not None else None

            before_lines = list(STATE["script"])
            after_lines, desc = mutate_script_lines(
                before_lines,
                op=str(op),
                line_text=line_text,
                var_name=var_name,
                val_text=val_text,
                index=idx,
            )
            STATE["script"] = after_lines
            STATE["script_version"] += 1
            STATE["last_mode"] = f"script:{desc}"
            STATE["last_actor"] = reader

            self._send_json({
                "from": "mutate",
                "reader": reader,
                "post_body_required": False,
                "post_result": {"mutation": desc, "script_version": STATE["script_version"], "line_count": len(after_lines)},
                "callback_href": f"{INSPECT_HOST}/callback?from=mutate&trigger=script:{quote(desc)}",
                "callback_method": "POST",
                "recommended_rel": "peer_callback",
                "_links": _script_links(reader=reader),
            })
            return

        prop = qs.get("prop", [None])[0]
        val = qs.get("val", [None])[0]

        if parsed.path == "/set":
            if prop is None or val is None:
                self._send_json({"error": "Provide 'prop' and 'val' as query parameters (no POST body needed)"}, status=400)
                return
            upd = set_property(str(prop), str(val), actor=reader)
            self._send_json({
                "from": "mutate",
                "reader": reader,
                "post_body_required": False,
                "post_result": {"updated": upd},
                "callback_href": f"{INSPECT_HOST}/callback?from=mutate&trigger=set:{quote(str(prop))}",
                "callback_method": "POST",
                "recommended_rel": "peer_callback",
                "_links": _two_way_links(reader=reader, prop=str(prop), val=str(val)),
            })
        elif parsed.path == "/save":
            saved = save_state_to_disk()
            self._send_json({
                "from": "mutate",
                "reader": reader,
                "post_body_required": False,
                "post_result": {"saved": saved["saved"], "file": saved["file"]},
                "callback_href": f"{INSPECT_HOST}/callback?from=mutate&trigger=save",
                "callback_method": "POST",
                "recommended_rel": "peer_callback",
                "_links": _two_way_links(reader=reader),
            })
        elif parsed.path == "/reset":
            reset_res = reset_state_data()
            self._send_json({
                "from": "mutate",
                "reader": reader,
                "post_body_required": False,
                "post_result": {"reset": reset_res["reset"]},
                "callback_href": f"{INSPECT_HOST}/callback?from=mutate&trigger=reset",
                "callback_method": "POST",
                "recommended_rel": "peer_callback",
                "_links": _two_way_links(reader=reader),
            })
        elif parsed.path == "/act":
            mode = qs.get("mode", [None])[0]
            self._send_json(mutate_and_decide(explicit_mode=mode, explicit_val=val, reader=reader))
        else:
            self._send_json({"error": "Not found"}, status=404)

    def log_message(self, format, *args):
        print(f"[MUTATE  :8002] {format % args}")


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 8002), MutateHandler)
    print("Callback-driven HATEOAS Mutate server on http://127.0.0.1:8002")
    server.serve_forever()
