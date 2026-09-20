---
id: "953561f7-cefc-5e57-9e3d-dd51ab122f49"
name: "Validate Buffer Timeout Configuration"
description: "Safety rule preventing buffer timeout misconfiguration in Flink DataStream execution. Enforces that buffer timeout values are never set to 0, which causes severe performance degradation. Guides selection between -1 (maximum throughput) or small positive values (5–10 ms for low-latency mode)."
version: "0.1.0"
tags:
  - "buffer_timeout"
  - "latency_control"
  - "throughput_tuning"
  - "performance_trap"
  - "flink_datastream"
  - "execution_configuration"
triggers:
  - "Before applying setBufferTimeout() call"
  - "During execution environment or operator configuration"
  - "When tuning latency or throughput trade-offs"
examples:
  - input: "setBufferTimeout(0)"
    output: "Rejected; replaced with setBufferTimeout(10) for low-latency use case"
    notes: "Zero timeout triggers safety rule; caller must choose throughput (-1) or latency (5–10 ms) goal"
  - input: "setBufferTimeout(-1)"
    output: "Accepted; maximum throughput mode enabled"
    notes: "Buffers flush only when full; suitable for batch-like or high-throughput scenarios"
  - input: "setBufferTimeout(5)"
    output: "Accepted; low-latency mode enabled"
    notes: "Buffers flush every 5 ms; suitable for real-time or interactive use cases"
---

# Validate Buffer Timeout Configuration

Safety rule preventing buffer timeout misconfiguration in Flink DataStream execution. Enforces that buffer timeout values are never set to 0, which causes severe performance degradation. Guides selection between -1 (maximum throughput) or small positive values (5–10 ms for low-latency mode).

## Prompt

Before calling setBufferTimeout(), validate the timeout value. Reject 0 immediately. If maximizing throughput is the goal, use -1. If minimizing latency is the goal, use a small positive value such as 5 or 10 ms. Document the choice and rationale.

## Objective

prevent_performance_degradation
## Applicable Signals

- setBufferTimeout() invocation pending
- buffer timeout parameter under review
- latency or throughput optimization in progress

## Contraindications

- Not applicable when buffer timeout tuning is not required
- Do not override this rule for experimental or one-off tests without explicit risk acceptance

## Intervention Moves

- Detect timeout value = 0
- Reject or replace with safe alternative
- Log the correction and rationale
- Proceed with validated timeout value

## Workflow Steps

- Intercept setBufferTimeout() invocation with proposed timeout value
- Validate that value is not equal to 0
- If value is 0, reject and prompt for alternative
- If value is -1, accept and confirm maximum throughput mode
- If value is positive integer ≥ 5 ms, accept and confirm low-latency mode
- Log validation result and proceed with execution

## Constraints

- Buffer timeout value must be validated before execution
- Zero (0) is strictly forbidden
- Allowed values: -1 (no timeout, flush only when full) or positive integers ≥ 5 ms

## Cautions

- A buffer timeout of 0 causes severe performance degradation and should never be used
- Trade-off: -1 maximizes throughput but increases latency; small positive values (5–10 ms) minimize latency at the cost of throughput

## Output Contract

- Buffer timeout value is validated and confirmed to be either -1 or a positive integer ≥ 5 ms. Zero values are rejected or replaced. Execution proceeds with safe timeout configuration.

## Example Executions

### Example 1

- Input: setBufferTimeout(0)
- Output: Rejected; replaced with setBufferTimeout(10) for low-latency use case
- Notes: Zero timeout triggers safety rule; caller must choose throughput (-1) or latency (5–10 ms) goal

### Example 2

- Input: setBufferTimeout(-1)
- Output: Accepted; maximum throughput mode enabled
- Notes: Buffers flush only when full; suitable for batch-like or high-throughput scenarios

### Example 3

- Input: setBufferTimeout(5)
- Output: Accepted; low-latency mode enabled
- Notes: Buffers flush every 5 ms; suitable for real-time or interactive use cases

## Triggers

- Before applying setBufferTimeout() call
- During execution environment or operator configuration
- When tuning latency or throughput trade-offs

## Examples

### Example 1

Input:

  setBufferTimeout(0)

Output:

  Rejected; replaced with setBufferTimeout(10) for low-latency use case

Notes:

  Zero timeout triggers safety rule; caller must choose throughput (-1) or latency (5–10 ms) goal

### Example 2

Input:

  setBufferTimeout(-1)

Output:

  Accepted; maximum throughput mode enabled

Notes:

  Buffers flush only when full; suitable for batch-like or high-throughput scenarios

### Example 3

Input:

  setBufferTimeout(5)

Output:

  Accepted; low-latency mode enabled

Notes:

  Buffers flush every 5 ms; suitable for real-time or interactive use cases
