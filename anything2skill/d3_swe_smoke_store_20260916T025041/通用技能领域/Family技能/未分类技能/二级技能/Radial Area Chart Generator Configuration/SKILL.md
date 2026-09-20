---
id: "c4b070f7-80ef-5335-a5b3-d46760112ac4"
name: "Radial Area Chart Generator Configuration"
description: "Configure and generate radial (polar) area chart shapes by setting angle and radius accessors, curve interpolation, and rendering context. Use this skill when building polar coordinate visualizations that require binding angle and radius accessors instead of Cartesian x/y coordinates."
version: "0.1.0"
tags:
  - "d3"
  - "visualization"
  - "radial_chart"
  - "polar_coordinates"
  - "area_chart"
  - "shape_generation"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "building radial or polar area charts"
  - "need to bind angle and radius accessors instead of Cartesian x/y coordinates"
  - "rendering data in polar coordinate space"
---

# Radial Area Chart Generator Configuration

Configure and generate radial (polar) area chart shapes by setting angle and radius accessors, curve interpolation, and rendering context. Use this skill when building polar coordinate visualizations that require binding angle and radius accessors instead of Cartesian x/y coordinates.

## Prompt

Create a radial area generator by instantiating d3.areaRadial(). Set the angle accessors (startAngle, endAngle) and radius accessors (innerRadius, outerRadius) to map data fields to polar coordinates. Apply curve interpolation and rendering context as needed. Chain accessor methods to configure the generator before passing a dataset to produce radial path output.

## Objective

produce a configured radial area generator for polar coordinate rendering
## Applicable Signals

- dataset with angular and radial dimensions
- requirement for polar visualization
- need for configurable curve interpolation in radial space

## Contraindications

- working with Cartesian coordinate systems
- rendering non-radial shapes
- data is pre-rendered or already in path format

## Workflow Steps

- {'step': 1, 'action': 'Instantiate radial area generator', 'detail': 'Call d3.areaRadial() to create a new generator instance'}
- {'step': 2, 'action': 'Configure angle accessors', 'detail': 'Use areaRadial.startAngle() and areaRadial.endAngle() to bind data fields to angular dimensions, or use areaRadial.angle() to set both simultaneously'}
- {'step': 3, 'action': 'Configure radius accessors', 'detail': 'Use areaRadial.innerRadius() and areaRadial.outerRadius() to bind data fields to radial dimensions, or use areaRadial.radius() to set both simultaneously'}
- {'step': 4, 'action': 'Set curve interpolation', 'detail': 'Call areaRadial.curve() to specify interpolation method (e.g., curveLinear, curveCardinal)'}
- {'step': 5, 'action': 'Set rendering context if needed', 'detail': 'Call areaRadial.context() to specify canvas or SVG rendering target; omit for path string output'}
- {'step': 6, 'action': 'Pass dataset to generator', 'detail': 'Invoke the configured generator with dataset array to produce radial path output'}

## Constraints

- angle accessors must map to numeric values in radians or degrees
- radius accessors must map to non-negative numeric values
- curve interpolator must be compatible with radial geometry

## Cautions

- Ensure angle values are in consistent units (radians or degrees) across all accessors
- Verify radius values are non-negative; negative values may produce unexpected geometry
- Test curve interpolation visually; some curves may not suit radial geometry

## Output Contract

- Returns a configured radial area generator object with angle and radius accessors and curve settings applied, ready to accept a dataset and produce radial path output (SVG path string or canvas drawing commands)

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- building radial or polar area charts
- need to bind angle and radius accessors instead of Cartesian x/y coordinates
- rendering data in polar coordinate space
