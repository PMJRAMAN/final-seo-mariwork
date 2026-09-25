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
