---
id: "406ccc39-4e23-5fc0-8440-b962bfa140cd"
name: "Configure Ordinal Scale Unknown Value Fallback"
description: "Set a fallback output value for domain inputs that are not explicitly mapped in an ordinal scale. Prevents undefined or null returns when an ordinal scale encounters unmapped domain values."
version: "0.1.0"
tags:
  - "ordinal_scale"
  - "fallback_handling"
  - "error_recovery"
  - "d3_scale"
triggers:
  - "An ordinal scale must handle unexpected or dynamically added domain values gracefully; prevents undefined or null returns."
---

# Configure Ordinal Scale Unknown Value Fallback

Set a fallback output value for domain inputs that are not explicitly mapped in an ordinal scale. Prevents undefined or null returns when an ordinal scale encounters unmapped domain values.

## Prompt

Call ordinal.unknown(value) to set the fallback output for any domain input not in the scale's explicit domain. This ensures graceful handling of unexpected or dynamically added domain values.

## Objective

Set the output value returned when an unmapped domain value is queried on an ordinal scale
## Applicable Signals

- Ordinal scale must handle unexpected or dynamically added domain values
- Caller needs graceful fallback instead of undefined/null returns
- Scale is used in contexts where unmapped inputs are possible

## Contraindications

- All possible domain values are known and pre-registered at scale creation
- Strict validation or error-on-unknown behavior is required
- Caller prefers exceptions over silent fallback handling

## Workflow Steps

- Obtain or create an ordinal scale instance
- Identify the desired fallback value (e.g., a default color, category, or placeholder)
- Call ordinal.unknown(fallbackValue) to register the handler
- Verify that subsequent queries with unmapped domain values return the fallback

## Constraints

- Must be applied to an existing ordinal scale instance
- Fallback value must be compatible with the scale's output range type
- Unknown-value handler applies only to subsequent queries after configuration

## Output Contract

- Ordinal scale with unknown-value handler configured; subsequent queries with unmapped inputs return the specified fallback value instead of undefined.

## Triggers

- An ordinal scale must handle unexpected or dynamically added domain values gracefully; prevents undefined or null returns.
