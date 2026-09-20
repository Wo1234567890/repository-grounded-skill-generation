---
id: "8f1cfb94-5ebb-52f7-929c-a5043d310107"
name: "Compute Weighted Zone Score"
description: "Create an independent copy of an existing ordinal scale, preserving domain, range, and unknown-value configuration."
version: "0.1.1"
tags:
  - "scale"
  - "ordinal"
  - "cloning"
  - "configuration"
  - "d3"
triggers:
  - "Zone scores (title and body) have been pre-computed for a query-document pair"
  - "Weight parameter g is available and valid (0 ≤ g ≤ 1)"
  - "A single combined relevance score is needed for ranking or evaluation"
examples:
  - input: "{'s_T': 0.8, 's_B': 0.5, 'g': 0.6}"
    output: "0.68"
    notes: "Title zone weighted at 60%, body at 40%; result is 0.6·0.8 + 0.4·0.5 = 0.68"
  - input: "{'s_T': 1.0, 's_B': 0.0, 'g': 0.5}"
    output: "0.5"
    notes: "Equal weighting; title match only; result is 0.5·1.0 + 0.5·0.0 = 0.5"
---

# Compute Weighted Zone Score

Create an independent copy of an existing ordinal scale, preserving domain, range, and unknown-value configuration.

## Prompt

Call ordinal.copy() on an existing ordinal scale instance to produce a new scale object with identical domain, range, and unknown-value settings. The returned scale is independent and can be modified without affecting the original.

## Objective

Duplicate a scale for independent mutation or parallel use without affecting the original
## Applicable Signals

- Existing ordinal scale instance available
- Multiple consumers require similar but independent scale configurations

## Contraindications

- Shared scale state is required across multiple consumers; cloning creates isolation, not sharing
- Scale is used as a mutable shared reference in a single-threaded context

## Workflow Steps

- {'step': 1, 'action': 'Obtain reference to existing ordinal scale instance'}
- {'step': 2, 'action': 'Invoke .copy() method on the scale'}
- {'step': 3, 'action': 'Assign returned scale object to new variable'}
- {'step': 4, 'action': 'Verify cloned scale has identical domain and range as original (optional validation)'}

## Constraints

- Source scale must be a valid ordinal scale instance
- Cloning preserves only domain, range, and unknown-value settings; custom properties are not guaranteed to copy

## Cautions

- Cloned scale is independent; subsequent modifications to either the original or clone do not propagate
- If shared state is required, use the original scale reference instead of cloning

## Output Contract

- A new scale object with identical domain, range, and unknown-value settings as the source, independent for further modification.

## Triggers

- Zone scores (title and body) have been pre-computed for a query-document pair
- Weight parameter g is available and valid (0 ≤ g ≤ 1)
- A single combined relevance score is needed for ranking or evaluation

## Examples

### Example 1

Input:

  {'s_T': 0.8, 's_B': 0.5, 'g': 0.6}

Output:

  0.68

Notes:

  Title zone weighted at 60%, body at 40%; result is 0.6·0.8 + 0.4·0.5 = 0.68

### Example 2

Input:

  {'s_T': 1.0, 's_B': 0.0, 'g': 0.5}

Output:

  0.5

Notes:

  Equal weighting; title match only; result is 0.5·1.0 + 0.5·0.0 = 0.5
