---
id: "5fec3304-bf88-58e3-9ae4-1247747273ca"
name: "Scale Instance Duplication"
description: "Create an independent copy of an existing ordinal scale, preserving its domain, range, and unknown-value configuration. Use this when you need a variant with the same initial settings but allow independent modifications without affecting the original."
version: "0.1.0"
tags:
  - "scale"
  - "ordinal"
  - "duplication"
  - "cloning"
  - "d3"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "You have a configured ordinal scale and need to create a variant with the same initial settings"
  - "You need to allow independent modifications without affecting the original scale"
examples:
  - input: "ordinal scale with domain=['a', 'b', 'c'] and range=['red', 'green', 'blue']"
    output: "new scale instance with domain=['a', 'b', 'c'] and range=['red', 'green', 'blue']"
    notes: "Modifying the copy's domain does not affect the original scale"
---

# Scale Instance Duplication

Create an independent copy of an existing ordinal scale, preserving its domain, range, and unknown-value configuration. Use this when you need a variant with the same initial settings but allow independent modifications without affecting the original.

## Prompt

Call ordinal.copy() on a configured ordinal scale instance to produce a new scale object with identical domain, range, and unknown-value settings. The returned scale is independent; mutations to the copy do not affect the source.

## Objective

Duplicate a scale for independent mutation or reuse in a separate context
## Applicable Signals

- Ordinal scale instance exists with domain, range, and unknown-value configuration
- Downstream code requires a separate scale instance with identical initial state

## Contraindications

- You only need a reference to the same scale; copying is unnecessary overhead
- The scale is not yet configured; copy after full configuration

## Workflow Steps

- {'step': 1, 'action': 'Obtain a reference to a configured ordinal scale instance', 'input': 'ordinal scale object', 'output': None}
- {'step': 2, 'action': 'Invoke the .copy() method on the scale', 'input': 'ordinal.copy()', 'output': 'new scale instance'}
- {'step': 3, 'action': 'Verify the copy has identical domain, range, and unknown-value settings', 'input': 'new scale instance', 'output': 'confirmation of state equivalence'}

## Constraints

- Source scale must be a valid ordinal scale instance
- Copy operation preserves state at invocation time; subsequent mutations to source are not reflected in the copy

## Cautions

- Copying is a shallow operation; ensure domain and range are immutable or handle mutations carefully

## Output Contract

- A new scale object with identical domain, range, and unknown-value settings, independent from the source scale. Mutations to the copy do not affect the original.

## Example Therapist Responses

### Example 1

- Client/Input: ordinal scale with domain=['a', 'b', 'c'] and range=['red', 'green', 'blue']
- Therapist/Output: new scale instance with domain=['a', 'b', 'c'] and range=['red', 'green', 'blue']
- Notes: Modifying the copy's domain does not affect the original scale

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- You have a configured ordinal scale and need to create a variant with the same initial settings
- You need to allow independent modifications without affecting the original scale

## Examples

### Example 1

Input:

  ordinal scale with domain=['a', 'b', 'c'] and range=['red', 'green', 'blue']

Output:

  new scale instance with domain=['a', 'b', 'c'] and range=['red', 'green', 'blue']

Notes:

  Modifying the copy's domain does not affect the original scale
