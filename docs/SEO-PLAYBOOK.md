# SEO Playbook — Mariwork

**Framework:** v1.0  
**Playbook state:** EVIDENCE-BUILDING

این سند فقط قواعد پذیرفته‌شده سایت را نگه می‌دارد. Audit spec نیست و Codex اجازه ندارد rule دلخواه را ACCEPTED کند.

## Rule Contract

```yaml
rule_id: PLAY-XXX
scope: FAMILY|SITEWIDE
status: PROPOSED|ACCEPTED|SUPERSEDED
decision_ref:
evidence_refs:
rule:
exceptions:
accepted_date:
```

## 1. URL Architecture
TBD after inventory/sitewide crawl audit.

## 2. Indexability / Facets
TBD after sitewide technical baseline.

## 3. Product Naming
TBD after product pilot batches.

## 4. SEO Titles
TBD.

Baseline principle:
- descriptive
- concise
- distinct
- no unnecessary repeated boilerplate

## 5. Meta Descriptions
TBD.

Meta is a candidate snippet source, not guaranteed displayed text.

## 6. H1 / Headings
TBD.

## 7. Product Variants
TBD after variant audit.

Baseline principle:
- variant identities must be stable/unique where markup requires them
- canonical/variant URL behavior must match chosen architecture

## 8. Product Structured Data
TBD after systemic schema audit.

Baseline principle:
- structured data matches visible/current product facts
- no fake ratings/reviews/specs

## 9. Brand / SKU / Identifier
TBD.

## 10. Images / ALT

Accepted baseline principles:
- ALT describes the actual image
- keyword stuffing ممنوع
- wrong volume/product ALT must be corrected
- hero/product evidence images should balance quality and performance

## 11. Product Content Architecture
TBD after dual audit.

Potential modules, only when useful:
- decision summary
- verified specs
- volume comparison
- use cases
- real samples/evidence
- usage/fixation guidance
- relevant questions

No mandatory word count.

## 12. Internal Linking
TBD after crawl/link baseline.

## 13. Category / Archive
TBD.

## 14. Education / Articles
TBD.

## 15. Faceted Navigation
TBD after URL-space audit.

## 16. AI / LLM Readability

Accepted baseline:
- no special AI markup/files required for Google AI features
- important content should be textual and accessible
- entity/facts clear
- structured sections
- visible content and structured data consistent
- no invented facts
- Search crawler access و training crawler policy دو موضوع جدا هستند
- اگر ChatGPT Search در scope باشد، OAI-SearchBot accessibility مستقلاً audit می‌شود؛ GPTBot policy جای آن را نمی‌گیرد

## 17. Content Automation

Accepted baseline:
- scaled low-value/template content ممنوع
- automation may assist drafting/analysis but human/project approval and unique value are required

## 18. Monitoring
TBD after first implementation cycle.


## 19. Technical Ownership

Accepted:
- Google documentation governs SEO rationale.
- Rank Math is the default WordPress SEO technical owner where installed-version capability exists.
- title/meta/robots/canonical/sitemap/schema/redirection ownership نباید بین چند implementation موازی پخش شود.
- custom code فقط به‌صورت Rank Math Extension مرکزی و مستند، وقتی Rank Math native capability کافی نیست.
- Platform ownership فقط با دلیل فنی و برای concern خارج از Rank Math.
