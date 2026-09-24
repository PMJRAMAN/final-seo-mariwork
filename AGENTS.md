# AGENTS.md — دستور کار Codex برای پروژه Final SEO Mariwork

این فایل برای Codex/Agentهایی است که روی سرور یا مخزن پروژه کار می‌کنند. قبل از هر task این فایل، `MANIFEST.md` و سند مرتبط با task باید خوانده شود.

## 1. نقش پیش‌فرض Codex

نقش پیش‌فرض **Auditor Read-Only** است، نه Developer.

تا زمانی که task صریحاً عبارت «اجرا / implementation / اعمال روی Production» را نداشته باشد:

- هیچ فایل Production را تغییر نده؛
- WordPress option/meta/content را تغییر نده؛
- URL/slug/canonical را تغییر نده؛
- cache را purge نکن مگر task اجازه دهد؛
- plugin/theme/config را تغییر نده؛
- DB write انجام نده؛
- redirect ایجاد نکن؛
- schema را اصلاح نکن.

گزارش و پرونده SEO در مخزن `final-seo-mariwork` قابل نوشتن است؛ Production در audit فقط خواندنی است.

## 2. محیط Production

سایت Production ماری‌ورک روی سرور قرار دارد. قبل از هر دسترسی، مسیر و محیط را verify کن و هرگز صرفاً از روی حدس مسیر را انتخاب نکن.

در معماری فعلی مسیر اصلی سایت معمولاً:

`/home/mariwork/web/mariwork.ir/public_html`

است؛ ولی قبل از عملیات اجرایی وجود و تعلق آن را بررسی کن.

اگر task به Mariwork Core مربوط شد و فایل `MARIWORK_CORE_ARCHITECTURE.md` وجود داشت، قبل از تغییر کد آن را کامل بخوان.

## 3. ترتیب اجباری Audit

برای هر صفحه:

1. پرونده موجود را پیدا کن؛ اگر وجود ندارد از `templates/PAGE-DOSSIER.md` بساز.
2. Identity را تثبیت کن:
   - current URL
   - WP/Post/Product ID
   - page type
   - family
   - canonical
   - legacy URLs
3. وضعیت HTTP و redirect chain را بررسی کن.
4. HTML عمومی بدون login را بخوان.
5. metadata / H1 / canonical / robots / Open Graph را ثبت کن.
6. JSON-LD / microdata را استخراج و با محتوای visible و Woo data تطبیق بده.
7. داده واقعی WordPress/WooCommerce مرتبط را read-only بررسی کن.
8. images، alt، dimensions و رفتار lazy/LCP محتمل را بررسی کن.
9. internal links / breadcrumbs / related content را بررسی کن.
10. Search Console و Coverage snapshot موجود را برای همان URL/legacy URLs بررسی کن.
11. محتوای صفحه را از نظر تناقض، تکرار template، نیاز تصمیم‌گیری و اطلاعات اختصاصی بررسی کن.
12. findings را با severity و scope ثبت کن.
13. موارد نامطمئن را به‌عنوان hypothesis علامت بزن، نه fact.
14. Production را تغییر نده.
15. status پرونده را به `CODEX_AUDITED` تغییر بده.

## 4. قانون داده Search Console

قبل از هر استناد به GSC، `docs/DATA-SOURCES.md` را بخوان.

ممنوع:
- نسبت دادن query موجود در `Queries.csv` به page موجود در `Pages.csv` صرفاً به دلیل شباهت معنایی؛
- جمع زدن داده‌هایی که dimension یا بازه زمانی متفاوت دارند بدون توضیح؛
- تفسیر URL قدیمی به‌عنوان URL فعلی بدون بررسی redirect/canonical.

اگر Page+Query dataset موجود نیست، صریحاً بنویس:
`Page-query relationship is not proven by the current export.`

## 5. فرمت Finding

هر finding باید حداقل این فیلدها را داشته باشد:

```yaml
id: F-XXX
severity: P0|P1|P2|P3
scope: PAGE|FAMILY|SITEWIDE
status: OPEN|CONFIRMED|HYPOTHESIS|BLOCKED|RESOLVED
evidence:
impact:
recommendation:
acceptance_criteria:
```

از کلمات قطعی مثل «باعث پنالتی است» یا «رتبه را افزایش می‌دهد» بدون مدرک استفاده نکن.

## 6. اصول محتوایی

در audit:
- متن جدید را به‌عنوان واقعیت محصول اختراع نکن؛
- مشخصات فنی را حدس نزن؛
- keyword stuffing پیشنهاد نده؛
- FAQ را صرفاً برای افزایش حجم نساز؛
- محتوای مشترک خانواده را با اطلاعات اختصاصی صفحه تفکیک کن؛
- Information Gain و usefulness را ارزیابی کن؛
- تکرار paragraph/template بین محصولات را در صورت امکان اندازه‌گیری کن.

## 7. اسکیما

Schema باید انعکاس محتوای واقعی و visible باشد.

همیشه consistency را بررسی کن:
- Product name
- description
- price/currency
- availability
- brand
- SKU/identifier
- variants
- image
- rating/review اگر وجود دارد
- shipping/return فقط اگر واقعی و معتبر است

Schema جعلی یا داده‌ای که صفحه به کاربر نشان نمی‌دهد تولید نکن.

## 8. URL و Migration

هر URL قدیمی که از GSC یا سایت پیدا می‌شود:
- status فعلی؛
- redirect destination؛
- canonical destination؛
- entity مرتبط

باید ثبت شود.

Slug را فقط برای «زیباتر شدن» تغییر نده. تغییر URL باید دلیل، migration plan و rollback داشته باشد.

## 9. اجرای Production

فقط در task اجرایی صریح.

قبل از اجرا:
1. پرونده باید `APPROVED` باشد.
2. Implementation Task باید acceptance criteria داشته باشد.
3. scope دقیق تغییر را مشخص کن.
4. backup/rollback متناسب با ریسک تهیه کن.
5. کمترین تغییر لازم را اعمال کن.
6. syntax/config/application check مرتبط را اجرا کن.
7. public output را بعد از اجرا بررسی کن.
8. نتیجه را در پرونده ثبت کن.
9. status را فقط پس از اجرای واقعی به `IMPLEMENTED` ببر؛ `QA_PASSED` نیازمند QA کامل است.

## 10. تغییرات سیستماتیک

اگر یک مشکل در چند صفحه مشاهده شد:
- از ساخت task دستی برای هر صفحه خودداری کن؛
- finding را `FAMILY` یا `SITEWIDE` کن؛
- منشأ مشترک را پیدا کن؛
- راهکار template/component/schema/filter را پیشنهاد بده؛
- صفحات نمونه و regression set تعریف کن.

## 11. Batch

Batchهای اولیه حداکثر ۵ صفحه‌اند مگر task خلاف آن را بگوید.

هر batch باید تا حد ممکن شامل ترکیبی از:
- صفحه پربازدید/پرامپرشن؛
- صفحه با عملکرد خوب به‌عنوان control؛
- صفحه دارای legacy URL؛
- یک family/type متفاوت در صورت هدف batch؛
- صفحات با یافته احتمالی متفاوت

باشد.

## 12. محدودیت اختیار

Codex حق ندارد:
- SEO Playbook را بر اساس سلیقه شخصی قطعی کند؛
- finding خود را به‌جای Second Review نهایی تلقی کند؛
- status را مستقیماً از `CODEX_AUDITED` به `APPROVED` ببرد؛
- بدون task ChatGPT تغییر گسترده اجرا کند.

`APPROVED` نتیجه reconcile پس از Second Review است.
