---
id: "dacfa22e-9831-5265-bbfc-73dd5fd505dc"
name: "Pie Chart Angle Computation"
description: "Generate arc angles from tabular data for pie or donut chart visualization. Configures value mapping, sort order, angular bounds, and inter-arc padding to produce a complete angle layout."
version: "0.1.0"
tags:
  - "pie_chart"
  - "donut_chart"
  - "angle_computation"
  - "data_visualization"
  - "geometric_layout"
triggers:
  - "Need to render categorical or grouped data as pie or donut chart"
  - "Have tabular dataset with numeric values"
---

# Pie Chart Angle Computation

Generate arc angles from tabular data for pie or donut chart visualization. Configures value mapping, sort order, angular bounds, and inter-arc padding to produce a complete angle layout.

## Prompt

Use this skill to transform a dataset into pie or donut chart arc angles. Create a pie generator, configure value accessor, sort order, start/end angles, and padding between arcs. Output is an array of arc angle objects ready for path generation.

## Objective

Transform dataset into pie/donut chart arc angles
## Applicable Signals

- Need to render categorical or grouped data as pie or donut chart
- Have tabular dataset with numeric values
- Require arc angle layout for visualization

## Contraindications

- Data is continuous or time-series
- Chart type is not pie or donut
- Values are negative or zero-only
- Dataset lacks numeric value column

## Workflow Steps

- {'step': 1, 'action': 'Create pie generator', 'detail': 'Instantiate d3.pie() to initialize the generator'}
- {'step': 2, 'action': 'Configure value accessor', 'detail': 'Set pie.value() to map dataset records to numeric values'}
- {'step': 3, 'action': 'Set sort order', 'detail': 'Apply pie.sort() or pie.sortValues() to define arc ordering'}
- {'step': 4, 'action': 'Define angular bounds', 'detail': 'Set pie.startAngle() and pie.endAngle() for overall rotation and span'}
- {'step': 5, 'action': 'Configure inter-arc padding', 'detail': 'Set pie.padAngle() to add spacing between adjacent arcs'}
- {'step': 6, 'action': 'Compute arc angles', 'detail': 'Call pie(dataset) to generate array of arc angle objects'}

## Constraints

- All dataset values must be non-negative numbers
- Dataset must contain at least one record
- Value accessor must return numeric values
- Start and end angles must be valid radians

## Cautions

- Ensure value accessor correctly maps to numeric column
- Verify sort comparator matches data type and intent
- Confirm padAngle does not exceed available angular space
- Test with sample data before production use

## Output Contract

- Array of arc angle objects, each containing startAngle, endAngle, padAngle, and data properties, ready for downstream arc path generation or rendering

## Triggers

- Need to render categorical or grouped data as pie or donut chart
- Have tabular dataset with numeric values
