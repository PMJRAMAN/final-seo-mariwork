# MASTER TODO — Final SEO Mariwork

**Role:** مرجع اصلی ترتیب اجرا و پوشش کامل پروژه  
**Framework:** v1.0  
**Current program:** STORE-FIRST  
**Rule:** هیچ URL/entity کشف‌شده نباید بدون disposition نهایی باقی بماند.

## 0. Coverage Contract

هر URL/entity در inventory باید در پایان یکی از این dispositionها را داشته باشد:

- `OPTIMIZE` — صفحه باید بهینه‌سازی و نگهداری شود
- `KEEP_AS_IS` — بررسی شده و تغییر لازم ندارد
- `REDIRECT` — URL باید با migration plan ادغام شود
- `NOINDEX` — وجود برای کاربر/سیستم لازم است ولی نباید در Search index هدف باشد
- `CANONICALIZE` — نسخه duplicate/alternate با canonical policy روشن
- `REMOVE_410` — فقط با دلیل مستند و approval
- `BLOCKED_NEEDS_DECISION` — موقت؛ قبل از پایان پروژه باید حل شود

«بررسی همه صفحات» به معنی «افزودن متن به همه صفحات» نیست؛ به معنی تصمیم SEO مستند برای همه URL spaces است.

---

# A. FOUNDATION / PRE-AUDIT

- [x] A-001 Framework v1.0
- [x] A-002 Dual Audit workflow
- [x] A-003 Page Dossier schema
- [x] A-004 Systemic findings/change dossiers
- [x] A-005 QA + monitoring framework
- [x] A-006 Framework change control
- [x] A-007 Google official-reference rule
- [x] A-008 Rank Math-first SEO ownership rule
- [ ] A-009 Autonomous Round-1 Audit Orchestration — deploy/verify runner; no Production writes
- [x] A-010 Build complete URL/Entity Inventory
- [ ] A-011 Map all current page types / taxonomies / custom post types
- [ ] A-012 Map legacy URLs from Search Console and redirects
- [ ] A-013 Sitewide Technical SEO Baseline
- [ ] A-014 Rank Math Configuration & Ownership Audit
- [ ] A-015 Detect duplicate SEO owners/output
- [ ] A-016 Normalize Search Console baseline
- [ ] A-017 Obtain/derive Page+Query data where possible
- [ ] A-018 Build initial Query/Intent Map
- [ ] A-019 Build initial Content Architecture
- [ ] A-020 Create first Systemic Findings registry
- [ ] A-021 Freeze Batch 001 selection

**Gate:** Store page audits شروع نمی‌شوند تا A-010 تا A-020 کامل یا blocker آن‌ها صریحاً ثبت شده باشد.

---

# B. STORE / WOOCOMMERCE — FIRST MAJOR PROGRAM

تمام URLهای فروشگاه باید پوشش داده شوند.

## B0 — Store architecture / non-page spaces

- [ ] B0-001 Shop archive audit
- [ ] B0-002 Product sitemap policy
- [ ] B0-003 Product category inventory
- [ ] B0-004 Product tag inventory
- [ ] B0-005 Product attribute archive inventory
- [ ] B0-006 Filter/faceted URL inventory
- [ ] B0-007 Sort/query parameter URL inventory
- [ ] B0-008 Pagination behavior
- [ ] B0-009 Product search URLs
- [ ] B0-010 Variant URL architecture
- [ ] B0-011 Bundle/set architecture
- [ ] B0-012 Legacy product URL mapping
- [ ] B0-013 Store internal-link baseline
- [ ] B0-014 Store schema ownership baseline
- [ ] B0-015 Store Rank Math settings baseline

## B1 — Product pilot

اول ۵ صفحه representative:
- [ ] B1-001 انتخاب Pilot Batch 001 بر اساس GSC + family diversity
- [ ] B1-002 Codex Audit همه ۵ صفحه
- [ ] B1-003 ChatGPT Second Review همه ۵ صفحه
- [ ] B1-004 استخراج FAMILY/SITEWIDE findings
- [ ] B1-005 Content/Title/Meta/Schema/ALT rules candidates
- [ ] B1-006 Systemic fixes before mass page edits
- [ ] B1-007 Canary implementation
- [ ] B1-008 Codex QA
- [ ] B1-009 ChatGPT Final QA

## B2 — All fabric-color products

Inventory exact URL list از `registry/URL-INVENTORY.csv` تولید شود.

برای **هر محصول**:
- [ ] baseline
- [ ] Codex Audit
- [ ] ChatGPT Second Review
- [ ] final findings
- [ ] target title/meta/H1
- [ ] content decision/rewrite where needed
- [ ] image/ALT decision
- [ ] internal linking
- [ ] schema/variant decision
- [ ] implementation
- [ ] Codex QA
- [ ] ChatGPT Final QA
- [ ] monitoring/disposition

Batchها ابتدا ۵تایی و پس از ثبات process حداکثر طبق تصمیم پروژه افزایش می‌یابند.

## B3 — Sets / Bundles

همه ست‌ها:
- 5/6/12/40-color sets و هر bundle کشف‌شده در inventory
- [ ] audit قیمت visible vs Woo vs schema
- [ ] محتویات bundle در HTML
- [ ] حجم/تعداد/تمایز عنوان
- [ ] cross-link between size variants
- [ ] Product/Offer/schema architecture
- [ ] همه dossiers dual-audited + optimized/kept

## B4 — Mediums

تمام مدیوم‌ها و محصولات کمکی:
- fixative
- basecoat
- texture
- puffy/other mediums
- glue/glitter-related
- هر medium دیگر در inventory

برای همه، dual audit + implementation + QA.

## B5 — Tools / Accessories

تمام ابزارها:
- heat pen
- nozzles
- totakali items
- سایر ابزارهای inventory

برای همه، dual audit + disposition.

## B6 — Other products

هر Product منتشرشده که در B2-B5 نیست:
- [ ] assign family
- [ ] dual audit
- [ ] optimize/keep/redirect/noindex decision
- [ ] QA

**Store completion invariant:** تعداد product entities در inventory = تعداد product dossiers با disposition نهایی.

## B7 — Product categories

برای **تمام Product Category URLها**:
- [ ] intent/indexability decision
- [ ] GSC data
- [ ] title/meta/H1
- [ ] unique useful intro/content where justified
- [ ] internal links
- [ ] sitemap
- [ ] canonical
- [ ] Rank Math ownership
- [ ] dual audit
- [ ] implementation/QA if indexable

## B8 — Product tags decommission / attribute archives audit

**Project direction:** Product Tags برای معماری نهایی فروشگاه نیاز نیستند و هدف، حذف کنترل‌شده آن‌هاست. حذف مستقیم بدون تحلیل URL history، GSC، indexation، internal links و migration mapping مجاز نیست. Product Attributes مستقل از Tags هستند و صرفاً به‌دلیل این تصمیم حذف نمی‌شوند.

### Product Tags — planned decommission
- [ ] B8-001 Inventory all Product Tags, tag assignments and public tag archive URLs
- [ ] B8-002 Analyze GSC/history, indexation, sitemap presence, internal links and any known inbound-link/value signals
- [ ] B8-003 Map every tag URL to the best replacement: relevant Product Category / Shop / specific durable destination; use `REMOVE_410` only when no meaningful replacement exists and evidence supports it
- [ ] B8-004 Prepare migration plan before deletion: redirects/410, internal-link cleanup, tag-assignment cleanup and rollback/verification scope
- [ ] B8-005 Remove Product Tag usage/archive exposure only after approval; clean Rank Math sitemap/indexability ownership accordingly
- [ ] B8-006 Implement approved 301/410 mapping without redirect chains or unrelated URL changes
- [ ] B8-007 Crawl + sitemap + canonical + internal-link + GSC follow-up QA after decommission

### Product Attributes — separate decision
- [ ] B8-008 Audit attribute archives independently for KEEP INDEXED / NOINDEX / REDIRECT / CANONICALIZE
- [ ] B8-009 Verify Rank Math robots/sitemap ownership and internal-link policy for attributes
- [ ] B8-010 Attribute archive QA

## B9 — Store facets / filters / parameters

- [ ] enumerate URL combinations
- [ ] determine crawl/index policy
- [ ] canonical/robots/internal-link behavior
- [ ] verify against Google faceted-navigation guidance
- [ ] implement via Rank Math where capability applies; platform layer only where necessary
- [ ] crawl regression

## B10 — Store final regression

- [ ] recrawl all store URL spaces
- [ ] zero unintended indexable duplicates
- [ ] zero unresolved price/schema contradiction P0/P1
- [ ] Rank Math single-owner check
- [ ] sitemap clean
- [ ] legacy redirect check
- [ ] internal links check
- [ ] store program coverage report

---

# C. HOMEPAGE — SECOND PROGRAM

- [ ] C-001 Homepage baseline
- [ ] C-002 Codex technical/content audit
- [ ] C-003 ChatGPT independent review
- [ ] C-004 brand/search intent
- [ ] C-005 title/meta/H1
- [ ] C-006 Organization/WebSite/other relevant schema review
- [ ] C-007 main navigation/internal links
- [ ] C-008 image/LCP/ALT
- [ ] C-009 content/CTA structure
- [ ] C-010 Rank Math ownership
- [ ] C-011 implementation
- [ ] C-012 dual QA
- [ ] C-013 monitoring

---

# D. OTHER STATIC / CORE PAGES

ابتدا inventory؛ سپس همه صفحات ثابت.

حداقل موارد شناخته‌شده و هر مورد دیگری که کشف شود:
- [ ] D-001 About / brand pages
- [ ] D-002 Contact / communication pages
- [ ] D-003 FAQ
- [ ] D-004 Stores address
- [ ] D-005 policy/terms/privacy pages — indexability decision
- [ ] D-006 landing pages
- [ ] D-007 other WordPress Pages

برای هر صفحه:
baseline → Codex Audit → ChatGPT Review → disposition → implementation → dual QA.

---

# E. BLOG / ARTICLES

تمام URLهای `articles` و blog-like content:

## E0 Architecture
- [ ] E0-001 Article inventory
- [ ] E0-002 Categories/tags inventory
- [ ] E0-003 archive/indexability policy
- [ ] E0-004 query/content overlap with Academy
- [ ] E0-005 article schema/author/date ownership
- [ ] E0-006 Rank Math article settings

### Blog Tags — planned decommission
**Project direction:** Blog Tags نیز در معماری نهایی موردنیاز نیستند و هدف حذف کنترل‌شده آن‌هاست؛ Categories/Articles/Hubs باید قبل از حذف نقش مقصد و ناوبری لازم را پوشش دهند.

- [ ] E0-007 Inventory all Blog Tags, assignments and public tag archive URLs
- [ ] E0-008 Analyze GSC/history, indexation, sitemap presence, internal links and any known inbound-link/value signals
- [ ] E0-009 Map every Blog Tag URL to the best durable replacement: relevant Category / Article / Content Hub; use `REMOVE_410` only when no meaningful replacement exists and evidence supports it
- [ ] E0-010 Prepare migration plan: redirect/410 mapping, internal-link cleanup, tag-assignment cleanup, Rank Math sitemap/indexability cleanup and rollback scope
- [ ] E0-011 Remove Blog Tag usage/archive exposure only after approval and implement the approved migration map
- [ ] E0-012 Crawl + sitemap + canonical + internal-link + GSC follow-up QA after decommission

## E1 All articles
برای **هر مقاله**:
- [ ] baseline/GSC
- [ ] query/intent
- [ ] Codex Audit
- [ ] ChatGPT Second Review
- [ ] accuracy/freshness
- [ ] heading/content architecture
- [ ] Information Gain
- [ ] author/reviewer/source where relevant
- [ ] title/meta
- [ ] internal links to products/academy
- [ ] image/ALT
- [ ] schema
- [ ] update/rewrite/merge/keep disposition
- [ ] implementation + dual QA
- [ ] monitoring

---

# F. ACADEMY / EDUCATION

تمام `education` pages/courses/lessons قابل crawl:

## F0 Architecture
- [ ] F0-001 Education inventory
- [ ] F0-002 taxonomy/archive inventory
- [ ] F0-003 course/lesson relationship
- [ ] F0-004 duplicate intent vs articles
- [ ] F0-005 internal links to relevant products
- [ ] F0-006 schema/content-type ownership

## F1 All education pages
برای هر صفحه همان dual-audit lifecycle کامل.

تمرکز اضافه:
- instructional accuracy
- step clarity
- media/video discoverability
- relevant product linking without forced commercial stuffing
- content freshness
- user questions

---

# G. ARTISTS / HISTORY / OTHER CUSTOM CONTENT

- [ ] G-001 Artists inventory
- [ ] G-002 Interview/profile pages
- [ ] G-003 History pages
- [ ] G-004 any custom post type discovered
- [ ] G-005 intent/indexability
- [ ] G-006 dual audit every indexable entity
- [ ] G-007 archive policy
- [ ] G-008 structured data where appropriate
- [ ] G-009 internal linking
- [ ] G-010 implementation + dual QA

---

# H. TAXONOMIES / ARCHIVES / SYSTEM URLS

تمام URLهایی که «محتوا» نیستند نیز باید تصمیم داشته باشند.

- [ ] H-001 WordPress categories
- [ ] H-002 tags
- [ ] H-003 author archives
- [ ] H-004 date archives
- [ ] H-005 media attachment URLs
- [ ] H-006 internal search result pages
- [ ] H-007 feeds
- [ ] H-008 pagination
- [ ] H-009 cart
- [ ] H-010 checkout
- [ ] H-011 my-account
- [ ] H-012 login/system endpoints relevant to crawl
- [ ] H-013 404 behavior
- [ ] H-014 any URL space discovered later

هدف برای این بخش معمولاً `KEEP_AS_IS/NOINDEX/REDIRECT/CANONICALIZE` است، نه تولید محتوا.

---

# I. FINAL SITEWIDE VALIDATION

بعد از پوشش همه families:

- [ ] I-001 Full URL inventory reconciliation
- [ ] I-002 Every entity has dossier/disposition
- [ ] I-003 Full crawl/indexability regression
- [ ] I-004 redirects/404/soft-404
- [ ] I-005 canonical consistency
- [ ] I-006 sitemap validation
- [ ] I-007 robots/meta/X-Robots
- [ ] I-008 internal linking/orphans
- [ ] I-009 structured-data regression
- [ ] I-010 Rank Math ownership regression
- [ ] I-011 duplicate title/meta review
- [ ] I-012 content cannibalization review
- [ ] I-013 mobile/CWV representative templates
- [ ] I-014 OAI-SearchBot/Googlebot access check where applicable
- [ ] I-015 unresolved P0/P1 = zero or formally accepted exception
- [ ] I-016 final Search Console baseline comparison
- [ ] I-017 final project coverage report

---

# J. CONTINUOUS MONITORING

- [ ] J-001 monthly/periodic GSC snapshots
- [ ] J-002 28/56-day change reviews
- [ ] J-003 new URL/entity discovery
- [ ] J-004 new 404/redirect issues
- [ ] J-005 Rank Math/plugin update regression
- [ ] J-006 Google documentation changes relevant to decisions
- [ ] J-007 content freshness queue
- [ ] J-008 price/schema consistency sampling
- [ ] J-009 new systemic finding triage

---

# Task-writing rule

ChatGPT هنگام نوشتن هر task Codex باید به این TODO استناد کند:

- Program ID
- Task ID
- entity/batch
- prerequisite status
- expected dossier/change outputs
- Google basis
- SEO owner (Rank Math / Rank Math Extension / Platform / Content)
- acceptance criteria
- next TODO item unlocked

هیچ task نباید بدون جایگاه مشخص در این Master TODO ساخته شود، مگر incident فوری که بعداً backfill شود.
