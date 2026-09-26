# Internal Link Requirement Matrix

**Status:** ACCEPTED STRATEGY FRAMEWORK / DESTINATION MAPPING PENDING  
**Authority:** DEC-040 through DEC-048, DEC-120  
**Date:** 2026-09-26
**Production writes:** 0

This matrix is the canonical policy layer for Mariwork internal linking. It defines required relationship classes. Exact destination URLs and page-level exceptions are resolved in research/implementation tasks and must not expand the policy.

## Matrix

| Source family | Link class | Target family/entity | Purpose | Applicability | Exceptions / boundaries |
|---|---|---|---|---|---|
| Homepage | CORE_MANDATORY | Shop, Academy, Magazine and other approved top-level durable hubs | Expose main brand/commercial/learning/editorial routes | Homepage navigation/CTA architecture | Do not duplicate links merely for count |
| Shop | CORE_MANDATORY | Durable Product Categories and current Products | Commercial discovery and crawlable traversal | Current durable Store architecture | Exclude retired/migration-only categories |
| Product Category | CORE_MANDATORY | Products in that Category; real parent/Shop hierarchy | Category → Product discovery and hierarchy | Durable Product Categories | No zero-assignment/retired taxonomy targets |
| Product Category | FAMILY_SPECIFIC / CONTEXTUAL | Relevant Academy/Article | Selection/use/technique/care support | Only when Category is content-supported and relationship is directly useful | No generic education block on every Category |
| Product | CORE_MANDATORY | Stable primary Product Category / Shop hierarchy | Commercial parent/family context | Published Products | May be supplied by breadcrumb/navigation; no forced body-copy duplication |
| Product | FAMILY_SPECIFIC / CONTEXTUAL | Relevant Academy/Article | Help selection, preparation, use, application, fixation/cure or care | Only where direct user value exists | Broad topic similarity alone is insufficient |
| Product | FAMILY_SPECIFIC | Verified sibling/volume destination | Support a real color/volume/product decision | Variable Product or verified sibling set | Parent remains canonical; variant preselection is not a new editorial entity |
| Set/Bundle Product | FAMILY_SPECIFIC | Verified components, sibling volumes, Set Category | Explain actual composition and adjacent choices | Only from verified YITH/Woo composition | No inferred component links |
| Academy hub / Course | CORE_MANDATORY | Real Course/Lesson/Guide hierarchy | Preserve structured learning traversal | Current Academy entities | Historical aliases are migration evidence, not canonical destinations |
| Lesson / Guide | CORE_MANDATORY | Parent Course/Collection → Academy | Preserve learning hierarchy | Current published instructional entities | Do not force fictional sequence/course relationships |
| Academy / Lesson / Guide | FAMILY_SPECIFIC / CONTEXTUAL | Product / Product Category | Identify real material/tool used or direct next step | Material/tool genuinely used, required or relevant | No generic commercial stuffing |
| Article | CORE_MANDATORY | Stable primary Blog Category → Magazine | Preserve editorial hierarchy | Published Articles | Avoid Tag dependency and near-duplicate loops |
| Article | FAMILY_SPECIFIC / CONTEXTUAL | Related Article / Academy | Useful continuation, deeper detail, prerequisite or practical follow-up | Semantically useful next step | No fixed count; no random Tag-based related links |
| Article | FAMILY_SPECIFIC / CONTEXTUAL | Product / Product Category | Useful commercial/material next step | Article materially discusses/uses the item/family | No unrelated Shop/Product links |
| Durable Blog Category | CORE_MANDATORY | Its current Articles; Magazine hierarchy | Make editorial hub crawlable/useful | Durable indexable Categories | Empty/retired Categories excluded |
| Durable Blog Category | FAMILY_SPECIFIC / CONTEXTUAL | Academy or another editorial hub | Distinct practical/reference handoff | Demonstrated topic relationship | No transitional Tag architecture |
| Static trust/support | CONTEXTUAL_OPTIONAL | Relevant durable hubs / trust pages | Support trust and real user tasks | Only when useful to page purpose | No repeated boilerplate for SEO |
| Product Tags / Blog Tags | TRANSITIONAL_ONLY | Approved durable successor where a migration mapping exists | Migration cleanup only | Specific approved mapping | Tags are not durable hubs; no mass linking |

## Interpretation

- CORE_MANDATORY applies to every applicable source entity unless a documented exception exists.
- FAMILY_SPECIFIC applies only when the defining family condition exists.
- CONTEXTUAL_OPTIONAL has no coverage target and is never inserted mechanically.
- Cross-family education/commercial relationships are **not CORE by default**.
- A missing link is a defect only when an accepted mandatory relationship applies.
- No mass keyword auto-linking, generic anchor replacement or sitewide contextual-link injection is allowed.

## Destination mapping

Before implementation, each scoped rollout must resolve:
1. exact destination entity/URL;
2. applicable source family/pages;
3. natural anchor/context;
4. documented exceptions;
5. current link presence/absence;
6. regression set.

Destination mapping must not infer Page→Query ownership without evidence.

## Regression set

For a broad internal-link change, include representative:
- Homepage;
- Shop;
- durable Product Category;
- Fabric Color Product;
- Medium/Tool Product;
- Set/Bundle;
- Academy hub/course;
- multiple Guides/Lessons with different materials;
- Article;
- durable Blog Category;
- Static trust page;
- unaffected control.

Validate crawlable href output, destination status/canonical, hierarchy consistency, anchor accuracy and absence of utility/cart/checkout/account regressions.

No Production write is authorized by this matrix alone.
