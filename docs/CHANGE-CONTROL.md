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
