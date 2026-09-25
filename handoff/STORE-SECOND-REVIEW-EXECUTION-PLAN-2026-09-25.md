# Store SEO — Second Review Execution Plan

**Date:** 2026-09-25  
**Repository baseline:** `68ff95045f1fed9776b12868eeae4471622c74ae`  
**Source review:** `audits/second-review/store/SR-004-CHATGPT-STORE-SECOND-REVIEW.md`  
**Mode:** REPOSITORY PLANNING ONLY  
**Production writes authorized by this document:** NO  
**Required authority before implementation:** approved target state + implementation task/change dossier per `AGENTS.md`

## 1. Current verified state

The Second Review phase is sufficiently complete to stop repeating broad Store discovery and move into approval + canary implementation planning.

Completed / materially closed:
- Foundation A-010..A-021 is recorded complete in `MASTER-TODO.md`.
- Rank Math is verified as the active Store SEO owner (Free 1.0.279).
- Yoast is historical/pre-migration; DB-SEO-001 found no confirmed Yoast-owned DB targets and public regression passed.
- Current Store evidence exists for Shop, products, Product Categories, Product Tags, `pa_volume`, parameter families, variable-product schema, bundles, title/H1 patterns and internal-link graph.
- SR-002 migration reconciliation is complete as a current-state evidence layer.
- SR-003 Store evidence closure is complete.
- SR-004 independent ChatGPT Store Second Review is complete and is the current recommendation baseline.

Not completed:
- No Store Production SEO implementation has occurred after SR-004.
- No SR-ST target-state recommendation has yet been recorded as owner-approved.
- No Store implementation task/change dossier has yet been created from SR-004.
- ProductGroup/variant schema has not been implemented.
- Product title normalization has not been implemented.
- Explicit product meta descriptions have not been implemented.
- Active Product Category/`pa_volume` sitemap policy has not been implemented.
- Facet/parameter target policy has not been implemented.
- Legacy category decommission (TERM-product_cat-20 / 27) has not been implemented.
- Contextual content → commerce internal-link work has not been implemented.
- Product Tag / Blog Tag decommission, unresolved legacy mappings, Blog empty-category lifecycle and image/ALT remain separate workstreams.

## 2. MASTER-TODO reconciliation

The current `MASTER-TODO.md` understates completed B0 audit/evidence work. Do not rerun these from zero.

### Evidence-complete or materially covered by Second Review
- B0-001 Shop archive audit
- B0-003 Product category inventory
- B0-004 Product tag inventory
- B0-006 Filter/faceted URL inventory
- B0-007 Sort/query parameter URL inventory
- B0-008 Pagination behavior
- B0-009 Product search URLs
- B0-011 Bundle/set architecture
- B0-013 Store internal-link baseline
- B0-014 Store schema ownership baseline
- B0-015 Store Rank Math settings baseline
- B0-021 Current product-title pattern audit

### Partially covered / decision or additional evidence still required
- B0-002 Product sitemap policy — current state known; target policy pending approval/implementation.
- B0-005 Product attribute archive inventory — `pa_volume` is well evidenced; do not assume every attribute family is closed without inventory confirmation.
- B0-010 Variant URL architecture — current architecture known, but stability remains PARTIAL without transactional testing.
- B0-012 Legacy product URL mapping — unresolved PARTIAL/UNKNOWN mappings remain.
- B0-016..B0-019 Internal Link Requirement Matrix / rule classification / family gap / reverse-link target design — current graph exists; target architecture still needs explicit design.
- B0-022 Product Title Naming Standard — SR-004 proposes family standards; owner approval still required.
- B0-023 Brand-token verification against approved family standard — cannot close before B0-022 approval.

### Not yet done
- B0-020 Approve target internal-link architecture.
- B0-024 Normalize product titles after approval.
- B0-025 Final product-title consistency regression.

Before mass execution, update tracking so Codex consumes SR-002/SR-003/SR-004 evidence instead of repeating discovery.

## 3. Execution order

### Wave 0 — Approval and implementation packaging

Goal: convert SR-004 recommendations into executable, rollback-capable tasks without touching Production.

1. Record owner decisions for SR-ST-001..SR-ST-011 as:
   - APPROVED
   - APPROVED_WITH_CHANGE
   - DEFERRED
   - REJECTED
2. For each approved FAMILY/SITEWIDE change, create a `changes/CHG-...` dossier from `templates/SYSTEMIC-CHANGE.md`.
3. For each approved write, create a scoped implementation task from `templates/IMPLEMENTATION-TASK.md`.
4. Recheck current Production state immediately before each write.
5. Preserve URL slugs unless a task explicitly includes migration/redirect work.
6. Keep Rank Math as owner wherever its installed capability is sufficient; use only a narrow `RANK_MATH_EXTENSION` when required.

Exit gate:
- exact approved targets;
- exact affected entities;
- backup/rollback;
- canary;
- regression set;
- Google basis/reference;
- Rank Math owner/path;
- no conflicting recent Production change.

### Wave 1 — Low-risk Store technical canaries

#### W1-01 Shop landing page — first implementation canary
Source: SR-ST-001

Scope:
- keep `/shop/` indexable and self-canonical;
- add one useful visible H1;
- replace archive-generated SEO title/meta with deliberate Store metadata;
- do not change the Shop URL.

Why first:
- isolated;
- low rollback cost;
- validates Rank Math/content ownership and QA flow before systemic changes.

Acceptance:
- HTTP/final URL unchanged;
- one intended H1;
- approved title/meta visible in output;
- self-canonical;
- index remains allowed;
- no duplicate title/meta owner;
- cart/checkout/product rendering unaffected.

#### W1-02 Active taxonomy SEO ownership + sitemap canary
Sources: SR-ST-006 / SR-ST-007

Canary set:
- one durable Product Category: TERM-product_cat-1902 (colors);
- one volume landing page: one approved `pa_volume` term.

Scope:
- explicit Rank Math taxonomy metadata controls;
- confirm robots/indexability;
- test sitemap inclusion only for approved indexable landing pages;
- no tag changes in this task.

Acceptance:
- title/meta/canonical/robots intentional;
- sitemap membership intentional;
- no duplicate taxonomy output;
- no accidental Product Tag exposure.

#### W1-03 Legacy volume-category decommission
Source: SR-ST-006

Entities:
- TERM-product_cat-20
- TERM-product_cat-27

Target:
- controlled migration to verified main colors category;
- preserve historical evidence;
- no slug-similarity bulk rules.

Acceptance:
- single-hop intended disposition;
- no redirect loop/chain;
- no sitemap/internal-link residue;
- destination remains correct/indexable;
- rollback mapping recorded.

#### W1-04 ProductGroup schema canary
Source: SR-ST-004

Representative canaries:
- one 30/60/250 volume-variable product;
- one 30/60 volume-variable product.

Target:
- coherent ProductGroup + variant Product model;
- per-variant Offer;
- stable variant identity/URL preselection;
- base parent remains canonical;
- no second independent JSON-LD emitter.

Owner:
- RANK_MATH_EXTENSION only if current Rank Math Free cannot natively produce the required variant model;
- integrate through documented Rank Math schema filters in the central Mariwork Core integration.

Acceptance:
- no duplicate Product schema pipeline;
- ProductGroup/variant identity consistent;
- price/currency/availability match visible Woo data;
- variant URLs preselect correctly;
- base canonical remains stable;
- purchase path unaffected.

#### W1-05 Bundle presentation canary
Source: SR-ST-005

Select one representative large YITH bundle.

Scope:
- reconcile visible component count/composition with current YITH/Woo data;
- keep bundle as its own Product/Offer, not ProductGroup.

Acceptance:
- visible count = current bundle data;
- schema and visible product identity do not contradict;
- price/add-to-cart unaffected.

#### W1-06 Parameter/facet policy canary
Source: SR-ST-008

Families:
- canonical pagination `/shop/page/N/`;
- product search;
- `filter_volume`;
- `orderby`;
- `per_page`;
- `per_row`;
- `shop_view`;
- legacy `product-page`;
- `attribute_pa_volume` variant preselection.

Rules:
- do not blanket-block `attribute_pa_volume`;
- do not use robots.txt as a substitute for indexability control;
- separate variant-preselection URLs from non-search landing states.

Acceptance:
- intended canonical/robots per family;
- no newly indexable duplicate parameter space;
- canonical pagination preserved;
- variant preselection still works;
- crawl regression passes.

### Wave 2 — Product/content normalization canary

Start only after Wave 1 technical ownership is stable.

#### W2-01 Product Title Naming Standard approval
Source: SR-ST-002

Proposed family standards from SR-004 are the baseline, not yet Production authority:
- Fabric colors: `رنگ پارچه [نام رنگ] ماری ورک کد [NNN]`
- Media/additives: `[نام دقیق محصول] ماری ورک کد [NNN]`
- Tools/accessories: `[نام ابزار] ماری ورک [کد NNN اگر وجود دارد]`
- Sets: concise identity + count/type + volume; move long “شامل ...” composition text into content.

Before write:
- approve digit style;
- approve separator policy;
- approve brand token policy;
- define exceptions;
- preserve URLs.

Canary:
- 5 representative products across families, including variable and bundle products.

#### W2-02 Product SEO title template
Only after visible-title canary passes.

Goal:
- remove unnecessary site-suffix duplication without losing brand identity on legacy exceptions.

Owner:
- RANK_MATH.

#### W2-03 Explicit product meta descriptions
Source: SR-ST-003

Priority:
1. leaked/broken descriptions first, including WP-28627 and WP-33327;
2. historically important Store entry pages/products;
3. repeated/overlong descriptions;
4. remaining products by family.

Rules:
- factual current product content only;
- no reconstruction/import from Yoast;
- no generic history copy in place of product-specific value;
- ChatGPT approval required for final content.

#### W2-04 Category/volume landing content
For approved indexable Product Categories and `pa_volume` pages:
- deliberate title/meta/H1;
- useful concise intro where justified;
- no boilerplate added merely for word count;
- contextual links to relevant products and learning content.

### Wave 3 — Contextual architecture

Source: SR-ST-009

Order:
1. design and approve Internal Link Requirement Matrix;
2. classify CORE / FAMILY-SPECIFIC / CONTEXTUAL;
3. Article → Product/Category links;
4. Academy/Lesson → Product/Category links where material/tool is actually used;
5. Category → Academy/Article learning links;
6. rerun deterministic graph.

Do not implement sitewide keyword auto-linking.

Acceptance:
- mandatory family links are consistent;
- anchors are natural;
- no irrelevant commercial stuffing;
- orphan/reciprocity gaps materially reduced;
- global navigation is not redundantly rewritten.

### Wave 4 — Family rollout

After canary + Codex QA + ChatGPT Final Acceptance:
- expand validated title/meta/schema rules by product family;
- expand approved taxonomy/sitemap policy;
- complete explicit product metadata;
- complete contextual links;
- run Store-wide regression.

Do not mass-roll a rule that failed or remains ambiguous in canary.

## 4. Separate workstreams — do not mix into initial Store canary

Keep separate from Wave 1/2 unless a dependency is proven:
- Product Tag controlled decommission (275 zero-assignment terms);
- Blog Tag cleanup/decommission (assigned terms remain);
- unresolved legacy product-volume URL dispositions;
- Blog empty-category lifecycle;
- image/ALT review;
- historical Education → Academy mapping completion.

This separation reduces rollback scope and prevents unrelated migration work from contaminating Store SEO canaries.

## 5. Recommended first Production task

**First write candidate:** W1-01 Shop landing page.

Reason:
- smallest isolated SEO/content change;
- no URL migration;
- no schema-family rollout;
- simple rollback;
- validates the complete APPROVED → IMPLEMENTING → CODEX_QA_PASSED → ChatGPT Final QA workflow.

After W1-01 passes Final QA, proceed to W1-02 taxonomy canary, then W1-04 schema canary. W1-03/W1-05/W1-06 may proceed only as their own scoped change dossiers/tasks.

## 6. Required reporting after every implementation task

Report:
- HEAD before/after;
- Production path verified;
- exact changed files/options/entities;
- backup/rollback location (without secrets/PII);
- before/after public evidence;
- HTTP/final URL;
- title/meta/H1;
- canonical/robots;
- schema summary;
- affected purchase/navigation behavior where applicable;
- Codex QA result;
- unresolved warnings;
- whether ChatGPT Final QA is still pending.

## 7. Stop conditions

Stop rollout and rollback/review if any canary causes:
- wrong canonical/indexability;
- duplicate SEO/schema output;
- broken variant selection;
- price/availability mismatch;
- add-to-cart/checkout regression;
- redirect chain/loop;
- unexpected sitemap exposure/removal;
- unrelated page output change;
- Rank Math ownership conflict.

## 8. Immediate next repository action

Create the W1-01 Shop implementation task only after the owner explicitly approves SR-ST-001 (or an edited target). Do not infer Production authorization from this planning document.
