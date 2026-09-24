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

echo "[2/6] Update repository as seo-audit"
runuser -u seo-audit -g seo-audit -- env HOME=/home/seo-audit \
  bash -c 'cd /home/seo-audit/Final-SEO-Codex && test -z "$(git status --porcelain=v1 --untracked-files=all)" && git fetch origin main && git merge --ff-only origin/main'

echo "[3/6] Syntax check before any restart — no bytecode artifact"
runuser -u seo-audit -g seo-audit -- env HOME=/home/seo-audit PYTHONDONTWRITEBYTECODE=1 \
  bash -c 'cd /home/seo-audit/Final-SEO-Codex && python3 -c '\''from pathlib import Path; p=Path("automation/seo_audit_runner.py"); compile(p.read_text(encoding="utf-8"), str(p), "exec")'\'''

echo "[4/6] Pin low-consumption Foundation default"
mkdir -p /etc/systemd/system/mariwork-seo-audit.service.d
cat >/etc/systemd/system/mariwork-seo-audit.service.d/20-low-consumption-v2.conf <<'EOF'
[Service]
Environment=MARIWORK_CODEX_MODEL=gpt-5.6-luna
Environment=MARIWORK_CODEX_REASONING=medium
# bubblewrap/Codex sandbox needs AF_NETLINK for local namespace/route setup.
# This does not enable model networking; Codex remains network_access=false.
RestrictAddressFamilies=
RestrictAddressFamilies=AF_UNIX AF_INET AF_INET6 AF_NETLINK
ExecStart=
ExecStart=/home/seo-audit/Final-SEO-Codex/automation/run_latest.sh auto --push
EOF
systemctl daemon-reload

echo "[5/6] Build deterministic evidence now — no Codex model call"
install -o root -g root -m 0644 \
  "$REPO/automation/systemd/mariwork-seo-audit-prepare.service" \
  /etc/systemd/system/mariwork-seo-audit-prepare.service
systemctl daemon-reload
systemd-analyze verify /etc/systemd/system/mariwork-seo-audit-prepare.service
systemctl start mariwork-seo-audit-prepare.service

echo "[6/6] Show status"
runuser -u seo-audit -g seo-audit -- env HOME=/home/seo-audit   bash -c 'cd /home/seo-audit/Final-SEO-Codex && python3 automation/seo_audit_runner.py status'

echo
echo "v2 installed. The paused Codex job was NOT resumed."
echo "After the usage window resets, resume with:"
echo "runuser -u seo-audit -g seo-audit -- env HOME=/home/seo-audit CODEX_HOME=/home/seo-audit/.codex MARIWORK_SEO_RUNNER_STATE=/home/seo-audit/.local/state/mariwork-seo-runner MARIWORK_SEO_ISOLATED_RUNTIME=1 PATH=/usr/local/bin:/usr/bin:/bin LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 bash -c 'cd /home/seo-audit/Final-SEO-Codex && automation/run_latest.sh resume --push'"
