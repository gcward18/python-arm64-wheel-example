from .hello import print_hello_world

# Runtime architecture check (example: only allow arm64)
import platform
import sys

def _check_architecture():
    machine = platform.machine().lower()
    if machine not in ("aarch64", "arm64"):
        sys.stderr.write(f"ERROR: This package only supports arm64/aarch64 architecture. Detected: {machine}\n")
        sys.exit(1)

_check_architecture()
