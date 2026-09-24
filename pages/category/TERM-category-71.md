---
framework_version: "1.0"
dossier_schema_version: "1.0"
entity_id: "TERM-category-71"
wp_id: "NOT_APPLICABLE"
type: "taxonomy"
family: "category"
current_url: "https://www.mariwork.ir/mag/articles/"
canonical_url: "https://www.mariwork.ir/mag/articles/"
workflow_status: CODEX_AUDITED
final_disposition: NOT_DECIDED
blocked: false
blockers: []
---

# Page Dossier — TERM-category-71

## 0. State

- Workflow status: CODEX_AUDITED
- Final disposition: NOT_DECIDED

## 1. Identity

- Entity: TERM-category-71
- Current URL: https://www.mariwork.ir/mag/articles/
- Canonical: https://www.mariwork.ir/mag/articles/
- Intended indexability: UNKNOWN_NEEDS_VERIFICATION
- Actual signals: HTTP 200; `index, follow`; self-canonical; category sitemap observed.

## 2. URL History

Legacy `/category/articles/` was observed redirecting 301 to the current URL; no additional legacy mapping is supplied.

## 3. Baseline

GSC Pages.csv reference is historical/URL-level only; Page+Query: NO. Page-query relationship is not proven by the current export.

## 4. Current Page Snapshot

HTTP 200; title `مقالات آموزشی - رنگ پارچه ماری ورک`; meta description empty; H1 `دسته مقالات آموزشی`; 9 article H2s; 136 internal links; 12 images with 7 missing ALT; 10 lazy images; no parsed schema types.

## 5. Search / Content Research

The archive visibly lists educational articles. Query ownership, overlap with other content families, and final indexability intent require Second Review.

## 6. Codex Audit

- Mode: READ-ONLY

### Findings

Audit outcome: populated, indexable article category observed. Empty meta description and measured ALT gaps are recorded without a final content or indexability decision.

- id: TERM-category-71-F001
  severity: P2
  scope: PAGE
  status: OPEN
  evidence_class: OBSERVED
  confidence: HIGH
  source_refs: [supplied inventory TERM-category-71, pages/category/TERM-category-71.md]
  impact: The page has an empty meta description, leaving snippet generation to other page content.
  recommendation: INITIAL — after intent and ownership review, consider an accurate page-specific description through the verified SEO owner; do not draft final metadata in Round 1.
  acceptance_criteria: Approved description matches visible article archive content and is emitted by one verified owner.
  google_basis: GOOGLE_CONSISTENT
  google_reference: https://developers.google.com/search/docs/appearance/snippet
  seo_owner_current: UNKNOWN_NEEDS_VERIFICATION
  seo_owner_target: RANK_MATH if capability is verified
  rank_math_capability_checked: BLOCKED_BY_ACCESS
  rank_math_path_or_reason_not_used: Installed Rank Math version/modules and current meta owner were not supplied.

- id: TERM-category-71-F002
  severity: P2
  scope: PAGE
  status: OPEN
  evidence_class: MEASURED
  confidence: HIGH
  source_refs: [supplied inventory TERM-category-71]
  impact: 7 of 12 reported images lack ALT; image meaning/decorative status was not independently verified.
  recommendation: INITIAL — review image roles; use descriptive ALT for informative images and empty ALT for decorative images.
  acceptance_criteria: Image-by-image role decisions and accurate ALT output are reviewed; no invented descriptions.
  google_basis: GOOGLE_RECOMMENDED
  google_reference: https://developers.google.com/search/docs/appearance/google-images
  seo_owner_current: CONTENT/UNKNOWN_NEEDS_VERIFICATION
  seo_owner_target: CONTENT for ALT decisions
  rank_math_capability_checked: BLOCKED_BY_ACCESS
  rank_math_path_or_reason_not_used: Image/template ownership was not supplied.

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

Round-1 only.
