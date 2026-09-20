---
id: "6524f5e4-b18a-58b0-b6bc-33cc92d1d10b"
name: "Infer and coerce value types in parsed data"
description: "Automatically detect and convert string values to appropriate types (number, date, boolean, etc.) after parsing delimiter-separated values. Normalizes parsed objects by inferring the most appropriate type for each field using d3.autoType or equivalent type inference logic."
version: "0.1.0"
tags:
  - "data_parsing"
  - "type_inference"
  - "data_normalization"
  - "csv"
  - "tsv"
  - "d3"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Parsed data contains all-string values from CSV or TSV"
  - "Need automatic type detection for numeric, date, or boolean fields"
  - "Post-parsing normalization step before analysis or visualization"
---

# Infer and coerce value types in parsed data

Automatically detect and convert string values to appropriate types (number, date, boolean, etc.) after parsing delimiter-separated values. Normalizes parsed objects by inferring the most appropriate type for each field using d3.autoType or equivalent type inference logic.

## Prompt

Apply automatic type inference to parsed data objects. Examine each string value and convert to number, date, boolean, or other appropriate type. Return the normalized object with coerced values.

## Objective

Type inference and coercion for parsed objects
## Applicable Signals

- Output from d3.csvParse, d3.tsvParse, or dsv.parse
- Object keys with string-only values
- Requirement for type-safe downstream operations

## Contraindications

- Types are already correct or pre-validated
- Explicit type schema is required and must not be inferred
- String preservation is needed for all fields
- Data contains intentional string-formatted numbers or dates that should remain strings

## Workflow Steps

- Receive parsed object or array of objects with string values
- Iterate over each field in each object
- Attempt type detection: number, date, boolean, or keep as string
- Apply coercion to matching fields
- Return normalized object with inferred types

## Constraints

- Input must be an object or array of objects from a parser
- Type inference must be deterministic and reversible where possible
- Coercion must not lose information or introduce ambiguity

## Cautions

- Automatic inference may misclassify edge cases (e.g., '123' as number vs. string ID)
- Date format detection depends on locale and format conventions
- Boolean inference may be ambiguous for values like '0', '1', 'yes', 'no'

## Output Contract

- Object or array of objects with inferred and coerced value types (numbers, dates, booleans where applicable); all fields retain their keys; unrecognized or ambiguous values remain as strings.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Parsed data contains all-string values from CSV or TSV
- Need automatic type detection for numeric, date, or boolean fields
- Post-parsing normalization step before analysis or visualization
