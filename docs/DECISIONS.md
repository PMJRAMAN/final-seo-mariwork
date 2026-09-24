# SEO Decision Log

این فایل تصمیم‌های رسمی معماری/فرآیند SEO را ثبت می‌کند.

---

## SEO-001 — Dual Audit Mandatory

**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** SITEWIDE / PROCESS

هر صفحه قبل از APPROVED شدن باید Codex Audit و سپس ChatGPT Second Review مستقل داشته باشد.

---

## SEO-002 — Repository as Source of Truth

**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** PROCESS

`PMJRAMAN/final-seo-mariwork` مرجع اصلی پرونده‌ها، تصمیم‌ها، findings و تاریخچه پروژه SEO است.

---

## SEO-003 — Raw Search Data Is Immutable

**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** DATA

CSVهای export خام ویرایش نمی‌شوند. هر پردازش در derived output یا پرونده تحلیلی جدا ثبت می‌شود.

---

## SEO-004 — Page/Query Attribution Requires Joined Evidence

**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** DATA

Query مستقل Search Console به URL خاص نسبت داده نمی‌شود مگر dataset یا filter دارای رابطه Page+Query باشد.

---

## SEO-005 — Findings Require Scope

**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** PROCESS

هر finding باید PAGE، FAMILY یا SITEWIDE باشد. مشکلات تکراری باید تا حد امکان سیستماتیک حل شوند.

---

## SEO-006 — Audit Is Read-Only on Production

**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** OPERATIONS

Codex در task audit روی Production write انجام نمی‌دهد. اجرا نیازمند APPROVED dossier و Implementation Task است.

---

## SEO-007 — Stable Entity ID Over Slug

**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** REPOSITORY

برای صفحات دارای WordPress/Product ID، نام پرونده باید ID پایدار را نگه دارد. تغییر slug/URL در همان پرونده ثبت می‌شود.

---

## قالب تصمیم جدید

```markdown
## SEO-XXX — Title

**Status:** Proposed | Accepted | Superseded
**Date:** YYYY-MM-DD
**Scope:** PAGE | FAMILY | SITEWIDE | PROCESS | DATA | OPERATIONS
**Supersedes:** optional

### Decision

### Evidence

### Consequences

### Exceptions
```
