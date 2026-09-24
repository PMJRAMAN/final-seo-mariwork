# Autonomous Round-1 SEO Runner

این پوشه فقط راند اول تحقیق را خودکار می‌کند.

## مرز اختیار

Runner/Codex می‌تواند:
- inventory و baseline بسازد؛
- live site و داده‌های مجاز را read-only بررسی کند؛
- dossier بسازد؛
- finding و systemic finding ثبت کند؛
- پیشنهاد اولیه رفع مشکل بدهد؛
- تا status = `CODEX_AUDITED` پیش برود.

Runner/Codex نمی‌تواند:
- Production را تغییر دهد؛
- تصمیم نهایی title/meta/content/internal links/schema/redirect بگیرد؛
- dossier را SECOND_REVIEWED یا APPROVED کند؛
- Playbook rule را خودکار ACCEPTED کند.

اولین human decision gate = ChatGPT Second Review.

## اجرا

```bash
python3 automation/seo_audit_runner.py status
python3 automation/seo_audit_runner.py auto --push
```

برای اجرای محدود:

```bash
python3 automation/seo_audit_runner.py auto --max-jobs 5 --push
```

اگر Codex به usage/rate limit یا auth مشکل بخورد، runner state را بیرون repo نگه می‌دارد و pause می‌شود. بعد از رفع مشکل:

```bash
python3 automation/seo_audit_runner.py resume --push
```

صفحه‌ای که دو بار به خطای غیر-limit بخورد در state داخلی runner blocked می‌شود و صف ادامه پیدا می‌کند:

```bash
python3 automation/seo_audit_runner.py status
python3 automation/seo_audit_runner.py retry-page ENTITY_ID
```

## State و logs

پیش‌فرض:

`~/.local/state/mariwork-seo-runner/`

قابل override:

```bash
export MARIWORK_SEO_RUNNER_STATE=/safe/path
```

Model در repo hard-code نشده است:

```bash
export MARIWORK_CODEX_MODEL="MODEL_ID"
export MARIWORK_CODEX_REASONING="high"
```

اگر unset باشد، تنظیم فعلی Codex استفاده می‌شود.

## Safety

- هر job در Git worktree موقت اجرا می‌شود.
- Codex فقط مسیرهای allowlist همان job را می‌تواند تغییر دهد؛ validator تغییر خارج scope را رد می‌کند.
- repo اصلی قبل از هر job باید clean باشد.
- پیش از هر job، runner در branch `main` از `origin/main` fetch می‌کند و فقط fast-forward را می‌پذیرد؛ خطای احراز هویت یا divergence صف را pause می‌کند.
- هر job موفق commit مستقل دارد.
- `--push` بعد از هر commit موفق branch فعلی را push می‌کند.
- autonomous worker باید تحت حساب/credentialی اجرا شود که Production write و DB-write در اختیارش نباشد.
- secrets/PII نباید وارد repo یا log prompt شوند.

## Hardened systemd runtime

The host-specific units in `automation/systemd/` run as `seo-audit`, deny
access to `/home/mariwork`, `/root`, and local database paths, and expose only
the SEO repository, Codex runtime, and external runner state as writable paths.
They are oneshot services with no automatic restart loop. Install/update them
as an administrator only after reviewing the paths and runtime isolation:

```bash
sudo install -o root -g root -m 0644 automation/systemd/mariwork-seo-audit-*.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start mariwork-seo-audit-smoke.service
sudo journalctl -u mariwork-seo-audit-smoke.service
sudo systemctl start mariwork-seo-audit.service
```

After a usage/rate-limit pause is resolved, use
`mariwork-seo-audit-resume.service`. A nonzero exit does not trigger a restart.
Logs in the service journal and runner JSONL contain job metadata only; raw
Codex JSONL output is not persisted. Runner state and restricted logs live in
`/home/seo-audit/.local/state/mariwork-seo-runner/`.

جزئیات setup سرور در `tasks/A-009-ROUND1-AUTOMATION.md`.
