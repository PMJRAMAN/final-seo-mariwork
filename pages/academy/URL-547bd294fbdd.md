---
framework_version: "1.0"
dossier_schema_version: "1.0"
entity_id: "URL-547bd294fbdd"
wp_id: "UNKNOWN_NEEDS_VERIFICATION"
type: "archive"
family: "academy"
current_url: "https://www.mariwork.ir/academy/"
canonical_url: "https://www.mariwork.ir/academy/"
workflow_status: CODEX_AUDITED
final_disposition: NOT_DECIDED
blocked: false
blockers: []
---

# Page Dossier — URL-547bd294fbdd

## 0. State

- Workflow status: CODEX_AUDITED
- Final disposition: NOT_DECIDED

## 1. Identity

- Entity: URL-547bd294fbdd
- Current URL: https://www.mariwork.ir/academy/
- Canonical: https://www.mariwork.ir/academy/

## 2. URL History

Round-1 evidence only.

## 3. Baseline

- Source: supplied deterministic page evidence, GSC Pages row reference `GSC:Pages.csv:336`.
- Page+Query: NO — Page-query relationship is not proven by the current export.
- Coverage/inspection: NOT_AVAILABLE.

## 4. Current Page Snapshot

- HTTP 200; no redirect; self-canonical; `index, follow`; X-Robots empty; sitemap `sfwd-courses-sitemap.xml`.
- Title: `دوره‌ها - رنگ پارچه ماری ورک`; meta description: `دوره‌ها Archive - رنگ پارچه ماری ورک`; H1: `دوره‌ها`.
- Initial HTML exposes the archive and one course entry (`37 درس`, `6 بخش`) plus descriptive introductory text; 100 internal links.
- 3 images, 1 missing ALT, 1 lazy image; no parsed schema types. OG and mobile/performance evidence: NOT_AVAILABLE.

## 5. Search / Content Research

- Primary intent: academy/course discovery (inferred from path and visible archive heading; LOW confidence).
- Query evidence and page-query relation: NOT_AVAILABLE. Cannibalization: UNKNOWN_NEEDS_VERIFICATION.

## 6. Codex Audit

- Mode: READ-ONLY

### Findings

#### URL-547bd294fbdd-F001 — Archive metadata is generic

```yaml
severity: P2
scope: PAGE
status: CONFIRMED
evidence_class: OBSERVED
confidence: HIGH
source_refs: [supplied evidence, GSC:Pages.csv:336]
google_basis: GOOGLE_CONSISTENT
google_reference: https://developers.google.com/search/docs/appearance/title-link
seo_owner_current: UNKNOWN_NEEDS_VERIFICATION
seo_owner_target: RANK_MATH if capability is verified; otherwise UNKNOWN_NEEDS_VERIFICATION
rank_math_capability_checked: BLOCKED_BY_ACCESS
rank_math_path_or_reason_not_used: Production configuration unavailable.
```
**Evidence:** The title identifies the archive, but the meta description is the generic `دوره‌ها Archive - ...`; intended indexability is unknown.
**Impact:** The search-result representation may not clearly describe the academy archive. No ranking or traffic causation is claimed.
**Recommendation:** INITIAL — review archive title/meta ownership and intent after verifying Rank Math capability and current owner; do not draft final copy in Round 1.
**Acceptance criteria:** Approved archive intent, owner matrix, and before/after title/meta evidence; no duplicate SEO output.

#### URL-547bd294fbdd-F002 — Image ALT coverage gap

```yaml
severity: P2
scope: PAGE
status: CONFIRMED
evidence_class: MEASURED
confidence: HIGH
source_refs: [supplied evidence]
google_basis: GOOGLE_RECOMMENDED
google_reference: https://developers.google.com/search/docs/appearance/google-images
```
**Evidence:** 1 of 3 reported images is missing ALT; image role was not independently inspected.
**Impact:** Image context/accessibility may be incomplete.
**Recommendation:** INITIAL — classify the image as informative or decorative, then add descriptive ALT only when justified; retain empty ALT for decorative imagery.
**Acceptance criteria:** Per-image decision and regression evidence; no invented image facts or keyword stuffing.

**Family reference:** SYS-011 (Academy/Education image ALT coverage gaps). `SYS-004` also covers the broader missing-schema evidence.

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
