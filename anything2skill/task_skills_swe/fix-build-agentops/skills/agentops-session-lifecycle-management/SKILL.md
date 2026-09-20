---
id: "a7c386e7-6b98-5ac6-8fbe-c7d3468b741d"
name: "AgentOps Session Lifecycle Management"
description: "Initialize and terminate an AgentOps observability session, wrapping agent or LLM interactions for end-to-end tracking and debugging."
version: "0.1.0"
tags:
  - "observability"
  - "session_management"
  - "debugging"
  - "audit_trail"
  - "agent_tracking"
triggers:
  - "starting an agent or multi-step LLM workflow that requires end-to-end observability, debugging logs, or audit trail"
examples:
  - input: "Start a workflow that calls an LLM multiple times and needs full observability."
    output: "Session initialized, all LLM calls tracked, session ended with 'Success' status, logs available."
    notes: "Typical use case for multi-turn agent interactions."
---

# AgentOps Session Lifecycle Management

Initialize and terminate an AgentOps observability session, wrapping agent or LLM interactions for end-to-end tracking and debugging.

## Prompt

Use this skill to set up and tear down an AgentOps observability session around your agent or multi-step LLM workflow. Call agentops.init() at the start of your session and agentops.end_session(status) at the end. This ensures all interactions are tracked, logged, and available for debugging.

## Objective

manage_observability_session
## Applicable Signals

- starting an agent or multi-step LLM workflow
- requirement for end-to-end observability
- need for debugging logs or audit trail
- multi-turn interaction requiring session state

## Contraindications

- no observability requirement
- local development without logging needs
- real-time streaming-only use case without session state
- single isolated LLM call without workflow context

## Workflow Steps

- {'step': 1, 'action': 'Initialize AgentOps session', 'detail': 'Call agentops.init() at the beginning of your workflow to start session tracking.'}
- {'step': 2, 'action': 'Execute agent or LLM interactions', 'detail': 'Run your agent logic, LLM calls, or multi-step workflow within the active session.'}
- {'step': 3, 'action': 'Terminate session with status', 'detail': "Call agentops.end_session(status) at the end, passing a status string such as 'Success' or 'Failure'."}

## Constraints

- Session must be initialized before any tracked interactions
- Session must be terminated to finalize logs and traces
- Status parameter is required at session end

## Cautions

- Ensure end_session() is called even if errors occur; consider using try-finally pattern
- Session state is lost if end_session() is not called
- Multiple concurrent sessions may require separate initialization and teardown

## Output Contract

- AgentOps session initialized at start; session terminated with provided status; logs and traces available for review and debugging.

## Example Executions

### Example 1

- Input: Start a workflow that calls an LLM multiple times and needs full observability.
- Output: Session initialized, all LLM calls tracked, session ended with 'Success' status, logs available.
- Notes: Typical use case for multi-turn agent interactions.

## Triggers

- starting an agent or multi-step LLM workflow that requires end-to-end observability, debugging logs, or audit trail

## Examples

### Example 1

Input:

  Start a workflow that calls an LLM multiple times and needs full observability.

Output:

  Session initialized, all LLM calls tracked, session ended with 'Success' status, logs available.

Notes:

  Typical use case for multi-turn agent interactions.
