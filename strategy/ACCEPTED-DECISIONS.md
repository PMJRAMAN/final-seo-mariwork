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

**Status:** ACCEPTED

- Course and Lesson titles describe the actual educational unit naturally.
- Default: Course H1 = Course SEO `<title>`.
- Default: Lesson H1 = Lesson SEO `<title>`.
- Remove repetitive `- رنگ پارچه ماری ورک` suffixes.
- Include Mariwork only when naturally part of the subject or Course identity.
- Preserve sequence numbers only for genuine multi-part instructional series.
- Retain existing titles when clear and accurate.
- Rewrite only when materially vague, inaccurate, misleading, excessively verbose, or inconsistent with content.
- Do not change URLs/slugs solely because titles are normalized.
- Schema/video naming follows visible Lesson identity; schema ownership/eligibility remains DEC-037/038.


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
