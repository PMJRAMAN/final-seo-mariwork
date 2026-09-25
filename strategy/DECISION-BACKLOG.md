# SEO Decision Backlog

**Purpose:** canonical queue of strategy/target-state decisions before Production implementation  
**Authority:** owner + ChatGPT  
**Codex authority:** evidence collection only; Codex cannot mark decisions `ACCEPTED`  
**Baseline:** SR-004 + SR-005 and current audit repository  
**Production implementation authorized by this file:** NO

See: `docs/DECISION-TO-EXECUTION-GOVERNANCE.md`.

## Status legend

- `OPEN` — requires discussion.
- `DISCUSSING` — currently under owner + ChatGPT review.
- `NEEDS_TARGETED_EVIDENCE` — requires a narrow evidence check first.
- `PROPOSED` — Second Review has a target direction; owner approval pending.
- `ACCEPTED` — owner-approved target state.
- `DEFERRED` — intentionally postponed; does not block unrelated scopes.
- `REJECTED`
- `SUPERSEDED`

## Working method

We will work through this backlog topic by topic over multiple sessions.

After each discussion:
1. record the decision;
2. update status;
3. record exact target state and exceptions;
4. identify implementation dependencies;
5. do **not** send a Production task to Codex until the required Decision IDs are accepted and an Execution Backlog item becomes `READY_FOR_TASK`.

---

# Session 1 — Site roles, indexability and architecture

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-001 | Approve durable site-family roles: Homepage, Shop, Product Categories, Products, Academy, Magazine/Articles, durable Blog Categories, Static trust/support | PROPOSED | SR-005 §4–15; CONTENT-ARCHITECTURE | Foundation for linking/content decisions |
| DEC-002 | Decide final Homepage role and whether current title/H1/meta remain the baseline | PROPOSED | WP-63; SR-005 §4 | Current state is coherent; no rewrite required by audit |
| DEC-003 | Decide Shop target state: H1, visible role, title/meta and relationship to Product Categories | PROPOSED | SR-004 SR-ST-001; WP-30918 | Required before Shop implementation |
| DEC-004 | Decide utility-page policy for Login, Fast Buy, Cart, Checkout and My Account | PROPOSED | SR-005 §5–6; WP-10/11/30919 | Proposed: utility/noindex where current role requires it |
| DEC-005 | Decide public role of current LearnDash Course Categories currently returning 404 | NEEDS_TARGETED_EVIDENCE | SR-005 §11; current SEO output | Verify whether terms are operationally needed before lifecycle decision |
| DEC-006 | Decide durable vs transitional taxonomy architecture at site level | PROPOSED | SR-005; tag/category reconciliation | Product Tags and Blog Tags proposed transitional |

# Session 2 — Titles, H1s and naming standards

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-007 | Product Title Naming Standard — fabric colors | OPEN | SR-004 SR-ST-002; current-title-h1-matrix | Decide product type, color name, «ماری ورک», code, numeral/separator rules |
| DEC-008 | Product Title Naming Standard — sets/bundles | OPEN | SR-004 SR-ST-002; bundle matrix | Decide count/type/volume order; move long composition clauses out of title |
| DEC-009 | Product Title Naming Standard — mediums/additives | OPEN | SR-004 SR-ST-002 | Decide exact naming and code policy |
| DEC-010 | Product Title Naming Standard — tools/accessories | OPEN | SR-004 SR-ST-002 | Decide brand/code exceptions |
| DEC-011 | Decide relationship between visible Product H1/title and Rank Math SEO title template | OPEN | SR-004 SR-ST-002; Rank Math ownership | Template decision must follow visible-title standard |
| DEC-012 | Static/Core title and H1 policy | OPEN | SR-005 §5; current SEO output | Includes About, Contact, Stores, FAQ, Magazine, Why Mariwork |
| DEC-013 | Article title/H1 conventions | OPEN | 12 article dossiers; current output | Preserve natural informational titles; avoid mechanical keyword repetition |
| DEC-014 | Academy course/lesson title/H1 conventions | OPEN | course + 37 lesson dossiers | Keep instructional clarity; decide brand suffix/template behavior |

# Session 3 — Meta descriptions and visible content

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-015 | Product meta-description strategy | PROPOSED | SR-004 SR-ST-003 | Proposed: explicit factual descriptions; no Yoast reconstruction; prioritize broken/repeated/long descriptions |
| DEC-016 | Product Category / Shop / volume landing meta strategy | OPEN | SR-004 SR-ST-001/006/007 | Decide explicit metadata vs templates and content source |
| DEC-017 | Static/Core meta-description strategy | PROPOSED | SR-005 §5 | Magazine missing; several pages have weak generic descriptions |
| DEC-018 | Article meta-description update rule | OPEN | current article output | Decide when to retain, shorten, fact-check or rewrite |
| DEC-019 | Academy course/lesson meta-description rule | OPEN | current course/lesson output | Decide family template vs page-specific copy |
| DEC-020 | Product-page visible content architecture by family | OPEN | CONTENT-ARCHITECTURE; product dossiers | Decide required facts/modules for colors, sets, mediums, tools |
| DEC-021 | Product Category visible intro/content policy | OPEN | SR-004 SR-ST-006 | No word-count padding; define useful minimum role |
| DEC-022 | Static/trust page content policy | OPEN | static dossiers | Decide what About/Why/Contact/Stores/FAQ should contain and what not to expand |
| DEC-023 | Article update/freshness/fact-check policy | PROPOSED | SR-005 §7; article dossiers | Includes safety/technical claims such as WP-13295 |
| DEC-024 | Academy lesson/course content standard | OPEN | education dossiers | Decide instructional structure, prerequisites/materials, summary/transcript where useful |

# Session 4 — Taxonomies, sitemap and lifecycle

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-025 | Durable Product Category set and sitemap/index policy | PROPOSED | SR-004 SR-ST-006; taxonomy reconciliation | Durable categories proposed indexable; migration categories 20/27 decommission candidates |
| DEC-026 | `pa_volume` 30/60/250 archive role, indexability and sitemap policy | NEEDS_TARGETED_EVIDENCE | SR-005 §13; current-volume-architecture | Must prove distinct user value/navigation role before sitemap approval |
| DEC-027 | Product Tags decommission policy and mapping rule | PROPOSED | SR-004 SR-ST-010; 275 zero assignments | Controlled migration; no per-tag optimization |
| DEC-028 | Blog Categories lifecycle | PROPOSED | SR-005 §8; current-blog-category-matrix | Articles + History durable; empty categories need individual lifecycle |
| DEC-029 | Blog Tags decommission policy and mapping rule | PROPOSED | SR-005 §9; tag reconciliation | Six assigned terms / 39 assignments require cleanup first |
| DEC-030 | Sitewide sitemap membership policy by family | OPEN | current sitemap evidence; SR-004/SR-005 | Must follow accepted family/indexability decisions |
| DEC-031 | Attachment/media URL public/index policy | NEEDS_TARGETED_EVIDENCE | SYSTEM-URL-SPACES-CLOSURE; image summary | Current attachment count discrepancy requires representative verification |

# Session 5 — Structured data / technical ownership

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-032 | Homepage Organization/WebSite/WebPage schema target | PROPOSED | SR-005 §4; current SEO output | Keep one owner; SearchAction low priority / retired sitelinks-search-box relevance |
| DEC-033 | Static/Core WordPress Page schema policy | PROPOSED | SYS-016; SR-005 §5 | Proposed: remove generic Article default where semantics do not fit |
| DEC-034 | Article schema policy | PROPOSED | SR-005 §7; current BlogPosting output | Current BlogPosting generally coherent |
| DEC-035 | Product variation ProductGroup/variant schema architecture | PROPOSED | SR-004 SR-ST-004; variable-schema matrix | Canary required; Rank Math extension only if Free lacks capability |
| DEC-036 | Bundle/set schema and visible component representation | PROPOSED | SR-004 SR-ST-005; bundle matrix | Bundle remains Product/Offer, not ProductGroup |
| DEC-037 | Academy/LearnDash schema owner and canary | PROPOSED | SYS-017; SR-005 §10 | One course + two representative video lessons proposed |
| DEC-038 | VideoObject eligibility/ownership policy for lessons and other videos | NEEDS_TARGETED_EVIDENCE | SR-005 §10; MASTER-TODO M | Requires video inventory/fetchability facts before broad rule |
| DEC-039 | Breadcrumb structured-data policy across Store/Academy/content | OPEN | current output + hierarchy | Use only where visible hierarchy is accurate |

# Session 6 — Internal-link architecture

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-040 | Approve CORE_MANDATORY / FAMILY_SPECIFIC / CONTEXTUAL_OPTIONAL model | PROPOSED | SR-005 §17; link matrix draft | Framework approved in Second Review; owner approval pending |
| DEC-041 | Exact mandatory parent/hub links by family | OPEN | INTERNAL-LINK-REQUIREMENT-MATRIX-DRAFT | Requires exact durable destinations |
| DEC-042 | Product → Academy/Article rules | OPEN | SR-004 SR-ST-009; current graph | Only real preparation/technique/care relevance |
| DEC-043 | Academy/Lesson → Product/Category rules | OPEN | SR-004 SR-ST-009 | Only when material/tool is actually used |
| DEC-044 | Article → Product/Category rules | OPEN | SR-005 §17 | Commercial next step only when useful/contextual |
| DEC-045 | Article → Article / Article → Academy relationship | PROPOSED | SR-005 §17 | Related Article should not be mandatory on every Article |
| DEC-046 | Category → education/reference links | OPEN | SR-004/SR-005 | Define selected hubs, not generic footer duplication |
| DEC-047 | Anchor-text policy | OPEN | CONTENT-RESEARCH-SPEC; Page+Query limitation | Natural descriptive anchors; no invented query-target anchors |
| DEC-048 | Orphan/underlinked thresholds and approved exceptions | OPEN | current graph | Resolver gaps are not broken-link count |

# Session 7 — Content-family boundaries and information architecture

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-049 | Article vs Academy intent boundary | OPEN | article + Academy dossiers; CONTENT-ARCHITECTURE | Decide when content stays reference vs structured lesson |
| DEC-050 | Product vs Category vs Article query/content role boundary | OPEN | CONTENT-ARCHITECTURE; SR-004 | Page+Query unavailable; use user intent + SERP research where needed |
| DEC-051 | Magazine hub and Blog Category hierarchy | OPEN | WP-70; categories 71/142 | Decide Magazine role and category visibility/navigation |
| DEC-052 | History / Artists content strategy | NEEDS_TARGETED_EVIDENCE | legacy map; category state; current census | Current historical Artist URLs are not current public entities |
| DEC-053 | Brand/trust content and canonical Mariwork facts | OPEN | Homepage/About/Why Mariwork; MASTER-TODO N | Facts must be verified before entity/brand consistency work |

# Session 8 — Images and video

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-054 | ALT policy by image role | PROPOSED | SYS-015; IMAGE-ALT-AUDIT-SUMMARY | Informative vs decorative first; no keyword stuffing |
| DEC-055 | Family-level image sampling and rollout method | PROPOSED | SR-005 §18 | Start representative visual review rather than mass fill |
| DEC-056 | Product image/gallery SEO policy | NEEDS_TARGETED_EVIDENCE | Store evidence + MASTER-TODO L | Requires visual/primary-image review |
| DEC-057 | Article/Academy instructional image policy | NEEDS_TARGETED_EVIDENCE | SYS-010/011 | Visual-purpose review required |
| DEC-058 | Video inventory, transcript/summary, thumbnail and host-page policy | NEEDS_TARGETED_EVIDENCE | MASTER-TODO M; SYS-017 | Full video inventory not yet strategy-locked |

# Session 9 — System URLs, facets and legacy migration

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-059 | Store facets/sort/display parameter policy | PROPOSED | SR-004 SR-ST-008; SR-005 §16 | Separate crawl traps from variant preselection before any blocking |
| DEC-060 | Shop pagination and legacy `product-page` policy | PROPOSED | parameter evidence | Keep normal pagination; stop/consolidate legacy alternate where approved |
| DEC-061 | Product search URL policy | PROPOSED | SR-004 | Keep noindex |
| DEC-062 | Author/date/feed/search/404 family policies | PROPOSED | SYSTEM-URL-SPACES-CLOSURE | Most are system-policy decisions, not content work |
| DEC-063 | Legacy URL prioritization rule | PROPOSED | SR-005 §19; A-012 | Prioritize URLs with meaningful historical evidence/value |
| DEC-064 | Legacy product-volume mapping disposition | NEEDS_TARGETED_EVIDENCE | legacy-volume-url-map | 68 partial + 14 unknown remain |
| DEC-065 | Historical Education → Academy mappings | NEEDS_TARGETED_EVIDENCE | education-academy-migration-map | 36 partial + 5 unknown remain |
| DEC-066 | Historical Artist/other removed-content URL disposition | NEEDS_TARGETED_EVIDENCE | A-012 legacy map | Do not infer replacement by slug similarity |
| DEC-067 | Redirect technical owner and implementation path | OPEN | SEO-OWNERSHIP; legacy workstreams | Rank Math first where supported; platform only when justified |

# Session 10 — Measurement, rollout and later programs

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-068 | Canary size and rollout rules by change class | OPEN | M-15; change templates | Define practical samples for metadata/schema/content/link changes |
| DEC-069 | Monitoring windows and success metrics | OPEN | M-18; MASTER-TODO J | Separate technical correctness from ranking/business outcome |
| DEC-070 | Strategy Lock scope for first implementation wave | OPEN | governance + accepted decisions | Decide which accepted decisions form first coherent rollout |
| DEC-071 | External PR / advertorial strategy | DEFERRED | MASTER-TODO K | Decide after internal architecture/landing pages stabilize |
| DEC-072 | Merchant Center / product feed program | DEFERRED | MASTER-TODO O | Requires separate eligibility/feed review |
| DEC-073 | Reviews/social-proof program | DEFERRED | MASTER-TODO O | Requires genuine review-data audit |

---

# Global constraints that apply to every decision

1. Repository evidence is the source of truth.
2. Current Production reality overrides stale Round-1 observations.
3. Google official documentation governs SEO basis.
4. Rank Math is the first technical owner where the installed version supports the concern.
5. No Page→Query attribution without joined evidence or explicit alternative research.
6. No invented product/content facts.
7. No mass implementation from a family recommendation before target state and exceptions are accepted.
8. No Codex Production task is generated directly from this file until the corresponding item(s) are `ACCEPTED` and represented in `tasks/EXECUTION-BACKLOG.md`.

# Strategy Lock checklist

For any scope proposed for implementation:

- [ ] all blocking DEC IDs = `ACCEPTED`
- [ ] exact target state written
- [ ] exact affected entity/family list known
- [ ] exceptions documented
- [ ] SEO owner known
- [ ] Google basis recorded
- [ ] content text approved where applicable
- [ ] canary/regression approach known
- [ ] unresolved dependencies are non-blocking and explicit
- [ ] Execution Backlog item created
