# SEO Technical Ownership — Rank Math First

**Status:** ACCEPTED  
**Applies from:** 2026-09-24

## 1. اصل مالکیت

در ماری‌ورک، Rank Math نسخه نصب‌شده **مالک فنی پیش‌فرض SEO در WordPress** است.

هر قابلیت SEO که نسخه نصب‌شده Rank Math واقعاً پشتیبانی می‌کند باید از Rank Math مدیریت شود، نه از:
- snippet پراکنده در theme/functions.php
- فایل PHP مستقل بی‌مالک
- hook ناشناس در افزونه دیگر
- meta/schema/canonical duplicate
- راهکار موقت بدون مسیر نگهداری

این اصل شامل مواردی است که Rank Math برای آن‌ها capability فعال و مناسب دارد، از جمله بر اساس نسخه/ماژول نصب‌شده:
- SEO title و meta description
- robots meta / advanced robots
- canonical
- XML sitemap settings
- product/category/tag SEO controls
- Product schema و WooCommerce integration در محدوده قابلیت موجود
- redirections / 404 monitoring اگر ماژول در نسخه نصب‌شده موجود و برای use case مناسب باشد
- robots.txt editor اگر معماری واقعی سایت اجازه استفاده از آن را بدهد
- سایر قابلیت‌های SEO که قبل از اجرا در Rank Math فعلی verify می‌شوند

مستندات رسمی Rank Math فقط **نحوه پیاده‌سازی** را توضیح می‌دهند؛ دلیل تصمیم SEO باید از مستندات رسمی Google، داده سایت و معماری پروژه بیاید.

## 2. Ownership Classes

هر implementation SEO باید یکی از این ownerها را ثبت کند:

### RANK_MATH
قابلیت به‌طور مستقیم از UI/config/meta Rank Math قابل اعمال است.

نمونه:
- title/meta
- robots
- canonical
- sitemap inclusion
- supported schema settings

### RANK_MATH_EXTENSION
نیاز SEO واقعی است ولی Rank Math UI/config فعلی به‌تنهایی کافی نیست.

در این حالت:
- قبل از کدنویسی capability نسخه نصب‌شده verify شود؛
- extension باید به Rank Math متصل و با ownership روشن باشد؛
- کد پراکنده ممنوع است؛
- محل نهایی فقط یک integration مرکزی و مستند است؛
- duplicate output با Rank Math ممنوع است؛
- hook/filter رسمی Rank Math در صورت وجود ترجیح دارد.

محل دقیق integration بعد از بررسی معماری Mariwork Core تعیین و در Change Dossier ثبت می‌شود. ایجاد فایل PHP مستقل تصادفی مجاز نیست.

### PLATFORM
فقط برای مواردی که ذاتاً خارج از مالکیت Rank Math هستند و Rank Math capability مناسب ندارد؛ مثل برخی server/WAF/performance/HTTP controls.

استفاده از PLATFORM برای دور زدن قابلیت Rank Math ممنوع است. دلیل عدم استفاده از Rank Math باید در task ثبت شود.

### CONTENT
متن visible، تصاویر، نمونه‌های واقعی و سایر محتوای editorial. metadata مرتبط همچنان اگر Rank Math آن را مدیریت می‌کند، owner = RANK_MATH است.

## 3. Capability Check قبل از پیشنهاد فنی

قبل از هر recommendation/implementation:

1. نسخه و ماژول‌های فعال Rank Math را verify کن.
2. مستندات رسمی Rank Math را برای capability فعلی بررسی کن.
3. current owner خروجی را پیدا کن.
4. duplicate owner را شناسایی کن.
5. target owner را ثبت کن.
6. اگر owner از Rank Math خارج می‌شود، دلیل فنی صریح لازم است.

## 4. Single Source of SEO Output

برای هر concern باید یک owner فعال داشته باشیم.

مثال:
- canonical → یک owner
- Product schema → یک owner/یک pipeline
- meta robots → یک owner
- title/meta → یک owner
- sitemap policy → یک owner

Rank Math و custom code نباید بدون طراحی صریح خروجی موازی/متناقض بسازند.

## 5. Google Basis اجباری

هر تغییر SEO فنی یا محتوایی باید یک Google basis داشته باشد:

- `GOOGLE_REQUIRED` — الزام روشن مستندات Google
- `GOOGLE_RECOMMENDED` — توصیه روشن Google
- `GOOGLE_CONSISTENT` — با اصول Google سازگار است ولی الزام مشخصی برای همین جزئیات وجود ندارد
- `PROJECT_DECISION` — تصمیم معماری/محتوایی پروژه؛ نباید به Google نسبت داده شود
- `EXPERIMENT` — فرضیه قابل اندازه‌گیری

هرجا applicable است، URL مرجع رسمی Google در finding/decision/task ثبت شود.

اگر مستند رسمی Google برای ادعایی وجود ندارد، Codex یا ChatGPT نباید آن را «قانون Google» بنامند.

## 6. Rank Math Configuration Audit

Sitewide baseline باید ثبت کند:
- نسخه نصب‌شده Rank Math
- Free/Pro status
- Advanced mode status
- modules enabled
- Titles & Meta settings
- Products/Product Categories/Product Tags settings
- sitemap settings
- canonical/robots ownership
- Schema module/WooCommerce behavior
- 404/Redirection modules
- robots.txt ownership
- custom Rank Math filters/hooks
- سایر کدهایی که title/meta/schema/canonical/robots/sitemap را دستکاری می‌کنند
- conflicts/duplicate output

## 7. Change Control

تغییر ownership یک concern SEO، تغییر معماری محسوب می‌شود و باید:
- finding
- owner_before
- owner_after
- reason
- rollback
- regression set

داشته باشد.

## Official implementation references

مراجع رسمی Rank Math در `docs/REFERENCES.md` نگهداری می‌شوند و قبل از implementation حساس باید دوباره بررسی شوند.
