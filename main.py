import argparse
import os
import signal
import socket
import subprocess
import sys
import time
from pathlib import Path


def wait_for_port(host: str, port: int, timeout: float = 10.0) -> None:
    deadline = time.monotonic() + timeout
    last_err: Exception | None = None
    while time.monotonic() < deadline:
        try:
            with socket.create_connection((host, port), timeout=0.5):
                return
        except OSError as exc:
            last_err = exc
            time.sleep(0.1)
    raise RuntimeError(f"Timed out waiting for {host}:{port} ({last_err})")


def start_background_server(script_path: Path, env: dict[str, str]) -> subprocess.Popen:
    popen_kwargs: dict = {
        "cwd": str(script_path.parent),
        "env": env,
        "stdout": subprocess.PIPE,
        "stderr": subprocess.STDOUT,
        "text": True,
        "bufsize": 1,
    }
    if os.name == "nt":
        popen_kwargs["creationflags"] = subprocess.CREATE_NEW_PROCESS_GROUP
    else:
        popen_kwargs["start_new_session"] = True

    return subprocess.Popen([sys.executable, "-u", str(script_path)], **popen_kwargs)


def stop_background_server(proc: subprocess.Popen | None, name: str, grace_seconds: float = 3.0) -> None:
    if proc is None or proc.poll() is not None:
        return

    print(f"[STACK] Stopping {name} (PID {proc.pid})...", flush=True)
    try:
        if os.name == "nt":
            proc.terminate()
        else:
            os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
    except ProcessLookupError:
        return

    deadline = time.monotonic() + grace_seconds
    while proc.poll() is None and time.monotonic() < deadline:
        time.sleep(0.1)

    if proc.poll() is None:
        print(f"[STACK] Force-killing {name} (PID {proc.pid})...", flush=True)
        try:
            if os.name == "nt":
                proc.kill()
            else:
                os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
        except ProcessLookupError:
            pass
        proc.wait(timeout=2.0)

    if proc.stdout is not None:
        try:
            remaining_logs = proc.stdout.read()
            if remaining_logs:
                for line in remaining_logs.strip().splitlines():
                    print(f"[{name} LOG] {line}", flush=True)
            proc.stdout.close()
        except Exception:
            pass


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Launch inspect_server.py and mutate_server.py, run two_way_hateoas_driver.py, and stop both servers."
    )
    parser.add_argument(
        "--base-dir",
        default=".",
        help="Directory containing inspect_server.py, mutate_server.py, and two_way_hateoas_driver.py (default: %(default)s)",
    )
    parser.add_argument(
        "--startup-timeout",
        type=float,
        default=10.0,
        help="Seconds to wait for ports 8001 and 8002 to open (default: %(default)s)",
    )
    parser.add_argument(
        "--show-server-logs",
        action="store_true",
        help="Print server logs after the driver exits",
    )
    parser.add_argument(
        "driver_args",
        nargs=argparse.REMAINDER,
        help="Arguments passed directly to two_way_hateoas_driver.py (prefix with '--' if needed)",
    )
    args = parser.parse_args()

    base_dir = Path(args.base_dir).resolve()
    inspect_script = base_dir / "inspect_server.py"
    mutate_script = base_dir / "mutate_server.py"
    driver_script = base_dir / "two_way_hateoas_driver.py"

    for required in (inspect_script, mutate_script, driver_script):
        if not required.exists():
            print(f"[ERROR] Missing required script: {required}", file=sys.stderr, flush=True)
            return 1

    forwarded_args = list(args.driver_args)
    if forwarded_args and forwarded_args[0] == "--":
        forwarded_args = forwarded_args[1:]

    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"

    inspect_proc: subprocess.Popen | None = None
    mutate_proc: subprocess.Popen | None = None
    driver_exit_code = 1

    def _handle_signal(signum, _frame):
        raise KeyboardInterrupt(f"Received signal {signum}")

    signal.signal(signal.SIGINT, _handle_signal)
    if hasattr(signal, "SIGTERM"):
        signal.signal(signal.SIGTERM, _handle_signal)

    try:
        print("[STACK] Starting inspect_server.py on :8001...", flush=True)
        inspect_proc = start_background_server(inspect_script, env)

        print("[STACK] Starting mutate_server.py on :8002...", flush=True)
        mutate_proc = start_background_server(mutate_script, env)

        wait_for_port("127.0.0.1", 8001, timeout=args.startup_timeout)
        wait_for_port("127.0.0.1", 8002, timeout=args.startup_timeout)
        print("[STACK] Both servers are listening on :8001 and :8002.", flush=True)

        driver_cmd = [sys.executable, "-u", str(driver_script), *forwarded_args]
        print(f"[STACK] Running driver: {' '.join(driver_cmd)}", flush=True)
        driver_res = subprocess.run(driver_cmd, cwd=str(base_dir), env=env)
        driver_exit_code = driver_res.returncode

    except KeyboardInterrupt as exc:
        print(f"\n[STACK] Interrupted ({exc}); shutting down...", flush=True)
        driver_exit_code = 130
    except Exception as exc:
        print(f"[STACK] Error: {exc}", file=sys.stderr, flush=True)
        driver_exit_code = 1
    finally:
        stop_background_server(mutate_proc, "MUTATE :8002")
        stop_background_server(inspect_proc, "INSPECT :8001")
        print(f"[STACK] Cleanup complete (driver_exit_code={driver_exit_code}).", flush=True)

    return driver_exit_code


if __name__ == "__main__":
    raise SystemExit(main())
