# Framework Change Control

**Current framework: v1.0 — FROZEN**

هدف این سند جلوگیری از تغییر مداوم ساختار وسط پروژه است.

## 1. بعد از Freeze

تغییرات framework فقط وقتی مجاز است که:
- خطای واقعی workflow پیدا شود؛
- نیاز مهم جدید قابل پوشش با ساختار فعلی نباشد؛
- requirement خارجی مهم تغییر کند.

سلیقه یا «مرتب‌تر شدن» دلیل کافی نیست.

## 2. Required Process

برای تغییر ساختاری:
1. Decision جدید در `docs/DECISIONS.md`
2. reason/evidence
3. affected files/templates
4. backward compatibility impact
5. migration instruction برای dossierهای قدیمی
6. framework version bump اگر breaking

## 3. Compatible Changes

بدون major redesign:
- افزودن optional field
- توضیح دقیق‌تر rule
- reference update
- template guidance تکمیلی

## 4. Breaking Changes

نیازمند version bump:
- حذف/تغییر status lifecycle
- تغییر معنی finding fields
- تغییر dossier identity model
- تغییر audit gates
- تغییر authority model

## 5. Dossier Versioning

هر dossier:
- `framework_version`
- `dossier_schema_version`

دارد.

پرونده قدیمی صرفاً برای cosmetic update migrate نمی‌شود.


## 6. Concurrent Changes

برای جلوگیری از attribution و regression مبهم:
- روی یک family/subsystem هم‌زمان چند systemic implementation مستقل اجرا نشود مگر coordination صریح وجود داشته باشد.
- هر active systemic change باید ID و status داشته باشد.
- implementation جدید باید active changes همان family/template/plugin را بررسی کند.
- تغییرهای unrelated که measurement یکدیگر را مخدوش می‌کنند تا حد امکان جدا شوند.


## 7. Compatible Extension — 2026-09-25 Decision-to-Execution Gate

**Decision:** SEO-019  
**Type:** Backwards-compatible workflow clarification  
**Framework version:** remains v1.0

Reason:
- the full-site audit and Second Review exposed many cross-family target-state choices that should be discussed before Production execution;
- existing M-02/M-15/M-17 already require approved target state/content before write, but the repository did not have a dedicated decision queue distinct from the execution queue.

Affected files:
- `docs/DECISION-TO-EXECUTION-GOVERNANCE.md`
- `strategy/DECISION-BACKLOG.md`
- `tasks/EXECUTION-BACKLOG.md`
- `docs/DECISIONS.md`
- `MANIFEST.md`
- `AGENTS.md`
- `MASTER-TODO.md`
- strategy/tasks README files
- `STATUS.md`

Backward compatibility:
- no lifecycle status is removed or redefined;
- no dossier identity/schema change;
- no authority transfer;
- no existing approved implementation is invalidated;
- old dossiers do not require migration.

The extension clarifies that complete-site coverage, target-state decisions and executable implementation work are separate artifacts.
