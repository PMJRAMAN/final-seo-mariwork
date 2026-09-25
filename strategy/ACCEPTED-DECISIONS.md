# Mariwork SEO — Accepted Decision Register

**Purpose:** convenient consolidated register of owner-approved SEO target-state decisions.  
**Authority:** mirror of accepted `DEC-###` items in `strategy/DECISION-BACKLOG.md` and `docs/DECISIONS.md`.  
**Production authority:** NONE by itself. Execution remains governed by the Decision-to-Execution process.  
**Last updated:** 2026-09-25

> This file is maintained after each owner-approved decision so accepted strategy is easy to find in one place. If a status conflict ever appears, `strategy/DECISION-BACKLOG.md` remains the canonical status source.

---

## DEC-001 — Durable Site-Family Roles

**Status:** ACCEPTED

- Homepage = brand/entity and primary navigation root.
- Shop = broad commercial discovery hub.
- Durable Product Categories = commercial category hubs for stable product families.
- Product pages = exact transactional entities.
- Academy / Course / Lessons = structured educational content.
- Magazine / Articles = informational/reference content.
- Only genuinely useful populated Blog Categories = editorial content hubs.
- Static pages = trust/support entities.
- Transitional, empty, utility, machine and legacy URL spaces are governed separately and are not promoted to durable families by default.

## DEC-002 — Homepage Role and Metadata Baseline

**Status:** ACCEPTED

- Homepage remains the Brand/Entity + top-level navigation page.
- Keep current Title baseline: `رنگ پارچه ماری‌ورک | تولیدکننده تخصصی رنگ پارچه`.
- Keep current H1 baseline: `رنگ پارچه ماری‌ورک`.
- Keep current Meta Description baseline.
- Do not expand the Homepage title with extra category/product keyword stuffing.
- H1 does not need to duplicate the full SEO title.
- Future changes require stronger intent evidence, verified brand-fact changes, or a deliberate Homepage content-strategy change.
- Brand claims such as “10+ years” remain subject to DEC-053 factual verification.

## DEC-003 — Shop Target State

**Status:** ACCEPTED

- `/shop/` remains indexable and self-canonical.
- Shop remains the broad commercial discovery hub and primary all-products listing.
- Product grid/listing remains a primary part of the page; no layout redesign is required by this decision.
- Visible H1: `فروشگاه ماری‌ورک`.
- SEO title: `فروشگاه ماری‌ورک | رنگ پارچه، مدیوم، ست و ابزار`.
- Replace the broken archive-generated meta description with a factual Shop-specific description.
- Shop should lead users/crawlers into durable Product Categories and Products without replacing category-specific landing pages.

## DEC-004 — Cart / Checkout Transactional Utility Policy

**Status:** ACCEPTED

- Cart and Checkout are transactional utility endpoints, not search landing pages.
- Cart remains `noindex, follow`.
- Checkout remains a non-search transactional endpoint and may redirect to Cart in the empty state.
- Keep Cart/Checkout out of sitemap/index targets.
- Do not add editorial SEO copy or independent commercial schema.
- Do not introduce crawl blocking that prevents intended `noindex` from being seen.
- No Production change is required where current behavior already matches this policy.

## DEC-005 — LearnDash Course Category Public Role

**Status:** ACCEPTED

- Current `Free` and `Paid` LearnDash Course Categories are not durable public SEO entities.
- Keep them out of index targets, sitemaps and deliberate Academy navigation.
- Current 404 behavior is acceptable while the terms are empty.
- They may remain internally if LearnDash needs them operationally.
- Do not redirect them without a proven semantic replacement.
- Revisit only if Mariwork later develops a real multi-course free/paid architecture.

## DEC-006 — Durable vs Transitional Taxonomy Architecture

**Status:** ACCEPTED

- Only taxonomies with a durable, distinct user-facing browse/content role may become public SEO landing pages.
- Durable Product Categories and useful populated Blog Categories form part of the final architecture.
- `pa_volume` remains conditional under DEC-026.
- Product Tags, Blog Tags, migration-era Product Categories, empty LearnDash categories and other transitional/empty taxonomies are not durable SEO entities.
- Transitional/empty taxonomies must not be promoted through sitemap membership, navigation or SEO content merely because they exist in WordPress.
- Every taxonomy family requires its own lifecycle/indexability decision before implementation.

## DEC-007 — Fabric-Color Product Naming Standard

**Status:** ACCEPTED

Canonical visible Product title/H1 pattern:

`رنگ پارچه [Color Name] ماری ورک کد [NNN]`

Rules:
- Start with `رنگ پارچه`.
- Follow with the exact factual color name.
- Include the canonical Mariwork brand spelling.
- End with the stable product code.
- No decorative `|` or `-` inside the visible Product title/H1.
- Use consistent Latin digits for product codes.
- Do not add 30/60/250 ml volume tokens to the parent Product title when those are variants of the same Product.
- Visible-title normalization must not trigger Product URL/slug changes.
- SEO `<title>` behavior is governed by DEC-011.
- Final brand spelling follows DEC-053.
- Persian half-space usage is a writing/brand-consistency standard, not a standalone SEO requirement.
- Do not bulk-edit URLs/content solely to normalize half-space usage.

---

## Deferred / paused decisions

- `DEC-008` — Set / Bundle Product Naming Standard — **DEFERRED by owner on 2026-09-25; return later.**


## DEC-009 — Medium / Additive Product Naming Standard

**Status:** ACCEPTED

Canonical visible Product title/H1 pattern:

`[Exact Product Name] ماری ورک کد [NNN]`

Rules:
- Use the exact factual Product identity.
- Do not force the generic term `مدیوم`.
- Preserve factual specific identities such as glitter, varnish, glue, shine, base coat, fixative, or medium.
- Include the canonical Mariwork brand spelling.
- End with the stable Product code.
- No decorative `|` or `-`.
- Use consistent Latin digits for Product codes.
- Do not include volume in this family under any circumstance.
- Do not change URLs/slugs solely because visible titles are normalized.
- SEO `<title>` is governed separately by DEC-011.
- Brand spelling/half-space conventions follow DEC-053.


## DEC-010 — Tools / Accessories Product Naming Standard

**Status:** ACCEPTED

Product naming must reflect the product's actual brand ownership.

For third-party or generic tools/accessories:

`[Exact Product Name] [Code if factually applicable]`

For products genuinely branded/manufactured by Mariwork:

`[Exact Product Name] ماری ورک کد [NNN]`

Rules:
- Do not append `ماری ورک` merely because the product is sold on mariwork.ir.
- Include Mariwork only when the product is genuinely Mariwork-branded/manufactured.
- Include a third-party brand only when it is genuinely part of the Product identity.
- Include a code only when it is a real, stable identifier.
- Never invent a brand or code for SEO.
- No decorative separators such as `|` or `-`.
- Do not include volume.
- Include model/size only for genuinely distinct Products, not ordinary variations.
- Do not change URLs/slugs solely because visible titles are normalized.


## DEC-011 — Product Visible Title / H1 and SEO Title Relationship

**Status:** ACCEPTED

- WooCommerce Product title / visible H1 is the primary Product identity source.
- Default Rank Math Product SEO title template target is `%title%`, not `%title% %sep% %sitename%`.
- By default, Product SEO `<title>` matches the approved visible Product title/H1.
- Do not automatically append site-name boilerplate when Product identity is already sufficient.
- Page-specific SEO title exceptions require concise factual clarity and must not be used for keyword expansion or artificial branding.
- Third-party/generic Products must not receive Mariwork branding through the SEO-title template.
- Global template implementation remains blocked until DEC-008 is resolved.
- Rollout requires regression checks for uniqueness, descriptiveness and duplicate-brand removal.


## DEC-012 — Static / Core Page Title and H1 Policy

**Status:** ACCEPTED

- Static/Core pages use concise, page-specific SEO titles and clear visible H1s.
- Repetitive suffixes such as `- رنگ پارچه ماری ورک` are not required when the page is already clearly identified.
- About: `درباره ماری‌ورک` / H1 same.
- Contact: `تماس با ماری‌ورک` / H1 `با ماری‌ورک در تماس باشید`.
- Magazine: `مجله ماری‌ورک` / H1 same.
- Why Mariwork: `چرا ماری‌ورک؟` / H1 `چرا رنگ پارچه ماری‌ورک؟`.
- Stores: `فروشگاه‌های ماری‌ورک` / H1 `فروشگاه‌های ماری‌ورک نزدیک شما`.
- FAQ: `سوالات متداول ماری‌ورک` / H1 `سوالات متداول`.
- SEO title and H1 may differ, but they must describe the same page role/topic.
- Creative taglines may remain as supporting copy, not as a replacement for a clear page-identity H1.


## DEC-013 — Article Title / H1 Convention

**Status:** ACCEPTED

- Article titles are natural, reader-facing and based on the actual subject.
- Default relationship: approved Article H1/title = SEO `<title>`.
- Remove the repetitive `- رنگ پارچه ماری ورک` suffix from the default Article title template.
- Include `رنگ پارچه`, `ماری ورک` or other terms only when naturally relevant to the Article.
- Do not mechanically inject keywords, dates, “best”, “complete guide”, or similar modifiers for SEO.
- Retain existing titles when accurate and useful.
- Rewrite only when materially vague, inaccurate, misleading, excessively verbose, or inconsistent with the content.
- Do not change URLs/slugs solely because Article titles are normalized.
- Cannibalization/overlap is governed separately by DEC-119.


## DEC-014 — Academy Course / Lesson Title and H1 Convention

**Status:** ACCEPTED — AMENDED 2026-09-25

- Academy is video-first.
- Course H1 remains the natural Course name.
- Course SEO title should explicitly communicate video format where useful; current target example: `راهنماهای یک دقیقه‌ای ماری‌ورک | آموزش‌های ویدیویی`.
- Lesson H1 remains the natural instructional title.
- Default Lesson SEO title: `[Lesson H1] | آموزش ویدیویی`.
- Example: H1 `چاپ سیلک اسکرین` → SEO title `چاپ سیلک اسکرین | آموزش ویدیویی`.
- Remove the repetitive `- رنگ پارچه ماری ورک` suffix.
- Include Mariwork only when naturally part of the subject/identity.
- Preserve sequence numbers only for genuine multi-part instructional series.
- Do not change URLs/slugs solely because titles are normalized.
- Video/schema naming remains semantically consistent with the Lesson identity; DEC-037/038 govern schema ownership/eligibility.

## DEC-015 — Product Meta Description Strategy

**Status:** ACCEPTED — GENERAL POLICY

- `%excerpt%` is not the final default Product meta-description strategy.
- Product metas must be page-specific, factual, concise, and based on verified Product data.
- Avoid generic/history copy, duplicate descriptions, keyword stuffing, unsupported claims, and artificial Mariwork branding.
- Do not impose a fixed 150/160-character rule.
- Manual or programmatic generation is allowed when output is accurate, human-readable, and meaningfully page-specific.
- Avoid hard-coded volatile price/stock facts without reliable synchronization.
- Do not restore historical Yoast metadata by default.
- Exact per-Product meta copy is deferred to implementation/content QA.


## DEC-016 — Shop Metadata Strategy

**Status:** ACCEPTED

- `/shop/` uses explicit Shop-specific Rank Math metadata.
- SEO title: `فروشگاه ماری‌ورک | رنگ پارچه، مدیوم، ست و ابزار`.
- Meta: `فروشگاه ماری‌ورک؛ خرید رنگ پارچه، مدیوم‌ها، ست‌های رنگ و ابزارهای مرتبط برای نقاشی و چاپ روی پارچه.`
- Do not derive Shop meta from archive templates or `%excerpt%`.
- Avoid keyword stuffing and volatile counts/prices/discounts/stock.
- Product Category metadata remains a separate decision domain.


## DEC-017 — Static / Core Meta Description Strategy

**Status:** ACCEPTED

- Important Static/Core pages use explicit page-specific meta descriptions.
- Do not rely on generic templates or `%excerpt%`.
- Each description must accurately summarize that page's real role and visible content.
- Avoid keyword stuffing and unsupported claims.
- Meta descriptions need not repeat Title/H1.
- No fixed 150/160-character rule.
- Final copy must align with visible content and DEC-053 canonical brand facts.
- Initial direction: About=story/activity/product focus; Contact=contact/support; Magazine=editorial/educational scope; Why Mariwork=features/use cases; Stores=physical points of sale; FAQ=common Product/educational questions.


## DEC-018 — Article Meta Description Update Rule

**Status:** ACCEPTED — AMENDED 2026-09-25

Classify each Article meta as:
- `KEEP`
- `SHORTEN / REFINE`
- `REWRITE`

Rules:
- Preserve accurate useful metas; do not blanket-rewrite all Articles.
- Resolve duplicate descriptions.
- Rewrite weak/generic/insufficient descriptions.
- Refine verbose introduction-like descriptions.
- No fixed 150/160-character rule.
- Summarize the Article rather than copy paragraph one.
- Current Article fact-check has already been completed and is not a remaining metadata workflow.
- This Decision governs metadata only, not substantive Article edits.
- Cannibalization remains DEC-119.

## DEC-019 — Academy Video-First Meta Description Rule

**Status:** ACCEPTED — AMENDED 2026-09-25

- Every current Academy Lesson contains a primary video.
- Academy = practical/demo/video-first intent.
- Magazine = explanatory/reference/text-first intent.
- Course/Lesson metas are page-specific.
- Lesson metas should explicitly communicate that the page is a video lesson and describe that Lesson's specific technique/task/concept/learning outcome.
- Visible context near the primary video should also make the video format clear.
- Classify existing metas as `KEEP`, `REFINE`, `REWRITE`, or `FACT-CHECK REQUIRED`.
- Resolve duplicate and mismatched metadata.
- Do not use raw `%excerpt%`, generic family metadata, mechanical brand/keyword injection, or fixed character limits.
- Metadata alone does not solve substantial Academy↔Magazine overlap.
- DEC-024 preserves the video-first visible-content architecture.
- DEC-119 governs overlap/cannibalization and any differentiate/merge/redirect decision.

## DEC-020 — Product-Page Visible Content Architecture

**Status:** ACCEPTED

- Product pages use a people-first, family-specific content architecture.
- Shared family templates define structure, not duplicated prose.
- Common core: Product identity, verified specs, variants, primary use, necessary usage/handling guidance, limitations/warnings where relevant, and useful contextual links.
- Colors: verified color/surface/technique/volume/fixation/washing facts.
- Mediums: function/use/verified ratios/compatibility/limitations.
- Sets: Woo/YITH-backed composition/count/volume/use/differentiation.
- Tools: factual identity/specs/use/compatibility without false Mariwork branding.
- No fixed word count, filler SEO copy, mandatory FAQ, or unsupported claims.
- Exact copy and visual layout remain implementation-level.


## DEC-021 — Product Category Visible Intro / Content Policy

**Status:** ACCEPTED

- Durable Product Categories are commercial discovery/product-selection pages.
- Use concise useful intros; keep Product grid primary.
- Add supplementary selection guidance only when genuinely useful.
- No fixed word count or filler SEO copy.
- Do not duplicate Product-page copy or Magazine/Academy educational content.
- FAQ is optional.
- Avoid keyword stuffing and boilerplate.
- Child volume-set Categories require genuinely distinct explanatory value.
- Use factual inventory/Product distinctions only.
- Do not falsely brand third-party tools as Mariwork.
- DEC-121–124 may later inform emphasis without artificial duplication.



## DEC-022 — Static / Trust Page Visible Content Policy

**Status:** ACCEPTED

- Static/Trust pages remain purpose-specific people-first support/trust entities.
- About = verified identity/history/people/activity (“Who is Mariwork?”).
- Why Mariwork = verified user-relevant Product/brand differentiators.
- Contact = verified actionable contact/support information.
- Stores = verified physical purchase-location information.
- FAQ = concise genuine answers plus routing: Academy for practical/video how-to, Magazine for explanatory/reference depth, Product/Category for commercial detail.
- No fixed word count or generic SEO filler.
- No unsupported superiority/safety/performance claims.
- No invented local or inventory claims.
- Avoid duplication across Static, Magazine, Academy and Commerce families.
- Canonical factual claims remain governed by DEC-053.


## DEC-023 — Article Update / Freshness Policy

**Status:** ACCEPTED

- Current Article fact-check has already been completed and is not a remaining workstream.
- Article age alone is not a reason to update or rewrite.
- Classify Articles as `KEEP / CURRENT`, `TARGETED UPDATE`, `SUBSTANTIVE UPDATE / REWRITE`, or `OVERLAP REVIEW`.
- Trigger updates when information materially changes, examples/sources become obsolete, factual errors are discovered, relevant Product/method context changes, or the Article no longer adequately serves its intended need.
- Prefer targeted correction over unnecessary full rewrites.
- Preserve original `datePublished`; use `dateModified` only for real content changes.
- Do not manipulate dates to create artificial freshness.
- Magazine remains text-first explanatory/reference content; practical video demonstrations route to Academy.
- Per-Article body-content review happens later as implementation-stage content QA under the accepted Article policies and related intent/linking/overlap Decisions.


## DEC-024 — Academy Course / Lesson Visible Content Standard

**Status:** ACCEPTED

- Academy is video-first practical/instructional content.
- Each Lesson functions as a dedicated watch page with the primary video as dominant content.
- Use natural H1 + clear visible video-lesson context + concise Lesson-specific introduction.
- Supporting modules are optional and practical only: materials/tools, preparation, key steps, practical notes/warnings, genuinely used products/tools, related next Lesson/reference.
- Full transcripts are optional; default to concise summaries/notes for short videos.
- Academy owns practical/demo intent; Magazine owns explanatory/reference text-first intent.
- Supporting Lesson text must not duplicate long-form Magazine content.
- Course page is a concise educational hub for scope, video-learning format and Lesson navigation.
- No generic long SEO copy or mandatory filler modules.
- Overlap/cannibalization remains governed by DEC-119.


## DEC-025 — Durable Product Category Set and Index / Sitemap Policy

**Status:** ACCEPTED

- Durable Product Categories: 1902 Fabric Colors, 28 Mediums/Glitters, 82 Sets root, 220 Tools/Accessories, and 1991/1992/1993 for 30/60/250 ml Sets.
- Durable categories target: 200, index/follow, self-canonical, Product Category sitemap inclusion and crawlable internal navigation.
- Parent Sets category may remain durable with zero direct assignments because it has a genuine child-category hub role.
- Low Product count alone does not disqualify a Category; genuine browse value is required.
- Historical categories 20 (60 ml colors) and 27 (250 ml colors) are not durable.
- Remove 20/27 from SEO architecture/navigation/sitemap, preserve migration evidence, redirect/consolidate their historical URLs to the verified Fabric Colors Category, then delete the obsolete category terms after confirming no operational dependency.
- Do not delete the legacy terms before URL disposition is secured.
- `pa_volume` remains separate under DEC-026.


## DEC-026 — pa_volume Archive Role, Indexability and Sitemap Policy

**Status:** ACCEPTED

- `30ml`, `60ml`, and `250ml` are durable cross-family commercial browse landing pages.
- Target: 200, index/follow, self-canonical, sitemap inclusion and deliberate crawlable internal navigation.
- Product listings must reflect real current availability in the selected volume.
- These pages are distinct from volume-specific Set Product Categories.
- `?filter_volume=` Shop states remain faceted/filter URLs, not search landing pages.
- Where reliable, links from volume pages should preselect the relevant Product variation.
- Title/H1 and visible page copy are decided later under DEC-116 and DEC-117.


## DEC-027 — Product Tags Decommission and Historical URL Mapping Policy

**Status:** ACCEPTED — AMENDED 2026-09-25

- Delete/decommission all 275 current Product Tag terms; they have zero current Product assignments.
- Product Tag archives are not durable SEO/navigation entities and stay out of sitemap/index targets.
- Permanent redirect only when a genuine semantic successor exists inside the commerce/store architecture.
- Allowed destinations: Product, Product Category, approved `pa_volume` landing page, or exceptionally Shop when it is genuinely the closest valid commercial replacement.
- Do not redirect Product Tags to Magazine, Academy, Static pages, Homepage, or unrelated broad destinations.
- Do not map by slug/keyword similarity and do not mass-redirect retired tags merely to avoid 404 responses.
- If no meaningful commerce replacement exists, return a proper 404 or 410; standard 404 is the default unless deliberate 410 is operationally useful.
- Preserve relevant historical evidence before deletion.
- Remove internal remnants and QA redirects for chains/soft 404s.

## DEC-028 — Blog Category Lifecycle Policy

**Status:** ACCEPTED

- Durable Magazine hubs: Educational Articles (71) and History (142).
- Artists (18) is transitional migration infrastructure for the new Artists project, not an ordinary empty-category deletion target.
- After the new Artists system is public/stable: identity-matched historical Artist URLs redirect one-to-one to new Artist profiles.
- Historical Artist URLs with no matching new profile redirect to the main Artists landing page.
- The old Artists category/archive consolidates to the main new Artists landing page.
- Never redirect to draft/private/non-public Artist targets; identity matching must be real, not slug-only.
- All other empty Blog Categories are approved for controlled deletion.
- Retired non-Artist category URLs redirect only when a genuine semantic successor exists; otherwise they return 404.
- Remove obsolete internal references and preserve relevant migration evidence before deletion.


## DEC-029 — Blog Tags Decommission and Mapping Policy

**Status:** ACCEPTED

- Fully delete/decommission all 54 current Blog Tag terms.
- Remove all 39 current Article↔Tag assignments; Article content and durable Blog Category membership remain unchanged.
- Blog Tag archives are not durable SEO/navigation entities and remain out of index/sitemap targets.
- Redirect only when a genuine editorial successor exists: Magazine Category, specific Article, or equivalent Magazine hub.
- Do not redirect Blog Tags to Store/Product destinations merely from keyword overlap.
- Do not map by tag name or slug similarity alone.
- URLs without a meaningful editorial replacement return 404/410; standard 404 is the default.
- Preserve relevant historical evidence and QA internal links, redirects, sitemap leakage and soft 404s.


## DEC-030 — Sitewide Sitemap Membership Policy

**Status:** ACCEPTED

- XML sitemap mirrors the approved canonical Search architecture only.
- Include intentional canonical/indexable targets: Homepage, Shop, indexable Products, durable Product Categories, approved `pa_volume`, durable Static/Trust, Articles, durable Blog Categories, public/indexable Academy Course/Lessons, and future public/indexable Artists URLs after launch.
- Exclude noindex utilities, tags, retired/empty taxonomies, deprecated categories, empty LearnDash categories, search/facet/sort/display/variation-query URLs, pagination, redirects, 404/410, legacy URLs, non-canonical duplicates and non-public content.
- Sitemap membership follows indexability/canonical decisions; it never determines them.
- `lastmod` reflects meaningful changes only.
- Sitemap QA is a dedicated implementation/release gate: validate every emitted URL for 200, indexability, canonical self-consistency, correct family eligibility, and absence of redirects/errors/retired entities; also verify all approved sitemap families are present.


## DEC-031 — Attachment / Media Public and Index Policy

**Status:** ACCEPTED

- Attachment HTML pages are not durable Search landing pages and should not be index/sitemap targets.
- Keep useful media asset files crawlable where required for rendering, Google Images and structured-data references.
- Attachment HTML URLs redirect to a clear owning canonical page when one exists; otherwise may redirect to the retained media file when appropriate; otherwise 404/410.
- Do not mass-redirect Attachment pages to unrelated destinations.
- DEC-031 does not itself authorize Media Library/file deletion.
- Required operational follow-up: inventory and safely remove genuinely unused/orphaned media only after proving no references remain across content, Product galleries/featured images, Academy, taxonomies/static content, schema/metadata, CSS/JS/theme/plugin/custom-field/template/runtime dependencies.
- Media cleanup must be backup/rollback-capable and batch/canary verified.
- Reconcile the current 626-returned vs 845-advertised attachment discrepancy before bulk cleanup.


## DEC-032 — Homepage Organization / WebSite / WebPage Schema Target

**Status:** ACCEPTED

- Keep one coherent Homepage graph: Organization + WebSite + WebPage.
- Keep ImageObject only when genuinely referenced by the graph.
- Homepage must not be Article.
- Rank Math remains the primary JSON-LD/schema owner where supported.
- Remove SearchAction as routine cleanup; Google's sitelinks search box feature is retired.
- Organization properties must be factual and verified; do not force an ecommerce subtype solely because products are sold.
- Do not add a second independent JSON-LD emitter for the same entities.
- Review theme microdata for factual/conflict consistency rather than removing harmless markup blindly.
- Validate rendered structured-data output after implementation.


## DEC-008 — Product Title Naming Standard — Sets / Bundles

**Status:** ACCEPTED

- Set/Bundle titles/H1s use concise purchasable identity plus genuinely identifying count/type and volume where applicable.
- Long `شامل ...` component strings move to Product content rather than the primary title.
- Use Mariwork branding only for genuinely Mariwork-branded Sets.
- Do not force Product codes without a real stable identifier.
- Normalize separators/digits consistently; no URL/slug changes.
- Exact per-Set wording is finalized from current YITH/Woo bundle composition during implementation/content QA.
- DEC-011 is no longer blocked by deferred DEC-008.


## DEC-033 — Static/Core WordPress Page Schema Policy

**Status:** ACCEPTED

- Remove generic Article schema from WordPress Pages where the page is not actually an article.
- Use role-appropriate page semantics, primarily WebPage for Static/Core pages.
- Keep Magazine hub as CollectionPage.
- FAQ-specific schema remains under DEC-086; Stores/local entity treatment under DEC-087.
- Remove Article-derived Person author nodes from generic Static/Core pages unless independently justified.
- Shared Organization/WebSite references must point to the authoritative site entities and must not create conflicting duplicates.
- Rank Math remains the primary schema owner where supported.
- Use representative canary rollout and rendered JSON-LD regression validation before family-wide application.


## DEC-034 — Article Schema Policy

**Status:** ACCEPTED

- Magazine Articles retain `BlogPosting` as the default schema type.
- Use factual headline, representative crawlable image, original datePublished and meaningful dateModified.
- Current Mariwork Articles have no individual named authors: `author` is the authoritative Mariwork `Organization`, not a fabricated/default `Person`.
- `publisher` is the same authoritative Mariwork Organization entity.
- Remove current Article-derived Person author nodes unless a future Article genuinely has an identified individual author.
- Reuse the authoritative Organization entity rather than creating per-Article duplicates.
- Rank Math remains primary schema owner; no duplicate BlogPosting emitter.
- Do not auto-add unrelated FAQ/HowTo/Video schema.
- Validate rendered structured data after rollout.


## DEC-035 — Product Variation ProductGroup / Variant Schema Architecture

**Status:** ACCEPTED

- Use Google's single-page ProductGroup model for real WooCommerce variable Products.
- Parent Product URL remains the single canonical ProductGroup URL.
- Each purchasable variation becomes a variant Product with its own factual Offer and direct preselection URL.
- Volume variation uses supported size semantics; non-volume variable Products use their real supported variation property.
- Do not fabricate identifiers.
- Rank Math Free remains the primary schema owner.
- Do not purchase Rank Math PRO solely for this capability.
- Implement through supported Rank Math server-side schema filters by mutating/replacing the existing Product node; never add a second independent Product/ProductGroup JSON-LD emitter.
- Do not leave conflicting legacy AggregateOffer/Product representation in parallel.
- If a clean single-owner graph cannot be achieved, stop for technical review rather than shipping duplicates.
- Canary one 30/60/250 and one 30/60 Product, then verify non-volume variants separately.
- Validate rendered graph, Offers, preselection, canonical, duplicates and rich-result output; regression-test after Rank Math/Woo updates.


## DEC-036 — Bundle / Set Schema and Visible Component Representation

**Status:** ACCEPTED

- Every current YITH Bundle/Set is a standalone fixed-volume Product with one factual Offer.
- Bundles do not use ProductGroup/hasVariant/isVariantOf.
- Current Bundles do not mix volumes; 30/60/250 ml Bundle identity must reconcile with its component variations.
- YITH/Woo composition is the canonical source for component identity, quantity and selected volume.
- Long component lists stay in visible Product content, not the primary title.
- Bundle price/currency/availability come from the actual purchasable Bundle.
- Existing button/AJAX component lists require crawlability audit.
- Search-visible component content must not require a user click. Prefer server-rendered component HTML with the UI button only toggling visibility.
- If component content is fetched only after click, refactor before accepting it as Search-visible.
- Validate raw HTML, rendered DOM before interaction, network behavior, YITH reconciliation and Google-rendered output.
- Sitewide AJAX/JS rules remain cross-referenced to DEC-080.
- Rank Math remains primary Product schema owner.


## DEC-037 — Academy / LearnDash Schema Ownership and Canary

**Status:** ACCEPTED

- Academy SEO/schema follows semantic role, not raw LearnDash post type.
- Current WP-32714 is a guide collection, not a coherent Course.
- Mariwork Core/UI already expresses this semantic distinction with `راهنما`, `شامل 37 راهنما`, and guide-oriented CTAs such as `دیدن راهنماها`; SEO/schema must mirror that same distinction.
- WP-32714 targets CollectionPage semantics.
- Its 37 children are individual guide/watch pages, not lessons of one single curriculum.
- Future genuine curricula may use Course semantics and course-oriented UI such as `درس` / `شامل N درس` when true.
- UI labels, CTAs, counts, metadata, internal hierarchy and structured data must remain semantically aligned.
- Rank Math remains first owner; Mariwork Core may fill unsupported Academy nodes without a conflicting second graph.
- Current canary: guide collection + two representative guide pages.
- First future true Course requires a separate Course canary.
- VideoObject remains under DEC-038; breadcrumbs under DEC-039.


## DEC-038 — VideoObject Eligibility / Ownership Policy

**Status:** ACCEPTED

- Apply VideoObject by real eligibility, not automatically wherever a video exists.
- Current primary-video guide pages are educational watch-page candidates: WebPage + eligible VideoObject.
- Current guides already have dedicated covers and supporting text that mirrors/emphasizes key points from the video; this is companion educational content, not Article semantics.
- Target layout: H1 + short context → primary video prominently near the top with stable cover/poster → expanded key points/supporting text.
- Do not bury the primary video at the end of a long text block when watching it is the main page purpose.
- Guide CollectionPage itself is not a VideoObject.
- Require factual name, stable crawlable thumbnailUrl and uploadDate; prefer contentUrl, otherwise valid embedUrl; add factual description/duration/creator where available.
- Never fabricate video metadata.
- Mariwork-produced videos may reuse the authoritative Mariwork Organization as creator.
- Player/video must be detectable in Google's rendered HTML without requiring a click to create the only representation.
- Secondary videos on Articles/Products are inventoried but not automatically treated as watch pages.
- Rank Math remains first owner; Mariwork Core may fill unsupported video nodes only in one coherent non-duplicate graph.
- Complete video inventory + two-guide canary before rollout.
- Video sitemap only for verified eligible watch pages; Clip/SeekToAction is optional, not default.


## DEC-038 — VideoObject Eligibility and Ownership Policy

**Status:** ACCEPTED

- VideoObject is eligibility-driven, not automatic.
- Current guide pages have cover/thumbnail + explanatory text + primary instructional video on the same page.
- This structure may qualify as a watch/guide page only when video remains a primary/prominent page purpose.
- Host page remains WebPage; eligible primary video may be mainEntity VideoObject.
- Use only factual name, stable thumbnailUrl, uploadDate, contentUrl/embedUrl, description, duration and creator data.
- Do not fabricate metadata.
- Video/player must be discoverable in rendered HTML without click-dependent loading.
- Guide collection itself is not one VideoObject.
- Secondary videos on Articles/Products are not automatically primary VideoObjects.
- Rank Math remains first owner; Mariwork Core may fill missing nodes only within one coherent graph.
- M-program inventory + two-guide canary required before rollout.
- Verify prominence, fetchability, rendered visibility, schema and Search Console video indexing.
- Video sitemap only for verified eligible watch pages.


## DEC-039 — Breadcrumb Structured-Data Policy Across Store, Academy and Content

**Status:** ACCEPTED

- Use breadcrumbs only where a meaningful site hierarchy exists.
- Breadcrumb trails represent typical user/navigation hierarchy, not mechanical URL paths.
- Store: Shop → durable Product Category → Product.
- Child Set categories preserve approved hierarchy; approved volume landing pages belong under Store, with exact naming deferred to DEC-116.
- Magazine: Magazine → durable primary Blog Category → Article.
- Current Guides: Academy → One-Minute Guides collection → Guide, aligned with DEC-037 and never represented as Course/Lesson.
- Future genuine Courses: Academy → Course → Lesson.
- Homepage, generic Static/Core pages and utility/noindex endpoints do not receive artificial breadcrumbs solely for schema coverage.
- Multi-parent pages use one deliberate stable primary hierarchy.
- Visible breadcrumb UI and structured-data hierarchy must agree.
- Duplicate emitters are only temporarily acceptable when they express the exact same factual trail; conflicting trails must be eliminated.
- Validate representative Store, Magazine, Guide Collection/Guide and future Course templates through rendered output and Rich Results testing.


## DEC-040 — Internal-Link Classification Model

**Status:** ACCEPTED

- Internal-link requirements use three classes: CORE/MANDATORY, FAMILY-SPECIFIC and CONTEXTUAL/OPTIONAL.
- CORE/MANDATORY links apply across every relevant entity in a defined family.
- FAMILY-SPECIFIC links apply only to the defined product/content family.
- CONTEXTUAL/OPTIONAL links are added only when genuinely useful to the page topic or user task.
- Equivalent pages must not randomly differ in mandatory-link coverage.
- Missing mandatory links require correction or an approved documented exception.
- Useful bidirectional Product/Category ↔ Academy/Article relationships are supported.
- Commercial links from informational content must remain contextually justified and must not be forced to increase link count.
- Exact destinations and family-level requirements remain governed by DEC-041 onward.


## DEC-041 — Mandatory Parent/Hub Links by Family

**Status:** ACCEPTED

- Product → stable primary Product Category → Shop.
- Child Product Category → real parent Product Category → Shop.
- Current Guide → One-Minute Guides collection → Academy.
- Future Lesson → genuine Course → Academy.
- Article → stable primary Blog Category → Magazine.
- Multi-parent entities use one deliberate stable primary hierarchy rather than random taxonomy selection.
- The relationship may be supplied through breadcrumb/navigation/taxonomy UI or another appropriate crawlable component.
- Do not force redundant boilerplate parent links into body copy when the hierarchy is already clearly and crawlably represented.
- Cross-family educational/commercial links remain governed by DEC-042–DEC-046.


## DEC-042 — Product to Academy / Article Linking Rules

**Status:** ACCEPTED

- Product → Academy/Article links require direct usefulness for selecting, preparing, using, applying, fixing/curing, caring for, or otherwise correctly working with the Product or Product family.
- Classify approved relationships as CORE/MANDATORY, FAMILY-SPECIFIC, or CONTEXTUAL/OPTIONAL under DEC-040.
- Broad topical similarity alone does not justify a Product-page link.
- Do not mass-add educational links merely to increase internal-link count.
- Maintain exact approved destinations and family coverage in the Internal Link Requirement Matrix.
- Reverse education/content → commercial linking remains governed by DEC-043 and DEC-044.


## DEC-043 — Academy / Lesson to Product / Category Linking Rules

**Status:** ACCEPTED

- Academy/Guide/Lesson → Product/Category links require actual instructional usefulness.
- Link when the Product, material, tool or Product family is used, required, or provides a direct useful next step.
- Prefer a specific Product when a specific item is involved.
- Prefer the relevant Product Category when the user needs to choose among suitable products in a family.
- Do not add generic or unrelated commercial links merely to increase internal-link volume.
- Apply the DEC-040 classification model and maintain approved relationships in the Internal Link Requirement Matrix.


## DEC-044 — Article to Product / Category Linking Rules

**Status:** ACCEPTED

- Article → Product/Category links require a directly relevant and useful commercial next step.
- Prefer a specific Product for product-specific relevance and a Product Category when the reader reasonably needs to choose among a family.
- There is no sitewide requirement for every Article to contain a commercial link.
- Informational Articles may legitimately contain no commercial destination.
- Do not add unrelated or generic commercial links merely to increase internal-link volume or SEO coverage.
- Apply DEC-040 classification and maintain approved relationships in the Internal Link Requirement Matrix.


## DEC-045 — Article to Article / Academy Linking Rules

**Status:** ACCEPTED

- Article → Article/Academy links require semantic relevance and a useful reader next step.
- Valid relationships include continuation, deeper detail, prerequisite/background, complementary reference, or a practical Academy destination.
- No fixed sitewide quota requires every Article to contain a specified number of Article or Academy links.
- Related-content modules must not create random links solely from shared Category/Tag membership.
- Automated and manual destinations follow the same relevance standard.
- Approved relationships are governed by DEC-040 and the Internal Link Requirement Matrix.


## DEC-046 — Category to Education / Reference Linking Rules

**Status:** ACCEPTED

- Listing-only Product Category archives are not required to contain Academy/Article links.
- Category → education/reference links become appropriate when the Category is developed into a content-supported landing page.
- Selected destinations must directly support understanding, selection, preparation, use, technique, or care for that Product Category.
- Do not add generic sitewide education/reference links merely for internal-link coverage.
- Category landing-page content structure and requirements require a separate content decision before implementation.


## DEC-047 — Internal-Link Anchor Text Policy

**Status:** ACCEPTED

- Internal-link anchors must be concise, natural, descriptive, and contextually accurate.
- Exact-match keyword repetition and fixed anchors across all source pages are not required.
- Do not invent query-target anchors without supporting evidence.
- Natural variation is allowed when the destination remains accurately described.
- Avoid generic anchors when a meaningful descriptive phrase is naturally available.


## DEC-048 — Orphan / Underlinked Thresholds and Approved Exceptions

**Status:** ACCEPTED

- Important indexable SEO/IA pages require a meaningful crawlable path from the internal site architecture.
- Orphaned means no meaningful internal crawl path reaches the page.
- Underlinked means required family/matrix relationships are missing.
- Do not define adequate linking with one universal minimum inbound-link count.
- Utility, noindex, temporary, and deliberately non-search-target pages may be documented exceptions.
- Broken URLs/404s are a separate issue.


## DEC-049 — Magazine vs Academy Intent Boundary

**Status:** ACCEPTED

- Academy is Mariwork's video-education destination for practical demonstrations, techniques, step-by-step learning, and product/material/tool use.
- Magazine is the broader editorial destination for fabric-painting and hand-printing art topics, reference/history, news, product introductions, and written tips or techniques.
- A technique or instructional tip does not by itself make Magazine content an Academy item.
- Magazine may link to Academy as a practical video next step; Academy → Magazine is not mandatory.
- Editorial product introduction belongs in Magazine; practical video instruction for product use belongs in Academy.


## DEC-050 — Product vs Category vs Article Query / Content Role Boundary

**Status:** ACCEPTED

- Product owns specific-product intent.
- Product Category/landing pages own product-family, browse, and choice intent.
- Magazine Articles own informational/editorial intent where reading or understanding is primary.
- Avoid assigning substantially the same primary intent across Product, Category, and Article without deliberate justification.
- Ambiguous cases require later keyword/SERP research and explicit page ownership.
- DEC-050 defines role boundaries only; research methodology, ownership mapping, conflict resolution, and implementation remain governed by later decisions.


## DEC-051 — Magazine Hub and Blog Category Hierarchy

**Status:** ACCEPTED

- `/mag/` is Mariwork's primary Magazine hub and editorial discovery surface.
- It provides structured access to Magazine categories and content through deliberate discovery components.
- Magazine categories form the navigational/content hierarchy beneath the hub.
- The hub is not an ordinary Article or Category archive.
- Final category taxonomy, names, and category-specific content strategy remain separate decisions.


## DEC-052 — History / Artists Content Strategy

**Status:** ACCEPTED

- Historical and globally significant artists may be covered as Magazine Articles when editorially, artistically, or historically valuable.
- Relevant History content belongs to the Magazine editorial architecture.
- Artist-focused Magazine Articles are editorial content, not Mariwork Artist profiles.
- `/artists/` and its profiles represent the separate Mariwork Artists directory/project.
- Historical Artist URL migration remains governed by DEC-028 and is not reopened by DEC-052.
- Artist selection, publishing volume, and detailed History editorial planning remain later content-strategy decisions.


## DEC-053 — Canonical Mariwork Facts and Naming-Consistency Registry

**Status:** ACCEPTED

- The owner-confirmed registry in `strategy/BRAND-ENTITY-SEARCH.md` is the factual baseline for Mariwork brand/entity naming, content and schema work.
- Canonical names: `ماری‌ورک` and `Mariwork`; website: `mariwork.ir`.
- Founder: `مریم مختاری` / `Maryam Mokhtari`; canonical title: Founder of Mariwork.
- Start year: 1395 SH; owner-confirmed experience claim: more than 10 years.
- Mariwork is an Iranian specialist brand/business in fabric colors and specialist products for fabric painting and hand printing.
- Mariwork fabric colors are for painting/printing on fabric, not dyeing, and must not be represented as ordinary acrylic paint; detailed technical differences require separate evidence.
- Formulation is performed in Iran by Iranian engineers using foreign-origin materials; production, mixing, filling and final preparation are performed in Iran.
- Core products are Mariwork-manufactured; third-party Other Tools items must not inherit Mariwork brand/manufacturer identity merely from being sold on the site.
- Education is a genuine brand activity and developing the art through education is a main goal.
- Third-party physical outlets are `فروشگاه‌های عرضه‌کننده محصولات ماری‌ورک`, not official/exclusive representatives or branches by default.
- No public official physical brand address is currently defined.
- Exact official social handles/URLs and phone/email/WhatsApp details remain deferred to DEC-127.
- Do not infer or strengthen facts beyond the verified registry.


## DEC-054 — ALT Policy by Image Role

**Status:** ACCEPTED

- ALT is based on image role and page context, not missing-count totals.
- Informative images require concise factual ALT; truly decorative images use empty ALT.
- Store/Product and Academy instructional imagery generally default to informative unless genuinely decorative.
- Reused image files may use different factual ALT across pages when context differs.
- Meaningful Magazine/Article/hero images require ALT; decorative textures, separators and ornament do not.
- Historical/artwork/artist identity facts must be verified, not inferred from the image.
- Homepage/Static/Category meaningful images require ALT; primary logo ALT is concise brand identity; redundant icons beside equivalent text are generally decorative.
- Linked-image ALT should communicate image/link purpose when the image is the meaningful link content without keyword inflation.
- Text-bearing images, infographics and instructional screenshots use concise purpose/meaning-oriented ALT; essential information should also be available in surrounding HTML/caption where appropriate.
- Verified structured facts may generate ALT automatically when image role is deterministic; context-dependent imagery requires contextual judgment.
- Automation must not invent unsupported visual facts or keyword-stuff ALT.
- Product-gallery specifics remain DEC-056.


## DEC-056 — Product Image / Gallery SEO Policy

**Status:** ACCEPTED

- Fabric-color Product primary image intentionally represents the 60 ml package/variant.
- This merchandising decision is not overridden by SEO merely to create a variant-neutral primary image.
- Selecting a volume variant changes the displayed image to the selected-volume image.
- SEO does not require simultaneous display of all volume images when variant-image switching exposes the correct image.
- Gallery count/diversity/composition/order are Product/design decisions, outside SEO unless a concrete discoverability, accessibility, factual-accuracy or Search issue exists.
- ALT remains DEC-054.
- SEO scope is primary/variant image consistency and technical discoverability, not gallery redesign.


## DEC-057 — Article / Academy Instructional Image Policy

**Status:** ACCEPTED

- No fixed SEO image quota applies to Magazine Articles or Academy pages.
- Academy is video-first; supporting images are used only when they materially improve instruction.
- Magazine images are used when they add real explanatory, documentary, artistic, Product or technique value.
- Do not add images merely to satisfy an SEO-image count.
- Instructional imagery must match the actual content context, not act as generic filler.
- Featured Images may represent Articles, but multiple in-body images are not required for SEO.
- ALT remains governed by DEC-054.


## DEC-059 — Store Facets / Sort / Display Parameter Policy

**Status:** ACCEPTED

- `filter_volume`, `orderby`, `per_page`, `per_row` and `shop_view` are Store UI states, not independent SEO landing pages.
- They are not separate Search targets or sitemap entries and should consolidate canonically to the relevant base Shop page.
- Durable `pa_volume` landing pages remain separate indexable SEO pages under DEC-026.
- Product-level `attribute_pa_volume` URLs remain available for direct variant preselection and are not treated as Store facet URLs.
- Avoid blanket robots blocking that could interfere with legitimate variant-selection behavior.


## DEC-060 — Shop Pagination and Legacy `product-page` Policy

**Status:** ACCEPTED

- `/shop/page/N/` is the canonical Shop pagination architecture.
- Legacy `?product-page=N` states must stop being generated.
- Historical `?product-page=N` URLs should consolidate to the corresponding `/shop/page/N/` URL.
- Do not maintain parallel pagination URL systems for the same Shop result pages.
- Product, `pa_volume`, Store facet/sort/display and Product variation-preselection behavior remain governed separately.


## DEC-061 — Product Search URL Policy

**Status:** ACCEPTED

- Internal Product search-result URLs remain user-facing utility pages.
- Keep them `noindex` and out of XML sitemaps.
- Do not optimize them as standalone Search landing pages.
- Keep search functionality available to users.
- Do not block crawling in a way that prevents the `noindex` directive from being seen.
- Durable Product, Category, `pa_volume` and other approved landing pages remain the intended Search targets.


## DEC-062 — Author / Date Archive Public and Indexability Policy

**Status:** ACCEPTED

- Author and Date archives are not independent SEO landing-page families for Mariwork.
- If publicly generated, keep them out of XML sitemaps and prevent them from becoming Search targets through the approved noindex/non-public path.
- Magazine Articles and durable Blog Categories remain the primary editorial discovery/index surfaces.
- Current Articles use the Mariwork Organization rather than individual author entities under DEC-034, so Author archives do not receive separate SEO ownership.
- Do not invent Author/Date archive URLs; verify actual route existence during implementation.


## DEC-063 — Legacy URL Prioritization Rule

**Status:** ACCEPTED

- Review historically valuable Legacy URLs first.
- Priority evidence includes meaningful GSC history, proven backlinks/internal links, identifiable high-value entities, and valuable URLs affected by 404s, bad redirects or redirect chains.
- Low-evidence/unknown URLs receive lower review priority.
- Age, slug similarity, traffic history or an existing redirect alone never proves semantic identity.
- Every final redirect still requires a genuine evidence-backed semantic successor.


## DEC-064 — Legacy Product-Volume Mapping Disposition

**Status:** ACCEPTED

- Proven historical volume-specific Product URLs map to the same current variable Product with the historical volume preselected when that variant still exists.
- Do not infer identity from slug similarity.
- Do not fabricate preselection for a volume that no longer exists.
- UNKNOWN mappings remain blocked until identity is verified.
- Existing 301 behavior must be audited first; do not recreate redirects blindly.
- Redirect owner, including possible Nginx ownership, must be verified rather than assumed.
- Existing parent-Product redirects should be preserved or refined only where needed to retain the proven historical volume selection.


## DEC-065 — Historical Education → Academy Mappings

**Status:** ACCEPTED

- Existing one-to-one 301 redirects from historical `/education/.../` lesson URLs to the corresponding Academy lessons are the intended target state when identity matches.
- Current evidence already shows 36 such mappings; preserve them rather than rebuilding the migration.
- Verify the current redirect owner before implementation changes.
- Remaining archive/pagination/feed UNKNOWNs are separate from Lesson mappings and require their own disposition.
- Do not infer destinations from slug similarity alone.


## DEC-066 — Historical Artist URL Disposition Timing

**Status:** ACCEPTED

- Final historical Artist URL disposition is deferred until the new `/artists/` system is public and stable.
- Review legacy Artist URLs manually after launch.
- Use 301 only where a genuine verified successor exists; otherwise a proper 404 remains an allowed outcome.
- Do not precommit unmatched historical Artist URLs to the Artists hub.
- Do not infer Artist identity from slug/name similarity.
- This supersedes only the historical-Artist redirect fallback in DEC-028/DEC-052; other Artist architecture decisions remain unchanged.
- Non-Artist removed-content disposition is separated into DEC-128.
