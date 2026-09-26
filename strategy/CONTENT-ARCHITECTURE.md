# Content Architecture — Accepted Strategy Framework

**Status:** ACCEPTED STRATEGY FRAMEWORK / IMPLEMENTATION RESEARCH PENDING  
**Authority:** DEC-001, DEC-007–024, DEC-040–050, DEC-076–077, DEC-085, DEC-088, DEC-115–125, DEC-130  
**Updated:** 2026-09-26

## Purpose

Define durable content roles so Mariwork does not create overlapping pages, filler content or random keyword-target pages.

## Durable page roles

| Family | Primary role | Keep distinct from | Useful modules only when justified |
|---|---|---|---|
| Homepage | Brand/entity gateway + top-level navigation | Shop/category/article | concise brand intro, major hub CTAs |
| Shop | Broad commercial discovery hub | Product detail; generated facets | orientation, durable category links, short archive content block |
| Product Category | Family browse/comparison/selection | Product detail; tag archives | family definition, products, selection guidance, relevant education, short archive content block |
| pa_volume | Cross-family commercial browse by genuine purchasable volume | volume filter parameter; old volume categories | volume role, eligible products, useful comparison, short archive content block |
| Fabric-color Product | Exact color/code/variant selection | generic article; sibling duplicates | decision summary, verified specs, variant choice, limitations, relevant education |
| Set/Bundle Product | Multi-item purchasable identity | individual colors; tag archives | verified contents, volume identity, components, use context |
| Mediums/Tools | Supporting-material selection | generic technique pages | verified function, limitations, relevant technique |
| Academy / Course / Guide / Lesson | Video-first practical/demo learning | text-first reference Article; Product detail | prerequisites, steps, materials, video context, learning progression |
| Magazine Article | Text-first explanation/reference/editorial | same-intent Academy lesson; Product detail | answer-first explanation, evidence, comparison, next useful step |
| Magazine hub | Editorial discovery hub | Article; Blog Category | category blocks, latest/reference discovery, short archive content block |
| Durable Blog Category | Editorial topic hub | tag archives | category intro, current Articles, relevant cross-family handoff |
| Artists | Separate Mariwork Artists directory/project when launched | Magazine artist/history Article | verified Artist identity/profile content only |
| Static trust/support | Specific trust/support task | editorial/commerce duplication | only purpose-specific verified information |
| Product/Blog Tags | Transitional migration spaces | durable Categories/Articles/Products | no durable content model |

## Product title/H1 standards

Accepted family rules are DEC-007 through DEC-011.

- Fabric Colors: `رنگ پارچه [Color Name] ماری‌ورک کد [NNN]` using verified color/code; no parent-title volume token.
- Sets/Bundles: concise purchasable identity + genuinely identifying count/type/volume where applicable; long component lists belong in body content.
- Mediums/Additives: exact Product identity + Mariwork + real code; no forced generic “medium”; no volume in this family title.
- Tools/Accessories: brand ownership must be factual; third-party items are not relabeled Mariwork.
- Woo Product title/H1 is the primary visible identity; default Rank Math Product SEO title target is `%title%` unless a justified page exception exists.
- Title normalization does not authorize URL/slug changes.

## Archive / hub content blocks

DEC-130 applies to every durable indexable archive/hub used as a Search/user destination.

Required characteristics:
- short;
- unique to that archive;
- useful to a human;
- explains what the page is, why it exists and what the user finds there;
- informed by later query/topic research where relevant;
- no filler, stuffing or mechanically duplicated intros.

Applies to Shop, durable Product Categories, pa_volume, Academy hub/archive, Magazine hub/archive, durable Blog Categories and equivalent future durable archives.

## Academy ↔ Magazine boundary

- Academy = video-first practical/demo/instructional intent.
- Magazine = text-first explanatory/reference/editorial intent.
- Topic overlap alone is not cannibalization.
- If two pages still serve substantially the same intent/content, resolve with evidence through differentiation, merge or redirect under DEC-119.

## Internal linking

Canonical rules:
- `strategy/INTERNAL-LINK-ARCHITECTURE.md`
- `strategy/INTERNAL-LINK-REQUIREMENT-MATRIX.md`

Key constraints:
- durable parent/hub hierarchy is mandatory where applicable;
- cross-family links are relevance-driven and are not mandatory by default;
- no fixed internal-link counts;
- no mass keyword auto-linking;
- no Page→Query anchor inference without evidence.

## Semantic positioning foundation

DEC-121 is upstream of keyword/topic expansion.

Mariwork content strategy is built around approved semantic/value directions including:
- fabric suitability;
- application quality;
- durability/stability;
- compatibility;
- economic value.

“Economic value” means evidence-backed useful performance/quality/efficiency/reduced waste or rework, not “lowest price”.

Exact mechanisms, superiority claims, safety claims and measurable performance claims require the evidence standard in DEC-125 before publication.

## Topic / cluster workflow

1. Start from DEC-121 semantic positioning.
2. Research real user problems/intents and query clusters under DEC-122.
3. Assign one primary durable page-family owner under DEC-123.
4. Design the user journey/coverage across families under DEC-124.
5. Apply claim evidence gates under DEC-125.
6. Use internal links to connect genuinely complementary steps.
7. Avoid doorway-like keyword variants and duplicate same-intent pages.

## Evidence boundaries

- Page+Query ownership is not inferred from independent Page and Query exports.
- Search demand may refine wording and prioritization but cannot invent product/brand positioning.
- Product facts, compatibility, durability, coverage, efficiency, safety or superiority are never invented.
- Exact per-page copy remains implementation/content work under approved strategy and QA.

## Implementation gate

This strategy file authorizes no Production write by itself.

A scoped implementation still requires:
- accepted blocking decisions;
- Strategy Lock;
- Execution Backlog item;
- exact entities/URLs;
- evidence inputs;
- change dossier/canary where applicable;
- Codex QA and ChatGPT Final QA.
