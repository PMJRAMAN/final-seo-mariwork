---
framework_version: "1.0"
dossier_schema_version: "1.0"
entity_id: "TERM-product_cat-82"
wp_id: "NOT_APPLICABLE"
type: "taxonomy"
family: "product_cat"
current_url: "https://www.mariwork.ir/product/fabric-color-set/"
canonical_url: "https://www.mariwork.ir/product/fabric-color-set/"
workflow_status: CODEX_AUDITED
final_disposition: NOT_DECIDED
blocked: false
blockers: []
---

# Page Dossier — TERM-product_cat-82

## 0. State

- Workflow status: CODEX_AUDITED
- Final disposition: NOT_DECIDED

## 1. Identity

- Entity: TERM-product_cat-82
- Current URL: https://www.mariwork.ir/product/fabric-color-set/
- Canonical: https://www.mariwork.ir/product/fabric-color-set/

## 2. URL History

Round-1 evidence only.

## 3. Baseline

Task position: B7 product-category audit; Round-1 batch of 5. Supplied evidence only. GSC page row is Pages.csv:47 (independent Pages export; no Page+Query relation).

## 4. Current Page Snapshot

HTTP 200 with no redirect; canonical matches current URL; `index, follow` meta robots observed; X-Robots-Tag empty. Category is absent from observed sitemaps. Title/H1: «ست های رنگ پارچه». The page lists 22 results and has 161 internal links; 22 images, none missing alt, 20 lazy-loaded. Parsed schema types: none.

## 5. Search / Content Research

No joined Page+Query evidence supplied. Current evidence supports a product-category listing intent, but does not establish query ownership, ranking cause, or final indexability policy. Legacy URLs: NOT_AVAILABLE.

## 6. Codex Audit

- Mode: READ-ONLY

### Findings

Audit outcome: current public HTML is technically reachable and canonicalized, but category indexability/sitemap policy and structured-data ownership are not sufficiently evidenced for a disposition.

#### TERM-product_cat-82-F001
- severity: P1
- scope: PAGE
- status: BLOCKED
- evidence_class: OBSERVED
- confidence: HIGH
- source_refs: `INPUT:evidence`; `GSC:Pages.csv:47`; `SITEMAP:observed sitemap set`
- impact: The page emits indexable robots and a self-canonical, while the category is not present in observed sitemaps; intended indexability and sitemap policy are both `UNKNOWN_NEEDS_VERIFICATION`.
- recommendation: INITIAL — verify the approved category policy, current Rank Math taxonomy settings and sitemap ownership before deciding KEEP INDEXED, noindex or another disposition. Do not change production in Round 1.
- acceptance_criteria: Current policy, Rank Math capability/current owner, sitemap inclusion rule, and representative category regression evidence are recorded and Second Reviewed.
- google_basis: GOOGLE_CONSISTENT
- google_reference: https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview
- seo_owner_current: UNKNOWN_NEEDS_VERIFICATION
- seo_owner_target: RANK_MATH where capability is verified; otherwise UNKNOWN_NEEDS_VERIFICATION
- rank_math_capability_checked: BLOCKED_BY_ACCESS (see SYS-001)
- rank_math_path_or_reason_not_used: Production Rank Math version/modules/settings unavailable.

#### TERM-product_cat-82-F002
- severity: P2
- scope: PAGE
- status: OPEN
- evidence_class: MEASURED
- confidence: MEDIUM
- source_refs: `INPUT:evidence`; `HTML:schema_types=[]`; `registry:SYS-004`
- impact: No parsed JSON-LD/microdata schema type was observed on a category page containing a 22-item product listing; structured-data presence and template ownership need validation.
- recommendation: INITIAL — validate initial and rendered HTML and the category template/plugin pipeline; if structured data is appropriate, maintain one verified owner and visible-data consistency. Do not invent product or offer data.
- acceptance_criteria: Rendered/schema audit confirms whether markup exists, identifies owner, and records consistency/regression results.
- google_basis: GOOGLE_CONSISTENT
- google_reference: https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- seo_owner_current: UNKNOWN_NEEDS_VERIFICATION
- seo_owner_target: RANK_MATH where capable; otherwise documented platform/template owner
- rank_math_capability_checked: BLOCKED_BY_ACCESS (see SYS-001)
- rank_math_path_or_reason_not_used: Capability and current output owner unavailable.

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

Round-1 only; ownership verification blocked and SYS-001 applies. No Production write authorized.
