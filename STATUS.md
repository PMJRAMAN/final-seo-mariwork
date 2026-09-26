# Project Status

**Project:** Final SEO Mariwork  
**Framework:** v1.0  
**Framework state:** FROZEN  
**Phase:** STRATEGY LOCK / EXECUTION RECONCILIATION
**Status:** PRE-LOCK AUDIT PASSED — READY FOR STRATEGY LOCK; EXECUTION RECONCILIATION PENDING
**Last framework review:** 2026-09-26

Final pre-lock audit: `audits/strategy/FINAL-PRE-STRATEGY-LOCK-AUDIT-2026-09-26.md`

## Decision Backlog v1 coverage freeze — 2026-09-25

P-001 through P-005 are complete.

- Decision coverage audit: completed by Codex.
- ChatGPT P-002 independent review: complete.
- Authoritative reconciliation: complete.
- Canonical coverage matrix: **135 rows / zero unexplained material gaps**.
- Decision Backlog: **129 decision records; highest ID DEC-130; DEC-126 is intentionally left unused and IDs are not renumbered**.
- Existing Decision IDs renumbered: **0**.
- Production writes: **0**.

The freeze applies to **decision-domain coverage**, not to the target states themselves.

Current Backlog has **zero OPEN / PROPOSED / DISCUSSING / NEEDS_TARGETED_EVIDENCE unresolved decisions**. Accepted-with-evidence/research decisions still carry their scoped evidence gates before execution.

Execution remains locked. P-006/P-007 are intentionally pending until the Execution Backlog is reconciled against this frozen structure before any implementation package is promoted to READY_FOR_TASK.

## Decision Backlog coverage freeze

Before the Decision Backlog is treated as exhaustive implementation governance, it must pass the P-program coverage freeze:

- P-000 ChatGPT preliminary precheck: complete.
- P-001 independent Codex Decision Backlog coverage audit: complete.
- P-002 ChatGPT review of P-001: complete.
- P-003/P-004 reconciliation and coverage matrix closure: complete.
- P-005 Decision Backlog v1 coverage freeze: complete.
- P-006/P-007 Execution Backlog reconciliation: pending.

Current authoritative Decision Backlog is **FROZEN_V1_COVERAGE** and may now be used as the canonical strategy queue.

Task: `tasks/P-001-DECISION-BACKLOG-COVERAGE-AUDIT.md`  
Precheck: `audits/strategy/P-000-CHATGPT-DECISION-BACKLOG-PRECHECK.md`

## Strategy / Decision Phase — 2026-09-25

The project does not move directly from audit findings to Production.

Current planning authorities:

- `MASTER-TODO.md` — complete-site coverage/program ordering.
- `strategy/DECISION-BACKLOG.md` — owner + ChatGPT target-state decisions.
- `tasks/EXECUTION-BACKLOG.md` — implementation packages unlocked only by accepted decisions.
- `docs/DECISION-TO-EXECUTION-GOVERNANCE.md` — governing process.

The Decision Backlog now records the resolved target-state strategy across titles/H1, metadata, taxonomies, sitemap, schema, internal links, content architecture, semantic positioning, images/video, AI-answer discoverability, system URL policy and legacy migration. Six future programs remain intentionally DEFERRED.

The Execution Backlog is intentionally locked. No Production Codex implementation task may be generated until the blocking Decision IDs are `ACCEPTED` and the related execution item is `READY_FOR_TASK`.

Process decision: `SEO-019`.

## ChatGPT full-site Second Review — 2026-09-25

Independent Second Review is complete and recorded in:

- `audits/second-review/sitewide/SR-005-CHATGPT-FULL-SITE-SECOND-REVIEW.md`

Result:

- broad full-site audit/discovery is closed; do not restart it;
- Store SR-004 remains operative and is confirmed by SR-005;
- human approval is still required before Production implementation;
- targeted work remains for `pa_volume` index/sitemap policy, tag migration mappings, selected historical mappings, LearnDash schema/video canary, representative visual ALT review, exact internal-link destinations, and final changed copy;
- Page+Query data remains unavailable but does not block unrelated technical implementation;
- closure bookkeeping is corrected for forward planning to **8 current Static/Core pages + 2 historical 404 Static dossiers**, rather than treating all 10 dossiers as current pages;
- SR-005 added systemic findings `SYS-016` through `SYS-018`;
- Production writes during Second Review: **0**.

Target-state decisions are now owner-approved where required. Implementation remains **NOT AUTHORIZED** until Strategy Lock scopes are recorded, P-006/P-007 reconcile the Execution Backlog, and each scoped item satisfies its evidence/dependency gates.

## Full-site closure — 2026-09-25

The current Production census is reconciled against `registry/URL-INVENTORY.csv`,
the existing 168 Round-1 dossiers, Store Second Review evidence, family-level
reconciliations and machine/system URL-space policies.

Closure artifacts:

- `audits/sitewide/PRE-IMPLEMENTATION-COVERAGE-MATRIX.json`
- `audits/sitewide/PRE-IMPLEMENTATION-AUDIT-CLOSURE.md`
- `audits/sitewide/SYSTEM-URL-SPACES-CLOSURE.md`
- `audits/sitewide/IMAGE-ALT-AUDIT-SUMMARY.md`
- `strategy/INTERNAL-LINK-REQUIREMENT-MATRIX.md`
- `handoff/FULL-SITE-PRE-IMPLEMENTATION-SECOND-REVIEW-HANDOFF-2026-09-25.md`

Three missing current system-page dossiers were added for WP-10 Checkout,
WP-11 My Account and WP-30919 Cart. They are policy-only dossiers; no editorial
copy recommendation was made.

Current entities: **502** (147 public post entities + 355 taxonomy terms).
Existing dossiers reused: **168**. New dossiers: **3**. Production writes:
**0**.

Second Review is now complete. Human approval, implementation, Codex QA after implementation and
ChatGPT Final QA remain pending. `NOT_DECIDED` inventory dispositions are
intentional at this stage; this closure does not approve redirects, noindex,
canonical, sitemap, taxonomy, content, schema or URL changes.

## Final pre-audit review

چارچوب پروژه دوباره بررسی و قبل از Batch 001 تثبیت شد.

اضافه/تقویت شده:
- Sitewide Technical Baseline
- Content Research Spec
- central systemic findings registry
- systemic change dossier
- canary + regression rollout
- Codex QA + independent ChatGPT Final QA
- framework change control
- measurement/change annotation
- data security/PII rules
- Query Map / Content Architecture
- official references registry
- evidence class + confidence

## Raw datasets موجود

- Search Performance export — 2026-09-24 — Last 16 months
- Coverage/Indexing export — 2026-09-24

پوشه‌های export فعلی در ریشه immutable raw snapshot هستند.

## Gate قبل از Page Audit

پیش از Batch 001:

1. URL/Entity Inventory
2. URL history mapping
3. Sitewide Technical Baseline
4. Search Console baseline normalization
5. Systemic findings registry initial pass
6. Batch 001 selection

## تغییر Production

تا این لحظه framework work فقط repository بوده است. هیچ تغییر SEO Production بخشی از این مرحله نیست.


## Master execution program

مرجع ترتیب کار: `MASTER-TODO.md`

Current priority:
1. A-010..A-020 Pre-audit baselines
2. Store/WooCommerce complete coverage
3. Homepage
4. Static pages
5. Blog/Articles
6. Academy/Education
7. Other content + archives/system URLs

قانون جدید:
- Google official documentation = SEO standard
- Rank Math = first technical owner for supported WordPress SEO concerns


## Round-1 automation

Runner و server-deployment task در repo تعریف شده‌اند. تا وقتی A-009 روی سرور deploy/verify نشده، automation زیرساخت آماده در repo ولی فعال‌شده روی Production environment محسوب نمی‌شود. Autonomous authority فقط تا CODEX_AUDITED است.


## Low-consumption v2 migration

Runner v1 consumed the short-window Codex allowance during A-013 after A-010, A-011 and A-012 completed. Those completed outputs remain valid.

Runner v2 is now present in the repository and must be deployed before A-013 resumes. It uses:
- deterministic evidence collection with no model call;
- grouped remaining Foundation work;
- no-model A-016/A-017/A-021;
- batched page audits (pilot 5, then default 15);
- FAMILY/SITEWIDE handling for repetitive taxonomy/system spaces;
- medium Foundation reasoning and low page-batch reasoning;
- disabled Codex network during analysis to prevent duplicate crawling.

Current paused A-013 state should be resumed only after A-009B deployment.


## Low-consumption v2.2 model policy

Pre-resume review now pins all autonomous Round-1 model calls to `gpt-5.6-luna` with `medium` reasoning, per project decision. Compact deterministic Foundation context, trimmed page-batch evidence payloads, Store-first ordering and disabled model network remain unchanged.

The launcher/installer were also hardened so syntax validation does not create `__pycache__` artifacts that can trip the clean-repository guard, and repository updates are performed as the dedicated `seo-audit` user. No authority or Production-write rule changed.


## Low-consumption v2.3 usage telemetry

The runner now records exact Codex JSON token usage per autonomous model job and cumulative usage in private runtime state:
input, cached input, derived uncached input, output, reasoning output when exposed, and cache-hit ratio. Status also separates Foundation and page-batch averages.

Rate-limit percentages are recorded only when the installed Codex CLI exposes them; the runner does not estimate an account quota from token counts alone. This telemetry is intended to verify whether compact evidence, grouped Foundation jobs and batched page audits materially reduce model consumption.


## A-013 sandbox compatibility fix

The first v2.3 A-013 attempt paused safely because the hardened systemd service allowed only AF_UNIX/AF_INET/AF_INET6 while Codex bubblewrap requires AF_NETLINK/NETLINK_ROUTE for local sandbox setup. The service policy now adds AF_NETLINK only. Codex model networking remains disabled, and Production/DB isolation is unchanged.

The failed attempt must not be treated as an SEO failure or completed A-013 output; retry A-013 only after the updated service policy is deployed.


## Pre-Strategy-Lock consistency review — 2026-09-26

Result: **PASS WITH NON-STRATEGY INPUT GATES**

- unresolved target-state decisions: **0**
- intentionally deferred decisions: **6**
- superseded traceability records: **2**
- accepted policies requiring targeted evidence before affected execution: retained as explicit gates
- canonical decision coverage: **135 rows / zero unexplained material gaps**
- DEC-028/052 Artist migration conflict: reconciled with DEC-066
- internal-link draft conflict: replaced by canonical accepted matrix
- Content Architecture / Visual / Video strategy files: reconciled with accepted decisions
- DEC-121 semantic positioning: promoted to a dedicated canonical foundation document
- DEC-129 AI discoverability: retained as a foundational content/SEO objective

Next governance step: Strategy Lock scope definition, then P-006/P-007 Execution Backlog reconciliation. No Production write is authorized by this review.
