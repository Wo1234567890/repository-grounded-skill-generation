---
id: "c98e0c2a-9dbf-5858-9874-398d962b4cc9"
name: "Scale Domain Normalization"
description: "Extend the scale domain to nice round numbers for cleaner axis presentation. Use when preparing scales for publication or when exact domain boundaries are less important than readability."
version: "0.1.0"
tags:
  - "scale"
  - "domain"
  - "axis"
  - "normalization"
  - "quantitative"
  - "visualization"
triggers:
  - "domain is computed from data and has irregular boundaries"
  - "need cleaner axis labels for visualization"
  - "preparing publication-ready visualizations"
---

# Scale Domain Normalization

Extend the scale domain to nice round numbers for cleaner axis presentation. Use when preparing scales for publication or when exact domain boundaries are less important than readability.

## Prompt

Call this skill to round the domain boundaries of a quantitative scale to the nearest nice round numbers. This improves axis label readability without requiring manual domain specification. The operation extends the domain slightly outward to encompass the nearest round values.

## Objective

adjust domain boundaries to round values
## Applicable Signals

- scale domain contains fractional or irregular values
- axis labels need human-readable formatting
- visualization is in final preparation phase

## Contraindications

- exact domain boundaries are required for accuracy
- domain is already normalized to round numbers
- working with categorical or ordinal scales

## Workflow Steps

- {'step': 1, 'action': 'invoke nice() on the scale instance', 'detail': 'call scale.nice() to extend domain to round boundaries'}
- {'step': 2, 'action': 'verify domain boundaries', 'detail': 'confirm that extended domain aligns with axis label requirements'}
- {'step': 3, 'action': 'regenerate axis or ticks if needed', 'detail': 'recompute tick positions and labels to reflect new domain'}

## Constraints

- only applicable to quantitative scales
- extends domain outward; does not shrink it
- modifies domain only; does not affect range or interpolation

## Cautions

- domain extension may include values outside original data range
- verify that extended domain does not introduce misleading gaps or outliers in visualization

## Output Contract

- scale with extended domain using round number boundaries; domain is guaranteed to encompass original data range and align to round values

## Triggers

- domain is computed from data and has irregular boundaries
- need cleaner axis labels for visualization
- preparing publication-ready visualizations
