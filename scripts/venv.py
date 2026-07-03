#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

"""Run commands in the project virtual environment."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VENV_DIR = ROOT / ".venv"
VENV_BIN = VENV_DIR / "bin"
VENV_ACTIVATE = VENV_BIN / "activate"


def ensure_venv() -> None:
    if VENV_ACTIVATE.is_file():
        return

    uv = shutil.which("uv")
    if uv:
        subprocess.run([uv, "venv", str(VENV_DIR)], check=True, cwd=ROOT)
        return

    print(f"Virtual environment not found at {VENV_DIR}", file=sys.stderr)
    print("Create it with: uv venv", file=sys.stderr)
    raise SystemExit(1)


def venv_env() -> dict[str, str]:
    env = os.environ.copy()
    env["VIRTUAL_ENV"] = str(VENV_DIR)
    env["PATH"] = f"{VENV_BIN}{os.pathsep}{env.get('PATH', '')}"
    env.pop("PYTHONHOME", None)
    return env


def main() -> None:
    ensure_venv()

    if len(sys.argv) > 1:
        os.execvpe(sys.argv[1], sys.argv[1:], venv_env())

    shell = os.environ.get("SHELL", "/bin/bash")
    os.execvpe(shell, [shell], venv_env())


if __name__ == "__main__":
    main()
