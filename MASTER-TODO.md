# MASTER TODO — Final SEO Mariwork

**Role:** مرجع اصلی ترتیب اجرا و پوشش کامل پروژه  
**Framework:** v1.0  
**Current program:** P-007 COMPLETE / READY_FOR_TASK PACKAGES AVAILABLE FOR GOVERNED TASK GENERATION  
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
- [ ] A-009B Low-consumption Round-1 runner v2 — deploy deterministic evidence + grouped Foundation + batched page audits before resuming A-013
- [x] A-010 Build complete URL/Entity Inventory
- [x] A-011 Map all current page types / taxonomies / custom post types
- [x] A-012 Map legacy URLs from Search Console and redirects
- [x] A-013 Sitewide Technical SEO Baseline
- [x] A-014 Rank Math Configuration & Ownership Audit
- [x] A-015 Detect duplicate SEO owners/output
- [x] A-016 Normalize Search Console baseline
- [x] A-017 Obtain/derive Page+Query data where possible
- [x] A-018 Build initial Query/Intent Map
- [x] A-019 Build initial Content Architecture
- [x] A-020 Create first Systemic Findings registry
- [x] A-021 Freeze Batch 001 selection

**Gate:** Store page audits شروع نمی‌شوند تا A-010 تا A-020 کامل یا blocker آن‌ها صریحاً ثبت شده باشد.

## 0.1 — 2026-09-25 Full-site pre-implementation closure reconciliation

`audits/sitewide/PRE-IMPLEMENTATION-COVERAGE-MATRIX.json` is the current
coverage source. The checks marked complete below mean that the audit/inventory
evidence exists; they do not mean that ChatGPT Second Review, approval,
implementation or QA is complete. Combined items that include future decisions
remain unchecked.

`A-009` and `A-009B` remain unchecked because `audits/sitewide/A-009-deployment-
blocker.md` records that the isolated runtime has not passed the no-write/no-
credential deployment gate. This task used existing repository evidence and
direct read-only checks; it did not resume autonomous execution.

## 0.2 — Decision-to-Execution Gate

After full-site Audit and ChatGPT Second Review, project work is governed by:

- `strategy/DECISION-BACKLOG.md` — the canonical list of unresolved/accepted target-state decisions.
- `tasks/EXECUTION-BACKLOG.md` — implementation packages unlocked only from accepted decisions.
- `docs/DECISION-TO-EXECUTION-GOVERNANCE.md` — process law.

**Important:** this MASTER-TODO remains the authority for complete-site coverage and program ordering, but no checkbox here independently authorizes a Production write.

Before any implementation task:
- all blocking Decision IDs must be `ACCEPTED`;
- the linked Execution item must be `READY_FOR_TASK`;
- exact target state/write scope must be known;
- required change dossier/canary/rollback/QA gates must exist.

Current strategy work is intentionally collaborative and may span multiple days. Findings and recommendations are converted into decisions first; execution tasks are generated later from the accepted decision set.

---

# B. STORE / WOOCOMMERCE — FIRST MAJOR PROGRAM

تمام URLهای فروشگاه باید پوشش داده شوند.

## B0 — Store architecture / non-page spaces

- [x] B0-001 Shop archive audit
- [ ] B0-002 Product sitemap policy
- [x] B0-003 Product category inventory
- [x] B0-004 Product tag inventory
- [ ] B0-005 Product attribute archive inventory
- [x] B0-006 Filter/faceted URL inventory
- [x] B0-007 Sort/query parameter URL inventory
- [x] B0-008 Pagination behavior
- [x] B0-009 Product search URLs
- [ ] B0-010 Variant URL architecture
- [x] B0-011 Bundle/set architecture
- [ ] B0-012 Legacy product URL mapping
- [x] B0-013 Store internal-link baseline
- [x] B0-014 Store schema ownership baseline
- [x] B0-015 Store Rank Math settings baseline
- [x] B0-016 Build Internal Link Requirement Matrix for Store ↔ Academy/Blog relationships
- [x] B0-017 Classify links by rule: CORE/MANDATORY, FAMILY-SPECIFIC, CONTEXTUAL/OPTIONAL
- [ ] B0-018 Audit every product family for missing mandatory links and inconsistent link coverage
- [x] B0-019 Define reverse links from Academy/Articles to relevant Product/Category destinations
- [ ] B0-020 Approve target internal-link architecture before mass page implementation
- [x] B0-021 Audit current product-title patterns across all Store families and identify inconsistencies
- [ ] B0-022 Define approved Product Title Naming Standard by family: product type/name/color, «ماری ورک»/Mariwork, code, size/volume ordering, required/optional tokens and exceptions
- [ ] B0-023 Verify consistent use of «ماری ورک» / Mariwork in product titles according to the approved family standard
- [ ] B0-024 Normalize product titles only after ChatGPT Second Review + approval; preserve product identity, intent and legacy URL history
- [ ] B0-025 Final product-title consistency regression across all published products

## B1 — Product pilot

اول ۵ صفحه representative:
- [ ] B1-001 انتخاب Pilot Batch 001 بر اساس GSC + family diversity
- [ ] B1-002 Codex Audit همه ۵ صفحه
- [ ] B1-003 ChatGPT Second Review همه ۵ صفحه
- [ ] B1-004 استخراج FAMILY/SITEWIDE findings
- [ ] B1-005 Content/Title/Meta/Schema/ALT rules candidates, including Product Title Naming Standard candidates
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

- [x] C-001 Homepage baseline
- [x] C-002 Codex technical/content audit
- [ ] C-003 ChatGPT independent review
- [ ] C-004 brand/search intent
- [ ] C-005 title/meta/H1
- [x] C-006 Organization/WebSite/other relevant schema review
- [x] C-007 main navigation/internal links
- [ ] C-008 image/LCP/ALT
- [ ] C-009 content/CTA structure
- [x] C-010 Rank Math ownership
- [ ] C-011 implementation
- [ ] C-012 dual QA
- [ ] C-013 monitoring

---

# D. OTHER STATIC / CORE PAGES

ابتدا inventory؛ سپس همه صفحات ثابت.

حداقل موارد شناخته‌شده و هر مورد دیگری که کشف شود:
- [x] D-001 About / brand pages
- [x] D-002 Contact / communication pages
- [x] D-003 FAQ
- [x] D-004 Stores address
- [ ] D-005 policy/terms/privacy pages — indexability decision
- [x] D-006 landing pages
- [x] D-007 other WordPress Pages

برای هر صفحه:
baseline → Codex Audit → ChatGPT Review → disposition → implementation → dual QA.

---

# E. BLOG / ARTICLES

تمام URLهای `articles` و blog-like content:

## E0 Architecture
- [x] E0-001 Article inventory
- [x] E0-002 Categories/tags inventory
- [x] E0-003 archive/indexability policy
- [x] E0-004 query/content overlap with Academy
- [x] E0-005 article schema/author/date ownership
- [x] E0-006 Rank Math article settings

### Blog Tags — planned decommission
**Project direction:** Blog Tags نیز در معماری نهایی موردنیاز نیستند و هدف حذف کنترل‌شده آن‌هاست؛ Categories/Articles/Hubs باید قبل از حذف نقش مقصد و ناوبری لازم را پوشش دهند.

- [x] E0-007 Inventory all Blog Tags, assignments and public tag archive URLs
- [x] E0-008 Analyze GSC/history, indexation, sitemap presence, internal links and any known inbound-link/value signals
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
- [x] F0-001 Education inventory
- [x] F0-002 taxonomy/archive inventory
- [x] F0-003 course/lesson relationship
- [x] F0-004 duplicate intent vs articles
- [x] F0-005 internal links to relevant products
- [x] F0-006 schema/content-type ownership

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

- [x] G-001 Artists inventory
- [ ] G-002 Interview/profile pages
- [ ] G-003 History pages
- [x] G-004 any custom post type discovered
- [x] G-005 intent/indexability
- [ ] G-006 dual audit every indexable entity
- [x] G-007 archive policy
- [ ] G-008 structured data where appropriate
- [ ] G-009 internal linking
- [ ] G-010 implementation + dual QA

---

# H. TAXONOMIES / ARCHIVES / SYSTEM URLS

تمام URLهایی که «محتوا» نیستند نیز باید تصمیم داشته باشند.

- [x] H-001 WordPress categories
- [x] H-002 tags
- [x] H-003 author archives
- [x] H-004 date archives
- [x] H-005 media attachment URLs
- [x] H-006 internal search result pages
- [x] H-007 feeds
- [x] H-008 pagination
- [x] H-009 cart
- [x] H-010 checkout
- [x] H-011 my-account
- [x] H-012 login/system endpoints relevant to crawl
- [x] H-013 404 behavior
- [x] H-014 any URL space discovered later

هدف برای این بخش معمولاً `KEEP_AS_IS/NOINDEX/REDIRECT/CANONICALIZE` است، نه تولید محتوا.

---

# I. FINAL SITEWIDE VALIDATION

بعد از پوشش همه families:

- [x] I-001 Full URL inventory reconciliation
- [ ] I-002 Every entity has dossier/disposition
- [ ] I-003 Full crawl/indexability regression
- [ ] I-004 redirects/404/soft-404
- [ ] I-005 canonical consistency
- [ ] I-006 sitemap validation
- [ ] I-007 robots/meta/X-Robots
- [ ] I-008 internal linking/orphans
- [ ] I-008A validate mandatory-link coverage against the approved Internal Link Requirement Matrix
- [ ] I-008B validate no family has inconsistent core-link coverage without a documented exception
- [ ] I-009 structured-data regression
- [ ] I-010 Rank Math ownership regression
- [ ] I-011 duplicate title/meta review
- [ ] I-011A validate all published product titles against the approved Product Title Naming Standard
- [ ] I-011B validate brand token, product type/name/color, product code and size/volume consistency; only documented exceptions may differ
- [ ] I-012 content cannibalization review
- [ ] I-013 mobile/CWV representative templates
- [ ] I-014 OAI-SearchBot/Googlebot access check where applicable
- [ ] I-015 unresolved P0/P1 = zero or formally accepted exception
- [ ] I-016 final Search Console baseline comparison
- [x] I-017 final project coverage report
- [ ] I-018 visual/image/multimodal SEO regression against approved L-program rules
- [ ] I-019 all-video SEO coverage/regression against M-program inventory
- [ ] I-020 brand/entity consistency regression against N-program target state

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

# K. EXTERNAL PR / ADVERTORIAL STRATEGY

این مرحله بعد از تثبیت Query Map، Content Architecture، Internal Link Architecture و صفحات هدف اجرا می‌شود. هدف، خرید صرف backlink نیست؛ هدف طراحی برنامه انتشار مقاله/رپورتاژ پولی و PR خارجی بر اساس داده و نقش واقعی هر landing page است.

- [ ] K-001 Build External PR / Advertorial Strategy from final SEO evidence
- [ ] K-002 Identify priority query/topic clusters that benefit from external amplification
- [ ] K-003 Select the correct landing page for each campaign: Category / Article / Academy / Product / Brand page
- [ ] K-004 Define supporting internal-link path from each external landing page into the site architecture
- [ ] K-005 Classify publisher types: major general media, art/culture media, lifestyle/creative media, specialist publications
- [ ] K-006 Define article angles by audience and publisher type; avoid duplicate/thin advertorial concepts
- [ ] K-007 Define anchor/link policy, including sponsored/nofollow handling where applicable
- [ ] K-008 Build publisher-evaluation criteria: topical relevance, real audience, editorial quality, visibility, referral potential, brand fit and publication permanence
- [ ] K-009 Create campaign matrix: publisher type × topic × landing page × supporting pages × CTA × KPI
- [ ] K-010 Prioritize campaigns by strategic value rather than domain metrics alone
- [ ] K-011 Define measurement plan: referral traffic, assisted conversions where available, branded search, GSC landing-page movement and downstream internal navigation
- [ ] K-012 Launch controlled pilot campaigns before scaling
- [ ] K-013 Review pilot results and update publisher/topic/landing-page rules
- [ ] K-014 Maintain external publication inventory with publication date, article URL, target page, link attributes, campaign purpose and measured outcome
- [ ] K-015 Periodic external-authority / PR strategy review as the site and content architecture evolve

**Rule:** هیچ رپورتاژ یا مقاله خارجی نباید صرفاً به‌دلیل DA/DR یا امکان دریافت لینک انتخاب شود. موضوع، رسانه، مخاطب و landing page باید با معماری و evidence نهایی پروژه هم‌راستا باشند.

---


# L. VISUAL / IMAGE / MULTIMODAL SEO — CORE WORKSTREAM

این برنامه جزو کارهای اصلی پروژه است و نباید به‌عنوان enhancement اختیاری در انتهای کار رها شود. Audit و implementation آن باید با Store / Blog / Academy / Homepage هماهنگ باشد.

- [ ] L-001 Build complete SEO-relevant image inventory by page/entity/family
- [ ] L-002 Audit primary product images and gallery-image discoverability
- [ ] L-003 Audit images across Category / Article / Academy / Homepage / trust content
- [ ] L-004 Define ALT policy by content type and image role; avoid keyword stuffing and decorative-image noise
- [ ] L-005 Define image filename / media naming policy for new assets
- [ ] L-006 Define primary-image consistency and representative-image rules by product/content family
- [ ] L-007 Map Google Images / visual / multimodal opportunities to approved query and content architecture
- [ ] L-008 Audit image context: surrounding copy, captions where useful, linked-image behavior and duplicate/reused media
- [ ] L-009 Review image technical delivery: dimensions, formats, lazy loading, accessibility and representative performance impact
- [ ] L-010 Produce implementation-ready image SEO rules by family
- [ ] L-011 Implement approved image/ALT/context changes
- [ ] L-012 Final image / visual SEO regression and coverage report
- [ ] L-013 Monitor image-search / multimodal visibility where data is available

**Completion invariant:** every important indexable family has an approved image policy and every priority image has an explicit SEO/accessibility disposition.

---

# M. VIDEO SEO — CORE WORKSTREAM

**Project rule:** تمام ویدیوهای سایت باید در برنامه SEO قرار بگیرند. Video SEO یک کار اصلی است، نه optional enhancement.

- [ ] M-001 Build complete video inventory across all public pages, Academy, Articles, Products and other content
- [ ] M-002 Map every video to its host page/entity, purpose, topic and search/user intent
- [ ] M-003 Audit crawlability/discoverability of every video and its host page
- [ ] M-004 Audit video titles, descriptions, surrounding text and page context
- [ ] M-005 Define VideoObject / video structured-data ownership and implementation strategy where eligible
- [ ] M-006 Define thumbnail quality, uniqueness, dimensions and representative-thumbnail policy
- [ ] M-007 Define video transcript / summary / key instructional text policy where useful
- [ ] M-008 Define video naming and reusable metadata standards
- [ ] M-009 Map video ↔ Academy / Article / Product / Category internal-link relationships
- [ ] M-010 Identify duplicate, weakly embedded, orphaned or context-poor videos
- [ ] M-011 Create per-video or family-level approved target states
- [ ] M-012 Implement approved Video SEO changes for ALL in-scope videos
- [ ] M-013 Validate video structured data / thumbnails / host-page indexability after implementation
- [ ] M-014 Final all-video SEO coverage report
- [ ] M-015 Monitor video-search/discovery performance where data is available

**Completion invariant:** every discovered public video has an inventory record, host-page relationship, SEO disposition and QA outcome.

---

# N. BRAND / ENTITY SEARCH STRATEGY — CORE WORKSTREAM

این برنامه نیز جزو کارهای اصلی پروژه است و باید با Homepage، About/Trust content، schema، external PR و branded-query monitoring هماهنگ شود.

- [ ] N-001 Build Mariwork brand/entity baseline
- [ ] N-002 Audit branded Search results and branded query families
- [ ] N-003 Audit Organization / WebSite / relevant entity schema ownership and consistency
- [ ] N-004 Audit Homepage / About / founder / history / contact / trust signals as entity-supporting content
- [ ] N-005 Audit brand naming consistency across titles, content, structured data and public profiles/evidence
- [ ] N-006 Map important off-site brand/entity references that can be verified without inventing relationships
- [ ] N-007 Identify brand/entity content and evidence gaps
- [ ] N-008 Define target Brand / Entity Search Strategy and canonical brand facts
- [ ] N-009 Connect external PR / advertorial strategy to approved brand/entity goals
- [ ] N-010 Implement approved entity-supporting site changes
- [ ] N-011 Final brand/entity consistency QA
- [ ] N-012 Monitor branded queries, branded landing pages and SERP changes over time

**Rule:** no fabricated credentials, awards, reviews, relationships or entity claims may be added for SEO.

---

# O. REQUIRED SEO EXPANSION REVIEWS / REMINDERS

این موارد فعلاً به‌عنوان review/reminder ثبت می‌شوند تا بعد از آماده‌شدن داده و معماری اصلی بررسی شوند. نتیجه هر review می‌تواند به یک برنامه اجرایی مستقل تبدیل شود.

## Merchant Center / Free Listings
- [ ] O-001 Review Google Merchant Center / Free Listings opportunity and eligibility
- [ ] O-002 Audit product-data readiness: identifiers, price, availability, images, landing pages and consistency
- [ ] O-003 Decide whether a Merchant Center / product-feed implementation program should be opened

## Product Feed / Variant Architecture
- [ ] O-004 Review product feed architecture against current Woo variable products / sets / mediums
- [ ] O-005 Review variant identity, SKU/ID, Product/ProductGroup-style representation, canonical and landing-page consistency
- [ ] O-006 Reconcile feed requirements with B0 variant architecture and structured-data ownership before implementation

## Reviews / Social Proof
- [ ] O-007 Review current review/social-proof availability and quality
- [ ] O-008 Define compliant collection/display/schema policy using only genuine reviews
- [ ] O-009 Decide whether review/social-proof improvements warrant an implementation program

---

# P. STRATEGY DECISION COVERAGE / FREEZE

This program validates that the Decision Backlog is complete enough to govern Production implementation.

- [x] P-001 Independent Codex Decision Backlog coverage audit against the full repository; Production read-only
- [x] P-002 ChatGPT independent review of P-001 findings and candidate missing/over-broad decisions
- [x] P-003 Reconcile Decision Backlog: add/split/merge/reclassify decisions; preserve stable DEC IDs already referenced
- [x] P-004 Build decision-source/dependency coverage matrix with zero unexplained material gaps
- [x] P-005 Freeze Decision Backlog v1 for collaborative decision sessions
- [x] P-005A Final ChatGPT pre-Strategy-Lock consistency audit after owner decisions; reconcile stale strategy docs and confirm zero unexplained material decision gaps
- [x] P-006 Reconcile Execution Backlog against the frozen Decision Backlog
- [x] P-007 Confirm every READY_FOR_TASK execution package is unlocked only by ACCEPTED decisions\n  - Result (2026-09-26): 57/57 packages validated; 16 `READY_FOR_TASK`; 41 `BLOCKED`; 0 Production writes. See `tasks/EXECUTION-BACKLOG.md`.
- [x] P-008 Build final execution TODO from all 57 P-007-validated packages; preserve gates/readiness; no Wave/priority assignment and no Codex Production task
  - Result (2026-09-26): `tasks/FINAL-EXECUTION-TODO.md`; 57/57 packages represented; 16 `READY_FOR_TASK`; 41 `BLOCKED`; 0 Production writes.
- [ ] P-009 Prioritize and Wave-plan the final execution TODO without bypassing package gates

**Freeze invariant:** before the first broad Production implementation wave, every material current SEO/content/technical choice must either:
- map to a Decision ID;
- be an already accepted framework/process rule;
- be explicitly classified as execution/QA-only rather than a strategy decision; or
- be intentionally DEFERRED with a documented reason.

No material audit finding, strategy TBD, current site family, technical-control domain, content/media workstream or migration policy may remain outside this classification.


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
