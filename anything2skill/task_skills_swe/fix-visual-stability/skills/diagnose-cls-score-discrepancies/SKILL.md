---
id: "dff1010b-df20-5916-8391-8992ca879246"
name: "Diagnose CLS Score Discrepancies"
description: "Identify whether layout shifts occur during page load or post-load by comparing CrUX field data against lab-based Lighthouse measurements. Use this to pinpoint the source of CLS issues and determine investigation strategy."
version: "0.1.0"
tags:
  - "cls"
  - "layout_shift"
  - "performance_measurement"
  - "field_vs_lab"
  - "web_vitals"
triggers:
  - "CrUX and Lighthouse CLS scores differ significantly; need to isolate load-time versus post-interaction shifts"
examples:
  - input: "PageSpeed Insights shows CrUX CLS = 0.25, Lighthouse CLS = 0.05"
    output: "Discrepancy = 0.20 (large). Classification: primarily post-load shifts. Recommendation: collect field data and monitor live metrics for interaction-triggered shifts."
    notes: "Large discrepancy indicates user interactions after initial load are causing significant layout shifts."
  - input: "PageSpeed Insights shows CrUX CLS = 0.08, Lighthouse CLS = 0.07"
    output: "Discrepancy = 0.01 (small). Classification: primarily load-phase shifts. Recommendation: use Lighthouse diagnostics and DevTools Layout Shifts track to identify culprits."
    notes: "Small discrepancy indicates most shifts occur during initial page load."
---

# Diagnose CLS Score Discrepancies

Identify whether layout shifts occur during page load or post-load by comparing CrUX field data against lab-based Lighthouse measurements. Use this to pinpoint the source of CLS issues and determine investigation strategy.

## Prompt

Compare CrUX user-perceived CLS (full page lifecycle) against Lighthouse lab-based load CLS (initial load only). Significant differences indicate post-load shifts. Use PageSpeed Insights to view both metrics side-by-side: field CLS in 'Discover what your real users are experiencing' section and lab CLS in 'Diagnose performance issues' section. Classify the discrepancy magnitude and identify whether shifts are load-phase or post-load. For post-load issues, escalate to field data collection and live metrics monitoring.

## Objective

Determine CLS source (load vs. post-load)
## Applicable Signals

- CrUX and Lighthouse CLS scores differ significantly
- Need to isolate load-time versus post-interaction shifts
- PageSpeed Insights shows conflicting field and lab metrics

## Contraindications

- Performing real-time performance optimization (use targeted fix skills instead)
- Already confirmed shift timing from prior analysis
- No access to field data or CrUX dataset

## Workflow Steps

- {'step': 1, 'action': 'Retrieve CrUX field CLS score', 'detail': "Access PageSpeed Insights 'Discover what your real users are experiencing' section to obtain user-perceived CLS measured across full page lifecycle."}
- {'step': 2, 'action': 'Retrieve Lighthouse lab CLS score', 'detail': "Access PageSpeed Insights 'Diagnose performance issues' section to obtain lab-based load CLS from initial page load measurement."}
- {'step': 3, 'action': 'Compare scores and calculate discrepancy', 'detail': 'Compute difference between CrUX and Lighthouse values. Significant difference (typically >0.05) indicates post-load shifts.'}
- {'step': 4, 'action': 'Classify CLS source', 'detail': 'If discrepancy is small, shifts are primarily load-phase. If discrepancy is large, shifts are primarily post-load.'}
- {'step': 5, 'action': 'Document culprit category and next steps', 'detail': 'For load CLS: use Lighthouse detailed diagnostics and DevTools Performance panel Layout Shifts track. For post-load CLS: escalate to field data collection and live metrics monitoring.'}

## Constraints

- Requires access to PageSpeed Insights and CrUX dataset
- Lighthouse measurements reflect controlled lab environment; post-load shifts may not be fully captured
- Field data collection needed for post-load diagnosis; live metrics view requires manual page interaction

## Cautions

- Do not assume all discrepancies are post-load; verify with DevTools Performance panel first
- CrUX data reflects aggregated user behavior; individual sessions may vary significantly
- Post-load shifts can be tricky to track without field data; consider implementing field monitoring before optimization

## Output Contract

- Clear classification of CLS as load-phase or post-load, with identified discrepancy magnitude (numeric difference between CrUX and Lighthouse scores) and likely culprit category (e.g., ad injection, lazy-loaded content, user interaction). Handoff to load-phase diagnostics (DevTools Performance panel) or post-load investigation (field data collection and live metrics monitoring).

## Example Executions

### Example 1

- Input: PageSpeed Insights shows CrUX CLS = 0.25, Lighthouse CLS = 0.05
- Output: Discrepancy = 0.20 (large). Classification: primarily post-load shifts. Recommendation: collect field data and monitor live metrics for interaction-triggered shifts.
- Notes: Large discrepancy indicates user interactions after initial load are causing significant layout shifts.

### Example 2

- Input: PageSpeed Insights shows CrUX CLS = 0.08, Lighthouse CLS = 0.07
- Output: Discrepancy = 0.01 (small). Classification: primarily load-phase shifts. Recommendation: use Lighthouse diagnostics and DevTools Layout Shifts track to identify culprits.
- Notes: Small discrepancy indicates most shifts occur during initial page load.

## Triggers

- CrUX and Lighthouse CLS scores differ significantly; need to isolate load-time versus post-interaction shifts

## Examples

### Example 1

Input:

  PageSpeed Insights shows CrUX CLS = 0.25, Lighthouse CLS = 0.05

Output:

  Discrepancy = 0.20 (large). Classification: primarily post-load shifts. Recommendation: collect field data and monitor live metrics for interaction-triggered shifts.

Notes:

  Large discrepancy indicates user interactions after initial load are causing significant layout shifts.

### Example 2

Input:

  PageSpeed Insights shows CrUX CLS = 0.08, Lighthouse CLS = 0.07

Output:

  Discrepancy = 0.01 (small). Classification: primarily load-phase shifts. Recommendation: use Lighthouse diagnostics and DevTools Layout Shifts track to identify culprits.

Notes:

  Small discrepancy indicates most shifts occur during initial page load.
