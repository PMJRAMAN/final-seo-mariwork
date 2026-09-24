# A-010 — Complete URL/Entity Inventory: Round-1 evidence

**Task:** A-010 · **Program:** FOUNDATION / STORE-FIRST · **Framework/schema:** v1.0 (existing 13-column inventory schema preserved)
**Audit date:** 2026-09-24 · **Task lifecycle:** CODEX_AUDITED · **Completeness:** best available inventory with explicit gaps; not an exhaustive database census.
**Authority:** INITIAL research only. No final SEO dispositions, Second Review, approval, or Production implementation. Individual records are inventoried, not page-audited.

## Result

Inventory contains **555 rows**: **530 entity/current-target or unresolved-URL rows** and **25 URL-space evidence rows covering 15 policies**, preserving **2104 distinct observed URL spellings** in JSON evidence. All **368/368 GSC page URLs**, **147/147 sitemap entries (146 unique URLs)**, and all returned REST content/term/attachment URLs are retained. Counts of URL spellings, rows, WP objects, and indexed pages are different measures.

Public crawl discovered 1480 URLs including sample additions and recorded 907 fetch results (initial URL checks, not total requests including redirect hops). 144 initial URLs had observed redirect chains. Fetch-result distribution: `{"200": 668, "404": 239, "UNKNOWN_NEEDS_VERIFICATION": 573}`. These are inventory measurements, not Search Console indexing counts.

## Sources and collection method

1. Read repository Manifest, latest SEO-016 decision and related decisions, AGENTS, workflow/audit/sitewide specs, Master TODO, data sources, ownership/reference rules, registry, and A-009 historical deployment note. Initial inventory was header-only; no page dossiers or existing systemic findings supplied URL evidence.
2. Public unauthenticated GET of robots.txt and sitemap_index.xml, followed recursively through all six listed child sitemaps. Only sitemap namespace `url/loc` entries counted as page URLs; image locs were not mistaken for pages.
3. Breadth-first initial-HTML `<a href>` discovery seeded by the home page, all GSC URLs, all sitemap URLs, then public REST links. Canonical, feed, and redirect destinations were also retained. Requests used User-Agent `Mariwork-SEO-ReadOnly-Inventory/1.0`, at most two concurrent crawl requests, 20-second timeout, and eight redirect hops. Same-site redirects only; unsafe/action/private paths were not followed. No browser interaction or form submission.
4. Crawl bounded at 900 initial fetches, 12 rounds per crawl pass; 7 additional representative parameter/attachment checks. Non-parameter content first; machine spaces retained without exhaustive combinations. Binary file links and transactional/account/admin paths were recorded without fetching. Known private-log/action links were excluded from navigation expansion; five GSC add-to-cart URLs were retained exactly under the transaction-actions policy without requests; no cart, order, logout, or account-security test was made.
5. Public REST discovery `/wp-json/wp/v2/types` and `/wp-json/wp/v2/taxonomies`, then collection GETs with `per_page=100&page=N&_fields=id,link,type,status,parent` for content or `_fields=id,link,taxonomy,parent,count&hide_empty=false` for terms. All advertised pages requested (up to safety cap 100; largest collection used nine). No users/orders/comments routes, credentials, authentication, DB connection, WP bootstrap, or full content fields requested. Only safe public ID/URL metadata persisted.
6. Temporary Python standard-library/requests extraction tools in `/tmp` parsed CSV, XML and HTML; extracted evidence lives in the allowed CSV JSON notes. Temporary scripts are not durable dependencies and no raw export was edited. Live HTML, cookie headers, contact data and response bodies were not saved to the repository.

### Sitemaps (HTTP 200, observed 2026-09-24)

| Sitemap | Page locs | SHA-256 of fetched XML |
|---|---:|---|
| https://www.mariwork.ir/sitemap_index.xml | 0 | `3650f11b10e07ada632762d37e061a84c7e45438298f1c1348d19322cfe8dd93` |
| https://www.mariwork.ir/post-sitemap.xml | 13 | `a3899b137d80312669c2dd7d3b1b608595a7311c6208648e3c8e72781e2ec668` |
| https://www.mariwork.ir/page-sitemap.xml | 9 | `5c5c61d50006549a4060d70bc68e11739d4777bc1b8ae44fa381ad20a2cbf6a9` |
| https://www.mariwork.ir/product-sitemap.xml | 84 | `992630d3185e0224e7b07c1ad9a24ce97a171df593181009a5232659d865c9a5` |
| https://www.mariwork.ir/sfwd-courses-sitemap.xml | 2 | `fa5ae95be42402afae0e8ff3f47ff9e26a8bc10446d6c4e0af42e6bcd61dd49c` |
| https://www.mariwork.ir/sfwd-lessons-sitemap.xml | 37 | `e84eba5625dd70f4bed7298d64c230bc1fdfa40a50d7b956ac7d06e81e7429b5` |
| https://www.mariwork.ir/category-sitemap.xml | 2 | `c3cebd3c661b8f78b59167641e83bead1ea98b66c0565a860223fb3fbbfb4d6b` |

The product sitemap has 83 product URLs plus /shop/. The shop URL also appears in the page sitemap, so 147 entries represent 146 unique URLs. The post sitemap has 12 post URLs plus its archive. The sitemap index explicitly identifies Rank Math as generator. This is public output attribution, not verification of installed version, active modules, or absence of custom filters. Sitemap presence is a discovery signal, not proof of current indexation.

### Public REST census

| Type/taxonomy | Returned records | Advertised total | HTTP statuses |
|---|---:|---:|---|
| post | 12 | 12 | 200 |
| page | 15 | 15 | 200 |
| attachment | 626 | 845 | 200 |
| mariwork_artist | 0 | 0 | 200 |
| product | 83 | 83 | 200 |
| sfwd-courses | 0 | BLOCKED_BY_ACCESS | 401 |
| sfwd-lessons | 0 | BLOCKED_BY_ACCESS | 401 |
| sfwd-topic | 0 | BLOCKED_BY_ACCESS | 401 |
| sfwd-quiz | 0 | BLOCKED_BY_ACCESS | 401 |
| category | 12 | 12 | 200 |
| post_tag | 54 | 54 | 200 |
| product_brand | 0 | 0 | 200 |
| product_cat | 9 | 9 | 200 |
| product_tag | 275 | 275 | 200 |
| ld_course_category | 2 | 2 | 200 |
| ld_course_tag | 0 | 0 | 200 |
| ld_lesson_category | 0 | 0 | 200 |
| ld_lesson_tag | 0 | 0 | 200 |
| ld_topic_category | 0 | 0 | 200 |
| ld_topic_tag | 0 | 0 | 200 |

REST endpoint for each table row and object IDs is retained in inventory evidence. Discovery exposed these additional registered types (declaration does not prove published/indexable URLs): `nav_menu_item`, `wp_block`, `wp_template`, `wp_template_part`, `wp_global_styles`, `wp_navigation`, `wp_font_family`, `wp_font_face`, `sfwd-question`, `ld-exam`, `groups`, `ct_content_block`, `gspbstylebook`, `rm_content_editor`. They are covered by SPACE-UNEXPOSED-CPT; internal/editor, exam and group collections were not enumerated because this task requires public SEO inventory rather than learning/user data.

Attachment responses advertised 845 objects but returned 626 unique IDs across nine requested pages. The 219-object difference is **UNKNOWN_NEEDS_VERIFICATION**; do not infer deletion, privacy status, or missing SEO pages. All 626 returned ID/link pairs are retained under SPACE-ATTACHMENT. Two sample attachment URLs redirected to a product and the home page respectively; this does not establish a policy for the other attachments.

LearnDash courses/lessons/topics/quizzes collections returned 401 (**BLOCKED_BY_ACCESS**). Public sitemaps/HTML provide course and lesson URLs; unpublished/private or unlinked items cannot be counted. The artist collection returned a public total of zero despite registered `mariwork_artist`; historical artist URLs remain in the inventory with observed HTTP evidence. Zero public REST records is not proof of zero stored objects.

### GSC provenance and limits

- Performance source: `httpswww.mariwork.ir-Performance-on-Search-2026-09-24/Pages.csv`; 368 rows, URL dimension; `Filters.csv`: Web / Last 16 months. `Chart.csv` actually spans 2025-05-22 through 2026-09-21; export dated 2026-09-24. Do not confuse export date with last measured day.
- Pages.csv SHA-256: `5b2b66cd4d7eb341899d182c0c6810329f08b5fd6acbb722c52bd209d520df31`. Inventory references `GSC:Pages.csv:<physical-line-number>` (header is line 1). Raw clicks/impressions/CTR/position stay on their exact historical URLs; no metrics summed or transferred to destinations.
- **Page-query relationship is not proven by the current export.** Queries.csv was not joined to Pages.csv. No query intent or page attribution was inferred.
- Coverage source: `httpswww.mariwork.ir-Coverage-2026-09-24/`: Chart.csv and issue CSVs are aggregate counts, Metadata.csv says All known pages. They contain no per-URL issue lists; therefore no URL-specific coverage status can be assigned from them. Live URL Inspection and Page+Query evidence: NOT_AVAILABLE.
- GSC top-page export is historical, not a full URL census. A URL absent from this export is not proven to have no impressions or value.

## Inventory interpretation / reproducibility

- Columns remain exactly those in the frozen inventory. Detailed provenance, redirects, HTTP/robots/canonical evidence and aliases fit in JSON `notes`; no governance schema change.
- `WP-<id>` uses a returned public REST post ID or observed HTML body `page-id-`/`postid-`. `TERM-<taxonomy>-<id>` uses public REST term identity; taxonomy IDs are not WP post IDs, so wp_id is NOT_APPLICABLE. `URL-<12 hex SHA256>` is a provisional URL identity where a stable object could not be established. A deterministic URL suffix resolves multiple distinct current URLs sharing an observed ID. Future verification must preserve ID history rather than silently replacing dossiers.
- Same scheme/host lowercasing and fragment removal only; path case, slash, query order and percent-encoding retained. Request-library Unicode percent-encoding may yield a distinct final URL spelling; both original and final are traceable. Percent encoding alone is not an HTTP redirect. No slug-semantic joins.
- An observed final HTTP destination groups redirected aliases with its current-target row. This is a transport mapping, not proof that an old entity is semantically equivalent to the target. In particular, home-page redirects must not inherit legacy entity meaning or historical metrics. Canonical-only alternatives were not merged by assertion.
- `current_url` for unresolved 404/unfetched legacy rows is the known candidate URL, not a declaration that it is current canonical content. `canonical_url` is the first HTML rel=canonical found on the final response, not Google-selected canonical. `NOT_AVAILABLE` means fetched HTML had no canonical element; otherwise unknown is explicit. Duplicate canonicals and validity within the HTML head remain A-013 scope.
- `actual_status` is final response HTTP status; original and intermediate 3xx statuses are in `notes.evidence[].redirect_chain`. Empty chain means directly fetched without HTTP redirect; UNKNOWN_NEEDS_VERIFICATION means no check. A 200 response is not proof of indexability or absence of a soft 404. No Googlebot equivalence claimed.
- `sitemap` lists source sitemaps anywhere in the grouped evidence. Exact URL membership is in each evidence source_refs: an alias in a sitemap does not prove the destination is included. NOT_PRESENT_IN_OBSERVED_SITEMAPS applies only to the six maps fetched, not all possible sitemaps.
- Large attachment/feed evidence sets are split into PART rows with shared policy_id/dossier and evidence_part/evidence_parts so standard CSV readers can parse every field. These are evidence partitions, not additional policies or canonical entities. Source refs retain all GSC/sitemap/REST sources plus up to three navigation/canonical/redirect refs, with additional_source_count; this is provenance, not a complete link graph. Page IDs from HTML are observational and are not a substitute for database access.
- Proposed `dossier` paths are NOT_CREATED. `final_disposition=NOT_DECIDED` for every row; intended indexability stays UNKNOWN_NEEDS_VERIFICATION. Content audit and final-disposition coverage must not count these rows as completed page audits.
- Machine-space rows preserve known URLs/attachment IDs in notes and select one observed representative. If none is known, `current_url=UNKNOWN_NEEDS_VERIFICATION` is a gap marker, not a crawl target. Representatives cannot stand in as canonical values or statuses for every URL in a space.

### Coverage by family (inventory rows, not total URLs)

| Family | Rows |
|---|---:|
| academy | 2 |
| articles | 12 |
| artists | 17 |
| attachment | 7 |
| author-archives | 1 |
| category | 13 |
| date-archives | 1 |
| education | 37 |
| facets | 1 |
| faq_taxonomy | 2 |
| feeds | 5 |
| homepage | 1 |
| ld_course_category | 2 |
| login-return | 1 |
| media-files | 1 |
| other | 8 |
| other-parameters | 1 |
| pagination | 1 |
| post_tag | 53 |
| product_attribute | 3 |
| product_cat | 7 |
| product_tag | 275 |
| products | 84 |
| search | 1 |
| shop | 1 |
| sort-display | 1 |
| static | 13 |
| system-endpoints | 1 |
| transaction-actions | 1 |
| unexposed-cpt | 1 |
| variations | 1 |

### Machine-space coverage / next research owner

| Space | Evidence and coverage | Next task |
|---|---|---|
| Facets/filter combinations | Observed filter_volume and query_type_volume; all encountered combinations retained, not expanded | B0-006, B9, A-013 |
| Sort/display | per_page/per_row/shop_view URLs and orderby form control; parameter-specific samples | B0-007, B9 |
| Pagination | /page/N/, product-page; retain sampled status/canonical, including historical 404s | B0-008, H-008 |
| Search | s/post_type forms observed; no fabricated search-results URL or form submission | B0-009, H-006 |
| Product variations/bundles | attribute_* and variation_id controls observed; variation IDs/parent-child census and bundle membership not extracted | B0-010/B0-011, A-011 |
| Feed | RSS link declarations and /feed/ URLs, sampled HTTP checks | H-007 |
| Media/attachment | All returned attachment IDs/links plus discovered raw media links; raw media not downloaded for inventory | H-005 |
| Login-return / actions | Return parameters retained; robots add-to-cart rules represented, never executed | H-011/H-012 |
| Cart/checkout/account | Discovered public URLs retained as entity candidates, no transaction/session tests | H-009/H-010/H-011 |
| Author/date | No concrete route proved; explicit unknown policy rows avoid invented pages | H-003/H-004 |
| API/system/custom types | REST and robots route declarations; editorial/system CPT gaps retained | A-011, G-004, H-012/H-014 |

## Access, ownership and completeness blockers

1. Production path `/home/mariwork/web/mariwork.ir/public_html` could not be verified: filesystem lookup returned Permission denied. No escalation or credential read attempted. WP executable exists, but no Production WP command or database query was run. Safe DB/Woo census, variations, unpublished/private counts, all registered attributes, redirect-table export, server logs and internal-only routes: BLOCKED_BY_ACCESS.
2. Installed Rank Math version, Free/Pro, Advanced mode, module settings, per-type sitemap settings and hooks: BLOCKED_BY_ACCESS. Public sitemap generator comment attributes sitemap output to Rank Math; exact owner pipeline for canonical/robots/schema and duplicate owners: UNKNOWN_NEEDS_VERIFICATION. Target owner remains Rank Math wherever installed capability is verified; otherwise no substitute owner is selected. `rank_math_capability_checked=BLOCKED_BY_ACCESS`; `rank_math_path_or_reason_not_used=configuration inaccessible; no SEO settings change proposed`. A-014/A-015 must resolve this before technical target-state recommendations.
3. Sitemap + navigation + public REST + historical GSC union is substantially broader than any one source, but cannot discover authenticated, orphaned, private, robots-blocked, JavaScript-only or unpublished entities exhaustively. No rendered JS crawl was performed. Parameter, action and binary spaces were intentionally bounded. Unfetched records are explicitly unknown, not silently dropped.
4. Tag REST counts and `count=0` values are observations, not grounds for deletion. Product/blog tag decommission is existing project direction in B8/E0; destination mapping, historical value, links, ownership, migration/rollback and Second Review remain unresolved. No final redirect, noindex or deletion list is produced here.
5. Raw export URL rows were preserved exactly, including legacy academy/education, articles/mag, product taxonomy, tags, media and historical maintenance/system pages. A-012 should investigate redirect semantics and unresolved URLs using the recorded chains; no semantic entity mapping is asserted for unverified cases.
6. The runner currently treats every nonempty entity_id/current_url as a page candidate and does not skip URL-space unknown markers; proposed dossier paths are not files. Before automatic page audits, orchestration must distinguish policy rows, unknown targets and unresolved legacy URLs from canonical content entities. This report does not authorize runner edits; A-009/A-021 review must account for the inventory contract.

## INITIAL research recommendations and Google basis

All items below are investigation recommendations only. Final URL/indexing/content/schema/redirect policy belongs to Second Review and human approval.

- Reconcile the remaining REST/media and access gaps in A-011/A-013; use sitemap plus crawlable links plus public object evidence, not sitemap membership as a completeness or indexing claim. `google_basis=GOOGLE_CONSISTENT` for this inventory methodology. Google explains that sitemaps aid discovery without guaranteeing crawling/indexing: [Sitemap overview](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview).
- In A-013/B9, examine each machine space before choosing which filtered URLs should be searchable. This task’s bounded sampling is `google_basis=PROJECT_DECISION`; the concern about potentially unbounded filter URLs is `GOOGLE_CONSISTENT` with [Google faceted-navigation guidance](https://developers.google.com/crawling/docs/faceted-navigation). No blanket crawl block or noindex recommendation is approved.
- Preserve observed redirect/canonical distinctions and verify intended canonical targets before any consolidation decision in A-012/A-013. `google_basis=GOOGLE_CONSISTENT`; [Google canonical guidance](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) describes redirects, canonical annotations and sitemap inclusion as different signals. Inventory grouping does not imply Google selected that canonical.
- Continue initial-HTML link discovery and separately test interaction-dependent content in A-013. `google_basis=GOOGLE_CONSISTENT`; [Google crawlable-link guidance](https://developers.google.com/search/docs/crawling-indexing/links-crawlable). robots.txt evidence is a crawl-control observation, not a noindex verdict: [Google robots introduction](https://developers.google.com/search/docs/crawling-indexing/robots/intro).

All five official Google references above were opened on 2026-09-24. No vendor advice is attributed to Google; no ranking outcome is promised.

## Validation

- Existing 13-column CSV schema and JSON notes parse; nonempty required fields; unique entity IDs; no disallowed lifecycle or final decisions.
- All 368 raw GSC URLs and all 147 sitemap entries (146 unique locs) are traceable in evidence. All 1,088 returned REST objects (including 626 attachments) are represented by their links/IDs, with machine-space aggregation explicit.
- Only `registry/URL-INVENTORY.csv` and this report are changed. MASTER-TODO, raw exports, governance, templates, dossiers and Production are unchanged. Runner owns TODO completion.
- Next research: A-011 taxonomy/CPT reconciliation, A-012 URL-history mapping, A-013 baseline, A-014/A-015 ownership, A-016 GSC normalization. These are next steps, not declarations that prerequisite gates have passed.
