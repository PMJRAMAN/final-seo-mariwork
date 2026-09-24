# Final SEO Mariwork

این مخزن **Source of Truth** پروژه SEO ماری‌ورک است. هدف آن نگهداری گزارش نیست؛ هدف ایجاد یک سیستم پایدار برای تحقیق، تصمیم‌گیری، اجرا، QA و اندازه‌گیری تمام تغییرات SEO سایت است.

**Framework version: 1.0 — FROZEN BEFORE PAGE AUDITS**

## مدل اصلی پروژه

هیچ صفحه‌ای با یک audit یا یک پیشنهاد مستقیم وارد اجرا نمی‌شود.

مسیر استاندارد هر صفحه:

```text
DISCOVERED
→ BASELINED
→ CODEX_AUDITED
→ SECOND_REVIEWED
→ APPROVED
→ IMPLEMENTING
→ IMPLEMENTED
→ CODEX_QA_PASSED
→ FINAL_QA_PASSED
→ MONITORING
→ COMPLETE
```

اگر صفحه در هر مرحله blocker داشته باشد، `blocked: true` و دلیل آن در dossier ثبت می‌شود؛ وضعیت‌های اصلی حذف یا دور زده نمی‌شوند.

### دو Audit اجباری

1. **Codex Audit**  
   بر اساس task نوشته‌شده توسط ChatGPT، با دسترسی read-only به Production و بررسی HTML، WordPress/WooCommerce، schema، images، links، Search Console، URL history و کد مسئول خروجی.

2. **ChatGPT Second Review**  
   بررسی مستقل URL زنده و intent/SEO/content، سپس خواندن و challenge کردن گزارش Codex و reconcile کردن یافته‌ها.

Audit دوم خلاصه Audit اول نیست.

### دو QA پس از اجرا

1. **Codex Implementation QA** — بررسی فنی بلافاصله بعد از اجرا.
2. **ChatGPT Final Acceptance QA** — بررسی مستقل خروجی عمومی، محتوای نهایی و نتیجه تغییر قبل از ورود به Monitoring.

## قبل از auditهای صفحه

قبل از Batch 001 این سه پایه باید ساخته شوند:

1. **URL / Entity Inventory**
2. **Sitewide Technical Baseline**
3. **Search/Data Baseline**

صفحه‌محور بودن audit نباید باعث نادیده گرفتن مشکلات سیستماتیک crawl، indexation، facets، schema، templates یا internal linking شود.

## اسناد حاکم و ترتیب اولویت

در صورت تناقض:

1. [MANIFEST.md](MANIFEST.md)
2. [docs/DECISIONS.md](docs/DECISIONS.md) — آخرین Decision پذیرفته‌شده و مرتبط
3. [AGENTS.md](AGENTS.md) — محدودیت‌های عملیاتی Agent
4. [docs/CHANGE-CONTROL.md](docs/CHANGE-CONTROL.md)
5. [docs/WORKFLOW.md](docs/WORKFLOW.md)
6. Specها: Audit / Technical / Content / Data / QA / Measurement
7. [docs/SEO-PLAYBOOK.md](docs/SEO-PLAYBOOK.md)
8. Templateها و READMEهای پوشه‌ها

هیچ Decision نمی‌تواند Manifest را بدون تغییر رسمی Manifest نقض کند.

## ساختار مخزن

```text
.
├── README.md
├── MANIFEST.md
├── AGENTS.md
├── STATUS.md
├── docs/
├── templates/
├── registry/
├── audits/sitewide/
├── strategy/
├── changes/
├── pages/
├── batches/
├── data/
├── httpswww.mariwork.ir-Performance-on-Search-2026-09-24/
└── httpswww.mariwork.ir-Coverage-2026-09-24/
```

### نقش مسیرها

- `registry/` — URL inventory و findings سیستماتیک
- `audits/sitewide/` — baselineهای فنی سراسری
- `strategy/` — Query Map و Content Architecture
- `changes/` — پرونده تغییرات FAMILY/SITEWIDE
- `pages/` — dossier دائمی هر entity/page
- `batches/` — مدیریت batchها، نه منبع نهایی حقیقت
- `data/` — داده خام و derived آینده

## پرونده هر صفحه

برای entityهای WordPress/WooCommerce، شناسه پایدار در filename حفظ می‌شود:

```text
pages/products/product-12544-gray-122.md
```

تغییر slug یا URL پرونده جدید نمی‌سازد. URL قبلی در `legacy_urls` ثبت می‌شود.

## Findings

هر finding باید دارای موارد زیر باشد:

- ID یکتا
- severity: `P0/P1/P2/P3`
- scope: `PAGE/FAMILY/SITEWIDE`
- evidence class: `OBSERVED/MEASURED/INFERRED/HYPOTHESIS`
- confidence: `HIGH/MEDIUM/LOW`
- source/evidence
- impact
- recommendation
- acceptance criteria

یافته FAMILY/SITEWIDE باید در `registry/SYSTEMIC-FINDINGS.md` ثبت شود و در صورت اجرا، Change Dossier مستقل داشته باشد.

## اصول بنیادین

- داده و شواهد مقدم بر حدس است.
- واقعیت فعلی Production مقدم بر گزارش قدیمی است.
- مشکل سیستماتیک با تغییر دستی ده‌ها صفحه حل نمی‌شود.
- raw data ویرایش نمی‌شود.
- اطلاعات محصول یا review/rating/spec ساختگی ممنوع است.
- word count هدف SEO نیست.
- LLM optimization سیستم جدا از SEO نیست.
- تغییر URL بدون migration plan ممنوع است.
- تغییرات غیرمرتبط در یک implementation bundle مخلوط نمی‌شوند.
- هر تغییر باید قابل rollback و قابل اندازه‌گیری باشد.
- customer data، secrets و credentialها هرگز وارد این repo نمی‌شوند.

برای شروع هر کار ابتدا [STATUS.md](STATUS.md) خوانده شود.
