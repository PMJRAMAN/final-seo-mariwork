# Content Architecture — Round 1

**Tasks:** A-018 / A-019 · **Status:** CODEX_AUDITED / PRE-IMPLEMENTATION CLOSURE · **Authority:** initial candidates and closure reconciliation only
**Framework:** v1.0 · **Date:** 2026-09-24

## Evidence baseline

The compact foundation contains 555 inventory rows, 167 model-page candidates and 25 policy/system spaces. Evidence contains 501 entities: 440 HTTP 200, 58 HTTP 404 and 3 safety-skipped. Public census: 83 products, 12 posts, 37 Academy lessons, 2 Academy/course rows, 7 product categories, 3 product-volume attributes, 275 product tags and 53 post-tag rows. The GSC export is page-only; **Page-query relationship is not proven by the current export.**

## Durable page roles

| Family | Role / decision | Keep distinct from | Useful modules only when verified |
|---|---|---|---|
| Shop | commercial entry and discovery | product detail; generated facets | orientation, durable category links |
| Product category | family comparison/navigation | product detail; tag archives | family definition, products, volume/set paths, education |
| Fabric-color product | exact color/code/volume selection | generic article; sibling duplicates | decision summary, specs, volume, limitations, siblings, education |
| Sets/bundles | multi-item selection | individual colors; tag archives | verified contents, volume comparison, components |
| Mediums/tools | supporting-material selection | generic technique pages | verified function, limitations, relevant technique |
| Academy/course/lesson | structured learning | product detail; generic article | prerequisites, steps, materials, next lesson |
| Article | durable reference/comparison | same-intent lesson; tag archives | answer-first explanation, evidence, comparison, next decision |
| Artists/trust | verified entity/context | product and technique intent | only verified profile/source material |
| Product Tags / Blog Tags | transitional taxonomy spaces | categories/products/articles | migration evidence only; no per-tag content model |

## Internal-link requirement candidates (not final)

### CORE / MANDATORY candidates

| Source | Destination | Purpose |
|---|---|---|
| Product | Shop + relevant durable category | commercial parent and family context |
| Product | Relevant Academy/article | answer real preparation/technique questions |
| Category/Shop | Products + relevant education hub | discovery and decision support |
| Academy/article | Relevant product/category | explicit commercial next step when justified |
| Course/lesson | Parent course/Academy | preserve learning hierarchy |
| Academy/article | Relevant sibling/hub | maintain learning navigation |

### FAMILY-SPECIFIC candidates

- Fabric-color product: volume siblings, related colors, category, preparation/fixation/technique education.
- Set/bundle: verified components, sibling volumes, set category and use education.
- Medium: compatible product family and lessons that explicitly use it.
- Tool/accessory: technique lesson/article only when genuinely relevant.
- Academy lesson: required materials/category, next/previous lesson, related technique article.
- Article: topic hub, distinct Academy lesson, durable category/product family.
- Category: subfamily/volume paths and selected education hub; do not use tag archives as architecture.

### CONTEXTUAL / OPTIONAL candidates

Color comparisons, individual siblings, article-paragraph links, store-address/about links and cross-family recommendations belong only where the visible topic and user decision justify them. Automated related links are not proof of relevance.

## Bidirectional relationships

1. Product/Category → Academy/Article: exact lesson/article for preparation, technique, fixation, fabric choice or comparison.
2. Academy/Article → Product/Category: durable family destination when a material/tool is actually named and sold/verified; do not invent availability.
3. Category ↔ Academy/Article: education hubs for comparison/selection while keeping reference and lesson roles distinct.
4. Sets ↔ components: only after bundle contents and identity are verified; variation/bundle completeness is currently blocked.

## Architecture risks

- Initial HTML reports 289 missing meta descriptions, 271 missing H1s and no parsed schema types; this is an output/ownership audit issue, not a reason to add repetitive copy.
- Product pages show shared navigation and related blocks, but complete rendered link coverage and relevance are not proven.
- Product tags contain redundant color/volume/brand/type dimensions; Blog Tags show separate behavior. Both are family-level decommission programs.
- Historical /articles/ and /education/ sources coexist with current /mag/articles/ and /academy/ families; transport does not prove identity.
- No content target, word count, FAQ volume or rewrite is approved.

## Product Title Naming Standard — candidate only

Observed patterns include:

- Fabric colors often use product type + color + Mariwork + code, but some H1s omit brand, some use a pipe before code, and Persian/Latin code digits vary.
- Sets vary in count/description/volume ordering; “includes” clauses are inconsistent.
- Mediums/tools use different type-first patterns; some titles include «ماری ورک» while H1s omit it.
- Volume appears as 30 میل, 60 میل, 250 میل, 30ml or 30میل, with inconsistent placement.
- Code forms vary: کد 105, کد ۱۰۵ and code-311. This is an observed consistency issue, not proof any code is wrong.

Candidate pattern for Second Review:

[product type] [specific product/color/name] [brand token if required] [verified code] [size/volume when distinguishing the offer]

Review separately for fabric colors, sets/bundles, mediums and tools: determine whether «ماری ورک»/Mariwork is mandatory, optional or omitted; code/separator/numeral convention; volume placement; title/H1 relationship; exceptions; and legacy title history. No bulk rename is authorized. Rank Math title ownership is UNKNOWN_NEEDS_VERIFICATION.

**Google basis:** GOOGLE_CONSISTENT for useful accessible non-duplicative content and descriptive links; PROJECT_DECISION for family roles and title candidates. References: [people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content), [SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide), [structured data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data).

## Pre-implementation closure

The current Store graph and cross-family relationships are reconciled in
`strategy/INTERNAL-LINK-REQUIREMENT-MATRIX-DRAFT.md`. That artifact separates
`CORE_MANDATORY`, `FAMILY_SPECIFIC` and `CONTEXTUAL_OPTIONAL` candidates across
Homepage, Shop, Categories, Products, Academy, Lessons, Articles, Blog
Categories and Static/Trust pages.

The matrix is a draft only. It does not approve link destinations, query
anchors, content rewrites, keyword auto-linking or Production changes.

| Durable family | Role | Current evidence | Target-state gate |
|---|---|---|---|
| Homepage | brand/entity gateway and family hub | `pages/homepage/WP-63.md` + current SEO output | Second Review |
| Shop / Product Categories | commercial discovery and comparison | Store matrices and SR-004 | human approval |
| Products / sets / bundles / tools | transactional decision pages | 84-product dossier set and Store matrices | canary + approval |
| Academy / courses / lessons | structured instruction | Academy architecture and 39 dossiers | Second Review |
| Magazine / Articles / Categories | durable reference and comparison | article/category dossiers and current schema output | Second Review |
| Static trust/support | brand, communication and task support | grouped static dossiers | Second Review |
| Product Tags / Blog Tags | transitional taxonomy spaces | tag reconciliation | migration decision |
| Cart / Checkout / My Account | utility/system endpoints | system-policy dossiers | system-policy review |

No keyword target, word-count target, editorial rewrite or final disposition
is invented by this closure. **Page-query relationship is not proven by the
current export.**
