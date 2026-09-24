# SEO Decision Log

Accepted decisions override lower-level workflow/playbook text when applicable, but never override Manifest without formal Manifest change.

## SEO-001 — Dual Audit Mandatory
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** PROCESS

Codex Audit + independent ChatGPT Second Review before APPROVED.

## SEO-002 — Repository as Source of Truth
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** PROCESS

این repository مرجع رسمی dossier، findings، decisions و change history است.

## SEO-003 — Raw Search Data Is Immutable
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** DATA

Raw exports edit نمی‌شوند.

## SEO-004 — Page/Query Attribution Requires Joined Evidence
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** DATA

Query مستقل به URL خاص نسبت داده نمی‌شود مگر Page+Query relation اثبات شده باشد.

## SEO-005 — Findings Require Scope
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** PROCESS

PAGE/FAMILY/SITEWIDE اجباری.

## SEO-006 — Audit Is Read-Only on Production
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** OPERATIONS

Audit هیچ write روی Production ندارد.

## SEO-007 — Stable Entity ID Over Slug
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** REPOSITORY

برای WP/Woo entity، stable ID هویت dossier است.

## SEO-008 — Sitewide Technical Baseline Before Page Batches
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** PROCESS

Inventory و baseline فنی سراسری قبل از audit گسترده صفحه‌ها انجام می‌شود.

## SEO-009 — Independent Final QA After Implementation
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** PROCESS

Codex QA کافی نیست؛ ChatGPT Final Acceptance QA قبل از Monitoring الزامی است.

## SEO-010 — Systemic Changes Need Change Dossier
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** OPERATIONS

FAMILY/SITEWIDE change باید canary/regression/rollback plan داشته باشد، در صورت عملی بودن.

## SEO-011 — Framework v1.0 Freeze
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** PROCESS

بعد از این review ساختار framework فقط طبق Change Control تغییر می‌کند.

## SEO-012 — Final Content Requires ChatGPT Approval
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** CONTENT

Codex draft به‌تنهایی Production-ready نیست. Target content/facts باید در dossier/brief تأیید شده باشد.

## Template

```markdown
## SEO-XXX — Title
**Status:** Proposed | Accepted | Superseded
**Date:** YYYY-MM-DD
**Scope:** PAGE | FAMILY | SITEWIDE | PROCESS | DATA | OPERATIONS | CONTENT
**Supersedes:** optional

### Decision
### Evidence
### Consequences
### Exceptions
```


## SEO-013 — Google Official Documentation Governs SEO Recommendations
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** PROCESS / CONTENT / OPERATIONS

هر پیشنهاد فنی یا محتوایی SEO باید با مستندات رسمی فعلی Google Search سازگار باشد. توصیه vendor جای استاندارد Google را نمی‌گیرد.

## SEO-014 — Rank Math First SEO Ownership
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** OPERATIONS

هر concern SEO که نسخه نصب‌شده Rank Math واقعاً پشتیبانی می‌کند باید از همان مسیر مدیریت شود. Custom SEO PHP پراکنده و duplicate owner ممنوع است.

## SEO-015 — Master TODO Is the Execution Authority
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** PROCESS

`MASTER-TODO.md` مرجع ترتیب familyها و پوشش کامل سایت است. همه URL/entityهای inventory باید disposition نهایی داشته باشند.
