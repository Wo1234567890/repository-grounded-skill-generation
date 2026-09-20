---
id: "6e5e7931-8031-512e-b31f-5a092a7c8933"
name: "Locale-Specific Time Formatter Creation"
description: "Define or retrieve a locale configuration and instantiate formatters and parsers bound to that locale's conventions. Enables repeated time formatting operations with consistent locale-specific rules."
version: "0.1.0"
tags:
  - "time_formatting"
  - "locale_configuration"
  - "d3_time_format"
  - "initialization"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Need to format or parse multiple timestamps with the same locale"
  - "Switching between default and custom locale configurations"
  - "Initializing a time formatting workflow that will be reused across multiple operations"
---

# Locale-Specific Time Formatter Creation

Define or retrieve a locale configuration and instantiate formatters and parsers bound to that locale's conventions. Enables repeated time formatting operations with consistent locale-specific rules.

## Prompt

1. Determine the target locale: use the default locale or define a custom locale via d3.timeFormatLocale().
2. Retrieve or create the locale object.
3. Bind formatter and parser methods to the locale object: locale.format(), locale.parse(), locale.utcFormat(), locale.utcParse().
4. Return the locale object with all four methods ready for invocation by downstream callers.

## Objective

Create a locale-bound formatter or parser object for repeated time formatting operations
## Applicable Signals

- Caller requests locale-specific time formatting
- Custom locale definition is provided
- Multiple formatting operations are planned with consistent locale rules

## Contraindications

- One-off time formatting with no reuse
- Using only ISO 8601 or UTC standard formats without locale customization
- No locale switching required

## Intervention Moves

- Validate locale definition structure before binding
- Confirm all four methods are accessible on the returned locale object

## Workflow Steps

- {'step': 1, 'action': 'Determine locale source', 'detail': 'Check if using default locale (d3.timeFormatDefaultLocale) or custom locale (d3.timeFormatLocale)'}
- {'step': 2, 'action': 'Retrieve or define locale', 'detail': 'If custom, call d3.timeFormatLocale(definition) with locale specification; otherwise use default'}
- {'step': 3, 'action': 'Bind formatter methods', 'detail': 'Access locale.format(), locale.parse(), locale.utcFormat(), locale.utcParse() to confirm all methods are available'}
- {'step': 4, 'action': 'Return locale object', 'detail': 'Pass the fully initialized locale object to caller for use in downstream formatting operations'}

## Constraints

- Locale object must be fully initialized before downstream formatters are invoked
- All four methods (format, parse, utcFormat, utcParse) must be bound to the same locale instance

## Cautions

- Ensure locale definition is valid before binding; invalid locale configurations will cause downstream formatting failures
- Locale objects are not thread-safe; do not share a single locale instance across concurrent formatting operations without synchronization

## Output Contract

- Locale object with bound format(), parse(), utcFormat(), and utcParse() methods ready for invocation. Caller receives a reusable locale instance that can be passed to multiple formatting operations without re-initialization.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Need to format or parse multiple timestamps with the same locale
- Switching between default and custom locale configurations
- Initializing a time formatting workflow that will be reused across multiple operations
