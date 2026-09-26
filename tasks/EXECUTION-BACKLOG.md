# SEO Execution Backlog

**Status:** P-007 VALIDATED — EXECUTION READINESS CLASSIFIED  
**Authority:** accepted decisions in `strategy/DECISION-BACKLOG.md` + active Strategy Locks  
**Reconciled:** 2026-09-26  
**Production implementation authorized by this file now:** ONLY FOR READY_FOR_TASK PACKAGES, AFTER TASK-LEVEL GOVERNANCE GATES

## Governing sources

- `docs/DECISION-TO-EXECUTION-GOVERNANCE.md`
- `strategy/DECISION-BACKLOG.md`
- `strategy/locks/README.md`
- `MASTER-TODO.md`
- `docs/SEO-OWNERSHIP.md`

## P-006 / P-007 rule

P-006 reconciled accepted strategy into executable scopes without promotion. P-007 independently validated all 57 packages.

P-007 distinguishes a true unresolved prerequisite from task-level preflight. A package is READY_FOR_TASK only when its accepted target state is sufficiently exact that Codex does not need to invent strategy, final copy, identity mapping, business facts, destinations, or implementation policy. Current-state verification may remain mandatory task preflight when it cannot change the accepted target state.

READY_FOR_TASK does not authorize a blind write. Generated tasks must still satisfy Change Dossier, backup/rollback, canary, acceptance criteria, Codex QA, ChatGPT Final QA, and immediate Production recheck requirements.
## Lifecycle

Allowed execution states:
- `LOCKED_BY_DECISIONS`
- `READY_FOR_TASK`
- `TASK_ISSUED`
- `IMPLEMENTING`
- `CODEX_QA`
- `CHATGPT_FINAL_QA`
- `COMPLETE`
- `BLOCKED`

Only `READY_FOR_TASK` may become a Production Codex task.

---

# A. Governance / measurement packages

| ID | Package | Strategy Lock | Decisions | MASTER refs | Primary owner | Remaining gate | State |
|---|---|---|---|---|---|---|---|
| EXE-001 | Change annotation + baseline + canary framework activation | SL-000 | DEC-068,069,102,103,104,112 | I, J | REPOSITORY / PROCESS | per-package baseline design | READY_FOR_TASK |
| EXE-002 | Monitoring outcome register and 28/56-day review workflow | SL-000 | DEC-069,102,103,104 | J-001–J-009 | REPOSITORY / PROCESS | metric availability by package | READY_FOR_TASK |

# B. Core technical / system URL packages

| ID | Package | Strategy Lock | Decisions | MASTER refs | Primary owner | Remaining gate | State |
|---|---|---|---|---|---|---|---|
| EXE-003 | Preferred host/protocol/trailing-slash normalization verification | SL-001 | DEC-067,078,079 | I-004–I-007 | NGINX + RANK_MATH | current Production verification | READY_FOR_TASK |
| EXE-004 | Store facet/sort/display + pagination normalization | SL-001/SL-002 | DEC-059,060,061,067,079 | B9, H-008 | NGINX + RANK_MATH | exact current generator/redirect evidence | BLOCKED |
| EXE-005 | General internal-search / RSS-feed / utility indexability reconciliation | SL-001 | DEC-004,074,075,107,108 | H-006,H-007,H-009–H-012 | RANK_MATH / WORDPRESS | current rendered robots/meta verification | READY_FOR_TASK |
| EXE-006 | Author/date archive indexability reconciliation | SL-001/SL-003 | DEC-062,079 | H-003,H-004 | RANK_MATH | route existence verification | READY_FOR_TASK |
| EXE-007 | 404/soft-404/error-page technical behavior | SL-001/SL-006 | DEC-109,067 | H-013,I-004 | NGINX + WORDPRESS | representative current response audit | READY_FOR_TASK |
| EXE-008 | JS/AJAX discoverability remediation candidates | SL-001 | DEC-080,036 | B0/B3, I | CUSTOM_CODE where needed | initial-HTML/rendered-DOM/network evidence | BLOCKED |
| EXE-009 | Search crawler access: Googlebot/OAI-SearchBot vs GPTBot controls | SL-001/SL-005 | DEC-110 | I-014 | NGINX / ROBOTS / WAF | actual robots/WAF/server behavior and published-bot verification | READY_FOR_TASK |
| EXE-010 | Attachment HTML lifecycle + orphan-media safety reconciliation | SL-001/SL-006 | DEC-031,067,109 | H-005,L | WORDPRESS + NGINX | attachment/media dependency inventory | BLOCKED |
| EXE-011 | Sitewide sitemap reconciliation | SL-001 | DEC-025,026,028,029,030,031,062,107,108 | B0-002,I-006 | RANK_MATH | exact current sitemap membership audit | READY_FOR_TASK |

# C. Store / Product / taxonomy packages

| ID | Package | Strategy Lock | Decisions | MASTER refs | Primary owner | Remaining gate | State |
|---|---|---|---|---|---|---|---|
| EXE-012 | Shop landing H1/title/meta/content-block implementation | SL-002 | DEC-003,016,114,130 | B0-001,B10 | CONTENT + RANK_MATH | current copy/placement recheck | BLOCKED |
| EXE-013 | Fabric-color Product title normalization canary | SL-002 | DEC-007,011,053,068 | B0-022–025,B2 | WOO + RANK_MATH | **item-1 canonical spelling consistency fix still pending**; exact 5-URL canary | BLOCKED |
| EXE-014 | Set/Bundle Product title normalization canary | SL-002 | DEC-008,011,053,068 | B0-022–025,B3 | WOO + RANK_MATH | item-1 spelling consistency fix; verified bundle identity | BLOCKED |
| EXE-015 | Medium/Additive Product title normalization canary | SL-002 | DEC-009,011,053,068 | B0-022–025,B4 | WOO + RANK_MATH | item-1 spelling consistency fix; verified Product identity | BLOCKED |
| EXE-016 | Tool/Accessory Product title normalization canary | SL-002 | DEC-010,011,053,068,081 | B0-022–025,B5 | WOO + RANK_MATH | exact real brand/code mapping | BLOCKED |
| EXE-017 | Product meta-description remediation by family | SL-002 | DEC-015,068,121–125 | B2–B6 | CONTENT + RANK_MATH | Product facts + copy QA | BLOCKED |
| EXE-018 | Product visible-content architecture remediation by family | SL-002 | DEC-020,042,083,088,121–125 | B2–B6 | CONTENT | family evidence + exact page scope | BLOCKED |
| EXE-019 | Durable Product Category SEO package | SL-002 | DEC-021,025,030,046,076,115,121–125,130 | B7 | CONTENT + RANK_MATH | keyword/query research + exact copy | BLOCKED |
| EXE-020 | pa_volume 30/60/250 durable landing package | SL-002 | DEC-026,030,077,116,117,130 | B8,H | CONTENT + RANK_MATH + WOO | exact query research + preselection verification | BLOCKED |
| EXE-021 | ProductGroup/variant structured-data canary | SL-002 | DEC-035,039,068,081,082 | B0-010,B2/B4 | RANK_MATH FILTER + WOO | identifier/Offer field-source mapping | BLOCKED |
| EXE-022 | Bundle/set schema + visible component discoverability canary | SL-002 | DEC-036,068,080,081,082 | B0-011,B3 | RANK_MATH + WOO/YITH + CUSTOM_CODE if required | raw/rendered/AJAX + YITH composition evidence | BLOCKED |
| EXE-023 | Product commercial facts / identifiers consistency audit-to-fix | SL-002 | DEC-081,082,083,113 | B2–B6,O-002 | WOO | targeted field mapping + actual shipping/returns rules | BLOCKED |
| EXE-024 | Product Tag controlled decommission | SL-002/SL-006 | DEC-027,063,067,109 | B8-001–007 | NGINX + WOO + RANK_MATH | URL-by-URL successor map + rollback | BLOCKED |
| EXE-025 | Obsolete Product Categories 20/27 decommission | SL-002/SL-006 | DEC-025,063,067 | B7/B8 | NGINX + WOO + RANK_MATH | operational dependency check + mapping verification | BLOCKED |
| EXE-026 | Out-of-stock/discontinued lifecycle implementation rules | SL-002 | DEC-083,109 | B2–B6 | WOO + CONTENT | identify genuinely discontinued Products | BLOCKED |

# D. Homepage / brand / static / editorial / Academy packages

| ID | Package | Strategy Lock | Decisions | MASTER refs | Primary owner | Remaining gate | State |
|---|---|---|---|---|---|---|---|
| EXE-027 | Homepage content/CTA + metadata/schema reconciliation | SL-003 | DEC-002,032,053,099,100,114 | C-003–C-013 | CONTENT + RANK_MATH | branded-query evidence for any baseline change | BLOCKED |
| EXE-028 | Static/trust page metadata/content/schema package | SL-003 | DEC-012,017,022,033,053,085,086,087,099,127 | D | CONTENT + RANK_MATH | exact owner-supplied contact/social facts where used | BLOCKED |
| EXE-029 | Canonical brand/entity consistency implementation | SL-003 | DEC-053,099,100,127 | N-001–N-012 | CONTENT + RANK_MATH | exact official handles/contact values; branded query mapping | BLOCKED |
| EXE-030 | Durable Blog Category archive/content package | SL-003 | DEC-028,030,051,118,121–125,130 | E0,H | CONTENT + RANK_MATH | final taxonomy/page-specific copy research | BLOCKED |
| EXE-031 | Blog Tag controlled decommission | SL-003/SL-006 | DEC-029,063,067,109 | E0-007–012 | NGINX + WORDPRESS + RANK_MATH | URL-by-URL editorial successor map | BLOCKED |
| EXE-032 | Article metadata/freshness/content pilot | SL-003 | DEC-013,018,023,034,044,045,049,050,068,085,088,119,121–125 | E1 | CONTENT + RANK_MATH | cluster ownership + article-level evidence/copy | BLOCKED |
| EXE-033 | Academy Guide/Course metadata/content pilot | SL-003 | DEC-014,019,024,037,043,049,068,085,088,121–125 | F0,F1 | CONTENT + RANK_MATH | current Guide vs future Course entity mapping | BLOCKED |
| EXE-034 | Academy/Guide schema + VideoObject host-page canary | SL-003/SL-005 | DEC-037,038,039,068,094–098 | F,M | RANK_MATH + CUSTOM_CODE if unsupported | two-guide host/player/video evidence | BLOCKED |
| EXE-035 | Durable archive/hub content-block program | SL-002/SL-003/SL-004 | DEC-021,051,117,118,130 | B0,B7,F,E,H | CONTENT | exact archive list + research + copy approval | BLOCKED |

# E. Content-strategy research packages

| ID | Package | Strategy Lock | Decisions | MASTER refs | Primary owner | Remaining gate | State |
|---|---|---|---|---|---|---|---|
| EXE-036 | Semantic positioning evidence registry | SL-003 | DEC-121,125,053 | A-018/A-019,N | RESEARCH / CONTENT | collect Product/spec/test/source evidence | READY_FOR_TASK |
| EXE-037 | Topic/query cluster research + prioritization | SL-003 | DEC-100,121,122 | A-018,E,F,N | RESEARCH | direct Search/GSC evidence | READY_FOR_TASK |
| EXE-038 | Cluster → primary page-family ownership map | SL-003 | DEC-050,100,122,123 | A-018/A-019 | RESEARCH | joined/direct query evidence | BLOCKED |
| EXE-039 | Content-journey coverage map | SL-003/SL-004 | DEC-040–050,121–124 | E,F,B,N | RESEARCH / CONTENT | EXE-037/038 outputs | BLOCKED |
| EXE-040 | Product/brand claim-evidence matrix | SL-003 | DEC-053,085,121,125 | B,E,F,N | RESEARCH / CONTENT | verified specs/tests/sources | READY_FOR_TASK |

# F. Internal-link / navigation packages

| ID | Package | Strategy Lock | Decisions | MASTER refs | Primary owner | Remaining gate | State |
|---|---|---|---|---|---|---|---|
| EXE-041 | Parent/hub mandatory-link consistency audit + fixes | SL-004 | DEC-040,041,048,120 | B0-018–020,I-008/A/B | THEME/BLOCK/CUSTOM depending component | exact source/destination matrix | BLOCKED |
| EXE-042 | Cross-family Product/Category ↔ Academy/Article link pilot | SL-004 | DEC-040,042–047,049–051,068,123,124 | B0-016–020,E,F | CONTENT + TEMPLATE as applicable | EXE-038/039 + exact destination mapping | BLOCKED |
| EXE-043 | Header/Footer/global navigation reconciliation | SL-004 | DEC-001,041,120 | C-007,I-008 | THEME/BLOCK | current menu inventory and exact approved hubs | BLOCKED |

# G. Image / video / performance / AI packages

| ID | Package | Strategy Lock | Decisions | MASTER refs | Primary owner | Remaining gate | State |
|---|---|---|---|---|---|---|---|
| EXE-044 | Image ALT/context representative audit + correction pilot | SL-005 | DEC-054,056,057,090,091,068 | L-001–L-012 | CONTENT + MEDIA/TEMPLATE | representative visual review | BLOCKED |
| EXE-045 | Responsive image delivery + LCP/CLS template canary | SL-005 | DEC-092,093,111,068 | C-008,L-009,I-013 | THEME/BLOCK + WP MEDIA | mobile/desktop slot, DPR, bytes and field/lab evidence | BLOCKED |
| EXE-046 | New-media filename policy implementation in upload workflow | SL-005 | DEC-089 | L-005,L-010 | MEDIA WORKFLOW | choose non-destructive future-upload enforcement path | BLOCKED |
| EXE-047 | Full public video inventory + metadata/thumbnail/lifecycle target map | SL-005 | DEC-038,094–098 | M-001–M-011 | RESEARCH / CONTENT | complete public video inventory | READY_FOR_TASK |
| EXE-048 | Video technical/schema implementation after inventory | SL-005 | DEC-038,094–098,068 | M-012–M-014 | RANK_MATH + CUSTOM_CODE if unsupported | EXE-047 + representative host/player canary | BLOCKED |
| EXE-049 | AI-search crawler eligibility technical verification | SL-005 | DEC-110,129 | I-014 | NGINX / ROBOTS / WAF | actual crawler access evidence | READY_FOR_TASK |
| EXE-050 | AI answer/citation content-research framework operationalization | SL-003/SL-005 | DEC-121–125,129 | A-018/A-019,E,F,N,L,M | RESEARCH / CONTENT | platform-specific current evidence + cluster map | BLOCKED |
| EXE-051 | AI/multimodal measurement instrumentation and reporting plan | SL-005/SL-000 | DEC-069,102–104,129 | J,L-013,M-015,N-012 | MEASUREMENT | available platform data and referral observability | READY_FOR_TASK |

# H. Legacy migration packages

| ID | Package | Strategy Lock | Decisions | MASTER refs | Primary owner | Remaining gate | State |
|---|---|---|---|---|---|---|---|
| EXE-052 | Current Nginx redirect inventory + conflict/chain verification | SL-006 | DEC-063,067,109 | A-012,I-004 | NGINX | current server rule evidence | READY_FOR_TASK |
| EXE-053 | Historical Product-volume migration batch | SL-006 | DEC-063,064,067 | B0-012 | NGINX + WOO | identity + current-volume verification per URL | BLOCKED |
| EXE-054 | Historical Education → Academy verify-and-preserve batch | SL-006 | DEC-063,065,067 | F,H,I-004 | NGINX | current redirect rule verification incl archive/feed exceptions | READY_FOR_TASK |
| EXE-055 | Historical Artist URL migration — post-launch manual batch | SL-006 | DEC-052,063,066,067 | G,I-004 | NGINX | **blocked until new Artists system is public/stable** + manual identity review | BLOCKED |
| EXE-056 | Other removed-content legacy URL disposition batch | SL-006 | DEC-063,067,109,128 | G,H,I-004 | NGINX | URL-level owner/source evidence where identity unclear | BLOCKED |

# I. Final regression package

| ID | Package | Strategy Lock | Decisions | MASTER refs | Primary owner | Remaining gate | State |
|---|---|---|---|---|---|---|---|
| EXE-057 | Final sitewide technical/content/link/schema/media regression | ALL ACTIVE LOCKS | all implemented-scope accepted DEC + DEC-069,102,103 | I-002–I-020 | QA | only after implemented packages reach QA | BLOCKED |

---

# Intentionally excluded / deferred programs

These do not enter current execution readiness:

- DEC-071 — External PR / advertorial
- DEC-072 — Merchant Center / Free Listings
- DEC-073 — Reviews/social proof
- DEC-101 — off-site PR/entity evidence program
- DEC-105 — Google Merchant Product Feed
- DEC-106 — review/rating structured-data ownership

They require explicit reactivation before any execution package is created.

# P-006 reconciliation findings

1. Old `EXE-023` dependency on superseded DEC-058 was removed; video work now depends on DEC-038 and DEC-094–098.
2. Historical Artists and other removed-content migrations are separated:
   - EXE-055 = Artist post-launch manual review;
   - EXE-056 = non-Artist removed-content disposition.
3. New accepted strategy areas absent from the old backlog now have explicit packages:
   - semantic positioning / topic clusters / page ownership / content journeys / claim evidence;
   - archive/hub content blocks;
   - responsive image sizing and CWV interaction;
   - OAI-SearchBot / AI crawler eligibility;
   - AI answer/citation content strategy and measurement;
   - social/contact fact gates are represented as blockers on brand/static work.
4. `ACCEPTED_WITH_TARGETED_EVIDENCE` decisions are not treated as execution-ready merely because policy is accepted.
5. Item 1 from the user's ordered workflow — canonical Persian spelling cleanup in old Product-title decisions — was **not performed in P-006** and remains an explicit blocker for EXE-013–015 because the user asked to proceed directly to item 2.
6. No package is promoted to `READY_FOR_TASK` during P-006.

# P-007 validation result

Validated: 2026-09-26.

- Packages inspected: **57 / 57**.
- READY_FOR_TASK: **16**.
- BLOCKED: **41**.
- Production writes performed during P-007: **0**.
- Package splits required now: **0**.

## READY_FOR_TASK set

EXE-001, EXE-002, EXE-003, EXE-005, EXE-006, EXE-007, EXE-009, EXE-011, EXE-036, EXE-037, EXE-040, EXE-047, EXE-049, EXE-051, EXE-052, EXE-054.

These packages have an accepted target state exact enough for task generation. Any remaining current-state check is mandatory task preflight or is itself the non-destructive purpose of the package.

## BLOCKED classes

The remaining 41 packages retain real prerequisites such as final visible-copy approval, exact Product/entity facts, query/cluster or page-ownership outputs, exact source-to-destination link mapping, exact redirect/successor identity mapping, component/variant/YITH field mapping, owner-supplied business/contact/social facts, responsive-image measurements that determine implementation, media dependency inventory, or an upstream package output.

Special blockers preserved:
- EXE-013–015: canonical ماری ورک → ماری‌ورک consistency cleanup remains pending by explicit owner sequencing.
- EXE-055: Artists migration remains blocked until the new Artists system is public/stable and manual identity review is possible.
- EXE-057: final regression remains blocked until implemented packages reach QA.

P-007 performed no Production writes and created no Codex Production tasks. Task generation is the next governed step for selected READY_FOR_TASK packages.
