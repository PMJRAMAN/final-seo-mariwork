# A-009 — Deploy Autonomous Round-1 SEO Audit Runner

**Program:** A — FOUNDATION / PRE-AUDIT  
**Mode:** SETUP / OPERATIONS  
**Production:** READ-ONLY  
**Human decision gate:** starts at ChatGPT Second Review  
**Next unlocked:** A-010 → A-021 → autonomous page CODEX_AUDITED queue

## Goal

Runner موجود در `automation/` را روی سرور به شکل ایمن راه‌اندازی کن و راند اول تحقیق SEO را شروع کن؛ به‌گونه‌ای که بعد از setup، کاربر فقط status/limit را گهگاه بررسی کند و بعد از رفع limit بتواند `resume` بزند.

## Read first

- MANIFEST.md
- AGENTS.md
- MASTER-TODO.md
- docs/WORKFLOW.md
- docs/CHANGE-CONTROL.md
- docs/SEO-OWNERSHIP.md
- automation/README.md
- automation/seo_audit_runner.py
- automation/round1_plan.json

## Required setup

1. مسیر واقعی repo و branch را verify کن.
2. نسخه فعلی Codex CLI و syntax واقعی `codex exec --help` را verify کن. اگر CLI فعلی با invocation runner تفاوت دارد، فقط runner/docs automation را با کمترین تغییر سازگار کن.
3. اجرای autonomous را با least privilege آماده کن:
   - no sudo during autonomous runs;
   - no WordPress/Production file writes;
   - no DB-write credentials exposed to autonomous Codex;
   - network فقط به اندازه نیاز برای Codex و public research;
   - اگر Rank Math/WP/server facts برای Foundation لازم است، یک read-only/sanitized evidence path بساز یا از read-only account موجود استفاده کن؛ هیچ secret/PII را commit نکن.
4. Git remote authentication را بدون ثبت secret در repo/log verify کن.
5. state/log path بیرون repo را بساز.
6. syntax-check:
   `python3 -m py_compile automation/seo_audit_runner.py`
7. status:
   `python3 automation/seo_audit_runner.py status`
8. یک smoke run ایمن انجام بده. اولین autonomous job باید A-010 باشد و هیچ Production write نداشته باشد.
9. خروجی و changed-file validator را verify کن.
10. پس از PASS شدن setup، A-009 را در MASTER-TODO به done تغییر بده و commit/push کن.
11. سپس worker را با این فرمان شروع کن:
   `python3 automation/seo_audit_runner.py auto --push`
   ترجیحاً آن را به یک service قابل start/stop تبدیل کن که روی exit ناشی از limit خودکار loop نکند. اگر systemd user/service در محیط مناسب نیست، روش پایدار معادل را مستند کن.
12. اگر usage/rate limit رخ داد، state باید حفظ شود. بعداً ادامه با:
   `python3 automation/seo_audit_runner.py resume --push`

## Hard prohibitions

- هیچ edit در public_html / WordPress / Woo / Rank Math / DB content.
- هیچ cache purge.
- هیچ slug/redirect/canonical/meta/schema implementation.
- هیچ raw GSC edit.
- هیچ customer/order data.
- هیچ APPROVED/SECOND_REVIEWED یا final content decision توسط Codex.
- برای راحتی runner دسترسی Production را broad نکن.

## Acceptance criteria

- runner syntax/preflight pass
- Codex CLI invocation verified on actual server
- runtime state outside repo
- Production write technically unavailable or safely isolated for autonomous worker
- first A-010 smoke job passes validator or exact blocker is documented
- rate-limit pause/resume path verified without losing completed work
- successful job creates a scoped commit and can push
- A-009 marked done only after setup passes
- autonomous queue has started or, if a safety blocker prevents start, exact blocker + safe remediation is recorded without weakening permissions
