---
id: "f0be0dd1-5afd-5cd1-8297-db7737d8cf0b"
name: "Reduce iterable into aggregated nested structure"
description: "Reduce an iterable into a nested Map or array by applying an aggregation function to grouped values. Combines grouping with reduction in a single operation, producing summary statistics or aggregate measures per group."
version: "0.1.0"
tags:
  - "data_transformation"
  - "aggregation"
  - "grouping"
  - "reduction"
  - "d3-array"
  - "nested_structure"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Input is an iterable (array, set, or other iterable collection)"
  - "You need to group data by one or more keys"
  - "You need to apply a reducer function (sum, count, mean, custom aggregation) to each group"
  - "Output should be a nested structure (Map or array) with one aggregated value per group"
examples:
  - input: "Array of objects: [{category: 'A', value: 10}, {category: 'A', value: 20}, {category: 'B', value: 5}]; reducer: (values) => values.reduce((a, b) => a + b, 0); grouping key: 'category'"
    output: "Map { 'A' => 30, 'B' => 5 } (using d3.rollup)"
    notes: "Sums values per category"
  - input: "Same array; reducer: (values) => values.length; grouping key: 'category'"
    output: "Map { 'A' => 2, 'B' => 1 } (using d3.rollup)"
    notes: "Counts items per category"
---

# Reduce iterable into aggregated nested structure

Reduce an iterable into a nested Map or array by applying an aggregation function to grouped values. Combines grouping with reduction in a single operation, producing summary statistics or aggregate measures per group.

## Prompt

Apply a reducer function (such as sum, count, mean, or custom aggregation) to an iterable after grouping by one or more keys. The result is a nested Map or array structure where each group contains the reduced value. Choose d3.rollup for Map output or d3.rollups for array output.

## Objective

Reduce grouped iterable into aggregated nested structure
## Applicable Signals

- Iterable data source available
- Grouping keys defined
- Reducer function defined and applicable to group values
- Nested output structure acceptable

## Contraindications

- You only need grouping without reduction; use d3.group or d3.groups instead
- Output must remain flat; use d3.flatRollup instead
- Reducer function is not defined or not applicable to the data
- You need to preserve individual values per group; reduction would lose detail

## Workflow Steps

- {'step': 1, 'action': 'Prepare input iterable and define grouping keys', 'detail': 'Ensure data is iterable and identify which field(s) will be used for grouping'}
- {'step': 2, 'action': 'Define reducer function', 'detail': 'Create a function that takes grouped values and returns a single aggregated result (e.g., sum, count, mean)'}
- {'step': 3, 'action': 'Choose output format', 'detail': 'Select d3.rollup for nested Map output or d3.rollups for nested array output'}
- {'step': 4, 'action': 'Invoke reduction operation', 'detail': 'Call the chosen function with iterable, reducer, and grouping keys as arguments'}
- {'step': 5, 'action': 'Validate output structure', 'detail': 'Verify that each group has exactly one aggregated value and structure matches expected nesting'}

## Constraints

- Reducer function must be compatible with the grouped values
- Grouping keys must be comparable or hashable
- Input iterable must be non-empty for meaningful aggregation

## Cautions

- Ensure reducer function handles edge cases (empty groups, null values, type mismatches)
- Nested structure depth depends on number of grouping keys; deeply nested results may be harder to traverse
- Map keys use object identity by default; use InternMap for non-primitive keys (dates, objects)

## Output Contract

- Nested Map (d3.rollup) or nested array (d3.rollups) where each leaf node contains one aggregated value per group. Structure is ready for visualization, further analysis, or downstream consumption.

## Example Therapist Responses

### Example 1

- Client/Input: Array of objects: [{category: 'A', value: 10}, {category: 'A', value: 20}, {category: 'B', value: 5}]; reducer: (values) => values.reduce((a, b) => a + b, 0); grouping key: 'category'
- Therapist/Output: Map { 'A' => 30, 'B' => 5 } (using d3.rollup)
- Notes: Sums values per category

### Example 2

- Client/Input: Same array; reducer: (values) => values.length; grouping key: 'category'
- Therapist/Output: Map { 'A' => 2, 'B' => 1 } (using d3.rollup)
- Notes: Counts items per category

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Input is an iterable (array, set, or other iterable collection)
- You need to group data by one or more keys
- You need to apply a reducer function (sum, count, mean, custom aggregation) to each group
- Output should be a nested structure (Map or array) with one aggregated value per group

## Examples

### Example 1

Input:

  Array of objects: [{category: 'A', value: 10}, {category: 'A', value: 20}, {category: 'B', value: 5}]; reducer: (values) => values.reduce((a, b) => a + b, 0); grouping key: 'category'

Output:

  Map { 'A' => 30, 'B' => 5 } (using d3.rollup)

Notes:

  Sums values per category

### Example 2

Input:

  Same array; reducer: (values) => values.length; grouping key: 'category'

Output:

  Map { 'A' => 2, 'B' => 1 } (using d3.rollup)

Notes:

  Counts items per category
