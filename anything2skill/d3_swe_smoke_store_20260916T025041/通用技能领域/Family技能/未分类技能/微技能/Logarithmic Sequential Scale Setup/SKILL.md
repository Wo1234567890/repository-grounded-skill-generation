---
id: "5c1dfee0-caaa-5c6a-81fc-ea466ebcc119"
name: "Logarithmic Sequential Scale Setup"
description: "Create a sequential scale with logarithmic domain transformation to map continuous quantitative data spanning multiple orders of magnitude to a fixed interpolator output."
version: "0.1.0"
tags:
  - "d3"
  - "scale"
  - "sequential"
  - "logarithmic"
  - "data_mapping"
  - "quantitative"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Data exhibits exponential or power-law distribution"
  - "Values span multiple orders of magnitude (e.g., 1 to 1,000,000)"
  - "Need to compress wide-range quantitative data into a fixed interpolator"
---

# Logarithmic Sequential Scale Setup

Create a sequential scale with logarithmic domain transformation to map continuous quantitative data spanning multiple orders of magnitude to a fixed interpolator output.

## Prompt

Use d3.scaleSequentialLog to create a sequential scale that applies a logarithmic transform to the input domain. Set the interpolator via sequential.interpolator() and optionally configure the output range with sequential.range() or sequential.rangeRound(). This is useful when data exhibits exponential or power-law behavior.

## Objective

Apply logarithmic transform to sequential scale domain for multi-order-of-magnitude data encoding
## Applicable Signals

- domain_range_spans_orders_of_magnitude
- exponential_or_powerlaw_distribution_detected
- sequential_color_or_value_interpolation_required

## Contraindications

- Domain contains zero or negative values
- Linear scale is sufficient for the data distribution
- Domain is already log-transformed upstream

## Workflow Steps

- {'step': 1, 'action': 'Create logarithmic sequential scale', 'detail': 'Call d3.scaleSequentialLog() to instantiate the scale'}
- {'step': 2, 'action': 'Set interpolator', 'detail': 'Call sequential.interpolator(fn) to define the output mapping function'}
- {'step': 3, 'action': 'Configure output range (optional)', 'detail': 'Call sequential.range([min, max]) or sequential.rangeRound([min, max]) to set discrete output values'}
- {'step': 4, 'action': 'Verify scale readiness', 'detail': 'Test scale with sample domain values to confirm logarithmic transform and interpolation work as expected'}

## Constraints

- Input domain must contain only positive values
- Interpolator must be set before scale is used
- Output range must be compatible with interpolator type

## Cautions

- Logarithmic transform can obscure small absolute differences in low-magnitude regions
- Verify interpolator choice matches intended visual or data encoding

## Output Contract

- A logarithmic sequential scale object ready to accept positive domain values and produce interpolated outputs via the configured interpolator

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Data exhibits exponential or power-law distribution
- Values span multiple orders of magnitude (e.g., 1 to 1,000,000)
- Need to compress wide-range quantitative data into a fixed interpolator
