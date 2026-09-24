# Workflow — Final SEO Mariwork v1.0

## Phase 0 — Framework Foundation

Manifest، rules، templates، change control و specs تثبیت می‌شوند.

**Gate:** `AUDIT_FRAMEWORK_READY`

## Phase 1 — Site / Entity Inventory

تمام URL spaces شناسایی شوند:
- products / variations
- product/category/tag/attribute archives
- shop
- education/articles/artists/static
- pagination
- search URLs
- faceted/filter/parameter URLs
- feeds/attachments در صورت وجود
- cart/checkout/account/system pages

برای entityهای مهم:
- entity ID
- WP ID
- type/family
- current URL
- canonical
- indexability intent
- sitemap
- legacy URL
- dossier path
- final disposition (در ابتدا NOT_DECIDED)

در `registry/URL-INVENTORY.csv`.

برای صفحات محتوایی/canonical entityها disposition فردی ثبت می‌شود. برای URL spaceهای ماشینی مثل facet combinations، policy سراسری/خانوادگی می‌تواند کل space را پوشش دهد و لازم نیست برای هر ترکیب بی‌نهایت dossier جدا ساخته شود.

## Phase 2 — Sitewide Technical Baseline

قبل از batchهای صفحه، طبق `docs/SITEWIDE-TECHNICAL-AUDIT-SPEC.md` بررسی شود:

- crawl/index controls
- robots/meta/X-Robots
- sitemaps
- redirects/404/soft-404
- canonical patterns
- duplicate URL spaces
- facets/parameters
- pagination
- JS/AJAX discoverability
- internal link graph/orphans
- schema architecture
- Woo product/variant patterns
- mobile/page experience/CWV data where available
- image/media patterns

خروجی در `audits/sitewide/` و findings در registry.

**Audit only — no Production writes.**

## Phase 3 — Data Baseline

طبق `docs/DATA-SOURCES.md`:
- GSC page metrics
- legacy URL metrics
- Coverage/Indexing
- device/search appearance
- Page+Query data در صورت دسترسی
- derived URL mapping

هر page قبل از Codex Audit تا حد ممکن `BASELINED` می‌شود.

## Phase 4 — Strategy Baseline

`strategy/QUERY-MAP.md` و `strategy/CONTENT-ARCHITECTURE.md` به‌تدریج ساخته می‌شوند.

هدف:
- query clusters
- intent
- target entity
- cannibalization risks
- hub/support relationships
- product ↔ education linking opportunities

Query Map داده را جایگزین نمی‌کند؛ فقط تصمیم مستند بر اساس evidence است.

## Phase 5 — Batch Selection

Batchها به‌طور پیش‌فرض ۵ صفحه‌ای در شروع.

نوع batch:
- `PILOT` — برای تثبیت روش
- `FAMILY` — نمونه‌های یک خانواده
- `OPPORTUNITY` — داده‌محور
- `VALIDATION` — regression/control

Selection rationale اجباری.

## Phase 6 — Codex Audit

ChatGPT task می‌نویسد.

Codex:
- Production read-only
- dossier را تکمیل
- findings را ثبت
- systemic refs را ثبت
- status = `CODEX_AUDITED`

## Phase 7 — ChatGPT Second Review

برای کاهش anchoring:

1. Identity و raw evidence را بگیر.
2. تا حد ممکن URL زنده را **مستقلاً** بررسی و independent notes بساز.
3. سپس Codex findings را finding-by-finding بخوان.
4. CONFIRM / MODIFY / REJECT / NEEDS_MORE_EVIDENCE.
5. SERP/intent/content usefulness را بررسی.
6. یافته مستقل اضافه کن.
7. systemic scope را challenge کن.
8. Final Approved Findings را آماده کن.

Status:
`CODEX_AUDITED → SECOND_REVIEWED`

## Phase 8 — Reconciliation / Target State

برای هر finding:
- evidence نهایی
- severity/scope
- تصمیم
- target state
- acceptance criteria

اگر content change لازم است، Content Brief یا متن نهایی تأییدشده ثبت شود.

اگر systemic است:
- registry update
- Change Dossier

وقتی Definition of Ready برقرار شد:
`SECOND_REVIEWED → APPROVED`

## Phase 9 — Playbook Consolidation

بعد از evidence کافی، قواعد تکرارشونده در Playbook ثبت می‌شوند.

Rule فقط با Decision/approval مناسب `ACCEPTED` می‌شود.

## Phase 10 — Systemic Changes First

برای root cause مشترک:
- `changes/` dossier
- canary/sample
- regression set
- backup/rollback
- rollout criteria

اول سیستم اصلاح می‌شود، بعد page-level exceptions.

## Phase 11 — Page Implementation

Implementation Task فقط findings APPROVED را اجرا می‌کند.

تغییرات unrelated در یک bundle ممنوع.

`APPROVED → IMPLEMENTING → IMPLEMENTED`

## Phase 12 — Codex QA

طبق `docs/QA-SPEC.md`.

اگر pass:
`IMPLEMENTED → CODEX_QA_PASSED`

## Phase 13 — ChatGPT Final Acceptance QA

ChatGPT مستقل:
- live output
- approved target
- visible content
- core technical fields
- systemic regression sample در صورت نیاز

را مقایسه می‌کند.

اگر pass:
`CODEX_QA_PASSED → FINAL_QA_PASSED`

اگر fail، remediation task و برگشت به implementation.

## Phase 14 — Monitoring

طبق `docs/MEASUREMENT-SPEC.md`:
- change date annotation
- 28d / 56d یا بازه مناسب
- query mix در صورت وجود
- CTR/position/click/impression
- conversion/business metric اگر مجاز و قابل اتکا
- seasonality/confounders

`FINAL_QA_PASSED → MONITORING → COMPLETE`

## Emergency Exception

رفع incident مستقل از SEO workflow ممکن است خارج این چرخه انجام شود، ولی اگر SEO-relevant بود باید بعداً dossier/decision را backfill کند.


## Program Order — Master TODO

ترتیب family-level اجرای پروژه از `MASTER-TODO.md` می‌آید:

1. Pre-audit baseline
2. Store/WooCommerce — همه محصولات و URL spaces
3. Homepage
4. Other static/core pages
5. Blog/Articles
6. Academy/Education
7. Artists/History/Other custom content
8. Taxonomies/archives/system URLs
9. Final sitewide validation
10. Continuous monitoring

Inventory می‌تواند child task جدید ایجاد کند ولی ترتیب کلان بدون Decision تغییر نمی‌کند.

## Google/Rank Math Gate در هر Implementation

قبل از APPROVED → IMPLEMENTING:
- Google basis و reference ثبت شود؛
- owner فنی concern ثبت شود؛
- اگر Rank Math capability دارد، target owner = RANK_MATH؛
- اگر ندارد، دلیل و extension/platform architecture ثبت شود.


## Autonomous Round-1 Orchestration

Phase 1 تا 6 می‌توانند توسط runner به‌صورت serial/resumable خودکار شوند، مشروط به حفظ تمام gateهای framework.

Autonomous Round 1 شامل inventory، technical/data/strategy baselines، Codex page audits، findings و initial recommendations است و فقط تا `CODEX_AUDITED` اختیار دارد.

**اولین mandatory human decision gate = Phase 7 / ChatGPT Second Review.** از این نقطه تصمیم‌های نهایی title/meta/content/internal linking/schema/redirect/disposition و هر Production implementation با مشارکت کاربر انجام می‌شود.

Automation حق تغییر authority model را ندارد و limit/auth interruption باید stateful pause/resume باشد.


### Low-consumption Round-1 execution

Autonomous Round 1 separates **collection** from **reasoning**.

Deterministic collectors should gather reusable HTTP/HTML, metadata, canonical, schema, image/link and exact-page GSC evidence once. Codex must consume this evidence rather than repeatedly crawling the same URLs.

A logical SEO batch is not necessarily one model call. The first pilot remains five entities, but after that multiple entities from the same family may be analyzed in one model execution while still producing independent canonical dossiers.

Taxonomy/system URL spaces such as Product Tags and Blog Tags planned for decommission may be covered by FAMILY/SITEWIDE policy analysis rather than repetitive per-URL model reasoning. Complete-site disposition coverage remains mandatory.

Model calls should use the lowest reasoning level that preserves audit quality. Escalation to stronger reasoning is reserved for anomalous/complex cases.
