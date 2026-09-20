---
id: "35f30758-446c-51fe-9b26-fe9ef5810a3c"
name: "Arc Generator Configuration"
description: "Configure and generate circular or annular sectors for pie and donut charts by setting radius, angle, padding, and rendering parameters."
version: "0.1.0"
tags:
  - "d3"
  - "visualization"
  - "chart"
  - "pie"
  - "donut"
  - "arc"
triggers:
  - "Building pie charts or donut charts"
  - "Need to define circular or annular sector geometry"
  - "Require custom radius, angles, or padding for radial visualizations"
---

# Arc Generator Configuration

Configure and generate circular or annular sectors for pie and donut charts by setting radius, angle, padding, and rendering parameters.

## Prompt

Create an arc generator by calling d3.arc(). Configure the generator by chaining methods to set innerRadius, outerRadius, startAngle, endAngle, cornerRadius, padAngle, and padRadius. Call the configured generator with a datum to produce arc path data. Use arc.centroid() to compute the arc's midpoint for label placement.

## Objective

Create and customize arc shapes for chart visualization
## Applicable Signals

- Chart type is pie, donut, or radial sector
- Geometry requires inner and outer radius specification
- Angles and padding must be configurable per datum

## Contraindications

- Rendering non-circular shapes
- Working with linear or rectangular chart types
- No arc or sector geometry required

## Workflow Steps

- Instantiate arc generator using d3.arc()
- Set innerRadius (for donut charts) or leave at 0 (for pie charts)
- Set outerRadius to define the arc's outer boundary
- Set startAngle and endAngle in radians
- Optionally set cornerRadius for rounded corners
- Optionally set padAngle and padRadius for spacing between arcs
- Optionally set rendering context (canvas or SVG)
- Call configured generator with datum to produce arc path data
- Use arc.centroid() if label positioning is needed

## Constraints

- Arc generator must be configured before calling with datum
- Radius values must be non-negative numbers
- Angles must be in radians
- Context parameter is optional; defaults to canvas/SVG path context

## Cautions

- Ensure angles are in radians, not degrees
- padAngle affects spacing; verify visual result matches intent
- Context setting affects output format (SVG path vs. canvas commands)

## Output Contract

- Configured arc generator object capable of producing arc path data (SVG path string or canvas drawing commands) for given datum with specified inner/outer radius, start/end angles, and corner rounding. Generator is reusable across multiple data points.

## Triggers

- Building pie charts or donut charts
- Need to define circular or annular sector geometry
- Require custom radius, angles, or padding for radial visualizations
