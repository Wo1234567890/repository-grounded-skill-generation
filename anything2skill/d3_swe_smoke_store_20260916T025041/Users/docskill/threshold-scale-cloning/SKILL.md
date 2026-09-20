---
id: "c00d3cbf-2fba-5cf3-93be-6fa44962917f"
name: "Threshold Scale Cloning"
description: "Create an independent copy of an existing threshold scale with the same domain, range, and configuration. Use this when you need a variant of an existing scale without modifying the original, or when reusing a scale configuration across multiple visualizations."
version: "0.1.0"
tags:
  - "scale"
  - "threshold"
  - "cloning"
  - "d3"
  - "quantizing"
  - "reuse"
triggers:
  - "Need to create a variant of an existing scale without modifying the original"
  - "Reusing a scale configuration across multiple visualizations"
  - "Preparing independent scale instances for parallel processing or branching logic"
---

# Threshold Scale Cloning

Create an independent copy of an existing threshold scale with the same domain, range, and configuration. Use this when you need a variant of an existing scale without modifying the original, or when reusing a scale configuration across multiple visualizations.

## Prompt

Call threshold.copy() on an existing threshold scale object to produce a new scale instance with identical domain, range, and all configuration properties. The returned scale is independent; modifications to the copy do not affect the original.

## Objective

Duplicate a threshold scale for independent modification or reuse
## Applicable Signals

- Existing threshold scale object is available
- Multiple consumers need the same scale configuration
- Scale will be modified downstream and original must be preserved

## Contraindications

- Creating a new scale from scratch is simpler and more direct
- No need for independent copies; a single shared scale is sufficient
- Performance-critical path where cloning overhead is unacceptable

## Workflow Steps

- {'step': 1, 'action': 'Obtain reference to existing threshold scale', 'detail': 'Ensure the source scale is a valid threshold scale instance with configured domain and range'}
- {'step': 2, 'action': 'Invoke copy() method', 'detail': 'Call sourceScale.copy() to generate a new independent scale instance'}
- {'step': 3, 'action': 'Verify cloned scale configuration', 'detail': 'Confirm that the returned scale has identical domain and range to the source'}
- {'step': 4, 'action': 'Use cloned scale independently', 'detail': 'Modify or query the cloned scale without affecting the original'}

## Constraints

- Source scale must be a valid threshold scale object
- Copy operation preserves domain, range, and all configuration at the time of cloning
- Subsequent modifications to the copy are independent of the original

## Cautions

- Cloning does not deep-copy nested objects in domain or range if they are mutable references; verify immutability of configuration values if needed
- Multiple clones consume additional memory; monitor for scale proliferation in long-running applications

## Output Contract

- Returns a new threshold scale object with identical domain, range, and configuration properties to the source scale. The returned scale is fully independent and ready for use or further modification.

## Triggers

- Need to create a variant of an existing scale without modifying the original
- Reusing a scale configuration across multiple visualizations
- Preparing independent scale instances for parallel processing or branching logic
