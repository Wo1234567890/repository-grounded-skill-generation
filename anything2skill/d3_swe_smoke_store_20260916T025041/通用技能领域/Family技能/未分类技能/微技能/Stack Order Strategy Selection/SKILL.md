---
id: "286adf35-1eb0-5f93-a39d-a3e65e4ae5d0"
name: "Stack Order Strategy Selection"
description: "Select and apply a stacking order strategy to control how series are layered in stacked visualizations. Choose from appearance (earliest bottom), ascending (smallest bottom), descending (largest bottom), inside-out (earlier centered), none (original order), or reverse (reversed order) to optimize visual emphasis and readability."
version: "0.1.0"
tags:
  - "stacking"
  - "layout"
  - "series-ordering"
  - "visualization-configuration"
  - "d3"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Configuring stack order for a stacked visualization"
  - "Need to emphasize earliest, smallest, largest, or balanced series visibility"
  - "Adjusting series layering to improve chart readability"
---

# Stack Order Strategy Selection

Select and apply a stacking order strategy to control how series are layered in stacked visualizations. Choose from appearance (earliest bottom), ascending (smallest bottom), descending (largest bottom), inside-out (earlier centered), none (original order), or reverse (reversed order) to optimize visual emphasis and readability.

## Prompt

Determine which series ordering strategy best serves your visualization goal. Appearance emphasizes chronological priority; ascending and descending emphasize magnitude; inside-out balances visibility; none and reverse preserve or invert the input order. Apply the selected order function to your stack generator before rendering.

## Objective

Choose series ordering for visual emphasis and readability
## Applicable Signals

- Stack generator created and ready for configuration
- Visual priority or emphasis requirement identified
- Series ordering preference specified by design or data semantics

## Contraindications

- Series order is already fixed by upstream data structure
- No visual ordering preference or constraint exists
- Order strategy conflicts with downstream rendering requirements

## Workflow Steps

- Identify the visual goal: chronological priority, magnitude emphasis, or balanced visibility
- Select the appropriate order strategy: appearance, ascending, descending, inside-out, none, or reverse
- Apply the order function to the stack generator via stack.order()
- Verify series are rendered in the intended order before final output

## Constraints

- Order function must be applied before stack generation
- Selected strategy must be one of the six standard options: d3.stackOrderAppearance, d3.stackOrderAscending, d3.stackOrderDescending, d3.stackOrderInsideOut, d3.stackOrderNone, or d3.stackOrderReverse
- Order affects visual hierarchy; verify alignment with intended message

## Cautions

- Inside-out ordering may obscure smaller series in the middle layers
- Descending order can emphasize outliers; verify this matches intent
- Order choice should align with data semantics and audience expectations

## Output Contract

- Stack order function applied; series rendered in specified order (earliest-bottom, smallest-bottom, largest-bottom, centered, original, or reversed). Downstream visualization receives correctly ordered stack data.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Configuring stack order for a stacked visualization
- Need to emphasize earliest, smallest, largest, or balanced series visibility
- Adjusting series layering to improve chart readability
