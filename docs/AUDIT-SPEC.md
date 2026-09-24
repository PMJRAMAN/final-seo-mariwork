# Page Audit Specification v1.0

این سند minimum contract برای audit هر page است. Sitewide audit سند جدا دارد.

## 1. Identity / State

- framework_version
- dossier_schema_version
- entity ID
- WP ID
- type/family
- current URL
- canonical
- legacy URLs
- HTTP/redirect
- sitemap
- intended indexability
- actual indexability signals

## 2. Search & Intent

- primary intent
- secondary intent
- branded/non-branded
- transactional/informational/mixed
- current SERP page types در Second Review
- query/page mismatch
- cannibalization hypothesis
- target entity relationship در Query Map

Query اختصاصی بدون evidence به صفحه تحمیل نمی‌شود.

## 3. Search Console

همیشه:
- source snapshot
- date range
- dimension
- current vs legacy URL

حداقل metrics در صورت وجود:
- clicks
- impressions
- CTR
- position
- device
- search appearance

Page+Query:
- YES / NO
- اگر NO: query-to-page attribution ممنوع

## 4. Crawl / Index / Canonical

- status
- redirect chain
- canonical
- robots meta
- X-Robots
- robots.txt accessibility
- sitemap membership
- canonical consistency
- accidental parameter/duplicate URL

robots.txt = crawl control، نه ابزار قابل‌اتکا برای noindex.

## 5. Metadata / HTML Semantics

- title
- meta description
- H1 count/content
- heading structure
- lang/dir where relevant
- OG/social
- snippet-sensitive visible content
- duplicate boilerplate pattern

## 6. Content Accessibility

- critical content in initial HTML
- AJAX/JS-only content
- crawlable links
- hidden/interaction-gated critical facts
- mobile-visible parity
- content loaded only after click/scroll

## 7. Content Quality

### Accuracy
- name/code/volume/price/application
- short vs long vs schema consistency
- outdated statements
- incomplete sentences
- unsupported claims

### Usefulness
- clear first-screen answer
- purchase/learning decision support
- Information Gain
- limitations/tradeoffs where relevant
- verified evidence/examples

### Similarity
- repeated headings
- repeated paragraphs
- family boilerplate
- truly unique sections

### LLM Extractability
- explicit entity
- factual attributes near entity
- concise answer blocks
- meaningful tables/lists
- no important fact trapped only in interaction UI
- visible/schema consistency

## 8. Product / WooCommerce

در product:
- product type
- variations/variation IDs
- SKU uniqueness
- attributes
- price/public price/sale conditions
- stock
- brand
- variation selection URLs
- bundle contents
- dimensions/weight only if real
- purchasing path

HTML/Woo/schema comparison اجباری برای price/availability در صفحه‌های مهم.

## 9. Structured Data

- Product / ProductGroup / Offer / AggregateOffer
- Breadcrumb
- Organization where relevant
- identifiers
- variants
- price/currency
- availability
- image
- genuine ratings/reviews
- shipping/returns only when real
- initial HTML where relevant to fast-changing product data
- Rich Results Test/URL Inspection when available in QA, not assumed from syntax alone

## 10. Images

- main image relevance
- unique images
- correct ALT
- repeated/wrong volume ALT
- dimensions/srcset
- lazy loading
- likely LCP
- product evidence/sample imagery
- file discoverability

ALT describes image; it is not a keyword field.

## 11. Internal Linking

- breadcrumb
- parent/category
- complementary products
- product ↔ education links
- related content
- orphan risk
- crawlable `<a href>`
- legacy internal URLs
- anchor relevance

## 12. Page Experience / Performance

تفکیک:
- field data
- lab data
- HTML observation

بررسی:
- Core Web Vitals data if available
- likely LCP image lazy issue
- mobile rendering
- intrusive UI/interstitials
- excessive layout shift causes when measurable

یک lab score به‌تنهایی verdict SEO نیست.

## 13. Trust / Evidence

بدون ساخت score مصنوعی:
- manufacturer/source clarity
- real product examples
- reviewer/editor identity where relevant
- update dates only if real
- first-hand evidence

E-E-A-T به‌عنوان «امتیاز عددی داخلی» استفاده نشود.

## 14. Finding Contract

هر finding:
- unique ID
- evidence class
- confidence
- severity
- scope
- source refs
- impact
- recommendation
- acceptance criteria

Audit با score کلی جایگزین findings نمی‌شود.
