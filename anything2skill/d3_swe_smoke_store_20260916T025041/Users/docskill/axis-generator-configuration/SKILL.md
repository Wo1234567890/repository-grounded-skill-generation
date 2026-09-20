---
id: "abeb590e-5462-5b96-95c0-99643c7f3394"
name: "Axis Generator Configuration"
description: "Configure and generate human-readable reference marks (axes) for data scales in D3 visualizations. Supports orientation selection, tick customization, formatting, and sizing."
version: "0.1.0"
tags:
  - "d3"
  - "visualization"
  - "axis"
  - "scale"
  - "rendering"
  - "chart_markup"
triggers:
  - "Building a chart or plot that requires labeled axes"
  - "Need to visualize scale reference marks with customizable tick marks"
  - "Require formatted axis labels and positioning control"
---

# Axis Generator Configuration

Configure and generate human-readable reference marks (axes) for data scales in D3 visualizations. Supports orientation selection, tick customization, formatting, and sizing.

## Prompt

To configure an axis generator: (1) Select orientation using d3.axisTop, d3.axisRight, d3.axisBottom, or d3.axisLeft. (2) Bind a scale using axis.scale(). (3) Customize ticks via axis.ticks(), axis.tickArguments(), or axis.tickValues(). (4) Set tick format with axis.tickFormat(). (5) Adjust tick sizing with axis.tickSize(), axis.tickSizeInner(), or axis.tickSizeOuter(). (6) Fine-tune spacing with axis.tickPadding() and axis.offset() for crisp rendering. (7) Apply the configured generator to a D3 selection to render the axis.

## Objective

Create and customize axis generators for scale visualization
## Applicable Signals

- Chart construction workflow initiated
- Scale object available and bound
- Axis orientation requirement specified

## Contraindications

- Axis is not needed for the visualization
- Data does not require scale reference marks
- Working with non-D3 visualization libraries
- Static or pre-rendered axis marks are sufficient

## Workflow Steps

- {'step': 1, 'action': 'Select axis orientation', 'detail': 'Choose one of d3.axisTop, d3.axisRight, d3.axisBottom, or d3.axisLeft based on chart layout'}
- {'step': 2, 'action': 'Bind scale to axis', 'detail': 'Call axis.scale(scaleObject) to attach the quantitative or ordinal scale'}
- {'step': 3, 'action': 'Configure tick generation', 'detail': 'Use axis.ticks(), axis.tickArguments(), or axis.tickValues() to control tick placement and count'}
- {'step': 4, 'action': 'Set tick format', 'detail': 'Apply axis.tickFormat(formatFunction) to customize label appearance'}
- {'step': 5, 'action': 'Adjust tick sizing', 'detail': 'Use axis.tickSize(), axis.tickSizeInner(), and axis.tickSizeOuter() to control visual dimensions'}
- {'step': 6, 'action': 'Fine-tune spacing and rendering', 'detail': 'Apply axis.tickPadding() for label spacing and axis.offset() for crisp edge alignment'}
- {'step': 7, 'action': 'Render axis to selection', 'detail': "Call selection.call(axis) or selection.append('g').call(axis) to apply the configured generator"}

## Constraints

- Scale must be defined and passed to axis.scale() before rendering
- Orientation must be selected from the four cardinal directions (top, right, bottom, left)
- Tick customization methods are mutually exclusive in some cases (e.g., tickValues overrides ticks)

## Cautions

- Offset adjustment (axis.offset()) should be used carefully to maintain crisp edge rendering
- Tick padding and size adjustments may affect label readability; test with target data range
- Format strings must be compatible with the scale's domain type

## Output Contract

- A configured axis generator object that can be applied to a D3 selection to render axis marks, labels, and ticks. The output is a callable function that, when invoked on a D3 selection, produces SVG elements representing the axis with all specified customizations.

## Triggers

- Building a chart or plot that requires labeled axes
- Need to visualize scale reference marks with customizable tick marks
- Require formatted axis labels and positioning control
