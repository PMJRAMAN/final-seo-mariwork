---
framework_version: "1.0"
dossier_schema_version: "1.0"
entity_id: "TERM-product_cat-28"
wp_id: "NOT_APPLICABLE"
type: "taxonomy"
family: "product_cat"
current_url: "https://www.mariwork.ir/product/fabric-printing-medium/"
canonical_url: "https://www.mariwork.ir/product/fabric-printing-medium/"
workflow_status: CODEX_AUDITED
final_disposition: NOT_DECIDED
blocked: false
blockers: []
---

# Page Dossier — TERM-product_cat-28

## 0. State

- Workflow status: CODEX_AUDITED
- Final disposition: NOT_DECIDED

## 1. Identity

- Entity: TERM-product_cat-28; WP ID: NOT_APPLICABLE; type/family: taxonomy/product_cat
- Current URL: https://www.mariwork.ir/product/fabric-printing-medium/
- Canonical: https://www.mariwork.ir/product/fabric-printing-medium/ (self-referential)
- Intended indexability: UNKNOWN_NEEDS_VERIFICATION; actual signals: 200, `index, follow`; sitemap: NOT_PRESENT_IN_OBSERVED_SITEMAPS

## 2. URL History

Round-1 evidence only; no legacy URL supplied.

## 3. Baseline

Search Console: Pages.csv:44 listed in supplied inventory; metrics: NOT_AVAILABLE here. Page+Query: NO — Page-query relationship is not proven by the current export. Coverage: NOT_AVAILABLE; sitemap: NOT_PRESENT_IN_OBSERVED_SITEMAPS.

## 4. Current Page Snapshot

- HTTP 200, no redirect, X-Robots empty, `index, follow`, self-canonical. Title: `مدیوم‌ها و اکلیل‌ها - رنگ پارچه ماری ورک`; meta description supplied; H1: `مدیوم‌ها و اکلیل‌ها`; OG: NOT_AVAILABLE.
- Initial HTML exposes 17 products and prices/options; 19 images/0 missing ALT/17 lazy; 150 internal links. Schema extraction: `[]`.

## 5. Search / Content Research

- Primary intent: transactional mediums/glitter browsing (INFERRED); exact query ownership: UNKNOWN_NEEDS_VERIFICATION.
- Product headings cover multiple subtypes; whether the category needs subcategory explanation or filtering guidance requires Second Review, not an automatic copy expansion.

## 6. Codex Audit

- Mode: READ-ONLY

### Findings

#### TERM-product_cat-28-F001 — Category structure/usefulness needs independent review

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
rank_math_path_or_reason_not_used: Visible category usefulness is not a metadata concern.
```
**Evidence:** The category combines glitter, glue, fixative, base coat and other medium products in the supplied headings; no category guidance block is evidenced in the excerpt.
**Impact:** Users may need clearer decision support, but the evidence does not establish that copy is required or that performance is affected.
**Recommendation:** INITIAL — Second Review should test whether the mixed assortment is understandable and identify only verified information gaps.
**Acceptance criteria:** Approved family/content brief defines useful, fact-checked guidance without keyword stuffing or invented product claims.

#### TERM-product_cat-28-F002 — Batch-level structured data and sitemap verification gaps

```yaml
severity: P1
scope: FAMILY
status: BLOCKED
evidence_class: MEASURED
confidence: HIGH
source_refs: ["INPUT:evidence.schema_types", "INPUT:inventory.sitemap", "SYS-001", "SYS-004"]
google_basis: GOOGLE_CONSISTENT
google_reference: https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
seo_owner_current: UNKNOWN_NEEDS_VERIFICATION
seo_owner_target: RANK_MATH where capability is verified
rank_math_capability_checked: BLOCKED_BY_ACCESS
rank_math_path_or_reason_not_used: Installed modules/settings unavailable.
```
**Evidence:** `schema_types: []`; sitemap is not present in observed sitemaps; page is 200/index-follow.
**Impact:** Family technical policy and schema ownership are unresolved.
**Recommendation:** INITIAL — validate family-level output and Rank Math ownership before any change.
**Acceptance criteria:** Regression sample verifies canonical, robots, sitemap and rendered schema.

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

Round-1 only. Rank Math capability/current owner: BLOCKED_BY_ACCESS; see SYS-001. No Production change authorized.
