---
id: "b7453454-b783-5c7e-892a-6c8896099cec"
name: "Enable bfcache for CLS reduction"
description: "Ensure web pages are eligible for back/forward cache (bfcache) to keep fully loaded pages instantly available in browser memory, eliminating layout shifts on navigation return."
version: "0.1.0"
tags:
  - "CLS"
  - "cumulative_layout_shift"
  - "bfcache"
  - "back_forward_cache"
  - "web_performance"
  - "browser_caching"
triggers:
  - "Optimizing for CLS scores"
  - "Pages experience layout shifts on return navigation"
  - "Seeking low-effort high-impact CLS reduction"
---

# Enable bfcache for CLS reduction

Ensure web pages are eligible for back/forward cache (bfcache) to keep fully loaded pages instantly available in browser memory, eliminating layout shifts on navigation return.

## Prompt

To reduce cumulative layout shift (CLS) using bfcache:
1. Verify your page meets bfcache eligibility requirements.
2. Ensure no unload handlers or blocking APIs prevent bfcache restoration.
3. Test that pages are restored exactly as left when user navigates back/forward.
4. Confirm no layout shifts occur during restoration from bfcache.
This technique keeps the fully loaded page in memory for instant restoration without the layout shifts normally seen during load.

## Objective

Reduce cumulative layout shift by leveraging browser caching mechanism
## Applicable Signals

- High CLS scores on back/forward navigation
- User navigation patterns involve returning to previously visited pages
- Layout shifts observed during page restoration

## Contraindications

- Pages require fresh data on every load
- bfcache eligibility constraints prevent implementation
- User interaction patterns do not involve back/forward navigation

## Workflow Steps

- Audit page for bfcache eligibility blockers
- Remove or refactor unload handlers and blocking APIs
- Test page restoration via back/forward navigation
- Verify no layout shifts occur during restoration
- Confirm bfcache eligibility in browser DevTools

## Constraints

- Page must meet bfcache eligibility requirements
- No unload handlers or blocking APIs should prevent restoration
- Browser support for bfcache varies; test across target browsers

## Cautions

- bfcache eligibility depends on page implementation; some APIs or patterns may disqualify pages
- Not all browsers support bfcache equally; verify support in target user base

## Output Contract

- Page restored exactly as left when user returns via back/forward button
- No layout shifts observed during restoration
- bfcache eligibility confirmed in browser memory

## Triggers

- Optimizing for CLS scores
- Pages experience layout shifts on return navigation
- Seeking low-effort high-impact CLS reduction
