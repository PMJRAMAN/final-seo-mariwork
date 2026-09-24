# Query / Intent Map — Round 1

**Task:** A-018 · **Status:** CODEX_AUDITED · **Authority:** evidence and initial recommendations only
**Framework:** v1.0 · **Date:** 2026-09-24

## Evidence contract

Primary inputs are data/normalized/round1-foundation-context.json, data/normalized/round1-evidence-summary.json, data/normalized/gsc-pages.json, A-016 and A-017. The GSC export is page-dimension history only. **Page-query relationship is not proven by the current export.** Separate Pages.csv and Queries.csv are not semantically joined here.

The map is a site/family intent map, not query attribution to named URLs. Target entities are architectural candidates; exact assignment needs joined Page+Query evidence, SERP research and Second Review. No keyword-density, causation or ranking-guarantee claim is made.

## Initial map

| ID | Query/theme | Intent | Candidate target role | Supporting roles | Evidence / limitation | Status |
|---|---|---|---|---|---|---|
| Q-01 | رنگ پارچه / خرید رنگ پارچه | Transactional/discovery | Shop or durable fabric-color category | Products; education | /shop/ is a top page (5,728 clicks; 75,811 impressions); page-only GSC | INITIAL |
| Q-02 | رنگ پارچه [color] / برند+کد | Exact transactional lookup | Individual fabric-color product | Category; sibling colors; education | 83 public products; title patterns vary; no query relation | INITIAL |
| Q-03 | ست رنگ پارچه [count/volume] | Bundle selection | Durable set/bundle product | Colors; volume siblings; category | 22 public yith_bundle products; contents/identity need verification | INITIAL |
| Q-04 | مدیوم/فیکساتیو/زیرساز/وارنیش | Product education/transactional | Medium family or product | Relevant lesson/article | Product families observed; parent/variant completeness blocked | INITIAL |
| Q-05 | ابزار چاپ/نقاشی روی پارچه | Solution discovery | Tools/accessories category or product | Technique education | Heat pen, tampon and stencil-brush examples observed | INITIAL |
| Q-06 | آموزش نقاشی/چاپ روی پارچه | Informational/how-to | Academy lesson or article | Relevant product/category | 37 lesson rows and 12 posts; page metrics do not prove query mapping | INITIAL |
| Q-07 | تثبیت/شست‌وشو/آماده‌سازی پارچه | Risk reduction | Article or lesson | Fixative/medium; category | Existing editorial/education families; facts require verification | INITIAL |
| Q-08 | تفاوت رنگ اکریلیک و پارچه | Comparison | Durable article or lesson | Fabric-color category/products | One article: 2,750 clicks/94,152 impressions page-only; not attribution | INITIAL |
| Q-09 | پارچه مناسب نقاشی/چاپ | Informational decision | Article or lesson | Category/products | Existing article has page-only history (741/9,933) | INITIAL |
| Q-10 | برند/محصول ماری‌ورک | Branded navigation/transactional | Brand-owned shop/category/product | About/Academy/articles | Brand tokens inconsistent across sampled title/H1 families | INITIAL |
| Q-11 | باتیک/شیبوری/استنسیل/چاپ | Technique learning | Academy lesson or article | Technique products | Academy and article families observed; some CPT access blocked | INITIAL |
| Q-12 | رنگ/حجم/کد/ست مشابه | Comparison/selection | Category, set or product family | Siblings and volume attributes | 3 volume rows and a sampled facet; combinations not exhaustive | INITIAL |
| Q-13 | Legacy product/article/education | Navigational recovery | Verified current equivalent only after identity review | Durable category/article | A-012: 67 GSC sources end at 404; equivalence unproven | BLOCKED |
| Q-14 | Product Tag / Blog Tag | Ambiguous archive | No durable target assigned in Round 1 | Migration destination after evidence | 275 product-tag and 53 post-tag rows; sampled behaviors differ | BLOCKED |

## Controls

1. High page clicks/impressions are importance signals only; they do not identify causing queries.
2. Product/category/article overlap is a hypothesis. Do not canonicalize, merge, redirect or rewrite from this map alone.
3. Legacy metrics remain on exact source URLs. A redirect proves transport, not entity equivalence.
4. Product Tags and Blog Tags are separate family-level decommission programs, not per-tag target maps or model audits.

## Second Review evidence needed

- Joined Page+Query export or direct filtered evidence; until then target URL = UNKNOWN_NEEDS_VERIFICATION.
- Current SERP composition and intent for material clusters.
- Verified product/category/lesson/article facts and identity.
- Family link graph and Rank Math capability/owner evidence.

**Google basis:** GOOGLE_CONSISTENT for evidence separation, duplicate-intent caution and no invented facts. References: [Search Console performance reporting](https://support.google.com/webmasters/answer/7576553), [canonicalization](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls), [faceted navigation](https://developers.google.com/crawling/docs/faceted-navigation).
