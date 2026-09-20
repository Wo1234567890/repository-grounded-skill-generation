---
id: "8cb6498a-ea10-5f4c-8f97-085638ab5d72"
name: "Area Edge Line Extraction"
description: "Extract individual line generators for the edges (baseline, topline, or radius boundaries) of an area shape. Use when you need to render or manipulate area boundaries as separate line elements."
version: "0.1.0"
tags:
  - "d3"
  - "geometry"
  - "area"
  - "line"
  - "edge"
  - "visualization"
triggers:
  - "Need to stroke or style area edges separately"
  - "Want to extract baseline or topline as independent line paths"
  - "Building composite visualizations with area boundaries as distinct elements"
---

# Area Edge Line Extraction

Extract individual line generators for the edges (baseline, topline, or radius boundaries) of an area shape. Use when you need to render or manipulate area boundaries as separate line elements.

## Prompt

Call the appropriate line accessor on a configured area generator to derive a line generator for one edge. For Cartesian areas, use lineX0 (left/baseline x), lineY0 (top/baseline y), lineX1 (right/topline x), or lineY1 (bottom/topline y). For radial areas, use lineStartAngle, lineInnerRadius, lineEndAngle, or lineOuterRadius. The returned line generator accepts the same dataset and produces a path for that edge only.

## Objective

Derive line geometry from area boundaries
## Applicable Signals

- Area generator is configured and ready
- Dataset is prepared for line rendering
- Edge styling or manipulation is required

## Contraindications

- Rendering complete area fill without edge separation
- Edge lines are not needed or area is already decomposed
- Performance-critical context where edge extraction overhead is unacceptable

## Workflow Steps

- {'step': 1, 'action': 'Identify area type (Cartesian or radial) and which edge is needed'}
- {'step': 2, 'action': 'Call the corresponding line accessor (lineX0, lineY0, lineX1, lineY1 for Cartesian; lineStartAngle, lineInnerRadius, lineEndAngle, lineOuterRadius for radial)'}
- {'step': 3, 'action': 'Receive line generator object'}
- {'step': 4, 'action': 'Pass dataset to line generator to produce path string or render to context'}

## Constraints

- Line generator must be called on an already-configured area or areaRadial instance
- Dataset passed to the derived line generator must match the structure expected by the parent area
- Curve interpolator and context settings are inherited from the parent area

## Cautions

- Derived line generators share state with the parent area; changes to parent accessors affect derived lines
- Output precision (digits) is inherited from parent area configuration

## Output Contract

- Line generator object ready to accept dataset and produce a path string or render to a specified context. Output is a single line path representing one edge of the original area.

## Triggers

- Need to stroke or style area edges separately
- Want to extract baseline or topline as independent line paths
- Building composite visualizations with area boundaries as distinct elements
