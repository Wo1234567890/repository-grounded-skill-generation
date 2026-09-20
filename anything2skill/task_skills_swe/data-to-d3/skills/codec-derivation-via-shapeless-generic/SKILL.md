---
id: "d48640d4-ca67-5f31-9713-9b0042e491cc"
name: "Codec Derivation via Shapeless Generic"
description: "Create an independent copy of an existing scale (ordinal, threshold, or other scale type), preserving domain, range, and configuration. Use this when you need a variant of a scale without modifying the original, or when reusing a scale template across multiple visualizations or independent mutations."
version: "0.1.3"
tags:
  - "d3"
  - "scale"
  - "threshold"
  - "cloning"
  - "copy"
triggers:
  - "Defining JSON serialization for a new case class or sealed trait"
  - "Need to avoid manual Encoder/Decoder implementations"
  - "Seeking to minimize compile-time overhead from macro expansion"
examples:
  - input: "Existing threshold scale with domain [0, 10, 20] and range ['low', 'medium', 'high']"
    output: "New threshold scale with same domain and range, independent from original"
    notes: "Modifications to the copy's domain or range do not affect the original scale"
---

# Codec Derivation via Shapeless Generic

Create an independent copy of an existing scale (ordinal, threshold, or other scale type), preserving domain, range, and configuration. Use this when you need a variant of a scale without modifying the original, or when reusing a scale template across multiple visualizations or independent mutations.

## Prompt

Call threshold.copy() on an existing threshold scale instance to produce a new scale object with identical domain, range, and all configuration properties. The returned scale is independent; modifications to the copy do not affect the original.

## Objective

Duplicate a threshold scale for independent modification or reuse
## Applicable Signals

- Need to create a variant of an existing scale without modifying the original
- Reusing a scale template across multiple visualizations
- Preparing independent scale instances for parallel data transformations

## Contraindications

- Sharing the same scale instance across multiple contexts is acceptable and preferred for memory efficiency
- Memory constraints prohibit duplication of scale objects
- Scale is only used once and will not be reused

## Workflow Steps

- {'step': 1, 'action': 'Obtain reference to existing scale instance', 'detail': 'Ensure you have access to a configured scale (ordinal, threshold, or other type) with domain and range already set'}
- {'step': 2, 'action': 'Invoke .copy() method on the scale', 'detail': 'Call scale.copy() on the scale instance'}
- {'step': 3, 'action': 'Assign returned scale object to new variable', 'detail': 'Store the new scale reference for independent use'}
- {'step': 4, 'action': 'Verify cloned scale has identical domain and range as original (optional validation)', 'detail': 'Confirm that scale.domain() and scale.range() match the original'}

## Constraints

- Source scale must be a valid scale instance (ordinal, threshold, or compatible type)
- Cloning preserves domain, range, and configuration settings at the time of cloning; custom properties are not guaranteed to copy
- Subsequent modifications to either scale are independent

## Cautions

- Cloned scale is independent; subsequent modifications to either the original or clone do not propagate
- If shared state is required, use the original scale reference instead of cloning

## Output Contract

- Returns a new threshold scale object with identical configuration to the source. The copy is a separate instance suitable for independent modification, querying, or reuse in different visualization contexts.

## Example Executions

### Example 1

- Input: Existing threshold scale with domain [0, 10, 20] and range ['low', 'medium', 'high']
- Output: New threshold scale with same domain and range, independent from original
- Notes: Modifications to the copy's domain or range do not affect the original scale

## Triggers

- Defining JSON serialization for a new case class or sealed trait
- Need to avoid manual Encoder/Decoder implementations
- Seeking to minimize compile-time overhead from macro expansion

## Examples

### Example 1

Input:

  Existing threshold scale with domain [0, 10, 20] and range ['low', 'medium', 'high']

Output:

  New threshold scale with same domain and range, independent from original

Notes:

  Modifications to the copy's domain or range do not affect the original scale
