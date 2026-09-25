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
