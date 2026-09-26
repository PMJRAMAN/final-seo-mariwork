# FINAL EXECUTION TODO — Mariwork SEO

**Status:** P-011 RECONCILED — PRIORITY / WAVE PLAN + EXECUTION BOUNDARIES  
**Generated from:** `tasks/EXECUTION-BACKLOG.md` after P-007  
**Date:** 2026-09-26  
**Production writes authorized here:** NO  
**Codex Production tasks issued here:** NO

## Purpose

This is the final execution-control TODO derived from the 57 validated execution packages. It does not replace the Execution Backlog, Decision Backlog, Strategy Locks, or MASTER-TODO. It provides one operational checklist for the remaining planning and execution lifecycle.

Stage 5 assigns dependency-aware planning Waves and priorities. A Wave is a planning lane, not permission to execute. A checked box here means the execution package itself has ultimately completed its governed lifecycle; READY_FOR_TASK is not completion.

## State contract

- **READY_FOR_TASK**: target state is sufficiently exact for a task to be written later. Remaining gate text is task preflight/evidence collection, not permission to skip governance.
- **BLOCKED**: a real prerequisite must be closed before task issuance.
- No Codex Production task is created by this document.
- No Production write is authorized until a specific package is READY_FOR_TASK and its exact Codex task is separately written under repository governance.
- Wave/priority metadata must not silently change decisions, gates, readiness, or package scope.
- A BLOCKED package may be assigned to a future Wave, but cannot receive a Production task until its gate closes and readiness is reconciled.

## Coverage summary

- Current execution packages after P-011: **58**
- Current READY_FOR_TASK: **17**
- Current BLOCKED: **41**
- Historical P-008 freeze before P-011: **57 packages / 16 READY / 41 BLOCKED**
- Completed execution packages: **0**
- Production writes in Stage 4: **0**

## P-009 priority and Wave plan

Priority means **planning/unlock priority**, not permission to write Production.

### Wave 0 — Control plane / execution safety
**Priority: P0 foundation.** Establish the measurement, annotation, review and change-control layer before broad implementation.

- EXE-001 — Change annotation + baseline + canary framework
- EXE-002 — Monitoring outcome register / 28–56 day review workflow
- EXE-051 — AI/multimodal measurement and reporting plan

### Wave 1 — Evidence, discovery and system baselines
**Priority: P0/P1 unlockers.** Run evidence-producing packages that define current state or unlock many downstream scopes.

- EXE-036 — Semantic positioning evidence registry
- EXE-037 — Topic/query cluster research
- EXE-040 — Product/brand claim-evidence matrix
- EXE-047 — Full public video inventory
- EXE-052 — Nginx redirect inventory / chain-conflict verification
- EXE-003 — host/protocol/trailing-slash verification
- EXE-005 — utility/search/feed indexability verification
- EXE-006 — author/date archive verification
- EXE-007 — 404/soft-404 behavior
- EXE-009 — crawler access controls
- EXE-011 — sitemap reconciliation
- EXE-049 — AI-search crawler eligibility verification
- EXE-054 — Education → Academy **read-only redirect verification**
- EXE-058 — non-pa_volume Product-attribute archive inventory + decision dossier (**read-only**)

These are currently READY_FOR_TASK, but task issuance remains Stage 6 and each task retains its stated preflight.

### Wave 2 — Architecture maps and blocker closure
**Priority: P1.** Convert Wave-1 evidence plus owner inputs into exact mappings, scopes and approved target data. Most items are currently BLOCKED and stay blocked until their stated gate closes.

- EXE-004, EXE-008, EXE-010 — technical evidence/mapping closure
- EXE-012–018, EXE-021–023, EXE-026 — Product/store facts, identities, copy scope and structured-data field mapping
- EXE-027–029, EXE-033 — brand/static/Academy facts and entity mapping
- EXE-038 — cluster → primary page-family ownership
- EXE-043 — approved global navigation/hub map
- EXE-044–046 — image/media review and delivery-policy evidence
- EXE-050 — AI answer/citation research framework after cluster evidence
- EXE-053, EXE-056 — legacy identity/disposition mapping
- EXE-013–015 no longer carry the stale spelling gate; they remain blocked on verified identity/composition/code and named canary scope.

### Wave 3 — Content architecture and destination maps
**Priority: P1/P2.** Build exact page-level content and linking targets after Wave-2 ownership/evidence is available.

- EXE-019, EXE-020 — durable Product Category / volume landing targets
- EXE-030, EXE-032, EXE-035 — Blog/archive/article content targets
- EXE-039 — content-journey coverage map
- EXE-041 — parent/hub mandatory-link source→destination matrix
- EXE-042 — cross-family Product/Category ↔ Academy/Article destination map
- EXE-034 — Academy/LearnDash schema-owner + host-eligibility canary evidence closure (**no VideoObject write**)

### Wave 4 — Controlled implementation / canaries / migrations
**Priority: P2 implementation.** Only packages whose gates have closed and state has become READY_FOR_TASK may enter Stage 6 task issuance.

- EXE-012–035 as applicable after their upstream evidence/copy/mapping gates close
- EXE-041–046 after exact link/media implementation scopes close
- EXE-048 — **sole VideoObject write package** after EXE-047 and, for Academy hosts, EXE-034 owner/eligibility output
- EXE-053, EXE-056 — legacy migrations after exact identity/disposition mapping
- EXE-055 — Artist migration remains excluded from active implementation until the Artists system is public/stable and manual identity review is complete

### Wave 5 — Sitewide regression and outcome handoff
**Priority: terminal QA.**

- EXE-057 — final sitewide technical/content/link/schema/media regression, only after implemented packages reach QA
- EXE-002 monitoring workflow continues into post-change 28/56-day outcome review.

### Dependency rules

1. Wave number never overrides a package gate or state.
2. Wave 0 control-plane work precedes broad Production implementation.
3. EXE-037 feeds EXE-038; EXE-037 + EXE-038 feed EXE-039; EXE-038/039 feed EXE-042.
4. EXE-036/040 evidence feeds Product/brand/content claims and copy scopes where relevant.
5. EXE-047 precedes EXE-048.
6. EXE-052 is the redirect baseline for legacy migration work; exact per-URL identity/disposition gates still apply.
7. EXE-055 is event-gated by the public/stable Artists system, not by Wave completion.
8. EXE-057 is terminal and cannot be pulled forward.
9. A BLOCKED item that closes early may move to READY_FOR_TASK, but Stage 6 still requires an exact separately written Codex task.
10. No Wave is a bulk authorization for Production writes.

### P-011 milestone boundary

- Waves 2 and 3 are **blocker-closure / design / mapping lanes**, not implementation authorization for packages that remain BLOCKED.
- A package may enter Wave 4 implementation only after its exact gate is closed, its state is explicitly reconciled to `READY_FOR_TASK` in both the Execution Backlog and this TODO, and its write owner/scope is unambiguous.
- Evidence-only READY packages may receive read-only Stage-6 tasks without implying a later write is authorized.
- EXE-009 owns robots/WAF/server crawler-control writes; EXE-049 never writes those controls.
- EXE-034 never writes VideoObject; EXE-048 is the sole VideoObject write owner.
- DEC-130 page-family write ownership: Shop=EXE-012, Product Category=EXE-019, pa_volume=EXE-020, Blog Category=EXE-030, residual Academy/Magazine/other hubs=EXE-035.
- EXE-054 may verify before EXE-052 completes, but any redirect mutation waits for EXE-052 baseline plus URL-specific identity/disposition.
- EXE-057 remains terminal and requires a versioned completed-package/Decision/Lock manifest.



### P-013 single-write-owner boundary

Before any affected package can move from blocker-closure into implementation:

- **EXE-033 vs EXE-035:** EXE-033 owns Guide/Course entity identity, metadata and non-DEC-130 supporting content. EXE-035 is the sole writer of the DEC-130 visible hub block on the Academy archive/current Guide collection and other residual durable hubs.
- **EXE-027 vs EXE-029:** EXE-027 owns Homepage visible content, SEO metadata and Homepage WebSite/WebPage outputs. Shared Organization/sameAs/contact entity facts/schema are excluded and belong to EXE-029.
- **EXE-028 vs EXE-029:** EXE-028 owns Static/Trust visible content, SEO metadata and page-local schema. Shared Organization/sameAs/contact entity facts/schema are excluded and belong to EXE-029.
- **EXE-029:** canonical brand/entity registry + shared Organization/sameAs/contact-channel entity facts/schema only; it supplies verified facts to page-family packages and does not duplicate their visible content/meta/page-local schema writes.
- These boundary changes do not close the packages' factual/content/query gates and do not promote any package to READY_FOR_TASK.

## Final execution checklist

| Done | ID | Execution package | Current state | Gate / preflight before or inside task | Strategy | MASTER | Owner |
|---|---|---|---|---|---|---|---|
| [ ] | EXE-001 | Change annotation + baseline + canary framework activation | **READY_FOR_TASK** | per-package baseline design | SL-000; DEC-068,069,102,103,104,112 | I, J | REPOSITORY / PROCESS |
| [ ] | EXE-002 | Monitoring outcome register and 28/56-day review workflow | **READY_FOR_TASK** | metric availability by package | SL-000; DEC-069,102,103,104 | J-001–J-009 | REPOSITORY / PROCESS |
| [ ] | EXE-003 | Preferred host/protocol/trailing-slash normalization verification | **READY_FOR_TASK** | current Production verification | SL-001; DEC-067,078,079 | I-004–I-007 | NGINX + RANK_MATH |
| [ ] | EXE-004 | Store facet/sort/display + pagination normalization | **BLOCKED** | exact current generator/redirect evidence | SL-001/SL-002; DEC-059,060,061,067,079 | B9, H-008 | NGINX + RANK_MATH |
| [ ] | EXE-005 | General internal-search / RSS-feed / utility indexability evidence + reconciliation | **READY_FOR_TASK** | **first Stage-6 task must be read-only evidence**: rendered robots/meta/current behavior; any mutation requires an exact URL/family manifest, owner/capability revalidation, and a separately authorized write scope | SL-001; DEC-004,074,075,107,108 | H-006,H-007,H-009–H-012 | RANK_MATH / WORDPRESS |
| [ ] | EXE-006 | Author/date archive indexability reconciliation | **READY_FOR_TASK** | route existence verification | SL-001/SL-003; DEC-062,079 | H-003,H-004 | RANK_MATH |
| [ ] | EXE-007 | 404/soft-404/error-page behavior evidence + reconciliation | **READY_FOR_TASK** | **first Stage-6 task must be read-only evidence** on representative URLs; any mutation requires URL-level disposition plus exact status/redirect owner and a separately authorized write scope | SL-001/SL-006; DEC-109,067 | H-013,I-004 | NGINX + WORDPRESS |
| [ ] | EXE-008 | JS/AJAX discoverability remediation candidates | **BLOCKED** | initial-HTML/rendered-DOM/network evidence | SL-001; DEC-080,036 | B0/B3, I | CUSTOM_CODE where needed |
| [ ] | EXE-009 | Search-crawler control evidence: Googlebot/OAI-SearchBot vs GPTBot | **READY_FOR_TASK** | **sole owner for robots/WAF/server crawler-control changes**; first Stage-6 task is read-only current-control evidence + published-bot verification; any mutation requires an exact control diff and separately authorized write scope | SL-001/SL-005; DEC-110 | I-014 | NGINX / ROBOTS / WAF |
| [ ] | EXE-010 | Attachment HTML lifecycle + orphan-media safety reconciliation | **BLOCKED** | attachment/media dependency inventory | SL-001/SL-006; DEC-031,067,109 | H-005,L | WORDPRESS + NGINX |
| [ ] | EXE-011 | Sitewide sitemap evidence + reconciliation | **READY_FOR_TASK** | **first Stage-6 task must be read-only sitemap membership evidence**; any mutation requires an exact family/URL manifest, verified Rank Math ownership, and a separately authorized write scope | SL-001; DEC-025,026,028,029,030,031,062,107,108 | B0-002,I-006 | RANK_MATH |
| [ ] | EXE-012 | Shop landing H1/title/meta/content-block implementation | **BLOCKED** | approved Shop copy/placement + current-page recheck; **EXE-012 is the sole Shop content-block write owner under DEC-130** | SL-002; DEC-003,016,114,130 | B0-001,B10 | CONTENT + RANK_MATH |
| [ ] | EXE-013 | Fabric-color Product title normalization canary | **BLOCKED** | exact named 5-URL canary with verified color names/codes; canonical `ماری‌ورک` spelling is already resolved in Decisions | SL-002; DEC-007,011,053,068 | B0-022–025,B2 | WOO + RANK_MATH |
| [ ] | EXE-014 | Set/Bundle Product title normalization canary | **BLOCKED** | verified bundle identity/composition + named canary; canonical `ماری‌ورک` spelling is already resolved in Decisions | SL-002; DEC-008,011,053,068 | B0-022–025,B3 | WOO + RANK_MATH |
| [ ] | EXE-015 | Medium/Additive Product title normalization canary | **BLOCKED** | verified Product identity/name/code + named canary; canonical `ماری‌ورک` spelling is already resolved in Decisions | SL-002; DEC-009,011,053,068 | B0-022–025,B4 | WOO + RANK_MATH |
| [ ] | EXE-016 | Tool/Accessory Product title normalization canary | **BLOCKED** | exact real brand/code mapping | SL-002; DEC-010,011,053,068,081 | B0-022–025,B5 | WOO + RANK_MATH |
| [ ] | EXE-017 | Product meta-description remediation by family | **BLOCKED** | Product facts + copy QA | SL-002; DEC-015,068,121–125 | B2–B6 | CONTENT + RANK_MATH |
| [ ] | EXE-018 | Product visible-content architecture remediation by family | **BLOCKED** | family evidence + exact page scope | SL-002; DEC-020,042,083,088,121–125 | B2–B6 | CONTENT |
| [ ] | EXE-019 | Durable Product Category SEO package | **BLOCKED** | keyword/query research + approved exact copy; **sole Product Category content-block write owner under DEC-130** | SL-002; DEC-021,025,030,046,076,115,121–125,130 | B7 | CONTENT + RANK_MATH |
| [ ] | EXE-020 | pa_volume 30/60/250 durable landing package | **BLOCKED** | exact query research + preselection verification + approved exact copy; **sole pa_volume content-block write owner under DEC-130** | SL-002; DEC-026,030,077,116,117,130 | B8,H | CONTENT + RANK_MATH + WOO |
| [ ] | EXE-021 | ProductGroup/variant structured-data canary | **BLOCKED** | identifier/Offer field-source mapping | SL-002; DEC-035,039,068,081,082 | B0-010,B2/B4 | RANK_MATH FILTER + WOO |
| [ ] | EXE-022 | Bundle/set schema + visible component discoverability canary | **BLOCKED** | raw/rendered/AJAX + YITH composition evidence | SL-002; DEC-036,068,080,081,082 | B0-011,B3 | RANK_MATH + WOO/YITH + CUSTOM_CODE if required |
| [ ] | EXE-023 | Product commercial facts / identifiers consistency audit-to-fix | **BLOCKED** | targeted field mapping + actual shipping/returns rules | SL-002; DEC-081,082,083,113 | B2–B6,O-002 | WOO |
| [ ] | EXE-024 | Product Tag controlled decommission | **BLOCKED** | URL-by-URL successor map + rollback | SL-002/SL-006; DEC-027,063,067,109 | B8-001–007 | NGINX + WOO + RANK_MATH |
| [ ] | EXE-025 | Obsolete Product Categories 20/27 decommission | **BLOCKED** | operational dependency check + mapping verification | SL-002/SL-006; DEC-025,063,067 | B7/B8 | NGINX + WOO + RANK_MATH |
| [ ] | EXE-026 | Out-of-stock/discontinued lifecycle implementation rules | **BLOCKED** | identify genuinely discontinued Products | SL-002; DEC-083,109 | B2–B6 | WOO + CONTENT |
| [ ] | EXE-027 | Homepage content/CTA + metadata + WebSite/WebPage schema reconciliation (**shared Organization entity excluded**) | **BLOCKED** | branded-query evidence for any baseline change; **sole write owner for Homepage visible content, SEO metadata and Homepage WebSite/WebPage outputs**; consume verified canonical brand/entity facts from EXE-029; **must not write the canonical/shared Organization/sameAs/contact registry or shared Organization entity facts/schema owned by EXE-029** | SL-003; DEC-002,032,053,099,100,114 | C-003–C-013 | CONTENT + RANK_MATH |
| [ ] | EXE-028 | Static/trust page content + metadata + page-local schema package (**shared Organization entity excluded**) | **BLOCKED** | exact owner-supplied contact/social facts where used; consume the verified EXE-029 registry; **sole write owner for Static/Trust visible content, SEO metadata and role-appropriate page-local schema**; **must not write the canonical/shared Organization/sameAs/contact registry or shared Organization entity facts/schema owned by EXE-029** | SL-003; DEC-012,017,022,033,053,085,086,087,099,127 | D | CONTENT + RANK_MATH |
| [ ] | EXE-029 | Canonical brand/entity registry + shared Organization/sameAs consistency implementation | **BLOCKED** | exact official handles/contact values; branded query mapping; **sole write owner for the canonical brand/entity registry and shared Organization/sameAs/contact-channel entity facts/schema**; may supply verified facts to EXE-027/028 but **must not edit Homepage or Static/Trust visible content, H1, page SEO metadata, or page-local WebSite/WebPage/CollectionPage content/schema owned by those packages** | SL-003; DEC-053,099,100,127 | N-001–N-012 | BRAND REGISTRY + RANK_MATH SHARED ENTITY |
| [ ] | EXE-030 | Durable Blog Category archive/content package | **BLOCKED** | final taxonomy/page-specific research + approved exact copy; **sole Blog Category content-block write owner under DEC-130** | SL-003; DEC-028,030,051,118,121–125,130 | E0,H | CONTENT + RANK_MATH |
| [ ] | EXE-031 | Blog Tag controlled decommission | **BLOCKED** | URL-by-URL editorial successor map | SL-003/SL-006; DEC-029,063,067,109 | E0-007–012 | NGINX + WORDPRESS + RANK_MATH |
| [ ] | EXE-032 | Article metadata/freshness/content pilot | **BLOCKED** | cluster ownership + article-level evidence/copy | SL-003; DEC-013,018,023,034,044,045,049,050,068,085,088,119,121–125 | E1 | CONTENT + RANK_MATH |
| [ ] | EXE-033 | Academy Guide/Course entity metadata/content pilot (**DEC-130 hub block excluded**) | **BLOCKED** | current Guide vs future Course entity mapping; owns Guide/Course entity identity, metadata and non-DEC-130 supporting content; **must not write the Academy archive/Guide-collection DEC-130 visible hub block owned by EXE-035** | SL-003; DEC-014,019,024,037,043,049,068,085,088,121–125 | F0,F1 | CONTENT + RANK_MATH |
| [ ] | EXE-034 | Academy/LearnDash schema ownership + video-host eligibility canary (**no VideoObject write**) | **BLOCKED** | EXE-047 inventory + two-guide host/player/fetchability evidence; output exact Academy host/schema-owner map; **VideoObject mutation is excluded and handed to EXE-048** | SL-003/SL-005; DEC-037,038,039,068,094–098 | F,M | RANK_MATH + CUSTOM_CODE if unsupported |
| [ ] | EXE-035 | Durable archive/hub DEC-130 content-block coordination + residual-hub implementation | **BLOCKED** | deduplicated archive roster + approved copy/placement; **must not write Shop/Product Category/pa_volume/Blog Category blocks owned by EXE-012/019/020/030**; **sole write owner for the DEC-130 visible hub block on Academy archive/Guide collection, Magazine archive, and other residual durable hubs not assigned elsewhere**; must not write Guide/Course entity metadata or non-hub supporting content owned by EXE-033 | SL-002/SL-003/SL-004; DEC-021,051,117,118,130 | B0,B7,F,E,H | CONTENT |
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
| [ ] | EXE-046 | New-media filename policy implementation in upload workflow | **BLOCKED** | owner-approved non-destructive future-upload enforcement design, implementation owner and rollback; **Codex may not choose the enforcement path** | SL-005; DEC-089 | L-005,L-010 | MEDIA WORKFLOW |
| [ ] | EXE-047 | Full public video inventory + metadata/thumbnail/lifecycle target map | **READY_FOR_TASK** | complete public video inventory | SL-005; DEC-038,094–098 | M-001–M-011 | RESEARCH / CONTENT |
| [ ] | EXE-048 | VideoObject technical/schema implementation — **sole VideoObject write owner** | **BLOCKED** | EXE-047 inventory + representative host/player canary + EXE-034 Academy host/schema-owner map where Academy pages are included | SL-005; DEC-038,094–098,068 | M-012–M-014 | RANK_MATH + CUSTOM_CODE if unsupported |
| [ ] | EXE-049 | AI-search eligibility verification (**read-only; no robots/WAF writes**) | **READY_FOR_TASK** | actual platform/crawler eligibility evidence; all robots/WAF/server control mutations belong exclusively to EXE-009 | SL-005; DEC-110,129 | I-014 | RESEARCH / TECHNICAL SEO |
| [ ] | EXE-050 | AI answer/citation content-research framework operationalization | **BLOCKED** | platform-specific current evidence + cluster map | SL-003/SL-005; DEC-121–125,129 | A-018/A-019,E,F,N,L,M | RESEARCH / CONTENT |
| [ ] | EXE-051 | AI/multimodal measurement instrumentation and reporting plan | **READY_FOR_TASK** | available platform data and referral observability | SL-005/SL-000; DEC-069,102–104,129 | J,L-013,M-015,N-012 | MEASUREMENT |
| [ ] | EXE-052 | Current Nginx redirect inventory + conflict/chain verification | **READY_FOR_TASK** | current server rule evidence | SL-006; DEC-063,067,109 | A-012,I-004 | NGINX |
| [ ] | EXE-053 | Historical Product-volume migration batch | **BLOCKED** | identity + current-volume verification per URL | SL-006; DEC-063,064,067 | B0-012 | NGINX + WOO |
| [ ] | EXE-054 | Historical Education → Academy verify-and-preserve batch | **READY_FOR_TASK** | **initial Stage-6 task is read-only verification** incl archive/feed exceptions; any redirect mutation requires EXE-052 baseline complete + URL-specific identity/disposition + separately authorized write scope | SL-006; DEC-063,065,067 | F,H,I-004 | NGINX |
| [ ] | EXE-055 | Historical Artist URL migration — post-launch manual batch | **BLOCKED** | **blocked until new Artists system is public/stable** + manual identity review | SL-006; DEC-052,063,066,067 | G,I-004 | NGINX |
| [ ] | EXE-056 | Other removed-content legacy URL disposition batch | **BLOCKED** | URL-level owner/source evidence where identity unclear | SL-006; DEC-063,067,109,128 | G,H,I-004 | NGINX |
| [ ] | EXE-057 | Final sitewide technical/content/link/schema/media regression | **BLOCKED** | only after implemented packages reach QA **and a versioned completed-package + Decision + Lock regression manifest is frozen for the run** | ALL ACTIVE LOCKS; all implemented-scope accepted DEC + DEC-069,102,103 | I-002–I-020 | QA |
| [ ] | EXE-058 | Non-pa_volume Product-attribute archive inventory + decision dossier (**read-only**) | **READY_FOR_TASK** | inventory all public/nonpublic Product attribute archives except pa_volume; record robots/sitemap/internal-link/current-use evidence and produce per-attribute decision dossier; **no indexability/redirect/canonical mutation until a later accepted per-family decision** | SL-002; DEC-006 | B8-008–B8-010 | RESEARCH / RANK_MATH EVIDENCE |

## Stage-6 handoff

P-009 is complete. The next planning action is not bulk execution. For any individual package that is actually READY_FOR_TASK, Stage 6 writes a precise Codex task referencing its Program/Task ID, entity/batch, prerequisite status, expected dossier/change outputs, Google basis, SEO owner, acceptance criteria, rollback/canary requirements, and the next TODO item unlocked.

After P-011 reconciliation the current inventory is **58 packages: 17 READY_FOR_TASK / 41 BLOCKED**. The original P-009 freeze was 57 packages / 16 READY / 41 BLOCKED. P-011 performs no Production write and issues no Production implementation task.
