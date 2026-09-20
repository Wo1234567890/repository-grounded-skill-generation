---
id: "0aa5626c-5ed7-50e1-87ed-4d879e19901d"
name: "Custom Reward Function Signature Compliance"
description: "Decorate Python functions with @operation to automatically create execution spans that track function calls, parameters, and return values for session visualization."
version: "0.1.1"
tags:
  - "instrumentation"
  - "observability"
  - "tracing"
  - "decorator"
  - "session_visualization"
  - "python"
triggers:
  - "implementing a custom reward function for GRPO trainer"
  - "need to pass dataset-specific metadata to reward computation"
  - "dataset contains columns beyond prompt and completion"
examples:
  - input: "function: process_data(data) that transforms input string to uppercase"
    output: "span created in session visualization showing process_data call with parameter data and return value"
    notes: "decorator requires no modification to function logic"
---

# Custom Reward Function Signature Compliance

Decorate Python functions with @operation to automatically create execution spans that track function calls, parameters, and return values for session visualization.

## Prompt

Apply the @operation decorator from agentops.sdk.decorators to any Python function you want to monitor. The decorator will automatically capture function execution, input parameters, and return values as spans in your session visualization, displayed alongside LLM calls.

## Objective

instrument_function_execution
## Applicable Signals

- custom function defined in agent codebase
- function execution needs to be correlated with LLM calls
- session visualization is active

## Contraindications

- function is already instrumented by another tracing mechanism
- only LLM call monitoring is required without custom function tracking
- function is part of a third-party library with its own instrumentation

## Workflow Steps

- import operation decorator from agentops.sdk.decorators
- apply @operation decorator to target function definition
- function executes normally with decorator active
- span is automatically created and added to session visualization

## Constraints

- function must be defined in user code (not external library)
- agentops SDK must be initialized in the session
- decorator must be imported from agentops.sdk.decorators

## Cautions

- decorator adds minimal overhead but may impact performance on very high-frequency function calls
- return values are captured; ensure sensitive data is not logged

## Output Contract

- decorated function executes normally and produces a span visible in session visualization with function name, parameters, and return value

## Example Executions

### Example 1

- Input: function: process_data(data) that transforms input string to uppercase
- Output: span created in session visualization showing process_data call with parameter data and return value
- Notes: decorator requires no modification to function logic

## Triggers

- implementing a custom reward function for GRPO trainer
- need to pass dataset-specific metadata to reward computation
- dataset contains columns beyond prompt and completion

## Examples

### Example 1

Input:

  function: process_data(data) that transforms input string to uppercase

Output:

  span created in session visualization showing process_data call with parameter data and return value

Notes:

  decorator requires no modification to function logic
