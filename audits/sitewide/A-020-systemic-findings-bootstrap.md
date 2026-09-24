# A-020 — Systemic Findings Bootstrap

**Task:** A-020 · **Program:** FOUNDATION / STORE-FIRST · **Framework:** v1.0
**Date:** 2026-09-24 · **Lifecycle:** CODEX_AUDITED
**Authority:** Round-1 evidence and initial recommendations only. No Second Review, approval, implementation or Production change.

## Scope and method

This bootstrap consolidates A-013 with A-018 Query Map and A-019 Content Architecture. Primary inputs were:

- data/normalized/round1-foundation-context.json
- data/normalized/round1-evidence-summary.json
- data/normalized/gsc-pages.json
- audits/sitewide/A-016-gsc-baseline.md
- audits/sitewide/A-017-page-query.md

Targeted support came from A-010/A-011/A-012/A-014/A-015 and representative JSONL evidence. URL-INVENTORY.csv was not full-read; raw exports and large ledgers were not edited.

## Baseline

- Foundation: 555 inventory rows, 167 model-page candidates and 25 policy/system spaces.
- Deterministic evidence: 501 entities; 440 HTTP 200, 58 HTTP 404, 3 safety-skipped.
- Issue summary: 289 missing meta descriptions, 271 missing H1s, 2 canonical differences, 286 noindex records, no parsed schema types.
- Public census: 83 products, 12 posts, 37 Academy lessons, 2 Academy/course rows, 7 product categories, 3 volume attributes, 275 product tags and 53 post-tag rows.
- GSC: 368 normalized page rows. No verified Page+Query dataset. **Page-query relationship is not proven by the current export.**
- Legacy: A-012 maps 375 selected sources; 67 GSC sources end at 404 and identity equivalence is unproven.
- Ownership: Rank Math version/modules/settings and complete current owners remain BLOCKED_BY_ACCESS.

## Registered findings

| ID | Scope | Severity | Status | Handoff |
|---|---|---:|---|---|
| SYS-001 | SITEWIDE | P1 | BLOCKED | Verify Rank Math capability and one owner per concern |
| SYS-002 | FAMILY | P1 | CONFIRMED | Separate Product Tag and Blog Tag migration programs |
| SYS-003 | SITEWIDE | P2 | CONFIRMED | Exact legacy source identity and disposition |
| SYS-004 | SITEWIDE | P1 | CONFIRMED | Segment metadata/H1/schema output by family |
| SYS-005 | SITEWIDE | P2 | BLOCKED | Map parameter/facet URL policy |
| SYS-006 | SITEWIDE | P1 | BLOCKED | Close duplicate SEO owner/output risk |
| SYS-007 | SITEWIDE | P1 | BLOCKED | Obtain joined Page+Query or direct filtered evidence |
| SYS-008 | FAMILY | P2 | OPEN | Review link matrix and product-title patterns |

Full finding contracts are in registry/SYSTEMIC-FINDINGS.md.

## Architecture handoff

The Query Map records family themes only and must not be read as query-to-URL attribution. The Content Architecture proposes durable roles for Shop, Product Category, Product, Set/Bundle, Medium/Tool, Academy/Lesson, Article and Trust content; CORE/MANDATORY, FAMILY-SPECIFIC and CONTEXTUAL/OPTIONAL link candidates; bidirectional Product/Category ↔ Academy/Article relationships; and a candidate Product Title Naming Standard covering «ماری ورک»/Mariwork, product type/name/color, code formatting and size/volume placement.

These are prepared for ChatGPT Second Review, not implementation rules.

## Initial recommendation order

1. Verify Rank Math version/modules/current owners before any metadata, canonical, robots, schema, sitemap or redirection implementation recommendation.
2. Obtain joined Page+Query or documented SERP/intent evidence; keep URL attribution unknown until then.
3. Create separate Product Tag and Blog Tag family migration dossiers with complete URL/term, history, links, sitemap, canonical/robots and replacement evidence.
4. Segment metadata/H1/schema issues by family and validate initial versus rendered output.
5. Build and review the internal-link requirement matrix and title-pattern inventory before bulk link/title changes.
6. Reconcile legacy 404/redirect sources by exact identity; preserve metrics and avoid unrelated bulk redirects.

## Authority and blockers

- Lifecycle ceiling: CODEX_AUDITED.
- Product Tag/Blog Tag outcomes, query URLs, title standard, internal-link rules, canonical/robots/schema policy and redirect mappings remain UNKNOWN_NEEDS_VERIFICATION, BLOCKED_BY_ACCESS or initial candidates.
- No page is approved. No content is production-ready. No Production, database, WordPress, WooCommerce, Rank Math, sitemap, redirect, taxonomy or raw-export write occurred.

**Google basis:** findings use GOOGLE_CONSISTENT or PROJECT_DECISION as stated in the registry. References: [Search Console performance reporting](https://support.google.com/webmasters/answer/7576553), [canonicalization](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls), [redirects](https://developers.google.com/search/docs/crawling-indexing/301-redirects), [faceted navigation](https://developers.google.com/crawling/docs/faceted-navigation), and [structured data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data).
