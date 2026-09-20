---
id: "fb580e02-5e97-5a98-9a88-593c837d8917"
name: "Read Timestamp Extension with Delta Overflow Handling"
description: "Determine whether a software package should be instrumented for monitoring by evaluating three conditions: whether it is already instrumented by AgentOps, whether it is a targeted agentic library, and whether it is a known provider. Returns a boolean decision to proceed with or skip instrumentation."
version: "0.1.1"
tags:
  - "package_monitoring"
  - "instrumentation"
  - "conditional_logic"
  - "initialization"
  - "agent_setup"
triggers:
  - "Validation phase"
  - "commit_ts > local rts"
  - "Need to make local version valid at commit_ts"
  - "Delta encoding space is constrained"
examples:
  - input: "commit_ts=5, tuple.wts=1, tuple.rts=4, delta_bits=15"
    output: "rts extended to 5; new TS_word written with wts=1, delta=4"
    notes: "Normal case: delta fits in 15 bits"
  - input: "commit_ts=32768, tuple.wts=1, tuple.rts=32767, delta_bits=15"
    output: "wts increased to 32769 (dummy write), delta reset to 0, rts extended to 32768"
    notes: "Overflow case: delta would exceed 15 bits; wts bumped to recover encoding space"
---

# Read Timestamp Extension with Delta Overflow Handling

Determine whether a software package should be instrumented for monitoring by evaluating three conditions: whether it is already instrumented by AgentOps, whether it is a targeted agentic library, and whether it is a known provider. Returns a boolean decision to proceed with or skip instrumentation.

## Prompt

Check if the package should be instrumented by verifying: (1) if already instrumented by AgentOps, return False and log skip reason; (2) if package is in AGENTIC_LIBRARIES or PROVIDERS, return True; (3) otherwise return False with debug log. Always log the decision rationale.

## Objective

decide_instrumentation_eligibility
## Applicable Signals

- package_name provided
- instrumentation decision required before hook application

## Contraindications

- Do not use if package is already confirmed instrumented by AgentOps
- Do not use if package is not in AGENTIC_LIBRARIES or PROVIDERS lists

## Intervention Moves

- Check _is_package_instrumented(package_name) first; if true, log and return False
- Check if package_name in AGENTIC_LIBRARIES; if true, proceed to provider check
- Check if package_name in PROVIDERS; if true, return True
- If neither agentic nor provider, log default False decision

## Workflow Steps

- {'step': 1, 'action': 'Check if package is already instrumented', 'condition': '_is_package_instrumented(package_name)', 'outcome': 'If true, log skip reason and return False'}
- {'step': 2, 'action': 'Check if package is a targeted agentic library', 'condition': 'package_name in AGENTIC_LIBRARIES', 'outcome': 'Set is_target_agentic flag'}
- {'step': 3, 'action': 'Check if package is a known provider', 'condition': 'package_name in PROVIDERS', 'outcome': 'Set is_target_provider flag'}
- {'step': 4, 'action': 'Evaluate eligibility', 'condition': 'is_target_agentic OR is_target_provider', 'outcome': 'If true, return True; otherwise log default False and return False'}

## Constraints

- AGENTIC_LIBRARIES and PROVIDERS lists must be available and current
- Package name must be a valid string identifier

## Cautions

- Ensure AGENTIC_LIBRARIES and PROVIDERS are synchronized with current package ecosystem
- Log entries should include package name and decision reason for troubleshooting

## Output Contract

- Boolean decision (True to instrument, False to skip) with corresponding debug log entry confirming the decision rationale and the condition that triggered it.

## Triggers

- Validation phase
- commit_ts > local rts
- Need to make local version valid at commit_ts
- Delta encoding space is constrained

## Examples

### Example 1

Input:

  commit_ts=5, tuple.wts=1, tuple.rts=4, delta_bits=15

Output:

  rts extended to 5; new TS_word written with wts=1, delta=4

Notes:

  Normal case: delta fits in 15 bits

### Example 2

Input:

  commit_ts=32768, tuple.wts=1, tuple.rts=32767, delta_bits=15

Output:

  wts increased to 32769 (dummy write), delta reset to 0, rts extended to 32768

Notes:

  Overflow case: delta would exceed 15 bits; wts bumped to recover encoding space
