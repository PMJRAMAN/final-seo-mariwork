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
