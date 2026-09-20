---
id: "0e20e2d8-98d7-5f5f-91fb-03614b550217"
name: "Bind Tools to LLM with Callback Tracking"
description: "Attach tool definitions to an LLM instance and ensure each tool has the AgentOps callback handler assigned so that tool invocations are recorded as observable spans during agent execution."
version: "0.1.0"
tags:
  - "agent_instrumentation"
  - "tool_binding"
  - "observability"
  - "callback_tracking"
  - "langchain"
triggers:
  - "Configuring an LLM-based agent that uses external tools"
  - "Before agent execution begins"
  - "When tools need to be bound to an LLM instance"
examples:
  - input: "tools = [find_movie, search_api]; agentops_handler initialized"
    output: "Each tool has t.callbacks = [agentops_handler]; llm_with_tools = llm.bind_tools([find_movie, search_api])"
    notes: "Tool calls will now appear as spans in AgentOps session"
---

# Bind Tools to LLM with Callback Tracking

Attach tool definitions to an LLM instance and ensure each tool has the AgentOps callback handler assigned so that tool invocations are recorded as observable spans during agent execution.

## Prompt

1. Iterate over each tool in your tools list.
2. Assign the agentops_handler callback to each tool's callbacks attribute.
3. Bind the tools to the LLM instance using llm.bind_tools([...]).
4. Verify that the LLM instance now has tools attached and each tool carries the callback handler.
Result: Tool calls will be recorded as spans in the AgentOps session.

## Objective

Enable observability of tool usage within an agent workflow
## Applicable Signals

- Agent workflow includes tool definitions (e.g., @tool decorated functions)
- AgentOps callback handler has been initialized
- LLM instance is ready for tool binding

## Contraindications

- Agent does not use external tools
- Tools are pre-instrumented or managed by a framework that handles callbacks automatically
- Callback handler has not been initialized before tool binding

## Workflow Steps

- {'step': 1, 'action': 'Create or retrieve the AgentOps callback handler instance', 'detail': 'agentops_handler = AgentOpsLangchainCallbackHandler(tags=[...])'}
- {'step': 2, 'action': 'Define tool functions with @tool decorator', 'detail': 'Each tool should have a clear docstring and return type'}
- {'step': 3, 'action': 'Assign callback handler to each tool', 'detail': 'for t in tools: t.callbacks = [agentops_handler]'}
- {'step': 4, 'action': 'Bind tools to LLM instance', 'detail': 'llm_with_tools = llm.bind_tools([tool1, tool2, ...])'}
- {'step': 5, 'action': 'Verify binding and callback attachment', 'detail': 'Confirm LLM instance has tools and each tool carries the handler'}

## Constraints

- AgentOps callback handler must be instantiated before tool assignment
- All tools requiring observability must be included in the iteration
- LLM instance must support bind_tools method

## Cautions

- Ensure callback handler is initialized before assigning to tools
- All tools in the tools list must be processed; missing tools will not be tracked
- Tool callbacks must be set before bind_tools is called for consistent recording

## Output Contract

- Tools are bound to the LLM instance; each tool has the AgentOps callback handler attached; subsequent tool invocations will be recorded as spans in the AgentOps session and visible in the dashboard.

## Example Executions

### Example 1

- Input: tools = [find_movie, search_api]; agentops_handler initialized
- Output: Each tool has t.callbacks = [agentops_handler]; llm_with_tools = llm.bind_tools([find_movie, search_api])
- Notes: Tool calls will now appear as spans in AgentOps session

## Triggers

- Configuring an LLM-based agent that uses external tools
- Before agent execution begins
- When tools need to be bound to an LLM instance

## Examples

### Example 1

Input:

  tools = [find_movie, search_api]; agentops_handler initialized

Output:

  Each tool has t.callbacks = [agentops_handler]; llm_with_tools = llm.bind_tools([find_movie, search_api])

Notes:

  Tool calls will now appear as spans in AgentOps session
