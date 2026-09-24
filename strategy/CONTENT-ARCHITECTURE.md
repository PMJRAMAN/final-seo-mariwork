# Content Architecture

Status: INITIAL

هدف:
- نقش Product / Category / Education / Article را تفکیک کند؛
- overlap و cannibalization را کاهش دهد؛
- internal links معنادار بسازد؛
- از تولید صفحات تکراری جلوگیری کند.

## Families

### Products
TBD

### Product Categories / Shop
TBD

### Education
TBD

### Articles
TBD

### Artists / Trust Content
TBD

## Cross-link Rules
Detailed rules live in `strategy/INTERNAL-LINK-ARCHITECTURE.md`.

The final model must distinguish:
- CORE / MANDATORY links that every relevant entity in a family should contain;
- FAMILY-SPECIFIC links required only for a defined product/content family;
- CONTEXTUAL / OPTIONAL links used only when the page topic makes them genuinely useful.

The architecture must be bidirectional where useful:
Product/Category → Academy/Article, and Academy/Article → relevant Product/Category.

TBD after sitewide link audit and first batches.


## Product Title Naming Standard

**Status:** INITIAL / NOT APPROVED

The Store requires an evidence-backed naming standard for each product family rather than ad-hoc title cleanup.

Round 1 must inventory current title patterns and inconsistencies. Round 2 will approve the final standard after query/intent and family review.

The review must explicitly determine:
- whether «ماری ورک» / Mariwork is mandatory, optional or omitted for each family;
- ordering of product type, descriptive name/color, brand and product code;
- product-code formatting;
- size/volume placement where it belongs in the canonical product title;
- rules for single colors, mediums, sets/bundles, tools/accessories and other products;
- duplicate or near-duplicate title patterns;
- inconsistencies between product title, H1 and entity identity;
- documented exceptions;
- legacy title/slug history when a title change could affect continuity.

Do not bulk-rename products from an assumed template. The naming standard must be approved before implementation.


## External Amplification

External PR / advertorial activity must follow the approved internal architecture rather than define it.

For every external article:
- choose a durable landing page based on intent and page role;
- ensure that landing page has a deliberate internal path to relevant products, categories, Academy lessons or articles;
- avoid sending all placements to the homepage or arbitrary products;
- use `strategy/EXTERNAL-PR-STRATEGY.md` for campaign planning and measurement.
