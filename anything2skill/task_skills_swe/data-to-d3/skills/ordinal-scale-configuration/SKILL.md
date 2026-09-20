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
  - "discrete"
triggers:
  - "Need to map categorical or discrete input values to a fixed set of output values"
  - "Building chart axes with categorical labels"
  - "Assigning colors or visual properties to discrete categories"
  - "Encoding categorical data in visualization"
examples:
  - input: "d3.scaleOrdinal().domain(['A', 'B', 'C']).range(['red', 'green', 'blue']).unknown('gray')"
    output: "scale('A') → 'red', scale('B') → 'green', scale('C') → 'blue', scale('D') → 'gray'"
    notes: "Categorical color assignment with fallback for unmapped categories"
  - input: "d3.scaleOrdinal().domain(['low', 'medium', 'high']).range([10, 20, 30])"
    output: "scale('low') → 10, scale('medium') → 20, scale('high') → 30"
    notes: "Discrete numeric encoding for categorical severity levels"
---

# Ordinal Scale Configuration

Create and configure an ordinal scale that maps discrete domain values to discrete range values, with support for unknown value handling and scale copying.

## Prompt

Use d3.scaleOrdinal() to create an ordinal scale. Chain .domain() to set input categorical values, .range() to set output values, and .unknown() to define fallback behavior for unmapped inputs. Call .copy() to create independent instances.

## Objective

Set up a reusable ordinal scale with domain, range, and unknown-value policies
## Applicable Signals

- Input domain contains non-numeric or categorical values
- Output range is a fixed set of discrete values
- Mapping is one-to-one or many-to-one from domain to range

## Contraindications

- Input domain is continuous or numeric; use linear or other continuous scales instead
- Implicit domain without explicit range definition
- Requirement for smooth interpolation between values

## Workflow Steps

- {'step': 1, 'action': 'Create ordinal scale', 'detail': 'Call d3.scaleOrdinal() to instantiate a new ordinal scale'}
- {'step': 2, 'action': 'Set domain', 'detail': 'Call .domain(array) with array of discrete input values (e.g., category names)'}
- {'step': 3, 'action': 'Set range', 'detail': 'Call .range(array) with array of discrete output values (e.g., colors, positions)'}
- {'step': 4, 'action': 'Define unknown-value behavior', 'detail': 'Call .unknown(value) to specify output for inputs not in domain; use d3.scaleImplicit for implicit domain extension'}
- {'step': 5, 'action': 'Optionally copy scale', 'detail': 'Call .copy() to create independent scale instance if needed for parallel configurations'}

## Constraints

- Domain and range must be explicitly defined before scale is used
- Unknown value policy must be set if unmapped inputs are possible
- Range cardinality should match or exceed domain cardinality for full coverage

## Cautions

- If domain is not explicitly set, scale behavior is undefined for new inputs
- Modifying domain or range after scale is in use may break existing mappings
- Unknown value must be compatible with range value type (e.g., color string for color range)

## Output Contract

- A configured ordinal scale object that accepts domain values via function call and returns corresponding range values; unknown inputs return the value set by .unknown(); scale is reusable across multiple data bindings.

## Example Executions

### Example 1

- Input: d3.scaleOrdinal().domain(['A', 'B', 'C']).range(['red', 'green', 'blue']).unknown('gray')
- Output: scale('A') → 'red', scale('B') → 'green', scale('C') → 'blue', scale('D') → 'gray'
- Notes: Categorical color assignment with fallback for unmapped categories

### Example 2

- Input: d3.scaleOrdinal().domain(['low', 'medium', 'high']).range([10, 20, 30])
- Output: scale('low') → 10, scale('medium') → 20, scale('high') → 30
- Notes: Discrete numeric encoding for categorical severity levels

## Triggers

- Need to map categorical or discrete input values to a fixed set of output values
- Building chart axes with categorical labels
- Assigning colors or visual properties to discrete categories
- Encoding categorical data in visualization

## Examples

### Example 1

Input:

  d3.scaleOrdinal().domain(['A', 'B', 'C']).range(['red', 'green', 'blue']).unknown('gray')

Output:

  scale('A') → 'red', scale('B') → 'green', scale('C') → 'blue', scale('D') → 'gray'

Notes:

  Categorical color assignment with fallback for unmapped categories

### Example 2

Input:

  d3.scaleOrdinal().domain(['low', 'medium', 'high']).range([10, 20, 30])

Output:

  scale('low') → 10, scale('medium') → 20, scale('high') → 30

Notes:

  Discrete numeric encoding for categorical severity levels
