---
id: "12888375-7271-5bd8-a3ad-cde4deb2c5cf"
name: "Time Format and Parse Operations"
description: "Create and apply time formatters and parsers using strptime/strftime-inspired syntax for both locale-specific and UTC/ISO 8601 timestamps. Converts between time objects and formatted strings."
version: "0.1.0"
tags:
  - "time"
  - "formatting"
  - "parsing"
  - "locale"
  - "UTC"
  - "ISO8601"
triggers:
  - "Need to format Date objects to strings"
  - "Need to parse time strings to Date objects"
  - "Working with locale-specific timestamps"
  - "Working with UTC or ISO 8601 timestamps"
---

# Time Format and Parse Operations

Create and apply time formatters and parsers using strptime/strftime-inspired syntax for both locale-specific and UTC/ISO 8601 timestamps. Converts between time objects and formatted strings.

## Prompt

Use this skill to format Date objects into strings or parse time strings into Date objects. Choose locale-specific formatters for regional conventions, UTC formatters for universal time, or ISO 8601 formatters for standard interchange. Apply the formatter or parser to your input and retrieve the result.

## Objective

Convert between time objects and formatted strings using locale or standard conventions
## Applicable Signals

- Input is a Date object requiring string representation
- Input is a time string requiring Date object conversion
- Locale-aware formatting is required
- UTC or ISO 8601 standard format is required

## Contraindications

- Performing timezone arithmetic or handling daylight saving time transitions
- Working with relative time durations
- Handling time zone offset calculations beyond format/parse scope

## Workflow Steps

- {'step': 1, 'action': 'Select formatter type', 'detail': 'Choose locale.format for locale-specific, locale.utcFormat for UTC, or d3.isoFormat for ISO 8601'}
- {'step': 2, 'action': 'Create formatter or parser', 'detail': 'Call the selected function with format pattern (for formatters) or no arguments (for parsers)'}
- {'step': 3, 'action': 'Apply to input', 'detail': 'Pass Date object to formatter or time string to parser'}
- {'step': 4, 'action': 'Return result', 'detail': 'Formatted string or parsed Date object'}

## Constraints

- Format pattern must follow strptime/strftime conventions
- Locale must be defined or use default locale
- Input must be a valid Date object or parseable time string

## Output Contract

- Formatted time string matching the specified locale and format pattern, or a parsed Date object from a valid time string. Output format adheres to strptime/strftime conventions or ISO 8601 standard as selected.

## Triggers

- Need to format Date objects to strings
- Need to parse time strings to Date objects
- Working with locale-specific timestamps
- Working with UTC or ISO 8601 timestamps
