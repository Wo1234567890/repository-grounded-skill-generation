---
id: "fe8a8902-a77c-5cd1-8055-71424e50730f"
name: "Stack Generator Configuration"
description: "Configure and apply a stack generator to transform multi-series dataset into stacked layout coordinates for visualization. Use when preparing data for stacked bar, area, or streamgraph rendering."
version: "0.1.0"
tags:
  - "d3"
  - "data-transformation"
  - "stacking"
  - "layout"
  - "visualization-preparation"
triggers:
  - "Need to stack multiple data series for visualization"
  - "Have dataset with multiple value columns or groups"
  - "Preparing data for stacked bar chart, stacked area chart, or streamgraph"
---

# Stack Generator Configuration

Configure and apply a stack generator to transform multi-series dataset into stacked layout coordinates for visualization. Use when preparing data for stacked bar, area, or streamgraph rendering.

## Prompt

Create a stack generator, set accessors for keys and values, apply an order strategy (appearance, ascending, descending, inside-out, none, or reverse), and apply an offset strategy (expand, diverging, none, silhouette, or wiggle) to produce stacked coordinate arrays with baseline and topline values for each series.

## Objective

Transform multi-series dataset into stacked coordinate layout
## Applicable Signals

- Multi-series dataset available
- Visualization target requires stacked layout
- Data contains grouping or category dimension

## Contraindications

- Data is already stacked
- Single-series dataset
- Unstacked or side-by-side visualization required
- Data lacks clear series or group structure

## Workflow Steps

- {'step': 1, 'action': 'Create stack generator', 'detail': 'Instantiate d3.stack()'}
- {'step': 2, 'action': 'Set keys accessor', 'detail': 'Call stack.keys() to specify which data properties represent series identifiers'}
- {'step': 3, 'action': 'Set value accessor', 'detail': 'Call stack.value() to specify which data property contains numeric values for stacking'}
- {'step': 4, 'action': 'Set order strategy', 'detail': 'Call stack.order() with one of: stackOrderAppearance, stackOrderAscending, stackOrderDescending, stackOrderInsideOut, stackOrderNone, or stackOrderReverse'}
- {'step': 5, 'action': 'Set offset strategy', 'detail': 'Call stack.offset() with one of: stackOffsetExpand, stackOffsetDiverging, stackOffsetNone, stackOffsetSilhouette, or stackOffsetWiggle'}
- {'step': 6, 'action': 'Apply generator to dataset', 'detail': 'Call stack(data) to produce stacked coordinate array'}

## Constraints

- Dataset must have identifiable series keys
- Each series must have corresponding numeric values
- Order and offset strategies must be compatible with visualization intent

## Cautions

- Order strategy affects visual hierarchy; choose based on data story
- Offset strategy affects baseline interpretation; expand normalizes to 0–1, diverging splits positive/negative, silhouette centers around zero
- Wiggle offset minimizes visual noise but may obscure individual series trends

## Output Contract

- Returns array of series, each containing array of [baseline, topline] coordinate pairs for each data point. Each series is indexed and labeled with its key. Ready for direct binding to visualization elements (bars, areas, paths).

## Triggers

- Need to stack multiple data series for visualization
- Have dataset with multiple value columns or groups
- Preparing data for stacked bar chart, stacked area chart, or streamgraph
