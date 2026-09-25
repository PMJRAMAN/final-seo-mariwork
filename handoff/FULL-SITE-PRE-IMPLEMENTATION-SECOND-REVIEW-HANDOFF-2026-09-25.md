# Full-Site Pre-Implementation Second Review Handoff

**Date:** 2026-09-25
**Lifecycle:** `CODEX_AUDITED`
**Mode:** Audit/reconciliation only
**Production writes:** `0`
**Implementation authorized:** `NO`
**Approval state:** `PENDING CHATGPT/HUMAN SECOND REVIEW`

## A. Coverage

- Current public entities: **502** = 147 public posts/entities + 355 taxonomy terms.
- Inventory: 555 rows = 530 entity/current-target or unresolved-URL rows + 25 URL-space policy rows; 2,104 observed URL spellings are preserved in A-010 evidence.
- Existing individual dossiers reused: **168** (`CODEX_AUDITED`), including 84 products after the WP-27727 supplemental dossier.
- New dossiers created: **3** — WP-10 Checkout, WP-11 My Account, WP-30919 Cart.
- Family/policy evidence reused: Store SR-002/SR-003/SR-004, current SEO output, migration reconciliation, URL-space inventory, current Academy architecture, image findings and Store internal-link graph.
- Family-level closure artifacts created: coverage matrix, system URL-space closure, image/ALT summary and draft cross-family link requirement matrix.
- No Round-1 dossier was duplicated or rewritten from zero.

Primary reconciliation artifact: `audits/sitewide/PRE-IMPLEMENTATION-COVERAGE-MATRIX.json`.

## B. Family readiness

| Family | Status | Evidence / note |
|---|---|---|
| Store | `READY_FOR_SECOND_REVIEW` | Shop, 84 products, categories, tags, `pa_volume`, variants, bundles, parameters, titles/H1 and graph are covered. SR-004 is pending human approval. |
| Homepage | `READY_FOR_SECOND_REVIEW` | `pages/homepage/WP-63.md`; current SEO output now reconciles the old parser/schema/Rank Math uncertainty. Independent intent review remains pending. |
| Static/Core | `READY_FOR_SECOND_REVIEW` | Ten editorial/core dossiers reused; WP-10/11/30919 are separated as system-commerce pages. |
| Articles | `READY_FOR_SECOND_REVIEW` | Twelve dossiers and current article schema/output evidence reused. Page+Query attribution remains unavailable; freshness and image-purpose review remain human review items. |
| Blog Categories | `READY_FOR_SECOND_REVIEW` | Twelve dossiers plus current category matrix: two non-empty/indexable, nine empty 200/noindex, one 404. Lifecycle decision remains pending. |
| Blog Tags | `READY_FOR_SECOND_REVIEW` | 54 terms, 6 assigned terms and 39 assignments; family-level migration evidence is sufficient for review, but destination mapping is unresolved. |
| Academy/Courses/Lessons | `READY_FOR_SECOND_REVIEW` | One course, 37 lessons, Academy archive/course dossiers and current hierarchy reused. Historical `/education/` mapping: 36 partial, 5 unknown; no broad lesson re-audit is needed. |
| LearnDash taxonomies | `READY_FOR_SECOND_REVIEW` | Two Course Category dossiers and current Academy reconciliation reused. |
| Product taxonomies | `READY_FOR_SECOND_REVIEW` | Seven durable Product Category dossiers; two migration-era categories and three `pa_volume` terms handled by family evidence; 275 Product Tags are policy-level. |
| System URLs | `READY_FOR_SECOND_REVIEW` | Three new WooCommerce system dossiers plus grouped policy for search, auth, archives, feeds, attachments, pagination, facets and 404s. No authenticated/transactional test. |
| Historical/legacy URLs | `PARTIAL — TARGETED EVIDENCE NEEDED` | A-012 and migration maps preserve transport/history. 68 volume mappings are partial and 14 unknown; redirects do not prove semantic identity. |
| Images/ALT | `PARTIAL — TARGETED EVIDENCE NEEDED` | Measured candidate gaps are recorded; visual informative/decorative classification is not complete. No ALT write performed. |

## C. Outstanding blockers

Only the following remain active blockers or decision gates:

1. **Page+Query dataset unavailable.** `Page-query relationship is not proven by the current export.` Separate `Pages.csv` and `Queries.csv` were not joined.
2. **Human Second Review and approval are pending.** No target-state recommendation in this handoff authorizes Production.
3. **Historical identity/migration mappings remain incomplete.** Transport redirects are preserved without semantic equivalence claims.
4. **Image/ALT visual review remains incomplete.** Counts alone do not identify informative versus decorative images.
5. **System-state validation is intentionally limited.** No login, cart mutation, checkout submission, order, customer or authenticated test was performed.
6. **Inventory dispositions remain `NOT_DECIDED`.** This task adds coverage classification; it does not assign final `OPTIMIZE`, `KEEP_AS_IS`, `NOINDEX`, `REDIRECT`, `CANONICALIZE` or `REMOVE_410` decisions.
7. **Autonomous runner deployment remains blocked by A-009 runtime isolation.** This manual closure used existing repository evidence and read-only checks; it did not resume autonomous execution.

Previously resolved evidence limitations, such as the old Rank Math/Yoast interpretation and Round-1 parser schema gap, are not treated as active blockers for review. Current Rank Math Free `1.0.279`, active modules and current public schema/output evidence are recorded in the Second Review evidence set.

## D. Cross-family architecture

### Intended roles

- Homepage: brand/entity gateway and navigation hub.
- Shop and durable Product Categories: commercial discovery and comparison.
- Products, sets, bundles, mediums and tools: transactional decisions based on verified Woo/YITH facts.
- Academy, courses and lessons: structured instruction and learning progression.
- Magazine, Articles and durable Blog Categories: reference, comparison and answer-oriented content.
- Static/Core pages: trust, communication, FAQ and support tasks.
- Cart, Checkout and My Account: utility/system endpoints, not editorial targets.
- Product Tags and Blog Tags: transitional taxonomy spaces, not durable content hubs.

### Draft link relationships

`strategy/INTERNAL-LINK-REQUIREMENT-MATRIX-DRAFT.md` defines candidate:

- `CORE_MANDATORY` — applicable parent/hierarchy/navigation relationships;
- `FAMILY_SPECIFIC` — real material, technique, volume, component or learning relationships;
- `CONTEXTUAL_OPTIONAL` — only when the visible topic and user task justify the link.

Major opportunities are Article → Product/Category, Academy/Lesson → Product/Category when materials are actually used, Category → relevant learning content, and consistent Course/Lesson hierarchy. No mass keyword auto-linking is proposed. The Store graph's 13,668 unresolved destinations are resolver gaps, not a broken-link count.

## Homepage Second Review handoff

Review `pages/homepage/WP-63.md` with current evidence in `audits/second-review/evidence/current-seo-output.jsonl` and `seo-ownership-matrix.json`.

- Current public state: 200, self-canonical, index/follow, one H1, sitemap membership and visible links to Store/Magazine/Academy.
- Current structured-data output is now evidenced as `ImageObject`, `Organization`, `SearchAction`, `WebPage`, `WebSite`; the old empty-parser observation is superseded for current state but remains in dossier history.
- Decide homepage role and cross-family link requirements.
- Do not infer query ownership or approve schema/title/content changes from this handoff.

## Static/Core grouped Second Review handoff

Review the ten existing editorial/core dossiers as a group. Exceptions:

- WP-10, WP-11 and WP-30919 are system-commerce dossiers and should not receive editorial copy recommendations.
- Login/utility pages and policies require intended-indexability decisions, not generic landing-page optimization.
- Existing Round-1 findings that assumed missing Rank Math/schema evidence must be reconciled against current output evidence before being retained.

## Article grouped Second Review handoff

Review the 12 article dossiers with category matrix, current BlogPosting output and SYS-010 image evidence.

- Confirm article versus Academy intent boundaries.
- Confirm factual freshness/accuracy candidates only where evidence supports them.
- Review Article → Product/Category links contextually; do not infer query targets.
- Review 83/133 measured missing-ALT candidates visually before any content task.
- Keep the Page+Query limitation explicit.

## E. Recommended Second Review queue

1. Review foundation/current-state interpretation and the `SYS-001`–`SYS-015` reconciliation boundaries.
2. Review Store SR-004 recommendations already prepared; do not redo Store discovery.
3. Review Homepage and Static/Core group, including the three system-commerce exceptions.
4. Review Articles and Blog Categories together, then Blog Tags as a family migration policy.
5. Review Academy/Course/Lesson hierarchy and the unresolved historical `/education/` mappings.
6. Review Product Category, `pa_volume` and Product Tag family policy.
7. Review the draft Internal Link Requirement Matrix and cross-family role model.
8. Review image/ALT candidate scope and define the human visual-review sample.
9. Record human decisions as `CONFIRM / MODIFY / REJECT / NEEDS_MORE_EVIDENCE`; only then create implementation tasks/change dossiers for approved items.

## Authority boundary

This handoff does not assign `SECOND_REVIEWED`, `APPROVED`, `FINAL_QA_PASSED` or any Production disposition. Production writes executed during this task: **0**.
