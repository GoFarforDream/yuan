import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
FRONTEND = ROOT / "frontend"


def main() -> None:
    backend = subprocess.Popen(
        [
            sys.executable,
            "-m",
            "uvicorn",
            "backend.main:app",
            "--app-dir",
            str(ROOT),
            "--host",
            "127.0.0.1",
            "--port",
            "13144",
            "--reload",
        ],
    )
    frontend = subprocess.Popen(
        ["npm", "--prefix", str(FRONTEND), "run", "dev", "--", "--host", "127.0.0.1"],
        shell=True,
    )

    print("Backend:  http://127.0.0.1:13144")
    print("Frontend: http://127.0.0.1:5173")
    print("Press Ctrl+C to stop.")

    try:
        frontend.wait()
    except KeyboardInterrupt:
        pass
    finally:
        frontend.terminate()
        backend.terminate()


if __name__ == "__main__":
    main()
