---
id: "ecceaf37-9cf4-54a4-9f88-37e3a1b5145d"
name: "Natural Order Comparison"
description: "Micro-operation to compute the natural order relationship between two values, returning a standardized comparison result (-1, 0, or 1) for use in sorting or ranking workflows."
version: "0.1.0"
tags:
  - "comparison"
  - "ordering"
  - "micro_operation"
  - "data_preparation"
  - "sorting_building_block"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Need to determine if one value is less than, equal to, or greater than another"
  - "Building custom sort or ranking logic"
  - "Validating order relationship between two data points"
---

# Natural Order Comparison

Micro-operation to compute the natural order relationship between two values, returning a standardized comparison result (-1, 0, or 1) for use in sorting or ranking workflows.

## Prompt

Compare two values using natural ordering rules. Invoke this skill when you need to determine the relative order of two individual values (less than, equal to, or greater than) without performing a full array sort. Returns a standardized comparison result suitable for use in custom sort implementations or ranking operations.

## Objective

Compare two values and determine natural order
## Applicable Signals

- Pairwise comparison required
- Natural ordering semantics applicable
- Caller implements custom sort or ranking workflow

## Contraindications

- Performing full array sort (use d3.sort instead)
- Applying custom comparators with non-natural ordering
- Comparing complex objects without natural order definition

## Workflow Steps

- Accept two values as input
- Apply natural ordering comparison logic
- Return standardized comparison result

## Constraints

- Both input values must be comparable under natural ordering rules
- Output is a standardized comparison result (-1, 0, or 1)

## Cautions

- Natural ordering may not apply to all data types; verify comparability before invocation
- This is an atomic operation; for sorting entire arrays, use higher-level sort skills

## Output Contract

- Comparison result (typically -1, 0, or 1) indicating relative order of two values: -1 if first value is less than second, 0 if equal, 1 if first value is greater than second.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Need to determine if one value is less than, equal to, or greater than another
- Building custom sort or ranking logic
- Validating order relationship between two data points
