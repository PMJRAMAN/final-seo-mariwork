validated blocker remains |# SEO Execution Backlog
validated blocker remains |
validated blocker remains |**Status:** P-007 VALIDATED — EXECUTION READINESS CLASSIFIED  
validated blocker remains |**Authority:** accepted decisions in `strategy/DECISION-BACKLOG.md` + active Strategy Locks  
validated blocker remains |**Reconciled:** 2026-09-26  
validated blocker remains |**Production implementation authorized by this file now:** ONLY FOR `READY_FOR_TASK` PACKAGES, AFTER TASK-LEVEL GOVERNANCE GATES
validated blocker remains |
validated blocker remains |## Governing sources
validated blocker remains |
validated blocker remains |- `docs/DECISION-TO-EXECUTION-GOVERNANCE.md`
validated blocker remains |- `strategy/DECISION-BACKLOG.md`
validated blocker remains |- `strategy/locks/README.md`
validated blocker remains |- `MASTER-TODO.md`
validated blocker remains |- `docs/SEO-OWNERSHIP.md`
validated blocker remains |
validated blocker remains |## P-006 rule
validated blocker remains |
validated blocker remains |This file is an execution package register, not a second strategy document.
validated blocker remains |
validated blocker remains |P-006 only reconciles accepted strategy into executable scopes. It does **not** promote any package to `READY_FOR_TASK`.
validated blocker remains |
validated blocker remains |Until P-007 is complete:
validated blocker remains |- every package remains `BLOCKED`;
validated blocker remains |- blocker `P-007` means execution-readiness has not yet been independently validated;
validated blocker remains |- packages with additional evidence/research/owner-input gates retain those blockers after P-007 unless satisfied.
validated blocker remains |
validated blocker remains |## Lifecycle
validated blocker remains |
validated blocker remains |Allowed execution states:
validated blocker remains |- `LOCKED_BY_DECISIONS`
validated blocker remains |- `READY_FOR_TASK`
validated blocker remains |- `TASK_ISSUED`
validated blocker remains |- `IMPLEMENTING`
validated blocker remains |- `CODEX_QA`
validated blocker remains |- `CHATGPT_FINAL_QA`
validated blocker remains |- `COMPLETE`
validated blocker remains |- `BLOCKED`
validated blocker remains |
validated blocker remains |Only `READY_FOR_TASK` may become a Production Codex task.
validated blocker remains |
validated blocker remains |---
validated blocker remains |
validated blocker remains |# A. Governance / measurement packages
validated blocker remains |
validated blocker remains || ID | Package | Strategy Lock | Decisions | MASTER refs | Primary owner | Remaining gate | State |
validated blocker remains ||---|---|---|---|---|---|---|---|
validated blocker remains || EXE-001 | Change annotation + baseline + canary framework activation | SL-000 | DEC-068,069,102,103,104,112 | I, J | REPOSITORY / PROCESS | P-007; per-package baseline design | BLOCKED |
validated blocker remains || EXE-002 | Monitoring outcome register and 28/56-day review workflow | SL-000 | DEC-069,102,103,104 | J-001–J-009 | REPOSITORY / PROCESS | P-007; metric availability by package | BLOCKED |
validated blocker remains |
validated blocker remains |# B. Core technical / system URL packages
validated blocker remains |
validated blocker remains || ID | Package | Strategy Lock | Decisions | MASTER refs | Primary owner | Remaining gate | State |
validated blocker remains ||---|---|---|---|---|---|---|---|
validated blocker remains || EXE-003 | Preferred host/protocol/trailing-slash normalization verification | SL-001 | DEC-067,078,079 | I-004–I-007 | NGINX + RANK_MATH | P-007; current Production verification | BLOCKED |
validated blocker remains || EXE-004 | Store facet/sort/display + pagination normalization | SL-001/SL-002 | DEC-059,060,061,067,079 | B9, H-008 | NGINX + RANK_MATH | P-007; exact current generator/redirect evidence | BLOCKED |
validated blocker remains || EXE-005 | General internal-search / RSS-feed / utility indexability reconciliation | SL-001 | DEC-004,074,075,107,108 | H-006,H-007,H-009–H-012 | RANK_MATH / WORDPRESS | P-007; current rendered robots/meta verification | BLOCKED |
validated blocker remains || EXE-006 | Author/date archive indexability reconciliation | SL-001/SL-003 | DEC-062,079 | H-003,H-004 | RANK_MATH | P-007; route existence verification | BLOCKED |
validated blocker remains || EXE-007 | 404/soft-404/error-page technical behavior | SL-001/SL-006 | DEC-109,067 | H-013,I-004 | NGINX + WORDPRESS | P-007; representative current response audit | BLOCKED |
validated blocker remains || EXE-008 | JS/AJAX discoverability remediation candidates | SL-001 | DEC-080,036 | B0/B3, I | CUSTOM_CODE where needed | P-007; initial-HTML/rendered-DOM/network evidence | BLOCKED |
validated blocker remains || EXE-009 | Search crawler access: Googlebot/OAI-SearchBot vs GPTBot controls | SL-001/SL-005 | DEC-110 | I-014 | NGINX / ROBOTS / WAF | P-007; actual robots/WAF/server behavior and published-bot verification | BLOCKED |
validated blocker remains || EXE-010 | Attachment HTML lifecycle + orphan-media safety reconciliation | SL-001/SL-006 | DEC-031,067,109 | H-005,L | WORDPRESS + NGINX | P-007; attachment/media dependency inventory | BLOCKED |
validated blocker remains || EXE-011 | Sitewide sitemap reconciliation | SL-001 | DEC-025,026,028,029,030,031,062,107,108 | B0-002,I-006 | RANK_MATH | P-007; exact current sitemap membership audit | BLOCKED |
validated blocker remains |
validated blocker remains |# C. Store / Product / taxonomy packages
validated blocker remains |
validated blocker remains || ID | Package | Strategy Lock | Decisions | MASTER refs | Primary owner | Remaining gate | State |
validated blocker remains ||---|---|---|---|---|---|---|---|
validated blocker remains || EXE-012 | Shop landing H1/title/meta/content-block implementation | SL-002 | DEC-003,016,114,130 | B0-001,B10 | CONTENT + RANK_MATH | P-007; current copy/placement recheck | BLOCKED |
validated blocker remains || EXE-013 | Fabric-color Product title normalization canary | SL-002 | DEC-007,011,053,068 | B0-022–025,B2 | WOO + RANK_MATH | P-007; **item-1 canonical spelling consistency fix still pending**; exact 5-URL canary | BLOCKED |
validated blocker remains || EXE-014 | Set/Bundle Product title normalization canary | SL-002 | DEC-008,011,053,068 | B0-022–025,B3 | WOO + RANK_MATH | P-007; item-1 spelling consistency fix; verified bundle identity | BLOCKED |
validated blocker remains || EXE-015 | Medium/Additive Product title normalization canary | SL-002 | DEC-009,011,053,068 | B0-022–025,B4 | WOO + RANK_MATH | P-007; item-1 spelling consistency fix; verified Product identity | BLOCKED |
validated blocker remains || EXE-016 | Tool/Accessory Product title normalization canary | SL-002 | DEC-010,011,053,068,081 | B0-022–025,B5 | WOO + RANK_MATH | P-007; exact real brand/code mapping | BLOCKED |
validated blocker remains || EXE-017 | Product meta-description remediation by family | SL-002 | DEC-015,068,121–125 | B2–B6 | CONTENT + RANK_MATH | P-007; Product facts + copy QA | BLOCKED |
validated blocker remains || EXE-018 | Product visible-content architecture remediation by family | SL-002 | DEC-020,042,083,088,121–125 | B2–B6 | CONTENT | P-007; family evidence + exact page scope | BLOCKED |
validated blocker remains || EXE-019 | Durable Product Category SEO package | SL-002 | DEC-021,025,030,046,076,115,121–125,130 | B7 | CONTENT + RANK_MATH | P-007; keyword/query research + exact copy | BLOCKED |
validated blocker remains || EXE-020 | pa_volume 30/60/250 durable landing package | SL-002 | DEC-026,030,077,116,117,130 | B8,H | CONTENT + RANK_MATH + WOO | P-007; exact query research + preselection verification | BLOCKED |
validated blocker remains || EXE-021 | ProductGroup/variant structured-data canary | SL-002 | DEC-035,039,068,081,082 | B0-010,B2/B4 | RANK_MATH FILTER + WOO | P-007; identifier/Offer field-source mapping | BLOCKED |
validated blocker remains || EXE-022 | Bundle/set schema + visible component discoverability canary | SL-002 | DEC-036,068,080,081,082 | B0-011,B3 | RANK_MATH + WOO/YITH + CUSTOM_CODE if required | P-007; raw/rendered/AJAX + YITH composition evidence | BLOCKED |
validated blocker remains || EXE-023 | Product commercial facts / identifiers consistency audit-to-fix | SL-002 | DEC-081,082,083,113 | B2–B6,O-002 | WOO | P-007; targeted field mapping + actual shipping/returns rules | BLOCKED |
validated blocker remains || EXE-024 | Product Tag controlled decommission | SL-002/SL-006 | DEC-027,063,067,109 | B8-001–007 | NGINX + WOO + RANK_MATH | P-007; URL-by-URL successor map + rollback | BLOCKED |
validated blocker remains || EXE-025 | Obsolete Product Categories 20/27 decommission | SL-002/SL-006 | DEC-025,063,067 | B7/B8 | NGINX + WOO + RANK_MATH | P-007; operational dependency check + mapping verification | BLOCKED |
validated blocker remains || EXE-026 | Out-of-stock/discontinued lifecycle implementation rules | SL-002 | DEC-083,109 | B2–B6 | WOO + CONTENT | P-007; identify genuinely discontinued Products | BLOCKED |
validated blocker remains |
validated blocker remains |# D. Homepage / brand / static / editorial / Academy packages
validated blocker remains |
validated blocker remains || ID | Package | Strategy Lock | Decisions | MASTER refs | Primary owner | Remaining gate | State |
validated blocker remains ||---|---|---|---|---|---|---|---|
validated blocker remains || EXE-027 | Homepage content/CTA + metadata/schema reconciliation | SL-003 | DEC-002,032,053,099,100,114 | C-003–C-013 | CONTENT + RANK_MATH | P-007; branded-query evidence for any baseline change | BLOCKED |
validated blocker remains || EXE-028 | Static/trust page metadata/content/schema package | SL-003 | DEC-012,017,022,033,053,085,086,087,099,127 | D | CONTENT + RANK_MATH | P-007; exact owner-supplied contact/social facts where used | BLOCKED |
validated blocker remains || EXE-029 | Canonical brand/entity consistency implementation | SL-003 | DEC-053,099,100,127 | N-001–N-012 | CONTENT + RANK_MATH | P-007; exact official handles/contact values; branded query mapping | BLOCKED |
validated blocker remains || EXE-030 | Durable Blog Category archive/content package | SL-003 | DEC-028,030,051,118,121–125,130 | E0,H | CONTENT + RANK_MATH | P-007; final taxonomy/page-specific copy research | BLOCKED |
validated blocker remains || EXE-031 | Blog Tag controlled decommission | SL-003/SL-006 | DEC-029,063,067,109 | E0-007–012 | NGINX + WORDPRESS + RANK_MATH | P-007; URL-by-URL editorial successor map | BLOCKED |
validated blocker remains || EXE-032 | Article metadata/freshness/content pilot | SL-003 | DEC-013,018,023,034,044,045,049,050,068,085,088,119,121–125 | E1 | CONTENT + RANK_MATH | P-007; cluster ownership + article-level evidence/copy | BLOCKED |
validated blocker remains || EXE-033 | Academy Guide/Course metadata/content pilot | SL-003 | DEC-014,019,024,037,043,049,068,085,088,121–125 | F0,F1 | CONTENT + RANK_MATH | P-007; current Guide vs future Course entity mapping | BLOCKED |
validated blocker remains || EXE-034 | Academy/Guide schema + VideoObject host-page canary | SL-003/SL-005 | DEC-037,038,039,068,094–098 | F,M | RANK_MATH + CUSTOM_CODE if unsupported | P-007; two-guide host/player/video evidence | BLOCKED |
validated blocker remains || EXE-035 | Durable archive/hub content-block program | SL-002/SL-003/SL-004 | DEC-021,051,117,118,130 | B0,B7,F,E,H | CONTENT | P-007; exact archive list + research + copy approval | BLOCKED |
validated blocker remains |
validated blocker remains |# E. Content-strategy research packages
validated blocker remains |
validated blocker remains || ID | Package | Strategy Lock | Decisions | MASTER refs | Primary owner | Remaining gate | State |
validated blocker remains ||---|---|---|---|---|---|---|---|
validated blocker remains || EXE-036 | Semantic positioning evidence registry | SL-003 | DEC-121,125,053 | A-018/A-019,N | RESEARCH / CONTENT | P-007; collect Product/spec/test/source evidence | BLOCKED |
validated blocker remains || EXE-037 | Topic/query cluster research + prioritization | SL-003 | DEC-100,121,122 | A-018,E,F,N | RESEARCH | P-007; direct Search/GSC evidence | BLOCKED |
validated blocker remains || EXE-038 | Cluster → primary page-family ownership map | SL-003 | DEC-050,100,122,123 | A-018/A-019 | RESEARCH | P-007; joined/direct query evidence | BLOCKED |
validated blocker remains || EXE-039 | Content-journey coverage map | SL-003/SL-004 | DEC-040–050,121–124 | E,F,B,N | RESEARCH / CONTENT | P-007; EXE-037/038 outputs | BLOCKED |
validated blocker remains || EXE-040 | Product/brand claim-evidence matrix | SL-003 | DEC-053,085,121,125 | B,E,F,N | RESEARCH / CONTENT | P-007; verified specs/tests/sources | BLOCKED |
validated blocker remains |
validated blocker remains |# F. Internal-link / navigation packages
validated blocker remains |
validated blocker remains || ID | Package | Strategy Lock | Decisions | MASTER refs | Primary owner | Remaining gate | State |
validated blocker remains ||---|---|---|---|---|---|---|---|
validated blocker remains || EXE-041 | Parent/hub mandatory-link consistency audit + fixes | SL-004 | DEC-040,041,048,120 | B0-018–020,I-008/A/B | THEME/BLOCK/CUSTOM depending component | P-007; exact source/destination matrix | BLOCKED |
validated blocker remains || EXE-042 | Cross-family Product/Category ↔ Academy/Article link pilot | SL-004 | DEC-040,042–047,049–051,068,123,124 | B0-016–020,E,F | CONTENT + TEMPLATE as applicable | P-007; EXE-038/039 + exact destination mapping | BLOCKED |
validated blocker remains || EXE-043 | Header/Footer/global navigation reconciliation | SL-004 | DEC-001,041,120 | C-007,I-008 | THEME/BLOCK | P-007; current menu inventory and exact approved hubs | BLOCKED |
validated blocker remains |
validated blocker remains |# G. Image / video / performance / AI packages
validated blocker remains |
validated blocker remains || ID | Package | Strategy Lock | Decisions | MASTER refs | Primary owner | Remaining gate | State |
validated blocker remains ||---|---|---|---|---|---|---|---|
validated blocker remains || EXE-044 | Image ALT/context representative audit + correction pilot | SL-005 | DEC-054,056,057,090,091,068 | L-001–L-012 | CONTENT + MEDIA/TEMPLATE | P-007; representative visual review | BLOCKED |
validated blocker remains || EXE-045 | Responsive image delivery + LCP/CLS template canary | SL-005 | DEC-092,093,111,068 | C-008,L-009,I-013 | THEME/BLOCK + WP MEDIA | P-007; mobile/desktop slot, DPR, bytes and field/lab evidence | BLOCKED |
validated blocker remains || EXE-046 | New-media filename policy implementation in upload workflow | SL-005 | DEC-089 | L-005,L-010 | MEDIA WORKFLOW | P-007; choose non-destructive future-upload enforcement path | BLOCKED |
validated blocker remains || EXE-047 | Full public video inventory + metadata/thumbnail/lifecycle target map | SL-005 | DEC-038,094–098 | M-001–M-011 | RESEARCH / CONTENT | P-007; complete public video inventory | BLOCKED |
validated blocker remains || EXE-048 | Video technical/schema implementation after inventory | SL-005 | DEC-038,094–098,068 | M-012–M-014 | RANK_MATH + CUSTOM_CODE if unsupported | P-007; EXE-047 + representative host/player canary | BLOCKED |
validated blocker remains || EXE-049 | AI-search crawler eligibility technical verification | SL-005 | DEC-110,129 | I-014 | NGINX / ROBOTS / WAF | P-007; actual crawler access evidence | BLOCKED |
validated blocker remains || EXE-050 | AI answer/citation content-research framework operationalization | SL-003/SL-005 | DEC-121–125,129 | A-018/A-019,E,F,N,L,M | RESEARCH / CONTENT | P-007; platform-specific current evidence + cluster map | BLOCKED |
validated blocker remains || EXE-051 | AI/multimodal measurement instrumentation and reporting plan | SL-005/SL-000 | DEC-069,102–104,129 | J,L-013,M-015,N-012 | MEASUREMENT | P-007; available platform data and referral observability | BLOCKED |
validated blocker remains |
validated blocker remains |# H. Legacy migration packages
validated blocker remains |
validated blocker remains || ID | Package | Strategy Lock | Decisions | MASTER refs | Primary owner | Remaining gate | State |
validated blocker remains ||---|---|---|---|---|---|---|---|
validated blocker remains || EXE-052 | Current Nginx redirect inventory + conflict/chain verification | SL-006 | DEC-063,067,109 | A-012,I-004 | NGINX | P-007; current server rule evidence | BLOCKED |
validated blocker remains || EXE-053 | Historical Product-volume migration batch | SL-006 | DEC-063,064,067 | B0-012 | NGINX + WOO | P-007; identity + current-volume verification per URL | BLOCKED |
validated blocker remains || EXE-054 | Historical Education → Academy verify-and-preserve batch | SL-006 | DEC-063,065,067 | F,H,I-004 | NGINX | P-007; current redirect rule verification incl archive/feed exceptions | BLOCKED |
validated blocker remains || EXE-055 | Historical Artist URL migration — post-launch manual batch | SL-006 | DEC-052,063,066,067 | G,I-004 | NGINX | P-007; **blocked until new Artists system is public/stable** + manual identity review | BLOCKED |
validated blocker remains || EXE-056 | Other removed-content legacy URL disposition batch | SL-006 | DEC-063,067,109,128 | G,H,I-004 | NGINX | P-007; URL-level owner/source evidence where identity unclear | BLOCKED |
validated blocker remains |
validated blocker remains |# I. Final regression package
validated blocker remains |
validated blocker remains || ID | Package | Strategy Lock | Decisions | MASTER refs | Primary owner | Remaining gate | State |
validated blocker remains ||---|---|---|---|---|---|---|---|
validated blocker remains || EXE-057 | Final sitewide technical/content/link/schema/media regression | ALL ACTIVE LOCKS | all implemented-scope accepted DEC + DEC-069,102,103 | I-002–I-020 | QA | P-007; only after implemented packages reach QA | BLOCKED |
validated blocker remains |
validated blocker remains |---
validated blocker remains |
validated blocker remains |# Intentionally excluded / deferred programs
validated blocker remains |
validated blocker remains |These do not enter current execution readiness:
validated blocker remains |
validated blocker remains |- DEC-071 — External PR / advertorial
validated blocker remains |- DEC-072 — Merchant Center / Free Listings
validated blocker remains |- DEC-073 — Reviews/social proof
validated blocker remains |- DEC-101 — off-site PR/entity evidence program
validated blocker remains |- DEC-105 — Google Merchant Product Feed
validated blocker remains |- DEC-106 — review/rating structured-data ownership
validated blocker remains |
validated blocker remains |They require explicit reactivation before any execution package is created.
validated blocker remains |
validated blocker remains |# P-006 reconciliation findings
validated blocker remains |
validated blocker remains |1. Old `EXE-023` dependency on superseded DEC-058 was removed; video work now depends on DEC-038 and DEC-094–098.
validated blocker remains |2. Historical Artists and other removed-content migrations are separated:
validated blocker remains |   - EXE-055 = Artist post-launch manual review;
validated blocker remains |   - EXE-056 = non-Artist removed-content disposition.
validated blocker remains |3. New accepted strategy areas absent from the old backlog now have explicit packages:
validated blocker remains |   - semantic positioning / topic clusters / page ownership / content journeys / claim evidence;
validated blocker remains |   - archive/hub content blocks;
validated blocker remains |   - responsive image sizing and CWV interaction;
validated blocker remains |   - OAI-SearchBot / AI crawler eligibility;
validated blocker remains |   - AI answer/citation content strategy and measurement;
validated blocker remains |   - social/contact fact gates are represented as blockers on brand/static work.
validated blocker remains |4. `ACCEPTED_WITH_TARGETED_EVIDENCE` decisions are not treated as execution-ready merely because policy is accepted.
validated blocker remains |5. Item 1 from the user's ordered workflow — canonical Persian spelling cleanup in old Product-title decisions — was **not performed in P-006** and remains an explicit blocker for EXE-013–015 because the user asked to proceed directly to item 2.
validated blocker remains |6. No package is promoted to `READY_FOR_TASK` during P-006.
validated blocker remains |
validated blocker remains |# P-007 validation target
validated blocker remains |
validated blocker remains |P-007 must inspect every package above and decide one of:
validated blocker remains |- promote to `READY_FOR_TASK` because all required inputs are already known;
validated blocker remains |- keep `BLOCKED` with exact evidence/research/owner-input prerequisite;
validated blocker remains |- split the package if exact safe scope cannot be expressed as one task.
validated blocker remains |
validated blocker remains |P-007 must not perform Production writes.
validated blocker remains |