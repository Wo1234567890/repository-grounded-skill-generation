---
id: "0c6f8e74-1f7b-5d39-bfcd-88ce3d52c947"
name: "ISO 8601 UTC Time Formatting and Parsing"
description: "Format Date objects to ISO 8601 UTC strings or parse ISO 8601 UTC strings to Date objects. Provides standard UTC time serialization and deserialization without locale customization."
version: "0.1.0"
tags:
  - "time_formatting"
  - "iso_8601"
  - "utc"
  - "serialization"
  - "deserialization"
  - "data_transformation"
triggers:
  - "Exchanging timestamps with external systems"
  - "Storing times in canonical UTC format"
  - "ISO 8601 compliance required"
examples:
  - input: "new Date('2024-01-15T10:30:45Z')"
    output: "2024-01-15T10:30:45Z"
    notes: "Format operation: Date object to ISO 8601 string"
  - input: "2024-01-15T10:30:45Z"
    output: "Date object representing 2024-01-15 10:30:45 UTC"
    notes: "Parse operation: ISO 8601 string to Date object"
---

# ISO 8601 UTC Time Formatting and Parsing

Format Date objects to ISO 8601 UTC strings or parse ISO 8601 UTC strings to Date objects. Provides standard UTC time serialization and deserialization without locale customization.

## Prompt

Use d3.isoFormat to convert a Date object to an ISO 8601 UTC string (e.g., 2024-01-15T10:30:45Z). Use d3.isoParse to convert an ISO 8601 UTC string back to a Date object. No locale configuration is required.

## Objective

Perform standard ISO 8601 UTC time serialization and deserialization
## Applicable Signals

- Need for interoperability with standard time formats
- UTC-only time representation required
- No locale-specific formatting needed

## Contraindications

- Locale-specific formatting needed
- Custom time format patterns required
- Local timezone representation required

## Workflow Steps

- {'step': 1, 'action': 'Determine operation type', 'detail': 'Decide whether to format (Date → string) or parse (string → Date)'}
- {'step': 2, 'action': 'Format operation', 'detail': 'Call d3.isoFormat(date) to convert Date object to ISO 8601 UTC string'}
- {'step': 3, 'action': 'Parse operation', 'detail': 'Call d3.isoParse(string) to convert ISO 8601 UTC string to Date object'}
- {'step': 4, 'action': 'Validate output', 'detail': 'Confirm string matches ISO 8601 format or Date object is valid'}

## Constraints

- Output is always UTC; no timezone offset customization
- Input strings must be valid ISO 8601 UTC format

## Cautions

- Ensure input Date objects are in UTC or convert before formatting
- Parsed Date objects are in UTC; apply timezone conversion if local time is needed

## Output Contract

- Returns either an ISO 8601 formatted UTC string (e.g., 2024-01-15T10:30:45Z) for format operations, or a valid Date object for parse operations. Both outputs are guaranteed to be in UTC.

## Example Executions

### Example 1

- Input: new Date('2024-01-15T10:30:45Z')
- Output: 2024-01-15T10:30:45Z
- Notes: Format operation: Date object to ISO 8601 string

### Example 2

- Input: 2024-01-15T10:30:45Z
- Output: Date object representing 2024-01-15 10:30:45 UTC
- Notes: Parse operation: ISO 8601 string to Date object

## Triggers

- Exchanging timestamps with external systems
- Storing times in canonical UTC format
- ISO 8601 compliance required

## Examples

### Example 1

Input:

  new Date('2024-01-15T10:30:45Z')

Output:

  2024-01-15T10:30:45Z

Notes:

  Format operation: Date object to ISO 8601 string

### Example 2

Input:

  2024-01-15T10:30:45Z

Output:

  Date object representing 2024-01-15 10:30:45 UTC

Notes:

  Parse operation: ISO 8601 string to Date object
