# Content Research Specification v1.0

هدف: قبل از rewrite بدانیم کاربر چه می‌خواهد، صفحه چه نقشی دارد و چه اطلاعات واقعی می‌تواند آن را بهتر کند.

## 1. Inputs

- page dossier
- current visible content
- joined Page+Query GSC data if available
- page-level GSC metrics
- Query Map
- current SERP
- related Mariwork pages
- verified product/source facts
- relevant competitor result pages فقط برای gap/format observation

## 2. Intent Research

ثبت:
- primary intent
- secondary intent
- transactional/informational/mixed
- decision user must make
- questions blocking that decision
- expected page type in current SERP

## 3. Query Research

Queryها:
- از Page+Query data ترجیحاً
- GSC query corpus در سطح سایت برای discovery
- current SERP research
- product terminology

هر query cluster فقط با evidence به target entity نگاشت می‌شود.

Keyword density یا exact-match repetition هدف نیست.

## 4. Cannibalization / Overlap

بررسی:
- چند URL برای query cluster مشابه
- product vs archive vs article conflict
- legacy URL remnants
- duplicated intent

راهکار ممکن است merge/internal-link/canonical/content differentiation باشد؛ از قبل فرض نمی‌شود.

## 5. Information Gap

سه ستون:
- information user needs
- currently present?
- verified source available?

اگر source نداریم، fact ساخته نمی‌شود؛ نیاز به data collection ثبت می‌شود.

## 6. Unique Value / First-Hand Evidence

برای محصولات:
- real sample
- substrate/fabric context
- light/dark background
- volume economics
- real usage instructions
- verified test results
- comparison with close colors/products

فقط شواهد واقعی.

## 7. Content Architecture

هر بخش باید دلیل داشته باشد:
- decision summary
- specs
- comparison
- usage
- evidence
- limitations
- relevant questions
- links to deeper education

بخش صرفاً برای افزایش طول اضافه نمی‌شود.

## 8. Competitor Research

مجاز:
- SERP composition
- missing topics
- format
- evidence type
- user questions

ممنوع:
- copy/paraphrase close text
- تقلید ادعاهای بدون verification
- ساخت content فقط چون competitor دارد

## 9. Trust

بدون E-E-A-T score:
- real author/reviewer if applicable
- source/manufacturer authority
- actual review date
- evidence/proof
- clear responsibility

## 10. LLM/AI Readability

- direct factual statements
- clear entity names
- structured attributes
- answer-first when appropriate
- tables/lists only where useful
- important facts in text
- no special fake AI schema

## 11. Output

برای rewrite بزرگ:
`templates/CONTENT-BRIEF.md`

Final text یا exact content requirements باید قبل از implementation تأیید شود.
