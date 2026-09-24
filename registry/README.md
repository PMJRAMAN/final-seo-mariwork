# Registry

مرجع مرکزی entityها و مشکلات مشترک.

## URL-INVENTORY.csv

یک row برای current entity/URL canonical target. legacy URLs می‌توانند در dossier یا derived URL map تفصیلی نگهداری شوند.

## SYSTEMIC-FINDINGS.md

فقط FAMILY/SITEWIDE findings.

Page findings داخل dossier می‌مانند.

## ID Rules

- Page finding: `{entity_id}-F001`
- Systemic finding: `SYS-001`
- Change dossier: `CHG-001`
- Decision: `SEO-001`
- Playbook: `PLAY-001`


## Final disposition

برای هر entity/content URL در inventory باید در پایان یکی از این مقادیر ثبت شود:

`OPTIMIZE`, `KEEP_AS_IS`, `REDIRECT`, `NOINDEX`, `CANONICALIZE`, `REMOVE_410`, `BLOCKED_NEEDS_DECISION`.

`NOT_DECIDED` فقط در طول پروژه مجاز است.

برای URL spaceهای ماشینی/نامحدود مثل ترکیب‌های faceted، یک policy FAMILY/SITEWIDE می‌تواند به‌جای dossier جدا برای تک‌تک ترکیب‌ها استفاده شود؛ اما تمام URL space باید تحت آن policy پوشش داده شود.
