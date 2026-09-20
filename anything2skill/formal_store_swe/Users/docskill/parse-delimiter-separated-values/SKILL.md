---
id: "b3b6bb8f-b90b-5824-9383-50090e9ebc25"
name: "Parse delimiter-separated values"
description: "Parse CSV or TSV strings into structured arrays of objects or rows. Use when ingesting tabular data from text format."
version: "0.1.0"
tags:
  - "data_parsing"
  - "csv"
  - "tsv"
  - "text_transformation"
  - "input_handling"
  - "d3-dsv"
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

- CSV or TSV formatted string detected
- Tabular data in text format ready for processing
- Data ingestion workflow initiated

## Contraindications

- Data is already structured (objects or arrays)
- Input is binary or non-text format
- Data requires custom delimiter not standard CSV/TSV

## Intervention Moves

- Invoke d3.csvParse or d3.tsvParse for object-keyed output
- Invoke d3.csvParseRows or d3.tsvParseRows for row array output
- Apply d3.autoType for automatic type inference on parsed objects

## Workflow Steps

- Receive delimited string input
- Determine delimiter type (comma for CSV, tab for TSV, or custom via d3.dsvFormat)
- Select appropriate parser variant (parse for objects, parseRows for row arrays)
- Execute parser on input string
- Optionally apply d3.autoType for type inference
- Return structured array output

## Constraints

- Input must be a valid delimited string
- Headers (if present) must be on first row for object parsing
- Delimiter must be consistent throughout input

## Cautions

- Ensure input encoding is UTF-8 or compatible
- Large files may require streaming or chunked parsing
- Special characters in values may need escaping or proper quoting

## Output Contract

- Array of objects with header keys (via csvParse/tsvParse), or array of row arrays (via csvParseRows/tsvParseRows), or custom delimiter output (via dsvFormat). Returns null or empty array if input is empty or malformed.

## Triggers

- Raw CSV or TSV string input is available
- Need to convert tabular text data into structured arrays
- Ingesting data from external text sources
