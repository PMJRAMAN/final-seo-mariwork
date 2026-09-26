# SL-006 — Legacy URL / Migration Disposition

**Status:** STRATEGY_LOCKED  
**Locked:** 2026-09-26  
**Lock refresh:** 2026-09-26 after final Product-naming/DEC-008 consistency amendment  
**Baseline repository HEAD:** `aa9116930ee5703b8b62e40dc55e97a32174ea6e`

## Accepted Decision IDs

Primary:
- DEC-027, DEC-028, DEC-029, DEC-031
- DEC-063, DEC-064, DEC-065, DEC-066, DEC-067
- DEC-084
- DEC-109
- DEC-128

Dependencies:
- DEC-025, DEC-026, DEC-052
- DEC-068, DEC-102, DEC-103
- SL-000
- SL-001 for canonical/redirect behavior

## Exact target state

- historical priority affects review order, not semantic disposition;
- redirect only to a genuine verified semantic successor;
- no redirect based on slug/name similarity alone;
- no generic Homepage/Shop/Category fallback merely to eliminate 404s;
- no genuine successor → proper 404/410 as appropriate;
- Nginx is the canonical redirect owner;
- preserve correct existing Nginx redirects rather than recreating them in WordPress/Rank Math;
- legacy Product-volume URLs map to the same current variable Product with matching volume preselection only when identity and current purchasable volume are verified;
- historical Education lesson mappings already correctly redirected are verify-and-preserve;
- historical individual Artist URLs wait until the new Artists system is public/stable, then are reviewed manually;
- unmatched Artist URLs are not precommitted to the Artists hub;
- non-Artist removed content follows DEC-128.

## Blocking / non-blocking inputs

- current Nginx rule verification before any redirect write;
- exact source→successor identity evidence;
- owner/source input for unresolved DEC-128 URL-level cases;
- Artist migration remains operationally blocked until the new Artists system is public/stable.

## Boundary

This lock defines migration policy, not permission for bulk redirect writes. Every batch still requires exact mappings, backup/rollback and regression QA.
