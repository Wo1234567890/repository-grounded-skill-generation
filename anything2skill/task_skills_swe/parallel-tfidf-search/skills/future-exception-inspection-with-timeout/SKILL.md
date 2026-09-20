---
id: "0745223a-841f-51d6-8381-727206ff716f"
name: "Future Exception Inspection with Timeout"
description: "Decorator-based pattern to define a reusable tool with name and cost attributes, enabling cost tracking and tool discovery in agent workflows."
version: "0.1.1"
tags:
  - "agent_tools"
  - "decorator_pattern"
  - "cost_tracking"
  - "tool_registration"
triggers:
  - "A parallel task has completed and the caller needs to examine what exception (if any) was raised, without propagating it immediately."
examples:
  - input: "Function: advanced_web_search(query: str) -> str; name='AdvancedSearch'; cost=0.02"
    output: "Decorated function registered as discoverable tool with cost metadata; callable as agent.advanced_web_search('topic')"
    notes: "Cost value 0.02 enables per-call billing; name enables tool discovery in agent routing"
---

# Future Exception Inspection with Timeout

Decorator-based pattern to define a reusable tool with name and cost attributes, enabling cost tracking and tool discovery in agent workflows.

## Prompt

Use the @tool decorator to register a callable function as a discoverable agent tool. Provide a name parameter for tool identification and a cost parameter for execution cost tracking. The decorated function becomes callable by agent instances and exposes metadata for routing and billing.

## Objective

Register a callable tool with metadata for agent invocation
## Applicable Signals

- Agent workflow requires external tool integration
- Cost accounting or billing per tool execution is required
- Multiple agents need access to the same tool

## Contraindications

- Tool is one-off or internal-only without reuse intent
- No cost tracking or billing requirement
- Tool does not need to be discoverable by agents

## Workflow Steps

- Define a Python function with the desired tool logic
- Apply @tool decorator with name and cost keyword arguments
- Ensure function signature and return type are clear for agent invocation
- Verify decorated function is accessible to agent class instances

## Constraints

- Function must be decorated before agent instantiation
- Name parameter must be unique within the tool registry
- Cost parameter must be a numeric value (float or int)

## Output Contract

- Tool function decorated with @tool, callable by agent instances with name and cost attributes accessible via metadata

## Example Executions

### Example 1

- Input: Function: advanced_web_search(query: str) -> str; name='AdvancedSearch'; cost=0.02
- Output: Decorated function registered as discoverable tool with cost metadata; callable as agent.advanced_web_search('topic')
- Notes: Cost value 0.02 enables per-call billing; name enables tool discovery in agent routing

## Triggers

- A parallel task has completed and the caller needs to examine what exception (if any) was raised, without propagating it immediately.

## Examples

### Example 1

Input:

  Function: advanced_web_search(query: str) -> str; name='AdvancedSearch'; cost=0.02

Output:

  Decorated function registered as discoverable tool with cost metadata; callable as agent.advanced_web_search('topic')

Notes:

  Cost value 0.02 enables per-call billing; name enables tool discovery in agent routing
