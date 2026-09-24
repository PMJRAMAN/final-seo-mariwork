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

در `registry/URL-INVENTORY.csv`.

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
