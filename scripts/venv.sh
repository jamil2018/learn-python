#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_ACTIVATE="$ROOT/.venv/bin/activate"

if [[ "${BASH_SOURCE[0]}" != "${0}" ]]; then
  # Sourced: activate the venv in the current shell.
  # Usage: source scripts/venv.sh
  if [[ ! -f "$VENV_ACTIVATE" ]]; then
    if command -v uv >/dev/null 2>&1; then
      uv venv "$ROOT/.venv"
    else
      echo "Virtual environment not found at $ROOT/.venv" >&2
      echo "Create it with: uv venv" >&2
      return 1
    fi
  else
    source "$VENV_ACTIVATE"
  fi
  return 0
fi

# Executed: prefer the uv script when uv is available.
# Usage: ./scripts/venv.sh [command ...]
if command -v uv >/dev/null 2>&1; then
  exec uv run --script "$ROOT/scripts/venv.py" "$@"
fi

if [[ ! -f "$VENV_ACTIVATE" ]]; then
  echo "Virtual environment not found at $ROOT/.venv" >&2
  echo "Create it with: uv venv" >&2
  exit 1
fi

source "$VENV_ACTIVATE"

if [[ $# -eq 0 ]]; then
  exec "$SHELL"
else
  exec "$@"
fi
