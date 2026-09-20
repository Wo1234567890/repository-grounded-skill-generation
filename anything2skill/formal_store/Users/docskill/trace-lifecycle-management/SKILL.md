---
id: "2088b931-a182-5233-b4ad-880545601196"
name: "Trace Lifecycle Management"
description: "Initialize, finalize, and update metadata for execution traces in agent debugging workflows. Manages trace context, state transitions, and metadata enrichment across the complete trace lifecycle."
version: "0.1.0"
tags:
  - "trace_management"
  - "agent_debugging"
  - "instrumentation"
  - "session_lifecycle"
triggers:
  - "Agent execution begins and requires trace initialization"
  - "Metadata needs to be attached to a running trace"
  - "Trace state must be finalized at agent execution end"
---

# Trace Lifecycle Management

Initialize, finalize, and update metadata for execution traces in agent debugging workflows. Manages trace context, state transitions, and metadata enrichment across the complete trace lifecycle.

## Prompt

Use this skill to manage the full lifecycle of a trace session: (1) start a new trace with optional name and tags, (2) update metadata on the running trace as needed, (3) end the trace with a final state. Ensure trace_context is provided when available to target the correct session; if omitted, operations affect all active spans.

## Objective

Establish and close bounded trace sessions with proper state and metadata tracking
## Applicable Signals

- session_start
- metadata_enrichment_required
- session_end

## Contraindications

- Trace context is already closed
- No active session exists
- Metadata update is not required for the current operation

## Workflow Steps

- {'step': 1, 'action': 'start_trace', 'description': 'Initialize a new trace with optional trace_name and tags', 'input': 'trace_name (str, optional), tags (list, optional)', 'output': 'TraceContext object'}
- {'step': 2, 'action': 'update_trace_metadata', 'description': 'Enrich the running trace with metadata key-value pairs', 'input': "metadata (Dict[str, Any]), prefix (str, default='trace.metadata')", 'output': 'bool (success indicator)'}
- {'step': 3, 'action': 'end_trace', 'description': 'Finalize the trace and record its end state', 'input': 'trace_context (TraceContext, optional), end_state (TraceState|StatusCode|str, default=TraceState.SUCCESS)', 'output': 'None (trace finalized)'}

## Constraints

- trace_context must be valid or None (to target all active spans)
- end_state must be a valid TraceState, StatusCode, or string
- metadata dict must be serializable

## Cautions

- If trace_context is not provided to end_trace, all active spans will be terminated
- Metadata updates must occur while the trace is active; updates after end_trace will fail

## Output Contract

- On start_trace: returns a TraceContext object for downstream reference. On update_trace_metadata: returns boolean indicating success. On end_trace: trace is finalized with the specified end_state recorded; if trace_context is None, all active session spans are ended.

## Triggers

- Agent execution begins and requires trace initialization
- Metadata needs to be attached to a running trace
- Trace state must be finalized at agent execution end
