import argparse
import copy
import json
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlparse
from urllib.request import Request, urlopen

INSPECT_DEFAULT = "http://127.0.0.1:8001"
MUTATE_DEFAULT = "http://127.0.0.1:8002"

REL_TO_PROPERTY = {
    "peer_set_value": "candidate",
    "set_value": "candidate",
    "peer_options": "candidate",
    "options": "candidate",
    "inspect_mutate_json": "document",
    "mutate_json": "document",
    "inspect_mutate_schema": "schema",
    "mutate_schema": "schema",
    "mutate_step_prime": "largest_prime",
    "step_prime": "largest_prime",
    "mutate_step_fib": "largest_fib",
    "inspect_mutate_step_fib": "largest_fib",
    "step_fib": "largest_fib",
    "set_largest_fib": "largest_fib",
    "peer_set_largest_fib": "largest_fib",
    "set_fib_candidate": "fib_candidate",
    "peer_fib": "fib_candidate",
    "inspect_fib": "fib_candidate",
}


def log_status(msg: str) -> None:
    print(msg, flush=True)


def req_json(url: str, method: str = "GET", reader: str = "client", timeout: float = 5.0) -> dict:
    req = Request(url, data=None, headers={"X-Reader": reader}, method=method)
    with urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def execute_post_with_callback(post_href: str, reader: str) -> tuple[dict, dict | None]:
    post_doc = req_json(post_href, method="POST", reader=reader)
    cb_href = post_doc.get("callback_href")
    cb_method = (post_doc.get("callback_method") or "POST").upper()
    cb_doc = None
    if cb_href:
        cb_doc = req_json(cb_href, method=cb_method, reader=reader)
    elif (post_doc.get("_links") or {}).get("peer_callback"):
        cb_link = post_doc["_links"]["peer_callback"]
        cb_doc = req_json(cb_link["href"], method=cb_link.get("method", "POST").upper(), reader=reader)
    return post_doc, cb_doc


def extract_comparable_state(doc: dict) -> dict:
    if not isinstance(doc, dict):
        return {}
    out_to_post = doc.get("output_to_post") if isinstance(doc.get("output_to_post"), dict) else {}
    script_mut = (
        out_to_post.get("script_mutation_output")
        if isinstance(out_to_post.get("script_mutation_output"), dict)
        else {}
    )

    if isinstance(doc.get("state"), dict):
        src = doc["state"]
    elif isinstance(out_to_post.get("state"), dict):
        src = out_to_post["state"]
    else:
        src = doc

    resp_post = (
        out_to_post
        if out_to_post
        else (doc.get("response_to_post") if isinstance(doc.get("response_to_post"), dict) else {})
    )
    prime_check = doc.get("prime_check") if isinstance(doc.get("prime_check"), dict) else {}
    fib_check = doc.get("fib_check") if isinstance(doc.get("fib_check"), dict) else {}
    out = {}

    for key in (
        "largest_prime",
        "candidate",
        "largest_fib",
        "fib_candidate",
        "schema",
        "document",
        "script",
        "script_version",
        "last_mode",
        "last_actor",
        "saved_at",
    ):
        if key in src:
            out[key] = copy.deepcopy(src[key])
        elif key in resp_post:
            out[key] = copy.deepcopy(resp_post[key])
        elif key == "script" and "after_lines" in script_mut:
            out["script"] = copy.deepcopy(script_mut["after_lines"])
        elif key == "script_version" and "script_version" in script_mut:
            out["script_version"] = script_mut["script_version"]
        elif key == "largest_prime" and "largest_prime" in prime_check:
            out["largest_prime"] = prime_check["largest_prime"]
        elif key == "candidate" and "n" in prime_check:
            out["candidate"] = prime_check["n"]
        elif key == "largest_fib" and "largest_fib" in fib_check:
            out["largest_fib"] = fib_check["largest_fib"]
        elif key == "fib_candidate" and "n" in fib_check:
            out["fib_candidate"] = fib_check["n"]

    return out


def compute_json_diff(prev_state: dict, curr_state: dict, path: str = "$") -> dict:
    diff = {"added": {}, "removed": {}, "changed": {}}
    if not isinstance(prev_state, dict) or not isinstance(curr_state, dict):
        if prev_state != curr_state:
            diff["changed"][path] = {"from": prev_state, "to": curr_state}
        return diff

    prev_keys = set(prev_state.keys())
    curr_keys = set(curr_state.keys())

    for key in sorted(curr_keys - prev_keys):
        diff["added"][f"{path}.{key}"] = curr_state[key]
    for key in sorted(prev_keys - curr_keys):
        diff["removed"][f"{path}.{key}"] = prev_state[key]
    for key in sorted(prev_keys & curr_keys):
        p_val = prev_state[key]
        c_val = curr_state[key]
        child_path = f"{path}.{key}"
        if p_val == c_val:
            continue
        if isinstance(p_val, dict) and isinstance(c_val, dict):
            sub = compute_json_diff(p_val, c_val, child_path)
            diff["added"].update(sub["added"])
            diff["removed"].update(sub["removed"])
            diff["changed"].update(sub["changed"])
        else:
            diff["changed"][child_path] = {"from": p_val, "to": c_val}
    return diff


def format_diff_compact(diff: dict) -> str:
    parts = []
    for k, v in diff.get("changed", {}).items():
        parts.append(f"~{k}: {json.dumps(v.get('from'))} -> {json.dumps(v.get('to'))}")
    for k, v in diff.get("added", {}).items():
        parts.append(f"+{k}: {json.dumps(v)}")
    for k, v in diff.get("removed", {}).items():
        parts.append(f"-{k}: {json.dumps(v)}")
    return " | ".join(parts) if parts else "(no state diff)"


def format_option_value(opt) -> str:
    if isinstance(opt, (dict, list)):
        return json.dumps(opt)
    return str(opt)


def pick_distinct_option(
    options_list: list,
    used_for_key: set[str],
    current_val,
    hop_index: int,
    fallback: str = "7",
) -> str:
    formatted_opts = [format_option_value(opt) for opt in options_list]
    current_str = format_option_value(current_val) if current_val is not None else None

    for candidate_str in formatted_opts:
        if candidate_str not in used_for_key and candidate_str != current_str:
            used_for_key.add(candidate_str)
            return candidate_str

    for candidate_str in formatted_opts:
        if candidate_str not in used_for_key:
            used_for_key.add(candidate_str)
            return candidate_str

    try:
        base_num = int(current_str) if current_str is not None else int(fallback)
        synthesized = str(base_num + hop_index)
        while synthesized in used_for_key:
            synthesized = str(int(synthesized) + 1)
        used_for_key.add(synthesized)
        return synthesized
    except ValueError:
        synthesized = f"{fallback}_hop{hop_index}"
        used_for_key.add(synthesized)
        return synthesized


def query_options_for_target(target_href: str, default_prop: str, fallback_base: str) -> tuple[str, dict]:
    parsed = urlparse(target_href)
    base_url = f"{parsed.scheme}://{parsed.netloc}" if parsed.scheme and parsed.netloc else fallback_base
    prop = REL_TO_PROPERTY.get(default_prop, default_prop)
    q_prop = quote(str(prop))
    opts_doc = req_json(f"{base_url}/options?prop={q_prop}", method="GET")
    return base_url, opts_doc


def pick_next_instruction(current_doc: dict, hop_index: int, fallback_base: str) -> tuple[str, str, str]:
    nxt = current_doc.get("next_instruction")
    if isinstance(nxt, dict) and nxt.get("href"):
        return (
            nxt.get("rel", "next_instruction"),
            (nxt.get("method") or "GET").upper(),
            nxt["href"],
        )

    links = current_doc.get("_links") or {}
    rec_rel = current_doc.get("recommended_rel")
    if rec_rel and rec_rel in links:
        lnk = links[rec_rel]
        return rec_rel, (lnk.get("method") or "GET").upper(), lnk["href"]

    for rel in ("peer_callback", "peer_fib", "peer_base", "options", "self"):
        if rel in links:
            lnk = links[rel]
            return rel, (lnk.get("method") or "GET").upper(), lnk["href"]

    return "peer_base", "GET", f"{fallback_base}/?reader=loop_hop_{hop_index}"


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Run a body-free POST -> HATEOAS callback -> GET peer state -> POST /script/mutate -> "
            "OUTPUT TO POST + next_instruction loop with /script/exec, distinct /options values, "
            "JSON state diffs, flushed output, timeout, and reset."
        )
    )
    parser.add_argument("--inspect-base", default=INSPECT_DEFAULT, help="Inspect server base URL")
    parser.add_argument("--mutate-base", default=MUTATE_DEFAULT, help="Mutate server base URL")
    parser.add_argument(
        "--server",
        choices=["inspect", "mutate"],
        default="mutate",
        help="Primary server to start from (default: %(default)s)",
    )
    parser.add_argument(
        "--prop",
        default="largest_fib",
        help="Initial property name to query options for and set (default: %(default)s)",
    )
    parser.add_argument(
        "--val",
        default=None,
        help="Explicit initial value to set (defaults to a distinct option from /options)",
    )
    parser.add_argument(
        "--timeout-seconds",
        type=float,
        default=15.0,
        help="Timeout in seconds for the infinite loop before stopping and resetting (default: %(default)s)",
    )
    parser.add_argument(
        "--max-hops",
        type=int,
        default=0,
        help="Optional positive hop cap; 0 means run until --timeout-seconds expires (default: %(default)s)",
    )
    parser.add_argument(
        "--step-delay",
        type=float,
        default=0.1,
        help="Optional pause in seconds between hops (default: %(default)s)",
    )
    parser.add_argument(
        "--no-script-exec",
        action="store_true",
        help="Skip invoking POST /script/exec during hops",
    )
    parser.add_argument(
        "--json-diff",
        action="store_true",
        help="Print structured JSON diff objects in addition to compact diff lines",
    )
    parser.add_argument(
        "--diff-log",
        default=None,
        help="Optional file path to append each hop's structured JSON diff record",
    )
    parser.add_argument(
        "--skip-reset",
        action="store_true",
        help="Leave mutated/saved state on both servers instead of resetting at the end",
    )
    args = parser.parse_args()

    insp_base = args.inspect_base.rstrip("/")
    mut_base = args.mutate_base.rstrip("/")
    primary_base = insp_base if args.server == "inspect" else mut_base
    peer_base = mut_base if args.server == "inspect" else insp_base

    used_options: dict[tuple[str, str], set[str]] = {}
    all_diffs: list[dict] = []

    def get_used_set(base_url: str, prop_name: str) -> set[str]:
        return used_options.setdefault((base_url, str(prop_name)), set())

    def record_diff(label: str, next_state: dict) -> dict:
        nonlocal tracked_state
        merged_next = {**tracked_state, **next_state}
        diff = compute_json_diff(tracked_state, merged_next)
        tracked_state = merged_next
        entry = {"label": label, "diff": diff}
        all_diffs.append(entry)
        if args.diff_log:
            with open(args.diff_log, "a", encoding="utf-8") as f:
                f.write(json.dumps(entry) + "\n")
        return diff

    start_time = time.monotonic()
    deadline = start_time + max(0.1, args.timeout_seconds)
    hop = 0
    stop_reason = "completed"
    tracked_state: dict = {}

    try:
        baseline_peer = req_json(f"{peer_base}/peer", method="GET")
        tracked_state = extract_comparable_state(baseline_peer)
        log_status(f"[BASE] Initial state={json.dumps(tracked_state)}")

        q_prop = quote(args.prop)
        opts_doc = req_json(f"{primary_base}/options?prop={q_prop}", method="GET")
        options_list = opts_doc.get("options") or []

        init_used = get_used_set(primary_base, args.prop)
        if args.val is not None:
            chosen_val = args.val
            init_used.add(chosen_val)
        else:
            chosen_val = pick_distinct_option(
                options_list=options_list,
                used_for_key=init_used,
                current_val=opts_doc.get("current_value"),
                hop_index=0,
                fallback="5",
            )

        set_doc, set_cb_doc = execute_post_with_callback(
            f"{primary_base}/set?prop={q_prop}&val={quote(chosen_val)}",
            reader=args.server,
        )
        init_diff = record_diff(
            "init_set_callback",
            {**extract_comparable_state(set_doc), **extract_comparable_state(set_cb_doc or {})},
        )
        log_status(
            f"[SET ] Body-free POST -> callback_next={(set_cb_doc or {}).get('next_instruction', {}).get('rel')} "
            f"| DIFF: {format_diff_compact(init_diff)}"
        )

        save_doc, save_cb_doc = execute_post_with_callback(
            f"{primary_base}/save?reader={args.server}",
            reader=args.server,
        )
        log_status(f"[SAVE] Body-free POST saved={save_doc.get('post_result', {}).get('saved')}")

        current_doc = save_cb_doc or req_json(f"{peer_base}/?reader={args.server}", method="GET", reader=args.server)
        log_status(
            f"[LOOP] Starting callback loop (timeout={args.timeout_seconds}s, "
            f"max_hops={'infinite' if args.max_hops <= 0 else args.max_hops})"
        )

        while True:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                stop_reason = f"timeout after {args.timeout_seconds:.2f}s"
                log_status(f"[LOOP] Timeout reached ({stop_reason}); stopping loop.")
                break

            if args.max_hops > 0 and hop >= args.max_hops:
                stop_reason = f"max_hops ({args.max_hops}) reached"
                log_status(f"[LOOP] {stop_reason}; stopping loop.")
                break

            hop += 1
            elapsed = time.monotonic() - start_time
            rec_rel, target_method, target_href = pick_next_instruction(current_doc, hop, peer_base)

            log_status(
                f"[HOP {hop:03d} | +{elapsed:5.2f}s | rem={remaining:5.2f}s] "
                f"Instruction [{rec_rel}] {target_method} {target_href}"
            )

            if target_method == "POST":
                step_doc, cb_doc = execute_post_with_callback(target_href, reader=args.server)
                current_doc = cb_doc or step_doc
                log_status(
                    f"[HOP {hop:03d} | CB  ] POST->callback->GET_PEER->POST_SCRIPT->OUTPUT -> "
                    f"end_next={(current_doc.get('next_instruction') or {}).get('rel')}"
                )
            else:
                current_doc = req_json(target_href, method=target_method, reader=args.server)

            parsed_target = urlparse(target_href)
            target_base = (
                f"{parsed_target.scheme}://{parsed_target.netloc}"
                if parsed_target.scheme and parsed_target.netloc
                else peer_base
            )

            exec_doc = None
            exec_cb_doc = None
            if not args.no_script_exec:
                exec_doc, exec_cb_doc = execute_post_with_callback(
                    f"{target_base}/script/exec?reader={args.server}",
                    reader=args.server,
                )
                log_status(
                    f"[HOP {hop:03d} | EXEC] {target_base}/script/exec -> "
                    f"exec_ok={exec_doc.get('exec_ok')} updated_vars={exec_doc.get('updated_vars')}"
                )

            hop_next = (exec_cb_doc or current_doc).get("next_instruction") or {}
            hop_rel = hop_next.get("rel") or (exec_cb_doc or current_doc).get("recommended_rel") or rec_rel
            hop_prop = REL_TO_PROPERTY.get(hop_rel, "largest_fib")

            hop_base_url, hop_opts_doc = query_options_for_target(
                target_href=hop_next.get("href") or target_href,
                default_prop=hop_prop,
                fallback_base=target_base,
            )
            hop_options = hop_opts_doc.get("options") or []
            hop_used = get_used_set(hop_base_url, str(hop_prop))
            distinct_val = pick_distinct_option(
                options_list=hop_options,
                used_for_key=hop_used,
                current_val=hop_opts_doc.get("current_value"),
                hop_index=hop,
                fallback="8",
            )

            set_hop_doc, set_hop_cb = execute_post_with_callback(
                f"{hop_base_url}/set?prop={quote(str(hop_prop))}&val={quote(distinct_val)}&reader={args.server}",
                reader=args.server,
            )
            current_doc = set_hop_cb or set_hop_doc

            hop_state = {
                **extract_comparable_state(current_doc),
                **extract_comparable_state(set_hop_doc),
                **extract_comparable_state(exec_doc or {}),
                **extract_comparable_state(exec_cb_doc or {}),
            }
            hop_diff = record_diff(f"hop_{hop}", hop_state)

            log_status(
                f"[HOP {hop:03d} | DIFF] picked={distinct_val} | "
                f"next={(current_doc.get('next_instruction') or {}).get('rel')} | "
                f"{format_diff_compact(hop_diff)}"
            )
            if args.json_diff:
                log_status(f"[HOP {hop:03d} | JSON] {json.dumps(hop_diff)}")

            if args.step_delay > 0:
                time.sleep(min(args.step_delay, max(0.0, deadline - time.monotonic())))

    except KeyboardInterrupt:
        stop_reason = "interrupted by user (KeyboardInterrupt)"
        log_status(f"\n[LOOP] {stop_reason}; stopping loop.")
    except HTTPError as exc:
        err_body = exc.read().decode("utf-8", errors="replace")
        log_status(f"[ERROR] HTTP {exc.code}: {err_body}")
        raise SystemExit(1) from exc
    except URLError as exc:
        log_status(f"[ERROR] Connection failed: {exc.reason}")
        log_status("Ensure both inspect_server.py (:8001) and mutate_server.py (:8002) are running.")
        raise SystemExit(1) from exc

    log_status(
        f"\n[SUMMARY] Hops={hop} | DiffEvents={len(all_diffs)} | "
        f"Elapsed={time.monotonic() - start_time:.2f}s | Stop={stop_reason}"
    )

    if not args.skip_reset:
        try:
            reset_primary, _ = execute_post_with_callback(f"{primary_base}/reset", reader="client")
            reset_peer, _ = execute_post_with_callback(f"{peer_base}/reset", reader="client")
            log_status(
                f"[RESET] {primary_base}/reset -> {reset_primary.get('post_result', {}).get('reset')} | "
                f"{peer_base}/reset -> {reset_peer.get('post_result', {}).get('reset')}"
            )
        except Exception as exc:
            log_status(f"[RESET] Warning during reset: {exc}")
    else:
        log_status("[RESET] Skipped (--skip-reset)")


if __name__ == "__main__":
    main()
