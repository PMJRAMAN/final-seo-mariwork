---
framework_version: "1.0"
dossier_schema_version: "1.0"
entity_id: "TERM-product_cat-1902"
wp_id: "NOT_APPLICABLE"
type: "taxonomy"
family: "product_cat"
current_url: "https://www.mariwork.ir/product/fabric-colors/"
canonical_url: "https://www.mariwork.ir/product/fabric-colors/"
workflow_status: CODEX_AUDITED
final_disposition: NOT_DECIDED
blocked: false
blockers: []
---

# Page Dossier — TERM-product_cat-1902

## 0. State

- Workflow status: CODEX_AUDITED
- Final disposition: NOT_DECIDED
- Blocked: No; page-level audit completed with baseline gaps noted below.
- Framework/schema: 1.0 / 1.0

## 1. Identity

- Entity: TERM-product_cat-1902; WP ID: NOT_APPLICABLE; type/family: taxonomy/product_cat
- Current URL: https://www.mariwork.ir/product/fabric-colors/
- Canonical: https://www.mariwork.ir/product/fabric-colors/ (self-referential)
- Intended indexability: UNKNOWN_NEEDS_VERIFICATION; actual signals: 200, `index, follow`; sitemap: NOT_PRESENT_IN_OBSERVED_SITEMAPS
- Legacy URLs: `https://www.mariwork.ir/product/fabric-colors-250-ml/` → 301 to current URL (source: supplied inventory evidence)

## 2. URL History

| URL | Source/period | HTTP/redirect | Canonical destination | Mapping confidence | Notes |
|---|---|---|---|---|---|
| `/product/fabric-colors-250-ml/` | GSC Pages.csv:62; REST term 27 | 301 → current | current URL | HIGH | Do not attribute legacy metrics to current without joined evidence. |

## 3. Baseline

- Search Console: Pages.csv:62 is available in the supplied inventory; clicks/impressions/CTR/position: NOT_AVAILABLE here. Page+Query: NO — Page-query relationship is not proven by the current export.
- Coverage/indexing: NOT_AVAILABLE in supplied evidence; sitemap membership: NOT_PRESENT_IN_OBSERVED_SITEMAPS.

## 4. Current Page Snapshot

- HTTP/crawl: 200, no redirect in current request, X-Robots empty, meta robots `index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large`; canonical self-referential.
- Metadata: title `رنگ‌های پارچه - رنگ پارچه ماری ورک`; meta description supplied; H1 `رنگ‌های پارچه`; OG: NOT_AVAILABLE.
- Content: initial HTML exposes a 40-result category listing (1–20 shown), product headings and prices/volume options. No separate category-introduction block is evidenced in the supplied excerpt before the listing.
- Images/links: 22 images, 0 missing ALT, 20 lazy; 161 internal links.
- Structured data: schema_types `[]` in supplied extraction; JS/AJAX dependence for critical listing: NOT_AVAILABLE.

## 5. Search / Content Research

- Primary intent: mixed transactional category browsing (INFERRED from taxonomy label and visible product grid); exact query ownership: UNKNOWN_NEEDS_VERIFICATION.
- Information-gap hypothesis: category-level selection/use guidance is not evidenced in the supplied initial excerpt; Second Review should verify usefulness before any copy decision.
- Cannibalization/query relation: NOT_PROVEN; see SYS-007.

## 6. Codex Audit

- Mode: READ-ONLY

### Findings

#### TERM-product_cat-1902-F001 — Category decision-support content not evidenced

```yaml
severity: P2
scope: PAGE
status: HYPOTHESIS
evidence_class: OBSERVED
confidence: MEDIUM
source_refs: ["INPUT:evidence.text_excerpt", "INPUT:evidence.headings"]
google_basis: GOOGLE_CONSISTENT
google_reference: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
seo_owner_current: CONTENT/UNKNOWN_NEEDS_VERIFICATION
seo_owner_target: CONTENT after Second Review
rank_math_capability_checked: NOT_APPLICABLE_FOR_VISIBLE_COPY
rank_math_path_or_reason_not_used: This concerns visible category usefulness, not metadata implementation.
```
**Evidence:** The supplied initial-HTML excerpt shows breadcrumb/navigation and product listing, but no distinct category guidance block.
**Impact:** Users may receive product choices without verified category-level selection context; ranking or traffic causation is not claimed.
**Recommendation:** INITIAL — independently review intent and add only verified, genuinely useful category guidance if a gap is confirmed; do not draft replacement copy in Round 1.
**Acceptance criteria:** Second Review confirms the gap and approved content brief uses only verified facts, with no keyword stuffing or invented claims.

#### TERM-product_cat-1902-F002 — Structured-data extraction gap

```yaml
severity: P1
scope: FAMILY
status: CONFIRMED
evidence_class: MEASURED
confidence: MEDIUM
source_refs: ["INPUT:evidence.schema_types", "SYS-004"]
google_basis: GOOGLE_CONSISTENT
google_reference: https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
seo_owner_current: UNKNOWN_NEEDS_VERIFICATION
seo_owner_target: RANK_MATH where capability is verified
rank_math_capability_checked: BLOCKED_BY_ACCESS
rank_math_path_or_reason_not_used: Installed version/modules and current output owner unavailable.
```
**Evidence:** `schema_types: []` for this page; the same extraction gap is present across the supplied batch and is tracked by SYS-004.
**Impact:** Structured-data presence and consistency cannot be verified from the supplied extraction; rich-result eligibility is not inferred.
**Recommendation:** INITIAL — validate rendered/public output and Rank Math ownership for the product-category family before any schema change.
**Acceptance criteria:** Family sample records actual JSON-LD ownership, visible consistency, and a regression set.

#### TERM-product_cat-1902-F003 — Indexability/sitemap state needs verification

```yaml
severity: P1
scope: FAMILY
status: BLOCKED
evidence_class: OBSERVED
confidence: HIGH
source_refs: ["INPUT:inventory.sitemap", "INPUT:evidence.meta_robots", "SYS-001"]
google_basis: GOOGLE_CONSISTENT
google_reference: https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview
seo_owner_current: UNKNOWN_NEEDS_VERIFICATION
seo_owner_target: RANK_MATH where capability is verified
rank_math_capability_checked: BLOCKED_BY_ACCESS
rank_math_path_or_reason_not_used: Sitemap/taxonomy settings unavailable.
```
**Evidence:** Page is 200 and index-follow in supplied HTML, while sitemap is `NOT_PRESENT_IN_OBSERVED_SITEMAPS`; intended indexability is unknown.
**Impact:** The intended relationship between category indexability and sitemap policy is unresolved; no indexing outcome is claimed.
**Recommendation:** INITIAL — verify complete sitemap set, Coverage/URL Inspection, taxonomy policy, and Rank Math ownership before deciding inclusion or exclusion.
**Acceptance criteria:** Evidence-backed family policy records intended indexability, sitemap state, canonical, owner, and regression examples.

## 7. ChatGPT Independent Second Review

Pending.

## 8. Final Approved Findings

Pending.

## 9. Target State

NOT APPROVED in Round 1.

## 10. Implementation Plan

Not authorized.

## 11. Implementation Result

Not started.

## 12. Codex QA

Not started.

## 13. ChatGPT Final Acceptance QA

Not started.

## 14. Monitoring

Not started.

## 15. Change Log

Pending.

## 16. SEO Basis / Ownership Record

Round-1 only. Rank Math version/modules and current owners: BLOCKED_BY_ACCESS; see SYS-001. No Production change authorized.
