---
id: "5bd92157-0311-5678-a200-c27eb8b66cfb"
name: "Radial Line Generator Configuration"
description: "Configure and generate radial (polar) line paths from datasets using angle and radius accessors instead of Cartesian x/y coordinates. Produces SVG path strings or canvas commands suitable for radar charts, circular time series, and other polar visualizations."
version: "0.1.0"
tags:
  - "d3"
  - "visualization"
  - "polar_coordinates"
  - "radial_chart"
  - "path_generation"
  - "radar_chart"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Creating radial or polar line charts (radar charts, circular time series)"
  - "Data naturally maps to angle and radius dimensions"
  - "Need to render connected points in polar coordinate space"
---

# Radial Line Generator Configuration

Configure and generate radial (polar) line paths from datasets using angle and radius accessors instead of Cartesian x/y coordinates. Produces SVG path strings or canvas commands suitable for radar charts, circular time series, and other polar visualizations.

## Prompt

1. Create a radial line generator using d3.lineRadial().
2. Set the angle accessor via lineRadial.angle() to map data values to angular position (0–2π radians).
3. Set the radius accessor via lineRadial.radius() to map data values to distance from origin.
4. Optionally configure lineRadial.defined() to handle missing or invalid data points.
5. Optionally set lineRadial.curve() to control interpolation behavior (e.g., curveLinear, curveCardinal).
6. Optionally set lineRadial.context() to render directly to a canvas context instead of returning an SVG path string.
7. Call the generator with your dataset to produce the polar path output.
8. Render the output on a radial axis system or canvas.

## Objective

Generate polar coordinate line paths with angle and radius mapping
## Applicable Signals

- Dataset with angular and radial components
- Requirement for polar visualization
- Multi-series radial chart construction

## Contraindications

- Working with Cartesian coordinates (use standard line generator instead)
- Rendering area charts in polar space (use areaRadial)
- Static or pre-computed paths that do not require dynamic generation

## Workflow Steps

- {'step': 1, 'action': 'Instantiate radial line generator', 'detail': 'Call d3.lineRadial() to create a new generator instance'}
- {'step': 2, 'action': 'Configure angle accessor', 'detail': 'Use lineRadial.angle(d => ...) to extract or compute angular position from each data element'}
- {'step': 3, 'action': 'Configure radius accessor', 'detail': 'Use lineRadial.radius(d => ...) to extract or compute radial distance from each data element'}
- {'step': 4, 'action': 'Optional: set defined condition', 'detail': 'Use lineRadial.defined(d => ...) to exclude null, undefined, or invalid points'}
- {'step': 5, 'action': 'Optional: set curve interpolator', 'detail': 'Use lineRadial.curve(curveType) to control smoothing (e.g., curveLinear, curveCardinal)'}
- {'step': 6, 'action': 'Optional: set rendering context', 'detail': 'Use lineRadial.context(canvasContext) to render directly to canvas instead of returning SVG path'}
- {'step': 7, 'action': 'Generate path', 'detail': 'Call the configured generator with your dataset: generator(data)'}
- {'step': 8, 'action': 'Render output', 'detail': 'Attach SVG path string to a <path> element or draw canvas commands to the target context'}

## Constraints

- Angle values must be in radians (0–2π range)
- Radius values must be non-negative
- Data must be sortable by angle for proper line continuity
- Defined accessor should filter out null or undefined data points before path generation

## Cautions

- Ensure angle accessor returns consistent units (radians, not degrees)
- Verify radius values are scaled appropriately for the target coordinate system
- Test curve interpolation behavior with sparse or non-uniformly distributed angular data

## Output Contract

- SVG path string (d attribute) or canvas drawing commands in polar coordinate space, ready for rendering on a radial axis system. Output is a continuous line connecting all defined data points in angular order.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Creating radial or polar line charts (radar charts, circular time series)
- Data naturally maps to angle and radius dimensions
- Need to render connected points in polar coordinate space
