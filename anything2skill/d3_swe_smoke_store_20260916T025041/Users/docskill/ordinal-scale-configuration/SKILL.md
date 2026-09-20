---
id: "721665f6-6f7e-558d-9e07-f8b600974990"
name: "Ordinal Scale Configuration"
description: "Create and configure an ordinal scale that maps discrete domain values to discrete range values, with support for unknown value handling and scale copying."
version: "0.1.0"
tags:
  - "d3"
  - "scale"
  - "ordinal"
  - "categorical"
  - "mapping"
  - "configuration"
triggers:
  - "You need to map categorical or discrete input values to a fixed set of output values; typical in chart axes, color encoding, or position mapping."
examples:
  - input: "d3.scaleOrdinal().domain(['A', 'B', 'C']).range(['red', 'green', 'blue']).unknown('gray')"
    output: "A scale that maps 'A' → 'red', 'B' → 'green', 'C' → 'blue', and any other input → 'gray'"
    notes: "Typical use case for categorical color encoding in a chart."
  - input: "d3.scaleOrdinal().domain(['small', 'medium', 'large']).range([10, 20, 30])"
    output: "A scale that maps size categories to numeric values for positioning or sizing."
    notes: "Unknown inputs will return d3.scaleImplicit by default."
---

# Ordinal Scale Configuration

Create and configure an ordinal scale that maps discrete domain values to discrete range values, with support for unknown value handling and scale copying.

## Prompt

Initialize an ordinal scale by setting its input domain, output range, and unknown-value fallback policy. Call d3.scaleOrdinal() to create the scale, then chain .domain(), .range(), and .unknown() to configure it. The scale will then map each domain value to its corresponding range value; any input not in the domain will return the unknown value.

## Objective

Set up a reusable ordinal scale with domain, range, and unknown-value policies
## Applicable Signals

- Need to map categorical or discrete input values to a fixed set of output values
- Building chart axes with non-numeric categories
- Encoding color or position by discrete attribute
- Assigning discrete symbols or shapes to categories

## Contraindications

- Input domain is continuous or numeric; use linear or other continuous scales instead
- Implicit domain without explicit range definition
- Requirement for smooth interpolation between values

## Workflow Steps

- {'step': 1, 'action': 'Create ordinal scale', 'detail': 'Call d3.scaleOrdinal() to instantiate a new ordinal scale.'}
- {'step': 2, 'action': 'Set input domain', 'detail': 'Call .domain([values]) with an array of discrete input values (e.g., category names).'}
- {'step': 3, 'action': 'Set output range', 'detail': 'Call .range([values]) with an array of discrete output values (e.g., colors, positions, or symbols).'}
- {'step': 4, 'action': 'Define unknown-value policy', 'detail': 'Call .unknown(value) to specify the output for any input not in the domain. If not set, d3.scaleImplicit is used.'}
- {'step': 5, 'action': 'Use or copy scale', 'detail': 'Apply the scale by calling it with domain values, or call .copy() to create an independent copy for reuse.'}

## Constraints

- Domain and range must both be defined before scale is used
- Range size should match or exceed domain size to avoid collisions
- Unknown value must be explicitly set if out-of-domain inputs are expected

## Cautions

- Modifying domain or range after scale is in use will affect all downstream mappings.
- Unknown value defaults to d3.scaleImplicit; explicitly set if a different fallback is required.
- Scale does not validate that range size matches domain size; caller is responsible for ensuring sufficient range values.

## Output Contract

- A configured ordinal scale object that accepts domain values and returns corresponding range values, with unknown-value fallback defined. The scale is callable and chainable.

## Example Therapist Responses

### Example 1

- Client/Input: d3.scaleOrdinal().domain(['A', 'B', 'C']).range(['red', 'green', 'blue']).unknown('gray')
- Therapist/Output: A scale that maps 'A' → 'red', 'B' → 'green', 'C' → 'blue', and any other input → 'gray'
- Notes: Typical use case for categorical color encoding in a chart.

### Example 2

- Client/Input: d3.scaleOrdinal().domain(['small', 'medium', 'large']).range([10, 20, 30])
- Therapist/Output: A scale that maps size categories to numeric values for positioning or sizing.
- Notes: Unknown inputs will return d3.scaleImplicit by default.

## Triggers

- You need to map categorical or discrete input values to a fixed set of output values; typical in chart axes, color encoding, or position mapping.

## Examples

### Example 1

Input:

  d3.scaleOrdinal().domain(['A', 'B', 'C']).range(['red', 'green', 'blue']).unknown('gray')

Output:

  A scale that maps 'A' → 'red', 'B' → 'green', 'C' → 'blue', and any other input → 'gray'

Notes:

  Typical use case for categorical color encoding in a chart.

### Example 2

Input:

  d3.scaleOrdinal().domain(['small', 'medium', 'large']).range([10, 20, 30])

Output:

  A scale that maps size categories to numeric values for positioning or sizing.

Notes:

  Unknown inputs will return d3.scaleImplicit by default.
