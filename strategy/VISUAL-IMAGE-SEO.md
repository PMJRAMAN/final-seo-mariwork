# Visual / Image / Multimodal SEO Strategy

**Status:** ACCEPTED STRATEGY FRAMEWORK / TARGETED EVIDENCE PENDING  
**Authority:** DEC-054, DEC-056, DEC-057, DEC-089 through DEC-093, DEC-111, DEC-129  
**Updated:** 2026-09-26

## Objective

Make important Mariwork visual assets understandable, accessible, technically efficient and discoverable without redesigning Product/media UX for SEO.

## Accepted rules

### ALT
- Informative images receive concise factual context-appropriate ALT.
- Decorative images use empty ALT.
- ALT is role/context based, not a missing-count exercise.
- Never infer visual facts or keyword-stuff ALT.
- Reused files may have context-specific ALT when each description remains factual.

### Product images / galleries
- SEO does not redefine Product gallery count, composition or merchandising order already governed by Product/design decisions.
- Fabric-color primary imagery may follow the approved 60 ml merchandising rule; variant selection may change the displayed image.
- Image reuse is not a defect by itself when the image is relevant and accurate.
- Corrective work requires evidence of factual mismatch, misleading reuse, accessibility or discoverability issues.

### Article / Academy imagery
- No fixed image quota.
- Academy is video-first; supplementary images exist only when they materially improve a step, tool, result, detail or concept.
- Magazine images exist when they improve understanding, documentation, identification, technique illustration or editorial value.
- No filler imagery added “for SEO”.

### New filenames
- Short, descriptive, stable and fact-based.
- Prefer lowercase Latin words separated by hyphens where practical.
- No stuffing or inferred facts.
- No historical bulk rename merely for SEO.

### Context / captions / linked images
- Captions are optional and usefulness-driven.
- Do not add captions mechanically.
- Image links require a relevant intentional destination.
- Linked-image ALT follows DEC-054.

### Discovery / crawlability
- Important images on indexable pages should remain crawlable/loadable unless deliberately excluded.
- A separate image sitemap is not mandatory by default.
- Add dedicated discovery mechanisms only when evidence supports a real need.

### Technical delivery
- Responsive image delivery must match real component/slot needs on mobile and desktop.
- Use correct responsive candidates plus `srcset`/`sizes`.
- Avoid routinely downloading images materially larger than rendered need.
- Avoid undersized/blurry delivery, including high-DPR displays.
- Preserve intrinsic dimensions/aspect ratio where applicable.
- Below-the-fold images may lazy-load.
- Likely LCP/hero images must not be blindly lazy-loaded.
- Standardize rules by component/template and QA mobile/desktop, DPR, bytes, visual quality and LCP/CLS.
- Performance claims require field/lab evidence.

## Evidence still required before implementation

- representative visual review where role/mismatch is uncertain;
- current rendered image markup and responsive-candidate behavior;
- representative mobile/desktop slot measurements;
- LCP/CLS lab/field evidence where performance changes are proposed;
- current crawlability/indexability evidence where discovery changes are proposed.

These are implementation/evidence gates, not unresolved strategy decisions.

## Multimodal / AI relationship

Image context, factual identity and technical fetchability also support the accepted AI-assistant discoverability framework in DEC-129. No separate AI-only image stuffing or fabricated metadata is allowed.

## Completion

Broad implementation requires a scoped inventory, priority issue list, canary/regression set and dual QA.

No Production write is authorized by this strategy file alone.
