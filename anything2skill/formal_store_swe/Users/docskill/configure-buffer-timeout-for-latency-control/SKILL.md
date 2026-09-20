---
id: "a81372ca-fd60-54ae-ac62-332a1e30474d"
name: "Configure Buffer Timeout for Latency Control"
description: "Select and apply a baseline offset strategy to control how stacked series are positioned relative to zero or each other. Choose from expand (normalize 0–1), diverging (positive above, negative below zero), none (zero baseline), silhouette (center around zero), or wiggle (minimize streamgraph oscillation)."
version: "0.1.1"
tags:
  - "d3"
  - "stacking"
  - "layout"
  - "baseline"
  - "offset"
  - "visualization"
triggers:
  - "need to optimize latency or throughput trade-off in streaming job"
  - "before job submission or on specific operators"
examples:
  - input: "Stacked bar chart with values [10, 20, 30] for three series; need proportional display"
    output: "Apply d3.stackOffsetExpand; baseline normalized to 0, topline to 1; each series scaled proportionally"
    notes: "Useful for 100% stacked charts"
  - input: "Streamgraph with positive and negative values; want centered layout"
    output: "Apply d3.stackOffsetSilhouette; stack centered around zero baseline"
    notes: "Reduces visual bias toward top or bottom"
  - input: "Diverging stacked bar with gains and losses"
    output: "Apply d3.stackOffsetDiverging; positive values above zero, negative below"
    notes: "Preserves semantic meaning of direction"
---

# Configure Buffer Timeout for Latency Control

Select and apply a baseline offset strategy to control how stacked series are positioned relative to zero or each other. Choose from expand (normalize 0–1), diverging (positive above, negative below zero), none (zero baseline), silhouette (center around zero), or wiggle (minimize streamgraph oscillation).

## Prompt

Identify the desired baseline alignment for your stacked layout. Apply the corresponding offset strategy using d3.stackOffset* function. Verify that the baseline and topline values reflect the chosen rule.

## Objective

Apply baseline offset rule to stack layout
## Applicable Signals

- Multiple series stacked together
- Baseline positioning affects visual balance
- Layout strategy not yet determined

## Contraindications

- Offset strategy already applied to stack generator
- Single series (no stacking required)
- Zero baseline is sufficient for use case

## Workflow Steps

- Determine baseline alignment requirement (expand, diverging, none, silhouette, or wiggle)
- Select corresponding d3.stackOffset* function
- Apply offset to stack generator via stack.offset()
- Generate stack and verify baseline and topline values match chosen strategy

## Constraints

- Must be applied before stack generation
- Incompatible with manual baseline adjustment
- Choice affects all series in the stack uniformly

## Output Contract

- Stack generator with selected offset strategy applied
- Baseline and topline values adjusted according to chosen rule
- Ready for data binding and rendering

## Example Executions

### Example 1

- Input: Stacked bar chart with values [10, 20, 30] for three series; need proportional display
- Output: Apply d3.stackOffsetExpand; baseline normalized to 0, topline to 1; each series scaled proportionally
- Notes: Useful for 100% stacked charts

### Example 2

- Input: Streamgraph with positive and negative values; want centered layout
- Output: Apply d3.stackOffsetSilhouette; stack centered around zero baseline
- Notes: Reduces visual bias toward top or bottom

### Example 3

- Input: Diverging stacked bar with gains and losses
- Output: Apply d3.stackOffsetDiverging; positive values above zero, negative below
- Notes: Preserves semantic meaning of direction

## Triggers

- need to optimize latency or throughput trade-off in streaming job
- before job submission or on specific operators

## Examples

### Example 1

Input:

  Stacked bar chart with values [10, 20, 30] for three series; need proportional display

Output:

  Apply d3.stackOffsetExpand; baseline normalized to 0, topline to 1; each series scaled proportionally

Notes:

  Useful for 100% stacked charts

### Example 2

Input:

  Streamgraph with positive and negative values; want centered layout

Output:

  Apply d3.stackOffsetSilhouette; stack centered around zero baseline

Notes:

  Reduces visual bias toward top or bottom

### Example 3

Input:

  Diverging stacked bar with gains and losses

Output:

  Apply d3.stackOffsetDiverging; positive values above zero, negative below

Notes:

  Preserves semantic meaning of direction
