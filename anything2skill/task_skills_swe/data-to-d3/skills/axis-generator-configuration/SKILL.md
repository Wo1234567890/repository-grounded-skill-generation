---
id: "d30ab8ff-b8d7-5e2c-99c5-2d0c7810e3d1"
name: "Axis Generator Configuration"
description: "Configure and generate human-readable reference marks (axes) for data scales in D3 visualizations. Supports orientation selection, tick customization, formatting, and sizing."
version: "0.1.0"
tags:
  - "d3"
  - "axis"
  - "scale"
  - "visualization"
  - "rendering"
  - "tick"
triggers:
  - "Building a chart or plot that requires labeled axes"
  - "Need to control tick placement, formatting, size, or padding"
  - "Rendering a scale-based visualization with reference marks"
---

# Axis Generator Configuration

Configure and generate human-readable reference marks (axes) for data scales in D3 visualizations. Supports orientation selection, tick customization, formatting, and sizing.

## Prompt

To create an axis: (1) Select an orientation (top, right, bottom, or left) and instantiate the corresponding axis generator. (2) Bind a scale to the axis using axis.scale(). (3) Customize tick generation via axis.ticks() or axis.tickArguments(), or set explicit values with axis.tickValues(). (4) Format tick labels with axis.tickFormat(). (5) Control tick appearance using axis.tickSize(), axis.tickSizeInner(), axis.tickSizeOuter(), and axis.tickPadding(). (6) Apply axis.offset() for crisp rendering if needed. (7) Call the axis generator on a D3 selection to render.

## Objective

Create and customize axis generators for scale visualization
## Applicable Signals

- Chart construction phase initiated
- Scale object available and bound
- Axis orientation requirement specified

## Contraindications

- Axis is not needed for the visualization
- Working with non-scale-based visual elements
- Rendering without reference marks or labels

## Workflow Steps

- {'step': 1, 'action': 'Select axis orientation', 'detail': 'Choose d3.axisTop, d3.axisRight, d3.axisBottom, or d3.axisLeft based on desired placement'}
- {'step': 2, 'action': 'Bind scale to axis', 'detail': 'Call axis.scale(scaleObject) to attach the data scale'}
- {'step': 3, 'action': 'Customize tick generation', 'detail': 'Use axis.ticks(), axis.tickArguments(), or axis.tickValues() to control tick placement and count'}
- {'step': 4, 'action': 'Format tick labels', 'detail': 'Apply axis.tickFormat(formatter) to customize label appearance'}
- {'step': 5, 'action': 'Configure tick sizing and spacing', 'detail': 'Set axis.tickSize(), axis.tickSizeInner(), axis.tickSizeOuter(), and axis.tickPadding() as needed'}
- {'step': 6, 'action': 'Apply offset for rendering', 'detail': 'Call axis.offset(pixels) if crisp edges are required'}
- {'step': 7, 'action': 'Render to selection', 'detail': 'Invoke the configured axis generator on a D3 selection to produce the rendered axis'}

## Constraints

- Scale must be bound before axis generation
- Orientation must be one of: top, right, bottom, left
- Tick customization must be applied before rendering to selection

## Cautions

- Ensure scale domain and range are properly configured before binding to axis
- Tick formatting should match the data type and scale type
- Offset adjustment may be necessary for pixel-perfect rendering on certain browsers

## Output Contract

- Rendered axis with correctly positioned ticks, formatted labels, and specified sizing applied to a D3 selection; axis is ready for display in the visualization

## Triggers

- Building a chart or plot that requires labeled axes
- Need to control tick placement, formatting, size, or padding
- Rendering a scale-based visualization with reference marks
