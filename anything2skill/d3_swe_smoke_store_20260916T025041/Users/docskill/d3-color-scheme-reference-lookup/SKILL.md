---
id: "39679eb6-0ad0-50d8-a709-1713e0bdae5d"
name: "D3 Color Scheme Reference Lookup"
description: "Canonical reference asset documenting D3 built-in color schemes (categorical, cyclical, diverging) with cardinality, visual properties, and recommended use cases. Enables informed color encoding strategy planning and team alignment without runtime execution."
version: "0.1.0"
tags:
  - "d3"
  - "color"
  - "scheme"
  - "reference"
  - "categorical"
  - "cyclical"
triggers:
  - "planning color encoding strategy"
  - "comparing scheme options"
  - "documenting color choices"
  - "training team on D3 color APIs"
examples:
  - input: "Need to select a categorical color scheme for 10 discrete categories"
    output: "d3.schemeCategory10 or d3.schemeObservable10 (both 10-color categorical schemes)"
    notes: "Categorical schemes are best for nominal data with distinct categories."
  - input: "Documenting color choices for a diverging heatmap"
    output: "Reference diverging section to identify appropriate scheme (e.g., d3.interpolateRdBu) and note visual properties (red-blue gradient for positive-negative contrast)"
    notes: "Diverging schemes emphasize extremes and midpoint; suitable for data with meaningful center value."
---

# D3 Color Scheme Reference Lookup

Canonical reference asset documenting D3 built-in color schemes (categorical, cyclical, diverging) with cardinality, visual properties, and recommended use cases. Enables informed color encoding strategy planning and team alignment without runtime execution.

## Prompt

Use this reference to identify and document D3 color schemes by type (categorical, cyclical, diverging). Each scheme entry includes cardinality (number of colors) and visual properties. Consult this asset during design planning, scheme comparison, team training, or documentation of color choices. Do not use for runtime color selection or custom color generation.

## Objective

document color scheme inventory and selection guidance
## Applicable Signals

- planning color encoding strategy
- comparing scheme options
- documenting color choices
- training team on D3 color APIs

## Contraindications

- runtime color selection (use micro_skill assets instead)
- custom color generation
- non-D3 color libraries

## Workflow Steps

- Identify data type (categorical, cyclical, or diverging)
- Determine required cardinality (number of distinct colors)
- Consult appropriate scheme section
- Review visual properties and recommended use cases
- Document scheme selection and rationale

## Constraints

- limited to D3 built-in schemes
- reference-only; does not execute color assignment
- cardinality and visual properties are fixed per scheme

## Cautions

- Do not use for dynamic or programmatic color selection at runtime.
- Schemes are predefined; custom palettes require separate tooling.

## Output Contract

- Reference document or lookup table mapping scheme names to cardinality, visual properties, and recommended data types.
- Enables informed scheme selection and team alignment on color strategy.

## Example Therapist Responses

### Example 1

- Client/Input: Need to select a categorical color scheme for 10 discrete categories
- Therapist/Output: d3.schemeCategory10 or d3.schemeObservable10 (both 10-color categorical schemes)
- Notes: Categorical schemes are best for nominal data with distinct categories.

### Example 2

- Client/Input: Documenting color choices for a diverging heatmap
- Therapist/Output: Reference diverging section to identify appropriate scheme (e.g., d3.interpolateRdBu) and note visual properties (red-blue gradient for positive-negative contrast)
- Notes: Diverging schemes emphasize extremes and midpoint; suitable for data with meaningful center value.

## Triggers

- planning color encoding strategy
- comparing scheme options
- documenting color choices
- training team on D3 color APIs

## Examples

### Example 1

Input:

  Need to select a categorical color scheme for 10 discrete categories

Output:

  d3.schemeCategory10 or d3.schemeObservable10 (both 10-color categorical schemes)

Notes:

  Categorical schemes are best for nominal data with distinct categories.

### Example 2

Input:

  Documenting color choices for a diverging heatmap

Output:

  Reference diverging section to identify appropriate scheme (e.g., d3.interpolateRdBu) and note visual properties (red-blue gradient for positive-negative contrast)

Notes:

  Diverging schemes emphasize extremes and midpoint; suitable for data with meaningful center value.
