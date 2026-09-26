# SL-005 — Visual / Video / Performance / AI Discoverability

**Status:** STRATEGY_LOCKED  
**Locked:** 2026-09-26  
**Lock refresh:** 2026-09-26 after final Product-naming/DEC-008 consistency amendment  
**Baseline repository HEAD:** `aa9116930ee5703b8b62e40dc55e97a32174ea6e`

## Accepted Decision IDs

Primary:
- DEC-038
- DEC-054, DEC-056, DEC-057
- DEC-089 through DEC-098
- DEC-110, DEC-111
- DEC-129

Dependencies:
- DEC-040–048 for media-related internal links
- DEC-085, DEC-121–125 for provenance/content/claims
- DEC-068, DEC-069, DEC-102–104 for rollout/measurement
- DEC-112 for technical ownership

## Exact target state

### Images
- role/context-based factual ALT;
- no fixed image quota;
- SEO does not redesign Product galleries;
- new filenames are descriptive/fact-based;
- captions/linked images only when useful;
- important images remain crawlable/loadable unless deliberately excluded;
- responsive delivery matches actual mobile/desktop slot needs;
- avoid both oversized downloads and blurry undersized candidates;
- do not blindly lazy-load likely LCP/hero images.

### Video
- VideoObject is eligibility-driven;
- genuine visible/playable host-page relationship required;
- factual titles/descriptions/thumbnails;
- transcripts/summaries only when useful;
- no thin standalone media pages;
- duplicate/orphan media receives an explicit lifecycle disposition.

### AI / generative answers
- AI-answer discoverability/citation is a first-class objective;
- crawl eligibility is separate from citation-worthiness;
- emphasize answerable structure, first-hand evidence, provenance, entity consistency, multimodal support and freshness;
- no thin GEO/FAQ scaling;
- no undocumented AI file/schema tricks;
- Search visibility controls remain separate from model-training controls.

### Performance
- use real-user/field evidence where available;
- current reference targets: LCP <= 2.5s, INP < 200ms, CLS < 0.1;
- fix evidenced bottlenecks rather than chasing a perfect lab score.

## Evidence gates

- representative image role/reuse review;
- rendered responsive-image behavior and slot/DPR measurements;
- current video inventory and host/player fetchability;
- actual robots/WAF access for Googlebot/OAI-SearchBot;
- current field/lab CWV evidence.

## Canonical files

- `strategy/VISUAL-IMAGE-SEO.md`
- `strategy/VIDEO-SEO.md`
- `strategy/AI-ASSISTANT-DISCOVERABILITY.md`
