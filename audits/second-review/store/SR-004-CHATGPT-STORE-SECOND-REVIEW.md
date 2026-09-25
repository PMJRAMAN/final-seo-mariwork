# SR-004 — ChatGPT Independent Store Second Review

**Review type:** Independent Second Review  
**Repository baseline:** `494866c2c9ebe6af60fedbcfde1188969f694e1a`  
**Production writes:** NONE  
**Approval state:** PENDING HUMAN APPROVAL  
**Implementation authorized:** NO  

This review supersedes stale Round-1 interpretations where SR-001/SR-002/SR-003 current-state evidence disproved the underlying observation. It does not rewrite Round-1 history.

## 1. Evidence basis

Primary current-state evidence:

- `audits/second-review/evidence/current-seo-output.jsonl`
- `audits/second-review/evidence/seo-ownership-matrix.json`
- `audits/second-review/reconciliation/SR-002-CURRENT-STATE-RECONCILIATION.md`
- `audits/second-review/store/SR-003-STORE-EVIDENCE-CLOSURE.md`
- `audits/second-review/store/current-variable-schema-matrix.json`
- `audits/second-review/store/variant-url-architecture.json`
- `audits/second-review/store/bundle-component-matrix.json`
- `audits/second-review/store/current-title-h1-matrix.json`
- `audits/second-review/store/current-internal-link-graph.json`
- `audits/second-review/store/current-parameter-policy-evidence.json`
- `audits/second-review/reconciliation/tag-category-attribute-reconciliation.json`
- `audits/second-review/maintenance/YOAST-LEGACY-PURGE.md`

Historical GSC metrics remain attached to their original URLs. Page→Query attribution remains unavailable.

## 2. Systemic finding Second Review

| Finding | Second Review result | Rationale |
|---|---|---|
| SYS-001 Rank Math ownership unknown | SUPERSEDED / RESOLVED FOR CURRENT STORE SEO | Rank Math Free 1.0.279 is verified active; current title/meta/robots/canonical/schema/sitemap settings are evidenced. Redirect ownership remains a separate concern. |
| SYS-002 Tag decommission | CONFIRMED, SPLIT BY FAMILY | Product Tags: 275 terms, zero assignments, noindex, sitemap off. Blog Tags: 54 terms, 6 assigned / 39 assignments, noindex, sitemap off. |
| SYS-003 Historical/error URL population | CONFIRMED AS MIGRATION WORK, NOT A BLANKET DEFECT | Legacy URLs require source-level disposition. Historical volume and Education URLs must not be treated as current entities. |
| SYS-004 Broad missing meta/H1/schema | REJECTED AS STATED / SUPERSEDED | Round-1 parser evidence was wrong. Current Store-specific issues replace it. |
| SYS-005 Facet/sort/pagination policy | CONFIRMED CURRENT ISSUE | SR-003 now provides current evidence for 9 parameter families. |
| SYS-006 Duplicate SEO owner/output risk | REJECTED AS STATED / SUPERSEDED | No duplicate parallel Product JSON-LD was observed. Mariwork Core only filters WooCommerce breadcrumb schema. Rank Math is the current Store SEO output owner. |
| SYS-007 Query→page attribution | RETAIN AS EVIDENCE LIMITATION | Joined Page+Query is unavailable. This blocks precise keyword attribution, not technical/family fixes. |
| SYS-008 Title/internal-link architecture | CONFIRMED, NARROWED | Product naming is inconsistent by family; content→commerce contextual linking is weak. Global navigation itself is strong. |
| SYS-009 Product-category sitemap/indexability | CONFIRMED, REDEFINED | Current taxonomy mixes durable landing pages with migration-era volume categories. Active indexable categories are excluded from the current sitemap. |
| SYS-010/011 ALT coverage | DEFER TO IMAGE/CONTENT WORKSTREAM | Image purpose must be reviewed before ALT changes. |
| SYS-012 Empty blog categories | CONFIRMED CURRENT ISSUE, DEFER TO BLOG/SYSTEM WORKSTREAM | 9 empty categories are 200/noindex; one empty category is 404; two categories are non-empty/indexable. |

## 3. Store target-state recommendations — pending approval

### SR-ST-001 — Shop landing page

Current Store archive is 200/index/self-canonical but has no H1 and its current meta description is `محصولات Archive - رنگ پارچه ماری ورک`.

**Recommended target:**
- keep `/shop/` indexable and self-canonical;
- add one visible, useful H1;
- replace the current archive-generated meta description;
- use a deliberate Store title instead of relying on an archive default.

Historical GSC evidence makes Shop a meaningful search entry page, but no query→page attribution is claimed.

### SR-ST-002 — Product title / H1 standards

Current product H1 equals the Woo product title for all 84 products. Naming is inconsistent across families.

**Recommended family standards:**

- Fabric colors: `رنگ پارچه [نام رنگ] ماری ورک کد [NNN]`
- Media/additives: `[نام دقیق محصول] ماری ورک کد [NNN]`
- Tools/accessories: `[نام ابزار] ماری ورک [کد NNN اگر وجود دارد]`
- Sets: concise product identity + count/type + volume; long “شامل ...” composition text belongs in page content, not in the primary title.

Normalize digit/separator policy consistently. Do not mass-change URLs when normalizing visible titles.

Current Rank Math template `%title% %sep% %sitename%` creates a repeated site suffix. Change the template only after visible product-title normalization so brand identity is not accidentally lost on legacy names.

### SR-ST-003 — Product meta descriptions

Current global source `%excerpt%` is not acceptable as the final Store metadata strategy.

Current evidence shows:
- many descriptions are excessively long;
- repeated descriptions exist across distinct products;
- WP-28627 and WP-33327 expose a leaked widget/configuration string in the description;
- some descriptions describe generic color/history rather than the concrete product.

**Recommended target:** explicit Rank Math product descriptions based on current factual product content, prioritized by historical page importance. Do not import or reconstruct Yoast metadata.

### SR-ST-004 — Variable-product structured data

All 60 variable parents currently emit `Product`; 58 use `AggregateOffer`; none emit `ProductGroup`, `hasVariant`, `isVariantOf`, `variesBy`, or a group identifier.

For Mariwork's volume-based single-page variants, the recommended target is a coherent `ProductGroup` + variant `Product` model with per-variant `Offer` data, unique variant identifiers, and stable preselection URLs. The base parent remains the single canonical URL.

Do not use `AggregateOffer` as the representation of the set of variants.

Rank Math Free remains the primary schema owner. Because Rank Math's documented ProductGroup/variation output is a PRO feature, implement only the missing variant layer through a narrowly scoped Rank Math schema filter in Mariwork Core, not a second independent JSON-LD emitter.

**Required canary before family rollout:** one 30/60/250 product and one 30/60 product. Validate ProductGroup/variant identity, price/currency/availability, variant preselection, canonical, and duplicate-output absence before expanding.

Official references:
- Google Product variants: https://developers.google.com/search/docs/appearance/structured-data/product-variants
- Google Product snippets / AggregateOffer: https://developers.google.com/search/docs/appearance/structured-data/product-snippet
- Rank Math WooCommerce Product Schema: https://rankmath.com/kb/woocommerce-product-schema/
- Rank Math schema filter API: https://rankmath.com/docs/filters-and-hooks/frontend/rich-snippets/

### SR-ST-005 — YITH bundles

All 22 current bundle parents have deterministic component mappings. Treat each purchasable set as its own Product/Offer, not as a product-variant group.

Before metadata expansion, reconcile visible component-count presentation with actual bundle composition. The canonical source of bundle contents must be current YITH/Woo data.

### SR-ST-006 — Product Categories

Split current Product Categories into durable landing pages and migration-era categories.

**Migration-era zero-assignment categories:**
- TERM-product_cat-20 — historical 60ml colors category
- TERM-product_cat-27 — historical 250ml colors category

Both currently return 200 and canonicalize to the main `/product/fabric-colors/` category. Recommended lifecycle: controlled decommission to the verified main colors category, preserving historical evidence.

**Durable current categories:**
- TERM-product_cat-1902 — colors
- TERM-product_cat-28 — media/glitters
- TERM-product_cat-82 — sets root
- TERM-product_cat-220 — tools/accessories
- TERM-product_cat-1991 — 30ml sets
- TERM-product_cat-1992 — 60ml sets
- TERM-product_cat-1993 — 250ml sets

Recommended target:
- keep durable categories indexable;
- enable precise Rank Math taxonomy metadata controls;
- stop using raw `%term_description%` as the final meta-description strategy;
- include approved indexable category URLs in the Product Category sitemap after migration cleanup.

### SR-ST-007 — pa_volume

Current volume terms 30ml / 60ml / 250ml are not the same concept as the old volume-specific Product Categories.

They are assigned to current products, have dedicated 200/self-canonical indexable URLs, and are strongly linked from site navigation.

Recommended target:
- retain the three volume landing pages as current navigational entities;
- keep them indexable if the current browse content remains useful and distinct;
- enable explicit Rank Math taxonomy metadata controls;
- include approved indexable volume landing pages in sitemap output;
- do not delete `pa_volume` as part of old-category cleanup.

### SR-ST-008 — Store parameters / facets

Recommended current policy:

- `/shop/page/N/`: KEEP indexable with self-canonical pagination.
- Product search: KEEP noindex.
- `filter_volume`, `orderby`, `per_page`, `per_row`, `shop_view`: non-search landing states; keep canonical consolidation to `/shop/` and prevent them from becoming index targets.
- `product-page`: legacy/alternate pagination route; stop generating it and consolidate to the canonical pagination architecture.
- `attribute_pa_volume`: DO NOT blanket-block. It is the direct variant-preselection mechanism and is needed for the proposed ProductGroup single-page variant model.

Avoid aggressive robots.txt blocking until variant/facet rules are separated and regression-tested.

Official references:
- https://developers.google.com/search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites
- https://developers.google.com/search/docs/crawling-indexing/canonicalization

### SR-ST-009 — Internal linking

The 13,668 “unresolved” link destinations in SR-003 are resolver gaps, not a broken-link count.

Global navigation is already strong. The meaningful weakness is contextual reciprocity:

- Products link broadly to Academy.
- Products mostly link to the Magazine through global navigation.
- The 12 reviewed Articles have no deterministic direct Product links.
- Academy/Lesson content has only a small number of direct Product links.

Recommended target:
- add contextual Article → Product/Category links where genuinely relevant;
- add contextual Lesson/Academy → Product/Category links where a material/tool is actually used;
- add Category → relevant Academy/Article learning links;
- preserve natural anchors and avoid sitewide automated keyword linking.

Reference:
- https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure

### SR-ST-010 — Tags

Product Tags are not an optimization target. With 275 terms and zero assignments, proceed later with the controlled decommission program after historical URL checks.

Blog Tags remain transitional because six terms still hold 39 assignments. Remove/replace their content relationships first; do not treat them as equivalent to Product Tags.

### SR-ST-011 — Legacy product-volume URLs

Do not mass-rewrite redirects based on slug similarity.

The existing legacy-volume evidence remains migration history:
- 68 PARTIAL mappings
- 14 UNKNOWN mappings

Keep historical metrics attached to source URLs. Resolve only mappings that need a redirect/disposition decision.

## 4. Implementation sequence after human approval

### Phase A — Store technical canary

1. Fix Shop H1/title/meta.
2. Clean taxonomy ownership/configuration for active Product Categories and `pa_volume`.
3. Decommission legacy empty Product Categories 20 and 27 with migration QA.
4. Implement ProductGroup schema canary on two representative volume-variable products.
5. Fix bundle component-count presentation on a representative large bundle.
6. Implement parameter/facet indexability rules with regression tests.

### Phase B — Store family normalization

1. Normalize visible product titles/H1 by family.
2. Then adjust Rank Math product title template to avoid unnecessary suffix duplication.
3. Create explicit product meta descriptions, starting with historically important products.
4. Expand validated ProductGroup implementation to eligible volume-variable parents.
5. Apply current Product Category / volume sitemap policy.

### Phase C — Contextual architecture

1. Article → Product/Category links.
2. Academy/Lesson → Product/Category links.
3. Category → Academy/Article links.
4. Re-run deterministic link graph and crawl/indexability regression.

### Separate migration workstreams

- Product Tag decommission
- Blog Tag cleanup/decommission
- unresolved legacy URL dispositions
- Blog empty-category lifecycle
- image/ALT review

## 5. Approval boundary

This document is a Second Review recommendation set, not an approval.

No Production implementation, Rank Math write, WordPress write, redirect change, taxonomy deletion, schema code change, title change, metadata change, or sitemap change is authorized until the project owner approves the relevant target-state decisions.

After approval, implementation must be canary-first and rollback-capable.
