---
id: "1b100721-bee7-562e-855a-5a8cb8a36ea0"
name: "Stack Order Strategy Selection"
description: "Select and apply a stacking order strategy to control how series are layered in a stacked visualization. Choose from appearance (earliest on bottom), ascending (smallest on bottom), descending (largest on bottom), inside-out (earlier series in middle), none (given order), or reverse (reverse of given order). Use when visual hierarchy or readability of stacked series matters."
version: "0.1.0"
tags:
  - "d3"
  - "stacking"
  - "layout"
  - "series-ordering"
  - "visualization-hierarchy"
triggers:
  - "Stacked visualization requires specific series ordering"
  - "Need to emphasize earliest, smallest, largest, or balanced series visibility"
  - "Visual hierarchy of stacked series must be controlled"
---

# Stack Order Strategy Selection

Select and apply a stacking order strategy to control how series are layered in a stacked visualization. Choose from appearance (earliest on bottom), ascending (smallest on bottom), descending (largest on bottom), inside-out (earlier series in middle), none (given order), or reverse (reverse of given order). Use when visual hierarchy or readability of stacked series matters.

## Prompt

1. Identify the desired series ordering priority: earliest visibility, smallest-first, largest-first, balanced middle emphasis, original order, or reversed order.
2. Select the corresponding stack order strategy function.
3. Apply the strategy to the stack generator via stack.order().
4. Verify series are reordered according to the chosen rule in the output layout.

## Objective

Apply series ordering rule to stack layout
## Applicable Signals

- Multiple series in dataset
- Stacked bar, area, or stream chart layout
- Series ordering affects readability or emphasis

## Contraindications

- Order is irrelevant to visualization goal
- Single series only
- Order already applied upstream in pipeline

## Intervention Moves

- stackOrderAppearance: put earliest series on bottom
- stackOrderAscending: put smallest series on bottom
- stackOrderDescending: put largest series on bottom
- stackOrderInsideOut: put earlier series in the middle
- stackOrderNone: use the given series order
- stackOrderReverse: use the reverse of the given series order

## Workflow Steps

- {'step': 1, 'action': 'Determine ordering priority', 'detail': 'Identify whether you want earliest series, smallest values, largest values, balanced visibility, original order, or reversed order'}
- {'step': 2, 'action': 'Select strategy function', 'detail': 'Choose one of: stackOrderAppearance, stackOrderAscending, stackOrderDescending, stackOrderInsideOut, stackOrderNone, stackOrderReverse'}
- {'step': 3, 'action': 'Apply to stack generator', 'detail': 'Call stack.order(selectedStrategy) on the stack generator instance'}
- {'step': 4, 'action': 'Verify output', 'detail': 'Confirm series in output are reordered according to chosen rule'}

## Constraints

- Must be applied before stack layout is finalized
- Requires multi-series dataset
- Order strategy is mutually exclusive; only one can be active

## Cautions

- Different order strategies produce different visual emphasis; test with actual data
- Inside-out ordering works best for streamgraphs; may be less effective for bar charts
- Order strategy interacts with offset strategy; coordinate both for desired effect

## Output Contract

- Stack generator with selected order strategy applied; series reordered according to chosen rule; ready for offset configuration or rendering

## Triggers

- Stacked visualization requires specific series ordering
- Need to emphasize earliest, smallest, largest, or balanced series visibility
- Visual hierarchy of stacked series must be controlled
