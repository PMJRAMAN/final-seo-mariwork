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
