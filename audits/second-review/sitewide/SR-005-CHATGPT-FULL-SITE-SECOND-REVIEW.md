# SR-005 — ChatGPT Full-Site Second Review

**Date:** 2026-09-25  
**Review type:** Independent Full-Site Second Review  
**Repository baseline:** `af0cd7d9436291047ed8925d8c3391f032910ead`  
**Source handoff:** `handoff/FULL-SITE-PRE-IMPLEMENTATION-SECOND-REVIEW-HANDOFF-2026-09-25.md`  
**Lifecycle:** `SECOND_REVIEWED`  
**Human approval:** `PENDING`  
**Implementation authorized:** `NO`  
**Production writes during review:** `0`

## 1. Executive decision

The broad discovery/audit phase is sufficiently complete to stop repeating full-site audits.

The repository now contains enough current-state evidence to proceed from audit into target-state approval and then phased implementation, subject to the human approval gate.

This does **not** mean every unresolved historical URL, ALT candidate, or query assignment is solved. Those remain targeted workstreams and do not justify restarting full-site audit.

Second Review classification:

- Foundation/current-state evidence: **CONFIRM WITH DOCUMENTATION CORRECTION**
- Store SR-004: **CONFIRM**, with the existing approval gate retained
- Homepage: **CONFIRM**
- Static/Core: **MODIFY**
- Articles: **CONFIRM WITH TARGETED CONTENT REVIEW**
- Blog Categories: **MODIFY**
- Blog Tags: **CONFIRM DECOMMISSION DIRECTION**
- Academy/LearnDash: **MODIFY**
- Product Categories: **CONFIRM**
- `pa_volume`: **NEEDS_MORE_EVIDENCE BEFORE FINAL INDEX/SITEMAP APPROVAL**
- Product Tags: **CONFIRM DECOMMISSION DIRECTION**
- System/utility URLs: **CONFIRM WITH POLICY CLARIFICATION**
- Cross-family internal-link model: **CONFIRM FRAMEWORK / MODIFY SOME MANDATORY RULES**
- Images/ALT: **CONFIRM TARGETED VISUAL REVIEW**
- Historical/legacy mappings: **KEEP AS SEPARATE MIGRATION WORKSTREAM**

No Production implementation is authorized by this review until the owner approves the target-state decisions.

---

## 2. Independent review basis

This review reconciles:

- current Production census and current SEO output;
- `PRE-IMPLEMENTATION-COVERAGE-MATRIX.json`;
- `PRE-IMPLEMENTATION-AUDIT-CLOSURE.md`;
- Store SR-002/SR-003/SR-004;
- current Rank Math ownership/output evidence;
- current Academy hierarchy;
- Blog category/tag reconciliation;
- system URL-space closure;
- draft cross-family internal-link matrix;
- image/ALT summary;
- official Google Search documentation current at review time.

Official Google basis used:

- robots meta: https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag
- ecommerce site structure/internal linking: https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure
- faceted navigation: https://developers.google.com/crawling/docs/faceted-navigation
- structured data: https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- Article structured data: https://developers.google.com/search/docs/appearance/structured-data/article
- Organization structured data: https://developers.google.com/search/docs/appearance/structured-data/organization
- Course list structured data: https://developers.google.com/search/docs/appearance/structured-data/course
- Video structured data: https://developers.google.com/search/docs/appearance/structured-data/video
- image SEO / ALT: https://developers.google.com/search/docs/appearance/google-images

The Page+Query dataset remains unavailable. Therefore no query-to-URL ownership, cannibalization conclusion, or exact keyword target is approved merely from separate Page and Query exports.

---

## 3. Coverage reconciliation correction

### SR5-COV-001 — Static/Core count in closure matrix needs correction

**Decision:** `MODIFY`

The closure matrix reports **10 current Static/Core editorial entities**, but the current public Page census contains only eight non-homepage/non-Shop/non-system current pages:

- WP-66
- WP-68
- WP-70
- WP-13798
- WP-14760
- WP-30906
- WP-30991
- WP-32895

The two additional pre-existing Static dossiers:

- WP-32689
- WP-34061

are historical Round-1 dossiers whose recorded current evidence was 404 and they are not present in the current public Page census.

Therefore:

- **8 current Static/Core pages**
- **2 historical Static dossiers**
- **3 current system-commerce pages**
- Homepage and Shop remain separate families.

This is a documentation/bookkeeping correction, not a Production defect.

### A-009 / A-009B

The isolated autonomous-runner deployment blocker is a tooling/runtime blocker. It is **not an SEO implementation blocker** once human-approved implementation tasks are executed through the normal controlled workflow.

---

## 4. Homepage

### Decision: `CONFIRM`

Current evidence supports the homepage as the primary brand/entity gateway and cross-family navigation hub.

Current state is coherent:

- 200
- index/follow
- self-canonical
- one H1
- deliberate title
- deliberate meta description
- links to Store, Academy and Magazine
- Rank Math ownership visible
- current JSON-LD includes `Organization`, `WebSite`, `WebPage`, `ImageObject` and `SearchAction`.

### Target state

Keep the homepage indexable and self-canonical.

Keep the current title/H1 direction unless later query evidence gives a specific reason to revise it.

Keep one authoritative Organization/WebSite graph rather than adding a second schema emitter.

`SearchAction` is no longer useful for Google's retired sitelinks search box. It is not harmful and is not a priority defect; remove only if doing so is simple and does not disturb the supported `WebSite`/site-name markup.

No homepage rewrite is required before implementation of unrelated technical fixes.

---

## 5. Static/Core pages

### Decision: `MODIFY`

The current page roles are generally valid, but the schema and metadata strategy needs correction.

### SR5-STATIC-001 — Article schema is over-applied to generic WordPress Pages

Current evidence shows `Article` + `Person` output on pages including:

- About
- Contact
- Stores address
- FAQ
- login
- Fast Buy
- Why Mariwork

Google's Article documentation is intended for news/blog/sports article content. A generic page-template default should not label unrelated utility, contact, account, or support pages as articles.

**Target state:**

- do not globally assign Article schema to the WordPress `page` post type;
- use role-appropriate page semantics or generic `WebPage`;
- preserve one Organization/WebSite owner;
- keep Article only on pages that genuinely function as an article;
- do not add FAQ schema merely to chase a rich result. FAQ rich results are generally not shown for sites outside Google's limited eligibility, so semantic correctness is the goal, not SERP decoration.

This should be implemented first as a small family canary, not a sitewide blind switch.

### SR5-STATIC-002 — metadata quality

Several durable pages have weak or absent meta descriptions:

- Magazine has no meta description;
- About / Contact / Stores / Why Mariwork use very short generic descriptions.

These are content-quality tasks, not technical emergencies.

Write explicit factual descriptions after approval. Do not use generic archive/excerpt leakage.

### Utility pages

`/login-otino/` and `/fast-buy/` are currently noindex. That is reasonable for their current utility role unless a deliberate future search-landing strategy is approved.

Their missing canonical is **not** a defect that requires adding a canonical merely for audit completeness.

---

## 6. System commerce pages

### Decision: `CONFIRM WITH POLICY CLARIFICATION`

WP-10 Checkout, WP-11 My Account and WP-30919 Cart are correctly separated from editorial SEO.

### Target state

- Cart: retain noindex utility treatment.
- My Account: retain noindex utility/privacy treatment.
- Checkout: the observed empty-session redirect to Cart is a system-state observation, not an SEO defect.
- Do not add editorial copy.
- Do not make these search targets.
- Do not add canonicals solely because the current noindex pages lack them.
- Any future regression must test WooCommerce state transitions without creating orders or exposing customer data.

No Production SEO change is currently required for these three pages.

---

## 7. Articles

### Decision: `CONFIRM WITH TARGETED CONTENT REVIEW`

All 12 current articles have:

- 200
- index/follow
- self-canonical
- H1
- meta description
- Rank Math marker
- `BlogPosting` structured data.

This supersedes the old Round-1 broad missing-schema interpretation.

### Target state

Keep the Article family indexable and continue using BlogPosting where facts match visible content.

Before content rewrites:

1. fact-check technical and safety claims;
2. review stale dates/examples where applicable;
3. shorten or rewrite overly long descriptions where useful;
4. add contextual Product/Category or Academy links only where the article genuinely names or explains that next step;
5. perform image-purpose review before ALT implementation.

WP-13295 remains a priority factual-review candidate because its visible/meta copy includes health/safety claims about industrial dyes.

No broad Article rewrite is approved.

---

## 8. Blog Categories

### Decision: `MODIFY`

Current family state:

- `TERM-category-71` Articles: non-empty, 200, indexable, self-canonical.
- `TERM-category-142` History: non-empty, 200, indexable, self-canonical.
- nine empty categories: 200/noindex.
- one Uncategorized category: 404.

### Target state

Treat Articles and History as durable content hubs.

Do not optimize empty noindex categories with artificial content.

For each empty category choose later between:

- remove term / retire archive;
- retain noindex for operational reasons;
- redirect only when a genuine durable semantic replacement exists.

No blanket redirect by slug similarity.

The current noindex state of empty archives is acceptable while lifecycle decisions are prepared.

---

## 9. Blog Tags

### Decision: `CONFIRM DECOMMISSION DIRECTION`

The family is not needed as a durable navigation/SEO architecture.

Current evidence shows 54 terms, with six assigned terms and 39 assignments.

### Target state

Before deletion:

- remove/replace meaningful content relationships;
- map historically valuable tag URLs only where a real Category/Article/Hub replacement exists;
- use 410 only where no meaningful replacement exists and evidence supports removal;
- remove internal tag dependencies;
- keep tag archives out of sitemap/index strategy.

Do not create 54 optimization projects.

---

## 10. Academy / LearnDash

### Decision: `MODIFY`

The current hierarchy is credible:

- one current course;
- 37 current lessons;
- hierarchy verified;
- all sampled/current course and lesson URLs are indexable/self-canonical;
- current evidence shows no Rank Math public marker or JSON-LD on the course/lesson family.

The absence of schema is **not automatically an SEO defect**.

### Target state

First establish one intentional SEO/schema owner for LearnDash entities.

Do **not** mass-apply Article schema to lessons.

Do **not** build a Google Course-list implementation now solely for rich-result purposes: Google currently requires at least three courses for the Course list feature, while Mariwork currently has one course.

For video-based lessons, `VideoObject` is a stronger candidate **only when**:

- the video is actually watchable on that URL;
- title/description/thumbnail/date/duration facts are available;
- Google can discover/fetch the video or valid embed;
- markup matches visible content.

Use one course + two representative video lessons as the schema/ownership canary.

Breadcrumb markup may be evaluated if it accurately represents the visible course/lesson hierarchy.

Historical `/education/` mappings remain a separate migration workstream.

---

## 11. LearnDash Course Categories

### Decision: `NEEDS_MORE_EVIDENCE FOR FINAL LIFECYCLE`

The two current taxonomy entities resolve as 404 in the current output sample.

Do not optimize or restore these archives automatically.

Confirm whether the terms are still operationally needed inside LearnDash. If not needed publicly, keep them out of the public SEO architecture and handle historical URLs through the migration workstream.

---

## 12. Product Categories

### Decision: `CONFIRM SR-004`

Keep durable product categories as the primary commercial family/navigation layer.

The two zero-assignment migration-era categories remain decommission candidates and should consolidate only to the proven main color-family destination.

Do not mass-change product/category slugs.

Approved durable categories should receive deliberate metadata and sitemap treatment after human approval.

---

## 13. pa_volume

### Decision: `NEEDS_MORE_EVIDENCE BEFORE FINAL INDEX/SITEMAP APPROVAL`

SR-004 correctly separated `pa_volume` from the old 60ml/250ml Product Categories.

However, current evidence is not sufficient to approve the three volume archives as permanent indexable sitemap targets.

Before approval verify for 30ml / 60ml / 250ml:

- unique user purpose beyond Shop filters;
- useful visible archive content;
- deliberate H1/title/meta;
- internal-link role;
- overlap with Product Categories and filter URLs;
- whether users can reach them through durable crawlable navigation.

Until that is proven:

- do not delete them;
- do not noindex them blindly;
- do not add them to the sitemap merely because they are currently indexable.

This is a targeted decision, not a new family audit.

---

## 14. Product Tags

### Decision: `CONFIRM DECOMMISSION DIRECTION`

275 terms currently have zero assignments.

Do not optimize them.

Proceed later through a controlled family migration:

- historical URL/value check;
- internal-link check;
- destination mapping only where semantic replacement exists;
- approved redirect/410 plan;
- cleanup and crawl regression.

---

## 15. Store / Products

### Decision: `CONFIRM SR-004`

SR-004 remains the operative Store Second Review.

No new evidence from closure requires reopening Store discovery.

Retain the SR-004 sequence for:

- Shop H1/meta;
- product title normalization;
- explicit product meta descriptions;
- ProductGroup/variant canary;
- bundle presentation;
- durable Product Category policy;
- parameters/facets;
- contextual links.

Google's current Product Variant guidance still supports single-page variant URLs with preselection parameters. Do not blanket-block the variant-selection mechanism.

---

## 16. Facets / parameters

### Decision: `MODIFY IMPLEMENTATION STRATEGY`

The current SR-004 caution against aggressive robots rules is correct during separation/testing.

Google's current faceted-navigation guidance states that when facet URLs do not need indexing, preventing crawling can be more effective long-term than relying only on canonical consolidation.

Therefore the eventual strategy should be staged:

1. separate variant-preselection parameters from non-search facet/sort/display parameters;
2. verify which parameter families must remain crawlable;
3. canonicalize/consolidate where appropriate;
4. only after regression, consider robots.txt blocking for clearly non-indexable crawl traps;
5. remember that a robots-blocked URL cannot expose its meta noindex to Google.

Do not deploy blanket parameter blocking before this separation.

---

## 17. Cross-family internal links

### Decision: `CONFIRM FRAMEWORK / MODIFY MANDATORY RULES`

The three-class model is approved for planning:

- `CORE_MANDATORY`
- `FAMILY_SPECIFIC`
- `CONTEXTUAL_OPTIONAL`

Approved principles:

- Homepage → major durable hubs.
- Shop/Category → real products and durable commercial hierarchy.
- Product → durable family/category and relevant learning content.
- Academy/Lesson → real Product/Category when material/tool is explicitly used.
- Article → Product/Category when the commercial next step is genuinely useful.
- Category → selected relevant educational/reference content.
- no mass keyword auto-linking.

Modification:

A distinct related Article should **not** be mandatory on every Article. The Article → category/hub relationship may be core; Article → Article should be contextual or family-specific unless a deliberate series requires it.

Exact targets and anchors must be mapped before implementation.

The 13,668 unresolved graph destinations remain resolver gaps, not a broken-link count.

---

## 18. Images / ALT

### Decision: `CONFIRM TARGETED VISUAL REVIEW`

Missing-ALT counts are candidate queues, not instructions to fill every empty ALT.

Use representative human visual review before implementation.

Recommended initial sample:

- 3 Articles;
- 3 Academy lessons;
- Homepage;
- 2 Products from different families;
- 1 Product Category;
- About / Stores / FAQ.

For each image classify:

- informative;
- decorative;
- linked/navigation;
- repeated/template;
- product/gallery;
- instructional.

Only informative images receive factual useful ALT.

Do not keyword-stuff and do not invent image details.

---

## 19. Historical / legacy URLs

### Decision: `KEEP AS SEPARATE MIGRATION WORKSTREAM`

Partial and unknown mappings do not block unrelated technical/content implementation.

Do not infer semantic identity from a redirect alone.

Prioritize historical URLs with meaningful clicks/impressions/links before low-value unknowns.

Legacy Artist URLs and other historical content must be resolved from source identity/history, not from stale search snapshots or slug similarity.

---

## 20. New Second Review findings

### SYS-016 — Generic WordPress Page schema is semantically over-broad

**Severity:** P1  
**Scope:** FAMILY  
**Status:** CONFIRMED

Current evidence shows Article/Person markup on generic static, support and utility WordPress Pages.

**Target:** role-appropriate page schema / generic WebPage; Article only where the content genuinely functions as an article. Rank Math remains first owner where supported.

### SYS-017 — LearnDash schema ownership is not intentional yet

**Severity:** P2  
**Scope:** FAMILY  
**Status:** CONFIRMED

Current course/lesson URLs have SEO output but no current Rank Math marker/JSON-LD evidence.

**Target:** establish single ownership first; use a small course/lesson canary. Do not mass-add unsupported or irrelevant schema.

### SYS-018 — Closure coverage count mixes current and historical Static dossiers

**Severity:** P3  
**Scope:** REPOSITORY/DOCUMENTATION  
**Status:** CONFIRMED

The closure matrix's Static/Core count should distinguish eight current public pages from two historical 404 dossiers.

No Production impact.

---

## 21. What remains before implementation

The following are **approval/targeted-work gates**, not reasons for another broad audit:

1. human approval of this Second Review and SR-004 target state;
2. exact `pa_volume` index/sitemap decision;
3. exact Blog Tag / Product Tag migration mappings;
4. selected historical URL mappings;
5. LearnDash schema/video canary definition;
6. representative visual ALT review;
7. exact internal-link destination matrix;
8. final content text approval for titles/meta/copy that will change.

Page+Query data can improve future content/query decisions but its absence does not block technical implementation that does not depend on query attribution.

---

## 22. Approval state

**Second Review:** COMPLETE  
**Human approval:** PENDING  
**Production implementation:** NOT AUTHORIZED

Once the owner approves the target states, implementation should proceed in controlled canaries, with Codex QA and ChatGPT Final Acceptance after each approved rollout.
