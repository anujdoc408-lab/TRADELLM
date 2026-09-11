"""First health-check program for the market research project.

This program deliberately makes no market prediction and places no trade.  It
only confirms that Python can run the project in a reproducible environment.
"""

from __future__ import annotations

import platform
from pathlib import Path


PROJECT_NAME = "Market AI Research"
PHASE = "Phase 1 — environment setup"


def project_root() -> Path:
    """Return the folder that contains this program."""
    return Path(__file__).resolve().parent


def main() -> None:
    """Print a small, safe health check for a new installation."""
    print(f"{PROJECT_NAME} health check")
    print(f"Current milestone: {PHASE}")
    print(f"Python version: {platform.python_version()}")
    print(f"Project folder: {project_root()}")
    print("Status: setup is working. No market data or trading logic has run.")


if __name__ == "__main__":
    main()
