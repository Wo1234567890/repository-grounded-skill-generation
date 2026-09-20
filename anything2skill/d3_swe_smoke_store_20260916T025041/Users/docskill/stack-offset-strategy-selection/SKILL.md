---
id: "677162cf-e759-597c-8cea-1dcd6234a3a0"
name: "Stack Offset Strategy Selection"
description: "Select and apply a stacking offset strategy to control baseline and topline positioning in stacked visualizations. Supports normalization (0–1 range), diverging (positive/negative split), zero baseline, silhouette centering, or wiggle minimization."
version: "0.1.0"
tags:
  - "d3"
  - "stacking"
  - "layout"
  - "offset"
  - "visualization"
  - "data_transformation"
triggers:
  - "Configuring stack offset for stacked visualization"
  - "Need to normalize baseline and topline positioning"
  - "Require diverging layout for positive/negative values"
  - "Streamgraph or area chart layout configuration"
examples:
  - input: "Stacked area chart with values [10, 20, 30] per series; goal is normalized 0–1 range"
    output: "Apply d3.stackOffsetExpand; baseline at 0, topline at 1, all series proportionally scaled"
    notes: "Useful for comparing relative proportions across stacks"
  - input: "Streamgraph with positive and negative values; goal is centered layout"
    output: "Apply d3.stackOffsetSilhouette; stack centered around zero, minimizing visual drift"
    notes: "Improves readability of streamgraph by reducing baseline movement"
  - input: "Diverging bar chart with positive/negative values; goal is split around zero"
    output: "Apply d3.stackOffsetDiverging; positive values above zero, negative below"
    notes: "Standard for diverging visualizations"
---

# Stack Offset Strategy Selection

Select and apply a stacking offset strategy to control baseline and topline positioning in stacked visualizations. Supports normalization (0–1 range), diverging (positive/negative split), zero baseline, silhouette centering, or wiggle minimization.

## Prompt

Choose an offset strategy based on your visualization goal: use Expand to normalize to 0–1 range, Diverging for positive/negative split around zero, None for zero baseline, Silhouette to center around zero, or Wiggle to minimize streamgraph oscillation. Apply the selected offset function to your stack generator.

## Objective

Choose baseline and topline normalization strategy for visual layout
## Applicable Signals

- Stack generator created and ready for offset configuration
- Dataset contains series requiring baseline adjustment
- Visualization type is stacked bar, area, or streamgraph

## Contraindications

- Offset already applied to stack
- No baseline adjustment needed
- Single-series data (offset not applicable)

## Workflow Steps

- Identify visualization goal and data characteristics (normalized, diverging, centered, or wiggle-optimized)
- Select appropriate offset strategy: Expand, Diverging, None, Silhouette, or Wiggle
- Apply offset function to stack generator via stack.offset()
- Verify baseline and topline positioning matches intended layout

## Constraints

- Offset must be applied before stack generation
- Only one offset strategy per stack generator
- Offset choice affects all series in the stack

## Cautions

- Expand strategy normalizes all values; use only when relative proportions matter
- Diverging strategy requires both positive and negative values for meaningful layout
- Wiggle minimization may not preserve exact value magnitudes

## Output Contract

- Stack offset function applied; baseline and topline positioned according to selected strategy. Downstream stack generation will use this offset configuration.

## Example Therapist Responses

### Example 1

- Client/Input: Stacked area chart with values [10, 20, 30] per series; goal is normalized 0–1 range
- Therapist/Output: Apply d3.stackOffsetExpand; baseline at 0, topline at 1, all series proportionally scaled
- Notes: Useful for comparing relative proportions across stacks

### Example 2

- Client/Input: Streamgraph with positive and negative values; goal is centered layout
- Therapist/Output: Apply d3.stackOffsetSilhouette; stack centered around zero, minimizing visual drift
- Notes: Improves readability of streamgraph by reducing baseline movement

### Example 3

- Client/Input: Diverging bar chart with positive/negative values; goal is split around zero
- Therapist/Output: Apply d3.stackOffsetDiverging; positive values above zero, negative below
- Notes: Standard for diverging visualizations

## Triggers

- Configuring stack offset for stacked visualization
- Need to normalize baseline and topline positioning
- Require diverging layout for positive/negative values
- Streamgraph or area chart layout configuration

## Examples

### Example 1

Input:

  Stacked area chart with values [10, 20, 30] per series; goal is normalized 0–1 range

Output:

  Apply d3.stackOffsetExpand; baseline at 0, topline at 1, all series proportionally scaled

Notes:

  Useful for comparing relative proportions across stacks

### Example 2

Input:

  Streamgraph with positive and negative values; goal is centered layout

Output:

  Apply d3.stackOffsetSilhouette; stack centered around zero, minimizing visual drift

Notes:

  Improves readability of streamgraph by reducing baseline movement

### Example 3

Input:

  Diverging bar chart with positive/negative values; goal is split around zero

Output:

  Apply d3.stackOffsetDiverging; positive values above zero, negative below

Notes:

  Standard for diverging visualizations
