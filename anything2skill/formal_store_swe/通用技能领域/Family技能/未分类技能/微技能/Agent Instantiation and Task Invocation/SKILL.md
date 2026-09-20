---
id: "c88710bc-82ee-5768-8451-985dc318299f"
name: "Agent Instantiation and Task Invocation"
description: "Creates a named agent instance and executes a single synchronous task method on it. Reusable pattern for spawning and executing agent operations within an active session context."
version: "0.1.0"
tags:
  - "agent"
  - "instantiation"
  - "task_execution"
  - "session_pattern"
  - "micro_operation"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Need to create a new agent instance within an active session"
  - "Ready to immediately invoke a task on the agent"
  - "Agent class is available and task method is defined"
examples:
  - input: "Agent class MyAgent with perform_task method; task description 'data analysis'"
    output: "Agent instance created with name 'research-agent'; task executed; result string returned"
    notes: "Synchronous execution within session context"
---

# Agent Instantiation and Task Invocation

Creates a named agent instance and executes a single synchronous task method on it. Reusable pattern for spawning and executing agent operations within an active session context.

## Prompt

Instantiate a named agent and execute a single task by calling the agent's task method. Pass the task description as an argument and capture the result for downstream use.

## Objective

Instantiate a named agent and execute a single task
## Applicable Signals

- Session context is active
- Agent class constructor accepts a name parameter
- Task method exists and accepts task description argument

## Contraindications

- Agent is already instantiated; reuse existing instance instead
- Task is asynchronous or requires pre-configuration before invocation
- Agent initialization requires complex setup or dependencies

## Workflow Steps

- Instantiate agent with name identifier: agent = AgentClass(name)
- Invoke task method with task description: result = agent.perform_task(task_description)
- Capture and return result for downstream handoff

## Constraints

- Agent must be instantiated before task invocation
- Task method must be synchronous and return a result
- Agent name must be a valid string identifier

## Cautions

- Ensure agent class is imported and available in scope
- Verify task method signature matches expected parameters
- Handle exceptions from task execution appropriately

## Output Contract

- Agent instance created and stored; task method executed; result object returned and available for caller handoff or further processing

## Example Executions

### Example 1

- Input: Agent class MyAgent with perform_task method; task description 'data analysis'
- Output: Agent instance created with name 'research-agent'; task executed; result string returned
- Notes: Synchronous execution within session context

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Need to create a new agent instance within an active session
- Ready to immediately invoke a task on the agent
- Agent class is available and task method is defined

## Examples

### Example 1

Input:

  Agent class MyAgent with perform_task method; task description 'data analysis'

Output:

  Agent instance created with name 'research-agent'; task executed; result string returned

Notes:

  Synchronous execution within session context
