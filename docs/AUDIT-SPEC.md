# Audit Specification

این سند حداقل بررسی اجباری هر صفحه را تعریف می‌کند. نوع صفحه می‌تواند موارد اضافه داشته باشد.

## 1. Identity

- current URL
- WP/Post/Product ID
- page type
- family
- public status
- legacy URLs
- redirect chain
- canonical
- sitemap presence
- robots/indexability

## 2. Search / SERP Context

در Second Review با دقت بیشتر:

- primary intent
- secondary intents
- branded / non-branded
- transactional / informational / mixed
- SERP title/snippet observed where possible
- competing page types
- query cannibalization hypothesis
- mismatch between page purpose and queries

هیچ keyword صرفاً بر اساس حدس به صفحه تخصیص داده نمی‌شود.

## 3. Search Console

ثبت snapshot date و range اجباری است.

حداقل:
- clicks
- impressions
- CTR
- average position
- device pattern در صورت مرتبط بودن
- search appearance
- current and legacy URL rows

اگر Page+Query dataset وجود دارد:
- top relevant queries
- query intent groups
- CTR opportunity
- anomalous high-impression queries

اگر وجود ندارد، relation ساخته نمی‌شود.

## 4. Technical On-Page

- status code
- redirect
- canonical
- robots meta/header
- title
- meta description
- H1 count/content
- heading hierarchy
- lang/dir if relevant
- Open Graph
- duplicate boilerplate signals
- HTML availability without interaction
- JS/AJAX-dependent critical content

## 5. Content

### Usefulness
- آیا کاربر می‌فهمد این صفحه چیست؟
- آیا پاسخ تصمیم اصلی در بالای صفحه وجود دارد؟
- آیا متن فقط کلی/قابل‌جایگزینی با محصولات دیگر است؟
- چه Information Gain واقعی دارد؟
- چه اطلاعات ضروری کم است؟

### Accuracy
- تناقض short/long/meta/schema
- حجم/قیمت/کد/نام/کاربرد
- جملات ناقص یا قدیمی
- ادعاهای بدون منبع

### LLM Extractability
- entity واضح
- ویژگی‌ها نزدیک به entity
- پاسخ کوتاه مستقیم
- headingهای معنادار
- جدول/لیست ساختاریافته در صورت مفید بودن
- عدم دفن مشخصات حیاتی داخل UI صرفاً AJAX
- consistency across visible text and structured data

## 6. Product-specific

برای WooCommerce Product:

- product type
- variations
- variation IDs
- SKU uniqueness
- public price
- sale/conditional price
- currency/unit conversion
- stock status
- brand
- attributes
- variation URLs/preselection
- bundle contents
- dimensions/weight if visible/structured
- purchasing path

قیمت HTML، Woo data و schema باید مقایسه شوند.

## 7. Structured Data

- Product / ProductGroup / Offer / AggregateOffer
- Breadcrumb
- Organization relevance
- required/recommended fields
- visible-content consistency
- URL
- image
- SKU/brand
- variant relationship
- price/currency
- availability
- reviews/ratings
- shipping/returns where real

Rich Results eligibility و schema syntax دو موضوع متفاوت‌اند.

## 8. Images

- unique images
- main image relevance
- alt accuracy
- repeated/misleading alt
- file naming as secondary concern
- width/height
- responsive image
- lazy load
- likely LCP
- product evidence images
- examples on real material when relevant

ALT برای توصیف تصویر است، نه تکرار keyword.

## 9. Internal Linking

- breadcrumbs
- parent/category
- related products
- complementary pages
- academy/articles
- orphan risk
- reciprocal contextual opportunities
- old URL links

## 10. Template Similarity

برای خانواده‌های بزرگ:
- repeated headings
- repeated paragraphs
- repeated metadata patterns
- near-duplicate text
- truly product-specific sections

هدف حذف اجزای مشترک مفید نیست؛ هدف جدا کردن boilerplate از اطلاعات اختصاصی است.

## 11. Performance Signals

Audit HTML به‌تنهایی Core Web Vitals را اثبات نمی‌کند.

بررسی:
- obvious lazy-LCP risk
- excessive initial HTML
- blocking elements where measurable
- mobile-first QA

ادعای CWV فقط با داده مناسب.

## 12. Finding Quality

هر finding باید:
- observable evidence داشته باشد؛
- impact منطقی داشته باشد؛
- recommendation مشخص؛
- acceptance criteria آزمون‌پذیر.

### Severity

**P0** — خرابی/ریسک بحرانی مثل indexability اشتباه یا داده خرید بسیار خطرناک  
**P1** — خطای مهم و مستقیم  
**P2** — فرصت مهم برای بهبود  
**P3** — polish / low priority

### Scope

**PAGE** — فقط این entity  
**FAMILY** — چند صفحه هم‌نوع  
**SITEWIDE** — سیستم سایت

## 13. Audit Output

Audit نباید با score کلی مثل «SEO 82/100» جایگزین findings شود. هدف تشخیص و اقدام قابل سنجش است.
