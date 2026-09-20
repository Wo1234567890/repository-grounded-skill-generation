---
id: "45d7de73-a915-5ec3-93ab-e09d3f705ca6"
name: "Locate Layout Shift Elements in DevTools"
description: "Use Chrome DevTools Performance panel to record, visualize, and inspect individual layout shift events during page load, including shift clusters, timing, score, and affected DOM elements. Prioritize shifts by size and replay animations to understand load-phase CLS issues."
version: "0.1.0"
tags:
  - "performance"
  - "CLS"
  - "layout_shift"
  - "DevTools"
  - "debugging"
  - "lab_diagnostics"
triggers:
  - "Debugging load-phase CLS issues"
  - "Need to identify which DOM elements shift and when"
  - "Have access to Chrome DevTools and can reproduce the page load"
examples:
  - input: "Page reload with visible layout instability during load"
    output: "DevTools trace showing Layout Shifts track with 3 clusters; largest shift (0.15 score) at 2.3s affecting banner element; second shift (0.08 score) at 3.1s affecting sidebar; third shift (0.05 score) at 4.2s affecting footer"
    notes: "Diamond size proportional to shift score; clicking each diamond replays the animation showing the exact element movement"
---

# Locate Layout Shift Elements in DevTools

Use Chrome DevTools Performance panel to record, visualize, and inspect individual layout shift events during page load, including shift clusters, timing, score, and affected DOM elements. Prioritize shifts by size and replay animations to understand load-phase CLS issues.

## Prompt

Open Chrome DevTools Performance panel. Record a new trace by reloading the page. In the results, locate the Layout Shifts track populated with purple bars representing Layout Shift clusters. Click on individual diamonds to view shift animations and details. Use the Summary panel to review start time, shift score, and shifted elements. Examine the Layout shift culprits insight in the Insights panel for total CLS and possible reasons. Prioritize inspection by diamond size, which is proportional to shift magnitude.

## Objective

Identify and inspect layout shift details at the element level during page load
## Applicable Signals

- CLS score discrepancy between lab and field tools
- Need for element-level shift attribution
- Reproducible load-phase performance issue

## Contraindications

- Analyzing post-load CLS without user interaction replay
- Investigating field-only issues without lab reproduction capability
- Debugging shifts that occur only under specific user interactions not captured in standard reload

## Workflow Steps

- {'step': 1, 'action': 'Open Chrome DevTools and navigate to the Performance tab'}
- {'step': 2, 'action': 'Click the record button and reload the page to capture a full trace'}
- {'step': 3, 'action': 'Locate the Layout Shifts track in the results (purple bars and diamonds)'}
- {'step': 4, 'action': 'Click on individual diamonds to trigger shift animation and view Summary panel details'}
- {'step': 5, 'action': 'Review start time, shift score, and list of shifted elements in the Summary view'}
- {'step': 6, 'action': 'Consult the Layout shift culprits insight in the Insights panel for aggregated CLS and root cause hints'}
- {'step': 7, 'action': 'Prioritize investigation by diamond size; larger diamonds indicate larger shifts'}

## Constraints

- Requires Chrome browser with DevTools access
- Page must be reproducibly loadable in lab environment
- Shifts must occur during initial page load to be captured in standard trace recording

## Cautions

- Post-load CLS may not appear in standard reload traces; use live metrics view for interaction-driven shifts
- Shift cluster grouping is automatic; individual diamonds within clusters show granular shift events
- Animation replay is transient; take notes on shift details before closing the panel

## Output Contract

- Annotated list of shifted elements with timing, shift score, cluster grouping, and visual confirmation via animation replay. Caller receives element identifiers, shift magnitude, and temporal sequence to guide remediation.

## Example Executions

### Example 1

- Input: Page reload with visible layout instability during load
- Output: DevTools trace showing Layout Shifts track with 3 clusters; largest shift (0.15 score) at 2.3s affecting banner element; second shift (0.08 score) at 3.1s affecting sidebar; third shift (0.05 score) at 4.2s affecting footer
- Notes: Diamond size proportional to shift score; clicking each diamond replays the animation showing the exact element movement

## Triggers

- Debugging load-phase CLS issues
- Need to identify which DOM elements shift and when
- Have access to Chrome DevTools and can reproduce the page load

## Examples

### Example 1

Input:

  Page reload with visible layout instability during load

Output:

  DevTools trace showing Layout Shifts track with 3 clusters; largest shift (0.15 score) at 2.3s affecting banner element; second shift (0.08 score) at 3.1s affecting sidebar; third shift (0.05 score) at 4.2s affecting footer

Notes:

  Diamond size proportional to shift score; clicking each diamond replays the animation showing the exact element movement
