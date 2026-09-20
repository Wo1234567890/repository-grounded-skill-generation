---
id: "b3b6bb8f-b90b-5824-9383-50090e9ebc25"
name: "Parse delimiter-separated values"
description: "Parse CSV or TSV strings into structured arrays of objects or rows. Use when ingesting tabular data from text format."
version: "0.1.0"
tags:
  - "data_parsing"
  - "csv"
  - "tsv"
  - "text_parsing"
  - "data_ingestion"
  - "structured_data"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Raw CSV or TSV string input is available"
  - "Need to convert tabular text data into structured arrays"
  - "Ingesting data from external text sources"
---

# Parse delimiter-separated values

Parse CSV or TSV strings into structured arrays of objects or rows. Use when ingesting tabular data from text format.

## Prompt

Accept a delimited string (CSV or TSV) and parse it into either an array of objects (with headers as keys) or an array of row arrays. Choose the appropriate parser based on delimiter type and desired output structure.

## Objective

Convert delimited text to structured data
## Applicable Signals

- CSV or TSV string format detected
- Tabular data in text representation
- Data ingestion workflow initiated

## Contraindications

- Data is already structured (objects or arrays)
- Binary or non-text formats
- Streaming or real-time data requiring incremental parsing

## Workflow Steps

- {'step': 1, 'action': 'Identify delimiter type', 'detail': 'Determine if input is CSV (comma-delimited) or TSV (tab-delimited)'}
- {'step': 2, 'action': 'Select parser variant', 'detail': 'Choose between parse (returns array of objects) or parseRows (returns array of row arrays)'}
- {'step': 3, 'action': 'Execute parsing', 'detail': 'Call appropriate parser function with the delimited string'}
- {'step': 4, 'action': 'Validate output structure', 'detail': 'Confirm output is array of objects or array of rows as expected'}

## Constraints

- Input must be a valid delimited string
- Delimiter must be consistent throughout the input
- Headers (if present) must be on the first row for object-based parsing

## Cautions

- Ensure delimiter matches the actual data format (comma for CSV, tab for TSV)
- Large files may require chunked or streaming parsing for performance
- Special characters or quoted fields must be properly escaped in input

## Output Contract

- Array of objects (with headers as keys) or array of row arrays, ready for downstream processing or analysis

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Raw CSV or TSV string input is available
- Need to convert tabular text data into structured arrays
- Ingesting data from external text sources
