---
id: "aab3ffd4-b361-5219-99d6-6887211ba633"
name: "Validate typical user flows for CLS regression using Lighthouse"
description: "Use Lighthouse's timespans user flow mode to test that common user interactions do not introduce new layout shifts during page lifecycle. This skill ensures that after CLS fixes are applied, typical user flows such as scrolling, clicking, and form submission do not regress cumulative layout shift metrics."
version: "0.1.0"
tags:
  - "web_performance"
  - "cls"
  - "layout_shift"
  - "lighthouse"
  - "regression_testing"
  - "user_flow"
triggers:
  - "After CLS fixes are applied; team wants to ensure typical user flows (scroll, click, form submission) do not regress CLS"
---

# Validate typical user flows for CLS regression using Lighthouse

Use Lighthouse's timespans user flow mode to test that common user interactions do not introduce new layout shifts during page lifecycle. This skill ensures that after CLS fixes are applied, typical user flows such as scrolling, clicking, and form submission do not regress cumulative layout shift metrics.

## Prompt

1. Open Lighthouse in your browser DevTools or CLI.
2. Switch to timespans user flow mode.
3. Record or define typical user flows for your page (e.g., scroll interactions, button clicks, form submissions).
4. Run Lighthouse with the recorded user flow.
5. Review the CLS metrics in the generated report.
6. Confirm that CLS values remain stable and do not exceed acceptable thresholds.
7. Establish baseline CLS values for future regression detection.

## Objective

validate_cls_stability_across_flows
## Applicable Signals

- CLS fixes have been applied to the page
- Team wants to ensure typical user flows do not introduce new layout shifts
- Regression testing infrastructure is available
- Defined typical user flows exist for the page

## Contraindications

- Initial CLS diagnosis is still in progress
- Page has no defined typical user flows
- Testing infrastructure or Lighthouse access is not available
- CLS root causes have not yet been identified

## Workflow Steps

- Identify and document typical user flows (scroll, click, form submission, etc.)
- Access Lighthouse timespans user flow mode
- Record or configure user flow interactions
- Execute Lighthouse test with the recorded flow
- Capture CLS metrics from the report
- Compare against baseline or acceptable thresholds
- Document results and establish baseline for future regression detection

## Constraints

- Lighthouse must be available (DevTools or CLI)
- Timespans user flow mode must be supported in the Lighthouse version
- User flows must be representative of actual user behavior
- Testing environment should match production as closely as possible

## Output Contract

- Lighthouse report with CLS metrics for the recorded user flow timespans
- Confirmation that CLS does not regress
- Baseline CLS values established for future regression detection

## Triggers

- After CLS fixes are applied; team wants to ensure typical user flows (scroll, click, form submission) do not regress CLS
