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

`رنگ پارچه [Color Name] ماری‌ورک کد [NNN]`

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
- Final brand spelling follows DEC-053: `ماری‌ورک`.
- Normalize visible Product naming to the canonical spelling when touched under the approved rollout.
- Do not change URLs/slugs solely for spelling normalization.


## DEC-009 — Medium / Additive Product Naming Standard

**Status:** ACCEPTED

Canonical visible Product title/H1 pattern:

`[Exact Product Name] ماری‌ورک کد [NNN]`

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

`[Exact Product Name] ماری‌ورک کد [NNN]`

Rules:
- Do not append `ماری‌ورک` merely because the product is sold on mariwork.ir.
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
- DEC-008 is accepted; global template rollout is no longer blocked by that decision and remains subject to normal canary/regression gates.
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
- After the new Artists system is public/stable, historical individual Artist URLs are reviewed manually under DEC-066.
- Use 301 only when a genuine verified Artist-profile successor exists; otherwise proper 404 is allowed.
- Do not precommit unmatched historical Artist URLs to the Artists hub and do not infer identity from slug/name similarity.
- The old Artists category/archive may consolidate to the new Artists hub only when collection-level equivalence is verified.
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
- Current primary-video Guide pages are educational watch-page candidates only when the video remains a primary/prominent purpose of the page.
- Host page remains WebPage; an eligible primary video may be the page's main VideoObject.
- Current Guide CollectionPage itself is not one VideoObject.
- Guide layout should keep the primary video prominent, with concise context and supporting educational text where useful; supporting text does not turn the Guide into Article semantics.
- Use only factual name, stable crawlable thumbnailUrl, uploadDate, contentUrl or valid embedUrl, and factual description/duration/creator where available.
- Never fabricate video metadata.
- Mariwork-produced videos may reference the authoritative Mariwork Organization as creator when factual.
- Player/video must be detectable in rendered output without requiring a user click to create the only discoverable representation.
- Secondary videos on Articles/Products are inventoried but are not automatically primary VideoObjects/watch pages.
- Rank Math remains first owner; Mariwork Core may fill unsupported video nodes only inside one coherent, non-duplicate graph.
- Complete video inventory and representative Guide canary are required before broad rollout.
- Validate prominence, fetchability, rendered visibility, schema and available Search/video-indexing evidence.
- Video sitemap is not automatic; only consider it for verified eligible watch pages when useful evidence supports it.
- Clip/SeekToAction is optional, not a default requirement.


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
- Historical individual Artist URL disposition is governed by DEC-066: manual post-launch review, verified one-to-one 301 only where a genuine successor exists, otherwise proper 404; no unmatched-Artist fallback to the hub.
- Artist selection, publishing volume, and detailed History editorial planning remain later content-strategy work.


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


## DEC-067 — Redirect Technical Owner and Implementation Path

**Status:** ACCEPTED

- Nginx is the canonical technical owner for Mariwork HTTP redirects, including migration/legacy redirects.
- Preserve correct existing Nginx redirects.
- Add new SEO/migration redirects to the centralized documented Nginx layer unless a narrow exception is explicitly approved.
- Do not maintain duplicate redirect ownership in Rank Math or another layer for the same source URL.
- Audit existing Nginx behavior before any redirect change.
- Nginx ownership is a project architecture/performance preference, not a Google ranking requirement.


## DEC-068 — Canary Size and Rollout Rules by Change Class

**Status:** ACCEPTED

- Default family-level Canary: 5 representative URLs.
- Sample should cover high-value, normal and edge-case behavior where applicable.
- Scale only after successful Codex QA + ChatGPT Final QA.
- Stop and correct/rollback the Canary if regression appears.
- Single-page changes use normal page QA rather than a separate Canary.
- Five is a default, not an inflexible rule.


## DEC-069 — Monitoring Windows and Core Success Metrics
**Status:** ACCEPTED
- Default monitoring checkpoints: 28 and 56 days.
- Compare against appropriate comparable pre-change windows.
- Core Search metrics: clicks, impressions, CTR and average position.
- Add business conversion/revenue metrics only where tracking and attribution are reliable.
- Document justified exceptions for seasonality, low volume or change class.

## DEC-070 — Strategy Lock Scope for Implementation Waves
**Status:** ACCEPTED
- Create Strategy Locks per coherent implementation scope once its blocking decisions are accepted.
- Do not wait for every sitewide decision before executing an independent locked scope.
- Each locked scope may generate its own ordered Execution Backlog.
- Explicitly record cross-scope dependencies and unresolved blockers.


## DEC-074 — Login / My Account Authentication and Account-Page Policy

**Status:** ACCEPTED

- Login and My Account are utility/account surfaces, not SEO landing pages.
- Keep them out of XML sitemaps and noindex.
- Do not add SEO/editorial copy just to optimize them.
- Preserve authentication, account-state and privacy behavior.
- Do not add canonicals solely because these noindex utility pages lack them.


## DEC-075 — Fast Buy Utility / Landing-Page Policy
**Status:** ACCEPTED
- Fast Buy remains a utility/conversion surface, not an SEO landing page.
- Keep it noindex and out of XML sitemaps.
- Do not add SEO/editorial copy merely for optimization.

## DEC-076 — Durable Product Category Metadata Strategy
**Status:** ACCEPTED
- Durable Product Categories receive deliberate category-specific metadata.
- Do not reuse Shop metadata or force one identical template across all categories.
- Final wording is decided later through keyword/search ownership.

## DEC-077 — pa_volume Metadata Strategy
**Status:** ACCEPTED
- Durable 30ml/60ml/250ml landing pages receive their own Title/Meta/H1.
- Keep their metadata distinct from Product Categories and filter parameter states.
- Final wording is decided later through keyword/search ownership.


## DEC-079 — Sitewide Canonical and Duplicate-URL Architecture
**Status:** ACCEPTED
- One intended canonical URL per durable content/entity page.
- Alternate/duplicate spaces must not compete as separate Search targets.
- Use the family-specific approved mechanism rather than a blanket canonical/noindex/redirect rule.

## DEC-080 — Critical JS/AJAX Content and Crawlable-Link Discoverability Policy
**Status:** ACCEPTED WITH TARGETED EVIDENCE
- Important SEO content and primary crawl/discovery links should not depend unnecessarily on JS/AJAX-only interaction when crawlable HTML is practical.
- JS/AJAX remains allowed for UX/dynamic behavior.
- Implementation changes require representative initial-HTML/rendered-DOM evidence first.


## DEC-078 — Preferred Host / Protocol / Trailing-Slash and URL Normalization Policy
**Status:** ACCEPTED
- Preferred canonical host/protocol remains `https://www.mariwork.ir/`.
- Do not introduce a non-www migration without a separate architecture decision.
- Normalize HTTP/non-www alternatives to HTTPS + www.
- Preserve the established trailing-slash convention for normal content URLs.
- Do not change durable slugs merely for cosmetic normalization.
- Nginx owns redirect normalization under DEC-067.


## DEC-081 — Product Identity Source of Truth
**Status:** ACCEPTED WITH TARGETED EVIDENCE
- SKU/GTIN/MPN/brand must come from verified Product/WooCommerce data.
- Never fabricate identifiers for SEO.
- Use Mariwork as brand only for genuine Mariwork-branded/manufactured Products.
- Third-party items retain their real brand.
- Verify current field/source coverage before schema/feed implementation.

## DEC-082 — Product Commercial-Fact Source of Truth
**Status:** ACCEPTED WITH TARGETED EVIDENCE
- Price/currency/sale/availability must come from authoritative WooCommerce commercial state.
- Do not maintain separate manual SEO copies.
- Visible page, schema and feed must agree.
- Verify hooks/edge cases before implementation.

## DEC-083 — Out-of-Stock Versus Discontinued Product Lifecycle
**Status:** ACCEPTED
- Temporary Out of Stock and permanent Discontinued are separate states.
- Temporary stockout normally keeps the Product page with accurate unavailable status.
- Discontinued Products require successor/lifecycle review: preserve, verified redirect, or proper 404/410.
- Do not bulk-redirect discontinued Products to generic destinations.


## DEC-084 — Future Product URL/Slug Change and History-Preservation Policy
**Status:** ACCEPTED
- Preserve old Product URLs when slugs change.
- 301 old URLs via Nginx to the same Product's new canonical URL.
- Update internal links, canonical and sitemap references.
- Do not reuse old Product slugs for different entities.
- Avoid cosmetic-only Product slug changes.

## DEC-085 — Editorial Provenance Policy
**Status:** ACCEPTED
- Use real dates and evidence-based sources where provenance is materially useful.
- Use named authors/reviewers only when verified.
- Never invent credentials, expertise or reviewer identities.
- Mariwork Organization remains the default author unless a genuine approved attribution requirement exists.

## DEC-086 — FAQ Visible-Content / Structured-Data Boundary
**Status:** ACCEPTED
- FAQs must be genuinely useful and visibly present.
- Do not create artificial FAQs for SEO/schema.
- Do not treat FAQ markup as a guaranteed rich-result tactic.
- No hidden or fabricated FAQ content solely for markup.


## DEC-087 — Stores / Location / NAP and Local-Trust Content Role
**Status:** ACCEPTED
- Use the canonical concept `فروشگاه‌های عرضه‌کننده محصولات ماری‌ورک`.
- Do not imply official representation, exclusivity, branch status or Mariwork ownership without evidence.
- Publish only verified store/address/contact facts.

## DEC-088 — Informational Article / Academy Commercial CTA Policy
**Status:** ACCEPTED
- Commercial CTAs are optional and relevance-driven.
- Add Product/Category purchase CTAs only when genuinely useful to the content.
- No fixed CTA count and no mechanical SEO/conversion insertion.

## DEC-089 — Image Filename and Media Naming Policy for New Assets
**Status:** ACCEPTED
- New filenames should be short, descriptive, stable and fact-based.
- Prefer lowercase Latin + hyphens where practical.
- No keyword stuffing or inferred facts.
- No historical bulk rename merely for SEO.


## DEC-090 — Primary / Representative Image, Gallery Consistency and Duplicate/Reuse Policy
**Status:** ACCEPTED WITH TARGETED EVIDENCE
- SEO does not redesign Product galleries governed by DEC-056.
- Image reuse is allowed when relevant and factually accurate.
- Duplication alone is not an SEO defect.
- Review suspected mismatch/misleading reuse before corrective implementation.

## DEC-091 — Image Context, Caption and Linked-Image Behavior Policy
**Status:** ACCEPTED
- Captions are optional and usefulness-driven.
- No mechanical captions for SEO.
- Image links require a relevant intentional destination.
- No image linking merely to create more internal links.

## DEC-092 — Image Discovery / Indexability / Sitemap Treatment
**Status:** ACCEPTED WITH TARGETED EVIDENCE
- Important images on indexable pages should remain crawlable/loadable unless deliberately blocked.
- No mandatory separate image sitemap by default.
- Add dedicated image-discovery mechanisms only when evidence supports a real need.


## DEC-093 — Image Technical Delivery Policy
**Status:** ACCEPTED WITH TARGETED EVIDENCE
- Responsive image delivery must match real component/slot needs on mobile and desktop.
- Use correct responsive candidates plus `srcset`/`sizes`; avoid both materially oversized downloads and undersized/blurry delivery.
- Preserve intrinsic dimensions/aspect ratio where applicable.
- Lazy-load below-the-fold images; do not blindly lazy-load likely LCP/hero images.
- Standardize by component/template and QA mobile/desktop, DPR, bytes, visual quality and LCP/CLS.
- Performance claims require evidence.

## DEC-094 — Video Host-Page / Fetchability / Prominence / Player Policy
**Status:** ACCEPTED WITH TARGETED EVIDENCE
- Important videos need a genuine visible/playable and contextually relevant host page.
- Required player/embed resources must be fetchable where Search discovery is intended.
- VideoObject only when eligibility conditions are actually met.
- Verify representative host/player behavior before broad rollout.

## DEC-095 — Video Title / Description / Naming Standard
**Status:** ACCEPTED
- Use truthful, descriptive, subject-specific video titles/descriptions.
- Avoid generic serial naming, stuffing and fabricated details.
- Visible/contextual naming and eligible structured-data metadata must agree semantically.


## DEC-096 — Video Thumbnail Policy
**Status:** ACCEPTED
- Thumbnails must be factual, clear and representative.
- No misleading thumbnails or one generic thumbnail across unrelated videos.
- Prefer uniqueness when it improves identification; do not create arbitrary SEO-only differences.

## DEC-097 — Video Transcript / Summary / Key-Text Policy
**Status:** ACCEPTED
- Full transcripts are not mandatory for every video.
- Add transcript/summary/steps/key-text only when materially useful.
- No filler text; supporting text must accurately reflect the video.

## DEC-098 — Duplicate / Orphan / Weak-Context Video Lifecycle
**Status:** ACCEPTED
- Media does not get independent SEO treatment merely because it exists.
- Establish the primary useful host/version first.
- Consolidate/remove/de-emphasize/relink redundant or weak instances as appropriate.
- No thin standalone SEO pages for media without a real user/Search role.


## DEC-099 — Brand/Trust Site-Content and Entity-Supporting Page Strategy
**Status:** ACCEPTED
- Entity-supporting pages use only verified Mariwork facts.
- Do not invent awards, credentials, partnerships, legal status, locations or other trust claims.

## DEC-100 — Branded Query and Landing-Page Role Strategy
**Status:** ACCEPTED WITH RESEARCH
- Branded queries do not all default to Homepage.
- Map meaningful branded query clusters to the most appropriate durable page using GSC/search evidence and page role.
- Final query ownership is a later research deliverable.
- Avoid intentional branded cannibalization.


## DEC-102 — Release Isolation / Change Annotation / Comparable Baseline
**Status:** ACCEPTED
- Record implementation time, exact scope, affected URLs/entities and change references.
- Capture comparable pre-change baselines where practical.
- Avoid overlapping unrelated systemic changes when attribution would become ambiguous.
- Record material confounders.

## DEC-103 — Monitoring Outcome Interpretation
**Status:** ACCEPTED
- Allowed outcomes: KEEP / ITERATE / ROLLBACK-CANDIDATE / INCONCLUSIVE.
- No automatic rollback from short-term movement alone.
- Consider comparable windows, confounders and evidence strength.
- Do not claim causality from timing alone.

## DEC-104 — Ongoing SEO Maintenance Triggers
**Status:** ACCEPTED
- Triage new URLs/entities, 404/redirect issues, plugin/platform regressions, relevant Google changes, freshness, price/schema consistency and systemic findings.
- Triage does not itself authorize Production changes.


## DEC-107 — Feed URL Crawl / Index Policy
**Status:** ACCEPTED
- WordPress/RSS/feed URLs are system distribution endpoints, not SEO landing pages.
- Keep them out of XML sitemaps and do not optimize them as Search targets.
- Do not disable or robots-block feed functionality solely for SEO without a separate technical reason.


## DEC-108 — General Internal-Search Result URL Policy
**Status:** ACCEPTED
- Internal-search URLs are utility/noindex and excluded from XML sitemaps.
- Preserve search functionality and allow crawlers to read noindex.

## DEC-109 — 404 / Soft-404 / Error-Page Lifecycle Policy
**Status:** ACCEPTED
- No genuine successor: proper 404/410.
- Verified semantic successor: permanent 301 via Nginx.
- Helpful error UX must retain the correct HTTP error status.
- No generic fallback redirects merely to eliminate 404s.

## DEC-110 — Search-Crawler Access / Training-Crawler Separation
**Status:** ACCEPTED WITH TARGETED EVIDENCE
- Keep public SEO targets accessible to legitimate Search crawlers including Googlebot and OAI-SearchBot.
- Treat OAI-SearchBot Search eligibility separately from GPTBot training use and ChatGPT-User.
- Verify robots/WAF/server access before implementation.
- AI citation/content strategy is separately governed by DEC-129.


## DEC-111 — Mobile / Core Web Vitals / Page Experience Remediation Policy
**Status:** ACCEPTED WITH TARGETED EVIDENCE
- Prefer field evidence; use lab data for diagnostics.
- Reference targets: LCP <= 2.5s, INP <= 200ms, CLS <= 0.1.
- Evaluate mobile and major templates separately.
- Fix evidenced bottlenecks; do not optimize for a perfect lab score.
- No ranking/traffic guarantee from CWV changes alone.

## DEC-112 — Concern-by-Concern SEO Technical Ownership
**Status:** ACCEPTED
- One primary owner per SEO concern.
- Rank Math first for supported metadata/robots/canonical/sitemap/schema.
- Nginx owns redirects under DEC-067.
- WooCommerce owns authoritative Product commercial facts.
- Custom code only when needed; no duplicate parallel owners.

## DEC-113 — Shipping / Returns Source of Truth
**Status:** ACCEPTED WITH TARGETED EVIDENCE
- Shipping/return facts come only from real business/WooCommerce rules.
- No invented SEO values.
- Visible policy and structured data must agree.
- Verify actual rules before implementation.


## DEC-114 — Homepage Visible Content and CTA Structure
**Status:** ACCEPTED
- Homepage is the main brand/entity gateway and cross-family navigation hub.
- Keep brand introduction concise and useful.
- Use CTAs toward major durable hubs.
- No long SEO-first filler sections.

## DEC-115 — Durable Product Category Title/H1 Naming Standard
**Status:** ACCEPTED
- H1 is concise and based on the real category/family identity.
- Brand and extra modifiers are not mandatory in H1.
- Title may be more descriptive when research supports it.
- Final wording comes later from keyword/query ownership.

## DEC-116 — pa_volume Title/H1 Naming Standard
**Status:** ACCEPTED
- Do not use bare 30ml/60ml/250ml as the complete H1/title.
- Naming must state the relevant product family/intent.
- Human-facing H1 and Search-oriented Title may differ where justified.


## DEC-117 — pa_volume Visible Landing-Content Standard
**Status:** ACCEPTED
- Retained indexable pa_volume landings get a short useful distinct content block.
- Explain the volume role and what users will find.
- No artificial long SEO copy.
- Follow DEC-130.

## DEC-118 — Durable Blog Category Presentation / Content Standard
**Status:** ACCEPTED
- Durable indexable Blog Categories get deliberate Title/H1/Meta plus a short category-specific intro block.
- Empty/temporary/noindex categories are excluded.
- Follow DEC-130.

## DEC-119 — Content Overlap / Cannibalization Resolution Policy
**Status:** ACCEPTED
- Topic similarity alone is not cannibalization.
- Academy = video-first practical/demo intent.
- Magazine = text-first explanatory/reference/editorial intent.
- Differentiate/merge/redirect only when evidence shows substantial same-intent overlap.

## DEC-130 — Durable Indexable Archive/Hub Visible Content-Block Standard
**Status:** ACCEPTED
- Every durable indexable archive/hub used as a Search/user destination gets a short, unique, useful visible content block.
- Applies to Shop, Product Categories, pa_volume, Academy, Magazine, durable Blog Categories and future equivalent indexable archives.
- Explain why the page exists, what users find there and its specific role.
- Human-first, concise, SEO-aware; no filler, stuffing or duplicated intros.
- Noindex/system/utility/empty/temporary archives are excluded.


## DEC-120 — Global Header/Footer/Navigation SEO Link Architecture
**Status:** ACCEPTED
- Global navigation exposes durable hubs and essential destinations only.
- No SEO-driven link inflation.
- Contextual relationships remain body-link decisions.

## DEC-121 — Semantic Positioning and Product Value Pillars
**Status:** ACCEPTED — FOUNDATIONAL
- This is the foundation of Mariwork's content strategy.
- Define semantic positioning and approved value pillars before keyword/topic expansion.
- Core directions include fabric suitability, application quality, durability/stability, compatibility and economic value.
- Economic value does not mean lowest price; it means evidence-backed useful performance/quality/efficiency/reduced waste or rework.
- Claims require evidence.
- DEC-122–125 and later content planning must derive from this foundation.

## DEC-122 — Topic / Keyword Cluster Research and Prioritization
**Status:** ACCEPTED
- Research clusters after and within DEC-121 positioning.
- Group by intent/problem/topic, not keyword variants.
- Prioritize with relevance, evidence, user value, GSC/SERP data and realistic opportunity.
- Search demand refines expression/priorities; it does not invent positioning.


## DEC-123 — Cluster-to-Page-Family Ownership Map
**Status:** ACCEPTED
- One primary durable owner per approved topic/query cluster.
- Avoid duplicate ownership, doorway variants and parallel same-intent pages.
- Supporting pages may contribute only with distinct roles.
- Final mapping remains evidence-based.

## DEC-124 — Content Journey and Coverage Strategy by Cluster
**Status:** ACCEPTED
- Build coherent content journeys, not isolated pages.
- Cover awareness → understanding → instruction/comparison → product selection/use/care as relevant.
- Distinct page roles and useful cross-family handoffs; no duplicated coverage for volume alone.

## DEC-125 — Product/Brand Claim Evidence Standard
**Status:** ACCEPTED
- Product/brand claims require claim-appropriate evidence.
- Verified specs/instructions, documented tests, reliable business data or credible sources may support claims.
- Marketing attractiveness alone is not evidence.
- Comparative/superiority and safety claims require especially strong support.


## DEC-127 — Official Social/Profile and Contact Registry
**Status:** ACCEPTED — OWNER DETAILS PENDING
- Only owner-verified official profile/contact details may be used.
- Confirmed channels: Instagram, YouTube, Telegram, Aparat, phone, email and WhatsApp.
- Exact values remain pending owner input; no inference is allowed.

## DEC-128 — Other Removed-Content Legacy URL Disposition
**Status:** ACCEPTED — URL-LEVEL EVIDENCE MAY BE PENDING
- Verified semantic successor → 301.
- No genuine successor → proper 404/410.
- No generic fallback redirects to unrelated destinations.

## DEC-129 — AI Assistant / Generative-Answer Discoverability, Citation and Content Strategy
**Status:** ACCEPTED — FOUNDATIONAL
- AI-answer discoverability and citation is a first-class Mariwork SEO/content objective.
- Separate crawl eligibility from citation-worthiness.
- Optimize around conversational intent, answerable structure, first-hand evidence, provenance, entity consistency, multimodal support, freshness and measurable citation/referral evidence.
- No thin GEO/FAQ scaling, fabricated authority or undocumented AI tricks.
