import argparse
import os
import subprocess
import sys
import threading
import time
from urllib.error import URLError
from urllib.request import Request, urlopen


def _pump_lines(proc: subprocess.Popen, tag: str) -> None:
    if proc.stdout is None:
        return
    for raw_line in iter(proc.stdout.readline, ""):
        if not raw_line:
            break
        line = raw_line.rstrip("\r\n")
        sys.stdout.write(f"[{tag}] {line}\n")
        sys.stdout.flush()


def _wait_for_server(url: str, timeout: float = 10.0) -> bool:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            req = Request(url, headers={"X-Reader": "runner"}, method="GET")
            with urlopen(req, timeout=1.5) as resp:
                if resp.status == 200:
                    return True
        except (URLError, OSError, TimeoutError):
            time.sleep(0.15)
    return False


def _stop_process(proc: subprocess.Popen | None, name: str) -> None:
    if proc is None or proc.poll() is not None:
        return
    proc.terminate()
    try:
        proc.wait(timeout=4.0)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait(timeout=2.0)
    sys.stdout.write(f"[RUNNER] Stopped {name} (pid={proc.pid})\n")
    sys.stdout.flush()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Launch inspect_server.py and mutate_server.py, run two_way_hateoas_driver.py, and clean up."
    )
    parser.add_argument("--inspect-script", default="inspect_server.py")
    parser.add_argument("--mutate-script", default="mutate_server.py")
    parser.add_argument("--driver-script", default="two_way_hateoas_driver.py")
    parser.add_argument("--lock-file", default="hateoas_io.lock")
    parser.add_argument("--server", choices=["inspect", "mutate"], default="mutate")
    parser.add_argument("--prop", default="largest_fib")
    parser.add_argument("--val", default=None)
    parser.add_argument("--timeout-seconds", type=float, default=10.0)
    parser.add_argument("--max-hops", type=int, default=0)
    parser.add_argument("--step-delay", type=float, default=0.1)
    parser.add_argument("--no-script-exec", action="store_true")
    parser.add_argument("--no-custom-ast-fns", action="store_true")
    parser.add_argument("--json-diff", action="store_true")
    parser.add_argument("--skip-reset", action="store_true")
    args = parser.parse_args()

    here = os.path.dirname(os.path.abspath(__file__))
    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"

    inspect_proc: subprocess.Popen | None = None
    mutate_proc: subprocess.Popen | None = None
    driver_rc = 0

    try:
        inspect_proc = subprocess.Popen(
            [sys.executable, os.path.join(here, args.inspect_script)],
            cwd=here,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
        mutate_proc = subprocess.Popen(
            [sys.executable, os.path.join(here, args.mutate_script)],
            cwd=here,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )

        threads = [
            threading.Thread(target=_pump_lines, args=(inspect_proc, "INSP_PROC"), daemon=True),
            threading.Thread(target=_pump_lines, args=(mutate_proc, "MUT_PROC"), daemon=True),
        ]
        for t in threads:
            t.start()

        if not _wait_for_server("http://127.0.0.1:8001/peer", timeout=10.0):
            raise RuntimeError("Inspect server failed to start on :8001")
        if not _wait_for_server("http://127.0.0.1:8002/peer", timeout=10.0):
            raise RuntimeError("Mutate server failed to start on :8002")

        driver_cmd = [
            sys.executable,
            os.path.join(here, args.driver_script),
            "--server",
            args.server,
            "--prop",
            args.prop,
            "--timeout-seconds",
            str(args.timeout_seconds),
            "--max-hops",
            str(args.max_hops),
            "--step-delay",
            str(args.step_delay),
            "--lock-file",
            args.lock_file,
        ]
        if args.val is not None:
            driver_cmd.extend(["--val", args.val])
        if args.no_script_exec:
            driver_cmd.append("--no-script-exec")
        if args.no_custom_ast_fns:
            driver_cmd.append("--no-custom-ast-fns")
        if args.json_diff:
            driver_cmd.append("--json-diff")
        if args.skip_reset:
            driver_cmd.append("--skip-reset")

        driver_proc = subprocess.Popen(
            driver_cmd,
            cwd=here,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
        driver_thread = threading.Thread(target=_pump_lines, args=(driver_proc, "DRV_PROC"), daemon=True)
        driver_thread.start()
        driver_rc = driver_proc.wait()
        driver_thread.join(timeout=2.0)

    except KeyboardInterrupt:
        sys.stdout.write("\n[RUNNER] Interrupted by user; shutting down.\n")
        sys.stdout.flush()
        driver_rc = 130
    finally:
        _stop_process(mutate_proc, "mutate_server")
        _stop_process(inspect_proc, "inspect_server")

    raise SystemExit(driver_rc)


if __name__ == "__main__":
    main()
