import copy
import json
import math
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, quote, urlparse
from urllib.request import Request, urlopen

INSPECT_HOST = "http://127.0.0.1:8001"
MUTATE_HOST = "http://127.0.0.1:8002"
STATE_FILE = "inspect_state.json"


def default_state() -> dict:
    return {
        "largest_prime": 2,
        "candidate": 3,
        "schema": {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}},
        "document": {"count": "3"},
        "last_mode": "init",
        "last_actor": "inspect",
        "reading_peer": False,
        "saved_at": None,
    }


STATE = default_state()


def is_prime(n: int) -> bool:
    if n < 2:
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
    cur = max(2, n + 1)
    while not is_prime(cur):
        cur += 1
    return cur


def is_valid_shape(doc, schema) -> bool:
    if not isinstance(schema, dict) or not isinstance(doc, dict):
        return False
    props = schema.get("properties", {})
    for req in schema.get("required", []):
        if req not in doc:
            return False
    for k, v in doc.items():
        t = (props.get(k) or {}).get("type")
        if t == "integer" and not (isinstance(v, int) and not isinstance(v, bool)):
            return False
        if t == "string" and not isinstance(v, str):
            return False
        if t == "boolean" and not isinstance(v, bool):
            return False
    return True


def _parse_value(raw: str):
    low = raw.strip().lower()
    if low == "true":
        return True
    if low == "false":
        return False
    if low == "null" or low == "none":
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


def set_property(prop: str, raw_val: str, actor: str = "inspect") -> dict:
    parsed_val = _parse_value(raw_val)
    if prop == "largest_prime" and isinstance(parsed_val, int):
        STATE["largest_prime"] = parsed_val
        if STATE["candidate"] <= parsed_val:
            STATE["candidate"] = parsed_val + 1
    elif prop == "candidate" and isinstance(parsed_val, int):
        STATE["candidate"] = parsed_val
    else:
        STATE[prop] = parsed_val
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
    catalog = {
        "largest_prime": [2, 3, 5, 7, 11, lp, next_prime_after(lp)],
        "candidate": [cand, cand + 1, next_prime_after(cand - 1)],
        "last_mode": ["step-prime", "mutate-json", "mutate-schema", "set", "save", "reset"],
        "schema": [
            {"type": "object", "required": ["count"], "properties": {"count": {"type": "integer"}}},
            {"type": "object", "required": ["count"], "properties": {"count": {"type": ["integer", "string"]}}},
        ],
        "document": [
            {"count": "3"},
            {"count": 3},
            {"count": 3, "verified": True},
        ],
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
        "current_values": {k: STATE.get(k) for k in catalog},
        "options_by_property": catalog,
    }


def call_url(url: str, method: str = "GET", reader: str = "inspect") -> dict:
    STATE["reading_peer"] = True
    try:
        req = Request(url, headers={"X-Reader": reader}, method=method)
        with urlopen(req, timeout=3.0) as resp:
            return json.loads(resp.read().decode("utf-8"))
    finally:
        STATE["reading_peer"] = False


def _two_way_links(reader: str = "client", prop: str = "candidate", val: str = "7") -> dict:
    q_prop = quote(str(prop))
    q_val = quote(str(val))
    return {
        "self": {"href": f"{INSPECT_HOST}/?reader={reader}", "method": "GET"},
        "peer_base": {"href": f"{MUTATE_HOST}/?reader=inspect", "method": "GET"},
        "options": {"href": f"{INSPECT_HOST}/options?prop={q_prop}", "method": "GET"},
        "peer_options": {"href": f"{MUTATE_HOST}/options?prop={q_prop}&reader=inspect", "method": "GET"},
        "set_value": {"href": f"{INSPECT_HOST}/set?prop={q_prop}&val={q_val}", "method": "POST"},
        "peer_set_value": {"href": f"{MUTATE_HOST}/set?prop={q_prop}&val={q_val}&reader=inspect", "method": "POST"},
        "save_state": {"href": f"{INSPECT_HOST}/save", "method": "POST"},
        "peer_save_state": {"href": f"{MUTATE_HOST}/save?reader=inspect", "method": "POST"},
        "reset_state": {"href": f"{INSPECT_HOST}/reset", "method": "POST"},
        "peer_reset_state": {"href": f"{MUTATE_HOST}/reset?reader=inspect", "method": "POST"},
        "peer_loop": {"href": f"{MUTATE_HOST}/loop?hops=5", "method": "GET"},
    }


def inspect_and_decide(reader: str = "client") -> dict:
    peer = {}
    try:
        peer = call_url(f"{MUTATE_HOST}/peer", method="GET", reader="inspect")
    except Exception:
        peer = {}

    for k in ("largest_prime", "candidate", "schema", "document", "last_mode"):
        if k in peer and peer[k] is not None:
            STATE[k] = peer[k]

    n = STATE["candidate"]
    prime_flag = is_prime(n)
    valid_flag = is_valid_shape(STATE["document"], STATE["schema"])
    peer_mode = peer.get("last_mode", STATE["last_mode"])

    if not valid_flag:
        recommended_rel = "peer_set_value"
        policy = "shape_invalid_align_value"
        suggest_prop, suggest_val = "document", '{"count": 3}'
    elif peer_mode.startswith("set:"):
        recommended_rel = "peer_save_state"
        policy = "after_set_persist_state"
        suggest_prop, suggest_val = "candidate", str(next_prime_after(STATE["largest_prime"]))
    else:
        recommended_rel = "peer_options"
        policy = "query_peer_options_and_handoff"
        suggest_prop, suggest_val = "candidate", str(next_prime_after(STATE["largest_prime"]))

    return {
        "from": "inspect",
        "reader": reader,
        "policy": policy,
        "saw_mutate_mode": peer_mode,
        "prime_check": {"n": n, "is_prime": prime_flag, "largest_prime": STATE["largest_prime"]},
        "shape_valid": valid_flag,
        "recommended_rel": recommended_rel,
        "_links": _two_way_links(reader=reader, prop=suggest_prop, val=suggest_val),
    }


def run_auto_loop(max_hops: int = 6) -> dict:
    trace = []
    current_doc = call_url(f"{MUTATE_HOST}/?reader=inspect", method="GET", reader="inspect")
    trace.append({"hop": 1, "target": f"{MUTATE_HOST}/?reader=inspect", "method": "GET", "response": current_doc})

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
        current_doc = call_url(href, method=method, reader="inspect")
        trace.append({"hop": hop, "rel": rec_rel, "target": href, "method": method, "response": current_doc})

    return {
        "initiator": "inspect",
        "first_target": f"{MUTATE_HOST}/",
        "hops_executed": len(trace),
        "state": copy.deepcopy(STATE),
        "trace": trace,
    }


class InspectHandler(BaseHTTPRequestHandler):
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
        reader = qs.get("reader", ["mutate" if self.headers.get("X-Reader") == "mutate" else "client"])[0]
        prop = qs.get("prop", [None])[0]
        val = qs.get("val", [None])[0]
        hops = int(qs.get("hops", ["6"])[0])

        if parsed.path == "/peer":
            self._send_json({
                "largest_prime": STATE["largest_prime"],
                "candidate": STATE["candidate"],
                "schema": STATE["schema"],
                "document": STATE["document"],
                "last_mode": STATE["last_mode"],
                "last_actor": STATE["last_actor"],
                "reading_peer": STATE["reading_peer"],
                "saved_at": STATE["saved_at"],
            })
        elif parsed.path == "/options":
            self._send_json({
                "from": "inspect",
                "reader": reader,
                **get_property_options(prop=prop),
                "recommended_rel": "set_value",
                "_links": _two_way_links(reader=reader, prop=prop or "candidate", val=str(next_prime_after(STATE["largest_prime"]))),
            })
        elif parsed.path == "/loop":
            self._send_json(run_auto_loop(max_hops=hops))
        elif parsed.path == "/save":
            self._send_json({"from": "inspect", **save_state_to_disk(), "recommended_rel": "peer_base", "_links": _two_way_links(reader=reader)})
        elif parsed.path == "/reset":
            self._send_json({"from": "inspect", **reset_state_data(), "recommended_rel": "peer_base", "_links": _two_way_links(reader=reader)})
        elif parsed.path == "/set" and prop is not None and val is not None:
            upd = set_property(prop, val, actor=reader)
            self._send_json({"from": "inspect", "updated": upd, "state": copy.deepcopy(STATE), "recommended_rel": "save_state", "_links": _two_way_links(reader=reader, prop=prop, val=val)})
        elif parsed.path in ("/", "/inspect"):
            self._send_json(inspect_and_decide(reader=reader))
        else:
            self._send_json({"error": "Not found"}, status=404)

    def do_POST(self):
        parsed = urlparse(self.path)
        qs = parse_qs(parsed.query)
        reader = qs.get("reader", ["client"])[0]
        length = int(self.headers.get("Content-Length", "0"))
        body_obj = json.loads(self.rfile.read(length).decode("utf-8")) if length > 0 else {}

        prop = qs.get("prop", [body_obj.get("prop")])[0]
        val = qs.get("val", [body_obj.get("val")])[0]

        if parsed.path == "/set":
            if prop is None or val is None:
                self._send_json({"error": "Provide 'prop' and 'val' via query or JSON"}, status=400)
                return
            upd = set_property(str(prop), str(val), actor=reader)
            self._send_json({
                "from": "inspect",
                "updated": upd,
                "state": copy.deepcopy(STATE),
                "recommended_rel": "save_state",
                "_links": _two_way_links(reader=reader, prop=str(prop), val=str(val)),
            })
        elif parsed.path == "/save":
            self._send_json({
                "from": "inspect",
                **save_state_to_disk(),
                "recommended_rel": "peer_base",
                "_links": _two_way_links(reader=reader),
            })
        elif parsed.path == "/reset":
            self._send_json({
                "from": "inspect",
                **reset_state_data(),
                "recommended_rel": "peer_base",
                "_links": _two_way_links(reader=reader),
            })
        else:
            self._send_json({"error": "Not found"}, status=404)

    def log_message(self, format, *args):
        print(f"[INSPECT :8001] {format % args}")


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 8001), InspectHandler)
    print("Two-way HATEOAS Inspect server on http://127.0.0.1:8001")
    server.serve_forever()
