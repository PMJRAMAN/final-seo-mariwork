# Internal Link Architecture

**Status:** INITIAL / NOT APPROVED
**Authority:** Round-1 evidence may propose rules; ChatGPT Second Review + human approval defines the target architecture before implementation.

## Purpose

Create a consistent internal-link network across Mariwork so links are not added or omitted randomly between equivalent pages.

The system must answer, for each content/product family:

1. Which links are mandatory on every relevant page?
2. Which links are required only for a specific family?
3. Which links are contextual and should appear only when genuinely relevant?
4. Which Academy/Article pages should link back to Products or Categories?
5. Which pages are orphaned or underlinked?
6. Which current links are irrelevant, duplicated or inconsistent?

## Link Classes

### CORE / MANDATORY

Links that every relevant entity in a defined family should contain.

Example pattern:
- if a fixation guide is a core instruction for all fabric-color products, every fabric-color product must link to it unless a documented exception exists.

### FAMILY-SPECIFIC

Links required only for a particular family.

Examples:
- medium products → usage guide for that medium/family;
- printing tools → relevant printing technique;
- sets → color-selection/mixing guidance where relevant.

### CONTEXTUAL / OPTIONAL

Links added only when the page topic or user task makes them useful.

They must not be mass-added merely to increase link count.

## Bidirectional Architecture

Where useful, relationships should work in both directions:

- Product → Academy / Article
- Category → Academy / Article
- Academy / Article → relevant Product
- Academy / Article → relevant Product Category

Commercial links from informational content must be useful and contextually justified, not forced.

## Required Deliverables

- family-level Internal Link Requirement Matrix;
- list of mandatory destinations per family;
- family-specific destination rules;
- contextual-link candidates;
- reverse-link rules from Academy/Articles;
- missing-link coverage report;
- orphan/underlinked page report;
- documented exceptions;
- implementation-ready target links for each approved page/family;
- final regression against the approved matrix.

## Example Matrix Structure

| Source family | Link class | Target family/entity | Requirement | Notes |
|---|---|---|---|---|
| Fabric Colors | CORE/MANDATORY | Fixation guide | Required on every fabric-color product | Final target TBD after review |
| Fabric Colors | FAMILY-SPECIFIC | Washing/care guide | Required if applicable to all products in family | Verify content scope |
| Mediums | FAMILY-SPECIFIC | Matching medium guide | Required for that medium family | Avoid unrelated guides |
| Any content | CONTEXTUAL/OPTIONAL | Related article/lesson/product | Only when semantically useful | No forced sitewide insertion |

## QA Rule

Equivalent pages in the same family must not randomly differ in mandatory-link coverage.

Any missing mandatory link must be either:
- fixed; or
- documented as an approved exception.

Final sitewide QA must validate the implemented network against this document and the approved matrix.
