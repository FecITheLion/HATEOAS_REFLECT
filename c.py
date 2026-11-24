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
}


def log_status(msg: str) -> None:
    print(msg, flush=True)


def req_json(url: str, method: str = "GET", reader: str = "client", timeout: float = 5.0) -> dict:
    req = Request(url, headers={"X-Reader": reader}, method=method)
    with urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def extract_comparable_state(doc: dict) -> dict:
    """Pull relevant state fields from a HATEOAS response or /peer snapshot."""
    if not isinstance(doc, dict):
        return {}
    if isinstance(doc.get("state"), dict):
        src = doc["state"]
    else:
        src = doc

    prime_check = doc.get("prime_check") if isinstance(doc.get("prime_check"), dict) else {}
    out = {}
    for key in ("largest_prime", "candidate", "schema", "document", "last_mode", "last_actor", "saved_at"):
        if key in src:
            out[key] = copy.deepcopy(src[key])
        elif key == "largest_prime" and "largest_prime" in prime_check:
            out["largest_prime"] = prime_check["largest_prime"]
        elif key == "candidate" and "n" in prime_check:
            out["candidate"] = prime_check["n"]
    return out


def compute_json_diff(prev_state: dict, curr_state: dict, path: str = "$") -> dict:
    """Compute a structured JSON diff with added, removed, and changed entries."""
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


def pick_next_link(current_doc: dict, hop_index: int, fallback_base: str) -> tuple[str, dict]:
    links = current_doc.get("_links") or {}
    rec_rel = current_doc.get("recommended_rel")

    if rec_rel and rec_rel in links:
        return rec_rel, links[rec_rel]

    for rel in ("peer_base", "peer_options", "options", "self"):
        if rel in links:
            return rel, links[rel]

    return "peer_base", {"href": f"{fallback_base}/?reader=loop_hop_{hop_index}", "method": "GET"}


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Run a timeout-bounded infinite two-way HATEOAS loop with distinct /options values, "
            "flushed status updates, and JSON state diffs per hop."
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
        default="candidate",
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
        "--json-diff",
        action="store_true",
        help="Print structured JSON diff objects in addition to the compact single-line diff",
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

    start_time = time.monotonic()
    deadline = start_time + max(0.1, args.timeout_seconds)
    hop = 0
    stop_reason = "completed"

    try:
        # Baseline peer snapshot before initial mutation
        baseline_peer = req_json(f"{peer_base}/peer", method="GET")
        tracked_state = extract_comparable_state(baseline_peer)
        log_status(f"[BASE] Initial state={json.dumps(tracked_state)}")

        # 1. Query /options
        q_prop = quote(args.prop)
        log_status(f"[INIT] Querying {primary_base}/options?prop={args.prop} ...")
        opts_doc = req_json(f"{primary_base}/options?prop={q_prop}", method="GET")
        options_list = opts_doc.get("options") or []
        peer_opts_link = (opts_doc.get("_links") or {}).get("peer_options")

        log_status(f"[INIT] Current={opts_doc.get('current_value')} | Options={options_list}")
        if peer_opts_link:
            peer_opts = req_json(peer_opts_link["href"], method=peer_opts_link.get("method", "GET"))
            log_status(f"[INIT] Peer ({peer_opts.get('from')}) options={peer_opts.get('options')}")

        # 2. Set initial property value
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
                fallback="7",
            )

        set_doc = req_json(
            f"{primary_base}/set?prop={q_prop}&val={quote(chosen_val)}",
            method="POST",
        )
        next_state = extract_comparable_state(set_doc) or {**tracked_state, args.prop: set_doc.get("updated", {}).get("value")}
        init_diff = compute_json_diff(tracked_state, next_state)
        tracked_state = next_state
        all_diffs.append({"phase": "init_set", "diff": init_diff})
        log_status(f"[SET ] {primary_base}/set -> {set_doc.get('updated')} | DIFF: {format_diff_compact(init_diff)}")

        # 3. Save initial state
        save_doc = req_json(f"{primary_base}/save", method="POST")
        log_status(f"[SAVE] {primary_base}/save -> file={save_doc.get('file')} saved={save_doc.get('saved')}")

        # 4. Infinite hop loop bounded by timeout_seconds (and optional max_hops)
        log_status(
            f"[LOOP] Starting infinite loop from {peer_base}/?reader={args.server} "
            f"(timeout={args.timeout_seconds}s, max_hops={'infinite' if args.max_hops <= 0 else args.max_hops})"
        )
        current_doc = req_json(f"{peer_base}/?reader={args.server}", method="GET")

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
            rec_rel, next_link = pick_next_link(current_doc, hop, peer_base)
            target_href = next_link.get("href", f"{peer_base}/")
            target_method = next_link.get("method", "GET").upper()

            log_status(
                f"[HOP {hop:03d} | +{elapsed:5.2f}s | rem={remaining:5.2f}s] "
                f"Following [{rec_rel}] {target_method} {target_href}"
            )
            current_doc = req_json(target_href, method=target_method, reader=args.server)

            hop_rel = current_doc.get("recommended_rel") or rec_rel
            hop_prop = REL_TO_PROPERTY.get(hop_rel, args.prop)
            hop_base_url, hop_opts_doc = query_options_for_target(
                target_href=target_href,
                default_prop=hop_prop,
                fallback_base=peer_base,
            )
            hop_options = hop_opts_doc.get("options") or []
            hop_used = get_used_set(hop_base_url, str(hop_prop))
            distinct_val = pick_distinct_option(
                options_list=hop_options,
                used_for_key=hop_used,
                current_val=hop_opts_doc.get("current_value"),
                hop_index=hop,
                fallback="13",
            )

            log_status(
                f"[HOP {hop:03d} | OPT ] {hop_base_url}/options?prop={hop_prop} "
                f"-> picked={distinct_val} (used={len(hop_used)})"
            )

            set_hop_doc = req_json(
                f"{hop_base_url}/set?prop={quote(str(hop_prop))}&val={quote(distinct_val)}",
                method="POST",
                reader=args.server,
            )
            save_hop_doc = req_json(f"{hop_base_url}/save", method="POST", reader=args.server)
            current_doc = req_json(
                f"{hop_base_url}/?reader={args.server}",
                method="GET",
                reader=args.server,
            )

            updated_state = extract_comparable_state(current_doc)
            if not updated_state:
                updated_state = extract_comparable_state(set_hop_doc)
            hop_diff = compute_json_diff(tracked_state, updated_state)
            tracked_state = updated_state
            all_diffs.append({"hop": hop, "prop": hop_prop, "diff": hop_diff})

            log_status(
                f"[HOP {hop:03d} | DIFF] saved={save_hop_doc.get('saved')} | "
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

    # 5. Reset both servers
    if not args.skip_reset:
        try:
            reset_primary = req_json(f"{primary_base}/reset", method="POST")
            reset_peer = req_json(f"{peer_base}/reset", method="POST")
            log_status(
                f"[RESET] {primary_base}/reset -> {reset_primary.get('reset')} | "
                f"{peer_base}/reset -> {reset_peer.get('reset')}"
            )
        except Exception as exc:
            log_status(f"[RESET] Warning during reset: {exc}")
    else:
        log_status("[RESET] Skipped (--skip-reset)")


if __name__ == "__main__":
    main()
