# Mariwork SEO — Round 1 Handoff

## Baseline
- Source HEAD: `01b91a5a3a41bf7df45bd8fb5e35252beabeb61f`
- Generation is deterministic and timestamp-free; reruns from identical inputs are byte-stable.
- Framework version: 1.0; dossier schema: 1.0.
- Round-1 completion: 167/167 model-reviewed entities; page queue complete.

## Integrity
- Expected/indexed entities: 167/167
- Missing/malformed dossiers: 0/0
- CODEX_AUDITED or later: 167
- Blocked entities: 0
- NOT_DECIDED: 167

## Entity Breakdown
- Review group — STORE / SHOP: 84
- Review group — HOMEPAGE: 1
- Review group — STATIC PAGES: 10
- Review group — BLOG / ARTICLES: 12
- Review group — ACADEMY: 39
- Review group — ARCHIVES / SYSTEM / TAXONOMIES: 21

## Highest Historical-Importance Entities
Historical metrics are copied from existing inventory notes only; Page and Query exports are not joined.
- `WP-14450` — impressions=328501, clicks=790 — `pages/products/WP-14450.md`
- `WP-12608` — impressions=172026, clicks=1851 — `pages/products/WP-12608.md`
- `WP-27041` — impressions=167540, clicks=181 — `pages/products/WP-27041.md`
- `WP-27142` — impressions=136318, clicks=236 — `pages/products/WP-27142.md`
- `WP-27051` — impressions=126416, clicks=937 — `pages/products/WP-27051.md`
- `WP-28242` — impressions=121098, clicks=468 — `pages/products/WP-28242.md`
- `WP-13305` — impressions=94152, clicks=2750 — `pages/articles/WP-13305.md`
- `WP-12536` — impressions=79126, clicks=181 — `pages/products/WP-12536.md`
- `WP-28244` — impressions=77643, clicks=224 — `pages/products/WP-28244.md`
- `WP-30918` — impressions=75811, clicks=5728 — `pages/shop/WP-30918.md`

## Existing Finding Breakdown
- Existing findings extracted verbatim: 324
- Repeated finding candidates: 24

## Repeated Round-1 Finding Candidates
These are grouping aids, not Second Review conclusions.
- `R001` — 15 occurrences (normalized-exact-match); families=products
- `R002` — 15 occurrences (normalized-exact-match); families=education
- `R003` — 15 occurrences (normalized-exact-match); families=products
- `R004` — 15 occurrences (normalized-exact-match); families=products
- `R005` — 13 occurrences (normalized-exact-match); families=products
- `R006` — 12 occurrences (normalized-exact-match); families=products
- `R007` — 9 occurrences (normalized-exact-match); families=category
- `R008` — 8 occurrences (normalized-exact-match); families=products
- `R009` — 8 occurrences (normalized-exact-match); families=products
- `R010` — 6 occurrences (normalized-exact-match); families=articles
- `R011` — 6 occurrences (normalized-exact-match); families=products
- `R012` — 6 occurrences (normalized-exact-match); families=education
- `R013` — 5 occurrences (normalized-exact-match); families=products
- `R014` — 5 occurrences (normalized-exact-match); families=products
- `R015` — 5 occurrences (normalized-exact-match); families=products

## Sitewide/Foundation Work
- `A-010` — Complete URL/Entity Inventory: Round-1 evidence — `audits/sitewide/A-010-inventory-notes.md`
- `A-011` — Content types, taxonomies and archive map — `audits/sitewide/A-011-content-types-taxonomies.md`
- `A-012` — Legacy URL map — `audits/sitewide/A-012-legacy-url-map.md`
- `A-013` — Sitewide Technical SEO Baseline — `audits/sitewide/A-013-technical-baseline.md`
- `A-014` — Rank Math Configuration & Ownership Audit — `audits/sitewide/A-014-rank-math-ownership.md`
- `A-015` — Duplicate SEO Owners / Output Audit — `audits/sitewide/A-015-duplicate-seo-owners.md`
- `A-016` — GSC baseline — `audits/sitewide/A-016-gsc-baseline.md`
- `A-017` — Page+Query evidence — `audits/sitewide/A-017-page-query.md`
- `A-020` — Systemic Findings Bootstrap — `audits/sitewide/A-020-systemic-findings-bootstrap.md`

## Foundation Strategy Artifacts
- `QUERY-MAP` — `strategy/QUERY-MAP.md`
- `CONTENT-ARCHITECTURE` — `strategy/CONTENT-ARCHITECTURE.md`

## Second Review Order
1. Sitewide/Foundation index and systemic findings.
2. Store/shop entities, then remaining review groups in `round1-review-index.csv` order.
3. Page-specific findings in `round1-findings.csv`; original dossier paths are retained.

Final dispositions remain `NOT_DECIDED` until independent human Second Review and approval. No Production implementation is authorized by this handoff.
