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
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
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

## 子技能目录
- [Format structured data as delimiter-separated values](通用技能领域/Family技能/未分类技能/微技能/Format structured data as delimiter-separated values/SKILL.md) ｜ 适用：Convert arrays of objects or rows into CSV, TSV, or custom delimiter-separated strings for export or transmission. Supports both object-based input (with headers extracted from keys) and row-based input (values only). Handles proper escaping of special characters and delimiter-containing values.
- [ISO 8601 UTC Time Formatting and Parsing](通用技能领域/Family技能/未分类技能/微技能/ISO 8601 UTC Time Formatting and Parsing/SKILL.md) ｜ 适用：Format Date objects to ISO 8601 UTC strings or parse ISO 8601 UTC strings to Date objects. Provides standard UTC time serialization and deserialization without locale customization.
- [Locale-Specific Time Formatter Creation](通用技能领域/Family技能/未分类技能/微技能/Locale-Specific Time Formatter Creation/SKILL.md) ｜ 适用：Define or retrieve a locale configuration and instantiate formatters and parsers bound to that locale's conventions. Enables repeated time formatting operations with consistent locale-specific rules.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `Format structured data as delimiter-separated values` 时，优先调用它。 线索：Need to export array of objects as CSV or TSV, Preparing tabular data for file output, Serializing data for transmission or API response, Converting in-memory data structures to text format, data_export
- 当目标、阶段或方法更接近 `ISO 8601 UTC Time Formatting and Parsing` 时，优先调用它。 线索：Exchanging timestamps with external systems, Storing times in canonical UTC format, ISO 8601 compliance required, time_formatting, iso_8601
- 当目标、阶段或方法更接近 `Locale-Specific Time Formatter Creation` 时，优先调用它。 线索：Need to format or parse multiple timestamps with the same locale, Switching between default and custom locale configurations, Initializing a time formatting workflow that will be reused across multiple operations, time_formatting, locale_configuration

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Need to format Date objects to strings
- Need to parse time strings to Date objects
- Working with locale-specific timestamps
- Working with UTC or ISO 8601 timestamps
