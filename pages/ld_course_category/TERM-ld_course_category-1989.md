---
framework_version: "1.0"
dossier_schema_version: "1.0"
entity_id: "TERM-ld_course_category-1989"
wp_id: "NOT_APPLICABLE"
type: "taxonomy"
family: "ld_course_category"
current_url: "https://www.mariwork.ir/mag/course-category/free/"
canonical_url: "NOT_AVAILABLE"
workflow_status: CODEX_AUDITED
final_disposition: NOT_DECIDED
blocked: false
blockers: []
---

# Page Dossier — TERM-ld_course_category-1989

## 0. State

- Workflow status: CODEX_AUDITED
- Final disposition: NOT_DECIDED

## 1. Identity

- Entity: TERM-ld_course_category-1989
- Current URL: https://www.mariwork.ir/mag/course-category/free/
- Canonical: NOT_AVAILABLE

## 2. URL History

Round-1 evidence only.

## 3. Baseline

- Source: supplied deterministic Round-1 page evidence; observed 2026-09-24T16:05:27Z.
- Search Console / Coverage / Page+Query: NOT_AVAILABLE in supplied batch; Page-query relationship is not proven by the current export.
- Task context: Autonomous Round-1 low-cost batch first-pass; no taxonomy-specific task ID was supplied.

## 4. Current Page Snapshot

- HTTP / redirect: `404`; no redirect; final URL is unchanged.
- Index signals: `follow, noindex`; X-Robots `NOT_AVAILABLE`; canonical absent; not present in observed sitemaps.
- Metadata/content: title `Page Not Found - رنگ پارچه ماری ورک`; meta description absent; H1 `اوه! این صفحه پیدا نمی‌شود.`; no parsed schema types.
- Body is a generic 404 shell with shared navigation/footer; taxonomy archive content is not observable in supplied initial HTML.
- Images: 2 reported, 0 missing ALT; supplied samples are the site logo SVG. Internal links: 96 reported.

## 5. Search / Content Research

- Primary intent: UNKNOWN_NEEDS_VERIFICATION because the live URL returns a generic 404.
- Query/page evidence: NOT_AVAILABLE; no Page+Query relation is established.
- Whether this term should be restored, replaced, or intentionally retired is unresolved; no destination is inferred from the slug.

## 6. Codex Audit

- Mode: READ-ONLY

### Findings

#### TERM-ld_course_category-1989-F001 — Taxonomy URL returns an unresolved 404

```yaml
id: TERM-ld_course_category-1989-F001
severity: P1
scope: PAGE
status: CONFIRMED
evidence_class: OBSERVED
confidence: HIGH
source_refs:
  - REST:https://www.mariwork.ir/wp-json/wp/v2/ld_course_category:id=1989
  - LINK:https://www.mariwork.ir/mag/course-category/free/
  - supplied_page_evidence:observed_at=2026-09-24T16:05:27Z
  - SYS-003
impact: The taxonomy archive is unavailable as a 404; its intended lifecycle, replacement relationship, and historical value are not established.
recommendation: INITIAL — verify lifecycle and historical/internal-link value, then decide restore, direct relevant redirect, or removal only with evidence. Do not map by slug similarity alone and do not implement in Round 1.
acceptance_criteria: Current taxonomy state, exact destination or no-replacement rationale, redirect/canonical behavior, historical signals, internal-link cleanup, Rank Math ownership, and regression checks are documented and Second Reviewed before change.
google_basis: GOOGLE_CONSISTENT
google_reference: https://developers.google.com/search/docs/crawling-indexing/301-redirects
seo_owner_current: UNKNOWN_NEEDS_VERIFICATION
seo_owner_target: RANK_MATH if verified capability covers taxonomy controls; otherwise UNKNOWN_NEEDS_VERIFICATION
rank_math_capability_checked: BLOCKED_BY_ACCESS
rank_math_path_or_reason_not_used: Installed version/modules and current owner were not supplied; no Production access or write was performed.
```

**Evidence:** HTTP 404, no redirect, unchanged final URL, `follow, noindex`, no canonical, no X-Robots value, absent from observed sitemaps, generic 404 H1/body, and no schema types.

**Impact:** The archive cannot be evaluated as an accessible taxonomy page; final disposition remains unresolved.

**Recommendation:** Initial evidence-gathering and lifecycle decision only; no redirect, canonical, robots, sitemap, or content change is authorized.

**Acceptance criteria:** See finding YAML; independently verify taxonomy state and Rank Math ownership before any implementation decision.

**Systemic reference:** `SYS-003`.

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

- Google basis: `GOOGLE_CONSISTENT`; [Google Search Central — Redirects](https://developers.google.com/search/docs/crawling-indexing/301-redirects).
- Current owner: `UNKNOWN_NEEDS_VERIFICATION`; target owner: `RANK_MATH` where verified capability applies.
- Rank Math capability check: `BLOCKED_BY_ACCESS`.
- Lifecycle ceiling: `CODEX_AUDITED`; initial recommendation only.
