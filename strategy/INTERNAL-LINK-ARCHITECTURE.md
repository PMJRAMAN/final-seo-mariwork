# Internal Link Architecture

**Status:** ACCEPTED STRATEGY FRAMEWORK  
**Authority:** DEC-040 through DEC-048, DEC-120  
**Date:** 2026-09-26

## Purpose

Create a consistent crawlable internal-link system across Mariwork without forcing irrelevant links or link-count targets.

## Accepted link classes

### CORE / MANDATORY
Links required across every applicable entity in a defined family. These are primarily durable parent/hub relationships and other explicitly approved structural links.

### FAMILY-SPECIFIC
Links required only when a defined family condition is present.

### CONTEXTUAL / OPTIONAL
Links added only when the page topic or user task makes them genuinely useful. They have no sitewide coverage quota.

## Accepted hierarchy rules

- Product → stable primary Product Category → Shop.
- Child Product Category → real parent Product Category → Shop.
- Current Guide → One-Minute Guides collection → Academy.
- Future genuine Lesson → Course → Academy.
- Article → stable primary Blog Category → Magazine.
- Multi-parent entities use one deliberate stable primary hierarchy.
- The relationship may be supplied by breadcrumb, navigation, taxonomy UI or another crawlable component; body-copy boilerplate is not required.

## Cross-family rules

- Product → Academy/Article only when the destination directly helps selection, preparation, use, application, fixation/cure, care or another real Product task.
- Academy/Lesson → Product/Category only when the Product/material/tool is actually used, required or a direct useful next step.
- Article → Product/Category only when the commercial destination genuinely supports the article topic.
- Article → Article/Academy only for a real continuation, deeper detail, prerequisite, complementary reference or practical follow-up.
- Product Category → Academy/Article becomes appropriate when the Category is developed into a content-supported landing page and the education/reference destination directly supports that Category.
- No fixed number of cross-family links is required.

## Global navigation

Header/Footer/Navigation expose important durable hubs and essential user destinations only.

Do not inflate global navigation with SEO-driven link inventories. Topic-, Product- and context-specific relationships remain body/context concerns.

## Anchor text

Anchors are concise, natural, descriptive and accurate to the destination.

- no forced exact-match repetition;
- no invented query-target anchors;
- natural variation is allowed;
- avoid generic anchors such as “click here” when a meaningful phrase is naturally available.

## Orphan / underlinked definitions

- **Orphan:** an important indexable page with an assigned role has no meaningful crawlable path from the intended architecture.
- **Underlinked:** the page is reachable but is missing a required relationship defined by the accepted family rules/matrix.
- No universal minimum inbound-link count defines adequacy.
- Utility, noindex, temporary and deliberate non-search pages may be documented exceptions.

## Canonical requirement matrix

The canonical family matrix is:

`strategy/INTERNAL-LINK-REQUIREMENT-MATRIX.md`

Exact destination URLs, anchors and page-level exceptions are implementation/research data, not new strategy decisions, provided they remain inside the accepted rules above.

## QA

Equivalent pages in the same family must not randomly differ in mandatory-link coverage. Any missing mandatory relationship must be fixed or documented as an approved exception.

No Production write is authorized by this strategy file alone.
