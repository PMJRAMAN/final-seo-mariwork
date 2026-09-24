# Systemic Findings Registry

**Round-1 scope:** A-013 + A-018/A-019/A-020 · **Lifecycle ceiling:** CODEX_AUDITED

Only FAMILY and SITEWIDE findings belong here. All recommendations are INITIAL; none is Second Reviewed, Approved, Implementing or a Production instruction.

## Registry

### SYS-001 — Rank Math configuration and SEO ownership cannot be verified

id: SYS-001
severity: P1 · scope: SITEWIDE · status: BLOCKED · evidence_class: OBSERVED · confidence: HIGH
source_refs: foundation context; A-010; A-013.
impact: Current owners/settings for title, meta, robots, canonical, schema, sitemap, redirects and taxonomy controls are unverified.
recommendation: INITIAL — verify installed Rank Math version/modules/settings/hooks and one owner per concern before any SEO-control change.
acceptance_criteria: Capability, current/target owner, conflicts, rollback and regression set are evidenced.
google_basis: GOOGLE_CONSISTENT · google_reference: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
seo_owner_current: UNKNOWN_NEEDS_VERIFICATION · seo_owner_target: RANK_MATH where verified; otherwise UNKNOWN_NEEDS_VERIFICATION
rank_math_capability_checked: BLOCKED_BY_ACCESS · rank_math_path_or_reason_not_used: Production configuration/code inaccessible.

### SYS-002 — Product Tag and Blog Tag archives are decommission candidates with unresolved migration risk

id: SYS-002 · severity: P1 · scope: FAMILY · family: product_tag + post_tag · status: CONFIRMED · evidence_class: OBSERVED · confidence: HIGH
source_refs: foundation context; A-011; page evidence; A-012.
impact: 275 product-tag and 53 post-tag rows; sampled product tags are 200/noindex without canonical/H1 and sampled blog tags are 404. Historical value, assignments, links and replacements unresolved.
recommendation: INITIAL — separate Product Tag and Blog Tag migration dossiers; inventory exact URLs, assignments, status/canonical/robots, sitemap, historical metrics and destinations before action.
acceptance_criteria: Complete family set, evidence-backed mapping/no-replacement outcomes, rollback, canary/regression set and Second Review.
google_basis: GOOGLE_CONSISTENT · google_reference: https://developers.google.com/crawling/docs/faceted-navigation
seo_owner_current: UNKNOWN_NEEDS_VERIFICATION · seo_owner_target: RANK_MATH for supported controls; CONTENT/PLATFORM only when justified
rank_math_capability_checked: BLOCKED_BY_ACCESS · rank_math_path_or_reason_not_used: Taxonomy settings/capability inaccessible.

### SYS-003 — Historical/error URL population requires source-level disposition

id: SYS-003 · severity: P2 · scope: SITEWIDE · status: CONFIRMED · evidence_class: MEASURED · confidence: HIGH
source_refs: round1 evidence summary; A-012; gsc-pages.
impact: 58/501 deterministic entities are 404; 67 GSC sources in A-012 end at 404; identity/replacement unresolved.
recommendation: INITIAL — reconcile exact source identity and intent before redirect, restoration or removal; do not infer by slug similarity or transfer metrics.
acceptance_criteria: Selected sources receive evidence-backed disposition or blocker; approved redirects are direct, relevant and canonical-consistent.
google_basis: GOOGLE_CONSISTENT · google_reference: https://developers.google.com/search/docs/crawling-indexing/301-redirects
seo_owner_current: UNKNOWN_NEEDS_VERIFICATION · seo_owner_target: RANK_MATH if supported; otherwise PLATFORM/server owner
rank_math_capability_checked: BLOCKED_BY_ACCESS · rank_math_path_or_reason_not_used: Redirect table/server ownership unavailable.

### SYS-004 — Initial-HTML SEO output has broad metadata/H1/schema evidence gaps

id: SYS-004 · severity: P1 · scope: SITEWIDE · status: CONFIRMED · evidence_class: MEASURED · confidence: MEDIUM
source_refs: round1 evidence summary; page evidence.
impact: 289 missing meta descriptions, 271 missing H1s and no parsed schema types; ranking/rich-result causation is not claimed.
recommendation: INITIAL — segment by family, validate initial/rendered output and verify one Rank Math/theme/plugin owner per concern.
acceptance_criteria: Family regression set measures title/meta/H1/schema, visible/schema consistency, ownership and before/after evidence.
google_basis: GOOGLE_CONSISTENT · google_reference: https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
seo_owner_current: UNKNOWN_NEEDS_VERIFICATION · seo_owner_target: RANK_MATH where capable; CONTENT for visible H1/content
rank_math_capability_checked: BLOCKED_BY_ACCESS · rank_math_path_or_reason_not_used: Modules/template ownership unavailable.

### SYS-005 — Facet, sort, pagination and parameter URL policy is incomplete

id: SYS-005 · severity: P2 · scope: SITEWIDE · status: BLOCKED · evidence_class: OBSERVED · confidence: HIGH
source_refs: foundation context; A-010; A-012.
impact: Machine URL spaces create multiple forms; sampled volume filter returned 200 and canonicalized to /shop/, but combinations were not exhaustive.
recommendation: INITIAL — classify each parameter family by value, crawlable links, canonical/robots, sitemap exclusion and content difference; avoid blanket policy.
acceptance_criteria: Policy covers observed/generated patterns, representative combinations, canonical targets, links and regression examples.
google_basis: GOOGLE_CONSISTENT · google_reference: https://developers.google.com/crawling/docs/faceted-navigation
seo_owner_current: UNKNOWN_NEEDS_VERIFICATION · seo_owner_target: RANK_MATH for supported controls; PLATFORM for server controls
rank_math_capability_checked: BLOCKED_BY_ACCESS · rank_math_path_or_reason_not_used: Settings unavailable.

### SYS-006 — Duplicate SEO owner/output risk remains unclosed

id: SYS-006 · severity: P1 · scope: SITEWIDE · status: BLOCKED · evidence_class: INFERRED · confidence: MEDIUM
source_refs: foundation context; evidence summary; A-014; A-015.
impact: Exclusive ownership for title/meta, canonical, robots, schema, sitemap and redirects is unproven; /shop/ appears in page and product sitemap outputs.
recommendation: INITIAL — create a concern-by-concern ownership matrix from verified configuration and public output; do not add competing output.
acceptance_criteria: Each concern has current/target owner, output location, Rank Math path, conflict status and regression test.
google_basis: GOOGLE_CONSISTENT · google_reference: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
seo_owner_current: UNKNOWN_NEEDS_VERIFICATION · seo_owner_target: RANK_MATH where verified; PLATFORM for server-only redirects
rank_math_capability_checked: BLOCKED_BY_ACCESS · rank_math_path_or_reason_not_used: Configuration, hooks, redirect table and server config inaccessible.

### SYS-007 — Query-to-page attribution and intent targeting are unproven

id: SYS-007 · severity: P1 · scope: SITEWIDE · status: BLOCKED · evidence_class: OBSERVED · confidence: HIGH
source_refs: A-016; A-017; strategy/QUERY-MAP.md.
impact: Page importance and family themes are available, but query ownership by product/category/Academy/article is not proven.
recommendation: INITIAL — obtain joined Page+Query or direct filtered evidence; use the family map for research only until then.
acceptance_criteria: Every approved query target has joined evidence or documented SERP/intent research, with overlap and legacy identity reviewed.
google_basis: PROJECT_DECISION · google_reference: https://support.google.com/webmasters/answer/7576553
seo_owner_current: NOT_APPLICABLE_CONTENT_RESEARCH · seo_owner_target: CONTENT after Second Review
rank_math_capability_checked: NOT_APPLICABLE_FOR_ATTRIBUTION · rank_math_path_or_reason_not_used: Attribution is an evidence problem, not metadata implementation.

### SYS-008 — Internal-link architecture and title naming conventions are inconsistent/unverified

id: SYS-008 · severity: P2 · scope: FAMILY · family: products + categories + academy + articles · status: OPEN · evidence_class: MEASURED · confidence: MEDIUM
source_refs: page evidence; strategy/CONTENT-ARCHITECTURE.md; foundation context.
impact: Shared navigation exists but cross-family relevance/coverage is unmeasured. Titles/H1s vary in brand presence, separators, code digits and volume placement across colors, sets, mediums and tools.
recommendation: INITIAL — build link requirement and title-pattern inventories, then Second Review CORE/FAMILY-SPECIFIC/CONTEXTUAL rules. Do not mass-add links or rename in Round 1.
acceptance_criteria: Complete-family inventory identifies links, bidirectional destinations, title tokens, exceptions, legacy history and regression set; approved changes use a dossier.
google_basis: GOOGLE_CONSISTENT · google_reference: https://developers.google.com/search/docs/fundamentals/seo-starter-guide
seo_owner_current: CONTENT/UNKNOWN_NEEDS_VERIFICATION for visible titles/links; metadata owner UNKNOWN_NEEDS_VERIFICATION
seo_owner_target: CONTENT for visible policy; RANK_MATH for approved title/meta output where capable
rank_math_capability_checked: BLOCKED_BY_ACCESS · rank_math_path_or_reason_not_used: Installed capability/current owner unavailable.

### SYS-009 — Product-category sitemap membership and indexability policy are unresolved

id: SYS-009 · severity: P1 · scope: FAMILY · family: product_cat · status: BLOCKED · evidence_class: OBSERVED · confidence: HIGH
source_refs: batch TERM-product_cat-1902/1991/1992/1993/220/28 supplied evidence; MASTER-TODO B7.
impact: All six sampled category URLs return 200 with `index, follow` and self-canonical signals, but are marked `NOT_PRESENT_IN_OBSERVED_SITEMAPS`; intended indexability and complete sitemap membership are not verified.
recommendation: INITIAL — verify the complete sitemap set, Coverage/URL Inspection and taxonomy policy; then document the family decision and Rank Math owner before any inclusion, exclusion or robots/canonical change.
acceptance_criteria: Family policy records intended indexability, current sitemap membership, canonical/robots output, source evidence, Rank Math capability/owner, and a regression set; no Production change occurs before approval.
google_basis: GOOGLE_CONSISTENT · google_reference: https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview
seo_owner_current: UNKNOWN_NEEDS_VERIFICATION · seo_owner_target: RANK_MATH where supported; otherwise documented owner
rank_math_capability_checked: BLOCKED_BY_ACCESS · rank_math_path_or_reason_not_used: Production configuration and installed modules unavailable.

### SYS-010 — Article image ALT coverage gaps in supplied batch

id: SYS-010 · severity: P2 · scope: FAMILY · family: articles · status: OPEN · evidence_class: MEASURED · confidence: HIGH
source_refs: Round-1 supplied evidence for WP-13295, WP-13305, WP-13312, WP-13316, WP-13318, WP-13320, WP-22192, WP-22193, WP-22194, WP-22196, WP-22197, WP-26387.
impact: The supplied batch reports 83 images missing ALT out of 133 images; image purpose and decorative status were not independently inspected.
recommendation: INITIAL — review article images as a family, assign descriptive ALT only when the image conveys useful page information, and retain empty ALT for decorative images; do not invent image facts.
acceptance_criteria: Article-family regression sample records each image's meaningful/decorative decision, ALT output, and no duplicate or invented descriptions.
google_basis: GOOGLE_RECOMMENDED · google_reference: https://developers.google.com/search/docs/appearance/google-images
seo_owner_current: CONTENT/UNKNOWN_NEEDS_VERIFICATION · seo_owner_target: CONTENT for image ALT decisions; RANK_MATH only for metadata concerns it actually owns
rank_math_capability_checked: BLOCKED_BY_ACCESS · rank_math_path_or_reason_not_used: Rank Math configuration and image/template ownership unavailable.

## Handoff

Product Tags and Blog Tags remain family-level migration programs. Query targets, title standard, internal-link rules and technical policies remain initial candidates or blockers. No finding authorizes Production, database, WordPress, WooCommerce, Rank Math, sitemap, redirect, taxonomy or raw-export writes.
