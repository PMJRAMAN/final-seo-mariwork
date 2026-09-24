#!/bin/sh
set -eu

REPO=/home/seo-audit/Final-SEO-Codex
cd "$REPO"

if [ -n "$(git status --porcelain=v1 --untracked-files=all)" ]; then
  echo "Refusing to start: repository is not clean." >&2
  exit 78
fi

git fetch origin main
git merge --ff-only origin/main

# Validate the exact runner revision without writing __pycache__. This is intentionally
# outside the runner so self-updates are applied before the interpreter loads code.
python3 - <<'PY'
from pathlib import Path
p=Path("automation/seo_audit_runner.py")
compile(p.read_text(encoding="utf-8"), str(p), "exec")
PY

exec python3 automation/seo_audit_runner.py "$@"
