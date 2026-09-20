---
id: "22d2c5e0-7764-54f9-8a29-c939f45cc0d5"
name: "Line Generator Configuration"
description: "Configure and generate line paths from datasets using D3's line generator with customizable accessors for x, y, curve interpolation, and rendering context."
version: "0.1.0"
tags:
  - "d3"
  - "visualization"
  - "line-chart"
  - "path-generation"
  - "svg"
  - "canvas"
triggers:
  - "Need to create line or polyline visualizations from tabular datasets"
  - "Require mapping of data fields to x/y coordinates"
  - "Want to control curve smoothing or interpolation behavior"
---

# Line Generator Configuration

Configure and generate line paths from datasets using D3's line generator with customizable accessors for x, y, curve interpolation, and rendering context.

## Prompt

Use this skill to create line chart paths from tabular data. Initialize a line generator, set x and y accessors to map data fields to coordinates, optionally configure curve interpolation and rendering context, then invoke the generator on your dataset to produce SVG path strings or canvas drawing commands.

## Objective

Generate line chart paths with configurable data accessors and curve behavior
## Applicable Signals

- Dataset with numeric x and y values available
- Target output is SVG path or canvas rendering
- Cartesian coordinate system in use

## Contraindications

- Rendering area charts (use area generator instead)
- Working with non-Cartesian coordinate systems (use lineRadial for polar coordinates)
- Rendering pre-computed path strings without transformation
- Radial or angular line visualization required

## Workflow Steps

- {'step': 1, 'action': 'Create line generator', 'detail': 'Invoke d3.line() to instantiate a new line generator'}
- {'step': 2, 'action': 'Set x accessor', 'detail': 'Call line.x(accessor_function) to define how to extract x values from data elements'}
- {'step': 3, 'action': 'Set y accessor', 'detail': 'Call line.y(accessor_function) to define how to extract y values from data elements'}
- {'step': 4, 'action': 'Configure curve interpolation (optional)', 'detail': 'Call line.curve(curve_type) to set smoothing behavior (e.g., d3.curveLinear, d3.curveMonotoneX)'}
- {'step': 5, 'action': 'Set rendering context (optional)', 'detail': 'Call line.context(canvas_context) if rendering to canvas instead of SVG'}
- {'step': 6, 'action': 'Generate line path', 'detail': 'Invoke line(dataset) to produce SVG path string or canvas drawing commands'}

## Constraints

- Data must be iterable (array or similar collection)
- x and y accessor functions must return numeric values
- Curve interpolator must be compatible with D3 curve types
- Rendering context (if canvas) must be valid 2D context

## Cautions

- Ensure accessor functions handle missing or undefined values gracefully; use line.defined() to filter data points if needed
- Curve interpolation choice affects visual appearance; test with your data distribution
- Canvas context rendering is stateful; ensure context is properly initialized before invoking generator

## Output Contract

- Returns SVG path string (d attribute value) or executes canvas drawing commands on the configured context. Output is ready for direct insertion into SVG <path> element or canvas rendering.

## Triggers

- Need to create line or polyline visualizations from tabular datasets
- Require mapping of data fields to x/y coordinates
- Want to control curve smoothing or interpolation behavior
