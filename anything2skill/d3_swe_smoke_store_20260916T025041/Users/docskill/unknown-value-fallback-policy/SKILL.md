---
id: "2fa9f966-03c3-5dd1-a4f1-9650bbbc87dd"
name: "Unknown Value Fallback Policy"
description: "Define and apply a fallback output value for domain inputs that are not explicitly mapped in an ordinal scale. When an ordinal scale receives a domain value outside its registered set, return a configured unknown value instead of undefined output."
version: "0.1.0"
tags:
  - "ordinal-scale"
  - "fallback"
  - "error-handling"
  - "d3-scale"
triggers:
  - "An ordinal scale receives a domain value that was not included in the initial domain definition; you need predictable behavior instead of undefined output."
examples:
  - input: "ordinal scale with domain ['a', 'b', 'c']; query with 'd' (unmapped); unknown set to 'N/A'"
    output: "scale('d') returns 'N/A'"
    notes: "Custom fallback value is returned for out-of-range input"
  - input: "ordinal scale with domain ['a', 'b']; query with 'c' (unmapped); unknown set to d3.scaleImplicit"
    output: "scale('c') returns implicit range value; 'c' is added to domain"
    notes: "Implicit mode auto-extends domain on first unmapped query"
---

# Unknown Value Fallback Policy

Define and apply a fallback output value for domain inputs that are not explicitly mapped in an ordinal scale. When an ordinal scale receives a domain value outside its registered set, return a configured unknown value instead of undefined output.

## Prompt

Set the unknown value handler on an ordinal scale using ordinal.unknown(value). Pass either d3.scaleImplicit (implicit domain mode) or a custom fallback value. When the scale is later queried with an unmapped domain input, it will return the configured fallback instead of undefined.

## Objective

Handle unmapped domain values gracefully by returning a configured unknown value
## Applicable Signals

- Ordinal scale receives a domain value not in the initial domain definition
- Need predictable fallback behavior for out-of-range inputs
- Caller wants to avoid undefined or null returns from scale queries

## Contraindications

- All possible domain values are known and pre-registered in advance
- Unknown-value handling is unnecessary or undesired
- Scale is not ordinal (e.g., linear, log, or other continuous scale)

## Workflow Steps

- {'step': 1, 'action': 'Create or retrieve an ordinal scale instance'}
- {'step': 2, 'action': 'Call ordinal.unknown(value) with either d3.scaleImplicit or a custom fallback value'}
- {'step': 3, 'action': 'Query the scale with domain inputs; unmapped values will return the configured unknown value'}

## Constraints

- Must be called on an ordinal scale instance before querying with unmapped inputs
- Unknown value must be a valid output type compatible with the scale's range

## Cautions

- Setting unknown to d3.scaleImplicit enables implicit domain mode; new unmapped values are added to the domain automatically
- Custom fallback values are returned as-is; ensure they are meaningful in the caller's context

## Output Contract

- The scale returns the configured unknown value (e.g., d3.scaleImplicit or a custom fallback) when queried with an unmapped input. No undefined or error is thrown.

## Example Therapist Responses

### Example 1

- Client/Input: ordinal scale with domain ['a', 'b', 'c']; query with 'd' (unmapped); unknown set to 'N/A'
- Therapist/Output: scale('d') returns 'N/A'
- Notes: Custom fallback value is returned for out-of-range input

### Example 2

- Client/Input: ordinal scale with domain ['a', 'b']; query with 'c' (unmapped); unknown set to d3.scaleImplicit
- Therapist/Output: scale('c') returns implicit range value; 'c' is added to domain
- Notes: Implicit mode auto-extends domain on first unmapped query

## Triggers

- An ordinal scale receives a domain value that was not included in the initial domain definition; you need predictable behavior instead of undefined output.

## Examples

### Example 1

Input:

  ordinal scale with domain ['a', 'b', 'c']; query with 'd' (unmapped); unknown set to 'N/A'

Output:

  scale('d') returns 'N/A'

Notes:

  Custom fallback value is returned for out-of-range input

### Example 2

Input:

  ordinal scale with domain ['a', 'b']; query with 'c' (unmapped); unknown set to d3.scaleImplicit

Output:

  scale('c') returns implicit range value; 'c' is added to domain

Notes:

  Implicit mode auto-extends domain on first unmapped query
