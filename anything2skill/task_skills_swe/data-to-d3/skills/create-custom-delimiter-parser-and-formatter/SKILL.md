---
id: "58123025-697f-56a3-8135-f0198a1b2efe"
name: "Create custom delimiter parser and formatter"
description: "Instantiate a reusable parser and formatter for non-standard delimiter-separated values. Use when working with custom-delimited data formats that require repeated parsing and formatting operations."
version: "0.1.0"
tags:
  - "data_parsing"
  - "text_parsing"
  - "delimiter"
  - "csv"
  - "tsv"
  - "dsv"
triggers:
  - "Non-standard delimiter (pipe, semicolon, etc.) is required"
  - "Need reusable parser for repeated use across multiple datasets"
  - "Custom delimiter format is known and fixed"
examples:
  - input: "delimiter = '|', text = 'name|age\\nAlice|30\\nBob|25'"
    output: "formatter.parse(text) returns [{name: 'Alice', age: '30'}, {name: 'Bob', age: '25'}]"
    notes: "Pipe-delimited data parsed into objects with header-derived keys"
  - input: "delimiter = ';', objects = [{id: '1', value: 'x'}, {id: '2', value: 'y'}]"
    output: "formatter.format(objects) returns 'id;value\\n1;x\\n2;y'"
    notes: "Objects serialized back to semicolon-delimited format"
---

# Create custom delimiter parser and formatter

Instantiate a reusable parser and formatter for non-standard delimiter-separated values. Use when working with custom-delimited data formats that require repeated parsing and formatting operations.

## Prompt

Call d3.dsvFormat(delimiter) with your custom delimiter character (e.g., '|', ';', '\t') to create a DSV formatter object. The returned object exposes parse, parseRows, format, formatBody, formatRows, formatRow, and formatValue methods. Use the same formatter instance across multiple parse/format operations to avoid recreating it.

## Objective

Instantiate delimiter-specific parsing and formatting functions for custom-delimited data
## Applicable Signals

- Input data uses non-CSV/TSV delimiter
- Caller has identified the exact delimiter character
- Multiple parse/format operations expected in same session

## Contraindications

- Standard CSV or TSV format suffices
- Delimiter is unknown or variable across inputs
- One-off parsing without reuse

## Workflow Steps

- {'step': 1, 'action': "Identify the custom delimiter character (e.g., '|', ';')", 'input': 'Delimiter string'}
- {'step': 2, 'action': 'Call d3.dsvFormat(delimiter) to create formatter object', 'input': 'Delimiter character', 'output': 'DSV formatter instance'}
- {'step': 3, 'action': 'Use formatter.parse(text) to parse delimited string into array of objects', 'input': 'Delimited text string', 'output': 'Array of objects with keys from header row'}
- {'step': 4, 'action': 'Use formatter.format(data) or formatter.formatRows(rows) to serialize back to delimited format', 'input': 'Array of objects or array of rows', 'output': 'Formatted delimited string'}

## Constraints

- Delimiter must be a single character or known string
- Formatter object should be created once and reused
- Input string must be well-formed for the specified delimiter

## Cautions

- Ensure delimiter does not appear unescaped within field values unless properly quoted
- Reuse formatter instance to avoid performance overhead of repeated instantiation

## Output Contract

- Returns a DSV formatter object with methods: parse(text), parseRows(text), format(objects), formatBody(objects), formatRows(rows), formatRow(row), formatValue(value). Each method operates on the specified delimiter. Caller receives a reusable, stateless formatter instance.

## Example Executions

### Example 1

- Input: delimiter = '|', text = 'name|age\nAlice|30\nBob|25'
- Output: formatter.parse(text) returns [{name: 'Alice', age: '30'}, {name: 'Bob', age: '25'}]
- Notes: Pipe-delimited data parsed into objects with header-derived keys

### Example 2

- Input: delimiter = ';', objects = [{id: '1', value: 'x'}, {id: '2', value: 'y'}]
- Output: formatter.format(objects) returns 'id;value\n1;x\n2;y'
- Notes: Objects serialized back to semicolon-delimited format

## Triggers

- Non-standard delimiter (pipe, semicolon, etc.) is required
- Need reusable parser for repeated use across multiple datasets
- Custom delimiter format is known and fixed

## Examples

### Example 1

Input:

  delimiter = '|', text = 'name|age\nAlice|30\nBob|25'

Output:

  formatter.parse(text) returns [{name: 'Alice', age: '30'}, {name: 'Bob', age: '25'}]

Notes:

  Pipe-delimited data parsed into objects with header-derived keys

### Example 2

Input:

  delimiter = ';', objects = [{id: '1', value: 'x'}, {id: '2', value: 'y'}]

Output:

  formatter.format(objects) returns 'id;value\n1;x\n2;y'

Notes:

  Objects serialized back to semicolon-delimited format
