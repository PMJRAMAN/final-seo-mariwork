# Internal Link Requirement Matrix — DRAFT

**Date:** 2026-09-25
**Status:** `DRAFT — NOT APPROVED FOR PRODUCTION`
**Lifecycle:** `CODEX_AUDITED`
**Production writes:** `0`

This matrix extends the Round-1 architecture and the current Store graph across durable Mariwork families. It is a review artifact, not a mass-linking instruction. Final rules require ChatGPT Second Review and human approval.

## Evidence basis

- `audits/second-review/store/current-internal-link-graph.json` — 157 entities, 16,656 observed edges, 13,668 unresolved resolver destinations.
- `strategy/INTERNAL-LINK-ARCHITECTURE.md` — CORE/FAMILY-SPECIFIC/CONTEXTUAL model.
- `strategy/CONTENT-ARCHITECTURE.md` — family roles and candidate relationships.
- `audits/second-review/store/SR-004-CHATGPT-STORE-SECOND-REVIEW.md` — Store contextual-link findings.
- `audits/second-review/reconciliation/current-academy-architecture.json` — current course/lesson hierarchy.

## Draft matrix

| Source family | Link class | Target family/entity | Purpose | Applicability | Exceptions | Evidence |
|---|---|---|---|---|---|---|
| Homepage | `CORE_MANDATORY` | Shop, durable Product Categories, Academy hub, Magazine/articles hub | Clarify brand, commercial and learning hubs | Homepage navigation/CTA sections | Do not duplicate links solely for count | `pages/homepage/WP-63.md` |
| Shop | `CORE_MANDATORY` | Durable Product Categories; current products | Make family discovery and product traversal crawlable | `/shop/` and approved navigation | Exclude empty/migration-only categories until lifecycle approval | `pages/shop/WP-30918.md`; SR-004 |
| Product Category | `CORE_MANDATORY` | Products in that category | Preserve category → product discovery | Durable categories with current assignments | No durable link to zero-assignment migration categories | product-category dossiers; current graph |
| Product Category | `FAMILY_SPECIFIC` | Relevant Academy lesson/article | Help selection/usage where a real topic is relevant | Category has demonstrated learning relationship | No generic Academy footer on every category | SR-004; Content Architecture |
| Product | `CORE_MANDATORY` | Shop and relevant durable Product Category | Provide commercial parent/family context | Published current product | Bundle/variation exceptions preserve actual Woo/YITH identity | Store dossiers; current graph |
| Product | `FAMILY_SPECIFIC` | Relevant Academy lesson/article | Answer preparation, technique, fixation or care questions | Only where relationship is real | No unrelated lesson or invented product use | SR-004 SR-ST-009 |
| Product | `FAMILY_SPECIFIC` | Verified sibling/volume destination | Support a real color/volume decision | Variable product or verified sibling set | Parent remains canonical; variant preselection is not a new editorial entity | variant matrix; volume architecture |
| Set/Bundle product | `FAMILY_SPECIFIC` | Verified components, sibling volumes, set category | Explain actual bundle composition and adjacent choices | Only after current YITH/Woo mapping | No inferred component links | bundle matrix; SR-004 |
| Academy archive/course | `CORE_MANDATORY` | Course/lesson hierarchy | Preserve learning-hub traversal | Current Academy/course entities | Historical `/education/` aliases are migration evidence | academy architecture |
| Lesson | `CORE_MANDATORY` | Parent course/Academy; next/previous lesson where real | Maintain instructional hierarchy and progression | Current published lessons | Do not force a sequence without evidence | lesson dossiers |
| Academy/Lesson | `FAMILY_SPECIFIC` | Product/Product Category | Identify real materials or tools used | Material/tool explicitly used and current | No commercial stuffing or availability invention | SR-004 SR-ST-009 |
| Article | `CORE_MANDATORY` | Article category/hub; distinct related article | Preserve durable reference navigation | Published articles | Avoid near-duplicate loops and tag-archive dependency | article dossiers; category matrix |
| Article | `FAMILY_SPECIFIC` | Academy lesson/course | Resolve a genuinely instructional follow-up | Lesson adds distinct value | Do not merge article and lesson intent by default | content architecture |
| Article | `FAMILY_SPECIFIC` | Product/Product Category | Provide a useful material/product next step | Article names/explains that product/family | No query-anchor automation or inferred target | SR-004 SR-ST-009 |
| Blog Category | `CORE_MANDATORY` | Its current articles | Make durable category hubs useful | Two non-empty/indexable categories currently evidenced | Empty/noindex categories need lifecycle decision | current-blog-category-matrix |
| Blog Category | `FAMILY_SPECIFIC` | Academy/article hub | Separate article reference from Academy instruction | Demonstrated topic relationship | Do not use transitional tags as architecture | category dossiers |
| Static trust/support | `CONTEXTUAL_OPTIONAL` | About, Contact, Stores, FAQ, relevant hubs | Support trust and user tasks | Page task requires it | System pages are not editorial link targets | static dossiers |
| Blog/Academy/Product/Category | `CONTEXTUAL_OPTIONAL` | Static trust/support | Add confidence/support path where useful | Relevant user decision only | No repeated boilerplate | strategy and family dossiers |
| Product Tags / Blog Tags | `CONTEXTUAL_OPTIONAL` | Durable Category/Article/Hub destination | Transitional migration support only | Specific term mapping is approved | Tags are not durable hubs; no mass tag links | tag reconciliation; SR-004 |

## Rule interpretation

- `CORE_MANDATORY` is a candidate for every applicable source page, subject to a documented exception.
- `FAMILY_SPECIFIC` applies only for a known family/topic/usage condition.
- `CONTEXTUAL_OPTIONAL` implies no coverage target or automatic insertion.
- A missing link is not a defect until the rule and exception are approved.
- The 13,668 unresolved graph destinations are resolver gaps, not a broken-link count.
- No mass keyword auto-linking, generic anchor replacement or sitewide link injection is recommended.

## Draft regression set

Review at least: homepage, shop, one durable category, one color product, one medium/tool, one set/bundle, one Academy course, three lessons with distinct materials, two articles, one durable blog category and one static trust page. Include an unaffected control and confirm no cart/checkout/account behavior changes.

## Required decisions before implementation

1. Approve or revise relationships and exceptions.
2. Identify exact destination URLs/entities for approved rules.
3. Confirm natural anchor text from visible meaning; do not invent query targets.
4. Record mandatory-link coverage and orphan/underlink measurements.
5. Create a scoped change dossier and implementation task; this draft authorizes no Production write.

**Google basis:** `GOOGLE_CONSISTENT` for crawlable, meaningful navigation and ecommerce hierarchy; https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure
