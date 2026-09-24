# Data Sources & Evidence Rules

## 1. سلسله مراتب شواهد

برای وضعیت فعلی صفحه:

1. رفتار واقعی URL عمومی
2. HTML/structured data فعلی
3. WordPress/WooCommerce current data
4. server/code responsible for output
5. Search Console / Coverage snapshot
6. گزارش‌های قدیمی

گزارش قدیمی برای تاریخچه مهم است ولی وضعیت فعلی را override نمی‌کند.

## 2. Search Console Performance — snapshot فعلی

پوشه فعلی:

`httpswww.mariwork.ir-Performance-on-Search-2026-09-24/`

Metadata ثبت‌شده:
- Search type: Web
- Date: Last 16 months
- Export date: 2026-09-24

فایل‌های مهم:
- `Pages.csv`
- `Queries.csv`
- `Devices.csv`
- `Search appearance.csv`
- `Countries.csv`
- `Chart.csv`
- `Filters.csv`

### محدودیت حیاتی

`Pages.csv` و `Queries.csv` aggregationهای جدا هستند.

بنابراین:
- وجود query «رنگ موکا پارچه»
- و وجود URL محصول موکا

اثبات نمی‌کند تمام metrics آن query متعلق به همان page است.

برای این رابطه باید dataset دارای dimension/filter `page + query` یا export/API معادل تهیه شود.

## 3. Search Console Coverage / Indexing

پوشه فعلی:

`httpswww.mariwork.ir-Coverage-2026-09-24/`

این snapshot برای:
- وضعیت کلی indexing
- critical issues
- روند تاریخی

استفاده می‌شود.

Coverage snapshot جای URL Inspection زنده را نمی‌گیرد.

## 4. Raw vs Derived

داده خام:
- ویرایش نشود؛
- overwrite نشود؛
- normalize در همان فایل نشود.

داده derived باید جدا باشد و شامل:
- source snapshot
- transformation
- date
- assumptions

باشد.

## 5. URL History

GSC ممکن است URLهایی را نشان دهد که اکنون redirect شده‌اند.

در تحلیل:
- URL تاریخی حذف نمی‌شود؛
- metrics تاریخی به entity مربوطه نگاشت می‌شود؛
- current URL و legacy URL جدا ثبت می‌شوند؛
- redirect باید verify شود.

## 6. Date Context

هر metric بدون:
- بازه زمانی
- snapshot date
- dimension

ناقص است.

مقایسه قبل/بعد باید تا حد ممکن:
- بازه هم‌طول
- seasonality
- تغییر قیمت/موجودی
- migration
- campaign
- sitewide changes

را در نظر بگیرد.

## 7. Public Web / SERP

برای تحلیل intent، رقبا یا مستندات جاری، web research مجاز و در Second Review مطلوب است.

منابع ترجیحی برای استانداردها:
- Google Search Central
- Google Search Console documentation
- schema.org در صورت نیاز
- WooCommerce/WordPress/Rank Math official docs برای رفتار محصول

ادعاهای رقبا یا بلاگ‌ها جای مستندات رسمی را نمی‌گیرند.

## 8. Production Server

Server audit برای واقعیت فنی مفید است:
- WP data
- plugin behavior
- custom code
- output sources

اما write در audit ممنوع است.
