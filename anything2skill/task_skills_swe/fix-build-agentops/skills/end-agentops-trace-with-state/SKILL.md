---
id: "930546b9-f828-59cf-b183-e43318fe6e54"
name: "End AgentOps Trace with State"
description: "Explicitly close an AgentOps trace session by calling end_trace() with a final state (e.g., 'Success', 'Failure'). This marks the session boundary and finalizes recording of all spans and events."
version: "0.1.0"
tags:
  - "agentops"
  - "instrumentation"
  - "session_management"
  - "trace_closure"
  - "finalization"
triggers:
  - "Agent execution completes successfully"
  - "Agent execution encounters a terminal error"
  - "Workflow reaches a defined exit point"
examples:
  - input: "Agent execution completed successfully; tracer object available"
    output: "agentops.end_trace(tracer, end_state='Success') called; session closed and spans flushed to dashboard"
    notes: "Standard success case after agent workflow finishes"
  - input: "Agent execution encountered an error; tracer object available"
    output: "agentops.end_trace(tracer, end_state='Failure') called; session closed with error state recorded"
    notes: "Error handling case; state reflects failure condition"
---

# End AgentOps Trace with State

Explicitly close an AgentOps trace session by calling end_trace() with a final state (e.g., 'Success', 'Failure'). This marks the session boundary and finalizes recording of all spans and events.

## Prompt

Call agentops.end_trace(tracer, end_state=<state>) where <state> is 'Success', 'Failure', or another terminal state string. This flushes all recorded spans and events to the AgentOps dashboard and closes the session.

## Objective

Finalize and mark completion of an AgentOps instrumented session
## Applicable Signals

- Agent task finished
- Final result available
- Error state reached

## Contraindications

- Session already closed via prior end_trace() call
- Using auto-closing context manager that handles trace closure implicitly
- Trace session not yet initialized

## Workflow Steps

- {'step': 1, 'action': 'Verify agent execution has completed and final state is determined', 'condition': 'Agent task finished or error encountered'}
- {'step': 2, 'action': 'Call agentops.end_trace(tracer, end_state=<state>)', 'condition': 'Tracer object is valid and session is open'}
- {'step': 3, 'action': 'Confirm session closure and span persistence', 'condition': 'end_trace() returns without exception'}

## Constraints

- Must be called after agent execution logic completes
- Must be called before exiting the agent workflow
- Requires valid tracer object from session initialization
- end_state parameter must be a string (e.g., 'Success', 'Failure')

## Cautions

- Calling end_trace() twice on the same session may cause errors; check session state first if uncertain
- If end_trace() is not called, spans may not be flushed to the dashboard

## Output Contract

- Trace session closed with final state recorded in AgentOps
- All spans and events persisted to dashboard
- Session no longer accepts new events

## Example Executions

### Example 1

- Input: Agent execution completed successfully; tracer object available
- Output: agentops.end_trace(tracer, end_state='Success') called; session closed and spans flushed to dashboard
- Notes: Standard success case after agent workflow finishes

### Example 2

- Input: Agent execution encountered an error; tracer object available
- Output: agentops.end_trace(tracer, end_state='Failure') called; session closed with error state recorded
- Notes: Error handling case; state reflects failure condition

## Triggers

- Agent execution completes successfully
- Agent execution encounters a terminal error
- Workflow reaches a defined exit point

## Examples

### Example 1

Input:

  Agent execution completed successfully; tracer object available

Output:

  agentops.end_trace(tracer, end_state='Success') called; session closed and spans flushed to dashboard

Notes:

  Standard success case after agent workflow finishes

### Example 2

Input:

  Agent execution encountered an error; tracer object available

Output:

  agentops.end_trace(tracer, end_state='Failure') called; session closed with error state recorded

Notes:

  Error handling case; state reflects failure condition
