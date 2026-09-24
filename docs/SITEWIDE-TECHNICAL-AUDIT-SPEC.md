# Sitewide Technical Audit Specification v1.0

این audit قبل از page batches انجام می‌شود و read-only است.

## A. Crawl & Index Controls

- robots.txt syntax/intent
- meta robots
- X-Robots-Tag
- noindex pages
- blocked-but-indexable risk
- HTTP/HTTPS/www normalization
- 3xx chains/loops
- 4xx/5xx
- soft-404 patterns
- canonical consistency

## B. Sitemaps

- sitemap index
- included URL types
- only intended canonical/indexable URLs
- stale/redirected/404 URLs
- unexpected count differences
- lastmod quality where used

## C. URL Spaces

Inventory:
- canonical pages
- product variants
- category/tag/attribute
- pagination
- search
- filter/faceted parameters
- sort/order parameters
- feeds
- attachments
- cart/checkout/account
- API/system URLs if publicly crawlable

هدف: تشخیص crawl traps، duplicate spaces و indexability intent.

## D. Faceted Navigation

برای هر facet:
- parameter pattern
- crawlable links
- canonical
- robots behavior
- index/noindex
- sitemap presence
- internal linking
- combinations/infinite space

هیچ سیاست facets قبل از دیدن data/architecture نهایی نمی‌شود.

## E. Canonical / Duplicate Architecture

- trailing slash
- www/non-www
- http/https
- parameters
- variant URLs
- archive duplicates
- legacy slugs
- content duplication
- canonical target status

## F. Internal Link Graph

- crawlable `<a href>`
- orphan pages
- click depth
- important page link coverage
- breadcrumb patterns
- product ↔ academy/articles
- legacy links
- nav/footer overlinking

## G. JavaScript / AJAX

- critical content in initial HTML
- AJAX-only bundle contents
- JS-only links
- lazy-loaded content
- rendered DOM where available
- variant selection/canonical behavior

Google rendering capability وجود دارد، اما critical content نباید بی‌دلیل به interaction وابسته باشد.

## H. Structured Data System

Sitewide generators/plugins/custom filters:
- Organization/OnlineStore
- Product/ProductGroup/Offer
- Breadcrumb
- Article where relevant
- duplication/conflicts among plugins
- price/currency source
- brand/SKU source
- reviews
- shipping/returns

خروجی visible و schema باید سازگار باشند.

## I. WooCommerce / Product Architecture

- product types
- variations
- parent/child URL policy
- bundles
- archives
- attribute pages
- duplicate SKU/identifier patterns
- price filters/hooks
- conditional discounts affecting public markup

## J. Images / Media

- image crawlability
- hero lazy patterns
- srcset/dimensions
- ALT template issues
- attachment pages
- image sitemap if relevant

## K. Performance / Page Experience

تفکیک field/lab:
- Search Console CWV if available
- PageSpeed/Lighthouse sample
- LCP/INP/CLS representative templates
- mobile usability/output
- intrusive overlays
- caching behavior

## L. Security / Access Relevant to Search

- HTTPS
- WAF/CDN blocks to search crawlers if evidence available
- accidental auth
- bot access logs where useful
- Googlebot access where relevant
- اگر هدف حضور در ChatGPT Search است: OAI-SearchBot robots/access/IP behavior جداگانه بررسی شود
- GPTBot (training control) با OAI-SearchBot (Search) یکی فرض نشود
- ChatGPT-User نیز crawler خودکار Search محسوب نشود

این بخش security audit کامل سرور نیست و سیاست training نباید به‌اشتباه به‌عنوان سیاست Search گزارش شود.

## M. Output

1. `audits/sitewide/...` report
2. systemic findings registry
3. URL inventory updates
4. recommended investigation order
5. no Production changes


## N. Rank Math Configuration & SEO Ownership Audit

ثبت اجباری قبل از page implementations:

- installed Rank Math version
- Free/Pro
- Advanced Mode
- active modules
- Titles & Meta settings
- Products/Product Categories/Product Tags settings
- sitemap ownership/settings
- robots meta/canonical ownership
- Schema/WooCommerce integration
- 404/Redirections modules
- robots.txt ownership
- custom `rank_math/*` hooks/filters
- theme/custom-plugin hooks affecting SEO output
- duplicate title/meta/canonical/schema/robots/sitemap sources
- owner_before و recommended owner_after

هر recommendation این بخش باید:
- Google basis/reference
- Rank Math capability check
- owner target

داشته باشد.
