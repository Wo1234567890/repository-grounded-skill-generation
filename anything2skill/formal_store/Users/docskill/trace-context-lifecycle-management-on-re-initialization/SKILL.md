---
id: "81c0b3ee-2927-545f-83ea-7faba8b3dc1d"
name: "Trace Context Lifecycle Management on Re-initialization"
description: "Detects active trace recording and cleanly ends the trace context when Client is re-initialized with a different API key. Logs warnings and resets trace state to prevent orphaned spans."
version: "0.1.0"
tags:
  - "trace_management"
  - "re_initialization"
  - "span_lifecycle"
  - "cleanup"
  - "state_reset"
triggers:
  - "Client re-initialization initiated with a different API key"
  - "_init_trace_context is not None"
  - "trace span is actively recording"
---

# Trace Context Lifecycle Management on Re-initialization

Detects active trace recording and cleanly ends the trace context when Client is re-initialized with a different API key. Logs warnings and resets trace state to prevent orphaned spans.

## Prompt

When Client re-initialization is triggered with a different API key, check if _init_trace_context exists and its span is actively recording. If so, end the trace with reason 'Reinitialized', log a warning, and reset _init_trace_context to None. This prevents trace corruption and orphaned spans.

## Objective

Clean up active trace spans before re-initialization to avoid trace corruption
## Applicable Signals

- provided_api_key differs from self.config.api_key
- self._init_trace_context exists
- self._init_trace_context.span.is_recording() returns True

## Contraindications

- API key has not changed
- trace context is None
- span is not recording
- trace cleanup is managed externally

## Intervention Moves

- Detect API key change and log warning
- Verify trace span is actively recording before cleanup
- End trace with explicit reason code
- Reset trace state variables to prevent stale references

## Workflow Steps

- {'step': 1, 'action': 'Check if provided_api_key differs from self.config.api_key', 'condition': 'provided_api_key is not None and provided_api_key != self.config.api_key'}
- {'step': 2, 'action': "Log warning: 'AgentOps Client being re-initialized with a different API key. This is unusual.'", 'condition': 'API key change detected'}
- {'step': 3, 'action': 'Check if _init_trace_context exists and span is recording', 'condition': 'self._init_trace_context is not None and self._init_trace_context.span.is_recording()'}
- {'step': 4, 'action': "Log warning: 'Ending previously auto-started trace due to re-initialization.'", 'condition': 'Trace context is active and recording'}
- {'step': 5, 'action': "Call tracer.end_trace(self._init_trace_context, 'Reinitialized')", 'condition': 'Trace span is actively recording'}
- {'step': 6, 'action': 'Set self._init_trace_context = None', 'condition': 'After trace has been ended'}
- {'step': 7, 'action': 'Set self._legacy_session_for_init_trace = None', 'condition': 'After trace context reset'}

## Constraints

- Must check API key change before attempting trace cleanup
- Must verify span is recording before calling end_trace
- Must reset _init_trace_context to None after ending trace

## Cautions

- Calling end_trace on a non-recording span may raise an exception
- Failure to reset _init_trace_context may cause subsequent initialization to reference stale trace state

## Output Contract

- Active trace span is ended with reason 'Reinitialized'; _init_trace_context is set to None; _legacy_session_for_init_trace is set to None; warning logs are emitted; subsequent initialization can proceed without trace conflicts.

## Triggers

- Client re-initialization initiated with a different API key
- _init_trace_context is not None
- trace span is actively recording
