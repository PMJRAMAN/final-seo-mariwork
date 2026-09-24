# Systemic Findings Registry

فقط findings با scope `FAMILY` یا `SITEWIDE`.

## Status
OPEN / INVESTIGATING / APPROVED / IMPLEMENTING / RESOLVED / REJECTED

## Template

### SYS-XXX — Title

```yaml
scope: FAMILY|SITEWIDE
family:
severity: P0|P1|P2|P3
status:
evidence_class:
confidence:
first_seen:
related_pages:
change_ref:
```

**Evidence**

**Root cause hypothesis / confirmed cause**

**Impact**

**Recommendation**

**Acceptance criteria**

**History**

## Round-1 A-013 registrations

### SYS-001 — Rank Math configuration and SEO ownership cannot be verified

```yaml
id: SYS-001
severity: P1
scope: SITEWIDE
status: BLOCKED
evidence_class: OBSERVED
confidence: HIGH
first_seen: 2026-09-24
related_pages: A-013
change_ref: NOT_APPLICABLE_ROUND1
source_refs: [data/normalized/round1-foundation-context.json, audits/sitewide/A-010-inventory-notes.md]
impact: Current owners and settings for robots, canonical, metadata, schema, sitemap, redirects, and taxonomy controls are not verified.
recommendation: INITIAL — verify installed Rank Math version/modules/settings/hooks in A-014/A-015; use Rank Math where capability is verified and avoid parallel output.
acceptance_criteria: One evidenced owner per concern, conflicts enumerated, rollback and regression set defined before any approved change.
google_basis: GOOGLE_CONSISTENT
google_reference: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
seo_owner_current: UNKNOWN_NEEDS_VERIFICATION
seo_owner_target: RANK_MATH where capability is verified; otherwise UNKNOWN_NEEDS_VERIFICATION
rank_math_capability_checked: BLOCKED_BY_ACCESS
rank_math_path_or_reason_not_used: Configuration and code paths inaccessible; no alternate owner selected.
```

### SYS-002 — Product Tag and Blog Tag archives are decommission candidates with unresolved migration risk

```yaml
id: SYS-002
severity: P1
scope: FAMILY
family: product_tag + post_tag
status: CONFIRMED
evidence_class: OBSERVED
confidence: HIGH
first_seen: 2026-09-24
related_pages: A-013, TERM-product_tag, TERM-post_tag
change_ref: NOT_APPLICABLE_ROUND1
source_refs: [data/normalized/round1-foundation-context.json, data/normalized/round1-page-evidence.jsonl, audits/sitewide/A-010-inventory-notes.md]
impact: 275 product-tag rows and 53 post-tag rows are inventoried; sampled product tags are 200/noindex without canonical or H1, while sampled blog tags are 404. Historical value and replacement mapping are unresolved.
recommendation: INITIAL — collect complete family behavior, historical sources, internal links, term assignments, sitemap/canonical/robots evidence, and destination identity before any decommission action.
acceptance_criteria: Approved family migration dossier with exact URL set, evidence-backed mapping/no-replacement outcomes, rollback, canary/regression set, and Second Review.
google_basis: GOOGLE_CONSISTENT
google_reference: https://developers.google.com/crawling/docs/faceted-navigation
seo_owner_current: UNKNOWN_NEEDS_VERIFICATION
seo_owner_target: RANK_MATH for supported controls; CONTENT/PLATFORM only when justified
rank_math_capability_checked: BLOCKED_BY_ACCESS
rank_math_path_or_reason_not_used: Taxonomy settings inaccessible; no production policy proposed.
```

### SYS-003 — Historical/error URL population requires source-level disposition

```yaml
id: SYS-003
severity: P2
scope: SITEWIDE
status: CONFIRMED
evidence_class: MEASURED
confidence: HIGH
first_seen: 2026-09-24
related_pages: A-012, A-013
change_ref: NOT_APPLICABLE_ROUND1
source_refs: [data/normalized/round1-evidence-summary.json, audits/sitewide/A-012-legacy-url-map.md]
impact: 58/501 deterministic entities are 404; 67 GSC source URLs in A-012 terminate at 404, with historical identity/replacement unproven.
recommendation: INITIAL — preserve exact source metrics and resolve source identity before any redirect, restoration, or removal decision; do not bulk-map unrelated URLs.
acceptance_criteria: Each selected source has an evidence-backed disposition or blocker; approved redirects are direct/relevant/canonical-consistent and regression-tested.
google_basis: GOOGLE_CONSISTENT
google_reference: https://developers.google.com/search/docs/crawling-indexing/301-redirects
seo_owner_current: UNKNOWN_NEEDS_VERIFICATION
seo_owner_target: RANK_MATH if supported; otherwise PLATFORM/server owner for HTTP behavior
rank_math_capability_checked: BLOCKED_BY_ACCESS
rank_math_path_or_reason_not_used: Redirect table/server ownership unavailable.
```

### SYS-004 — Initial-HTML SEO output has broad metadata/H1/schema evidence gaps

```yaml
id: SYS-004
severity: P1
scope: SITEWIDE
status: CONFIRMED
evidence_class: MEASURED
confidence: MEDIUM
first_seen: 2026-09-24
related_pages: A-013
change_ref: NOT_APPLICABLE_ROUND1
source_refs: [data/normalized/round1-evidence-summary.json, data/normalized/round1-page-evidence.jsonl]
impact: Evidence summary reports 289 missing meta descriptions, 271 missing H1s, and no parsed schema types; ranking/rich-result causation is not claimed.
recommendation: INITIAL — segment by page family, validate initial/rendered output, and verify one Rank Math/theme/plugin owner per concern.
acceptance_criteria: Family regression set measures title/meta/H1/schema output, visible/schema consistency, ownership, and approved before/after evidence.
google_basis: GOOGLE_CONSISTENT
google_reference: https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
seo_owner_current: UNKNOWN_NEEDS_VERIFICATION
seo_owner_target: RANK_MATH where capable; CONTENT for visible H1/content; otherwise UNKNOWN_NEEDS_VERIFICATION
rank_math_capability_checked: BLOCKED_BY_ACCESS
rank_math_path_or_reason_not_used: Installed modules/template ownership unavailable.
```

### SYS-005 — Facet, sort, pagination, and parameter URL policy is incomplete

```yaml
id: SYS-005
severity: P2
scope: SITEWIDE
status: BLOCKED
evidence_class: OBSERVED
confidence: HIGH
first_seen: 2026-09-24
related_pages: A-013, SPACE-FACETS, SPACE-SORT-DISPLAY, SPACE-PAGINATION
change_ref: NOT_APPLICABLE_ROUND1
source_refs: [data/normalized/round1-foundation-context.json, audits/sitewide/A-010-inventory-notes.md, audits/sitewide/A-012-legacy-url-map.md]
impact: Observed filter/sort/pagination/search/action spaces create multiple URL forms; combinations and generated links were not exhaustively measured.
recommendation: INITIAL — classify each parameter family by user value, crawlable links, canonical/robots behavior, sitemap exclusion, and duplicate difference; do not apply a blanket policy.
acceptance_criteria: Parameter policy covers observed/generated patterns, representative combinations, canonical targets, internal links, and safe regression examples.
google_basis: GOOGLE_CONSISTENT
google_reference: https://developers.google.com/crawling/docs/faceted-navigation
seo_owner_current: UNKNOWN_NEEDS_VERIFICATION
seo_owner_target: RANK_MATH for supported controls; PLATFORM for server controls where required
rank_math_capability_checked: BLOCKED_BY_ACCESS
rank_math_path_or_reason_not_used: Settings unavailable; investigation only.
```

### SYS-006 — Duplicate SEO owner/output risk remains unclosed

```yaml
id: SYS-006
severity: P1
scope: SITEWIDE
status: BLOCKED
evidence_class: INFERRED
confidence: MEDIUM
first_seen: 2026-09-24
related_pages: A-014, A-015, SYS-001
change_ref: NOT_APPLICABLE_ROUND1
source_refs: [data/normalized/round1-foundation-context.json, data/normalized/round1-evidence-summary.json, audits/sitewide/A-010-inventory-notes.md:34,140-147, audits/sitewide/A-013-technical-baseline.md:34,39,44,50-70]
impact: Current source ownership and duplicate-output status for title/meta, canonical, robots, schema, sitemap, and redirects cannot be confirmed. The public sitemap marker attributes output to Rank Math, but exclusive pipeline ownership is not proven; `/shop/` appears in both page and product sitemap outputs.
recommendation: INITIAL — build a concern-by-concern ownership matrix from verified configuration and representative public output. Use Rank Math wherever installed capability supports the concern; do not add or remove competing output until an approved change dossier defines exact scope, rollback, canary, and regression evidence.
acceptance_criteria: Each concern has one evidenced current owner, one target owner, output location, Rank Math capability/module path, conflict status, and representative regression tests; sitemap membership and redirect chains are separately validated.
google_basis: GOOGLE_CONSISTENT
google_reference: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
seo_owner_current: UNKNOWN_NEEDS_VERIFICATION
seo_owner_target: RANK_MATH where capability is verified; PLATFORM for server-only redirect behavior; otherwise UNKNOWN_NEEDS_VERIFICATION
rank_math_capability_checked: BLOCKED_BY_ACCESS
rank_math_path_or_reason_not_used: Production configuration, hooks, theme/custom-plugin code, redirect table, and server configuration are inaccessible; no broader access requested.
```
