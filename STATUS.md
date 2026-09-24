# Project Status

**Project:** Final SEO Mariwork  
**Framework:** v1.0  
**Framework state:** FROZEN  
**Phase:** Pre-Audit Baseline  
**Status:** AUDIT_FRAMEWORK_READY  
**Last framework review:** 2026-09-24

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
