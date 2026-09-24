#!/bin/sh
set -eu

REPO=/home/seo-audit/Final-SEO-Codex
SERVICE=mariwork-seo-audit.service

if [ "$(id -u)" -ne 0 ]; then
  echo "Run this installer as root."
  exit 1
fi

echo "[1/6] Stop old runner"
systemctl stop "$SERVICE" 2>/dev/null || true

echo "[2/6] Update repository"
cd "$REPO"
git status --short
git fetch origin main
git merge --ff-only origin/main

echo "[3/6] Syntax check before any restart"
python3 -m py_compile automation/seo_audit_runner.py

echo "[4/6] Pin low-consumption Foundation default"
mkdir -p /etc/systemd/system/mariwork-seo-audit.service.d
cat >/etc/systemd/system/mariwork-seo-audit.service.d/20-low-consumption-v2.conf <<'EOF'
[Service]
Environment=MARIWORK_CODEX_REASONING=medium
EOF
systemctl daemon-reload

echo "[5/6] Build deterministic evidence now — no Codex model call"
runuser -u seo-audit -g seo-audit -- env   HOME=/home/seo-audit   CODEX_HOME=/home/seo-audit/.codex   MARIWORK_SEO_RUNNER_STATE=/home/seo-audit/.local/state/mariwork-seo-runner   MARIWORK_SEO_ISOLATED_RUNTIME=1   PATH=/usr/local/bin:/usr/bin:/bin   LANG=C.UTF-8   PYTHONDONTWRITEBYTECODE=1   bash -c 'cd /home/seo-audit/Final-SEO-Codex && python3 automation/seo_audit_runner.py prepare --push'

echo "[6/6] Show status"
runuser -u seo-audit -g seo-audit -- env HOME=/home/seo-audit   bash -c 'cd /home/seo-audit/Final-SEO-Codex && python3 automation/seo_audit_runner.py status'

echo
echo "v2 installed. The paused Codex job was NOT resumed."
echo "After the usage window resets, resume with:"
echo "runuser -u seo-audit -g seo-audit -- env HOME=/home/seo-audit CODEX_HOME=/home/seo-audit/.codex MARIWORK_SEO_RUNNER_STATE=/home/seo-audit/.local/state/mariwork-seo-runner MARIWORK_SEO_ISOLATED_RUNTIME=1 PATH=/usr/local/bin:/usr/bin:/bin LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 bash -c 'cd /home/seo-audit/Final-SEO-Codex && python3 automation/seo_audit_runner.py resume --push'"
