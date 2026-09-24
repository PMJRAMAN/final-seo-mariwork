# A-011 — Content types, taxonomies and archive map
**Task:** A-011 · **Program:** FOUNDATION / STORE-FIRST · **Framework:** 1.0 · **Dossier schema:** NOT_APPLICABLE (sitewide report; frozen 13-column inventory preserved).
**Date:** 2026-09-24 · **Lifecycle:** CODEX_AUDITED · **Completeness:** public census with explicit access blockers, not an exhaustive WordPress database census.
**Authority:** INITIAL research and recommendations only. No Production change, tag removal, final disposition, or approval. MASTER-TODO and systemic registry are outside this task’s write allowlist.

## Result
Observed 23 REST-declared post types, 15 REST-declared taxonomies, and three additional Woo global attribute taxonomies. Public collections contain 83 products, 12 posts, 15 pages and zero artist objects. Products comprise **60 variable, 22 yith_bundle and one simple**. Product variations and private/internal objects are not counted as zero when inaccessible.
**Product Tags:** 275 terms; all report count 0; all 83 public products return empty product_tag arrays, independently consistent with empty Store API tags. **Blog Tags:** 54 terms, six with nonzero counts, 39 assignments across all 12 public posts. Critically, post_tag is also registered on courses, lessons and groups; their assignments remain BLOCKED_BY_ACCESS. Neither tag system was removed.
Reconciliation retains **555 inventory rows**, with no new concrete URL discovered. It adds object-level product types and assignments, per-term current counts and tag assignment IDs, volume term IDs, registered type/taxonomy declarations, and archive evidence. Existing academy and artists URL identities are preserved and their type is clarified to archive. New family coverage is metadata within the existing unexposed-CPT policy; no invented public URL or duplicate term entity was added.

## Evidence and reproducibility
- Collection began `2026-09-24T16:15:32.504736+00:00`; archive samples below carry exact UTC timestamps. Anonymous GET only; User-Agent `Mariwork-SEO-ReadOnly-A011/1.0`; sequential requests, 25-second timeout, no authentication or forms. No cart/order/customer/user routes, DB connection or WP bootstrap.
- `/wp-json/wp/v2/types` and `/taxonomies` supply registration declarations exposed to REST; absence here does not prove a type/taxonomy is unregistered in WordPress. `has_archive` is a declaration, not proof of HTTP accessibility. Public/queryable flags and complete rewrite rules: UNKNOWN_NEEDS_VERIFICATION.
- Collections requested `per_page=100&page=N`, following all advertised pages, and `hide_empty=false` for WP terms. Fields restricted to public object IDs, links, status, hierarchy, taxonomy IDs and counts; Store API adds type, categories/tags and attributes. Product tags use three pages; other successful content/term collections one. All successful enumerated WP term/content collections match advertised totals. No truncation cap reached.
- Initial `_fields` filtering on associative type/taxonomy discovery returned unusable empty arrays; retried without that filter. Those empty responses were not used as absence evidence.
- Temporary Python requests/HTMLParser scripts computed joins by exact type+object ID or taxonomy+term ID, never by slug semantics. Durable derived evidence is in this report and `notes.a011_*` in the CSV. Existing aliases, HTTP history, IDs and final dispositions are preserved; percent-encoding case is not treated as a redirect. Attribute IDs enrich existing rows without renaming them.
- Input inventory SHA-256: `d56a21b0a5145163eff2cd2618cce71226812c071558355d1e57bcab2d716da8`. Source baseline: [A-010](A-010-inventory-notes.md), particularly media counts and six child-sitemap totals; those historical same-day observations are not represented as new A-011 fetches.
- Production path probe `/home/mariwork/web/mariwork.ir/public_html` returned Permission denied. The configured runner isolation is documented in automation/README.md. No escalation or secret read attempted. Full runtime registry, DB-status counts, hidden assignments, variation parents/children, bundle contents and installed plugin configuration: BLOCKED_BY_ACCESS.
- GSC exports were not joined or reprocessed. **Page-query relationship is not proven by the current export.** Per-URL live Google indexation, inbound-link value and current Page+Query data: NOT_AVAILABLE. Inventory or sitemap inclusion is not proof of indexation.

### Request ledger
| Source URL (exact query) | HTTP | Advertised objects | Advertised pages |
| --- | --- | --- | --- |
| https://www.mariwork.ir/wp-json/wp/v2/types | 200 | NOT_AVAILABLE | NOT_AVAILABLE |
| https://www.mariwork.ir/wp-json/wp/v2/taxonomies | 200 | NOT_AVAILABLE | NOT_AVAILABLE |
| https://www.mariwork.ir/wp-json/wp/v2/categories?per_page=100&page=1&_fields=id%2Cslug%2Clink%2Ctaxonomy%2Cparent%2Ccount&hide_empty=false | 200 | 12 | 1 |
| https://www.mariwork.ir/wp-json/wp/v2/tags?per_page=100&page=1&_fields=id%2Cslug%2Clink%2Ctaxonomy%2Cparent%2Ccount&hide_empty=false | 200 | 54 | 1 |
| https://www.mariwork.ir/wp-json/wp/v2/menus?per_page=100&page=1&_fields=id%2Cslug%2Clink%2Ctaxonomy%2Cparent%2Ccount&hide_empty=false | 401 | NOT_AVAILABLE | NOT_AVAILABLE |
| https://www.mariwork.ir/wp-json/wp/v2/wp_pattern_category?per_page=100&page=1&_fields=id%2Cslug%2Clink%2Ctaxonomy%2Cparent%2Ccount&hide_empty=false | 200 | 0 | 0 |
| https://www.mariwork.ir/wp-json/wp/v2/product_brand?per_page=100&page=1&_fields=id%2Cslug%2Clink%2Ctaxonomy%2Cparent%2Ccount&hide_empty=false | 200 | 0 | 0 |
| https://www.mariwork.ir/wp-json/wp/v2/product_cat?per_page=100&page=1&_fields=id%2Cslug%2Clink%2Ctaxonomy%2Cparent%2Ccount&hide_empty=false | 200 | 9 | 1 |
| https://www.mariwork.ir/wp-json/wp/v2/product_tag?per_page=100&page=1&_fields=id%2Cslug%2Clink%2Ctaxonomy%2Cparent%2Ccount&hide_empty=false | 200 | 275 | 3 |
| https://www.mariwork.ir/wp-json/wp/v2/product_tag?per_page=100&page=2&_fields=id%2Cslug%2Clink%2Ctaxonomy%2Cparent%2Ccount&hide_empty=false | 200 | 275 | 3 |
| https://www.mariwork.ir/wp-json/wp/v2/product_tag?per_page=100&page=3&_fields=id%2Cslug%2Clink%2Ctaxonomy%2Cparent%2Ccount&hide_empty=false | 200 | 275 | 3 |
| https://www.mariwork.ir/wp-json/wp/v2/ld_course_category?per_page=100&page=1&_fields=id%2Cslug%2Clink%2Ctaxonomy%2Cparent%2Ccount&hide_empty=false | 200 | 2 | 1 |
| https://www.mariwork.ir/wp-json/wp/v2/ld_course_tag?per_page=100&page=1&_fields=id%2Cslug%2Clink%2Ctaxonomy%2Cparent%2Ccount&hide_empty=false | 200 | 0 | 0 |
| https://www.mariwork.ir/wp-json/wp/v2/ld_lesson_category?per_page=100&page=1&_fields=id%2Cslug%2Clink%2Ctaxonomy%2Cparent%2Ccount&hide_empty=false | 200 | 0 | 0 |
| https://www.mariwork.ir/wp-json/wp/v2/ld_lesson_tag?per_page=100&page=1&_fields=id%2Cslug%2Clink%2Ctaxonomy%2Cparent%2Ccount&hide_empty=false | 200 | 0 | 0 |
| https://www.mariwork.ir/wp-json/wp/v2/ld_topic_category?per_page=100&page=1&_fields=id%2Cslug%2Clink%2Ctaxonomy%2Cparent%2Ccount&hide_empty=false | 200 | 0 | 0 |
| https://www.mariwork.ir/wp-json/wp/v2/ld_topic_tag?per_page=100&page=1&_fields=id%2Cslug%2Clink%2Ctaxonomy%2Cparent%2Ccount&hide_empty=false | 200 | 0 | 0 |
| https://www.mariwork.ir/wp-json/wp/v2/ld_group_category?per_page=100&page=1&_fields=id%2Cslug%2Clink%2Ctaxonomy%2Cparent%2Ccount&hide_empty=false | 200 | 0 | 0 |
| https://www.mariwork.ir/wp-json/wp/v2/ld_group_tag?per_page=100&page=1&_fields=id%2Cslug%2Clink%2Ctaxonomy%2Cparent%2Ccount&hide_empty=false | 200 | 0 | 0 |
| https://www.mariwork.ir/wp-json/wp/v2/posts?per_page=100&page=1&_fields=id%2Clink%2Ctype%2Cstatus%2Cparent%2Ctags%2Ccategories%2Cproduct_tag%2Cproduct_cat%2Cproduct_brand | 200 | 12 | 1 |
| https://www.mariwork.ir/wp-json/wp/v2/pages?per_page=100&page=1&_fields=id%2Clink%2Ctype%2Cstatus%2Cparent%2Ctags%2Ccategories%2Cproduct_tag%2Cproduct_cat%2Cproduct_brand | 200 | 15 | 1 |
| https://www.mariwork.ir/wp-json/wp/v2/product?per_page=100&page=1&_fields=id%2Clink%2Ctype%2Cstatus%2Cparent%2Ctags%2Ccategories%2Cproduct_tag%2Cproduct_cat%2Cproduct_brand | 200 | 83 | 1 |
| https://www.mariwork.ir/wp-json/wp/v2/artists?per_page=100&page=1&_fields=id%2Clink%2Ctype%2Cstatus%2Cparent%2Ctags%2Ccategories%2Cproduct_tag%2Cproduct_cat%2Cproduct_brand | 200 | 0 | 0 |
| https://www.mariwork.ir/wp-json/wp/v2/sfwd-courses?per_page=100&page=1&_fields=id%2Clink%2Ctype%2Cstatus%2Cparent%2Ctags%2Ccategories%2Cproduct_tag%2Cproduct_cat%2Cproduct_brand | 401 | NOT_AVAILABLE | NOT_AVAILABLE |
| https://www.mariwork.ir/wp-json/wp/v2/sfwd-lessons?per_page=100&page=1&_fields=id%2Clink%2Ctype%2Cstatus%2Cparent%2Ctags%2Ccategories%2Cproduct_tag%2Cproduct_cat%2Cproduct_brand | 401 | NOT_AVAILABLE | NOT_AVAILABLE |
| https://www.mariwork.ir/wp-json/wp/v2/sfwd-topic?per_page=100&page=1&_fields=id%2Clink%2Ctype%2Cstatus%2Cparent%2Ctags%2Ccategories%2Cproduct_tag%2Cproduct_cat%2Cproduct_brand | 401 | NOT_AVAILABLE | NOT_AVAILABLE |
| https://www.mariwork.ir/wp-json/wp/v2/sfwd-quiz?per_page=100&page=1&_fields=id%2Clink%2Ctype%2Cstatus%2Cparent%2Ctags%2Ccategories%2Cproduct_tag%2Cproduct_cat%2Cproduct_brand | 401 | NOT_AVAILABLE | NOT_AVAILABLE |
| https://www.mariwork.ir/wp-json/wc/store/v1/products?per_page=100&page=1&_fields=id%2Cpermalink%2Ctype%2Ccategories%2Ctags%2Cattributes%2Cis_variation%2Cparent_id | 200 | 83 | 1 |
| https://www.mariwork.ir/wp-json/wc/store/v1/products/attributes | 200 | NOT_AVAILABLE | NOT_AVAILABLE |


## Post types / CPTs
Counts below describe returned public objects, not all stored statuses. Core content, custom content, editor objects and operational candidates remain distinct. No learner/group membership or question/exam content was collected.
| Type | REST collection | has_archive | Registered taxonomies | Count | Scope |
| --- | --- | --- | --- | --- | --- |
| post | wp/v2/posts | false | category, post_tag | 12 | public collection |
| page | wp/v2/pages | false | NOT_APPLICABLE | 15 | public collection |
| attachment | wp/v2/media | false | NOT_APPLICABLE | 626 / advertised 845 (A-010) | 219-object discrepancy unresolved; not recollected |
| nav_menu_item | wp/v2/menu-items | false | nav_menu | UNKNOWN_NEEDS_VERIFICATION | declaration only; internal/learning collection not enumerated |
| wp_block | wp/v2/blocks | false | wp_pattern_category | UNKNOWN_NEEDS_VERIFICATION | declaration only; internal/learning collection not enumerated |
| wp_template | wp/v2/templates | false | NOT_APPLICABLE | UNKNOWN_NEEDS_VERIFICATION | declaration only; internal/learning collection not enumerated |
| wp_template_part | wp/v2/template-parts | false | NOT_APPLICABLE | UNKNOWN_NEEDS_VERIFICATION | declaration only; internal/learning collection not enumerated |
| wp_global_styles | wp/v2/global-styles | false | NOT_APPLICABLE | UNKNOWN_NEEDS_VERIFICATION | declaration only; internal/learning collection not enumerated |
| wp_navigation | wp/v2/navigation | false | NOT_APPLICABLE | UNKNOWN_NEEDS_VERIFICATION | declaration only; internal/learning collection not enumerated |
| wp_font_family | wp/v2/font-families | false | NOT_APPLICABLE | UNKNOWN_NEEDS_VERIFICATION | declaration only; internal/learning collection not enumerated |
| wp_font_face | wp/v2/font-families/(?P<font_family_id>[\d]+)/font-faces | false | NOT_APPLICABLE | UNKNOWN_NEEDS_VERIFICATION | declaration only; internal/learning collection not enumerated |
| mariwork_artist | wp/v2/artists | artists | NOT_APPLICABLE | 0 | public collection |
| product | wp/v2/product | shop | product_brand, product_cat, product_tag | 83 | public collection |
| sfwd-courses | wp/v2/sfwd-courses | true | category, post_tag, ld_course_category, ld_course_tag | BLOCKED_BY_ACCESS | 401; course/lesson sitemap evidence in A-010 |
| sfwd-lessons | wp/v2/sfwd-lessons | false | category, post_tag, ld_lesson_category, ld_lesson_tag | BLOCKED_BY_ACCESS | 401; course/lesson sitemap evidence in A-010 |
| sfwd-topic | wp/v2/sfwd-topic | false | ld_topic_category, ld_topic_tag | BLOCKED_BY_ACCESS | 401; course/lesson sitemap evidence in A-010 |
| sfwd-quiz | wp/v2/sfwd-quiz | false | NOT_APPLICABLE | BLOCKED_BY_ACCESS | 401; course/lesson sitemap evidence in A-010 |
| sfwd-question | wp/v2/sfwd-question | false | NOT_APPLICABLE | UNKNOWN_NEEDS_VERIFICATION | declaration only; internal/learning collection not enumerated |
| ld-exam | wp/v2/ld-exam | false | NOT_APPLICABLE | UNKNOWN_NEEDS_VERIFICATION | declaration only; internal/learning collection not enumerated |
| groups | wp/v2/groups | true | category, post_tag, ld_group_category, ld_group_tag | UNKNOWN_NEEDS_VERIFICATION | declaration only; internal/learning collection not enumerated |
| ct_content_block | wp/v2/ct_content_block | false | NOT_APPLICABLE | UNKNOWN_NEEDS_VERIFICATION | declaration only; internal/learning collection not enumerated |
| gspbstylebook | wp/v2/gspbstylebook | false | NOT_APPLICABLE | UNKNOWN_NEEDS_VERIFICATION | declaration only; internal/learning collection not enumerated |
| rm_content_editor | wp/v2/rm_content_editor | false | NOT_APPLICABLE | UNKNOWN_NEEDS_VERIFICATION | declaration only; internal/learning collection not enumerated |

`product_variation`, Woo operational/order types, non-REST CPTs and non-REST taxonomies such as product-type/visibility controls cannot be exhaustively mapped from these declarations. These are verification gaps, not assertions of installed registrations; no order census is needed for SEO. An authorized sanitized runtime export should list registry names/public flags and aggregate non-sensitive content counts, excluding records and PII.

## Public families and route map
| Family | Observed pattern / identity | Coverage and next owner |
| --- | --- | --- |
| Homepage / static / system pages | /; page REST links (15 objects) | A-010: 14 page-classified rows, plus shop special case; C, D, H |
| Blog posts / index | /mag/articles/{slug}/; /mag/ | 12 posts; /mag/ has blog body class; legacy /articles/ evidence preserved; E |
| Products / shop | /shop/{slug}/; /shop/ | 83 products plus one shop row; Woo product archive overlaps a WP page identity; B0/B1–B6 |
| Course archive / course | /academy/; /academy/{slug}/ | A-010: one course plus archive; archive now HTML-confirmed; F |
| Lessons | /academy/{course}/lessons/{slug}/ | 37 A-010 lesson entities; REST 401; legacy /education/ preserved; F |
| Topics / quizzes / questions / exams / groups | UNKNOWN_NEEDS_VERIFICATION | CPT declarations only; groups has_archive=true does not establish a route; F/G-004/H-014 |
| Artists | /artists/ | Archive confirmed HTTP 200 despite public artist collection total 0; historical artist URLs remain; G |
| FAQ / history | Historical /yith_faq_cat/{slug}/; history content may be posts | Two FAQ legacy URLs were 404 in A-010; no current FAQ CPT demonstrated; G/H |
| Attributes | /volume/{30ml,60ml,250ml}/ | Three existing rows now linked to pa_volume term IDs; pa_brand/pa_color archive flags false; B8-008 |
| Author / date | UNKNOWN_NEEDS_VERIFICATION | Explicit existing policy rows; no concrete route verified; H-003/H-004 |
| Media / attachment | Returned attachment links and /wp-content/uploads/… | Existing policy partitions retain A-010 evidence; attachment redirect policy incomplete; H-005 |
| Search / facets / pagination / feeds | s, post_type, filter_volume, query_type_volume, /page/N/, /feed/ | Existing A-010 spaces retained; not an exhaustive combination crawl; B0/B9/H |
| Cart / checkout / account / actions | Existing A-010 URL evidence | No transactional tests; retain independent system policies; H-009–H-012 |
| Editor / navigation / internal custom objects | REST declarations only | nav_menu, wp_pattern_category, editor CPTs; no indexable-page assumption; H-014 |


## Taxonomy census
WP term counts were collected with hide_empty=false. A term’s returned link is an advertised archive address, not proof that the address responds 200. Counts are term-object counts reported by the endpoint; they are not Google indexed-page counts.
| Taxonomy | Object types | Hierarchical | Returned terms | Nonzero terms / sum count |
| --- | --- | --- | --- | --- |
| category | post, sfwd-courses, sfwd-lessons, groups | True | 12 | 2 / 15 |
| post_tag | post, sfwd-courses, sfwd-lessons, groups | False | 54 | 6 / 39 |
| nav_menu | nav_menu_item | False | BLOCKED_BY_ACCESS | BLOCKED_BY_ACCESS |
| wp_pattern_category | wp_block | False | 0 | 0 / 0 |
| product_brand | product | True | 0 | 0 / 0 |
| product_cat | product | True | 9 | 7 / 105 |
| product_tag | product | False | 275 | 0 / 0 |
| ld_course_category | sfwd-courses | True | 2 | 0 / 0 |
| ld_course_tag | sfwd-courses | False | 0 | 0 / 0 |
| ld_lesson_category | sfwd-lessons | True | 0 | 0 / 0 |
| ld_lesson_tag | sfwd-lessons | False | 0 | 0 / 0 |
| ld_topic_category | sfwd-topic | True | 0 | 0 / 0 |
| ld_topic_tag | sfwd-topic | False | 0 | 0 / 0 |
| ld_group_category | groups | True | 0 | 0 / 0 |
| ld_group_tag | groups | False | 0 | 0 / 0 |

Newly explicit relative to the A-010 report: nav_menu (401), wp_pattern_category (0 public terms), ld_group_category (0), ld_group_tag (0), pa_brand, pa_color and pa_volume. Empty collections remain registered families. Missing-family registration coverage is stored under SPACE-UNEXPOSED-CPT. Existing TODO owners F0-002, G-004, H-014 and B0-005 cover follow-up; runner/human planning may add child tasks. MASTER-TODO was not edited under the task-specific prohibition.

### Taxonomy route patterns

- `category`: returned links use `/mag/{slug}/`; exact 12 IDs, parent IDs and links remain in inventory. This differs from historical `/category/` aliases.
- `product_cat`: `/product/{slug}/` and hierarchical `/product/{parent}/{child}/`; nine terms. These archive routes are distinct from product singles under `/shop/`.
- `post_tag`: `/mag/tag/{slug}/`; 54 advertised links in the complete ledger below.
- `product_tag`: `/product-tag/{slug}/`; 275 advertised links below.
- `ld_course_category`: `/mag/course-category/{slug}/`; IDs 1989 and 1990, two advertised terms (exact links in inventory).
- `pa_volume`: `/volume/{slug}/`; three existing archive rows, independent of tag removal.
- All other REST taxonomies have zero returned public terms or an access blocker; concrete public archive URL patterns are `UNKNOWN_NEEDS_VERIFICATION`. Do not derive public routes from REST base names. `pa_brand` and `pa_color` report `has_archives=false`; no public archive URLs were invented.

### Woo attributes (separate from Product Tags)
| Attribute ID / taxonomy | Store declaration count | has_archives | Term endpoint returned IDs / counts |
| --- | --- | --- | --- |
| 1 / pa_brand | 1 | False | 0 returned; total NOT_AVAILABLE |
| 2 / pa_color | 3 | False | 0 returned; total NOT_AVAILABLE |
| 3 / pa_volume | 3 | True | 1908:250ml=11, 1906:30ml=56, 1907:60ml=56 |

pa_brand declares count 1 and pa_color count 3, while their Store term endpoints returned empty lists. Do not conclude there are no stored terms; hide-empty behavior or other filters require verification. pa_volume declares three terms and returns three. `product_brand` is a distinct registered taxonomy with zero public terms; it must not be merged with pa_brand. Attribute terms/endpoints and declarations are preserved in inventory metadata.
Four public products expose local non-taxonomy variation attributes: WP-27903 (دورگیر), WP-27680 (رنگ), WP-24183 (سایز), WP-23912 (رنگ). These do not establish additional public taxonomy archives. Full product-attribute arrays are preserved under product a011_objects. Bundle membership and variation ID/parent totals remain BLOCKED_BY_ACCESS; product names are not used to infer type.

### Product type assignment census
| Woo product type | Public count | Exact WP product IDs |
| --- | --- | --- |
| variable | 60 | 12009, 12471, 12475, 12479, 12484, 12488, 12492, 12498, 12502, 12506, 12511, 12516, 12520, 12524, 12528, 12532, 12536, 12541, 12544, 12548, 12581, 12585, 12588, 12591, 12594, 14446, 14448, 14449, 14450, 23912, 24183, 24252, 27025, 27034, 27037, 27039, 27041, 27043, 27046, 27051, 27054, 27142, 27149, 27328, 27333, 27369, 27378, 27384, 27386, 27506, 27512, 27621, 27680, 27893, 27901, 27903, 28232, 28239, 28242, 28244 |
| yith_bundle | 22 | 12597, 12602, 12605, 12608, 14465, 14466, 14471, 17265, 25397, 27396, 28610, 28623, 28627, 33318, 33319, 33320, 33322, 33323, 33324, 33325, 33326, 33327 |
| simple | 1 | 24043 |

Store API and WP product collections have identical sets of 83 IDs. No grouped/external products were returned; this does not verify whether those or other product types are registered or used in unpublished objects. Woo type is saved separately from the WP post type product and business family products.

## Tag assignments and controlled-decommission scope
**Existing project direction, not a Google requirement:** B8-001–B8-007 and E0-007–E0-012 plan controlled removal of Product Tags and Blog Tags. This report supplies an initial inventory only. Count 0, HTTP 404 or noindex alone is not authorization to delete terms or choose redirects.
| System | Terms | Zero / nonzero count | Public object assignments | Remaining scope |
| --- | --- | --- | --- | --- |
| product_tag | 275 | 275 / 0 | 0 across 83/83 public products; WP and Store agree | Private/draft products and DB relationships BLOCKED_BY_ACCESS |
| post_tag | 54 | 48 / 6 | 39 across 12/12 public posts; six distinct assigned terms | Courses, lessons, groups and nonpublic status assignments BLOCKED_BY_ACCESS |

Blog Tag shared registration is confirmed by both the type and taxonomy declarations. Sum of public-post assignments equals sum of reported term counts (39), but that equality does not prove absence of assignments on other post types or statuses. Tag assignment cleanup must explicitly include that unresolved scope.

### Nonzero Blog Tag assignment matrix
| Term ID | Decoded slug (label only) | REST count | Exact public post IDs |
| --- | --- | --- | --- |
| 211 | تاریخچه-چاپ-و-نقاشی-پارچه | 3 | 22196, 22197, 22193 |
| 183 | چاپ-پارچه | 3 | 22196, 22197, 22193 |
| 167 | راهنما | 9 | 26387, 22192, 22194, 13320, 13318, 13316, 13312, 13305, 13295 |
| 166 | رنگ-پارچه | 9 | 26387, 22192, 22194, 13320, 13318, 13316, 13312, 13305, 13295 |
| 210 | مقاله | 12 | 26387, 22192, 22196, 22197, 22194, 22193, 13320, 13318, 13316, 13312, 13305, 13295 |
| 168 | نقاشی-پارچه | 3 | 22196, 22197, 22193 |

All 48 other Blog Tags and all 275 Product Tags have an explicit empty public assignment list in the inventory. The complete term ledger below includes every term; object URLs are available by WP ID in existing inventory evidence. Empty lists mean no assignments in the enumerated public collection, not no database relationships.

## Archive HTTP samples and sitemap evidence
Fresh initial HTML samples only, no rendered-JS claim. Canonical absence = NOT_AVAILABLE. All listed samples had no HTTP redirect; requests percent-encoded/uppercased some URL bytes without a redirect. Full original/final spellings and body classes are retained below or in inventory notes.
| Requested URL | HTTP | Canonical | Robots | Observed UTC |
| --- | --- | --- | --- | --- |
| https://www.mariwork.ir/mag/ | 200 | https://www.mariwork.ir/mag/ | index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large | 2026-09-24T16:17:05.914865+00:00 |
| https://www.mariwork.ir/academy/ | 200 | https://www.mariwork.ir/academy/ | index, follow | 2026-09-24T16:17:05.939861+00:00 |
| https://www.mariwork.ir/artists/ | 200 | https://www.mariwork.ir/artists/ | index, follow | 2026-09-24T16:17:05.963407+00:00 |
| https://www.mariwork.ir/volume/30ml/ | 200 | https://www.mariwork.ir/volume/30ml/ | index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large | 2026-09-24T16:17:06.017631+00:00 |
| https://www.mariwork.ir/product-tag/16-%d9%85%d8%af%db%8c%d9%88%d9%85/ | 200 | NOT_AVAILABLE | follow, noindex | 2026-09-24T16:17:06.042723+00:00 |
| https://www.mariwork.ir/mag/tag/bootcamp/ | 404 | NOT_AVAILABLE | follow, noindex | 2026-09-24T16:17:07.310667+00:00 |
| https://www.mariwork.ir/mag/tag/%d8%aa%d8%a7%d8%b1%db%8c%d8%ae%da%86%d9%87-%da%86%d8%a7%d9%be-%d9%88-%d9%86%d9%82%d8%a7%d8%b4%db%8c-%d9%be%d8%a7%d8%b1%da%86%d9%87/ | 404 | NOT_AVAILABLE | follow, noindex | 2026-09-24T16:17:08.582950+00:00 |

The two sampled Blog Tag routes (one count 0, one count 3) both returned 404. The sampled Product Tag route (term 1895, count 0) returned 200 with noindex and no canonical. These observations do not establish behavior for all tags. WordPress-advertised route /mag/tag/{slug}/ must not be confused with historical /tag/{slug}/ aliases; legacy chains remain A-010/A-012 evidence.
Fresh sitemap index: HTTP 200, Rank Math generator marker, the same six listed children: post, page, product, sfwd-courses, sfwd-lessons and category. No tag, product-category, attribute or artist child sitemap is listed. Child files were not re-fetched in A-011; A-010 counted 147 entries / 146 distinct URLs. No claim is made that an unlisted sitemap cannot exist. No sitemap inclusion or exclusion change is proposed.

## Inventory reconciliation and remaining gaps
All 352 returned term IDs (12 categories + 54 Blog Tags + 9 Product Categories + 275 Product Tags + 2 course categories) map to existing exact REST identities. Inventory has only 53 post_tag-family rows, seven product_cat-family rows and 13 category-family rows: A-010 grouped URLs by observed HTTP destination, so row counts are not term counts. All 54/9/12 term identities remain present inside evidence, including identities grouped under another target. New a011_terms preserves that distinction; no term is silently dropped.
All 110 public content objects (12 posts + 15 pages + 83 products) map to existing exact REST identities. Woo types add an orthogonal classification; product subfamilies are not inferred from type or tag names. No newly collected term/content link is missing from existing URL evidence. Artists/academy archives were already rows and are now typed from observed HTML. Volume IDs 1906/1907/1908 enrich existing provisional URL entities without creating duplicate rows.
Completeness gaps: non-REST registered types/taxonomies; private/unpublished status counts and relationships; LearnDash assignments; full variations and bundle composition; attribute empty-list discrepancy; author/date routes; attachment 626/845 discrepancy inherited from A-010; internal-editor object counts; exact rewrite rules; Google indexation/history and inbound links; installed Rank Math ownership/configuration. None is represented as zero or resolved.

## Findings — INITIAL, task-local IDs
The systemic registry was read and contains no registered entries. It is outside ALLOWED WRITES. IDs below are unique task-local findings pending A-020 registration as SYS IDs; no SYS number is claimed/reserved and no governance file was edited.
### A-011-F001
```yaml
id: "A-011-F001"
severity: "P2"
scope: "SITEWIDE"
status: "BLOCKED"
evidence_class: "OBSERVED"
confidence: "HIGH"
source_refs: "Production permission denial; REST type/taxonomy ledger; A-010 media gap"
impact: "Public discovery cannot certify all current runtime types, statuses and relationships."
recommendation: "Obtain an authorized sanitized read-only runtime registry/aggregate content export; reconcile with the 23/15/3 public declarations and exact IDs."
acceptance_criteria: "Every registry type/taxonomy classified as public, internal or excluded with reason; public entity counts reconcile or retain explicit blocker; no PII export."
google_basis: "PROJECT_DECISION"
google_reference: "NOT_APPLICABLE (completeness verification is a project process requirement)"
seo_owner_current: "UNKNOWN_NEEDS_VERIFICATION; public sitemap generator attributes only sitemap output to Rank Math"
seo_owner_target: "RANK_MATH where installed capability verified; taxonomy assignment ownership requires platform verification"
rank_math_capability_checked: "BLOCKED_BY_ACCESS"
rank_math_path_or_reason_not_used: "Installed version/modules/settings/hooks inaccessible; no technical setting or replacement code selected"
```

### A-011-F002
```yaml
id: "A-011-F002"
severity: "P2"
scope: "FAMILY"
status: "OPEN"
evidence_class: "OBSERVED"
confidence: "HIGH"
source_refs: "post_tag declaration; 54-term ledger; 39-assignment matrix; LearnDash 401 responses"
impact: "Blog Tag decommission could omit course/lesson/group usage if restricted to posts. Current cross-type usage is unknown."
recommendation: "Extend decommission research to every registered post_tag object type, all relevant statuses, historical URLs and links; prepare a Change Dossier before any cleanup."
acceptance_criteria: "Each of 54 terms has verified relationships or explicit blocker, per-URL history/value review, proposed destination rationale, link cleanup, rollback and regression scope for Second Review."
google_basis: "PROJECT_DECISION"
google_reference: "https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes (GOOGLE_CONSISTENT for migration preparation, not tag-removal direction)"
seo_owner_current: "UNKNOWN_NEEDS_VERIFICATION; public sitemap generator attributes only sitemap output to Rank Math"
seo_owner_target: "RANK_MATH where installed capability verified; taxonomy assignment ownership requires platform verification"
rank_math_capability_checked: "BLOCKED_BY_ACCESS"
rank_math_path_or_reason_not_used: "Installed version/modules/settings/hooks inaccessible; no technical setting or replacement code selected"
```

### A-011-F003
```yaml
id: "A-011-F003"
severity: "P2"
scope: "FAMILY"
status: "OPEN"
evidence_class: "OBSERVED"
confidence: "HIGH"
source_refs: "Archive sample term IDs 1988, 211, 1895; tag ledger"
impact: "REST-advertised archive URLs do not imply live archive success; assigned Blog Tag 211 responds 404. This complicates migration inventory, without proving traffic loss."
recommendation: "Investigate rewrite/output ownership and exact legacy/current URL behavior across both tag systems before choosing dispositions; retain 275 Product Tags despite zero public usage."
acceptance_criteria: "Each tag address/history has HTTP chain, canonical, sitemap/link evidence and proposed decision; verify representative empty/nonempty/legacy samples and all assigned Blog Tag routes; no blanket redirect mapping."
google_basis: "GOOGLE_CONSISTENT"
google_reference: "https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes"
seo_owner_current: "UNKNOWN_NEEDS_VERIFICATION; public sitemap generator attributes only sitemap output to Rank Math"
seo_owner_target: "RANK_MATH where installed capability verified; taxonomy assignment ownership requires platform verification"
rank_math_capability_checked: "BLOCKED_BY_ACCESS"
rank_math_path_or_reason_not_used: "Installed version/modules/settings/hooks inaccessible; no technical setting or replacement code selected"
```


## Ownership, initial research order and Google basis
Rank Math installed version, Free/Pro status, enabled modules, Advanced Mode, taxonomy title/robots/canonical/sitemap/redirection capabilities, filters and duplicate owners: BLOCKED_BY_ACCESS. Public sitemap generator is observed as Rank Math; exact robots/canonical owner UNKNOWN_NEEDS_VERIFICATION. Target SEO owner remains RANK_MATH wherever installed support is verified. A-014/A-015 must verify capability before any technical target state; no custom substitute is proposed. Term assignments and Woo product types are platform data, separate from Rank Math SEO output.
1. A-012/B8/E0: reconcile per-tag historical and advertised URLs, exact assignments, links and value evidence before Second Review. Proposed decommission is PROJECT_DECISION. Preparing corresponding URL mappings, updating links and monitoring is GOOGLE_CONSISTENT with [Google site-move guidance](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes). No final 301/410/noindex destination is selected; unrelated blanket redirects are not a substitute for mapping.
2. A-013/F/G/H: retain every newly explicit family and resolve archive/registration gaps. Inventory methodology is GOOGLE_CONSISTENT with [sitemap overview](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview): sitemaps aid discovery but do not guarantee crawling/indexing. The public census cannot establish complete coverage alone.
3. B8/E0: inventory current internal tag links before any approved cleanup, following [Google crawlable-link guidance](https://developers.google.com/search/docs/crawling-indexing/links-crawlable) (GOOGLE_CONSISTENT). This task did not calculate a complete link graph or claim orphan status.
All three official Google references were opened on 2026-09-24. They support investigation and migration principles, not a claim that Google requires removing tags or that removal improves rankings. Regression set for a future Change Dossier: nonempty Blog Tag 211, empty Blog Tag 1988, Product Tag 1895, a tagged post, each accessible LearnDash type, /mag/, /academy/, /shop/, and /volume/30ml/. Per-URL policy, canary, rollback triggers and final acceptance remain Second Review/human decisions.

## Validation
- CSV retains its 13 columns, 555 unique row IDs, all prior evidence and NOT_DECIDED dispositions. Existing object/term IDs were joined exactly. Both tag assignment matrices are reproducible from per-object arrays; 83 WP/Store product IDs match; Blog Tag reported counts equal the 39 public-post assignments.
- Only this report and registry/URL-INVENTORY.csv are modified. No Production, raw export, governance, template, MASTER-TODO or registry finding write. No credentials, cookie headers, customer/order records or learner data persisted. All recommendations remain INITIAL; page lifecycle and final dispositions are unchanged.

## Complete tag ledger
Public archive URL is the REST-advertised URL. HTTP/canonical observations are separate evidence, not implied by this column. The inventory row locator may reference a merged target and must not be mistaken for a one-row-per-term model. Assigned IDs for nonzero Blog Tags are in the matrix above and for every term in CSV a011_terms.
### product_tag
| Term ID | Reported count | Public assigned IDs | Inventory row | Advertised archive URL |
| --- | --- | --- | --- | --- |
| 138 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-138 | https://www.mariwork.ir/product-tag/%d9%87%d8%af%db%8c%d9%87/ |
| 221 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-221 | https://www.mariwork.ir/product-tag/%d8%ae%d9%88%d8%af%da%a9%d8%a7%d8%b1-%d8%ad%d8%b1%d8%a7%d8%b1%d8%aa%db%8c%d8%8c-%d8%ae%d9%88%d8%af%da%a9%d8%a7%d8%b1%d8%8c-%d8%b7%d8%b1%d8%a7%d8%ad%db%8c%d8%8c-%d9%86%d9%82%d8%a7%d8%b4%db%8c%d8%8c/ |
| 223 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-223 | https://www.mariwork.ir/product-tag/%d8%aa%d8%a7%d9%85%d9%be%d9%88%d9%86/ |
| 224 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-224 | https://www.mariwork.ir/product-tag/%da%86%d8%a7%d9%be-%d9%85%d9%87%d8%b1/ |
| 225 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-225 | https://www.mariwork.ir/product-tag/%d9%85%d9%87%d8%b1/ |
| 226 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-226 | https://www.mariwork.ir/product-tag/%d8%a7%d8%b3%d9%81%d9%86%d8%ac/ |
| 227 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-227 | https://www.mariwork.ir/product-tag/%d8%b2%d8%b1%d8%af%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c/ |
| 228 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-228 | https://www.mariwork.ir/product-tag/%d8%b2%d8%b1%d8%af%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c-%d8%b1%d9%86%da%af-%d9%85%d8%ae%d8%b5/ |
| 229 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-229 | https://www.mariwork.ir/product-tag/%d8%a2%d8%ac%d8%b1%db%8c%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c-%d8%b1%d9%86%da%af-%d9%85%d8%ae/ |
| 230 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-230 | https://www.mariwork.ir/product-tag/%d8%b3%d8%a8%d8%b2%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c-%d8%b1%d9%86%da%af-%d9%85%d8%ae%d8%b5/ |
| 231 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-231 | https://www.mariwork.ir/product-tag/%d8%a8%d9%86%d9%81%d8%b4%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c-%d8%b1%d9%86%da%af-%d9%85%d8%ae/ |
| 232 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-232 | https://www.mariwork.ir/product-tag/%d8%a7%da%a9%d8%b1%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c-%d8%b1%d9%86%da%af-%d9%85%d8%ae%d8%b5/ |
| 233 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-233 | https://www.mariwork.ir/product-tag/%d9%82%d9%87%d9%88%d9%87%d8%a7%db%8c-%d8%b4%da%a9%d9%84%d8%a7%d8%aa%db%8c%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c/ |
| 234 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-234 | https://www.mariwork.ir/product-tag/%d9%82%d9%87%d9%88%d9%87%d8%a7%db%8c%d8%8c-%d8%b4%da%a9%d9%84%d8%a7%d8%aa%db%8c%d8%8c-%d9%82%d9%87%d9%88%d9%87%d8%a7%db%8c-%d8%b4%da%a9%d9%84%d8%a7%d8%aa%db%8c%d8%8c-60%d9%85%db%8c/ |
| 235 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-235 | https://www.mariwork.ir/product-tag/%d8%b3%d8%a8%d8%b2%d8%8c-%d8%b2%db%8c%d8%aa%d9%88%d9%86%db%8c%d8%8c-%d8%b3%d8%a8%d8%b2-%d8%b2%db%8c%d8%aa%d9%88%d9%86%db%8c%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86/ |
| 236 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-236 | https://www.mariwork.ir/product-tag/%d8%b7%d9%84%d8%a7%db%8c%db%8c%d8%8c-%d8%b7%d9%84%d8%a7%db%8c%db%8c-%d8%b1%d9%88%d8%b4%d9%86%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1/ |
| 237 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-237 | https://www.mariwork.ir/product-tag/%d9%86%d8%a7%d8%b1%d9%86%d8%ac%db%8c%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c-%d8%b1%d9%86%da%af/ |
| 238 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-238 | https://www.mariwork.ir/product-tag/%d9%82%d9%87%d9%88%d9%87%d8%a7%db%8c%d8%8c-%d8%aa%db%8c%d8%b1%d9%87%d8%8c-%d9%82%d9%87%d9%88%d9%87%d8%a7%db%8c-%d8%aa%db%8c%d8%b1%d9%87%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86/ |
| 239 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-239 | https://www.mariwork.ir/product-tag/%d9%81%db%8c%d8%b1%d9%88%d8%b2%d9%87%d8%a7%db%8c%d8%8c-%d9%81%db%8c%d8%b1%d9%88%d8%b2%d9%87-%d8%a7%db%8c%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87/ |
| 240 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-240 | https://www.mariwork.ir/product-tag/%d8%b7%d9%84%d8%a7%db%8c%db%8c%d8%8c-%d8%aa%db%8c%d8%b1%d9%87%d8%8c-%d8%b7%d9%84%d8%a7%db%8c%db%8c-%d8%aa%db%8c%d8%b1%d9%87%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86/ |
| 241 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-241 | https://www.mariwork.ir/product-tag/%d9%82%d8%b1%d9%85%d8%b2%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c-%d8%b1%d9%86%da%af-%d9%85%d8%ae/ |
| 242 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-242 | https://www.mariwork.ir/product-tag/%d8%b3%db%8c%d8%a7%d9%87%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c-%d8%b1%d9%86%da%af-%d9%85%d8%ae/ |
| 243 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-243 | https://www.mariwork.ir/product-tag/%d8%a2%d8%a8%db%8c%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c-%d8%b1%d9%86%da%af-%d9%85%d8%ae%d8%b5/ |
| 244 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-244 | https://www.mariwork.ir/product-tag/%d9%85%d8%b3%db%8c%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c-%d8%b1%d9%86%da%af-%d9%85%d8%ae%d8%b5/ |
| 245 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-245 | https://www.mariwork.ir/product-tag/%d8%b3%d8%b1%d8%ae%d8%8c-%d8%a2%d8%a8%db%8c%d8%8c-%d8%b3%d8%b1%d8%ae%d8%a2%d8%a8%db%8c%d8%8c-%d8%b3%d8%b1%d8%ae-%d8%a2%d8%a8%db%8c%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be/ |
| 246 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-246 | https://www.mariwork.ir/product-tag/%d8%b3%d9%81%db%8c%d8%af%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c-%d8%b1%d9%86%da%af-%d9%85%d8%ae/ |
| 247 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-247 | https://www.mariwork.ir/product-tag/%d8%ae%d8%a7%da%a9%d8%b3%d8%aa%d8%b1%db%8c%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c-%d8%b1%d9%86%da%af/ |
| 248 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-248 | https://www.mariwork.ir/product-tag/%d9%be%d9%88%d8%b3%d8%aa%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d9%88%d8%b3%d8%aa%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88/ |
| 249 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-249 | https://www.mariwork.ir/product-tag/%d8%b2%d8%b1%d8%af%d8%8c-%d9%81%d9%84%d9%88%d8%b1%d8%8c-%d9%81%d9%84%d9%88%d8%b1%d8%b3%d8%aa%d8%8c-%d8%b2%d8%b1%d8%af-%d9%81%d9%84%d9%88%d8%b1%d8%b3%d9%86%d8%aa%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1/ |
| 250 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-250 | https://www.mariwork.ir/product-tag/%d9%86%d8%a7%d8%b1%d9%86%d8%ac%db%8c%d8%8c-%d9%81%d9%84%d9%88%d8%b1%d8%8c-%d9%81%d9%84%d9%88%d8%b1%d8%b3%d8%aa%d8%8c-%d9%86%d8%a7%d8%b1%d9%86%d8%ac%db%8c-%d9%81%d9%84%d9%88%d8%b1%d8%b3%d9%86%d8%aa/ |
| 251 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-251 | https://www.mariwork.ir/product-tag/%d8%b3%d8%a8%d8%b2%d8%8c-%d9%81%d9%84%d9%88%d8%b1%d8%8c-%d9%81%d9%84%d9%88%d8%b1%d8%b3%d8%aa%d8%8c-%d8%b3%d8%a8%d8%b2-%d9%81%d9%84%d9%88%d8%b1%d8%b3%d9%86%d8%aa%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1/ |
| 252 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-252 | https://www.mariwork.ir/product-tag/%d8%b5%d9%88%d8%b1%d8%aa%db%8c%d8%8c-%d9%81%d9%84%d9%88%d8%b1%d8%8c-%d9%81%d9%84%d9%88%d8%b1%d8%b3%d8%aa%d8%8c-%d8%b5%d9%88%d8%b1%d8%aa%db%8c-%d9%81%d9%84%d9%88%d8%b1%d8%b3%d9%86%d8%aa%d8%8c-60%d9%85/ |
| 253 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-253 | https://www.mariwork.ir/product-tag/%d8%a7%da%a9%d9%84%db%8c%d9%84%d8%8c-%d8%b7%d9%84%d8%a7%db%8c%db%8c%d8%8c-%d8%a7%da%a9%d9%84%db%8c%d9%84-%d8%b7%d9%84%d8%a7%db%8c%db%8c%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7/ |
| 254 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-254 | https://www.mariwork.ir/product-tag/%d8%a7%da%a9%d9%84%db%8c%d9%84%d8%8c-%d9%86%d9%82%d8%b1%d9%87%d8%a7%db%8c%d8%8c-%d9%86%d9%82%d8%b1%d9%87-%d8%a7%db%8c%d8%8c-%d8%a7%da%a9%d9%84%db%8c%d9%84-%d9%86%d9%82%d8%b1%d9%87/ |
| 255 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-255 | https://www.mariwork.ir/product-tag/%da%86%d8%b3%d8%a8%d8%8c-%d8%a7%da%a9%d9%84%db%8c%d9%84%d8%8c-%da%86%d8%b3%d8%a8-%d8%a7%da%a9%d9%84%db%8c%d9%84%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c/ |
| 256 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-256 | https://www.mariwork.ir/product-tag/%d8%ab%d8%a8%d8%a7%d8%aa%d8%8c-%d8%ab%d8%a8%d8%a7%d8%aa-%d8%af%d9%87%d9%86%d8%af%d9%87%d8%8c-%d8%ab%d8%a8%d8%a7%d8%aa%d8%af%d9%87%d9%86%d8%af%d9%87%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1/ |
| 257 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-257 | https://www.mariwork.ir/product-tag/%d8%b2%db%8c%d8%b1%d8%b3%d8%a7%d8%b2%d8%8c-%d8%b2%db%8c%d8%b1%d8%b3%d8%a7%d8%b2-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c/ |
| 258 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-258 | https://www.mariwork.ir/product-tag/%d8%b3%d8%aa%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c-%d8%b1%d9%86%da%af-%d9%85%d8%ae%d8%b5%d9%88/ |
| 259 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-259 | https://www.mariwork.ir/product-tag/%d8%b3%d8%aa%d8%8c-%d8%b3%d8%aa-%db%b8-%d8%b1%d9%86%da%af%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c/ |
| 260 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-260 | https://www.mariwork.ir/product-tag/%d8%b3%d8%aa%d8%8c-%d8%b3%d8%aa-12-%d8%b1%d9%86%da%af%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c-%d8%b1/ |
| 261 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-261 | https://www.mariwork.ir/product-tag/%d8%b3%d8%aa%d8%8c-%d8%b3%d8%aa-%da%a9%d8%a7%d9%85%d9%84%d8%8c-%d8%a7%d9%81%d8%b2%d9%88%d8%af%d9%86%db%8c%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c/ |
| 262 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-262 | https://www.mariwork.ir/product-tag/%d8%b3%d8%aa%d8%8c-%d8%b3%d8%aa-6-%d8%b1%d9%86%da%af%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c-%d8%b1/ |
| 263 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-263 | https://www.mariwork.ir/product-tag/%d8%b3%d8%aa%d8%8c-%d8%b3%d8%aa-%db%b8-%d8%b1%d9%86%da%af%d8%8c-250-%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c/ |
| 264 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-264 | https://www.mariwork.ir/product-tag/%d8%b3%d8%aa%d8%8c-%d8%b3%d8%aa-5-%d8%b1%d9%86%da%af%d8%8c-30-%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c-%d8%b1/ |
| 265 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-265 | https://www.mariwork.ir/product-tag/%d8%b3%d8%aa%d8%8c-%d8%b3%d8%aa-4-%d8%b1%d9%86%da%af%d8%8c-%d9%81%d9%84%d9%88%d8%b1%d8%b3%d9%86%d8%aa%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85/ |
| 266 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-266 | https://www.mariwork.ir/product-tag/%d8%b2%d8%b1%d8%af%d8%8c-250%d9%85%db%8c%d9%84%d8%8c-250-%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c-%d8%b1%d9%86/ |
| 267 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-267 | https://www.mariwork.ir/product-tag/%d8%b3%d8%a8%d8%b2%d8%8c-250%d9%85%db%8c%d9%84%d8%8c-250-%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c-%d8%b1%d9%86/ |
| 268 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-268 | https://www.mariwork.ir/product-tag/%d8%a8%d9%86%d9%81%d8%b4%d8%8c-250%d9%85%db%8c%d9%84%d8%8c-250-%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c-%d8%b1/ |
| 269 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-269 | https://www.mariwork.ir/product-tag/%d8%a7%da%a9%d8%b1%d8%8c-250%d9%85%db%8c%d9%84%d8%8c-250-%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c-%d8%b1%d9%86/ |
| 270 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-270 | https://www.mariwork.ir/product-tag/%d8%b3%d8%a8%d8%b2%d8%8c-%d8%b2%db%8c%d8%aa%d9%88%d9%86%db%8c%d8%8c-%d8%b3%d8%a8%d8%b2-%d8%b2%db%8c%d8%aa%d9%88%d9%86%db%8c%d8%8c-250%d9%85%db%8c%d9%84%d8%8c-250-%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86/ |
| 271 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-271 | https://www.mariwork.ir/product-tag/%d9%81%db%8c%d8%b1%d9%88%d8%b2%d9%87%d8%a7%db%8c%d8%8c-%d9%81%db%8c%d8%b1%d9%88%d8%b2%d9%87-%d8%a7%db%8c%d8%8c-250%d9%85%db%8c%d9%84%d8%8c-250-%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af/ |
| 272 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-272 | https://www.mariwork.ir/product-tag/%d9%82%d8%b1%d9%85%d8%b2%d8%8c-250%d9%85%db%8c%d9%84%d8%8c-250-%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c-%d8%b1/ |
| 273 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-273 | https://www.mariwork.ir/product-tag/%d8%b3%db%8c%d8%a7%d9%87%d8%8c-250%d9%85%db%8c%d9%84%d8%8c-250-%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c-%d8%b1/ |
| 274 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-274 | https://www.mariwork.ir/product-tag/%d8%b3%db%8c%d8%a7%d9%87%d8%8c-%d9%85%d8%b4%da%a9%db%8c%d8%8c-250%d9%85%db%8c%d9%84%d8%8c-250-%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c/ |
| 275 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-275 | https://www.mariwork.ir/product-tag/%d8%a2%d8%a8%db%8c%d8%8c-250%d9%85%db%8c%d9%84%d8%8c-250-%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c-%d8%b1%d9%86/ |
| 276 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-276 | https://www.mariwork.ir/product-tag/%d8%b3%d8%b1%d8%ae%d8%8c-%d8%a2%d8%a8%db%8c%d8%8c-%d8%b3%d8%b1%d8%ae%d8%a2%d8%a8%db%8c%d8%8c-%d8%b3%d8%b1%d8%ae-%d8%a2%d8%a8%db%8c%d8%8c-250%d9%85%db%8c%d9%84%d8%8c-250-%d9%85%db%8c%d9%84/ |
| 277 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-277 | https://www.mariwork.ir/product-tag/%d8%b3%d9%81%db%8c%d8%af%d8%8c-250%d9%85%db%8c%d9%84%d8%8c-250-%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c-%d8%b1/ |
| 278 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-278 | https://www.mariwork.ir/product-tag/%d8%a8%d8%b1%d8%a7%d8%b4/ |
| 279 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-279 | https://www.mariwork.ir/product-tag/%d8%a7%d8%b3%d8%aa%d9%86%d8%b3%db%8c%d9%84/ |
| 280 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-280 | https://www.mariwork.ir/product-tag/%d8%a8%d8%b1%d8%a7%d8%b4-%d8%a7%d8%b3%d8%aa%d9%86%d8%b3%db%8c%d9%84/ |
| 281 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-281 | https://www.mariwork.ir/product-tag/%d8%a7%d8%a8%d8%b2%d8%a7%d8%b1/ |
| 282 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-282 | https://www.mariwork.ir/product-tag/%d8%a7%d8%a8%d8%b2%d8%a7%d8%b1%d9%87%d8%a7/ |
| 283 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-283 | https://www.mariwork.ir/product-tag/%da%86%d8%a7%d9%be-%d9%be%d8%a7%d8%b1%da%86%d9%87/ |
| 284 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-284 | https://www.mariwork.ir/product-tag/%d9%82%d9%84%d9%85%d9%88/ |
| 285 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-285 | https://www.mariwork.ir/product-tag/%d9%82%d9%84%d9%85%d9%88-%d8%a7%d8%b3%d8%aa%d9%86%d8%b3%db%8c%d9%84/ |
| 286 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-286 | https://www.mariwork.ir/product-tag/%d9%85%d8%af%db%8c%d9%88%d9%85/ |
| 287 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-287 | https://www.mariwork.ir/product-tag/%d9%85%d8%af%db%8c%d9%88%d9%85-%d9%be%d9%81%da%a9%db%8c/ |
| 288 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-288 | https://www.mariwork.ir/product-tag/texture-medium/ |
| 289 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-289 | https://www.mariwork.ir/product-tag/medium/ |
| 290 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-290 | https://www.mariwork.ir/product-tag/%d9%be%d9%81%da%a9%db%8c/ |
| 291 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-291 | https://www.mariwork.ir/product-tag/%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9/ |
| 300 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-300 | https://www.mariwork.ir/product-tag/%d8%b8%d8%b1%d9%81-%d9%86%da%af%d9%87%d8%af%d8%a7%d8%b1%d9%86%d8%af%d9%87-%d8%b1%d9%86%da%af/ |
| 301 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-301 | https://www.mariwork.ir/product-tag/%d8%b8%d8%b1%d9%81/ |
| 302 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-302 | https://www.mariwork.ir/product-tag/%d9%86%da%af%d9%87%d8%af%d8%a7%d8%b1%d9%86%d8%af%d9%87/ |
| 303 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-303 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af/ |
| 304 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-304 | https://www.mariwork.ir/product-tag/%d9%86%da%af%d9%87%d8%af%d8%a7%d8%b1%db%8c/ |
| 305 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-305 | https://www.mariwork.ir/product-tag/%d8%b8%d8%b1%d9%88%d9%81/ |
| 306 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-306 | https://www.mariwork.ir/product-tag/%d8%b4%d9%81%d8%a7%d9%81/ |
| 307 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-307 | https://www.mariwork.ir/product-tag/%d8%b3%d8%aa-12-%d8%b1%d9%86%da%af/ |
| 308 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-308 | https://www.mariwork.ir/product-tag/30-%d9%85%db%8c%d9%84/ |
| 309 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-309 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87/ |
| 310 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-310 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%85%d8%ae%d8%b5%d9%88%d8%b5-%d9%be%d8%a7%d8%b1%da%86%d9%87/ |
| 311 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-311 | https://www.mariwork.ir/product-tag/mariwork/ |
| 312 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-312 | https://www.mariwork.ir/product-tag/%d8%b3%d8%aa/ |
| 1754 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1754 | https://www.mariwork.ir/product-tag/%d9%82%d8%b1%d9%85%d8%b2-%d8%a7%d8%b3%da%a9%d8%a7%d8%b1%d9%84%d8%aa/ |
| 1755 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1755 | https://www.mariwork.ir/product-tag/scarlet-red/ |
| 1756 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1756 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%82%d8%b1%d9%85%d8%b2-%d8%a7%d8%b3%da%a9%d8%a7%d8%b1%d9%84%d8%aa/ |
| 1757 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1757 | https://www.mariwork.ir/product-tag/%d9%82%d8%b1%d9%85%d8%b2/ |
| 1758 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1758 | https://www.mariwork.ir/product-tag/60%d9%85%db%8c%d9%84/ |
| 1759 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1759 | https://www.mariwork.ir/product-tag/permanet-rose/ |
| 1760 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1760 | https://www.mariwork.ir/product-tag/%d8%b5%d9%88%d8%b1%d8%aa%db%8c-%d9%be%d8%b1%d9%85%d9%86%d8%aa-%d8%b1%d9%8f%d8%b2/ |
| 1761 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1761 | https://www.mariwork.ir/product-tag/%d8%b5%d9%88%d8%b1%d8%aa%db%8c/ |
| 1762 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1762 | https://www.mariwork.ir/product-tag/light-pink/ |
| 1763 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1763 | https://www.mariwork.ir/product-tag/%d8%b5%d9%88%d8%b1%d8%aa%db%8c-%d8%b1%d9%88%d8%b4%d9%86/ |
| 1764 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1764 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d8%b5%d9%88%d8%b1%d8%aa%db%8c-%d8%b1%d9%88%d8%b4%d9%86/ |
| 1765 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1765 | https://www.mariwork.ir/product-tag/%da%af%d9%84%d8%a8%d9%87%db%8c/ |
| 1766 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1766 | https://www.mariwork.ir/product-tag/papaya/ |
| 1767 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1767 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87-%da%af%d9%84%d8%a8%d9%87%db%8c/ |
| 1768 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1768 | https://www.mariwork.ir/product-tag/%db%8c%d8%a7%d8%b3%db%8c/ |
| 1769 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1769 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%db%8c%d8%a7%d8%b3%db%8c/ |
| 1770 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1770 | https://www.mariwork.ir/product-tag/lilac/ |
| 1771 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1771 | https://www.mariwork.ir/product-tag/%d8%a8%d9%86%d9%81%d8%b4-%d9%81%d9%84%d9%88%d8%b1%d8%b3%d9%86%d8%aa/ |
| 1772 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1772 | https://www.mariwork.ir/product-tag/fluorescent-purple/ |
| 1773 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1773 | https://www.mariwork.ir/product-tag/%d8%a8%d9%86%d9%81%d8%b4-%d9%84%d9%88%d9%86%d8%af%d8%b1/ |
| 1774 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1774 | https://www.mariwork.ir/product-tag/lavender/ |
| 1775 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1775 | https://www.mariwork.ir/product-tag/sky-blue/ |
| 1776 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1776 | https://www.mariwork.ir/product-tag/%d8%a2%d8%a8%db%8c-%d8%a2%d8%b3%d9%85%d8%a7%d9%86%db%8c/ |
| 1777 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1777 | https://www.mariwork.ir/product-tag/%d8%a2%d8%a8%db%8c-%d8%b3%db%8c%d8%a7%d9%86/ |
| 1778 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1778 | https://www.mariwork.ir/product-tag/cyan/ |
| 1779 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1779 | https://www.mariwork.ir/product-tag/yellow/ |
| 1780 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1780 | https://www.mariwork.ir/product-tag/green/ |
| 1781 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1781 | https://www.mariwork.ir/product-tag/red/ |
| 1782 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1782 | https://www.mariwork.ir/product-tag/blue/ |
| 1783 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1783 | https://www.mariwork.ir/product-tag/black/ |
| 1784 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1784 | https://www.mariwork.ir/product-tag/%d8%b3%db%8c%d8%a7%d9%87%d8%8c-60%d9%85%db%8c%d9%84%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c-%d9%85%d8%b4%da%a9%db%8c%d8%8c/ |
| 1785 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1785 | https://www.mariwork.ir/product-tag/violet/ |
| 1786 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1786 | https://www.mariwork.ir/product-tag/%d8%a7%d9%8f%da%a9%d8%b1/ |
| 1787 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1787 | https://www.mariwork.ir/product-tag/ochre/ |
| 1788 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1788 | https://www.mariwork.ir/product-tag/olivegreen/ |
| 1789 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1789 | https://www.mariwork.ir/product-tag/olive-green/ |
| 1790 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1790 | https://www.mariwork.ir/product-tag/turquose-blue/ |
| 1791 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1791 | https://www.mariwork.ir/product-tag/magenta/ |
| 1792 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1792 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87-%d9%86%d8%a7%d8%b1%d9%86%d8%ac%db%8c-%d9%be%d8%a7%d9%be%d8%a7%db%8c%d8%a7/ |
| 1793 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1793 | https://www.mariwork.ir/product-tag/%d8%a2%d8%a8%db%8c/ |
| 1794 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1794 | https://www.mariwork.ir/product-tag/%d8%b3%d8%a8%d8%b2/ |
| 1795 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1795 | https://www.mariwork.ir/product-tag/%d8%b3%d8%a8%d8%b2-%da%86%d9%85%d9%86%db%8c/ |
| 1796 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1796 | https://www.mariwork.ir/product-tag/green-grass/ |
| 1797 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1797 | https://www.mariwork.ir/product-tag/%d9%be%d8%a7%d9%be%d8%a7%db%8c%d8%a7/ |
| 1798 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1798 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87-%d9%be%d8%a7%d9%be%d8%a7%db%8c%d8%a7/ |
| 1799 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1799 | https://www.mariwork.ir/product-tag/red-brown/ |
| 1800 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1800 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87-%d8%a2%d8%ac%d8%b1%db%8c/ |
| 1801 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1801 | https://www.mariwork.ir/product-tag/saddlebrown/ |
| 1802 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1802 | https://www.mariwork.ir/product-tag/%d9%82%d9%87%d9%88%d9%87-%d8%a7%db%8c-%d8%b4%da%a9%d9%84%d8%a7%d8%aa%db%8c/ |
| 1803 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1803 | https://www.mariwork.ir/product-tag/light-gold/ |
| 1804 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1804 | https://www.mariwork.ir/product-tag/orange/ |
| 1805 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1805 | https://www.mariwork.ir/product-tag/darkbrown/ |
| 1806 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1806 | https://www.mariwork.ir/product-tag/brown/ |
| 1807 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1807 | https://www.mariwork.ir/product-tag/light-salmon/ |
| 1808 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1808 | https://www.mariwork.ir/product-tag/%d9%84%db%8c%d9%85%d9%88%db%8c%db%8c/ |
| 1809 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1809 | https://www.mariwork.ir/product-tag/lemon/ |
| 1810 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1810 | https://www.mariwork.ir/product-tag/%d9%86%d9%82%d8%b1%d9%87-%d8%a7%db%8c/ |
| 1811 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1811 | https://www.mariwork.ir/product-tag/silver/ |
| 1812 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1812 | https://www.mariwork.ir/product-tag/%d9%86%d9%82%d8%b1%d9%87%d8%a7%db%8c/ |
| 1813 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1813 | https://www.mariwork.ir/product-tag/%d8%b5%d8%af%d9%81%db%8c/ |
| 1814 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1814 | https://www.mariwork.ir/product-tag/%d8%b3%d9%81%db%8c%d8%af-%d8%b5%d8%af%d9%81%db%8c/ |
| 1815 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1815 | https://www.mariwork.ir/product-tag/pearl/ |
| 1816 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1816 | https://www.mariwork.ir/product-tag/%d9%85%d8%af%db%8c%d9%88%d9%85-%da%af%d9%84%db%8c%d8%aa%d8%b1/ |
| 1817 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1817 | https://www.mariwork.ir/product-tag/%da%af%d9%84%db%8c%d8%aa%d8%b1/ |
| 1818 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1818 | https://www.mariwork.ir/product-tag/%da%af%d9%84%db%8c%d8%aa%d8%b1-%d9%87%d9%81%d8%aa-%d8%b1%d9%86%da%af/ |
| 1819 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1819 | https://www.mariwork.ir/product-tag/rainbow-glitter/ |
| 1820 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1820 | https://www.mariwork.ir/product-tag/%da%af%d9%84%db%8c%d8%aa%d8%b1-%d9%86%d9%82%d8%b1%d9%87%d8%a7%db%8c/ |
| 1821 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1821 | https://www.mariwork.ir/product-tag/%da%af%d9%84%db%8c%d8%aa%d8%b1-%d9%86%d9%82%d8%b1%d9%87-%d8%a7%db%8c/ |
| 1822 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1822 | https://www.mariwork.ir/product-tag/silver-glitter/ |
| 1823 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1823 | https://www.mariwork.ir/product-tag/%da%af%d9%84%db%8c%d8%aa%d8%b1-%d8%b7%d9%84%d8%a7%db%8c%db%8c/ |
| 1824 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1824 | https://www.mariwork.ir/product-tag/%d8%b7%d9%84%d8%a7%db%8c%db%8c/ |
| 1825 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1825 | https://www.mariwork.ir/product-tag/golden-glitter/ |
| 1826 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1826 | https://www.mariwork.ir/product-tag/gold/ |
| 1827 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1827 | https://www.mariwork.ir/product-tag/gold-glitter/ |
| 1828 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1828 | https://www.mariwork.ir/product-tag/%d9%87%d9%81%d8%aa-%d8%b1%d9%86%da%af/ |
| 1829 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1829 | https://www.mariwork.ir/product-tag/glitter/ |
| 1830 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1830 | https://www.mariwork.ir/product-tag/rainbow/ |
| 1831 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1831 | https://www.mariwork.ir/product-tag/%d9%85%d8%af%db%8c%d9%88%d9%85-%d8%b1%d9%88%d8%b4%d9%86-%da%a9%d9%86%d9%86%d8%af%d9%87/ |
| 1832 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1832 | https://www.mariwork.ir/product-tag/%d8%b1%d9%88%d8%b4%d9%86-%da%a9%d9%86%d9%86%d8%af%d9%87/ |
| 1833 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1833 | https://www.mariwork.ir/product-tag/lightening-medium/ |
| 1834 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1834 | https://www.mariwork.ir/product-tag/thickening-medium/ |
| 1835 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1835 | https://www.mariwork.ir/product-tag/thickening/ |
| 1836 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1836 | https://www.mariwork.ir/product-tag/%d8%ba%d9%84%d8%b8%d8%aa-%d8%af%d9%87%d9%86%d8%af%d9%87/ |
| 1837 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1837 | https://www.mariwork.ir/product-tag/%d8%ba%d9%84%d8%b8%d8%aa/ |
| 1838 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1838 | https://www.mariwork.ir/product-tag/%d8%aa%d9%88%d8%aa%da%a9%d8%a7%d9%84%db%8c/ |
| 1839 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1839 | https://www.mariwork.ir/product-tag/%da%86%d8%b3%d8%a8/ |
| 1840 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1840 | https://www.mariwork.ir/product-tag/%d8%b7%d9%84%d8%a7/ |
| 1841 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1841 | https://www.mariwork.ir/product-tag/totakali/ |
| 1842 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1842 | https://www.mariwork.ir/product-tag/glue/ |
| 1843 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1843 | https://www.mariwork.ir/product-tag/60-%d9%85%db%8c%d9%84/ |
| 1845 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1845 | https://www.mariwork.ir/product-tag/%d9%88%d8%b1%d9%82-%d8%aa%d9%88%d8%aa%da%a9%d8%a7%d9%84%db%8c/ |
| 1846 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1846 | https://www.mariwork.ir/product-tag/%d8%a2%d8%a8%db%8c-%d8%b3%d8%a7%db%8c%d8%a7%d9%86/ |
| 1847 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1847 | https://www.mariwork.ir/product-tag/%d9%88%d8%a7%d8%b1%d9%86%db%8c%d8%b4/ |
| 1848 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1848 | https://www.mariwork.ir/product-tag/%d9%88%d8%a7%d8%b1%d9%86%db%8c%d8%b4-%d8%a8%d8%b1%d8%a7%d9%82/ |
| 1849 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1849 | https://www.mariwork.ir/product-tag/%da%86%d8%b1%d9%85/ |
| 1850 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1850 | https://www.mariwork.ir/product-tag/%d9%85%d8%ad%d8%a7%d9%81%d8%b8-%d8%b1%d9%86%da%af-%d8%b1%d9%88%db%8c-%da%86%d8%b1%d9%85/ |
| 1851 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1851 | https://www.mariwork.ir/product-tag/%d8%af%d8%b1%d8%ae%d8%b4%d9%86%d8%af%da%af%db%8c/ |
| 1852 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1852 | https://www.mariwork.ir/product-tag/%d8%b3%d8%a7%db%8c%d8%b4/ |
| 1853 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1853 | https://www.mariwork.ir/product-tag/%d8%ae%d8%b1%d8%a7%d8%b4/ |
| 1854 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1854 | https://www.mariwork.ir/product-tag/glossy-varnish/ |
| 1855 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1855 | https://www.mariwork.ir/product-tag/varnish/ |
| 1856 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1856 | https://www.mariwork.ir/product-tag/leather/ |
| 1857 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1857 | https://www.mariwork.ir/product-tag/%d9%88%d8%a7%d8%b1%d9%86%db%8c%d8%b4-%d9%86%db%8c%d9%85%d9%87-%d9%85%d8%a7%d8%aa/ |
| 1858 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1858 | https://www.mariwork.ir/product-tag/semi-matte-varnish/ |
| 1859 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1859 | https://www.mariwork.ir/product-tag/contouring-pot/ |
| 1860 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1860 | https://www.mariwork.ir/product-tag/30%d9%85%db%8c%d9%84/ |
| 1861 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1861 | https://www.mariwork.ir/product-tag/%d8%b8%d8%b1%d9%81-%d8%af%d9%88%d8%b1%da%af%db%8c%d8%b1/ |
| 1862 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1862 | https://www.mariwork.ir/product-tag/%d8%af%d9%88%d8%b1%da%af%db%8c%d8%b1%db%8c-%d9%86%d9%82%d8%a7%d8%b4%db%8c/ |
| 1863 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1863 | https://www.mariwork.ir/product-tag/%d9%86%d9%82%d8%a7%d8%b4%db%8c-%d8%b1%d9%88%db%8c-%d9%be%d8%a7%d8%b1%da%86%d9%87/ |
| 1864 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1864 | https://www.mariwork.ir/product-tag/%d9%87%d9%86%d8%b1/ |
| 1865 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1865 | https://www.mariwork.ir/product-tag/%d8%b5%d9%86%d8%a7%db%8c%d8%b9-%d8%af%d8%b3%d8%aa%db%8c/ |
| 1866 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1866 | https://www.mariwork.ir/product-tag/%d8%aa%d8%b2%d8%a6%db%8c%d9%86/ |
| 1867 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1867 | https://www.mariwork.ir/product-tag/%d8%aa%d8%b2%db%8c%db%8c%d9%86/ |
| 1868 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1868 | https://www.mariwork.ir/product-tag/%d8%b3%d8%aa-5-%d8%b1%d9%86%da%af/ |
| 1869 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1869 | https://www.mariwork.ir/product-tag/%d9%81%d9%84%d9%88%d8%b1%d8%b3%d9%86%d8%aa/ |
| 1870 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1870 | https://www.mariwork.ir/product-tag/%d8%b3%d8%aa-5-%d8%b1%d9%86%da%af-%d9%81%d9%84%d9%88%d8%b1%d8%b3%d9%86%d8%aa-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9/ |
| 1871 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1871 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%81%d9%84%d9%88%d8%b1%d8%b3%d9%86%d8%aa/ |
| 1872 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1872 | https://www.mariwork.ir/product-tag/%da%86%d8%a7%d9%be-%d8%b1%d9%88%db%8c-%d9%be%d8%a7%d8%b1%da%86%d9%87/ |
| 1873 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1873 | https://www.mariwork.ir/product-tag/%d8%b7%d8%b1%d8%ad%d9%87%d8%a7%db%8c-%d8%ae%d9%84%d8%a7%d9%82%d8%a7%d9%86%d9%87/ |
| 1874 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1874 | https://www.mariwork.ir/product-tag/%d8%aa%db%8c%d8%b4%d8%b1%d8%aa-%d9%81%d9%84%d9%88%d8%b1%d8%b3%d9%86%d8%aa/ |
| 1875 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1875 | https://www.mariwork.ir/product-tag/%da%a9%db%8c%d9%81-%d8%af%d8%b3%d8%aa%db%8c/ |
| 1876 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1876 | https://www.mariwork.ir/product-tag/%d8%b4%d8%a7%db%8c%d9%86-%d8%b7%d9%84%d8%a7%db%8c%db%8c/ |
| 1877 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1877 | https://www.mariwork.ir/product-tag/%d8%b4%d8%a7%db%8c%d9%86/ |
| 1878 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1878 | https://www.mariwork.ir/product-tag/golden-color-shine/ |
| 1879 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1879 | https://www.mariwork.ir/product-tag/golden-shine/ |
| 1880 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1880 | https://www.mariwork.ir/product-tag/golden/ |
| 1881 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1881 | https://www.mariwork.ir/product-tag/shine/ |
| 1882 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1882 | https://www.mariwork.ir/product-tag/%d8%b4%d8%a7%db%8c%d9%86-%d9%86%d9%82%d8%b1%d9%87%d8%a7%db%8c/ |
| 1883 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1883 | https://www.mariwork.ir/product-tag/silver-shine/ |
| 1884 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1884 | https://www.mariwork.ir/product-tag/silver-color-shine/ |
| 1885 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1885 | https://www.mariwork.ir/product-tag/%d9%85%d9%88%da%a9%d8%a7/ |
| 1886 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1886 | https://www.mariwork.ir/product-tag/mocha-mousse/ |
| 1887 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1887 | https://www.mariwork.ir/product-tag/mocha/ |
| 1888 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1888 | https://www.mariwork.ir/product-tag/%da%a9%d9%84%d9%87-%d8%ba%d8%a7%d8%b2%db%8c/ |
| 1889 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1889 | https://www.mariwork.ir/product-tag/teal/ |
| 1890 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1890 | https://www.mariwork.ir/product-tag/%d9%86%d8%a7%d8%b2%d9%84/ |
| 1891 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1891 | https://www.mariwork.ir/product-tag/%da%af%d9%88%d8%aa%d8%a7/ |
| 1892 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1892 | https://www.mariwork.ir/product-tag/nozzle/ |
| 1893 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1893 | https://www.mariwork.ir/product-tag/40-%d8%b1%d9%86%da%af/ |
| 1894 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1894 | https://www.mariwork.ir/product-tag/%d8%b3%d8%aa-%da%a9%d8%a7%d9%85%d9%84/ |
| 1895 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1895 | https://www.mariwork.ir/product-tag/16-%d9%85%d8%af%db%8c%d9%88%d9%85/ |
| 1901 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1901 | https://www.mariwork.ir/product-tag/%d8%b2%d8%b1%d8%af%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c-%d8%b1%d9%86%da%af-%d9%85%d8%ae%d8%b5%d9%88%d8%b5-%d9%be%d8%a7%d8%b1/ |
| 1903 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1903 | https://www.mariwork.ir/product-tag/%d9%82%d8%b1%d9%85%d8%b2%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c-%d8%b1%d9%86%da%af-%d9%85%d8%ae%d8%b5%d9%88%d8%b5-%d9%be%d8%a7/ |
| 1904 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1904 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9%d8%8c-%d8%b1%d9%86%da%af-%d9%85%d8%ae%d8%b5%d9%88%d8%b5-%d9%be%d8%a7%d8%b1%da%86%d9%87%d8%8c-%d8%b1%d9%86/ |
| 1905 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1905 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87-%d8%b3%db%8c%d8%a7%d9%87%d8%8c-%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87-%d9%85%d8%b4%da%a9%db%8c%d8%8c-%d8%b1%d9%86%da%af-%d8%b3%db%8c%d8%a7/ |
| 1909 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1909 | https://www.mariwork.ir/product-tag/%d8%b2%d8%b1%d8%af/ |
| 1910 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1910 | https://www.mariwork.ir/product-tag/250%d9%85%db%8c%d9%84/ |
| 1911 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1911 | https://www.mariwork.ir/product-tag/250-%d9%85%db%8c%d9%84/ |
| 1912 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1912 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87-%d8%b2%d8%b1%d8%af/ |
| 1913 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1913 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87-%d8%b2%d8%b1%d8%af-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9/ |
| 1914 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1914 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87-%d8%b3%d8%a8%d8%b2/ |
| 1915 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1915 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87-%d8%b3%d8%a8%d8%b2-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9/ |
| 1916 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1916 | https://www.mariwork.ir/product-tag/purple/ |
| 1917 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1917 | https://www.mariwork.ir/product-tag/%d8%a8%d9%86%d9%81%d8%b4/ |
| 1918 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1918 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87-%d8%a8%d9%86%d9%81%d8%b4/ |
| 1919 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1919 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87-%d8%a8%d9%86%d9%81%d8%b4-%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9/ |
| 1920 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1920 | https://www.mariwork.ir/product-tag/%d8%a2%d8%ac%d8%b1%db%8c/ |
| 1921 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1921 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d8%a2%d8%ac%d8%b1%db%8c-%d9%be%d8%a7%d8%b1%da%86%d9%87/ |
| 1922 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1922 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%86%d9%82%d8%a7%d8%b4%db%8c-%d8%b1%d9%88%db%8c-%d9%be%d8%a7%d8%b1%da%86%d9%87/ |
| 1923 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1923 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%84%d8%a8%d8%a7%d8%b3/ |
| 1924 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1924 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%85%d8%ae%d8%b5%d9%88%d8%b5-%d9%86%d9%82%d8%a7%d8%b4%db%8c-%d8%b1%d9%88%db%8c-%d9%84%d8%a8%d8%a7%d8%b3/ |
| 1925 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1925 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d8%b3%d8%a8%d8%b2-%d9%be%d8%a7%d8%b1%da%86%d9%87/ |
| 1926 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1926 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d8%a8%d9%86%d9%81%d8%b4-%d9%be%d8%a7%d8%b1%da%86%d9%87/ |
| 1927 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1927 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87-%d8%a7%d9%8f%da%a9%d8%b1/ |
| 1928 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1928 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d8%a7%d9%8f%da%a9%d8%b1-%d9%be%d8%a7%d8%b1%da%86%d9%87/ |
| 1929 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1929 | https://www.mariwork.ir/product-tag/chocolate-brown/ |
| 1930 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1930 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87-%d9%82%d9%87%d9%88%d9%87-%d8%a7%db%8c-%d8%b4%da%a9%d9%84%d8%a7%d8%aa%db%8c/ |
| 1931 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1931 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%82%d9%87%d9%88%d9%87-%d8%a7%db%8c-%d8%b4%da%a9%d9%84%d8%a7%d8%aa%db%8c-%d9%be%d8%a7%d8%b1%da%86%d9%87/ |
| 1932 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1932 | https://www.mariwork.ir/product-tag/%d8%b3%d8%a8%d8%b2-%d8%b2%db%8c%d8%aa%d9%88%d9%86%db%8c/ |
| 1933 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1933 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87-%d8%b3%d8%a8%d8%b2-%d8%b2%db%8c%d8%aa%d9%88%d9%86%db%8c/ |
| 1934 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1934 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d8%b3%d8%a8%d8%b2-%d8%b2%db%8c%d8%aa%d9%88%d9%86%db%8c-%d9%be%d8%a7%d8%b1%da%86%d9%87/ |
| 1935 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1935 | https://www.mariwork.ir/product-tag/%d8%b7%d9%84%d8%a7%db%8c%db%8c-%d8%b1%d9%88%d8%b4%d9%86/ |
| 1936 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1936 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87-%d8%b7%d9%84%d8%a7%db%8c%db%8c-%d8%b1%d9%88%d8%b4%d9%86/ |
| 1937 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1937 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d8%b7%d9%84%d8%a7%db%8c%db%8c-%d9%be%d8%a7%d8%b1%da%86%d9%87/ |
| 1938 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1938 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%85%d8%aa%d8%a7%d9%84%db%8c%da%a9-%d9%be%d8%a7%d8%b1%da%86%d9%87/ |
| 1939 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1939 | https://www.mariwork.ir/product-tag/%d9%86%d8%a7%d8%b1%d9%86%d8%ac%db%8c/ |
| 1940 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1940 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87-%d9%86%d8%a7%d8%b1%d9%86%d8%ac%db%8c/ |
| 1941 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1941 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%86%d8%a7%d8%b1%d9%86%d8%ac%db%8c-%d9%be%d8%a7%d8%b1%da%86%d9%87/ |
| 1942 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1942 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%da%af%d8%b1%d9%85-%d9%be%d8%a7%d8%b1%da%86%d9%87/ |
| 1943 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1943 | https://www.mariwork.ir/product-tag/%d9%82%d9%87%d9%88%d9%87-%d8%a7%db%8c/ |
| 1944 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1944 | https://www.mariwork.ir/product-tag/%d8%aa%db%8c%d8%b1%d9%87/ |
| 1945 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1945 | https://www.mariwork.ir/product-tag/%d9%82%d9%87%d9%88%d9%87-%d8%a7%db%8c-%d8%aa%db%8c%d8%b1%d9%87/ |
| 1946 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1946 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87-%d9%82%d9%87%d9%88%d9%87-%d8%a7%db%8c-%d8%aa%db%8c%d8%b1%d9%87/ |
| 1947 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1947 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%82%d9%87%d9%88%d9%87-%d8%a7%db%8c-%d8%aa%db%8c%d8%b1%d9%87-%d9%be%d8%a7%d8%b1%da%86%d9%87/ |
| 1948 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1948 | https://www.mariwork.ir/product-tag/%d9%81%db%8c%d8%b1%d9%88%d8%b2%d9%87%d8%a7%db%8c/ |
| 1949 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1949 | https://www.mariwork.ir/product-tag/%d9%81%db%8c%d8%b1%d9%88%d8%b2%d9%87-%d8%a7%db%8c/ |
| 1950 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1950 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87-%d9%81%db%8c%d8%b1%d9%88%d8%b2%d9%87-%d8%a7%db%8c/ |
| 1951 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1951 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%81%db%8c%d8%b1%d9%88%d8%b2%d9%87-%d8%a7%db%8c-%d9%be%d8%a7%d8%b1%da%86%d9%87/ |
| 1952 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1952 | https://www.mariwork.ir/product-tag/%d8%b7%d9%84%d8%a7%db%8c%db%8c-%d8%aa%db%8c%d8%b1%d9%87/ |
| 1953 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1953 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87-%d8%b7%d9%84%d8%a7%db%8c%db%8c-%d8%aa%db%8c%d8%b1%d9%87/ |
| 1954 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-product_tag-1954 | https://www.mariwork.ir/product-tag/%d8%b1%d9%86%da%af-%d8%b7%d9%84%d8%a7%db%8c%db%8c-%d8%aa%db%8c%d8%b1%d9%87-%d9%be%d8%a7%d8%b1%da%86%d9%87/ |

### post_tag
| Term ID | Reported count | Public assigned IDs | Inventory row | Advertised archive URL |
| --- | --- | --- | --- | --- |
| 158 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-158 | https://www.mariwork.ir/mag/tag/%d9%85%d8%b9%d8%b1%d9%81%db%8c-%d9%87%d9%86%d8%b1%d9%85%d9%86%d8%af/ |
| 162 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-162 | https://www.mariwork.ir/mag/tag/%d9%88%db%8c%d8%af%db%8c%d9%88-%d8%a2%d9%85%d9%88%d8%b2%d8%b4%db%8c/ |
| 163 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-163 | https://www.mariwork.ir/mag/tag/%d9%86%d9%82%d8%a7%d8%b4%db%8c-%d8%a8%d8%a7%d8%aa%db%8c%da%a9/ |
| 164 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-164 | https://www.mariwork.ir/mag/tag/%d9%85%d8%b5%d8%a7%d8%ad%d8%a8%d9%87/ |
| 165 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-165 | https://www.mariwork.ir/mag/tag/%d9%87%d9%86%d8%b1%d9%85%d9%86%d8%af%d8%a7%d9%86/ |
| 166 | 9 | 26387, 22192, 22194, 13320, 13318, 13316, 13312, 13305, 13295 | TERM-post_tag-166 | https://www.mariwork.ir/mag/tag/%d8%b1%d9%86%da%af-%d9%be%d8%a7%d8%b1%da%86%d9%87/ |
| 167 | 9 | 26387, 22192, 22194, 13320, 13318, 13316, 13312, 13305, 13295 | TERM-post_tag-167 | https://www.mariwork.ir/mag/tag/%d8%b1%d8%a7%d9%87%d9%86%d9%85%d8%a7/ |
| 168 | 3 | 22196, 22197, 22193 | TERM-post_tag-168 | https://www.mariwork.ir/mag/tag/%d9%86%d9%82%d8%a7%d8%b4%db%8c-%d9%be%d8%a7%d8%b1%da%86%d9%87/ |
| 169 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-169 | https://www.mariwork.ir/mag/tag/%d8%aa%da%a9%d9%86%db%8c%da%a9/ |
| 170 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-170 | https://www.mariwork.ir/mag/tag/%d9%85%d8%a7%d8%b1%db%8c-%d9%88%d8%b1%da%a9/ |
| 171 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-171 | https://www.mariwork.ir/mag/tag/%d8%aa%d8%b3%d8%aa-%d8%ab%d8%a8%d8%a7%d8%aa/ |
| 172 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-172 | https://www.mariwork.ir/mag/tag/%d8%aa%da%a9%d9%86%db%8c%da%a9-%d9%86%d9%85%da%a9/ |
| 173 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-173 | https://www.mariwork.ir/mag/tag/%da%86%d8%b1%d8%ae%d9%87-%d8%b1%d9%86%da%af/ |
| 174 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-174 | https://www.mariwork.ir/mag/tag/%da%af%d9%84%d8%af%d9%88%d8%b2%db%8c/ |
| 175 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-175 | https://www.mariwork.ir/mag/tag/%d8%ad%d8%b1%db%8c%d8%b1/ |
| 176 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-176 | https://www.mariwork.ir/mag/tag/%da%a9%d8%aa%d8%a7%d9%86/ |
| 177 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-177 | https://www.mariwork.ir/mag/tag/%d9%85%d8%af%db%8c%d9%88%d9%85-%d9%be%d9%81%da%a9%db%8c/ |
| 178 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-178 | https://www.mariwork.ir/mag/tag/%da%a9%d9%81%d8%b4-%d9%88-%da%86%d8%b1%d9%85/ |
| 179 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-179 | https://www.mariwork.ir/mag/tag/%d9%86%d9%82%d8%a7%d8%b4%db%8c-%d8%ac%db%8c%d9%86/ |
| 180 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-180 | https://www.mariwork.ir/mag/tag/%d8%a8%db%8c%d8%b3-%da%a9%d9%88%d8%aa/ |
| 181 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-181 | https://www.mariwork.ir/mag/tag/%d9%85%d8%af%db%8c%d9%88%d9%85-%d9%81%db%8c%da%a9%d8%b3%d8%a7%d8%aa%db%8c%d9%88/ |
| 182 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-182 | https://www.mariwork.ir/mag/tag/%d9%86%d9%85%d8%af/ |
| 183 | 3 | 22196, 22197, 22193 | TERM-post_tag-183 | https://www.mariwork.ir/mag/tag/%da%86%d8%a7%d9%be-%d9%be%d8%a7%d8%b1%da%86%d9%87/ |
| 184 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-184 | https://www.mariwork.ir/mag/tag/%d9%85%d9%88%d9%86%d9%88%d8%aa%d8%a7%db%8c%d9%be/ |
| 185 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-185 | https://www.mariwork.ir/mag/tag/%d9%85%d9%88%d9%86%d9%88%d9%be%d8%b1%db%8c%d9%86%d8%aa/ |
| 186 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-186 | https://www.mariwork.ir/mag/tag/%d9%85%d8%af%db%8c%d9%88%d9%85-%d8%a8%db%8c%d8%b3-%da%a9%d9%88%d8%aa/ |
| 187 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-187 | https://www.mariwork.ir/mag/tag/%d8%ad%d9%88%d9%84%d9%87/ |
| 188 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-188 | https://www.mariwork.ir/mag/tag/%d8%a8%d8%a7%d9%86%d8%af%d8%a7%d9%86%d8%a7/ |
| 189 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-189 | https://www.mariwork.ir/mag/tag/%d8%b4%db%8c%d8%a8%d9%88%d8%b1%db%8c/ |
| 190 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-190 | https://www.mariwork.ir/mag/tag/%d9%85%d9%87%d8%b1-%da%86%d9%88%d8%a8%db%8c/ |
| 191 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-191 | https://www.mariwork.ir/mag/tag/%d8%a7%da%a9%d9%84%db%8c%d9%84/ |
| 192 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-192 | https://www.mariwork.ir/mag/tag/%da%86%d8%b3%d8%a8-%d8%a7%da%a9%d9%84%db%8c%d9%84/ |
| 193 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-193 | https://www.mariwork.ir/mag/tag/%da%86%d8%a7%d9%be-%d8%a7%d8%b3%d8%aa%d9%86%d8%b3%db%8c%d9%84/ |
| 194 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-194 | https://www.mariwork.ir/mag/tag/%da%86%d8%a7%d9%be-%d8%aa%d8%b1%d8%a7%d9%81%d8%a7%d8%b1%d8%af/ |
| 195 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-195 | https://www.mariwork.ir/mag/tag/%da%86%d8%a7%d9%be-%d8%b4%d8%a7%d8%a8%d9%84%d9%88%d9%86%db%8c/ |
| 196 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-196 | https://www.mariwork.ir/mag/tag/%d9%85%d9%87%d8%b1/ |
| 197 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-197 | https://www.mariwork.ir/mag/tag/%d9%85%d9%87%d8%b1-%d8%a7%d8%b3%d9%81%d9%86%d8%ac%db%8c/ |
| 198 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-198 | https://www.mariwork.ir/mag/tag/%d8%aa%d8%ab%d8%a8%db%8c%d8%aa/ |
| 199 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-199 | https://www.mariwork.ir/mag/tag/%da%86%d8%a7%d9%be-%d8%b3%d8%a7%d8%af%d9%87/ |
| 200 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-200 | https://www.mariwork.ir/mag/tag/%d8%b4%d8%b3%d8%aa%d8%b4%d9%88/ |
| 201 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-201 | https://www.mariwork.ir/mag/tag/%d9%85%d9%87%d8%b1-%d9%84%db%8c%d9%86%d9%88/ |
| 202 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-202 | https://www.mariwork.ir/mag/tag/%d9%84%db%8c%d9%86%d9%88%d9%84%d8%a6%d9%88%d9%85/ |
| 203 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-203 | https://www.mariwork.ir/mag/tag/%d8%aa%d8%b1%d9%85%db%8c%d9%85/ |
| 204 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-204 | https://www.mariwork.ir/mag/tag/%d8%b1%d9%86%da%af-%d9%84%d8%a8%d8%a7%d8%b3/ |
| 205 | 0 | NONE_IN_PUBLIC_COLLECTION | SPACE-OTHER-PARAMETERS | https://www.mariwork.ir/mag/tag/%da%86%d8%a7%d9%be-%d8%b3%db%8c%d9%84%da%a9-%d8%a7%d8%b3%da%a9%d8%b1%db%8c%d9%86/ |
| 206 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-206 | https://www.mariwork.ir/mag/tag/%d8%b3%db%8c%d9%84%da%a9-%d8%a7%d8%b3%da%a9%d8%b1%db%8c%d9%86/ |
| 207 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-207 | https://www.mariwork.ir/mag/tag/%d8%aa%db%8c-%d8%b4%d8%b1%d8%aa/ |
| 208 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-208 | https://www.mariwork.ir/mag/tag/%d8%b4%d9%86%d8%a7%d8%ae%d8%aa-%d9%be%d8%a7%d8%b1%da%86%d9%87/ |
| 209 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-209 | https://www.mariwork.ir/mag/tag/%d9%85%da%a9%d8%b1%d9%88%d9%85%d9%87/ |
| 210 | 12 | 26387, 22192, 22196, 22197, 22194, 22193, 13320, 13318, 13316, 13312, 13305, 13295 | TERM-post_tag-210 | https://www.mariwork.ir/mag/tag/%d9%85%d9%82%d8%a7%d9%84%d9%87/ |
| 211 | 3 | 22196, 22197, 22193 | TERM-post_tag-211 | https://www.mariwork.ir/mag/tag/%d8%aa%d8%a7%d8%b1%db%8c%d8%ae%da%86%d9%87-%da%86%d8%a7%d9%be-%d9%88-%d9%86%d9%82%d8%a7%d8%b4%db%8c-%d9%be%d8%a7%d8%b1%da%86%d9%87/ |
| 1986 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-1986 | https://www.mariwork.ir/mag/tag/free/ |
| 1987 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-1987 | https://www.mariwork.ir/mag/tag/paid/ |
| 1988 | 0 | NONE_IN_PUBLIC_COLLECTION | TERM-post_tag-1988 | https://www.mariwork.ir/mag/tag/bootcamp/ |

