---
id: "fe8a8902-a77c-5cd1-8055-71424e50730f"
name: "Stack Generator Configuration"
description: "Configure and apply a D3 stack generator to transform multi-series dataset into stacked layout coordinates. Use when preparing data for stacked bar, area, or streamgraph visualizations."
version: "0.1.0"
tags:
  - "d3"
  - "data-transformation"
  - "stacking"
  - "layout"
  - "visualization-preparation"
triggers:
  - "Need to stack multiple data series for visualization"
  - "Have dataset with multiple value columns or series"
  - "Preparing data for stacked bar chart, stacked area chart, or streamgraph"
---

# Stack Generator Configuration

Configure and apply a D3 stack generator to transform multi-series dataset into stacked layout coordinates. Use when preparing data for stacked bar, area, or streamgraph visualizations.

## Prompt

1. Create a new stack generator using d3.stack().
2. Set the keys accessor to identify which columns represent series.
3. Set the value accessor to extract numeric values from each data point.
4. Choose a stack order (appearance, ascending, descending, inside-out, none, or reverse) to determine series layering.
5. Choose a stack offset (expand, diverging, none, silhouette, or wiggle) to set baseline and spacing behavior.
6. Apply the configured stack generator to your dataset to produce stacked coordinate output.

## Objective

Transform multi-series dataset into stacked coordinate layout
## Applicable Signals

- Multi-column dataset with series identifiers
- Requirement for baseline and topline coordinate pairs
- Visualization type requires layered series rendering

## Contraindications

- Data is already pre-stacked
- Single-series dataset
- Non-hierarchical or non-layered data layout required

## Workflow Steps

- {'step': 1, 'action': 'Instantiate stack generator', 'detail': 'Call d3.stack() to create a new stack generator instance'}
- {'step': 2, 'action': 'Configure keys accessor', 'detail': 'Use stack.keys() to specify which data properties represent series identifiers'}
- {'step': 3, 'action': 'Configure value accessor', 'detail': 'Use stack.value() to specify how to extract numeric values from each data point'}
- {'step': 4, 'action': 'Set stack order', 'detail': 'Choose order method: stackOrderAppearance, stackOrderAscending, stackOrderDescending, stackOrderInsideOut, stackOrderNone, or stackOrderReverse'}
- {'step': 5, 'action': 'Set stack offset', 'detail': 'Choose offset method: stackOffsetExpand, stackOffsetDiverging, stackOffsetNone, stackOffsetSilhouette, or stackOffsetWiggle'}
- {'step': 6, 'action': 'Apply stack generator', 'detail': 'Call the configured stack generator on your dataset to produce stacked coordinate output'}

## Constraints

- Dataset must have consistent structure across all series
- Keys accessor must correctly identify series columns
- Value accessor must extract numeric values

## Cautions

- Order and offset choices significantly affect visual appearance; test multiple combinations
- Ensure all series have values for all data points to avoid gaps in stacking
- Diverging offset requires both positive and negative values

## Output Contract

- Stacked coordinate array where each series contains an array of [baseline, topline] value pairs for each data point, ready for visualization rendering

## Triggers

- Need to stack multiple data series for visualization
- Have dataset with multiple value columns or series
- Preparing data for stacked bar chart, stacked area chart, or streamgraph
