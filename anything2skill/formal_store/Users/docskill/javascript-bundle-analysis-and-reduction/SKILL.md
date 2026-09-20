---
id: "cdfbc947-30cc-5a7e-946d-afb57c123d6b"
name: "JavaScript Bundle Analysis and Reduction"
description: "Use Chrome DevTools Performance panel to record, visualize, and inspect individual layout shifts with timing, score, and affected elements. Apply when load-time CLS needs detailed root-cause identification."
version: "0.1.2"
tags:
  - "performance"
  - "CLS"
  - "layout_shift"
  - "DevTools"
  - "diagnosis"
  - "instrumentation"
triggers:
  - "application bundle size is large"
  - "performance metrics indicate slow initial load"
  - "need to diagnose bundle composition before optimization"
examples:
  - input: "Page reload in DevTools Performance panel; CLS score 0.15 reported by Lighthouse"
    output: "Layout Shifts track shows 3 shift clusters: (a) banner ad loads at 2.3s, shifts content down 0.08 score; (b) web font renders at 1.8s, shifts text 0.05 score; (c) image without dimensions loads at 3.1s, shifts layout 0.02 score. Culprits insight confirms ad and font as primary causes."
    notes: "Largest shift (banner) is prioritized for fix; reserve space or lazy-load ad to reduce CLS."
  - input: "Post-load interaction (user clicks button) causes layout shift"
    output: "Shift does not appear in reload trace; use live metrics view instead to capture interaction-driven shifts."
    notes: "This skill is for load-phase CLS only; post-load requires different approach."
---

# JavaScript Bundle Analysis and Reduction

Use Chrome DevTools Performance panel to record, visualize, and inspect individual layout shifts with timing, score, and affected elements. Apply when load-time CLS needs detailed root-cause identification.

## Prompt

1. Open Chrome DevTools and navigate to the Performance tab.
2. Click the record button and reload the page to capture a full trace.
3. Stop recording when the page has fully loaded.
4. In the results, locate the Layout Shifts track (purple bars and diamonds).
5. Click individual diamonds to view shift animations and details in the Summary panel.
6. Note the start time, shift score, and affected elements for each shift cluster.
7. Cross-reference with the Layout shift culprits insight in the Insights panel to identify root causes.
8. Document the largest shifts (diamond size indicates magnitude) and their timing relative to page load events.

## Objective

Pinpoint layout shift culprits and their magnitude during page load
## Applicable Signals

- High CLS detected in lab tools (Lighthouse, PageSpeed Insights)
- Page reload is reproducible
- Chrome DevTools Performance panel is accessible
- Load-time CLS is the focus (not post-load interactions)

## Contraindications

- Post-load CLS only (shifts occurring after page fully loads)
- Field-only issues without reproducible lab scenario
- Non-Chrome browsers or environments without DevTools access

## Workflow Steps

- {'step': 1, 'action': 'Open DevTools Performance panel', 'detail': 'Press F12 or Ctrl+Shift+I, navigate to Performance tab'}
- {'step': 2, 'action': 'Record a trace', 'detail': 'Click record button, reload the page, wait for full load, stop recording'}
- {'step': 3, 'action': 'Locate Layout Shifts track', 'detail': 'In results, find the purple bars and diamonds in the Layout Shifts track'}
- {'step': 4, 'action': 'Inspect individual shifts', 'detail': 'Click each diamond to view animation and Summary panel details (start time, score, elements)'}
- {'step': 5, 'action': 'Review Layout shift culprits insight', 'detail': 'Check Insights panel on left for total CLS and possible reasons'}
- {'step': 6, 'action': 'Document findings', 'detail': 'Record shifted elements, scores, timing, and magnitude (diamond size) for each cluster'}

## Constraints

- Requires Chrome browser with DevTools enabled
- Page must be reloadable to capture trace
- Lab environment must be stable enough to replicate shifts consistently

## Cautions

- Layout shifts during trace recording may differ from production due to network throttling or CPU simulation settings
- Post-load CLS (from user interactions or late-loaded content) will not appear in a simple reload trace; use live metrics view for those

## Output Contract

- Deliverable is a set of identified layout shift clusters with: (1) affected element names/selectors, (2) shift score for each cluster, (3) start time relative to page load, (4) visual animation confirmation, and (5) root-cause hypothesis from culprits insight. Caller can use this to prioritize fixes (largest shifts first) and validate solutions in subsequent traces.

## Example Therapist Responses

### Example 1

- Client/Input: Page reload in DevTools Performance panel; CLS score 0.15 reported by Lighthouse
- Therapist/Output: Layout Shifts track shows 3 shift clusters: (a) banner ad loads at 2.3s, shifts content down 0.08 score; (b) web font renders at 1.8s, shifts text 0.05 score; (c) image without dimensions loads at 3.1s, shifts layout 0.02 score. Culprits insight confirms ad and font as primary causes.
- Notes: Largest shift (banner) is prioritized for fix; reserve space or lazy-load ad to reduce CLS.

### Example 2

- Client/Input: Post-load interaction (user clicks button) causes layout shift
- Therapist/Output: Shift does not appear in reload trace; use live metrics view instead to capture interaction-driven shifts.
- Notes: This skill is for load-phase CLS only; post-load requires different approach.

## Triggers

- application bundle size is large
- performance metrics indicate slow initial load
- need to diagnose bundle composition before optimization

## Examples

### Example 1

Input:

  Page reload in DevTools Performance panel; CLS score 0.15 reported by Lighthouse

Output:

  Layout Shifts track shows 3 shift clusters: (a) banner ad loads at 2.3s, shifts content down 0.08 score; (b) web font renders at 1.8s, shifts text 0.05 score; (c) image without dimensions loads at 3.1s, shifts layout 0.02 score. Culprits insight confirms ad and font as primary causes.

Notes:

  Largest shift (banner) is prioritized for fix; reserve space or lazy-load ad to reduce CLS.

### Example 2

Input:

  Post-load interaction (user clicks button) causes layout shift

Output:

  Shift does not appear in reload trace; use live metrics view instead to capture interaction-driven shifts.

Notes:

  This skill is for load-phase CLS only; post-load requires different approach.
