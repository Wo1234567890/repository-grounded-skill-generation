---
id: "a4306205-1f72-5158-91e6-122dd38c830c"
name: "Agentic Library Detection and Instrumentation Halt"
description: "Detect when an agentic library (e.g., CrewAI, AutoGen) is instrumented during module iteration and halt further instrumentation to prevent conflicts and redundant instrumentation."
version: "0.1.0"
tags:
  - "instrumentation"
  - "safety"
  - "conflict_prevention"
  - "agentic_libraries"
  - "initialization"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Module iteration begins during instrumentation startup"
  - "_has_agentic_library flag is checked within the loop"
---

# Agentic Library Detection and Instrumentation Halt

Detect when an agentic library (e.g., CrewAI, AutoGen) is instrumented during module iteration and halt further instrumentation to prevent conflicts and redundant instrumentation.

## Prompt

During module iteration in the instrumentation startup phase, check the _has_agentic_library flag. If it becomes True, immediately break the loop and return to prevent further module instrumentation. This guardrail ensures that once an agentic library is detected and instrumented, no additional instrumentation attempts are made that could cause conflicts.

## Objective

Prevent redundant or conflicting instrumentation of agentic libraries
## Applicable Signals

- sys.modules iteration is active
- _has_agentic_library transitions from False to True

## Contraindications

- No agentic libraries are present in the runtime environment
- Instrumentation startup is already complete
- Module iteration has not yet begun

## Workflow Steps

- {'step': 1, 'action': 'Check _has_agentic_library flag at the start of each module iteration', 'condition': 'Loop is active and iterating through sys.modules'}
- {'step': 2, 'action': 'If _has_agentic_library is True, break the loop immediately', 'condition': 'Flag evaluates to True'}
- {'step': 3, 'action': 'Return from instrumentation function to halt further processing', 'condition': 'Loop has been broken'}

## Constraints

- The _has_agentic_library flag must be accessible and mutable during iteration
- The check must occur within the module iteration loop
- Loop termination must be immediate upon flag detection

## Cautions

- Ensure the flag is set to True only when an agentic library is actually instrumented, not on false positives
- Verify that breaking the loop does not leave partial instrumentation state

## Output Contract

- Loop breaks immediately when _has_agentic_library becomes True; no further modules are instrumented after agentic library detection. Caller receives confirmation that instrumentation has halted to prevent conflicts.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Module iteration begins during instrumentation startup
- _has_agentic_library flag is checked within the loop
