"""Smoke test for the first project program."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class MainProgramTests(unittest.TestCase):
    def test_health_check_runs(self) -> None:
        result = subprocess.run(
            [sys.executable, "main.py"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            check=True,
            text=True,
        )

        self.assertIn("Market AI Research health check", result.stdout)
        self.assertIn("Status: setup is working", result.stdout)


if __name__ == "__main__":
    unittest.main()
