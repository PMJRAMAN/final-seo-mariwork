# SEO Decision Log

Accepted decisions override lower-level workflow/playbook text when applicable, but never override Manifest without formal Manifest change.

## SEO-001 — Dual Audit Mandatory
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** PROCESS

Codex Audit + independent ChatGPT Second Review before APPROVED.

## SEO-002 — Repository as Source of Truth
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** PROCESS

این repository مرجع رسمی dossier، findings، decisions و change history است.

## SEO-003 — Raw Search Data Is Immutable
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** DATA

Raw exports edit نمی‌شوند.

## SEO-004 — Page/Query Attribution Requires Joined Evidence
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** DATA

Query مستقل به URL خاص نسبت داده نمی‌شود مگر Page+Query relation اثبات شده باشد.

## SEO-005 — Findings Require Scope
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** PROCESS

PAGE/FAMILY/SITEWIDE اجباری.

## SEO-006 — Audit Is Read-Only on Production
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** OPERATIONS

Audit هیچ write روی Production ندارد.

## SEO-007 — Stable Entity ID Over Slug
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** REPOSITORY

برای WP/Woo entity، stable ID هویت dossier است.

## SEO-008 — Sitewide Technical Baseline Before Page Batches
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** PROCESS

Inventory و baseline فنی سراسری قبل از audit گسترده صفحه‌ها انجام می‌شود.

## SEO-009 — Independent Final QA After Implementation
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** PROCESS

Codex QA کافی نیست؛ ChatGPT Final Acceptance QA قبل از Monitoring الزامی است.

## SEO-010 — Systemic Changes Need Change Dossier
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** OPERATIONS

FAMILY/SITEWIDE change باید canary/regression/rollback plan داشته باشد، در صورت عملی بودن.

## SEO-011 — Framework v1.0 Freeze
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** PROCESS

بعد از این review ساختار framework فقط طبق Change Control تغییر می‌کند.

## SEO-012 — Final Content Requires ChatGPT Approval
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** CONTENT

Codex draft به‌تنهایی Production-ready نیست. Target content/facts باید در dossier/brief تأیید شده باشد.

## Template

```markdown
## SEO-XXX — Title
**Status:** Proposed | Accepted | Superseded
**Date:** YYYY-MM-DD
**Scope:** PAGE | FAMILY | SITEWIDE | PROCESS | DATA | OPERATIONS | CONTENT
**Supersedes:** optional

### Decision
### Evidence
### Consequences
### Exceptions
```


## SEO-013 — Google Official Documentation Governs SEO Recommendations
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** PROCESS / CONTENT / OPERATIONS

هر پیشنهاد فنی یا محتوایی SEO باید با مستندات رسمی فعلی Google Search سازگار باشد. توصیه vendor جای استاندارد Google را نمی‌گیرد.

## SEO-014 — Rank Math First SEO Ownership
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** OPERATIONS

هر concern SEO که نسخه نصب‌شده Rank Math واقعاً پشتیبانی می‌کند باید از همان مسیر مدیریت شود. Custom SEO PHP پراکنده و duplicate owner ممنوع است.

## SEO-015 — Master TODO Is the Execution Authority
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** PROCESS

`MASTER-TODO.md` مرجع ترتیب familyها و پوشش کامل سایت است. همه URL/entityهای inventory باید disposition نهایی داشته باشند.


## SEO-016 — Autonomous Round-1 Audit Orchestration
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** PROCESS / OPERATIONS

Phaseهای تحقیق اولیه و Codex Audit می‌توانند توسط runner به‌صورت autonomous و resumable اجرا شوند تا `CODEX_AUDITED`. این یک extension سازگار با Framework v1.0 است و lifecycle یا authority را تغییر نمی‌دهد. ChatGPT Second Review نخستین human decision gate باقی می‌ماند و Production write قبل از APPROVED همچنان ممنوع است.


## SEO-017 — Low-Consumption Round-1 Execution
**Status:** Accepted  
**Date:** 2026-09-24  
**Scope:** PROCESS / OPERATIONS

Round-1 evidence collection is deterministic by default and Codex is reserved for material synthesis/judgment.

- public HTTP/HTML/meta/canonical/schema/link evidence is collected once by Python and reused;
- A-014 + A-015 are one model synthesis;
- A-016 + A-017 are deterministic and use no model call;
- A-018 + A-019 + A-020 are one model synthesis;
- A-021 is deterministic;
- the five-page pilot remains capped at five entities; later page audits default to 15 entities per model execution;
- Product Tags, Blog Tags, attributes, attachments and other policy/system URL spaces are handled at FAMILY/SITEWIDE level rather than one model call per URL where appropriate;
- Foundation reasoning defaults to medium and repetitive page-batch reasoning to low;
- Codex network access is disabled in autonomous analysis so it must reuse repository evidence instead of recrawling;
- raw Codex JSONL is retained privately for observability.

This is an execution-efficiency change only. Dual Audit, complete-site coverage, Production read-only rules and human/ChatGPT approval authority are unchanged.


## SEO-018 — GPT-5.6 Luna Medium for Autonomous Round-1
**Status:** Accepted
**Date:** 2026-09-24
**Scope:** PROCESS / OPERATIONS
**Supersedes:** SEO-017 only for autonomous model selection and page-batch reasoning level

All autonomous Round-1 model calls are pinned to `gpt-5.6-luna` with `medium` reasoning.

- Foundation synthesis uses `gpt-5.6-luna` / medium.
- Page-audit batches also use `gpt-5.6-luna` / medium.
- Deterministic/no-model jobs remain deterministic.
- The runner must refuse a different configured model during autonomous execution.
- Evidence reuse, grouped calls, batch sizing, Production read-only rules and human approval gates remain unchanged.

This is an execution-model decision only and does not change SEO authority, lifecycle, audit coverage or Production permissions.


## SEO-019 — Decision Backlog Before Execution
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** PROCESS / OPERATIONS / CONTENT

### Decision

After Codex Audit and ChatGPT Second Review, Mariwork SEO enters a deliberate Strategy / Decision Phase before Production implementation.

The workflow has three separate authorities:

1. `MASTER-TODO.md` = complete-project coverage and program ordering.
2. `strategy/DECISION-BACKLOG.md` = unresolved and accepted target-state decisions.
3. `tasks/EXECUTION-BACKLOG.md` = implementation packages generated only from accepted decisions.

No audit finding, Second Review recommendation, MASTER-TODO checkbox, or Codex suggestion by itself authorizes a Production write.

A Codex Production implementation task may be issued only when:
- all blocking Decision IDs are `ACCEPTED`;
- the corresponding Execution item is `READY_FOR_TASK`;
- exact target state and write scope are known;
- required Change Dossier/canary/rollback/QA gates are satisfied;
- final visible content is approved where applicable.

Codex cannot mark strategy decisions `ACCEPTED` and cannot infer unresolved business/editorial strategy from audit evidence.

### Evidence

- Full-site audit closure: `af0cd7d9436291047ed8925d8c3391f032910ead`
- ChatGPT full-site Second Review: `audits/second-review/sitewide/SR-005-CHATGPT-FULL-SITE-SECOND-REVIEW.md`
- Existing M-02, M-07, M-11, M-15 and M-17 gates.
- Owner requirement to complete target-state decisions collaboratively before generating the final implementation TODO and Codex tasks.

### Consequences

- Strategy may be decided incrementally over multiple sessions.
- GitHub preserves every durable decision between sessions.
- Execution work is derived from accepted decisions rather than from raw findings.
- Independent scopes may be implemented earlier only when unresolved decisions cannot materially change them.
- Cross-family changes such as internal linking remain locked until dependent family decisions are sufficiently stable.

### Compatibility

This is a backwards-compatible clarification of the existing approval/implementation workflow. It does not add or remove lifecycle statuses, change dossier identity, or transfer approval authority.

Detailed rule: `docs/DECISION-TO-EXECUTION-GOVERNANCE.md`.


## SEO-020 — Decision Backlog v1 Coverage Freeze
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** PROCESS / STRATEGY

### Decision

The **coverage/structure** of the Mariwork SEO Decision Backlog is frozen as v1 after P-001 through P-004 reconciliation.

Canonical decision range:

`DEC-001`–`DEC-120`

P-004 reports zero unexplained material decision-domain gaps.

This freeze means the project may begin owner + ChatGPT decision sessions using the Decision Backlog as the canonical strategy queue.

It does **not** accept the target state of any OPEN, PROPOSED or NEEDS_TARGETED_EVIDENCE item and does not authorize Production.

### Evidence

- `audits/strategy/DECISION-BACKLOG-COVERAGE-AUDIT.md`
- `audits/strategy/P-002-CHATGPT-DECISION-COVERAGE-REVIEW.md`
- `audits/strategy/P-003-DECISION-BACKLOG-RECONCILIATION.md`
- `audits/strategy/P-004-CANONICAL-DECISION-COVERAGE-MATRIX.json`
- `audits/strategy/P-004-DECISION-COVERAGE-CLOSURE.md`

### Change rule

New Decision IDs may be appended only when future discovery or platform/site changes introduce a genuinely new material target-state choice.

Existing Decision IDs are never renumbered.

Operational, evidence or QA mechanics must not be promoted into Decision IDs merely to increase coverage count.

### Consequences

- Decision sessions may now start.
- Execution packages remain locked until their blocking decisions are ACCEPTED.
- P-006/P-007 must reconcile Execution Backlog dependencies against the frozen v1 Decision range before an EXE item can become READY_FOR_TASK.


## DEC-001 — Durable Site-Family Roles
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** SITEWIDE / INFORMATION ARCHITECTURE

### Accepted target state

- Homepage = brand/entity and primary navigation root.
- Shop = broad commercial discovery hub.
- Durable Product Categories = commercial category hubs for real stable product families.
- Product pages = exact transactional entities.
- Academy / Course / Lessons = structured educational content.
- Magazine / Articles = informational/reference content.
- Only genuinely useful, populated Blog Categories = editorial content hubs.
- Static pages = trust/support entities such as About, Why Mariwork, Contact, Stores and FAQ.
- Transitional, empty, utility, machine and legacy URL spaces are not promoted to durable content families by this decision; their dedicated DEC items govern them.

### Consequence

Later title/meta/content/schema/internal-link/indexability decisions must preserve these family roles unless a later accepted decision explicitly supersedes this architecture.


## DEC-002 — Homepage Role and Metadata Baseline
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** HOMEPAGE

### Accepted target state

- Homepage remains Mariwork's Brand/Entity + top-level navigation page.
- Keep current Title as baseline: `رنگ پارچه ماری‌ورک | تولیدکننده تخصصی رنگ پارچه`.
- Keep current H1 as baseline: `رنگ پارچه ماری‌ورک`.
- Keep current Meta Description as baseline.
- Do not expand Homepage title with additional category/product keyword stuffing.
- H1 does not need to duplicate the full SEO title.
- Future changes require materially better intent evidence, verified brand-fact changes, or a deliberate Homepage content-strategy change.
- Brand factual claims such as «بیش از ۱۰ سال» remain subject to DEC-053 factual verification.


## DEC-003 — Shop Target State
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** SHOP / COMMERCIAL DISCOVERY

### Accepted target state

- `/shop/` remains indexable and self-canonical.
- Shop remains Mariwork's broad commercial discovery hub and primary all-products listing.
- Product grid/listing remains a primary part of the page; this decision does not require a layout redesign.
- Add one visible H1: `فروشگاه ماری‌ورک`.
- Use SEO title: `فروشگاه ماری‌ورک | رنگ پارچه، مدیوم، ست و ابزار`.
- Replace the broken archive-generated meta description with a factual Shop-specific description.
- Shop should help users/crawlers discover durable Product Categories and Products.
- Shop must not replace or intentionally compete with category-specific landing pages.
- Any future category shortcuts or short introductory copy must support product discovery rather than displace the all-products listing.


## DEC-004 — Cart / Checkout Transactional Utility Policy
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** SYSTEM-COMMERCE

### Accepted target state

- Cart and Checkout are transactional utility endpoints, not search landing pages.
- Cart remains `noindex, follow`.
- Checkout remains a non-search transactional endpoint; in the empty public state it may redirect to Cart.
- Keep Cart/Checkout out of sitemap/index targets.
- Do not add editorial SEO copy or independent commercial schema to these endpoints.
- Do not introduce crawl blocking that would prevent the intended noindex directive from being seen.
- Missing canonical on these noindex utility states is not, by itself, an implementation defect.
- No Production change is required where current behavior already matches this policy.


## DEC-005 — LearnDash Course Category Public Role
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** ACADEMY / LEARNDASH TAXONOMY

### Accepted target state

- Current `Free` and `Paid` LearnDash Course Categories are not durable public SEO entities.
- Keep them out of index targets, sitemaps and deliberate Academy navigation.
- Current public 404 behavior is acceptable while the terms are empty.
- The terms may remain internally if LearnDash needs them operationally.
- If they are not operationally needed, cleanup may be handled separately.
- Do not redirect these URLs to Academy or the current course without a proven semantic replacement.
- If Mariwork later develops a real multi-course free/paid architecture, reopen the taxonomy strategy through a new decision.


## DEC-006 — Durable vs Transitional Taxonomy Architecture
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** SITEWIDE / TAXONOMY ARCHITECTURE

### Accepted target state

Mariwork taxonomy architecture is intentionally selective.

- Only taxonomies with a durable, distinct user-facing browse or content role may become public SEO landing pages.
- Durable Product Categories and useful populated Blog Categories form part of the final site architecture.
- `pa_volume` remains conditional and is governed separately by DEC-026.
- Product Tags, Blog Tags, migration-era Product Categories, empty LearnDash categories, and other transitional or empty taxonomies are not durable SEO entities.
- Transitional or empty taxonomies must not be promoted through sitemap membership, navigation, or SEO content merely because they exist in WordPress.
- Every taxonomy family requires its own lifecycle and indexability decision before implementation.


## DEC-007 — Fabric-Color Product Naming Standard
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** PRODUCT / FABRIC COLORS

### Accepted target state

The canonical visible Product title/H1 pattern for Mariwork fabric-color products is:

`رنگ پارچه [Color Name] ماری ورک کد [NNN]`

Rules:
- Start with the product type `رنگ پارچه`.
- Follow with the exact factual color name.
- Include the canonical Mariwork brand spelling.
- End with the stable product code.
- Do not use decorative separators such as `|` or `-` inside the visible Product title/H1.
- Use one consistent numeral system for product codes; Latin digits are preferred for identifier consistency.
- Do not add 30/60/250 ml volume tokens to the parent Product title when those volumes are variants of the same Product.
- Visible-title normalization must not trigger mass Product URL/slug changes.
- SEO `<title>` template behavior is governed separately by DEC-011.
- Final Mariwork brand spelling follows DEC-053.
- Persian half-space usage is a writing and brand-consistency standard, not a standalone SEO requirement.
- Do not perform bulk URL or content changes solely to normalize half-space usage.


## DEC-009 — Medium / Additive Product Naming Standard
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** PRODUCT / MEDIUMS / ADDITIVES

### Accepted target state

The canonical visible Product title/H1 pattern is:

`[Exact Product Name] ماری ورک کد [NNN]`

Rules:
- Use the exact factual Product identity; do not force every product to include the generic term `مدیوم`.
- Preserve specific Product identities such as glitter, varnish, glue, shine, base coat, fixative, or medium where factually appropriate.
- Include the canonical Mariwork brand spelling.
- End with the stable Product code.
- Remove decorative separators such as `|` and `-` from the visible Product title/H1.
- Use consistent Latin digits for Product codes.
- Do not include volume in this family under any circumstance.
- English technical terminology may be retained only when it is a genuine, useful Product name/synonym, not for keyword expansion.
- Visible-title normalization must not trigger URL/slug changes.
- SEO `<title>` behavior is governed separately by DEC-011.
- Brand spelling and Persian half-space conventions follow DEC-053.


## DEC-010 — Tools / Accessories Product Naming Standard
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** PRODUCT / TOOLS / ACCESSORIES

### Accepted target state

Product naming must reflect the product's actual brand ownership.

For third-party or generic tools/accessories:

`[Exact Product Name] [Code if factually applicable]`

For products genuinely branded/manufactured by Mariwork:

`[Exact Product Name] ماری ورک کد [NNN]`

Rules:
- Do not append `ماری ورک` merely because the product is sold on mariwork.ir.
- Include the Mariwork brand only when the product is factually Mariwork-branded or manufactured.
- For third-party products, include the actual third-party brand only when it is a genuine part of the Product identity.
- Include a code only when it is a real, stable Product identifier.
- Never invent a brand or Product code for SEO purposes.
- Remove decorative separators such as `|` and `-`.
- Do not include volume in the visible Product title/H1.
- Include model/size only when it identifies a genuinely distinct Product rather than an ordinary variation.
- Visible-title normalization must not trigger URL/slug changes.
- SEO `<title>` behavior is governed separately by DEC-011.


## DEC-011 — Product Visible Title / H1 and SEO Title Relationship
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** PRODUCT / TITLE TEMPLATE

### Accepted target state

The WooCommerce Product title / visible H1 is the primary source of Product identity.

Default Rank Math Product SEO title template target:

`%title%`

instead of:

`%title% %sep% %sitename%`

Rules:
- By default, Product SEO `<title>` should match the approved visible Product title/H1.
- Do not automatically append the site name when the Product title already contains sufficient Product/brand identity.
- Avoid repetitive family-wide boilerplate such as `Product Name - رنگ پارچه ماری ورک`.
- A page-specific SEO title may differ only when a concise factual distinction materially improves clarity.
- Do not use SEO-title exceptions for keyword expansion or artificial brand insertion.
- Third-party/generic Products must not receive Mariwork branding merely through the SEO-title template.
- Product title normalization must be completed before the global Rank Math Product title template is changed.
- Global implementation remains blocked until deferred DEC-008 is resolved.
- Template rollout requires regression checks for unique, descriptive titles and absence of unintended duplicate branding.


## DEC-012 — Static / Core Page Title and H1 Policy
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** STATIC / CORE PAGES

### Accepted target state

Static/Core pages use concise, page-specific SEO titles and clear visible H1s. Repetitive global suffixes such as `- رنگ پارچه ماری ورک` are not required when a shorter branded page title already identifies the page.

Approved targets:
- About: SEO title `درباره ماری‌ورک`; H1 `درباره ماری‌ورک`. Existing creative tagline may remain as supporting copy, not the sole H1.
- Contact: SEO title `تماس با ماری‌ورک`; H1 `با ماری‌ورک در تماس باشید`.
- Magazine: SEO title/H1 `مجله ماری‌ورک`.
- Why Mariwork: SEO title `چرا ماری‌ورک؟`; H1 `چرا رنگ پارچه ماری‌ورک؟`.
- Stores: SEO title `فروشگاه‌های ماری‌ورک`; H1 `فروشگاه‌های ماری‌ورک نزدیک شما`.
- FAQ: SEO title `سوالات متداول ماری‌ورک`; H1 `سوالات متداول`.

Rules:
- SEO title and H1 do not need to be identical, but they must describe the same page role/topic.
- Each page should have one clear primary H1.
- A creative tagline should not replace a descriptive primary H1 when it obscures page identity.
- Avoid repetitive site-wide title boilerplate when the page title already carries sufficient brand/context.
- Do not add keywords unrelated to the actual page purpose.
- Canonical brand spelling remains governed by DEC-053.


## DEC-013 — Article Title / H1 Convention
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** EDITORIAL / ARTICLES

### Accepted target state

Mariwork editorial Articles use natural, reader-facing titles based on the actual subject of each Article rather than a mechanical SEO keyword template.

Default relationship:

`Article H1 = Article SEO <title>`

Rules:
- Use one clear, descriptive primary H1.
- By default, the SEO `<title>` uses the approved Article title without an automatic site-wide keyword suffix.
- Remove the repetitive `- رنگ پارچه ماری ورک` suffix from the default Article title template.
- Include terms such as `رنگ پارچه` or `ماری ورک` only when they naturally describe the Article's actual subject.
- Do not mechanically inject keywords, brand terms, dates, “complete guide”, “best”, or similar modifiers merely for SEO.
- Existing Article titles should be retained when accurate, clear and useful.
- Rewrite a title only when materially vague, inaccurate, misleading, excessively verbose, or inconsistent with the Article content.
- Visible title normalization must not trigger URL/slug changes.
- Potential overlapping/cannibalizing Articles are governed separately by DEC-119.


## DEC-014 — Academy Course / Lesson Title and H1 Convention
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** ACADEMY / COURSE / LESSON

### Accepted target state

Mariwork Academy titles describe the actual educational unit naturally and independently, without a repetitive global SEO keyword suffix.

Default relationships:

`Course H1 = Course SEO <title>`

`Lesson H1 = Lesson SEO <title>`

Rules:
- Use one clear, descriptive primary H1 for every Course and Lesson.
- Remove the repetitive default `- رنگ پارچه ماری ورک` suffix from Course/Lesson SEO titles.
- Include `ماری ورک` only when it is naturally part of the actual educational subject or Course identity.
- Do not automatically inject brand, product, or keyword terms into generic instructional lessons.
- Preserve sequence numbers only when they represent a genuine multi-part instructional sequence.
- Do not infer a sequence merely because legacy titles contain numeric suffixes.
- Existing clear and accurate Course/Lesson titles should be retained.
- Rewrite only when a title is materially vague, inaccurate, misleading, excessively verbose, or inconsistent with the instructional content.
- Title normalization must not trigger URL/slug changes.
- Video/schema naming should remain consistent with the approved visible Lesson identity, while schema ownership and eligibility are governed separately by DEC-037 and DEC-038.


## DEC-015 — Product Meta Description Strategy
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** PRODUCT / META DESCRIPTION

### Accepted target state

This is a general policy. Exact per-Product meta copy is not fixed by this Decision and remains subject to implementation-stage content QA.

- Rank Math `%excerpt%` must not remain the final default Product meta-description strategy.
- Product meta descriptions should be page-specific, factual, concise, and based on verified Product data.
- Each description should summarize the specific purchasable Product and its primary factual purpose or differentiator.
- Avoid generic educational/history copy that does not specifically describe the Product.
- Avoid duplicate or near-duplicate descriptions across materially different Products.
- Do not use keyword lists or mechanical keyword repetition.
- Do not impose an arbitrary fixed 150/160-character rule; descriptions should be concise and sufficiently informative.
- Avoid hard-coding volatile facts such as current price or stock status unless a deliberate reliable synchronization mechanism exists.
- Do not introduce unsupported promotional, quality, safety, performance, or superiority claims.
- Third-party Products must not be represented as Mariwork-branded products.
- Meta descriptions may be written manually or generated programmatically from verified page-specific Product data. Programmatic output must remain human-readable, accurate, and meaningfully page-specific.
- Do not reconstruct or restore historical Yoast descriptions merely because they previously existed.
- Google may generate the search snippet from visible page content instead of the meta description; the meta description is an eligible descriptive source, not a guaranteed SERP snippet.
- Final per-Product meta copy remains subject to the existing content-approval gate before Production.


## DEC-016 — Shop Metadata Strategy
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** SHOP / METADATA

### Accepted target state

`/shop/` uses explicit, Shop-specific Rank Math metadata rather than generic archive/excerpt templates.

Approved SEO title from DEC-003:

`فروشگاه ماری‌ورک | رنگ پارچه، مدیوم، ست و ابزار`

Approved meta description:

`فروشگاه ماری‌ورک؛ خرید رنگ پارچه، مدیوم‌ها، ست‌های رنگ و ابزارهای مرتبط برای نقاشی و چاپ روی پارچه.`

Rules:
- Shop metadata must be explicitly defined for the Shop landing page.
- Do not derive the Shop meta description from a generic archive template, `%excerpt%`, or strings such as `محصولات Archive`.
- Preserve the DEC-003 Shop SEO title as the explicit target.
- The meta description should summarize the Shop's broad commercial-discovery role.
- Do not stuff category lists or repetitive keywords into the description.
- Do not hard-code volatile product counts, prices, discounts, or stock state.
- Update Shop metadata only when the actual Shop role/product scope materially changes.
- Google may generate a different search snippet from visible page content.
- Product Category metadata is governed separately.


## DEC-017 — Static / Core Meta Description Strategy
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** STATIC / CORE / META DESCRIPTION

### Accepted target state

Important Static/Core pages use explicit, page-specific meta descriptions rather than generic templates or raw excerpts.

Rules:
- Write a dedicated meta description for each important Static/Core page.
- The description must accurately summarize that page's actual role and visible content.
- Do not rely on generic phrases, shared templates, or `%excerpt%`.
- Avoid keyword stuffing and unsupported brand/product claims.
- Meta descriptions do not need to repeat the SEO title or H1 verbatim.
- Do not impose a fixed 150/160-character rule; prioritize concise and sufficiently descriptive copy.
- Google may generate the search snippet from visible page content instead of the supplied meta description.
- Final copy must remain factually aligned with the final visible page content and any canonical brand facts governed by DEC-053.

Initial page-specific direction:
- About: describe Mariwork's story, activity and product focus.
- Contact: describe available contact/support purposes.
- Magazine: describe the editorial/educational content scope.
- Why Mariwork: describe the page's explanation of Mariwork fabric-paint features/use cases.
- Stores: describe discovery of physical points of sale.
- FAQ: describe answers to common Product and educational questions.


## DEC-018 — Article Meta Description Update Rule
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** EDITORIAL / ARTICLE META DESCRIPTION

### Accepted target state

Existing Article meta descriptions must not be rewritten mechanically merely because they are old.

Each Article meta is classified as:

- `KEEP` — accurate, useful, page-specific and aligned with the Article.
- `SHORTEN / REFINE` — factually sound but unnecessarily verbose, unfocused, or introduction-like.
- `REWRITE` — materially weak, generic, duplicated, misleading, or insufficiently descriptive.
- `FACT-CHECK REQUIRED` — contains factual, historical, scientific, safety, technical, or other claims that require validation before retention or rewriting.

Rules:
- Preserve existing meta descriptions when already accurate and useful.
- Do not perform a blanket Article-meta rewrite.
- Each Article should have meaningfully page-specific metadata.
- Duplicate descriptions across distinct Articles should be resolved.
- Very short descriptions that fail to explain the Article should be rewritten.
- Long descriptions are not rejected by character count alone; refine them when they function as copied introduction paragraphs rather than concise summaries.
- Do not impose a fixed 150/160-character limit.
- Meta descriptions should summarize the Article rather than mechanically copy its first paragraph.
- Avoid keyword stuffing, unsupported claims, and exaggerated promotional language.
- Claims that require substantive source verification are escalated to DEC-023.
- DEC-018 governs metadata only; it does not authorize substantive Article-content changes.
- Article overlap/cannibalization remains governed separately by DEC-119.


## DEC-019 — Academy Course / Lesson Meta Description Rule
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** ACADEMY / META DESCRIPTION

### Accepted target state

Academy Course and Lesson meta descriptions must be page-specific rather than generated from a shared generic family template.

Course metadata should summarize the educational scope and purpose of the Course.

Lesson metadata should clearly describe the specific technique, task, concept, or learning outcome covered by that Lesson.

Classify existing metadata as:
- `KEEP` — accurate and genuinely page-specific.
- `REFINE` — accurate but insufficiently focused or descriptive.
- `REWRITE` — duplicated, mismatched, generic, misleading, or otherwise not representative of the Lesson.
- `FACT-CHECK REQUIRED` — contains technical, durability, safety, compatibility, performance, or other claims that require verification.

Rules:
- Do not use a shared Academy family description or raw `%excerpt%` as the final metadata strategy.
- Each Lesson description must reflect that specific Lesson.
- Duplicate metadata across distinct Lessons should be resolved.
- Mismatched metadata must be rewritten.
- Include Mariwork branding only where genuinely relevant to the educational subject.
- Do not mechanically inject `رنگ پارچه`, brand terms, or SEO keywords.
- Do not impose a fixed 150/160-character limit.
- Do not mechanically copy a transcript or the first content paragraph.
- Factual technical/safety/performance claims require verification before final approval.
- DEC-019 governs metadata only; Academy visible-content standards remain DEC-024 and video/schema concerns remain separate.


## DEC-020 — Product-Page Visible Content Architecture
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** PRODUCT / VISIBLE CONTENT

### Accepted target state

Mariwork Product pages use a people-first, family-specific content architecture. A shared family structure is allowed; mass-produced filler copy is not.

Common Product core:
- concise Product identity;
- verified specifications;
- applicable variants;
- primary purpose/use;
- necessary usage or handling guidance;
- material limitations/warnings where relevant;
- useful contextual links.

Family-specific priorities:
- Fabric colors: verified color identity, applicable surfaces/techniques, relevant variant/volume guidance, and verified preparation/fixation/washing guidance.
- Mediums/additives: what the Product does, when/how it is used, verified usage conditions/ratios where available, compatibility and limitations.
- Sets/bundles: bundle identity, current component composition, count/volume facts, intended use and meaningful differentiation. Current Woo/YITH data is the canonical component source. Naming remains DEC-008.
- Tools/accessories: exact tool identity, factual specifications, intended use, compatibility and necessary usage instructions. Third-party products must not be represented as Mariwork-manufactured/branded without factual support.

General rules:
- No fixed word-count target.
- Do not add long SEO copy merely to increase page length.
- Family templates define information structure, not mandatory duplicated prose.
- Avoid generic background/history unless directly useful to the purchaser.
- FAQ is optional and only where genuine Product-specific questions warrant it.
- Contextual links must be genuinely relevant.
- Do not repeat benefits/summaries/keywords across sections solely for SEO.
- Performance, durability, safety, compatibility, suitability, economy and usage claims require factual support before family-wide publication.
- AI-assisted Product copy requires review for accuracy, relevance, duplication and unsupported claims.
- Visible Product content and structured data must describe the same actual purchasable Product/variants.
- This Decision does not define exact copy or visual layout.


## DEC-021 — Product Category Visible Intro / Content Policy
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** PRODUCT CATEGORY / VISIBLE CONTENT

### Accepted target state

Durable Product Category pages are primarily commercial discovery and product-selection pages, not long-form editorial articles.

Target structure:
- Provide a concise, useful visible introduction explaining what the category contains and the meaningful basis for choosing among its products.
- Keep the Product listing/grid as the primary page function.
- Add supplementary selection guidance only where it provides genuine user value.

Rules:
- Do not target a fixed word count.
- Do not add long SEO copy merely to increase page length.
- Category content should help users understand the category and choose among its products.
- Do not duplicate Product-page descriptions across the Category.
- Do not duplicate long-form educational content that belongs in Magazine or Academy.
- FAQ content is optional, not a mandatory Category module.
- Avoid keyword stuffing, repetitive commercial phrases and boilerplate.
- Child Categories such as 30/60/250 ml Sets must have genuinely distinct explanatory value if retained as durable landing pages; do not create near-identical copy with only the volume token changed.
- Product-category content must reflect actual current inventory and factual Product distinctions.
- Third-party tools/accessories must not be described as Mariwork-manufactured merely because they appear in a Mariwork category.
- Future semantic/value pillars from DEC-121–124 may inform Category emphasis, but must not create artificial or duplicated content.
- Metadata remains governed by DEC-076; title/H1 by DEC-115; durable Category/indexability decisions by DEC-025.


### DEC-019 amendment reopened — 2026-09-25

Owner clarification materially changes the Academy metadata policy:

- Every current Academy Lesson contains a video; there are no text-only Lessons in the Academy.
- Academy must be treated as video-first practical/instructional content.
- Magazine must remain text-first explanatory/reference/editorial content.
- The revised DEC-019 must decide how video format is explicitly communicated in SEO title, meta description, and/or visible page context.
- Unique metadata must describe the specific Lesson/video.
- Metadata alone is not sufficient to resolve Academy↔Magazine overlap; visible-content differentiation is governed by DEC-024 and overlap/cannibalization policy by DEC-119.
- The previously accepted DEC-019 wording is not the current final target until this amendment is approved by the owner.


## DEC-014 Amendment — Video-First Academy Titles
**Status:** Accepted  
**Date:** 2026-09-25  
**Supersedes:** the prior DEC-014 default equality between Lesson H1 and Lesson SEO title where video-format differentiation is needed.

### Accepted amended target state

Mariwork Academy is video-first.

Course:
- Visible H1 remains the natural Course name.
- SEO `<title>` should explicitly communicate the video format where useful.
- Current Course target example: `راهنماهای یک دقیقه‌ای ماری‌ورک | آموزش‌های ویدیویی`.

Lesson:
- Visible H1 remains the natural instructional title.
- Default Lesson SEO title pattern: `[Lesson H1] | آموزش ویدیویی`.
- Example: H1 `چاپ سیلک اسکرین`; SEO title `چاپ سیلک اسکرین | آموزش ویدیویی`.

Rules:
- Do not append the old repetitive `- رنگ پارچه ماری ورک` suffix.
- The `آموزش ویدیویی` qualifier is an Academy identity/search-intent signal, not a requirement imposed by Google.
- Include `ماری‌ورک` only when it naturally belongs to the subject or Course identity.
- Preserve numeric sequence only for genuine multi-part instructional sequences.
- Existing clear natural H1s should be retained.
- Title normalization must not trigger URL/slug changes.
- Video/schema names should remain semantically consistent with the approved visible Lesson identity; schema ownership/eligibility remains governed by DEC-037 and DEC-038.


## DEC-019 — Academy Video-First Meta Description Rule — Final Amendment
**Status:** Accepted  
**Date:** 2026-09-25  
**Supersedes:** the reopened/pre-amendment DEC-019 wording.

### Accepted target state

Every current Mariwork Academy Lesson contains a primary video. Academy is therefore a **video-first practical/instructional content family**.

Magazine remains a **text-first explanatory/reference/editorial content family**.

Course metadata:
- Must be page-specific.
- Must summarize the educational scope/purpose of the Course.
- Should communicate the video-led nature of the Course when relevant.

Lesson metadata:
- Must be page-specific.
- Should explicitly communicate that the page is a video lesson.
- Must describe the specific technique, task, concept, demonstration, or learning outcome covered by that Lesson.
- Must not reuse metadata from unrelated Lessons.

Existing metadata classification:
- `KEEP` — accurate, page-specific, and already communicates the Lesson correctly.
- `REFINE` — accurate but insufficiently focused or insufficiently clear about the video/lesson purpose.
- `REWRITE` — duplicated, mismatched, generic, misleading, or not representative of the Lesson/video.
- `FACT-CHECK REQUIRED` — contains technical, durability, safety, compatibility, performance, or other claims needing verification.

Academy↔Magazine boundary:
- Academy = practical/demo/video-first intent: users primarily come to watch how something is done.
- Magazine = explanatory/reference/text-first intent: users primarily come to read and understand the topic.
- A topic may exist in both families only when the user intent and page content are materially differentiated.
- Metadata wording alone does not solve substantial same-intent/same-content overlap.
- DEC-024 governs visible Academy supporting content and must preserve the video-first role.
- DEC-119 governs overlap/cannibalization, differentiation, merge, and redirect decisions.

Additional rules:
- Visible context near the primary video should make the video format clear (for example, `آموزش ویدیویی`).
- Do not use raw `%excerpt%` or a shared generic Academy description as the final strategy.
- Do not mechanically inject `رنگ پارچه`, Mariwork branding, or other SEO keywords.
- Do not impose a fixed 150/160-character limit.
- Do not mechanically copy transcripts or first paragraphs into metadata.
- Google may generate snippets from visible page content; supplied meta descriptions are not guaranteed SERP snippets.


## DEC-022 — Static / Trust Page Visible Content Policy
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** STATIC / TRUST / VISIBLE CONTENT

### Accepted target state

Static/Trust pages remain purpose-specific, people-first support and trust entities. They must not be expanded with generic SEO copy merely to increase page length or keyword coverage.

**About**
- Answers: “Who is Mariwork?”
- Contains verified brand history, identity, people, activity scope, experience, and relevant organization background.
- Brand-history and experience claims require factual verification.
- Must not become a duplicate commercial or educational landing page.

**Why Mariwork**
- Answers: “Why should a user consider Mariwork and its products?”
- Focuses on verified, user-relevant differentiators and Product/brand characteristics.
- Unsupported superiority, safety, quality, durability, or performance claims are prohibited.
- Deep educational explanations belong in Magazine; practical demonstrations belong in Academy.

**Contact**
- Answers: “How can I contact Mariwork?”
- Contains actionable, verified contact/support information.
- Do not add unrelated editorial SEO copy.

**Stores**
- Answers: “Where can I purchase Mariwork products in person?”
- Contains verified store/location identity, address, contact and operating information where available.
- Do not create location-keyword filler, invented local claims, or unsupported inventory promises.

**FAQ**
- Provides concise answers to genuine recurring user questions.
- Functions partly as a routing/support layer.
- Detailed practical/how-to content should route to Academy video lessons.
- Detailed explanatory/reference content should route to Magazine.
- Product-specific commercial detail should route to the relevant Product/Category where appropriate.
- Do not create artificial keyword-driven questions or duplicate full Academy/Magazine content.

**Cross-family rules**
- Static/Trust pages preserve distinct user purpose.
- No fixed word-count target applies.
- Avoid duplicated content across Static, Magazine, Academy and Commerce families.
- Exact factual claims remain subject to DEC-053.
- FAQ content is created for user support, not for pursuing FAQ rich results.


## DEC-018 Amendment — Article Fact-Check Requirement Closed
**Status:** Accepted  
**Date:** 2026-09-25

The owner confirmed that the current Article fact-check work has already been completed. Therefore Article meta-description handling no longer includes a remaining `FACT-CHECK REQUIRED` state.

Current Article meta classifications are:
- `KEEP`
- `SHORTEN / REFINE`
- `REWRITE`

All other DEC-018 rules remain unchanged.


## DEC-023 — Article Update / Freshness Policy
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** MAGAZINE / ARTICLE CONTENT MAINTENANCE

### Accepted target state

Current Article fact-check has already been completed and is not a remaining workstream under this Decision.

Article age alone is not a reason to update or rewrite content.

Classify existing Articles as:
- `KEEP / CURRENT` — still accurate, useful, sufficiently complete, and aligned with the intended informational/reference role.
- `TARGETED UPDATE` — a specific section, example, source, fact, or recommendation has become outdated or incomplete.
- `SUBSTANTIVE UPDATE / REWRITE` — material portions no longer adequately serve the intended user need.
- `OVERLAP REVIEW` — the primary issue is same-intent/content overlap rather than freshness; governed by DEC-119.

Rules:
- Do not rewrite Articles merely because they are old.
- Do not change publication/update dates merely to create an appearance of freshness.
- Trigger review when information materially changes, examples or sources become obsolete, a factual error is discovered, relevant Product/method context changes, or the Article materially fails its intended user need.
- Prefer targeted correction over unnecessary full-Article rewrites.
- Preserve the original `datePublished`.
- `dateModified` must reflect a real content modification and must not be manipulated for SEO freshness.
- Visible “updated” treatment should correspond to meaningful content change rather than trivial editorial edits.
- Magazine remains text-first explanatory/reference content; practical video demonstrations should route to Academy rather than be duplicated.
- Meta-description handling remains governed by DEC-018.
- Author/reviewer/source presentation remains governed by DEC-085.
- Content overlap/cannibalization remains governed by DEC-119.
- Detailed body-content review of each individual Article is an implementation-stage content QA task after strategy approval, constrained by DEC-013, DEC-018, DEC-023, DEC-044, DEC-045, DEC-049, DEC-050, DEC-085, DEC-119 and DEC-123. It does not require a new strategy Decision unless a new material policy choice emerges.


## DEC-024 — Academy Course / Lesson Visible Content Standard
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** ACADEMY / COURSE / LESSON / VISIBLE CONTENT

### Accepted target state

Mariwork Academy is a video-first practical/instructional content family.

### Lesson pages

Each published Lesson containing its primary instructional video functions as a dedicated video watch page.

Required content principles:
- The natural Lesson H1 identifies the instructional subject.
- Visible context clearly identifies the content as a video lesson.
- The primary video remains the dominant/main content of the page and is readily accessible without unrelated content obscuring it.
- Include a concise, Lesson-specific introduction explaining what the user will see or learn.
- Supporting text adds practical user value rather than turning the Lesson into a duplicate long-form Article.

Optional supporting modules, only where genuinely useful:
- materials/tools used;
- preparation requirements;
- key execution steps;
- important practical notes or warnings;
- products/tools genuinely used in the demonstration;
- relevant next Lesson or deeper reference content.

No module is mandatory merely to satisfy an SEO template.

### Transcript policy

Full transcripts are optional, not mandatory for every Lesson.

Default to concise summaries and useful practical notes for short video lessons.

A full or substantial transcript may be provided when it materially improves accessibility, comprehension, or preservation of important spoken instructional information.

Do not generate transcripts merely to increase text volume or keyword coverage.

### Academy ↔ Magazine boundary

Academy owns practical/demo/video-first intent: “show me how this is done.”

Magazine owns explanatory/reference/text-first intent: “explain what this is, why it matters, its types, context, comparisons, or deeper theory.”

Supporting Lesson text must not reproduce a long-form Magazine Article on the same topic.

Where both families cover the same subject:
- Academy focuses on execution/demonstration;
- Magazine focuses on explanation/reference depth;
- they may contextually link to each other where useful.

Substantial same-intent/same-content overlap remains governed by DEC-119.

### Course page

The Course page functions as an educational hub, not as a watch page or long-form Article.

It should:
- explain the Course scope concisely;
- make its video-learning format clear;
- organize and expose its Lessons clearly;
- help users move from the Course overview to the appropriate video Lesson.

Do not add long generic SEO content merely to increase page length.

### Cross-decision boundaries

- Lesson title/H1 and video-format title signaling: DEC-014.
- Course/Lesson meta descriptions: DEC-019.
- Video structured data/indexability: DEC-038 and related schema decisions.
- Academy→Product/internal-link rules: dedicated internal-link Decisions.
- Academy↔Magazine overlap/cannibalization: DEC-119.
- Exact visual layout remains an implementation/design concern rather than a strategy requirement.


## DEC-025 — Durable Product Category Set and Index / Sitemap Policy
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** PRODUCT CATEGORY / INDEXABILITY / SITEMAP / LIFECYCLE

### Accepted target state

Mariwork maintains a selective set of durable WooCommerce Product Category landing pages.

Approved durable Product Categories:

Top-level:
- `TERM-product_cat-1902` — Fabric Colors
- `TERM-product_cat-28` — Mediums / Glitters
- `TERM-product_cat-82` — Fabric Color Sets
- `TERM-product_cat-220` — Tools / Accessories

Child Set categories:
- `TERM-product_cat-1991` — 30 ml Sets
- `TERM-product_cat-1992` — 60 ml Sets
- `TERM-product_cat-1993` — 250 ml Sets

Target state for durable categories:
- HTTP 200;
- `index,follow`;
- self-canonical;
- included in the Product Category XML sitemap;
- reachable through durable crawlable internal navigation;
- retain a genuine commercial browse/product-selection role.

A parent Category does not require directly assigned Products when it provides a genuine hierarchy/hub role through useful child Categories.

Low Product count alone does not disqualify a Category, but a thin keyword-variant page without genuine browse value is not durable.

### Migration-era categories

- `TERM-product_cat-20` — historical 60 ml Fabric Colors
- `TERM-product_cat-27` — historical 250 ml Fabric Colors

These are not durable search landing pages.

Accepted lifecycle:
1. remove them from the durable SEO architecture, navigation and sitemap target set;
2. preserve historical/migration evidence;
3. consolidate/redirect their historical URLs to the verified main Fabric Colors Category;
4. after redirect/disposition is in place and operational dependency checks pass, delete the obsolete WooCommerce category terms themselves.

Do not delete first and decide URL disposition afterward.

`pa_volume` is a separate taxonomy and is governed by DEC-026.

Product Category visible-content policy remains governed by DEC-021; metadata by DEC-076; title/H1 by DEC-115.


## DEC-026 — pa_volume Archive Role, Indexability and Sitemap Policy
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** PRODUCT ATTRIBUTE / VOLUME / INDEXABILITY / SITEMAP

### Accepted target state

The current `pa_volume` terms `30ml`, `60ml`, and `250ml` are durable cross-family commercial browse landing pages.

Their role is to let users browse Products that are genuinely purchasable in a specific volume across applicable Product families.

Approved terms:
- `TERM-pa_volume-1906` — 30 ml
- `TERM-pa_volume-1907` — 60 ml
- `TERM-pa_volume-1908` — 250 ml

Target state:
- HTTP 200;
- `index,follow`;
- self-canonical;
- included in the appropriate XML sitemap;
- reachable through deliberate crawlable navigation/internal links;
- Product listings reflect actual current volume availability.

The `pa_volume` landing pages are distinct from volume-specific Set Product Categories.

Shop parameter states such as `?filter_volume=30ml` remain functional faceted/filter URLs and are not independent search landing pages.

Where technically reliable, Product links from a volume landing page should preserve/preselect the relevant WooCommerce volume variation.

Low relative Product count alone does not disqualify the 250 ml page while it retains genuine distinct browse value.

Title/H1 policy is governed by DEC-116; visible landing content by DEC-117; parameter/facet handling remains separate.


## DEC-027 — Product Tags Decommission and Historical URL Mapping Policy
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** PRODUCT TAG / DECOMMISSION / REDIRECT / REMOVAL

### Accepted target state

The current WooCommerce Product Tag family is not part of Mariwork's durable SEO, navigation, or Product-discovery architecture.

Current evidence shows 275 Product Tag terms with zero Product assignments.

All current Product Tag terms are approved for controlled decommission and deletion.

Rules:
- Do not optimize, index, content-expand, or include Product Tag archives in XML sitemaps.
- Do not use Product Tags as a future Mariwork SEO/navigation landing-page system.
- Preserve relevant historical Search/backlink/migration evidence before term deletion.
- Establish URL disposition before deleting terms where historical URLs matter.

### Redirect rule

Use a permanent redirect only when a genuine semantic successor or equivalent destination exists.

A valid destination may be:
- a Product;
- a Product Category;
- an Academy Lesson;
- a Magazine Article;
- a Static/support page;
- or another durable page that genuinely replaces the retired tag's meaning.

Do not infer mappings from keyword or slug similarity alone.

Do not mass-redirect retired tags to the Homepage, Shop, or a broad unrelated Category merely to avoid 404 responses.

### No-replacement rule

When no meaningful replacement exists, the retired URL should return a proper HTTP `404` or `410`.

Google accepts both for content that has been removed without a replacement. Mariwork does not require a special SEO preference between them; standard 404 is the default implementation unless a deliberate 410 is operationally useful.

### Execution order

1. freeze/export the Product Tag term + URL inventory;
2. preserve relevant historical evidence;
3. create only verified semantic redirect mappings;
4. remove remaining internal references;
5. establish approved redirects independently of term existence;
6. delete obsolete Product Tag terms;
7. allow unmapped retired URLs to return proper 404/410;
8. run crawl/regression QA for redirect chains, soft 404s, sitemap leakage and internal-link remnants.

The underlying WooCommerce `product_tag` capability does not need to be removed from WooCommerce core; it may remain unused.

Blog Tags remain a separate lifecycle domain because they still have assigned Article relationships.


## DEC-027 Amendment — Commerce-Only Redirect Destinations
**Status:** Accepted  
**Date:** 2026-09-25

The owner narrowed the Product Tag redirect policy.

Historical Product Tag URLs may redirect only to a genuine semantic successor within Mariwork's commerce/store architecture.

Allowed destination classes:
- Product;
- Product Category;
- approved `pa_volume` landing page;
- Shop only in exceptional cases where it is genuinely the closest valid commercial replacement.

Disallowed destination classes for Product Tag migration:
- Magazine Article;
- Academy Course/Lesson;
- Static/support pages;
- Homepage;
- unrelated broad destinations.

All prior DEC-027 rules remain unchanged:
- no mapping by slug/keyword similarity;
- no mass redirects;
- no-replacement URLs return proper 404/410;
- standard 404 remains the default unless deliberate 410 is operationally useful;
- preserve historical evidence before deletion;
- perform redirect/internal-link/sitemap regression QA.


## DEC-028 — Blog Category Lifecycle Policy
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** MAGAZINE / BLOG CATEGORY / ARTISTS MIGRATION / LIFECYCLE

### Durable Magazine categories

The following remain durable editorial hubs:
- `TERM-category-71` — Educational Articles
- `TERM-category-142` — History

Their detailed presentation/content treatment remains governed separately.

### Artists migration exception

`TERM-category-18` — Artists is not an ordinary empty-category cleanup target.

A new Artists project is in development and is expected to become public shortly.

Once the new Artists system is public and stable:
- if a historical Artist entity can be confidently identity-matched to a new Artist profile, redirect the old Artist URL one-to-one to that new profile;
- if a historical Artist entity has no matching profile in the new system, redirect that historical Artist URL to the main new Artists landing page;
- the old Artists category/archive should consolidate to the main new Artists landing page;
- do not redirect Artist URLs to draft, private, or otherwise non-public targets.

Identity matching must be based on actual Artist identity, not slug similarity alone.

### Other empty Blog Categories

All other empty Blog Categories are approved for controlled deletion, including current empty Education/video, Cultural, Guides, Literature, Uncategorized variants, Free, General, Paid, and other empty non-Artist terms.

For each retired category URL:
- redirect only when a genuine semantic successor exists;
- otherwise return a proper 404;
- do not retain empty categories merely as SEO placeholders.

Preserve relevant migration evidence before deletion and remove obsolete internal references.


## DEC-029 — Blog Tags Decommission and Mapping Policy
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** MAGAZINE / BLOG TAG / DECOMMISSION / URL DISPOSITION

### Accepted target state

Blog Tags are not part of Mariwork's durable editorial SEO, navigation, or information architecture.

Current evidence shows 54 Blog Tag terms. Six currently have assignments, representing 39 Article↔Tag relationships.

All 54 current Blog Tag terms are approved for full controlled deletion.

Rules:
- remove all current Article↔Tag assignments before or together with term deletion;
- Article content and durable Blog Category membership remain unaffected;
- do not optimize, index, content-expand, expose in navigation, or include Blog Tag archives in XML sitemaps;
- do not recreate Blog Tags as SEO landing pages.

### Historical URL disposition

Use a permanent redirect only when a genuine editorial successor exists.

Allowed destination classes:
- durable Magazine Category;
- specific Magazine Article;
- another durable Magazine editorial hub when genuinely equivalent.

Do not redirect Blog Tag URLs to Store/Product destinations merely because the same keyword appears there.

Do not infer mappings from tag name or slug similarity alone.

When no meaningful editorial replacement exists, return a proper HTTP `404` or `410`; standard 404 is the default implementation.

### Execution order

1. freeze/export the Blog Tag term + URL + assignment inventory;
2. preserve relevant historical evidence;
3. verify durable Category ownership for affected Articles;
4. remove all 39 current Article↔Tag assignments;
5. establish only verified semantic redirects;
6. delete all 54 Blog Tag terms;
7. allow unmapped retired URLs to return proper 404/410;
8. verify no Tag sitemap, navigation, internal-link remnants, redirect chains, or soft 404s remain.


## DEC-030 — Sitewide Sitemap Membership Policy
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** SITEWIDE / XML SITEMAP / INDEXABILITY / CANONICAL

### Accepted target state

Mariwork XML sitemaps must represent the site's approved canonical Search architecture, not every URL generated by WordPress, WooCommerce, LearnDash, filters, taxonomies, or legacy systems.

Include only canonical URLs intentionally eligible and intended for Search:
- Homepage;
- Shop;
- indexable Products;
- durable Product Categories under DEC-025;
- approved `pa_volume` landing pages under DEC-026;
- durable indexable Static/Trust pages;
- Magazine Articles;
- durable Blog Categories;
- public/indexable Academy Course and Lessons;
- future public/indexable Artists hub and Artist profiles after the new Artists system is launched and stable.

Exclude:
- noindex utility/account/transactional pages;
- Product Tags;
- Blog Tags;
- retired/empty taxonomies;
- deprecated Product Categories;
- empty LearnDash categories;
- internal search URLs;
- faceted/filter/sort/display parameters;
- Product variation-selection query URLs;
- paginated archive URLs;
- redirects;
- 404/410 URLs;
- legacy URLs;
- non-canonical duplicates;
- draft/private/non-public content.

Sitemap membership follows approved indexability/canonical policy for each family and must never be used as a reason to make a URL indexable.

`<lastmod>` should reflect meaningful page changes rather than artificial freshness.

### Sitemap QA gate

Sitemap correctness is a dedicated implementation/release gate.

After each sitemap-affecting rollout, verify every emitted URL for:
- expected family membership;
- HTTP 200;
- intended indexability;
- self-consistent canonical;
- no redirect;
- no 404/410;
- no retired/decommissioned entity;
- no utility/filter/parameter leakage;
- no draft/private URL leakage.

Also verify that every approved durable sitemap family is actually represented.

Artists URLs enter sitemap only after the new Artists system is public/stable; historical Artist URLs that redirect must not remain in sitemap output.


## DEC-031 — Attachment / Media Public and Index Policy
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** MEDIA / ATTACHMENT URLS / INDEXABILITY / CLEANUP SAFETY

### Accepted target state

WordPress Attachment HTML pages are not part of Mariwork's durable Search landing-page architecture.

Media asset files and Attachment HTML pages are separate concerns.

#### Media files
- Public image/media asset URLs used by durable public content remain accessible and crawlable where required for page rendering, Google Images, and structured-data image references.
- Do not block useful `/wp-content/uploads/` assets merely to suppress Attachment HTML pages.

#### Attachment HTML pages
- are not independent SEO landing pages;
- must not be intentionally indexed;
- must not be included in XML sitemaps;
- do not receive standalone SEO-content expansion;
- do not become navigation/hub entities.

#### Disposition hierarchy
1. If an attachment has a clear durable owning page, permanently redirect the Attachment HTML URL to that canonical page.
2. If no single semantic owner exists but the media asset remains valid/public, the Attachment HTML URL may redirect to the actual media-file URL when technically reliable.
3. If neither a meaningful owner nor a retained valid asset exists, return proper 404/410.
4. Never mass-redirect Attachment pages to Homepage or unrelated destinations.

This Decision does not authorize deleting Media Library records or physical media files.

### Operational follow-up — unused/orphan media cleanup

Mariwork has a large historical Media Library and the owner explicitly requires a later cleanup pass for media assets no longer used anywhere on the site.

This cleanup is operational maintenance rather than a direct ranking-policy decision, but it is a required follow-up to DEC-031.

Before deleting any media record or physical file, prove that the asset is not referenced by:
- post/page body content or block data;
- Product featured images or Product galleries;
- Academy Course/Lesson content;
- taxonomy or Static/Trust content;
- featured-image relationships;
- structured data or SEO/social metadata;
- CSS, JS, theme, child-theme, plugin, shortcode or custom-field references;
- reusable blocks/patterns/templates;
- other runtime or migration dependencies.

Deletion must be inventory-driven, backup/rollback-capable, and batch/canary verified. Filename presence or apparent non-use in rendered HTML alone is insufficient proof of orphan status.

Current evidence reports 626 returned attachment IDs versus 845 advertised records. This discrepancy must be reconciled before any bulk media deletion or bulk attachment-URL change.

Detailed image naming, ALT/context, image discovery/sitemap, duplicate/reuse policy and technical delivery remain governed by the dedicated image Decisions.


## DEC-032 — Homepage Organization / WebSite / WebPage Schema Target
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** HOMEPAGE / STRUCTURED DATA / ENTITY GRAPH / OWNERSHIP

### Accepted target state

The Mariwork Homepage should expose one coherent primary entity graph rather than accumulating independent or duplicate schema emitters.

Retain:
- `Organization` — Mariwork as the brand/business entity;
- `WebSite` — `mariwork.ir` as the website entity;
- `WebPage` — the Homepage document.

Use `ImageObject` only where it represents a real image/logo entity referenced by the graph.

Do not classify the Homepage as `Article`.

### Organization

The Homepage is the primary Organization structured-data location.

Organization properties must use verified factual data only, including applicable name, canonical URL, logo, contact details and verified official `sameAs` identities.

Do not invent properties merely to increase schema completeness.

Use a more specific Organization subtype only when it accurately represents Mariwork's real business/entity model; do not force an ecommerce subtype solely because the site sells Products.

### WebSite / SearchAction

Retain a single authoritative `WebSite` entity for `mariwork.ir`.

Remove the current `SearchAction` markup as routine cleanup. Google's sitelinks search box feature is retired; this removal is schema simplification, not a ranking intervention.

### Ownership

Rank Math remains the primary Homepage JSON-LD/schema owner where supported.

Do not introduce a second independent Organization/WebSite/WebPage JSON-LD emitter.

Existing theme microdata should be checked for factual/conflict consistency during implementation; do not remove harmless semantic markup merely for deduplication aesthetics.

All Homepage schema changes require rendered-output validation after implementation.


## DEC-008 — Product Title Naming Standard — Sets / Bundles
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** PRODUCT / SET / BUNDLE / TITLE / H1

### Accepted target state

Set/Bundle visible Product titles and H1s should express the concise purchasable identity of the Set.

Rules:
- include the genuine Set/Bundle identity;
- include count/type when it materially identifies the Set;
- include volume when it materially distinguishes the Set identity;
- use `ماری ورک` only for genuinely Mariwork-branded Sets;
- do not force a Product code unless a real stable code exists;
- long composition strings such as `شامل ...` belong in visible Product content, not the primary title/H1;
- do not use decorative separator-heavy title construction;
- normalize digit/separator treatment consistently;
- title normalization must not trigger URL/slug changes.

Examples of the intended direction:
- concise identities such as a 5-color fluorescent Set, a 24-color Set, a complete colors-and-mediums Set, or a glitter Set may retain the identifying count/type and applicable volume;
- detailed component lists belong in the Product body and must be reconciled against current YITH/Woo bundle composition evidence.

Exact per-Set wording is finalized during implementation/content QA from current factual YITH/Woo data.

SEO `<title>` relationship remains governed by DEC-011.

### DEC-011 dependency update

DEC-008 is no longer deferred. The DEC-011 Product title-template rollout is no longer blocked by DEC-008; it remains subject to normal implementation QA and the other accepted Product naming decisions.


## DEC-033 — Static/Core WordPress Page Schema Policy
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** STATIC / CORE PAGES / STRUCTURED DATA / SCHEMA OWNERSHIP

### Accepted target state

The generic WordPress `page` post type must not automatically receive `Article` structured data.

Structured data must reflect the actual role of each page rather than its CMS post type.

Target:
- About → `WebPage`
- Contact → `WebPage`
- Why Mariwork → `WebPage`
- Stores → `WebPage`, with store/local entity treatment governed separately
- FAQ → `WebPage`, with FAQ-specific schema governed separately by DEC-086
- Login → utility `WebPage`, noindex
- Fast Buy → utility `WebPage`, noindex
- Magazine hub → retain appropriate `CollectionPage`

Remove `Article` and Article-derived author `Person` nodes from generic Static/Core pages unless a page genuinely functions as an article or person/profile entity.

Shared Organization/WebSite references may remain when they use the authoritative site entity IDs; do not emit conflicting duplicate entities per page.

Rank Math remains the primary schema owner where supported.

Roll out with representative canary pages and rendered JSON-LD regression validation before family-wide application.


## DEC-034 — Article Schema Policy
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** MAGAZINE / ARTICLE / STRUCTURED DATA / AUTHORSHIP

### Accepted target state

Mariwork Magazine Articles use `BlogPosting` as the default Article structured-data type.

Do not convert normal Magazine Articles to `NewsArticle`.

Each BlogPosting should use factual page-aligned data:
- `headline` reflecting the approved Article identity;
- a representative crawlable Article image;
- original factual `datePublished`;
- `dateModified` only for real content modifications;
- coherent relationships to the canonical `WebPage`, `WebSite` and authoritative Mariwork `Organization` entity.

### Author and publisher

Current Mariwork Articles do not have individual named authors and are written on behalf of Mariwork.

Therefore:
- `author` must reference the authoritative Mariwork `Organization` entity;
- `publisher` must reference that same authoritative Mariwork `Organization` entity;
- do not fabricate, infer, or retain a default `Person` author merely to satisfy schema;
- remove current Article-derived `Person` author nodes unless a future Article genuinely has an identified individual author;
- if a future Article has a real individual author, that exception may use `Person` when the visible attribution and entity data genuinely support it.

The Mariwork Organization identity must reuse the authoritative site entity rather than creating a separate Organization per Article.

### Ownership and boundaries

Rank Math remains the primary Article schema owner where supported.

Do not introduce a second independent `BlogPosting` emitter.

Do not automatically add FAQ, HowTo, Video or other schema merely because related elements occur inside an Article.

Exact future author/reviewer/source governance remains under DEC-085.

Rendered structured-data validation is required after rollout.


## DEC-035 — Product Variation ProductGroup / Variant Schema Architecture
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** PRODUCT / VARIABLE PRODUCT / STRUCTURED DATA / PRODUCTGROUP / RANK MATH

### Accepted target state

Mariwork variable WooCommerce Products use Google's single-page Product variant architecture.

The canonical parent Product URL represents the single ProductGroup landing page.

Each real purchasable variation is represented as a variant `Product` with its own factual `Offer`.

Volume-based variants use the supported `size` property for package sizes such as `30 ml`, `60 ml`, and `250 ml`, with `variesBy` using `https://schema.org/size`.

Products varying by another supported property use the actual property, such as `color` or `size`; do not force the volume model onto all variable Products.

Each variant must have a distinct direct/preselection URL that resolves to the correct selected variation, price, availability and purchasable state. Variant selector query URLs are not independent canonical Search landing pages; the base Product URL remains the single canonical ProductGroup URL.

Each variant Product carries its own factual Offer data.

Do not use `AggregateOffer` as a substitute for explicit variant representation once the ProductGroup model is deployed.

ProductGroup and variant identities must be stable and unique. Do not fabricate SKU, GTIN or MPN values; identifier governance remains coordinated with DEC-081.

### Rank Math ownership and Free implementation

Rank Math Free remains the primary schema owner.

The project preference is NOT to purchase Rank Math PRO solely for Product variation schema.

Where Rank Math Free does not natively emit the required ProductGroup/variant graph, extend the existing Rank Math JSON-LD output through supported server-side filters.

Implementation requirement:
- mutate, replace or extend the relevant existing Rank Math Product entity inside the existing Rank Math graph;
- do not output a second independent Product/ProductGroup JSON-LD graph;
- do not keep the legacy Product/AggregateOffer representation in parallel when it duplicates or conflicts with the new ProductGroup/variant representation;
- preserve unrelated Rank Math graph entities such as WebSite/Organization/ItemPage as appropriate;
- keep all schema generation server-rendered in the initial HTML where practical.

If a clean single-owner graph cannot be produced through the supported Rank Math filter layer, stop and return for technical review rather than shipping duplicate/conflicting schema or automatically purchasing PRO.

Rank Math PRO is not required solely for this accepted capability.

### Canary / regression gate

Before family rollout:
1. implement one 30/60/250 variable Product canary;
2. implement one 30/60 variable Product canary;
3. separately verify the non-volume variable Product cases.

Validate:
- exactly one intended ProductGroup representation;
- correct number and identity of variant Products;
- supported `variesBy` properties;
- per-variant Offers;
- factual price/currency/availability;
- direct variation preselection;
- parent canonical;
- no duplicate Product/ProductGroup entities or competing JSON-LD scripts;
- no loss of unrelated Rank Math entities;
- Google Rich Results / schema validation output.

Re-run the schema regression suite after Rank Math or WooCommerce updates because filter/output internals may change.


## DEC-036 — Bundle / Set Schema and Visible Component Representation
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** PRODUCT / YITH BUNDLE / SET / STRUCTURED DATA / VISIBLE COMPONENTS / AJAX DISCOVERABILITY

### Accepted target state

Each current Mariwork YITH Bundle/Set is a standalone fixed-volume purchasable `Product` with its own factual `Offer`.

Bundles are not Product variant groups:
- do not use `ProductGroup`;
- do not use `hasVariant`;
- do not use `isVariantOf` for Bundle components.

Current Mariwork Bundles do not have internal volume variants and do not mix volumes:
- a 30 ml Bundle contains the intended 30 ml component variations;
- a 60 ml Bundle contains the intended 60 ml component variations;
- a 250 ml Bundle contains the intended 250 ml component variations.

Bundle volume is an intrinsic Product attribute, not a variation dimension.

### Component source of truth

Current YITH/Woo Bundle composition is the canonical source of truth for:
- component identity;
- component quantity;
- selected component variation/volume.

Visible Bundle content must reconcile with current YITH/Woo data.

Long composition strings such as `شامل ...` belong in visible Product content rather than the primary title/H1, consistent with DEC-008.

Where a component has a durable Product page, the visible component may link contextually to it. Where appropriate, the link may use the accepted direct variation-preselection URL architecture from DEC-035.

Bundle price, currency and availability must represent the actual purchasable Bundle and must not be manually reconstructed from component totals.

### AJAX / crawler discoverability requirement

The existing component-list interaction is currently opened through a button and AJAX and must be audited before implementation acceptance.

Search-visible Bundle component content must not require a user click or other user interaction to become available to crawlers.

Preferred implementation:
- server-render the factual component list in the initial HTML/DOM;
- use the current button/accordion interaction only to visually show/hide that already-present content.

An alternative automatically rendered client-side implementation is acceptable only if the component content appears in rendered DOM without any user action and is reliably retrievable by Google rendering.

If the component list is fetched only after the user clicks the button, refactor the implementation before treating that component content as Search-visible.

Required validation:
- raw HTML inspection;
- rendered DOM inspection before any manual interaction;
- AJAX/network behavior;
- component count/identity/volume reconciliation with YITH;
- Google Search Console URL Inspection rendered output where available;
- Rich Results/rendered structured-data checks where relevant.

Sitewide JavaScript/AJAX crawlability remains additionally governed by DEC-080.

### Schema ownership

Rank Math remains the primary Product schema owner.

Do not add ProductGroup or nested component Product entities solely to model Bundle composition for Google Product structured data.

Representative small, medium and large Bundle canaries are required before family rollout.


## DEC-037 — Academy / LearnDash Schema Ownership and Canary
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** ACADEMY / LEARNDASH / SEMANTIC ROLE / STRUCTURED DATA / UI-SEO CONSISTENCY

### Accepted semantic rule

Academy SEO and structured data must follow the real semantic role presented to users, not the raw LearnDash post type alone.

A LearnDash object may be technically stored as a Course while intentionally functioning as a different content type in the public product experience.

### Current guide collection

The current entity:

- WP-32714 — `راهنماهای یک دقیقه‌ای ماری‌ورک`

is not one coherent curriculum or a single-topic instructional Course.

It is a broad collection of short independent guides around fabric painting, printing and related techniques.

Mariwork already customizes this entity at the product/UI layer:
- Mariwork Core intentionally uses the user-facing concept `راهنما` instead of `درس` for this collection;
- count/summary language is guide-oriented, e.g. `شامل 37 راهنما`;
- CTA/action language is guide-oriented, e.g. `دیدن راهنماها`, not `دیدن درس‌ها`.

SEO/schema must mirror this semantic customization.

Therefore:
- WP-32714 uses collection semantics, targeting `CollectionPage` rather than `Course`;
- its 37 child URLs are individual guide/watch pages;
- those 37 URLs must not be treated as lessons of one coherent curriculum merely because LearnDash stores them under a Course-type object;
- generic Article schema must not be applied to those guide pages.

### Future real Courses

Future Academy entities such as:
- beginner course;
- advanced course;
- doll-painting course;
- other coherent curricula with a defined instructional path;

may use `Course` semantics only when their actual visible structure and content support that meaning.

For a genuine Course:
- UI language should reflect the actual course model;
- count/summary language may use patterns such as `شامل N درس`;
- child units may be represented as lessons/modules when that is the true visible structure;
- Course schema eligibility and Google-specific rich-result eligibility must be checked at launch rather than assumed from LearnDash type alone.

The semantic distinction between Guide Collection and Course must remain consistent across:
- UI labels;
- CTAs;
- count summaries;
- titles/meta where relevant;
- structured data;
- internal linking/hierarchy;
- future breadcrumb behavior.

### Ownership

Rank Math remains the first schema owner where it can produce semantically correct output.

Mariwork Core may fill unsupported Academy-specific nodes or semantics, but must not create a second conflicting graph.

### Canary

Current initial canary:
1. WP-32714 guide collection;
2. one practical guide/watch page;
3. one informational/guidance guide/watch page.

When the first genuine Course launches, it requires a separate Course-specific canary before any Course-family rollout.

Validate:
- semantic role matches visible UI;
- no unwanted Course schema on the current guide collection;
- no unwanted Article/Person schema on guide pages;
- single schema ownership;
- stable canonical/entity relationships;
- Organization/WebSite reuse;
- no duplicate JSON-LD.

VideoObject policy remains under DEC-038.
Breadcrumb policy remains under DEC-039.


## DEC-038 — VideoObject Eligibility / Ownership Policy
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** VIDEO / ACADEMY / GUIDE PAGES / STRUCTURED DATA / WATCH PAGE

### Accepted principle

Video structured data is applied by semantic and technical eligibility, not merely because a page contains a video.

Current Mariwork guide pages whose primary purpose is watching one instructional video are treated as educational watch pages.

The host document remains a `WebPage`. Where eligible, its primary instructional video may be represented as the page's `VideoObject` main entity.

The guide CollectionPage itself must not be represented as one VideoObject.

### Current guide-page content model

Current guide pages already contain:
- a dedicated video cover/poster image;
- visible explanatory text about the guide;
- text that substantially reflects the instructional content of the video while emphasizing selected important points;
- one primary instructional video.

This text is supporting/companion educational content. Its presence does not by itself convert the guide page into an Article.

For pages intended to qualify clearly as watch pages, the target presentation is:
1. descriptive H1;
2. concise introductory/context text;
3. primary video/player prominently near the top, using the stable guide cover/poster;
4. expanded key points, supporting explanation and other useful instructional text after the video.

Do not bury the primary video at the end of a long text block when watching that video is the principal reason for visiting the page.

The text and video may overlap in subject matter, but the text should remain useful supporting context rather than mechanically duplicating a transcript solely for SEO.

### VideoObject eligibility

A VideoObject may be emitted only when factual metadata is available.

Required/critical facts include:
- unique factual `name`;
- stable crawlable `thumbnailUrl`;
- factual `uploadDate`.

Prefer a stable fetchable `contentUrl`. Where unavailable, use a valid `embedUrl` as appropriate.

Add factual:
- `description`;
- `duration`;
- `creator`;

where available.

Do not fabricate upload dates, durations, creator identities, content URLs or embed URLs merely to satisfy validation.

Current dedicated video covers are candidates for `thumbnailUrl`, subject to crawlability, stability and rendered-page verification.

Mariwork-produced videos may reuse the authoritative Mariwork Organization entity as creator.

### Discoverability and rendering

The video/player must be discoverable in Google's rendered HTML without requiring a user click to instantiate the only video representation.

Verify source/player/thumbnail accessibility and whether Google can fetch the relevant resource.

### Other page families

Videos embedded as secondary content on Articles, Products or other non-watch pages remain in the complete sitewide video inventory but are not automatically promoted to watch-page/VideoObject status.

Future video-first lessons in genuine Courses may use the same WebPage + VideoObject model where eligible.

### Ownership

Rank Math remains the first general schema owner where supported.

Mariwork Core may provide unsupported Academy/video-specific structured-data nodes only as part of one coherent graph. Do not create duplicate competing VideoObject/WebPage entities.

### Rollout gate

Before broad VideoObject rollout:
- complete the M-program video inventory and host-page mapping;
- run a two-guide canary;
- verify raw HTML and rendered HTML;
- verify stable cover/thumbnail;
- verify factual uploadDate and duration;
- verify contentUrl/embedUrl and fetchability;
- verify schema validity and duplicate absence;
- inspect the page in Search Console URL Inspection / video indexing where available.

Video sitemap inclusion is limited to verified eligible watch pages and is finalized in the Video SEO implementation workstream.

`Clip` / `SeekToAction` is not a default requirement and is considered only where useful and technically supported.


## DEC-038 — VideoObject Eligibility and Ownership Policy
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** VIDEO SEO / ACADEMY / WATCH PAGES / STRUCTURED DATA

### Accepted policy

Video structured data is applied by semantic and technical eligibility, not merely because a page contains a video.

Current Mariwork guide pages have this visible pattern:
- a cover/thumbnail;
- a short explanatory text section before the video;
- that text summarizes or overlaps the video topic while emphasizing key points;
- the primary instructional video appears lower on the same page.

This structure may still qualify as a video watch/guide page only when the video remains a primary and prominent purpose of the page rather than a minor secondary embed.

The host page keeps `WebPage` semantics. An eligible primary video may be represented as its `mainEntity` `VideoObject`.

### Eligibility/data requirements

Use factual metadata only:
- `name`;
- stable crawlable `thumbnailUrl`;
- factual `uploadDate`;
- prefer stable fetchable `contentUrl`;
- otherwise use a valid `embedUrl`;
- factual `description`;
- factual `duration` where available;
- real creator identity.

Do not fabricate upload dates, duration, creator identity, thumbnail, or source URLs to satisfy validation.

Mariwork-produced videos may reuse the authoritative Mariwork Organization as creator.

The video/player must be discoverable in Google's rendered HTML without requiring a click or other user interaction to create/load the only copy of the video element.

The explanatory text before the video is allowed and can improve page usefulness. QA must nevertheless verify that the video remains prominent enough to represent the page's primary instructional media/purpose.

### Boundaries

- The current guide CollectionPage is not represented as a single VideoObject.
- Future video-first Course lessons may use the same WebPage + VideoObject model when eligible.
- Videos embedded as secondary content on Articles, Products or other non-watch pages remain in the video inventory but are not automatically treated as primary watch-page VideoObjects.
- Clip/SeekToAction is not a default requirement.

### Ownership and rollout

Rank Math remains the first general schema owner.

Mariwork Core may add unsupported Academy/video nodes only as part of one coherent graph, without duplicate VideoObject/WebPage entities.

Before broad rollout:
1. complete the M-program video inventory;
2. run a two-guide canary;
3. verify video prominence and host-page purpose;
4. verify rendered discoverability;
5. verify thumbnail/source fetchability;
6. verify factual uploadDate/duration/creator data;
7. validate rendered structured data;
8. verify Search Console video indexing behavior where available.

Video sitemap inclusion is limited to verified eligible watch pages and is finalized during Video SEO implementation.


## DEC-039 — Breadcrumb Structured-Data Policy Across Store, Academy and Content
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** SITEWIDE / STRUCTURED DATA / INFORMATION ARCHITECTURE

### Accepted target state

- Use breadcrumbs only where a meaningful site hierarchy exists.
- Breadcrumb trails represent the typical user/navigation hierarchy rather than mechanically mirroring URL paths.
- Store hierarchy: Shop → durable Product Category → Product.
- Child Set categories preserve their approved category hierarchy.
- Approved volume landing pages belong under the Store hierarchy; exact volume-page naming remains governed by DEC-116.
- Magazine hierarchy: Magazine → durable primary Blog Category → Article.
- The Article primary category must be real, durable and deliberate rather than a tag or legacy category.
- Current Academy guide hierarchy: Academy → One-Minute Guides collection → individual Guide.
- Current Guide hierarchy must remain aligned with DEC-037 and must not be represented as Course/Lesson.
- Future genuine Course hierarchy: Academy → genuine Course → Lesson.
- Homepage, generic Static/Core pages without meaningful hierarchy, and utility/noindex endpoints do not receive artificial breadcrumbs solely for structured-data coverage.
- Pages with multiple possible parents use one deliberate stable primary hierarchy.
- Visible breadcrumb UI and structured-data hierarchy must agree.
- Duplicate breadcrumb emitters are acceptable only temporarily when they express the exact same factual trail; conflicting duplicate trails must be eliminated and one owner established.

### Consequences

- Validate representative Store, Magazine, Guide Collection/Guide and future Course templates in rendered output and Rich Results testing.
- Product pages with multiple categories require a stable primary commercial hierarchy rather than arbitrary category selection.
- Volume landing-page breadcrumb labels remain dependent on DEC-116.
- Utility/noindex endpoints such as Login, Cart, Checkout, My Account and Fast Buy are not breadcrumb SEO targets.


## DEC-040 — Internal-Link Classification Model
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** SITEWIDE / INTERNAL LINKING / INFORMATION ARCHITECTURE

### Accepted target state

- Internal-link requirements use three classes: CORE/MANDATORY, FAMILY-SPECIFIC and CONTEXTUAL/OPTIONAL.
- CORE/MANDATORY links apply across every relevant entity in a defined family.
- FAMILY-SPECIFIC links apply only to a defined product/content family.
- CONTEXTUAL/OPTIONAL links are used only when genuinely useful to the source-page topic or user task.
- Equivalent pages in the same family must not randomly differ in mandatory-link coverage.
- A missing mandatory link must either be corrected or recorded as an approved documented exception.
- The architecture may be bidirectional where useful: Product/Category → Academy/Article and Academy/Article → relevant Product/Category.
- Commercial links from informational content must remain contextually useful rather than being forced merely to increase link count.

### Consequences

- The Internal Link Requirement Matrix must classify approved relationships using these three classes.
- QA must compare equivalent family members against mandatory-link requirements.
- Exact mandatory parent/hub destinations remain governed by DEC-041.
- Product↔education, Article↔commercial and anchor-text rules remain governed by DEC-042 onward.


## DEC-041 — Mandatory Parent/Hub Links by Family
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** SITEWIDE / INTERNAL LINKING / INFORMATION ARCHITECTURE

### Accepted target state

- Product → stable primary Product Category → Shop.
- Child Product Category → real parent Product Category → Shop.
- Current Guide → One-Minute Guides collection → Academy.
- Future Lesson → genuine Course → Academy.
- Article → stable primary Blog Category → Magazine.
- Multi-parent entities use one deliberate stable primary hierarchy rather than random taxonomy selection.
- The required parent/hub relationship may be supplied through breadcrumb UI, navigation, taxonomy UI or another appropriate crawlable component.
- Do not force redundant boilerplate parent links into body copy when the hierarchy is already clearly and crawlably represented.
- Cross-family educational/commercial links are not mandatory parent/hub links under this Decision and remain governed by DEC-042 through DEC-046.

### Consequences

- Family-level QA must verify that required parent/hub relationships are crawlable and consistent.
- Multi-parent Products and Articles require stable primary hierarchy selection.
- Breadcrumb implementation may satisfy part of this requirement where its visible crawlable trail matches the accepted hierarchy.



## DEC-042 — Product to Academy / Article Linking Rules
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** PRODUCT / INTERNAL LINKING / EDUCATIONAL CONTENT

### Accepted target state

- Product pages link to Academy Guides/Lessons or Magazine Articles only when the destination directly helps the user select, prepare, use, apply, fix/cure, care for, or otherwise correctly work with that Product or Product family.
- Approved Product → education relationships are classified under DEC-040 as CORE/MANDATORY, FAMILY-SPECIFIC, or CONTEXTUAL/OPTIONAL.
- A guide that provides an essential instruction shared by an entire Product family may become CORE/MANDATORY for that family.
- Content relevant only to a defined Product family may be FAMILY-SPECIFIC.
- Content useful only in a particular page context remains CONTEXTUAL/OPTIONAL.
- Broad topical similarity alone does not justify adding a Product-page internal link.
- Educational links must not be mass-added merely to increase internal-link count.
- Exact approved destinations and family coverage are maintained in the Internal Link Requirement Matrix.

### Consequences

- Product-family QA must compare implemented educational links against the approved matrix.
- Equivalent Products must not randomly omit CORE/MANDATORY relationships.
- Historical, inspirational, or broadly related Articles are not automatically Product-page link targets.
- Reverse Academy/Article → Product/Category rules remain governed by DEC-043 and DEC-044.


## DEC-043 — Academy / Lesson to Product / Category Linking Rules
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** ACADEMY / INTERNAL LINKING / COMMERCIAL DESTINATIONS

### Accepted target state

- Academy, Guide and Lesson pages link to a Product or Product Category only when the Product, material, tool, or Product family is actually used, required, or provides a direct useful next step for completing the instruction.
- Prefer a specific Product destination when the instruction concerns a specific item.
- Prefer the relevant Product Category when the user reasonably needs to choose among a family of suitable products.
- Commercial links must remain useful in the instructional context.
- Do not add generic, unrelated, or sitewide commercial links merely to increase SEO/internal-link volume.
- Approved relationships remain subject to the DEC-040 classification model and the Internal Link Requirement Matrix.

### Consequences

- Academy-family QA must verify that commercial destinations match the actual instructional need.
- Product-level links require real product-specific relevance.
- Category-level links are preferred when the instructional need is category-wide or requires user choice.
- Article → Product/Category rules remain governed separately by DEC-044.


## DEC-044 — Article to Product / Category Linking Rules
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** MAGAZINE / INTERNAL LINKING / COMMERCIAL DESTINATIONS

### Accepted target state

- Article pages link to a Product or Product Category only when the commercial destination directly supports the article topic and provides a useful next step for the reader.
- Prefer a specific Product when the Article materially discusses, recommends in context, or uses that specific item.
- Prefer the relevant Product Category when the reader reasonably needs to choose among a family of suitable products.
- There is no sitewide requirement for every Article to contain a commercial link.
- Historical, inspirational, artist-focused, reference, or other informational Articles may legitimately contain no commercial link when no useful commercial next step exists.
- Do not add unrelated or generic Shop/Product links merely to increase internal-link volume or SEO coverage.
- Approved relationships remain subject to DEC-040 and the Internal Link Requirement Matrix.

### Consequences

- Article-family QA evaluates commercial links by contextual usefulness rather than raw link presence.
- Missing commercial links are not defects when no relevant commercial next step exists.
- Product-level links require product-specific relevance; category-level links are preferred when user choice across a family is more appropriate.
- Article → Article / Academy relationships remain governed by DEC-045.


## DEC-045 — Article to Article / Academy Linking Rules
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** MAGAZINE / INTERNAL LINKING / EDITORIAL AND EDUCATIONAL DESTINATIONS

### Accepted target state

- Article → Article and Article → Academy links are based on semantic relevance and a useful next step for the reader.
- Valid Article → Article relationships include genuine continuation, deeper detail, prerequisite/background material, or complementary reference content.
- Article → Academy links are appropriate when a practical Guide/Lesson lets the reader apply or learn the article topic in a useful next step.
- There is no sitewide quota requiring every Article to contain a fixed number of links to other Articles or Academy content.
- Related-content modules must not create random links solely because pages share a Category, Tag, or broad keyword.
- Automated or templated related-content destinations must satisfy the same relevance rule as manually selected links.
- Approved relationships remain subject to DEC-040 and the Internal Link Requirement Matrix.

### Consequences

- Article-family QA evaluates editorial/educational links by relevance and usefulness rather than raw link count.
- An Article may legitimately have no Article/Academy contextual link when no useful destination exists.
- The execution matrix must identify approved mandatory/family-specific relationships separately from page-level contextual candidates.


## DEC-046 — Category to Education / Reference Linking Rules
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** PRODUCT CATEGORY / INTERNAL LINKING / CONTENT LANDINGS

### Accepted target state

- Product Category archives are not required to add Academy or Article links while they remain product-listing-only archives.
- Category → Academy/Article linking becomes appropriate when a Product Category is deliberately developed into a content-supported landing page.
- On a content-supported Category landing page, selected educational/reference destinations must directly support understanding, selection, preparation, use, technique, or care for that Product Category.
- Do not add generic sitewide education/reference link sets to Category archives solely to increase internal-link coverage.
- A Category landing page may contain no educational/reference link when no sufficiently relevant destination exists.
- The content structure, required sections, depth, and editorial requirements for Product Category landing pages are not defined by this decision and require a separate content decision before implementation.

### Consequences

- Current listing-only Category archives do not require artificial educational-link modules.
- Future Category landing-page content may create natural Category → Academy/Article relationships.
- Category landing-page content requirements must be explicitly decided before implementation.


## DEC-047 — Internal-Link Anchor Text Policy
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** SITEWIDE / INTERNAL LINKING / ANCHOR TEXT

### Accepted target state

- Internal-link anchor text must be concise, natural, descriptive, and contextually accurate to the destination.
- Exact-match keyword repetition is not required.
- Do not force one fixed anchor across all source pages linking to the same destination.
- Do not invent query-target anchors without supporting evidence.
- Natural anchor variation is allowed when each variant accurately describes the destination in its source context.
- Avoid generic anchors such as “click here” when a meaningful descriptive phrase is naturally available.
- Anchor wording must serve reader comprehension first and must not be distorted merely to repeat a target keyword.

### Consequences

- Internal-link QA evaluates anchor relevance and clarity rather than exact-match consistency.
- Equivalent links may use different natural anchor wording across different source contexts.
- Keyword/query evidence may inform anchor language but does not create a requirement for repetitive exact-match anchors.


## DEC-048 — Orphan / Underlinked Thresholds and Approved Exceptions
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** SITEWIDE / INTERNAL LINKING / COVERAGE QA

### Accepted target state

- Important indexable pages with an assigned SEO or information-architecture role must have a meaningful crawlable path from the internal site architecture.
- A page is considered orphaned when no meaningful internal crawl path reaches it.
- A page is considered underlinked when required relationships defined for its page family or in the approved internal-link rules/matrix are missing.
- Do not use a universal minimum inbound-link count as the definition of adequate internal linking.
- Utility, noindex, temporary, or deliberately non-search-target pages may be documented exceptions.
- Broken URLs and 404 links are a separate issue from orphan/underlinked coverage.

### Consequences

- Internal-link QA evaluates architectural coverage and required relationships rather than a generic link-count threshold.
- Missing required family relationships must be corrected or documented as an approved exception.
- Pages outside the intended search architecture do not require artificial links solely to avoid an orphan label.


## DEC-049 — Magazine vs Academy Intent Boundary
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** CONTENT ARCHITECTURE / MAGAZINE / ACADEMY

### Accepted target state

- Academy is Mariwork's video-education destination.
- Academy content is centered on practical learning: demonstrations, techniques, step-by-step instruction, and how to use products, materials, or tools.
- Magazine is Mariwork's broader editorial destination for art topics related to fabric painting and hand printing, reference and historical content, news/editorial coverage, product introductions, and written tips or techniques.
- The presence of a technique, tip, or limited instructional material does not by itself make Magazine content an Academy item.
- Magazine may link to Academy when a practical video lesson is a useful next step for the reader.
- Academy is not required to link back to a Magazine Article merely because the Article discusses a related topic.
- Product introduction, editorial coverage, context, or discussion belongs in Magazine when editorial in nature.
- Practical instruction showing how to use a Product belongs in Academy when delivered as video education.

### Consequences

- Content placement is determined by the role and format of the content, not merely by topic overlap.
- Magazine and Academy may cover related subjects without being treated as interchangeable page families.
- Magazine → Academy is a natural editorial-to-practical progression when relevant; the reverse relationship is optional and context-dependent.


## DEC-050 — Product vs Category vs Article Query / Content Role Boundary
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** CONTENT ARCHITECTURE / PAGE OWNERSHIP / SEARCH INTENT

### Accepted target state

- Product pages own specific-product intent.
- Product Category or content-supported Category landing pages own product-family, browse, comparison-within-family, and choice intent.
- Magazine Articles own informational/editorial intent where the user primarily needs to understand, explore, compare, or read about a subject rather than browse a product family.
- Do not assign substantially the same primary intent to Product, Category, and Article pages without a deliberate documented reason.
- Ambiguous intent boundaries require later keyword research, SERP research where needed, and explicit page ownership.
- This decision defines the page-role boundary only.
- Research methodology, Page Ownership Matrix rules, conflict resolution, and implementation are governed by later decisions and must not be inferred or executed from DEC-050 alone.

### Consequences

- DEC-050 does not authorize implementation or page reassignment by itself.
- Ambiguous topics remain unresolved until the relevant research and ownership decisions are completed.
- Later page-ownership work must preserve this role boundary unless a formally accepted decision changes it.


## DEC-051 — Magazine Hub and Blog Category Hierarchy
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** CONTENT ARCHITECTURE / MAGAZINE / NAVIGATION

### Accepted target state

- `/mag/` is the primary Magazine hub and discovery surface for Mariwork editorial content.
- The Magazine hub provides structured access to Magazine categories and their content.
- The hub may use category blocks, archive/list sections, latest-content modules, or other deliberate discovery components.
- Magazine categories form the navigational and content hierarchy beneath the Magazine hub.
- The Magazine hub is not treated as an ordinary Article or an ordinary Category archive.
- DEC-051 does not define the final Magazine category taxonomy, category names, or category-specific content strategy.
- Final category taxonomy and category-specific content roles require separate content decisions.

### Consequences

- Magazine navigation and discovery should preserve `/mag/` as the central editorial hub.
- Category architecture may evolve without changing the hub role established by this decision.


## DEC-052 — History / Artists Content Strategy
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** MAGAZINE / HISTORY / ARTISTS BOUNDARY

### Accepted target state

- Historical and globally significant artists may be covered as Magazine Articles when they have genuine editorial, artistic, or historical value.
- History content about art, fabric painting, hand printing, techniques, movements, and relevant artists belongs to the Magazine editorial architecture.
- A Magazine Article about an artist is editorial content and is not an Artist profile merely because its subject is an artist.
- The future `/artists/` hub and its profiles represent the separate Mariwork Artists directory/project.
- Historical Artist URL migration remains governed by DEC-028: use one-to-one identity-matched redirects to new Artist profiles where a real match exists; otherwise use the main Artists hub as the approved fallback, and consolidate the old Artists archive to that hub after the new system is public and stable.
- DEC-052 does not define which artists must be covered, publishing volume, or a detailed History editorial calendar.

### Consequences

- Magazine History/artist editorial content and Mariwork Artist profiles remain separate content families with separate roles.
- DEC-052 does not supersede or reopen the Artists migration policy accepted in DEC-028.
- Detailed History editorial planning remains a later content-strategy decision.


## DEC-053 — Canonical Mariwork Facts and Naming-Consistency Registry
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** BRAND / ENTITY / NAMING / FACTUAL CONSISTENCY

### Accepted target state

- The owner-confirmed canonical facts registry in `strategy/BRAND-ENTITY-SEARCH.md` is the factual baseline for Mariwork brand/entity naming, content and structured-data work.
- Canonical Persian brand name: `ماری‌ورک`.
- Canonical English brand name: `Mariwork`.
- Official website: `mariwork.ir`.
- Founder: `مریم مختاری`; canonical English name: `Maryam Mokhtari`.
- Canonical founder title: Founder of Mariwork.
- Start year: 1395 SH.
- Owner-confirmed experience claim: more than 10 years.
- Mariwork is an Iranian brand/business, not a company/legal entity label by default.
- Preferred concise brand definition: `ماری‌ورک تولیدکننده رنگ‌های پارچه و محصولات تخصصی نقاشی و چاپ روی پارچه است.`
- Mariwork specializes in fabric painting and hand printing.
- Mariwork fabric colors are designed for painting and printing on fabric, not fabric dyeing.
- Mariwork fabric colors must not be represented as ordinary acrylic paint or merely an equivalent/subtype of standard acrylic paint; detailed technical differences require separate factual evidence.
- Products are formulated in Iran by Iranian engineers using foreign-origin materials.
- Production, mixing, filling and final preparation are performed in Iran.
- Primary market/activity geography: Iran.
- Mariwork manufactures its core portfolio; a small number of Other Tools items are third-party products and must not be represented as Mariwork-branded/manufactured merely because they are sold on mariwork.ir.
- Primary audience: artists, learners/students, and professional or educational users of fabric painting and hand printing.
- Education is a real brand activity, and developing the art through education is one of Mariwork's main goals; Mariwork must not be reduced to an educational institute.
- Existing English tagline: `add color to your life`; it is not a mandatory sitewide SEO/entity message.
- Official logo wordmark text: `Mariwork`; there is no separate official Persian wordmark.
- Official section labels include `آکادمی ماری‌ورک`, `مجله ماری‌ورک`, and `هنرمندان` for the `/artists/` project.
- Shop navigation may use `فروشگاه`; `فروشگاه ماری‌ورک` may be used naturally in Titles/H1/prose where useful, but brand insertion is not mandatory.
- Mariwork sells directly through its online store and is also stocked by third-party physical stores.
- Canonical wording for those outlets is `فروشگاه‌های عرضه‌کننده محصولات ماری‌ورک`.
- Mariwork currently has no official or exclusive representative/dealer network by default; do not label third-party outlets as official representatives, exclusive representatives, branches or Mariwork-owned stores without separate verification.
- Mariwork has no public official physical brand address to publish as a canonical Organization/Contact location.
- Official social presence exists on Instagram, YouTube, Telegram and Aparat, and official phone/email/WhatsApp contact channels exist; exact verified handles, URLs and contact details are deferred to DEC-127.
- Do not infer or invent legal status, awards, credentials, technical Product mechanisms, addresses, social URLs, contact details or other entity facts beyond the verified registry.

### Consequences

- Future Homepage, About, Why Mariwork, Product, Article, Academy, Organization schema and brand-entity work must remain consistent with this registry unless a later accepted decision amends a fact.
- Earlier uses of `ماری ورک` or `ماریورک` in visible naming are non-canonical and should be normalized during the appropriate implementation/content pass without changing URLs solely for spelling normalization.
- Exact social/contact identity is not authorized by DEC-053 and remains blocked on DEC-127.
- Stores/location/NAP treatment remains governed by DEC-087.


## DEC-054 — ALT Policy by Image Role
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** IMAGE SEO / ALT / ACCESSIBILITY / CONTENT FAMILIES

### Accepted target state

- ALT decisions are based on the actual role and context of an image, not on missing-ALT counts alone.
- Informative images require concise, factual, context-appropriate ALT.
- Truly decorative images use an empty ALT attribute.
- Do not invent visual facts or use keyword-stuffed ALT.
- Store/Product imagery generally defaults to informative unless an asset is genuinely decorative.
- Academy instructional/explanatory imagery generally defaults to informative unless an asset is genuinely decorative.
- Reused image files do not require identical ALT across pages. ALT may vary by page context and image role as long as every version remains factually accurate to the visible image and useful in that context.
- Magazine/Article images that support understanding, identify an artwork/artist/product, explain a technique or otherwise carry meaning require ALT.
- Meaningful featured/hero images require ALT.
- Decorative textures, separators and ornamental graphics use empty ALT.
- Historical, artwork and artist ALT may include identity facts only when verified; do not infer names, works or context from the image alone.
- Homepage/Static/Category images that represent a Product, Category, Academy, Magazine, brand subject or other meaningful content require ALT.
- Decorative backgrounds, patterns, shapes and UI ornament use empty ALT.
- The primary logo uses concise brand ALT such as `ماری‌ورک`.
- Icons next to equivalent visible text are generally decorative and should not create redundant ALT.
- Representative Product Category images use factual, category-relevant ALT.
- For linked images, ALT must make the image/link purpose understandable when the image is the meaningful link content. Where equivalent visible link text already communicates the destination, avoid redundant or inflated ALT.
- Images containing meaningful text, infographics and instructional screenshots require concise purpose/meaning-oriented ALT rather than raw filenames, generic labels or automatic OCR dumps.
- Essential information shown in a text-bearing image or infographic should also exist in surrounding HTML or a useful caption where appropriate instead of being available only inside the image.
- ALT may be generated automatically from verified structured facts when the image role is deterministic, for example a primary Product image using the canonical Product identity or a representative Category image using the canonical Category identity.
- Context-dependent Article, Academy, screenshot, infographic, artwork and similar imagery requires contextual judgment; page Title alone is not a sufficient universal ALT source.
- Automation must never infer unsupported colors, techniques, artist identities, Product properties, uses or other visual facts.
- Product-gallery-specific image behavior remains governed by DEC-056.

### Google basis

Google states that alt text is an important source of image metadata, uses it together with page context and computer vision to understand image subject matter, and may use image ALT as anchor text when an image is a link. Google recommends useful, information-rich ALT that fits the page context and warns against keyword stuffing.

### Consequences

- Missing ALT is a review candidate, not an automatic instruction to populate text.
- Family-level QA must distinguish informative from decorative imagery.
- Bulk ALT generation is allowed only when factual source data and image role make the output deterministic and accurate.
- Implementation remains separate from this strategy decision.


## DEC-056 — Product Image / Gallery SEO Policy
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** PRODUCT IMAGE SEO / VARIANTS / GALLERY BOUNDARY

### Accepted target state

- For Mariwork fabric-color Products, the primary Product image intentionally represents the 60 ml package/variant.
- This is a deliberate merchandising/commercial decision and must not be overridden by SEO merely to make the primary image variant-neutral.
- For variable fabric-color Products, selecting a volume variant changes the displayed Product image to the image for that selected volume.
- SEO does not require all volume images to be shown simultaneously in the gallery when the variant-image interaction already exposes the correct selected-volume image.
- Gallery image count, diversity, composition and merchandising order are fixed Product/design decisions and are outside SEO strategy unless a specific technical discoverability, accessibility, factual-accuracy or Search issue is evidenced.
- ALT behavior remains governed by DEC-054.
- Product image behavior must remain factually aligned with the available variants and must not misrepresent the purchasable Product.
- SEO scope is limited to primary/variant image consistency and technical image discoverability; DEC-056 does not authorize gallery redesign.

### Google basis

Google requires Product structured-data images to represent the marked-up Product and to be crawlable/indexable. Google also recommends clear representative Product imagery, but does not require Mariwork to change its merchandising choice of a 60 ml default image when the page accurately represents the variable Product and the selected variant image updates correctly.

### Consequences

- The 60 ml default image is preserved for fabric-color Products.
- Variant-image switching remains part of the intended Product experience.
- SEO QA may flag broken, inaccessible or factually mismatched Product images, but not gallery composition merely because a different merchandising arrangement might exist.


## DEC-057 — Article / Academy Instructional Image Policy
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** MAGAZINE / ACADEMY / INSTRUCTIONAL IMAGERY

### Accepted target state

- There is no fixed SEO quota for the number of images in a Magazine Article or Academy page.
- Mariwork Academy is video-first. Supplementary images are used only when they materially improve explanation of a step, tool, result, detail or concept.
- Magazine/Article images are used when they improve understanding, documentation, artwork/artist/Product identification, technique illustration or editorial quality.
- Do not add images merely so a page has images for SEO.
- Instructional images must align with the actual lesson, Article and video context rather than functioning as generic filler.
- A representative Featured Image may support an Article, but multiple in-body images are not an SEO requirement.
- ALT behavior remains governed by DEC-054.

### Consequences

- Image count is determined by content need, not an SEO formula.
- Academy remains video-first even when supporting images are present.
- Magazine and Academy content QA evaluates image usefulness and factual relevance rather than raw image quantity.


## DEC-059 — Store Facets / Sort / Display Parameter Policy
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** STORE / FACETS / SORT / DISPLAY PARAMETERS / VARIANT PRESELECTION

### Accepted target state

- Store filter, sort and display parameter states are user-interface states, not independent SEO landing pages.
- This includes parameter families such as `filter_volume`, `orderby`, `per_page`, `per_row` and `shop_view`.
- These parameter states must not be promoted as separate Search targets or XML sitemap entries.
- They should consolidate canonically to the relevant base Shop page rather than compete as standalone Search pages.
- Approved durable `pa_volume` landing pages such as `/volume/30ml`, `/volume/60ml` and `/volume/250ml` remain separate indexable SEO landing pages under DEC-026.
- Product-level variation-preselection URLs using `attribute_pa_volume` are a separate mechanism and must remain available for direct variant selection.
- Product variation-preselection URLs must not be treated as Shop facet URLs merely because they use query parameters.
- Do not apply blanket robots blocking that could interfere with legitimate Product variant-selection behavior.

### Consequences

- Shop filters and sort/display controls remain usable for users without becoming separate SEO landing-page families.
- Volume SEO ownership remains with the durable `pa_volume` landing pages accepted in DEC-026.
- Product-level direct variant links remain available.
- Technical implementation must distinguish Shop facet/query states from Product variation-preselection states.


## DEC-060 — Shop Pagination and Legacy `product-page` Policy
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** SHOP / PAGINATION / LEGACY URL CONSOLIDATION

### Accepted target state

- `/shop/page/N/` is the canonical Shop pagination architecture.
- Legacy or alternate `?product-page=N` pagination states must stop being generated by the site.
- Historical `?product-page=N` URLs should consolidate to the corresponding canonical `/shop/page/N/` URL through the approved redirect/canonical implementation path.
- Do not maintain two parallel pagination URL systems for the same Shop result pages.
- This decision does not change Product URLs, approved `pa_volume` landing pages, Store facet/sort/display states, or Product variation-preselection URLs.

### Consequences

- Shop pagination has one durable URL pattern.
- Legacy `product-page` URLs become migration/consolidation concerns rather than a second active pagination family.


## DEC-061 — Product Search URL Policy
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** INTERNAL PRODUCT SEARCH / INDEXABILITY / UTILITY URLS

### Accepted target state

- Internal Product search result URLs remain available for users as utility pages.
- They are not independent SEO landing pages.
- Keep internal Product search result URLs `noindex`.
- Exclude them from XML sitemaps.
- Do not optimize internal search-result URLs as query-target landing pages.
- Search functionality remains available to users.
- Do not rely on robots.txt blocking in a way that prevents crawlers from seeing the `noindex` directive.
- Product, Product Category, approved `pa_volume` and other durable landing pages remain the intended Search targets.

### Consequences

- Internal search remains a UX/navigation feature rather than an indexable landing-page family.
- Search-result query combinations do not become a scalable source of low-value indexable URLs.


## DEC-062 — Author / Date Archive Public and Indexability Policy
**Status:** Accepted  
**Date:** 2026-09-25  
**Scope:** WORDPRESS ARCHIVES / AUTHOR / DATE / INDEXABILITY

### Accepted target state

- Author archives are not an independent SEO landing-page family for Mariwork.
- Date archives are not an independent SEO landing-page family for Mariwork.
- If these archive routes are publicly generated, keep them out of XML sitemaps and prevent them from becoming Search targets through the approved noindex/non-public implementation path.
- Current Magazine Articles and durable Blog Categories remain the primary editorial discovery and index surfaces.
- Current Mariwork Articles use the authoritative Mariwork Organization rather than individual named author entities under DEC-034; Author archives therefore do not receive separate SEO ownership.
- Date archives do not receive independent Search targeting merely because WordPress can generate chronological archive routes.
- Current evidence does not prove concrete public Author or Date archive routes; implementation must verify actual route existence and behavior rather than inventing URLs.

### Consequences

- Article and Category architecture remains the durable editorial search architecture.
- Author/Date archive handling remains separate from feeds, internal search and general 404/error lifecycle decisions.
