---
id: "c4d1beb0-c8ff-5831-b353-1106e46cb437"
name: "Format structured data as delimiter-separated values"
description: "Convert arrays of objects or rows into CSV, TSV, or custom delimiter-separated strings for export or transmission. Supports both object-based input (with headers extracted from keys) and row-based input (values only). Handles proper escaping of special characters and delimiter-containing values."
version: "0.1.0"
tags:
  - "data_export"
  - "serialization"
  - "csv"
  - "tsv"
  - "delimiter"
  - "text_formatting"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Need to export array of objects as CSV or TSV"
  - "Preparing tabular data for file output"
  - "Serializing data for transmission or API response"
  - "Converting in-memory data structures to text format"
examples:
  - input: "Array of objects: [{name: 'Alice', age: 30}, {name: 'Bob', age: 25}], delimiter: ','"
    output: "name,age\nAlice,30\nBob,25"
    notes: "Standard CSV format from object array with headers"
  - input: "Array of rows: [['Alice', 30], ['Bob', 25]], delimiter: '\\t'"
    output: "Alice\t30\nBob\t25"
    notes: "TSV format from row array (no headers extracted)"
  - input: "Array of objects with custom delimiter: [{x: 1, y: 2}], delimiter: '|'"
    output: "x|y\n1|2"
    notes: "Custom delimiter support"
---

# Format structured data as delimiter-separated values

Convert arrays of objects or rows into CSV, TSV, or custom delimiter-separated strings for export or transmission. Supports both object-based input (with headers extracted from keys) and row-based input (values only). Handles proper escaping of special characters and delimiter-containing values.

## Prompt

Given an array of objects (with consistent keys) or an array of rows (arrays of values), format it as a delimited string using the specified delimiter (comma for CSV, tab for TSV, or custom). Support variants: full format with headers, body-only (excluding headers), individual rows, or individual values. Ensure proper escaping of values containing delimiters, newlines, or quotes.

## Objective

Convert structured data to delimited text format
## Applicable Signals

- Array of objects with uniform keys ready for export
- Array of row arrays (values only) ready for export
- Delimiter preference specified (CSV, TSV, or custom)
- Need to export tabular data for file output or API transmission

## Contraindications

- Data is already in text or binary format
- Binary output is required
- Data structure is irregular or deeply nested
- Streaming output is required for very large datasets

## Workflow Steps

- Receive array of objects or rows and delimiter specification
- If object array: extract headers from first object keys
- Format headers as first row using delimiter (unless body-only variant)
- Iterate through data rows and format each value with proper escaping
- Join all rows with newline characters
- Return complete delimited string ready for output

## Constraints

- Input must be an array (of objects or rows)
- For object arrays, all objects should have consistent keys
- Delimiter must be a single character or string
- Values containing the delimiter must be escaped or quoted

## Cautions

- Ensure values containing the delimiter are properly escaped or quoted per CSV/TSV standards
- Large datasets may produce very large strings; consider streaming for production use
- Special characters (newlines, quotes) in values require proper escaping
- Inconsistent object keys may result in missing or misaligned columns

## Output Contract

- A formatted string in the specified delimiter format (CSV, TSV, or custom), ready for file write, API transmission, or further processing. String includes headers (unless body-only variant used) and properly escaped values. Output is a single string with rows separated by newlines.

## Example Therapist Responses

### Example 1

- Client/Input: Array of objects: [{name: 'Alice', age: 30}, {name: 'Bob', age: 25}], delimiter: ','
- Therapist/Output: name,age
Alice,30
Bob,25
- Notes: Standard CSV format from object array with headers

### Example 2

- Client/Input: Array of rows: [['Alice', 30], ['Bob', 25]], delimiter: '\t'
- Therapist/Output: Alice	30
Bob	25
- Notes: TSV format from row array (no headers extracted)

### Example 3

- Client/Input: Array of objects with custom delimiter: [{x: 1, y: 2}], delimiter: '|'
- Therapist/Output: x|y
1|2
- Notes: Custom delimiter support

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Need to export array of objects as CSV or TSV
- Preparing tabular data for file output
- Serializing data for transmission or API response
- Converting in-memory data structures to text format

## Examples

### Example 1

Input:

  Array of objects: [{name: 'Alice', age: 30}, {name: 'Bob', age: 25}], delimiter: ','

Output:

  name,age
  Alice,30
  Bob,25

Notes:

  Standard CSV format from object array with headers

### Example 2

Input:

  Array of rows: [['Alice', 30], ['Bob', 25]], delimiter: '\t'

Output:

  Alice	30
  Bob	25

Notes:

  TSV format from row array (no headers extracted)

### Example 3

Input:

  Array of objects with custom delimiter: [{x: 1, y: 2}], delimiter: '|'

Output:

  x|y
  1|2

Notes:

  Custom delimiter support
