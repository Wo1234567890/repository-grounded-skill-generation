---
id: "64a5ce52-07a9-52f9-808d-dbdc2659a314"
name: "Group iterable into nested structure"
description: "Transform an iterable into a grouped nested Map or array structure, organizing discrete values by one or more grouping keys. Use when you need to aggregate or organize data by categorical dimensions without reducing values."
version: "0.1.0"
tags:
  - "grouping"
  - "aggregation"
  - "data_organization"
  - "iterable"
  - "nested_structure"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Input is an iterable; you need to organize values by one or more discrete keys; output should be nested Map or array."
examples:
  - input: "Array of objects: [{category: 'A', value: 10}, {category: 'A', value: 20}, {category: 'B', value: 30}]; grouping key: d => d.category"
    output: "Map { 'A' => [{category: 'A', value: 10}, {category: 'A', value: 20}], 'B' => [{category: 'B', value: 30}] }"
    notes: "Single-level grouping by category"
  - input: "Same array; grouping keys: d => d.category, d => d.value % 2"
    output: "Map { 'A' => Map { 0 => [{category: 'A', value: 20}], 1 => [{category: 'A', value: 10}] }, 'B' => Map { 0 => [{category: 'B', value: 30}] } }"
    notes: "Two-level hierarchical grouping"
---

# Group iterable into nested structure

Transform an iterable into a grouped nested Map or array structure, organizing discrete values by one or more grouping keys. Use when you need to aggregate or organize data by categorical dimensions without reducing values.

## Prompt

Call d3.group() to produce a nested Map, or d3.groups() to produce a nested array. Pass the iterable and one or more accessor functions that extract grouping keys from each element. The result organizes all elements by their key combinations in a hierarchical structure.

## Objective

Transform iterable into grouped nested structure
## Applicable Signals

- Input is an iterable (array, Set, or other iterable type)
- Need to organize values by one or more discrete categorical keys
- Output should preserve all original values in a nested Map or array structure
- Downstream processing requires hierarchical access by grouping dimensions

## Contraindications

- Data is already grouped or pre-organized
- Flat output is required without nesting
- Grouping keys are continuous, numeric, or non-discrete
- You need to reduce or aggregate values (use rollup instead)
- You need to index by a single unique key (use index instead)

## Workflow Steps

- Receive iterable and one or more grouping key accessors
- Choose output format: d3.group() for nested Map or d3.groups() for nested array
- Apply grouping operation, organizing elements by key combinations
- Return nested structure with values accessible by key path

## Constraints

- Grouping keys must be discrete and comparable
- All elements in the iterable must be processable by the accessor functions
- Nesting depth equals the number of grouping key accessors provided

## Cautions

- Map-based output (d3.group) uses key interning; use InternMap for non-primitive keys like dates
- Large iterables with many unique key combinations may produce deeply nested structures with memory implications
- Order of grouping accessors determines nesting hierarchy

## Output Contract

- Nested Map (via d3.group) or nested array (via d3.groups) with values organized by grouping keys, ready for downstream aggregation, iteration, or further transformation.

## Example Therapist Responses

### Example 1

- Client/Input: Array of objects: [{category: 'A', value: 10}, {category: 'A', value: 20}, {category: 'B', value: 30}]; grouping key: d => d.category
- Therapist/Output: Map { 'A' => [{category: 'A', value: 10}, {category: 'A', value: 20}], 'B' => [{category: 'B', value: 30}] }
- Notes: Single-level grouping by category

### Example 2

- Client/Input: Same array; grouping keys: d => d.category, d => d.value % 2
- Therapist/Output: Map { 'A' => Map { 0 => [{category: 'A', value: 20}], 1 => [{category: 'A', value: 10}] }, 'B' => Map { 0 => [{category: 'B', value: 30}] } }
- Notes: Two-level hierarchical grouping

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Input is an iterable; you need to organize values by one or more discrete keys; output should be nested Map or array.

## Examples

### Example 1

Input:

  Array of objects: [{category: 'A', value: 10}, {category: 'A', value: 20}, {category: 'B', value: 30}]; grouping key: d => d.category

Output:

  Map { 'A' => [{category: 'A', value: 10}, {category: 'A', value: 20}], 'B' => [{category: 'B', value: 30}] }

Notes:

  Single-level grouping by category

### Example 2

Input:

  Same array; grouping keys: d => d.category, d => d.value % 2

Output:

  Map { 'A' => Map { 0 => [{category: 'A', value: 20}], 1 => [{category: 'A', value: 10}] }, 'B' => Map { 0 => [{category: 'B', value: 30}] } }

Notes:

  Two-level hierarchical grouping
