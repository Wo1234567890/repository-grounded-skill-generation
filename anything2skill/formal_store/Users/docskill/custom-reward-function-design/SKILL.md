---
id: "a600fbef-41ac-5267-a405-97b2503d08a6"
name: "Custom Reward Function Design"
description: "Apply the @operation decorator to wrap functions and automatically track their execution, parameters, and return values as spans in session visualization. Use when you need to monitor internal function behavior alongside LLM calls."
version: "0.1.1"
tags:
  - "instrumentation"
  - "debugging"
  - "decorator"
  - "span_tracking"
  - "session_visualization"
  - "function_monitoring"
triggers:
  - "Need to optimize for domain-specific completion quality"
  - "Have clear reward criteria (e.g., length, format, correctness)"
  - "Want to steer model behavior during GRPO training"
examples:
  - input: "Optimize for completions close to 20 characters"
    output: "def reward_len(completions, **kwargs):\n    return [-abs(20 - len(completion)) for completion in completions]"
    notes: "Simple length-based reward; higher scores for completions near target length"
  - input: "Optimize for completions containing specific format (e.g., numbered steps)"
    output: "def reward_format(completions, **kwargs):\n    return [1.0 if '1.' in c and '2.' in c else -1.0 for c in completions]"
    notes: "Binary reward based on format detection; can be extended with graduated scoring"
---

# Custom Reward Function Design

Apply the @operation decorator to wrap functions and automatically track their execution, parameters, and return values as spans in session visualization. Use when you need to monitor internal function behavior alongside LLM calls.

## Prompt

To instrument a function:
1. Import the operation decorator from agentops.sdk.decorators
2. Apply @operation decorator above the function definition
3. The decorated function will automatically create spans capturing execution, parameters, and return values
4. These spans appear in session visualization alongside LLM calls

Example:
from agentops.sdk.decorators import operation

@operation
def process_data(data):
    result = data.upper()
    return result

## Objective

Track function execution and parameters as instrumented spans
## Applicable Signals

- Function is part of agent logic and should be tracked
- Session visualization is active and spans are being collected
- Function is modifiable (not external/third-party)

## Contraindications

- Function is external or third-party code that cannot be modified
- Function is called at very high frequency where span creation overhead is unacceptable
- Span collection is disabled or session visualization is not in use

## Workflow Steps

- Import operation decorator: from agentops.sdk.decorators import operation
- Place @operation decorator immediately above target function definition
- Invoke the decorated function normally; decorator automatically creates span
- Span captures function name, parameters, return value, and execution timing
- Span appears in session visualization alongside other LLM and operation spans

## Constraints

- Function must be accessible and modifiable in source code
- agentops.sdk.decorators module must be available
- Session must be initialized to capture and display spans

## Output Contract

- Function execution appears as a span in session visualization with captured parameters and return value; function behavior and return value are unchanged.

## Triggers

- Need to optimize for domain-specific completion quality
- Have clear reward criteria (e.g., length, format, correctness)
- Want to steer model behavior during GRPO training

## Examples

### Example 1

Input:

  Optimize for completions close to 20 characters

Output:

  def reward_len(completions, **kwargs):
      return [-abs(20 - len(completion)) for completion in completions]

Notes:

  Simple length-based reward; higher scores for completions near target length

### Example 2

Input:

  Optimize for completions containing specific format (e.g., numbered steps)

Output:

  def reward_format(completions, **kwargs):
      return [1.0 if '1.' in c and '2.' in c else -1.0 for c in completions]

Notes:

  Binary reward based on format detection; can be extended with graduated scoring
