---
id: "03e5c804-cb85-5bec-acea-42783de9c0c8"
name: "Buffer Timeout Configuration for Latency Control"
description: "Configure buffer timeout on StreamExecutionEnvironment or individual operators to balance throughput and latency. Use setBufferTimeout() to control when data is flushed from buffers."
version: "0.1.0"
tags:
  - "buffer_management"
  - "latency_control"
  - "throughput_optimization"
  - "stream_execution"
  - "runtime_tuning"
triggers:
  - "latency requirements are critical or throughput optimization is needed; operator-level tuning is preferred over global settings for fine-grained control"
examples:
  - input: "Requirement: maximize throughput"
    output: "env.setBufferTimeout(-1)"
    notes: "Buffers flush only when full; highest throughput, higher latency"
  - input: "Requirement: minimize latency"
    output: "env.setBufferTimeout(10)"
    notes: "Buffers flush every 10 ms; lower latency, reduced throughput"
  - input: "Requirement: operator-level tuning for specific stage"
    output: "env.generateSequence(1, 10).map(myMap).setBufferTimeout(5)"
    notes: "Fine-grained control on individual operator; does not affect other operators"
---

# Buffer Timeout Configuration for Latency Control

Configure buffer timeout on StreamExecutionEnvironment or individual operators to balance throughput and latency. Use setBufferTimeout() to control when data is flushed from buffers.

## Prompt

Call setBufferTimeout(timeoutMillis) on the StreamExecutionEnvironment or on individual operators. For maximum throughput, use -1 (buffers flush only when full). For minimum latency, use a small positive value (5–10 ms). Never use 0, as it causes severe performance degradation.

## Objective

optimize_latency_throughput_tradeoff
## Applicable Signals

- latency requirements are critical
- throughput optimization is needed
- operator-level tuning is preferred over global settings for fine-grained control

## Contraindications

- Do not set buffer timeout to 0 (causes severe performance degradation)
- Do not apply uniformly without understanding downstream impact on latency and throughput

## Intervention Moves

- Call env.setBufferTimeout(timeoutMillis) on StreamExecutionEnvironment
- Call .setBufferTimeout(timeoutMillis) on individual operators for targeted control
- Set timeout to -1 for maximum throughput
- Set timeout to 5–10 ms for minimum latency

## Workflow Steps

- Determine latency vs. throughput priority for the job
- Choose timeout value: -1 for throughput, 5–10 ms for latency
- Apply setBufferTimeout() to environment or target operators
- Verify latency/throughput tradeoff is achieved as intended

## Constraints

- Buffer timeout value must be -1 or a positive integer (milliseconds)
- Timeout of 0 is explicitly forbidden

## Cautions

- Setting timeout to 0 causes severe performance degradation; avoid entirely
- Global environment-level timeout affects all operators; operator-level overrides provide finer control

## Output Contract

- Buffer timeout value is applied to environment or operator; latency and throughput behavior reflects the configured timeout setting.

## Example Therapist Responses

### Example 1

- Client/Input: Requirement: maximize throughput
- Therapist/Output: env.setBufferTimeout(-1)
- Notes: Buffers flush only when full; highest throughput, higher latency

### Example 2

- Client/Input: Requirement: minimize latency
- Therapist/Output: env.setBufferTimeout(10)
- Notes: Buffers flush every 10 ms; lower latency, reduced throughput

### Example 3

- Client/Input: Requirement: operator-level tuning for specific stage
- Therapist/Output: env.generateSequence(1, 10).map(myMap).setBufferTimeout(5)
- Notes: Fine-grained control on individual operator; does not affect other operators

## Triggers

- latency requirements are critical or throughput optimization is needed; operator-level tuning is preferred over global settings for fine-grained control

## Examples

### Example 1

Input:

  Requirement: maximize throughput

Output:

  env.setBufferTimeout(-1)

Notes:

  Buffers flush only when full; highest throughput, higher latency

### Example 2

Input:

  Requirement: minimize latency

Output:

  env.setBufferTimeout(10)

Notes:

  Buffers flush every 10 ms; lower latency, reduced throughput

### Example 3

Input:

  Requirement: operator-level tuning for specific stage

Output:

  env.generateSequence(1, 10).map(myMap).setBufferTimeout(5)

Notes:

  Fine-grained control on individual operator; does not affect other operators
