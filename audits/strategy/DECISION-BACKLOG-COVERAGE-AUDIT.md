# P-001 — Decision Backlog Coverage Audit

**Date:** 2026-09-25
**Repository HEAD before audit:** `387cedb` (`387cedb` is the fast-forwarded `main` baseline)
**Branch:** `main`
**Mode:** `REPOSITORY AUDIT / PRODUCTION READ-ONLY`
**Lifecycle authority:** `CODEX_AUDITED`
**Production writes:** `0`
**Authoritative files changed:** none

## 1. Executive verdict

**`NOT_READY_FOR_FREEZE`**

The current Decision Backlog is a useful first governance layer, but it is not yet safe to use as the only unlock source for all future implementation packages. The repository contains material choices that are only implicit in broad decisions or accepted process rules, and several existing decisions combine independently selectable policies. The gap is governance coverage, not an instruction to implement any SEO change.

The decision count is **73** (`DEC-001` through `DEC-073`): 32 `OPEN`, 27 `PROPOSED`, 11 `NEEDS_TARGETED_EVIDENCE`, and 3 `DEFERRED`; none is `ACCEPTED`. Freeze is therefore not implied by the current status table.

### Freeze blockers

1. Sitewide URL normalization/canonical architecture is not represented by an atomic target-state decision.
2. Product identity and commercial-fact source-of-truth rules are not explicit enough for schema/feed/visible-output implementation.
3. Product lifecycle decisions for out-of-stock versus discontinued entities and future slug/URL changes are absent.
4. Image and video strategy documents contain material target-state dimensions not represented by atomic decisions; `DEC-058` also overlaps `DEC-038`.
5. Brand facts/naming and branded landing/monitoring decisions are broader or less explicit than the Brand/Entity strategy requires.
6. Monitoring/rollout policy is mixed into broad items and does not yet express baseline/change annotation versus success/iterate/rollback interpretation.
7. Existing EXE packages omit a material rollout dependency for 15 packages, listed in §12.

These blockers do not authorize a backlog edit. They are proposals for ChatGPT P-002 and the owner.

## 2. Method and evidence boundary

The audit used deterministic repository inspection followed by classification. It did not recrawl Production and did not query or write WordPress, WooCommerce, Rank Math, the database, caches, redirects, sitemap configuration or server files.

Evidence reused:

- `strategy/DECISION-BACKLOG.md` and `tasks/EXECUTION-BACKLOG.md`;
- `MASTER-TODO.md`, all required workflow/spec/ownership documents and the decision-to-execution governance document;
- all canonical page dossiers under `pages/**` (171 dossier files after excluding `pages/README.md`);
- current census: 502 public entities (147 posts/entities + 355 taxonomy terms), 19 non-public relevant posts;
- current families: 84 products, 13 pages, 12 articles, 1 course, 37 lessons, 12 Blog Categories, 54 Blog Tags, 9 Product Categories, 275 Product Tags, 3 `pa_volume` terms and 2 LearnDash Course Categories;
- SR-004, SR-005, current Store/Academy reconciliation, system URL closure, image/ALT summary and prior coverage matrix;
- `registry/SYSTEMIC-FINDINGS.md` through `SYS-018`;
- current strategy documents for content, query, links, images, video, Brand/Entity and External PR.

Page dossiers were parsed for finding headings, `NOT_DECIDED`, `BLOCKED`, `TBD`, `UNKNOWN_NEEDS_VERIFICATION`, target-state and owner references. This preserves dossier history; it does not turn historical Round-1 observations into current decisions.

## 3. Source coverage summary

The machine-readable row-level matrix is `audits/strategy/decision-source-coverage-matrix.json`. Every row has one primary classification from the P-001 contract.

| Source class | Coverage result | Main conclusion |
|---|---:|---|
| MASTER-TODO Programs A–P | Partial | Audit/inventory and implementation/QA items are distinguishable, but material policy items in URL normalization, product facts/lifecycle, media, Brand/Entity, monitoring and deferred expansion need explicit mapping or candidate decisions. |
| `SYS-001`–`SYS-018` | Covered with corrections | Current-state supersessions are respected. `SYS-001`, `SYS-004`, `SYS-006` and parts of `SYS-009` are not treated as unresolved current Store facts where SR-004/SR-005 superseded them; active migration, image, system, schema and evidence limitations remain mapped. |
| SR-004 `SR-ST-001`–`SR-ST-011` | Covered | Store recommendations map to existing DEC IDs, accepted rules, or explicit evidence/approval gates. No Store discovery was repeated. |
| SR-005 sections and findings | Covered with gaps | All material sections map to decisions/rules; Static schema, LearnDash ownership, `pa_volume`, Blog lifecycle, image review and historical mapping remain target-state gates. |
| Technical audit specification | Partial | Crawl/index, sitemap, parameter, schema, Woo and ownership domains map, but URL normalization, canonical architecture and JS/AJAX discoverability need atomic decisions. |
| Content research specification | Partial | Intent, boundaries, titles/meta, freshness and links map; editorial provenance, FAQ semantics, location/NAP and informational CTA policy are not atomic enough. |
| Visual/Image strategy | Partial | ALT and review sampling map; filename, representative/gallery/reuse, context/discovery and technical delivery do not have independent target-state coverage. |
| Video strategy | Partial | VideoObject eligibility maps to `DEC-038`; `DEC-058` is too broad and overlaps it; host-page, metadata/thumbnail/transcript and orphan/link policy need separate coverage. |
| Brand/Entity strategy | Partial | `DEC-053` is too broad; facts, naming, branded landing/monitoring and off-site verification need clearer atomic coverage. |
| External PR / Merchant / Reviews | Intentionally deferred with child-gap warning | `DEC-071`–`DEC-073` may remain deferred for unrelated work, but Merchant/feed and genuine-review policies must be split before those programs can unlock implementation. |
| Current durable families | Partial | Current families have evidence and family-level roles, but several applicable dimensions remain dependent on the missing candidates below. |
| Execution Backlog | Dependency gaps | 15 existing EXE rows omit a material rollout/decision dependency; no item is unlocked and no status is changed. |

## 4. Material missing-decision candidates

The proposal file contains the full `CAND-*` records. The count of **missing decision candidates is 27** and counts only `ADD` candidates; it does not silently allocate authoritative `DEC-###` IDs.

| Candidate area | Why it is material |
|---|---|
| Preferred host/protocol, trailing slash and future URL normalization | A cross-family canonical/redirect target cannot be inferred from individual parameter or migration decisions. |
| Sitewide canonical/duplicate architecture | Current decisions cover selected Store parameters and migrations, not the sitewide target relationship between alternate URL spaces and canonical entities. |
| Critical JS/AJAX discoverability | The technical spec treats initial HTML, rendered content and crawlable links as a sitewide domain, but no target policy is represented. |
| Product identity source of truth | SKU/GTIN/MPN/brand source must be decided before Product/Offer/variant schema or feed work. |
| Product commercial-fact source of truth | Visible price, sale/discount, currency and availability need one authoritative source/consistency rule. |
| Out-of-stock versus discontinued lifecycle | This affects indexability, schema availability, internal links and migration disposition independently of title/schema policy. |
| Future product slug/URL lifecycle | Existing legacy rules do not state the future URL/slug policy for new changes while preserving history. |
| Editorial provenance | Author/reviewer/date/source/citation requirements are not fully represented by the article update rule. |
| FAQ visible content versus schema boundary | Static content and generic page schema decisions do not explicitly govern whether FAQ semantics are visible-content-only or structured-data eligible. |
| Stores/location/NAP role | The Stores page has an independent trust/location decision beyond generic static-page content. |
| Informational CTA/commerciality policy | Article/Academy → Product links are covered, but when a commercial CTA is appropriate is not an explicit content policy. |
| Image filename/media naming | Required by the image strategy and L-program, absent from the current decision set. |
| Representative image/gallery/reuse policy | Primary image, gallery consistency and duplicate/reused image handling are independently selectable. |
| Image context/linked-image/discovery policy | Captions/surrounding context, linked-image behavior and image discovery/sitemap treatment need a target rule. |
| Image technical delivery policy | Dimensions, formats, `srcset`, lazy loading and LCP/performance treatment are not covered by an image target decision. |
| Video host-page/fetchability/prominence | VideoObject eligibility alone does not decide whether a video is sufficiently visible, discoverable or correctly hosted. |
| Video metadata/thumbnail/transcript policy | Title/description, thumbnail, transcript/summary and key instructional text are separate target choices. |
| Video duplicate/orphan/internal-link lifecycle | Duplicate, weak, orphaned and cross-family video relationships need an explicit disposition policy. |
| Canonical brand facts and naming consistency | `DEC-053` combines factual registry, trust content and brand strategy; the facts/naming source needs its own gate. |
| Branded query/landing-page and monitoring policy | Branded search targets and monitoring are not the same decision as factual content/schema. |
| Verified off-site entity references | Off-site reference opportunities require a fact-verification boundary before PR or entity implementation. |
| Monitoring baseline/change annotation | Measurement requires explicit release isolation, affected scope and baseline-window policy before attribution or rollback discussion. |
| Monitoring success/iterate/rollback interpretation | Cadence and metrics alone do not state what evidence permits KEEP, ITERATE or ROLLBACK-CANDIDATE. |
| Maintenance triggers | Rank Math/plugin updates, Google documentation changes, new URLs/404s, systemic findings and freshness queues need a durable triage policy. |
| Merchant Center / feed program entry and eligibility | `DEC-072` combines a deferred opportunity review with a future implementation program gate. |
| Product feed identity/variant/data consistency | External feed identity, price, availability, image and landing-page consistency needs a child decision separate from on-site schema. |
| Genuine reviews/social-proof collection/display/schema | `DEC-073` does not atomically decide collection, display, eligibility or schema boundaries. |

## 5. Over-broad decisions needing split or rewording

The count is **9**. These are not rejected decisions; they are candidates for making the target state discussable without silently choosing several unrelated policies.

| Decision | Concern | Proposed treatment |
|---|---|---|
| `DEC-004` | Login, Fast Buy, Cart, Checkout and My Account have different state/privacy/transport behavior. | Split by system-policy family or retain a parent with explicit child exceptions. |
| `DEC-016` | Product Category, Shop and volume landing metadata are independent family strategies. | Split family metadata decisions under a common metadata rule. |
| `DEC-053` | Brand/trust content, canonical facts, schema, branded search and entity references are distinct choices. | Split facts/naming, site content/schema, branded landing/monitoring and off-site references. |
| `DEC-055` | Image sampling is evidence/QA; rollout is implementation governance. | Reclassify the sampling part and retain a separate rollout decision only if needed. |
| `DEC-058` | Inventory, host-page role, metadata, thumbnail, transcript, VideoObject and links are multiple decisions. | Split into inventory/evidence, host-page/discoverability, media/text policy and relationship/lifecycle decisions. |
| `DEC-062` | Author, date, feed, search and 404 spaces have different policy questions. | Split or define a parent plus explicit family child decisions. |
| `DEC-069` | Monitoring windows, metrics, interpretation and rollback are independently selectable. | Split baseline/cadence from success/iteration/rollback and maintenance triggers. |
| `DEC-072` | Merchant Center eligibility and product-feed architecture are separate future programs. | Split before opening either implementation path. |
| `DEC-073` | Review availability, collection/display policy and schema eligibility are separate. | Split before any review/social-proof package is unlocked. |

## 6. Duplicate / merge candidates

The count is **1**.

- `DEC-038` already owns VideoObject eligibility/ownership, while `DEC-058` repeats VideoObject ownership inside a much broader video policy. Reword `DEC-058` to remove schema ownership and keep `DEC-038` as the single schema-eligibility decision. This is an overlap/reword candidate, not authorization to merge or edit the backlog.

Other apparent overlaps are intentionally parent/child relationships rather than duplicates: `DEC-025`/`DEC-030` (family versus sitewide sitemap), `DEC-063`/`DEC-067` (migration priority versus technical owner), `DEC-054`/`DEC-057` (global image-role rule versus family exception), and `DEC-040`/`DEC-041` (link model versus exact destinations).

## 7. Items that are execution, QA or evidence rather than standalone decisions

No current `DEC-###` item is wholly execution-only or wholly QA-only; each existing item has a target-state or governance choice. However, the following boundaries must remain explicit:

- `DEC-055` contains an evidence/sample component that belongs in a visual review or QA plan, not in an approved image target state.
- MASTER-TODO implementation, backup, crawl, regression and checkbox rows are `EXECUTION_ONLY` or `QA_ONLY` and must not be forced into new decisions.
- `SYS-001`, `SYS-007`, `SYS-014`, the unresolved portions of attachments/404s and the page-dossier `UNKNOWN_NEEDS_VERIFICATION` values are evidence gates, not target-state decisions by themselves.
- Historical identity observations without a current/future disposition are `HISTORICAL_SUPERSEDED` or `EVIDENCE_COLLECTION_ONLY`; they do not justify invented redirects or content decisions.

## 8. Deferred programs assessment

| Program | Current assessment | Freeze treatment |
|---|---|---|
| External PR / advertorial (`DEC-071`) | Safe to remain `DEFERRED` while internal architecture and landing pages stabilize. | Keep umbrella deferred; create child decisions at program opening for publisher, link attribute, landing page, campaign and measurement policy. |
| Merchant Center / product feed (`DEC-072`) | Umbrella is not sufficient once feed work is opened; eligibility and feed/variant/data architecture differ. | Keep deferred, but record split candidates now. No EXE unlock. |
| Reviews / social proof (`DEC-073`) | Genuine-data availability, collection/display and schema eligibility are separate. | Keep deferred, but record child candidates before implementation. |
| Images, video, Brand/Entity | These are core workstreams, not optional future programs. | They are freeze blockers until their material child decisions are represented. |

## 9. Family completeness assessment

The family matrix in the JSON artifact records each required family and its applicable dimensions. Summary:

| Family group | Result | Material gap |
|---|---|---|
| Homepage / Shop / Product Categories / `pa_volume` | Partial | Roles and family decisions exist; canonical/sitemap and product-fact dependencies remain gated. |
| Fabric-color, sets/bundles, mediums/additives, tools/accessories, other products | Partial | Naming/content/schema decisions exist; identifier/commercial source and lifecycle/URL rules are missing or broad. |
| Product Tags / Blog Tags / Blog Categories | Covered with migration gates | Family directions exist; exact mapping/lifecycle remains evidence and approval work. |
| Magazine / Articles | Partial | Article roles/schema/freshness/link decisions exist; provenance, CTA and image/video rules need atomic coverage. |
| Academy course/lessons / LearnDash taxonomies | Partial | Hierarchy and schema canary are represented; ownership, video and taxonomy lifecycle remain targeted gates. |
| About / Why Mariwork / Contact / Stores / FAQ | Partial | Static roles/schema/meta decisions exist; brand facts, location/NAP and FAQ semantics need explicit policy. |
| Login / Fast Buy / Cart / Checkout / My Account | Covered by system policy with split warning | `DEC-004` is too broad; no editorial optimization is authorized. |
| System/archive/machine URL spaces | Partial | Parameter/search/feed/pagination policies exist; URL normalization/canonical and bounded-space follow-up remain. |
| Historical/legacy URLs | Covered with targeted gaps | Prioritization, mapping and owner decisions exist; unresolved identity is intentionally not inferred. |
| Images | Partial | ALT and visual review direction exist; naming, primary/gallery, context and delivery are missing. |
| Videos | Partial | VideoObject canary direction exists; host-page, metadata, transcript and orphan policy are not atomic. |
| Brand/Entity | Partial | Current homepage/Organization evidence exists; canonical facts, naming, branded landing and off-site reference gates need separation. |

## 10. Technical-domain completeness

| Domain | Classification | Decision/rule mapping |
|---|---|---|
| robots.txt, meta robots, X-Robots-Tag, blocked/indexable risk | `COVERED_BY_ACCEPTED_RULE` + family gates | `docs/SEO-OWNERSHIP.md`, `DEC-004`, `DEC-059`–`DEC-062`; owner/capability must be verified per implementation. |
| preferred host/protocol, trailing slash, URL normalization | `MISSING_DECISION` | Candidate `CAND-001`. |
| canonical architecture and duplicate targets | `MISSING_DECISION` | Candidate `CAND-002`; selected parameter/migration decisions are not sitewide architecture. |
| redirects, 4xx/5xx, soft-404 and 301/404/410 | `COVERED_BY_UMBRELLA_DECISION` | `DEC-062`, `DEC-063`, `DEC-064`–`DEC-067`, plus evidence gates. |
| sitemap membership and lastmod quality | `COVERED_BY_UMBRELLA_DECISION` | `DEC-025`, `DEC-026`, `DEC-028`–`DEC-031`; lastmod remains QA/evidence unless a policy change is proposed. |
| facets, parameters, pagination, search and feeds | `COVERED_EXACT` / `COVERED_BY_UMBRELLA_DECISION` | `DEC-059`–`DEC-062`. |
| attachments/media URL policy | `COVERED_EXACT` with evidence gap | `DEC-031`; current 626/845 attachment discrepancy remains targeted evidence. |
| JS/AJAX critical content and crawlable links | `MISSING_DECISION` | Candidate `CAND-003`. |
| structured data and Rank Math ownership | `COVERED_EXACT` / `COVERED_BY_ACCEPTED_RULE` | `DEC-032`–`DEC-039`, `docs/SEO-OWNERSHIP.md`; `DEC-038` is the sole VideoObject ownership gate. |
| Woo product/variation/bundle architecture | `COVERED_EXACT` | `DEC-035`, `DEC-036`. |
| identifiers, price, currency, availability and sale source | `MISSING_DECISION` | Candidates `CAND-004` and `CAND-005`. |
| reviews/ratings and shipping/returns | `INTENTIONALLY_DEFERRED` / accepted consistency rule | `DEC-073`, `M-08`, structured-data consistency; child review/data policy is needed before expansion. |
| images/media | `PARTIAL` | `DEC-054`–`DEC-057` plus `CAND-012`–`CAND-015`. |
| mobile/CWV/page experience | `QA_ONLY` | `I-013`, `docs/MEASUREMENT-SPEC.md` and `docs/QA-SPEC.md`; no target performance claim is inferred. |
| crawler/WAF, Googlebot, OAI-SearchBot, GPTBot/ChatGPT-User | `COVERED_BY_ACCEPTED_RULE` + `QA_ONLY` | `SITEWIDE-TECHNICAL-AUDIT-SPEC.md`, `SEO-PLAYBOOK.md`, `I-014`; search and training crawler policy remain distinct. |

## 11. Content, media, Brand and editorial completeness

- Intent/page role and Product/Category/Article/Academy boundaries map to `DEC-001`, `DEC-049` and `DEC-050`; exact query ownership remains blocked because Page→Query attribution is not proven.
- Title/H1/meta families map to `DEC-007`–`DEC-019`; `DEC-016` is too broad across Shop, Category and volume landing pages.
- Visible content architecture maps to `DEC-020`–`DEC-024`, but editorial provenance, FAQ semantics, location/NAP and contextual CTA policy are candidates `CAND-008`–`CAND-011`.
- Factual accuracy/freshness is represented by `DEC-023`, the Article review of WP-13295 and the no-invented-facts rules. Author/reviewer/date/source requirements still need an atomic target.
- Internal links map to `DEC-040`–`DEC-048` and the draft requirement matrix. Exact destinations, anchors, exceptions and approved mandatory coverage remain human decision gates.
- Image ALT maps to `DEC-054` and `SYS-015`; the remaining image dimensions are candidates `CAND-012`–`CAND-015`.
- VideoObject maps to `DEC-038`; `DEC-058` must be split and the three video child areas are candidates `CAND-016`–`CAND-018`.
- Brand/entity evidence maps partly to `DEC-032` and `DEC-053`; candidates `CAND-019`–`CAND-021` close the facts, branded landing and off-site evidence boundary.

## 12. Execution Backlog dependency findings

The count of existing EXE rows with a material dependency gap is **15**. The common missing dependency is the rollout/canary policy represented by `DEC-068`; in `EXE-028` there is also an unrepresented Brand/Entity child decision, and in `EXE-023` the `DEC-038`/`DEC-058` overlap must be resolved before unlocking.

| EXE rows | Gap |
|---|---|
| `EXE-001`, `EXE-006`, `EXE-007`, `EXE-008`, `EXE-009`, `EXE-010`, `EXE-011` | Implementation package has no explicit canary/rollout decision dependency. |
| `EXE-013`, `EXE-018` | Schema or metadata/content package has no explicit rollout dependency. |
| `EXE-024`, `EXE-025`, `EXE-026`, `EXE-027` | Migration/system package has no explicit rollout/rollback policy dependency. |
| `EXE-028` | Brand package depends only on broad `DEC-053`; it needs the brand facts/naming and rollout child decisions. |
| `EXE-023` | Video package depends on the over-broad `DEC-058` while schema ownership is already `DEC-038`; split/reword is required. |

No EXE status was changed. All existing rows remain `LOCKED_BY_DECISIONS`; no package becomes `READY_FOR_TASK` from this audit.

## 13. Recommended session grouping

1. **Foundation and controls:** URL normalization, canonical architecture, system-page split, crawler/JS discoverability and sitemap relationship.
2. **Store facts and lifecycle:** identifiers/commercial sources, titles/meta, product lifecycle, slugs, categories, variants and bundle policy.
3. **Content trust and family boundaries:** provenance, FAQ/location/CTA, Article–Academy and Product–Category–Article boundaries.
4. **Internal links:** approve the three-class model, exact durable destinations, anchors, exceptions and orphan thresholds.
5. **Images and video:** split `DEC-055`/`DEC-058`, approve visual role and media delivery rules, then define canaries.
6. **Brand/Entity:** factual registry, naming, schema/site roles, branded landing/monitoring and verified off-site references.
7. **Migration and measurement:** legacy mappings, redirect owner, baseline/change annotations, monitoring interpretation and maintenance triggers.
8. **Deferred expansion:** Merchant/feed and genuine reviews only after their child decisions are represented; PR remains deferred until landing architecture is stable.

## 14. Freeze conclusion

The repository is ready for **ChatGPT P-002**, not for a Decision Backlog freeze. P-002 should challenge the 27 missing candidates, the 9 over-broad decisions, the one overlap candidate and the 15 EXE dependency gaps. Only after reconciliation should P-003/P-004 edit or freeze the authoritative backlog.

No item in this audit authorizes a title, meta, schema, canonical, robots, sitemap, redirect, taxonomy, content, media, Rank Math or WooCommerce change.
