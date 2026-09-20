---
id: "d9f3b831-1d1c-59fa-b44f-9062edcd0b2b"
name: "Format structured data as delimiter-separated values"
description: "Convert arrays of objects or rows into CSV or TSV strings for export or transmission. Handles both object-based and row-based input formats with support for custom delimiters."
version: "0.1.0"
tags:
  - "csv"
  - "tsv"
  - "serialization"
  - "export"
  - "delimiter-separated-values"
triggers:
  - "Need to export array of objects or rows as CSV/TSV; preparing data for file output or transmission"
examples:
  - input: "[{name: \"Alice\", age: 30}, {name: \"Bob\", age: 25}]"
    output: "name,age\nAlice,30\nBob,25"
    notes: "csvFormat on array of objects produces CSV with header row"
  - input: "[[\"Alice\", 30], [\"Bob\", 25]]"
    output: "Alice,30\nBob,25"
    notes: "csvFormatRows on array of rows produces CSV without headers"
  - input: "[{name: \"Alice\", age: 30}]"
    output: "Alice,30"
    notes: "csvFormatBody on array of objects produces body only (no header)"
---

# Format structured data as delimiter-separated values

Convert arrays of objects or rows into CSV or TSV strings for export or transmission. Handles both object-based and row-based input formats with support for custom delimiters.

## Prompt

Given an array of objects (with consistent keys) or an array of rows (arrays of values), format it as a delimited string using the specified delimiter (comma for CSV, tab for TSV, or custom). Optionally format only the body (excluding headers) or individual rows/values.

## Objective

Convert structured data to delimited text
## Applicable Signals

- Need to export array of objects as CSV or TSV
- Preparing tabular data for file output
- Serializing data for transmission or API response
- Converting in-memory table to text format

## Contraindications

- Data is already in text or binary format
- Binary output is required
- Streaming large datasets (use row-by-row formatting instead)

## Intervention Moves

- Call csvFormat() or tsvFormat() on array of objects to produce full CSV/TSV with headers
- Call csvFormatBody() or tsvFormatBody() to format objects without header row
- Call csvFormatRows() or tsvFormatRows() on array of rows (no headers)
- Call csvFormatRow() or tsvFormatRow() on single row
- Call csvFormatValue() or tsvFormatValue() on single value to escape/quote as needed
- Call dsvFormat(delimiter) to create custom delimiter formatter

## Workflow Steps

- {'step': 1, 'action': 'Determine input type: array of objects or array of rows', 'condition': 'Inspect input structure'}
- {'step': 2, 'action': 'Select formatter: csvFormat/tsvFormat for objects, csvFormatRows/tsvFormatRows for rows', 'condition': 'Based on input type and whether headers are needed'}
- {'step': 3, 'action': 'Call formatter with input array', 'condition': 'Input is valid and non-empty'}
- {'step': 4, 'action': 'Return formatted string', 'condition': 'Formatting completed without error'}

## Constraints

- Input must be a valid array of objects (with consistent keys) or array of rows
- Delimiter must be a single character or recognized string
- Special characters in values (quotes, newlines, delimiters) are automatically escaped

## Cautions

- Ensure all objects in array have the same keys; missing keys produce empty cells
- Large arrays may produce very large strings; consider memory constraints
- Line endings are normalized; verify output line-ending convention matches target system

## Output Contract

- A formatted CSV or TSV string with proper escaping and quoting, ready for file write, HTTP transmission, or downstream consumption. String includes headers (if input is objects) and all rows.

## Example Executions

### Example 1

- Input: [{name: "Alice", age: 30}, {name: "Bob", age: 25}]
- Output: name,age
Alice,30
Bob,25
- Notes: csvFormat on array of objects produces CSV with header row

### Example 2

- Input: [["Alice", 30], ["Bob", 25]]
- Output: Alice,30
Bob,25
- Notes: csvFormatRows on array of rows produces CSV without headers

### Example 3

- Input: [{name: "Alice", age: 30}]
- Output: Alice,30
- Notes: csvFormatBody on array of objects produces body only (no header)

## Triggers

- Need to export array of objects or rows as CSV/TSV; preparing data for file output or transmission

## Examples

### Example 1

Input:

  [{name: "Alice", age: 30}, {name: "Bob", age: 25}]

Output:

  name,age
  Alice,30
  Bob,25

Notes:

  csvFormat on array of objects produces CSV with header row

### Example 2

Input:

  [["Alice", 30], ["Bob", 25]]

Output:

  Alice,30
  Bob,25

Notes:

  csvFormatRows on array of rows produces CSV without headers

### Example 3

Input:

  [{name: "Alice", age: 30}]

Output:

  Alice,30

Notes:

  csvFormatBody on array of objects produces body only (no header)
