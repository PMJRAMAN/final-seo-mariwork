# SL-004 — Internal Links / Navigation / Hub Relationships

**Status:** STRATEGY_LOCKED  
**Locked:** 2026-09-26  
**Baseline repository HEAD:** `486abc31d66910d8b0f7323b25954b79d49134e6`

## Accepted Decision IDs

Primary:
- DEC-040 through DEC-048
- DEC-051
- DEC-120
- DEC-123, DEC-124
- DEC-130

Dependencies:
- DEC-001, DEC-025, DEC-026, DEC-049, DEC-050
- DEC-121, DEC-122
- SL-000

## Exact target state

- use CORE_MANDATORY / FAMILY_SPECIFIC / CONTEXTUAL_OPTIONAL classes;
- mandatory links primarily preserve deliberate parent/hub hierarchy;
- Product → Category → Shop, Article → Blog Category → Magazine, Guide/Lesson → collection/course → Academy;
- cross-family education/commercial links are relevance-driven and not CORE by default;
- Header/Footer expose durable hubs and essential destinations only;
- no sitewide link-count targets;
- no mass keyword auto-linking;
- natural descriptive anchors;
- no universal inbound-link threshold for orphan/underlinked status.

Canonical files:
- `strategy/INTERNAL-LINK-ARCHITECTURE.md`
- `strategy/INTERNAL-LINK-REQUIREMENT-MATRIX.md`

## Non-blocking implementation inputs

- exact destination URLs/entities;
- source-page applicability lists;
- natural anchor/context;
- documented exceptions;
- current coverage measurements.

## Boundary

Exact link mappings must remain inside the accepted matrix and may not silently redefine page/query ownership.
