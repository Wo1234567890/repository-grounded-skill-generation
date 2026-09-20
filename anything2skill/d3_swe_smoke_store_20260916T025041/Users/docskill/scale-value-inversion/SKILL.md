---
id: "8178b070-8aca-5d19-93e2-2b2a984a8273"
name: "Scale Value Inversion"
description: "Compute the domain value corresponding to a given range value on a linear scale. Use when reverse-mapping output values back to input domain for interaction or coordinate transformation."
version: "0.1.0"
tags:
  - "scale"
  - "inversion"
  - "coordinate_transformation"
  - "interaction"
  - "reverse_mapping"
triggers:
  - "need to convert screen coordinates or output values back to data domain"
  - "handling mouse interactions or zoom operations"
  - "reverse-lookup from rendered position to underlying data value"
---

# Scale Value Inversion

Compute the domain value corresponding to a given range value on a linear scale. Use when reverse-mapping output values back to input domain for interaction or coordinate transformation.

## Prompt

Call this skill when you need to convert a range value (e.g., screen coordinate, output value) back to its corresponding domain value (e.g., data value). Provide the range value to invert. The skill returns the single domain value that maps to that range value under the current scale configuration.

## Objective

reverse-map a range value to its corresponding domain value
## Applicable Signals

- user interaction event with screen coordinate
- output value requiring domain interpretation
- coordinate transformation request

## Contraindications

- scale has clamping disabled and input is outside range
- scale is not invertible (e.g., some color scales)
- range value is undefined or null

## Workflow Steps

- receive range value as input
- apply scale inversion function to range value
- return corresponding domain value

## Constraints

- scale must be invertible
- range value must be within or near the configured output range
- scale configuration must remain stable during inversion

## Cautions

- verify scale invertibility before calling
- handle edge cases where range value is at or beyond domain boundaries
- consider numerical precision for floating-point range values

## Output Contract

- single domain value corresponding to the provided range input; null or error if inversion is not possible

## Triggers

- need to convert screen coordinates or output values back to data domain
- handling mouse interactions or zoom operations
- reverse-lookup from rendered position to underlying data value
