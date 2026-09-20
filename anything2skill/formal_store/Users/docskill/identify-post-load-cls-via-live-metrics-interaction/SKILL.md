---
id: "af4774f1-6811-5515-812c-ec65a6e10182"
name: "Identify Post-Load CLS via Live Metrics Interaction"
description: "Monitor CLS score in real-time while interacting with the page using DevTools Performance panel live metrics view to detect user-interaction-triggered layout shifts. Use when post-load CLS is suspected but cannot be reproduced via static page load."
version: "0.1.0"
tags:
  - "performance"
  - "cls"
  - "cumulative-layout-shift"
  - "devtools"
  - "live-metrics"
  - "post-load"
triggers:
  - "CrUX reports significantly higher CLS than Lighthouse lab measurement"
  - "Post-load CLS suspected but not reproducible via page reload"
  - "Need to identify which user interactions trigger layout shifts"
---

# Identify Post-Load CLS via Live Metrics Interaction

Monitor CLS score in real-time while interacting with the page using DevTools Performance panel live metrics view to detect user-interaction-triggered layout shifts. Use when post-load CLS is suspected but cannot be reproduced via static page load.

## Prompt

Open DevTools Performance panel. Switch to live metrics view. Interact with the page (scroll, click, hover, expand content) while observing the CLS score. Record which interactions cause CLS score increases. Note the timing and magnitude of shifts. Cross-reference with CrUX field data to confirm post-load CLS patterns.

## Objective

Capture and correlate post-load CLS events with specific user interactions
## Applicable Signals

- Disagreement between field CLS (CrUX) and lab CLS (Lighthouse)
- Page exhibits interactive behavior (dynamic content, ads, embeds, animations)
- User reports layout instability after initial page load

## Contraindications

- Only static load-time shifts present; no user interaction expected
- Page is non-interactive or fully static
- CLS issue is reproducible via standard page reload profiling

## Workflow Steps

- Open DevTools and navigate to Performance panel
- Locate and activate live metrics view
- Begin recording or monitoring mode
- Systematically interact with page elements (scroll, click, expand, hover)
- Observe CLS score changes in real-time
- Note timing, magnitude, and triggering interaction for each shift
- Stop monitoring and review recorded interactions against CLS deltas
- Cross-reference findings with CrUX field data to validate post-load pattern

## Constraints

- Requires DevTools Performance panel access
- Live metrics view must be available in target browser
- Observer must actively interact with page during monitoring
- Shifts must occur within session; cannot capture delayed post-session shifts

## Cautions

- Live metrics view captures only shifts during active observation window
- User interactions may not replicate all field conditions
- Multiple simultaneous interactions may obscure individual shift causes

## Output Contract

- Recorded CLS score changes correlated with specific user interactions; identified which interactions trigger layout shifts; documented timing and magnitude of post-load shifts; confirmed post-load CLS pattern for downstream remediation

## Triggers

- CrUX reports significantly higher CLS than Lighthouse lab measurement
- Post-load CLS suspected but not reproducible via page reload
- Need to identify which user interactions trigger layout shifts
