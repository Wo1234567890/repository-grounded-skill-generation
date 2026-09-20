---
id: "5fe5b251-d073-5aa2-b6ae-047528915fd6"
name: "Agent Step Execution and Response Handling"
description: "Execute a single step of agent reasoning with a user query and capture the structured response. Invoke this micro-skill when you need to run one agent reasoning cycle, pass a query string, and retrieve the output for logging or downstream processing."
version: "0.1.0"
tags:
  - "agent"
  - "step_execution"
  - "single_turn"
  - "response_handling"
  - "micro_operation"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Single-turn agent query execution required"
  - "Need to capture agent reasoning output for one interaction cycle"
  - "Logging or inspection of agent response needed"
examples:
  - input: "query_string = \"What is AgentOps?\""
    output: "response object with agent reasoning and answer"
    notes: "Single-step agent invocation with query capture"
---

# Agent Step Execution and Response Handling

Execute a single step of agent reasoning with a user query and capture the structured response. Invoke this micro-skill when you need to run one agent reasoning cycle, pass a query string, and retrieve the output for logging or downstream processing.

## Prompt

Call agent.step(query_string) with your input question or instruction. Capture the returned response object. The response contains the agent's reasoning output and is ready for logging, display, or further processing.

## Objective

Execute one agent step and retrieve response
## Applicable Signals

- User provides a query string to be processed by agent
- Single reasoning step is sufficient for the task
- Response must be captured and made available to caller

## Contraindications

- Multi-turn conversation management required—use session-level workflow instead
- Batch or streaming responses needed
- Continuous agent loop without explicit step boundaries

## Workflow Steps

- {'step': 1, 'action': 'Prepare query string input', 'detail': 'Ensure the query is well-formed and ready for agent processing'}
- {'step': 2, 'action': 'Invoke agent.step(query_string)', 'detail': 'Call the step method with the prepared query'}
- {'step': 3, 'action': 'Capture response object', 'detail': 'Store the returned response for logging or further processing'}

## Constraints

- Input must be a valid query string
- Agent instance must be initialized and ready
- Response object must be structured and serializable for downstream use

## Cautions

- Do not use for multi-turn orchestration; delegate to session-level skill
- Ensure agent is properly initialized before calling step()

## Output Contract

- Returns a structured response object from agent.step() containing reasoning output, ready for logging, display, or handoff to downstream processing.

## Example Executions

### Example 1

- Input: query_string = "What is AgentOps?"
- Output: response object with agent reasoning and answer
- Notes: Single-step agent invocation with query capture

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Single-turn agent query execution required
- Need to capture agent reasoning output for one interaction cycle
- Logging or inspection of agent response needed

## Examples

### Example 1

Input:

  query_string = "What is AgentOps?"

Output:

  response object with agent reasoning and answer

Notes:

  Single-step agent invocation with query capture
