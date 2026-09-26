# SL-001 — Core Technical / System URL Architecture

**Status:** STRATEGY_LOCKED  
**Locked:** 2026-09-26  
**Baseline repository HEAD:** `486abc31d66910d8b0f7323b25954b79d49134e6`

## Accepted Decision IDs

Primary:
- DEC-004, DEC-030, DEC-031
- DEC-059, DEC-060, DEC-061, DEC-062
- DEC-067
- DEC-074, DEC-075
- DEC-078, DEC-079, DEC-080
- DEC-107, DEC-108, DEC-109, DEC-110, DEC-111

Cross-cutting governance:
- DEC-068, DEC-069, DEC-102, DEC-103, DEC-104, DEC-112

## Exact target state

- preferred canonical host/protocol remains `https://www.mariwork.ir/`;
- preserve established trailing-slash convention and avoid cosmetic URL migrations;
- one intended canonical URL per durable entity;
- utility/account/transactional/internal-search pages are not Search landing pages;
- RSS/feed endpoints are system distribution URLs, not Search targets;
- Shop facets/sort/display states do not become independent landing pages;
- canonical pagination uses the approved `/shop/page/N/` architecture;
- Attachment HTML pages are not durable Search targets;
- Author/Date archives are not independent SEO families;
- real removed URLs use 404/410 unless a genuine semantic successor warrants 301;
- Nginx is the canonical redirect owner;
- important crawl/discovery links/content must not unnecessarily depend on click-only JS/AJAX;
- legitimate Search crawler access is preserved subject to deliberate page-level exclusions;
- CWV remediation is evidence-driven, using field evidence where available.

## Evidence gates before affected execution

- DEC-080 representative initial HTML/rendered DOM checks;
- DEC-110 actual robots/WAF/server crawler behavior;
- DEC-111 mobile/template field/lab performance evidence;
- Attachment/media reconciliation before destructive cleanup.

## Scope boundaries

Does not authorize Product/content rewrite, taxonomy deletion, media deletion or redirect creation without the corresponding family/migration execution package.

## Dependencies

- SL-000
- family sitemap/indexability decisions
- DEC-067 for every redirect write
