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

# Compile the exact runner revision that will be executed. This is intentionally
# outside Python so self-updates are applied before the interpreter loads code.
python3 -m py_compile automation/seo_audit_runner.py

exec python3 automation/seo_audit_runner.py "$@"
