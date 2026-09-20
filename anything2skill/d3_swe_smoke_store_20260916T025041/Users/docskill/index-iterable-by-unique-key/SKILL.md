---
id: "efe1894a-36bf-5e1f-9083-1587b3561647"
name: "Index iterable by unique key"
description: "Create a nested Map or array index from an iterable, mapping unique key values to their corresponding records. Use when you need fast lookup or deduplication by one or more key fields."
version: "0.1.0"
tags:
  - "indexing"
  - "lookup"
  - "deduplication"
  - "data_structure"
  - "d3"
triggers:
  - "Input is an iterable; you need to map unique key(s) to records; lookup speed or deduplication is important."
---

# Index iterable by unique key

Create a nested Map or array index from an iterable, mapping unique key values to their corresponding records. Use when you need fast lookup or deduplication by one or more key fields.

## Prompt

Call d3.index() to produce a nested Map indexed by one or more key accessors, or d3.indexes() to produce a nested array. Each unique key maps to exactly one record. Use this when you need O(1) or O(log n) lookup performance or when deduplication by key is required.

## Objective

Index iterable into keyed nested structure
## Applicable Signals

- Input is an iterable (array, set, or other iterable collection)
- You need to map unique key(s) to records
- Lookup speed or deduplication by key field is important
- You want O(1) or O(log n) access to records by key

## Contraindications

- You need to aggregate or group multiple records per key (use d3.group or d3.groups instead)
- Keys are not unique in your dataset
- Output must be grouped rather than indexed
- You need to reduce/summarize values per key (use d3.rollup or d3.rollups instead)

## Workflow Steps

- Prepare iterable input (array, set, or other collection)
- Define key accessor function(s) to extract unique key(s) from each record
- Call d3.index(iterable, ...keyAccessors) for Map output or d3.indexes(iterable, ...keyAccessors) for array output
- Verify that keys are unique; if duplicates exist, the last record per key will overwrite earlier ones
- Use the resulting index for O(1) lookup by key

## Constraints

- Keys must be unique; duplicate keys will result in the last record overwriting earlier ones
- Key accessors must be functions that extract comparable values from records
- Output structure is nested if multiple key accessors are provided

## Cautions

- If keys are not guaranteed unique, consider using d3.group instead to preserve all records per key
- For large datasets, verify that the key accessor function is efficient
- Nested Maps or arrays may consume significant memory for high-cardinality keys

## Output Contract

- Nested Map (via d3.index) or nested array (via d3.indexes) with one record per unique key, enabling fast lookup and deduplication.

## Triggers

- Input is an iterable; you need to map unique key(s) to records; lookup speed or deduplication is important.
