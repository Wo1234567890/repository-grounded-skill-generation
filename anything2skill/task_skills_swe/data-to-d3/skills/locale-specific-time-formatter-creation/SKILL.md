---
id: "6e5e7931-8031-512e-b31f-5a092a7c8933"
name: "Locale-Specific Time Formatter Creation"
description: "Invoke the generate_documentation.py script to automatically create documentation files from example notebooks. Use this micro operation after creating or updating notebooks and before publishing to the website."
version: "0.1.1"
tags:
  - "documentation"
  - "automation"
  - "notebook_processing"
  - "script_invocation"
  - "example_management"
triggers:
  - "Formatting or parsing multiple timestamps with the same locale"
  - "Need to switch between default and custom locales"
examples:
  - input: "Create a formatter for a custom locale with French month names, then format a date"
    output: "const locale = d3.timeFormatLocale({...frenchMonthNames}); const fmt = locale.format('%d %B %Y'); fmt(new Date(2024, 0, 15)) → '15 janvier 2024'"
    notes: "Locale definition includes months, days, and format specifiers; formatter function is reusable"
  - input: "Set default locale and use shorthand d3.timeFormat()"
    output: "d3.timeFormatDefaultLocale({...customDef}); d3.timeFormat('%Y-%m-%d')(date) → uses custom locale"
    notes: "After setting default, d3.timeFormat() and d3.timeParse() use the new locale"
---

# Locale-Specific Time Formatter Creation

Invoke the generate_documentation.py script to automatically create documentation files from example notebooks. Use this micro operation after creating or updating notebooks and before publishing to the website.

## Prompt

Execute the generate_documentation.py script with the notebook source as input. The script will parse the notebook and generate corresponding documentation files. Ensure the notebook is self-contained and follows naming conventions before invocation.

## Objective

Produce documentation artifacts from notebook source
## Applicable Signals

- Notebook file created or modified
- Documentation refresh requested
- Pre-publication validation phase

## Contraindications

- Do not use when manually editing generated documentation files
- Do not use for creating documentation for non-notebook content
- Do not invoke if notebook is not self-contained or runnable

## Workflow Steps

- Verify notebook is self-contained and follows naming conventions
- Invoke generate_documentation.py script with notebook path as input
- Script parses notebook and generates documentation files
- Verify generated files are created in docs/v2/examples/ directory
- Confirm documentation is ready for website deployment

## Constraints

- Notebook must be self-contained and executable
- Notebook must follow existing naming conventions
- Output directory docs/v2/examples/ must exist and be writable

## Cautions

- Ensure notebook content is complete before running script
- Verify output files are correctly formatted before publishing
- Check that generated documentation matches notebook intent

## Output Contract

- Generated documentation files created in docs/v2/examples/ directory, ready for website visibility and deployment

## Triggers

- Formatting or parsing multiple timestamps with the same locale
- Need to switch between default and custom locales

## Examples

### Example 1

Input:

  Create a formatter for a custom locale with French month names, then format a date

Output:

  const locale = d3.timeFormatLocale({...frenchMonthNames}); const fmt = locale.format('%d %B %Y'); fmt(new Date(2024, 0, 15)) → '15 janvier 2024'

Notes:

  Locale definition includes months, days, and format specifiers; formatter function is reusable

### Example 2

Input:

  Set default locale and use shorthand d3.timeFormat()

Output:

  d3.timeFormatDefaultLocale({...customDef}); d3.timeFormat('%Y-%m-%d')(date) → uses custom locale

Notes:

  After setting default, d3.timeFormat() and d3.timeParse() use the new locale
