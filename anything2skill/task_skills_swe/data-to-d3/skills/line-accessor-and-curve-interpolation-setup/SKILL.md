---
id: "d8c989e7-2bde-5238-b242-6f8677974794"
name: "Line Accessor and Curve Interpolation Setup"
description: "Configure accessor functions and curve interpolation strategy for line generators to control how data fields map to visual coordinates and how points are connected."
version: "0.1.0"
tags:
  - "d3"
  - "line-generator"
  - "accessor"
  - "curve-interpolation"
  - "data-mapping"
  - "configuration"
triggers:
  - "Need to specify custom data field extraction (x, y, angle, radius)"
  - "Need to change curve interpolation strategy (linear, cardinal, monotone, etc.)"
  - "Preparing a line generator for non-default data structure or visual behavior"
---

# Line Accessor and Curve Interpolation Setup

Configure accessor functions and curve interpolation strategy for line generators to control how data fields map to visual coordinates and how points are connected.

## Prompt

Use this skill to set custom accessor functions (x, y for Cartesian; angle, radius for radial) and specify curve interpolation behavior (linear, cardinal, monotone, etc.) on a line generator instance. Call the appropriate accessor methods on the generator, then set the curve interpolator. The result is a configured generator ready for data binding.

## Objective

Configure data-to-visual mapping and interpolation behavior for line generators
## Applicable Signals

- Data fields do not match default x/y or angle/radius naming
- Curve smoothing or interpolation style requirement specified
- Line generator instance created but not yet bound to data

## Contraindications

- Using default accessors and linear interpolation with no custom data transformation
- Generator already bound to data; accessor changes may require rebinding
- Radial and Cartesian line generators have different accessor sets; do not mix

## Workflow Steps

- {'step': 1, 'action': 'Obtain or create a line generator instance (d3.line or d3.lineRadial)'}
- {'step': 2, 'action': 'Set x accessor (Cartesian) or angle accessor (radial) to extract or transform the horizontal/angular dimension from data'}
- {'step': 3, 'action': 'Set y accessor (Cartesian) or radius accessor (radial) to extract or transform the vertical/radial dimension from data'}
- {'step': 4, 'action': 'Set curve interpolator to control how points are connected (e.g., d3.curveLinear, d3.curveCardinal)'}
- {'step': 5, 'action': 'Optionally set defined accessor to mark which data points should be included in the line'}
- {'step': 6, 'action': 'Return or store the configured generator instance for data binding'}

## Constraints

- Accessor functions must return numeric values compatible with scale domains
- Curve interpolator must be a valid d3 curve factory (d3.curveLinear, d3.curveCardinal, etc.)
- Accessor and curve configuration must occur before data binding for predictable results

## Cautions

- Changing accessors or curve after data binding may require re-rendering
- Radial line generators use angle and radius; Cartesian use x and y; do not confuse the two
- Custom accessor functions should handle undefined or missing data gracefully

## Output Contract

- Line generator instance with configured accessors and curve interpolator, ready for data binding and path generation. The generator will extract specified fields from input data and produce a path string or context commands following the chosen interpolation strategy.

## Triggers

- Need to specify custom data field extraction (x, y, angle, radius)
- Need to change curve interpolation strategy (linear, cardinal, monotone, etc.)
- Preparing a line generator for non-default data structure or visual behavior
