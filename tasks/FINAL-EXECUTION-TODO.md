# FINAL EXECUTION TODO — Mariwork SEO

**Status:** P-008 COMPLETE — EXECUTION TODO FROZEN FOR WAVE PLANNING  
**Generated from:** `tasks/EXECUTION-BACKLOG.md` after P-007  
**Date:** 2026-09-26  
**Production writes authorized here:** NO  
**Codex Production tasks issued here:** NO

## Purpose

This is the final execution-control TODO derived from the 57 validated execution packages. It does not replace the Execution Backlog, Decision Backlog, Strategy Locks, or MASTER-TODO. It provides one operational checklist for the remaining planning and execution lifecycle.

Stage 4 deliberately does **not** assign priority, Wave, or execution order. Those belong to Stage 5. A checked box here means the execution package itself has ultimately completed its governed lifecycle; READY_FOR_TASK is not completion.

## State contract

- **READY_FOR_TASK**: target state is sufficiently exact for a task to be written later. Remaining gate text is task preflight/evidence collection, not permission to skip governance.
- **BLOCKED**: a real prerequisite must be closed before task issuance.
- No Codex Production task is created by this document.
- No Production write is authorized until a specific package is READY_FOR_TASK and its exact Codex task is separately written under repository governance.
- Stage 5 may add Wave/priority metadata but must not silently change decisions, gates, or package scope.

## Coverage summary

- Total execution packages: **57**
- READY_FOR_TASK at Stage-4 freeze: **16**
- BLOCKED at Stage-4 freeze: **41**
- Completed execution packages: **0**
- Production writes in Stage 4: **0**

## Final execution checklist

| Done | ID | Execution package | Current state | Gate / preflight before or inside task | Strategy | MASTER | Owner |
|---|---|---|---|---|---|---|---|
| [ ] | EXE-001 | Change annotation + baseline + canary framework activation | **READY_FOR_TASK** | per-package baseline design | SL-000; DEC-068,069,102,103,104,112 | I, J | REPOSITORY / PROCESS |
| [ ] | EXE-002 | Monitoring outcome register and 28/56-day review workflow | **READY_FOR_TASK** | metric availability by package | SL-000; DEC-069,102,103,104 | J-001–J-009 | REPOSITORY / PROCESS |
| [ ] | EXE-003 | Preferred host/protocol/trailing-slash normalization verification | **READY_FOR_TASK** | current Production verification | SL-001; DEC-067,078,079 | I-004–I-007 | NGINX + RANK_MATH |
| [ ] | EXE-004 | Store facet/sort/display + pagination normalization | **BLOCKED** | exact current generator/redirect evidence | SL-001/SL-002; DEC-059,060,061,067,079 | B9, H-008 | NGINX + RANK_MATH |
| [ ] | EXE-005 | General internal-search / RSS-feed / utility indexability reconciliation | **READY_FOR_TASK** | current rendered robots/meta verification | SL-001; DEC-004,074,075,107,108 | H-006,H-007,H-009–H-012 | RANK_MATH / WORDPRESS |
| [ ] | EXE-006 | Author/date archive indexability reconciliation | **READY_FOR_TASK** | route existence verification | SL-001/SL-003; DEC-062,079 | H-003,H-004 | RANK_MATH |
| [ ] | EXE-007 | 404/soft-404/error-page technical behavior | **READY_FOR_TASK** | representative current response audit | SL-001/SL-006; DEC-109,067 | H-013,I-004 | NGINX + WORDPRESS |
| [ ] | EXE-008 | JS/AJAX discoverability remediation candidates | **BLOCKED** | initial-HTML/rendered-DOM/network evidence | SL-001; DEC-080,036 | B0/B3, I | CUSTOM_CODE where needed |
| [ ] | EXE-009 | Search crawler access: Googlebot/OAI-SearchBot vs GPTBot controls | **READY_FOR_TASK** | actual robots/WAF/server behavior and published-bot verification | SL-001/SL-005; DEC-110 | I-014 | NGINX / ROBOTS / WAF |
| [ ] | EXE-010 | Attachment HTML lifecycle + orphan-media safety reconciliation | **BLOCKED** | attachment/media dependency inventory | SL-001/SL-006; DEC-031,067,109 | H-005,L | WORDPRESS + NGINX |
| [ ] | EXE-011 | Sitewide sitemap reconciliation | **READY_FOR_TASK** | exact current sitemap membership audit | SL-001; DEC-025,026,028,029,030,031,062,107,108 | B0-002,I-006 | RANK_MATH |
| [ ] | EXE-012 | Shop landing H1/title/meta/content-block implementation | **BLOCKED** | current copy/placement recheck | SL-002; DEC-003,016,114,130 | B0-001,B10 | CONTENT + RANK_MATH |
| [ ] | EXE-013 | Fabric-color Product title normalization canary | **BLOCKED** | **item-1 canonical spelling consistency fix still pending**; exact 5-URL canary | SL-002; DEC-007,011,053,068 | B0-022–025,B2 | WOO + RANK_MATH |
| [ ] | EXE-014 | Set/Bundle Product title normalization canary | **BLOCKED** | item-1 spelling consistency fix; verified bundle identity | SL-002; DEC-008,011,053,068 | B0-022–025,B3 | WOO + RANK_MATH |
| [ ] | EXE-015 | Medium/Additive Product title normalization canary | **BLOCKED** | item-1 spelling consistency fix; verified Product identity | SL-002; DEC-009,011,053,068 | B0-022–025,B4 | WOO + RANK_MATH |
| [ ] | EXE-016 | Tool/Accessory Product title normalization canary | **BLOCKED** | exact real brand/code mapping | SL-002; DEC-010,011,053,068,081 | B0-022–025,B5 | WOO + RANK_MATH |
| [ ] | EXE-017 | Product meta-description remediation by family | **BLOCKED** | Product facts + copy QA | SL-002; DEC-015,068,121–125 | B2–B6 | CONTENT + RANK_MATH |
| [ ] | EXE-018 | Product visible-content architecture remediation by family | **BLOCKED** | family evidence + exact page scope | SL-002; DEC-020,042,083,088,121–125 | B2–B6 | CONTENT |
| [ ] | EXE-019 | Durable Product Category SEO package | **BLOCKED** | keyword/query research + exact copy | SL-002; DEC-021,025,030,046,076,115,121–125,130 | B7 | CONTENT + RANK_MATH |
| [ ] | EXE-020 | pa_volume 30/60/250 durable landing package | **BLOCKED** | exact query research + preselection verification | SL-002; DEC-026,030,077,116,117,130 | B8,H | CONTENT + RANK_MATH + WOO |
| [ ] | EXE-021 | ProductGroup/variant structured-data canary | **BLOCKED** | identifier/Offer field-source mapping | SL-002; DEC-035,039,068,081,082 | B0-010,B2/B4 | RANK_MATH FILTER + WOO |
| [ ] | EXE-022 | Bundle/set schema + visible component discoverability canary | **BLOCKED** | raw/rendered/AJAX + YITH composition evidence | SL-002; DEC-036,068,080,081,082 | B0-011,B3 | RANK_MATH + WOO/YITH + CUSTOM_CODE if required |
| [ ] | EXE-023 | Product commercial facts / identifiers consistency audit-to-fix | **BLOCKED** | targeted field mapping + actual shipping/returns rules | SL-002; DEC-081,082,083,113 | B2–B6,O-002 | WOO |
| [ ] | EXE-024 | Product Tag controlled decommission | **BLOCKED** | URL-by-URL successor map + rollback | SL-002/SL-006; DEC-027,063,067,109 | B8-001–007 | NGINX + WOO + RANK_MATH |
| [ ] | EXE-025 | Obsolete Product Categories 20/27 decommission | **BLOCKED** | operational dependency check + mapping verification | SL-002/SL-006; DEC-025,063,067 | B7/B8 | NGINX + WOO + RANK_MATH |
| [ ] | EXE-026 | Out-of-stock/discontinued lifecycle implementation rules | **BLOCKED** | identify genuinely discontinued Products | SL-002; DEC-083,109 | B2–B6 | WOO + CONTENT |
| [ ] | EXE-027 | Homepage content/CTA + metadata/schema reconciliation | **BLOCKED** | branded-query evidence for any baseline change | SL-003; DEC-002,032,053,099,100,114 | C-003–C-013 | CONTENT + RANK_MATH |
| [ ] | EXE-028 | Static/trust page metadata/content/schema package | **BLOCKED** | exact owner-supplied contact/social facts where used | SL-003; DEC-012,017,022,033,053,085,086,087,099,127 | D | CONTENT + RANK_MATH |
| [ ] | EXE-029 | Canonical brand/entity consistency implementation | **BLOCKED** | exact official handles/contact values; branded query mapping | SL-003; DEC-053,099,100,127 | N-001–N-012 | CONTENT + RANK_MATH |
| [ ] | EXE-030 | Durable Blog Category archive/content package | **BLOCKED** | final taxonomy/page-specific copy research | SL-003; DEC-028,030,051,118,121–125,130 | E0,H | CONTENT + RANK_MATH |
| [ ] | EXE-031 | Blog Tag controlled decommission | **BLOCKED** | URL-by-URL editorial successor map | SL-003/SL-006; DEC-029,063,067,109 | E0-007–012 | NGINX + WORDPRESS + RANK_MATH |
| [ ] | EXE-032 | Article metadata/freshness/content pilot | **BLOCKED** | cluster ownership + article-level evidence/copy | SL-003; DEC-013,018,023,034,044,045,049,050,068,085,088,119,121–125 | E1 | CONTENT + RANK_MATH |
| [ ] | EXE-033 | Academy Guide/Course metadata/content pilot | **BLOCKED** | current Guide vs future Course entity mapping | SL-003; DEC-014,019,024,037,043,049,068,085,088,121–125 | F0,F1 | CONTENT + RANK_MATH |
| [ ] | EXE-034 | Academy/Guide schema + VideoObject host-page canary | **BLOCKED** | two-guide host/player/video evidence | SL-003/SL-005; DEC-037,038,039,068,094–098 | F,M | RANK_MATH + CUSTOM_CODE if unsupported |
| [ ] | EXE-035 | Durable archive/hub content-block program | **BLOCKED** | exact archive list + research + copy approval | SL-002/SL-003/SL-004; DEC-021,051,117,118,130 | B0,B7,F,E,H | CONTENT |
| [ ] | EXE-036 | Semantic positioning evidence registry | **READY_FOR_TASK** | collect Product/spec/test/source evidence | SL-003; DEC-121,125,053 | A-018/A-019,N | RESEARCH / CONTENT |
| [ ] | EXE-037 | Topic/query cluster research + prioritization | **READY_FOR_TASK** | direct Search/GSC evidence | SL-003; DEC-100,121,122 | A-018,E,F,N | RESEARCH |
| [ ] | EXE-038 | Cluster → primary page-family ownership map | **BLOCKED** | joined/direct query evidence | SL-003; DEC-050,100,122,123 | A-018/A-019 | RESEARCH |
| [ ] | EXE-039 | Content-journey coverage map | **BLOCKED** | EXE-037/038 outputs | SL-003/SL-004; DEC-040–050,121–124 | E,F,B,N | RESEARCH / CONTENT |
| [ ] | EXE-040 | Product/brand claim-evidence matrix | **READY_FOR_TASK** | verified specs/tests/sources | SL-003; DEC-053,085,121,125 | B,E,F,N | RESEARCH / CONTENT |
| [ ] | EXE-041 | Parent/hub mandatory-link consistency audit + fixes | **BLOCKED** | exact source/destination matrix | SL-004; DEC-040,041,048,120 | B0-018–020,I-008/A/B | THEME/BLOCK/CUSTOM depending component |
| [ ] | EXE-042 | Cross-family Product/Category ↔ Academy/Article link pilot | **BLOCKED** | EXE-038/039 + exact destination mapping | SL-004; DEC-040,042–047,049–051,068,123,124 | B0-016–020,E,F | CONTENT + TEMPLATE as applicable |
| [ ] | EXE-043 | Header/Footer/global navigation reconciliation | **BLOCKED** | current menu inventory and exact approved hubs | SL-004; DEC-001,041,120 | C-007,I-008 | THEME/BLOCK |
| [ ] | EXE-044 | Image ALT/context representative audit + correction pilot | **BLOCKED** | representative visual review | SL-005; DEC-054,056,057,090,091,068 | L-001–L-012 | CONTENT + MEDIA/TEMPLATE |
| [ ] | EXE-045 | Responsive image delivery + LCP/CLS template canary | **BLOCKED** | mobile/desktop slot, DPR, bytes and field/lab evidence | SL-005; DEC-092,093,111,068 | C-008,L-009,I-013 | THEME/BLOCK + WP MEDIA |
| [ ] | EXE-046 | New-media filename policy implementation in upload workflow | **BLOCKED** | choose non-destructive future-upload enforcement path | SL-005; DEC-089 | L-005,L-010 | MEDIA WORKFLOW |
| [ ] | EXE-047 | Full public video inventory + metadata/thumbnail/lifecycle target map | **READY_FOR_TASK** | complete public video inventory | SL-005; DEC-038,094–098 | M-001–M-011 | RESEARCH / CONTENT |
| [ ] | EXE-048 | Video technical/schema implementation after inventory | **BLOCKED** | EXE-047 + representative host/player canary | SL-005; DEC-038,094–098,068 | M-012–M-014 | RANK_MATH + CUSTOM_CODE if unsupported |
| [ ] | EXE-049 | AI-search crawler eligibility technical verification | **READY_FOR_TASK** | actual crawler access evidence | SL-005; DEC-110,129 | I-014 | NGINX / ROBOTS / WAF |
| [ ] | EXE-050 | AI answer/citation content-research framework operationalization | **BLOCKED** | platform-specific current evidence + cluster map | SL-003/SL-005; DEC-121–125,129 | A-018/A-019,E,F,N,L,M | RESEARCH / CONTENT |
| [ ] | EXE-051 | AI/multimodal measurement instrumentation and reporting plan | **READY_FOR_TASK** | available platform data and referral observability | SL-005/SL-000; DEC-069,102–104,129 | J,L-013,M-015,N-012 | MEASUREMENT |
| [ ] | EXE-052 | Current Nginx redirect inventory + conflict/chain verification | **READY_FOR_TASK** | current server rule evidence | SL-006; DEC-063,067,109 | A-012,I-004 | NGINX |
| [ ] | EXE-053 | Historical Product-volume migration batch | **BLOCKED** | identity + current-volume verification per URL | SL-006; DEC-063,064,067 | B0-012 | NGINX + WOO |
| [ ] | EXE-054 | Historical Education → Academy verify-and-preserve batch | **READY_FOR_TASK** | current redirect rule verification incl archive/feed exceptions | SL-006; DEC-063,065,067 | F,H,I-004 | NGINX |
| [ ] | EXE-055 | Historical Artist URL migration — post-launch manual batch | **BLOCKED** | **blocked until new Artists system is public/stable** + manual identity review | SL-006; DEC-052,063,066,067 | G,I-004 | NGINX |
| [ ] | EXE-056 | Other removed-content legacy URL disposition batch | **BLOCKED** | URL-level owner/source evidence where identity unclear | SL-006; DEC-063,067,109,128 | G,H,I-004 | NGINX |
| [ ] | EXE-057 | Final sitewide technical/content/link/schema/media regression | **BLOCKED** | only after implemented packages reach QA | ALL ACTIVE LOCKS; all implemented-scope accepted DEC + DEC-069,102,103 | I-002–I-020 | QA |

## Stage-5 handoff

Stage 5 must take this exact 57-package checklist and add dependency-aware priority/Wave planning. It must preserve the 16/41 readiness classification unless new evidence closes a blocker or reveals a new blocker. Any readiness change must also be reconciled back to `tasks/EXECUTION-BACKLOG.md`.

Stage 5 must distinguish foundation/process work, evidence/research packages that unlock later packages, independent technical scopes, content/entity/link/media packages with upstream dependencies, legacy migrations with exact mapping gates, and terminal final regression.

No Codex Production execution begins merely because a package is placed in a Wave.
