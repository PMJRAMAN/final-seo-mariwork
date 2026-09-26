# AI Assistant / Generative-Answer Discoverability Strategy

**Status:** DRAFT / DECISION PENDING  
**Primary Decision:** DEC-129  
**Created:** 2026-09-26  
**Scope:** ChatGPT Search, Microsoft Copilot/Bing AI, Google generative Search features, and other evidence-backed AI answer surfaces.

## Objective

Treat AI-answer visibility and citation as a first-class Mariwork SEO objective.

The goal is not merely to allow crawlers. Mariwork content should be:
- technically discoverable;
- semantically clear;
- easy to retrieve for real user intents;
- factual and evidence-backed;
- citation-worthy;
- consistent across text, schema, image and video;
- measurable where platforms expose reliable visibility/citation data.

This workstream is connected to classic SEO, but is not reduced to rankings, robots.txt or structured data alone.

## Current Evidence Boundary

### OpenAI / ChatGPT Search
- OpenAI documents `OAI-SearchBot` as the crawler used for surfacing websites in ChatGPT Search.
- Search eligibility is independent from `GPTBot`, which is used for potential model-training crawling.
- `ChatGPT-User` is a separate user-triggered access pattern.
- Allowing crawler access does not guarantee inclusion or placement.

Official references:
- https://developers.openai.com/api/docs/bots
- https://help.openai.com/en/articles/9237897-searching-the-web-with-chatgpt
- https://help.openai.com/en/articles/12627856-publishers-and-developers-faq

### Microsoft Copilot / Bing AI
- Bing Webmaster Tools exposes AI Performance data for citations in Microsoft Copilot, Bing AI-generated summaries and selected partner experiences.
- Available signals include cited pages, citation counts and grounding queries.
- Bing recommends clear intent alignment, depth, evidence, freshness, clear structure and consistency across formats.

Official references:
- https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c
- https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/

### Google Generative Search
- Google states that standard SEO best practices remain relevant for generative Search features.
- Eligibility still depends on crawlability/indexability and Search requirements.
- Google explicitly warns against spam and scaled low-value content aimed at manipulating Search or generative answers.
- Google states that `llms.txt` is not required for Google Search and does not positively or negatively affect Google Search visibility/rankings.

Official references:
- https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- https://developers.google.com/search/docs/essentials/spam-policies
- https://developers.google.com/search/updates

## Strategy Pillars to Decide Under DEC-129

### 1. Technical Eligibility
- crawler access by platform;
- robots/WAF/server behavior;
- indexability/canonical consistency;
- fetchable HTML, images and video;
- explicit separation of Search visibility controls from model-training controls.

### 2. Conversational Intent and Page Ownership
- research real questions and conversational intents around fabric painting, hand printing, products, techniques and Mariwork;
- map each durable intent cluster to a clear owner page;
- avoid creating thin pages for every chatbot-style wording;
- reuse the existing Product / Category / Academy / Magazine / Brand architecture.

### 3. Answerable Content Structure
- concise factual answer near the relevant section;
- descriptive headings;
- stepwise instructions where the topic is procedural;
- comparison tables only where they genuinely help;
- clear definitions, limitations and exceptions;
- avoid filler, keyword stuffing and artificial FAQ expansion.

### 4. Citation-Worthy First-Hand Evidence
Prefer content that contributes something retrievable and verifiable:
- real Mariwork product facts;
- real tests and demonstrations;
- substrate/context examples;
- documented comparisons;
- verified usage instructions;
- original images/video;
- founder/brand facts from the canonical registry;
- unique educational expertise that can be stated accurately.

Do not fabricate studies, tests, citations, credentials, relationships or authority signals.

### 5. Provenance and Factual Reliability
- use verified sources when factual/technical/historical claims require them;
- maintain real publish/update dates;
- identify author/reviewer only when genuinely applicable and verified;
- clearly distinguish Mariwork first-hand evidence from external facts.

### 6. Entity Consistency
Keep the same factual identity across:
- visible content;
- Organization/Product/Article/Video structured data where eligible;
- About/Why/Contact pages;
- images and captions;
- video titles/descriptions;
- external references where later verified.

### 7. Multimodal Retrieval
AI discovery should include:
- useful image context and ALT;
- factual thumbnails;
- crawlable/fetchable media;
- transcripts/summaries where useful;
- consistent product/image/video identity.

Existing DEC-054, DEC-089–098 and related visual/video decisions remain authoritative.

### 8. Freshness and Maintenance
- refresh facts when products, availability, techniques or policies change;
- do not fake freshness by changing dates without meaningful updates;
- use the ongoing maintenance framework under DEC-104.

### 9. Measurement
Potential evidence sources include:
- ChatGPT referral/citation evidence where observable;
- Bing Webmaster Tools AI Performance: citations, cited pages and grounding queries;
- Google Search Console generative-AI reporting where available;
- server logs for crawler access diagnostics;
- business/conversion outcomes where attribution is reliable.

Measurement must distinguish:
- citation/appearance;
- referral traffic;
- classic Search visibility;
- business outcome.

No single metric should be treated as a universal AI ranking score.

## Guardrails

- No thin "GEO" pages generated only to match chatbot prompts.
- No scaled FAQ/question pages without independent user value.
- No fabricated authority, experts, reviews, citations or relationships.
- No unsupported claim that a special file, schema type or formatting trick guarantees AI inclusion.
- No separate duplicate content strategy for each chatbot when one strong durable page can satisfy the intent.
- Platform-specific tactics require current official evidence.
- Search visibility and model-training permission are separate owner decisions.

## Relationship to Existing Decisions

- DEC-110: technical crawler access and Search/training separation.
- DEC-040–050: internal linking, content-family roles and query ownership.
- DEC-053 / DEC-099 / DEC-100: brand facts and branded query ownership.
- DEC-054 / DEC-089–093: image quality/discovery/delivery.
- DEC-094–098: video discoverability and content support.
- DEC-102–104: measurement, monitoring and maintenance.
- DEC-071 / DEC-101: external PR/entity evidence, deferred.
- DEC-129: governs the final AI-assistant / generative-answer content strategy.

## Decision Work Still Required

DEC-129 must later define and approve:
1. priority AI platforms/surfaces for Mariwork;
2. conversational-intent research method;
3. AI-specific content quality checklist by page family;
4. evidence/citation requirements by topic class;
5. measurement dashboard and monitoring cadence;
6. crawler policy matrix by platform;
7. whether any platform-specific files/protocols are justified by documented support;
8. canary and QA rules for AI-focused content changes.

No Production implementation is authorized by this draft.
