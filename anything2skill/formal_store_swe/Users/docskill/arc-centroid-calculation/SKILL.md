---
id: "5b460cb5-a73a-54bb-ba2d-d549c40ac27e"
name: "Arc Centroid Calculation"
description: "Compute the midpoint or centroid of an arc sector, useful for label positioning in pie and donut charts."
version: "0.1.0"
tags:
  - "arc"
  - "geometry"
  - "chart_rendering"
  - "label_positioning"
  - "pie_chart"
  - "donut_chart"
triggers:
  - "Need to position labels at the center of an arc sector"
  - "Placing pie slice labels or donut segment annotations"
  - "Calculating label anchor points for circular chart elements"
---

# Arc Centroid Calculation

Compute the midpoint or centroid of an arc sector, useful for label positioning in pie and donut charts.

## Prompt

Use arc.centroid() to calculate the [x, y] coordinates of an arc sector's midpoint. Pass the arc datum (with startAngle, endAngle, innerRadius, outerRadius properties) to the centroid method. The returned coordinates represent the geometric center of the arc sector and are suitable for direct placement of labels, text, or annotations.

## Objective

Calculate arc midpoint for label or annotation placement
## Applicable Signals

- Arc sector defined with startAngle, endAngle, innerRadius, outerRadius
- Label or annotation element needs positioning
- Pie or donut chart rendering in progress

## Contraindications

- Do not use for arc perimeter or arc length calculations
- Do not use for positioning elements outside the arc boundary
- Do not use when no label or annotation is needed
- Do not use for non-arc geometric shapes

## Intervention Moves

- Call arc.centroid(datum) with arc configuration
- Extract [x, y] from returned centroid coordinates
- Apply coordinates to label transform or positioning property

## Constraints

- Arc datum must include startAngle, endAngle, innerRadius, and outerRadius properties
- Centroid calculation assumes valid angle range (0 to 2π)
- Output coordinates are in the same coordinate system as the arc generator context

## Cautions

- Verify arc angles are in radians, not degrees
- Ensure innerRadius and outerRadius are non-negative and innerRadius ≤ outerRadius
- Test label positioning with actual data to confirm visual alignment

## Output Contract

- Returns [x, y] centroid coordinates representing the midpoint of the arc sector, ready for direct use in label positioning (e.g., text element transform or anchor point).

## Triggers

- Need to position labels at the center of an arc sector
- Placing pie slice labels or donut segment annotations
- Calculating label anchor points for circular chart elements
