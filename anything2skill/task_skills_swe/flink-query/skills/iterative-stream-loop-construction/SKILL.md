---
id: "568447d8-71c4-552c-b75e-25889b5a1fdf"
name: "Iterative Stream Loop Construction"
description: "Group a sequence of agent operations or define logical units of work using the @trace decorator or manual trace management. Use when you need to organize related operations into traceable logical blocks for debugging and monitoring."
version: "0.1.1"
tags:
  - "tracing"
  - "operation_grouping"
  - "debugging"
  - "monitoring"
  - "agent_instrumentation"
  - "decorator_pattern"
triggers:
  - "Need to apply repeated transformations until convergence"
  - "Implement recursive or feedback-based stream logic"
  - "Process elements through multiple passes with state carried between iterations"
examples:
  - input: "DataStream<Long> of integers 0–1000"
    output: "DataStream<Long> containing only integers ≤ 0 after repeated decrement"
    notes: "Subtract 1 from each element in a loop until value ≤ 0; feedback branch filters value > 0, output branch filters value ≤ 0."
---

# Iterative Stream Loop Construction

Group a sequence of agent operations or define logical units of work using the @trace decorator or manual trace management. Use when you need to organize related operations into traceable logical blocks for debugging and monitoring.

## Prompt

To group operations into a trace:
1. Import the trace decorator: from agentops.sdk.decorators import trace
2. Either apply @trace decorator to a function/method, or call agentops.start_trace() manually for complex scenarios.
3. Ensure that if auto_start_session=False in agentops.init(), you use @trace or agentops.start_trace() so data is recorded.
4. Operations within the trace will be grouped together with clear logical boundaries.

## Objective

Organize and record grouped operations within an agent session
## Applicable Signals

- Multiple related operations that form a logical work unit
- Session initialized with auto_start_session=False
- Debugging or monitoring requirements for operation sequences

## Contraindications

- Recording individual atomic operations that do not form a logical group
- Session auto-start is enabled and no custom grouping is needed
- Operations are already implicitly grouped by the framework

## Workflow Steps

- Import trace decorator from agentops.sdk.decorators
- Apply @trace decorator to function or call agentops.start_trace() manually
- Execute operations within the decorated function or trace context
- Verify grouped operations are recorded with clear logical boundaries

## Constraints

- If auto_start_session=False, @trace or agentops.start_trace() must be used for any data to be recorded
- Trace decorator or manual trace calls must be applied before operations execute

## Cautions

- Without @trace or manual trace management when auto_start_session=False, no data will be captured
- Ensure trace boundaries align with logical work units for effective debugging

## Output Contract

- Grouped operations recorded in trace with clear logical boundaries and execution sequence captured for downstream debugging and monitoring

## Triggers

- Need to apply repeated transformations until convergence
- Implement recursive or feedback-based stream logic
- Process elements through multiple passes with state carried between iterations

## Examples

### Example 1

Input:

  DataStream<Long> of integers 0–1000

Output:

  DataStream<Long> containing only integers ≤ 0 after repeated decrement

Notes:

  Subtract 1 from each element in a loop until value ≤ 0; feedback branch filters value > 0, output branch filters value ≤ 0.
