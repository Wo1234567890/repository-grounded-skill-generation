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
  - "d3"
triggers:
  - "need to convert screen coordinates or output values back to data domain"
  - "handling mouse interactions or zoom operations"
  - "coordinate transformation from range space to domain space"
---

# Scale Value Inversion

Compute the domain value corresponding to a given range value on a linear scale. Use when reverse-mapping output values back to input domain for interaction or coordinate transformation.

## Prompt

Call the invert method on a linear scale instance with a range value to obtain the corresponding domain value. This is useful for converting screen coordinates or output values back to data space.

## Objective

reverse-map a range value to its corresponding domain value
## Applicable Signals

- user interaction event with screen position
- output value requiring reverse lookup
- zoom or pan operation needing domain-space equivalents

## Contraindications

- scale has clamping disabled and input is outside range
- scale is not invertible (e.g., some color scales)
- domain or range is non-monotonic

## Workflow Steps

- Obtain or reference a configured linear scale instance
- Call the invert method with the range value to be converted
- Receive the corresponding domain value
- Use the domain value in downstream logic (e.g., data lookup, event handling)

## Constraints

- scale must be invertible
- input range value must be within or near the scale's output range for meaningful results
- linear scale must have been properly configured with domain and range before inversion

## Cautions

- non-invertible scales will return undefined or throw an error
- clamping behavior affects inversion results; verify scale configuration
- floating-point precision may affect exact domain recovery

## Output Contract

- Returns a single domain value corresponding to the provided range input. If the scale is not invertible or input is invalid, behavior is undefined or an error is raised.

## Triggers

- need to convert screen coordinates or output values back to data domain
- handling mouse interactions or zoom operations
- coordinate transformation from range space to domain space
