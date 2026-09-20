---
id: "c204c15c-15eb-5cb6-a367-0177d593379a"
name: "Trace Context Cleanup on Re-initialization"
description: "Ends any active trace recording and clears trace context when Client is re-initialized with a different API key, preventing orphaned or misattributed traces."
version: "0.1.0"
tags:
  - "trace_cleanup"
  - "re-initialization"
  - "state_management"
  - "api_key_rotation"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Client re-initialization detected with a different API key"
  - "_init_trace_context is not None"
  - "_init_trace_context.span.is_recording() returns True"
---

# Trace Context Cleanup on Re-initialization

Ends any active trace recording and clears trace context when Client is re-initialized with a different API key, preventing orphaned or misattributed traces.

## Prompt

When the Client detects re-initialization with a different API key and an active trace context exists, end the trace with reason 'Reinitialized' and clear both _init_trace_context and _legacy_session_for_init_trace to None.

## Objective

Clean up active trace state during Client re-initialization
## Applicable Signals

- provided_api_key differs from self.config.api_key
- self.initialized is True
- Active trace span in recording state

## Contraindications

- Trace context is None
- Trace span is not recording
- Client is not being re-initialized

## Workflow Steps

- {'step': 1, 'action': 'Check if _init_trace_context is not None and span is recording', 'condition': 'self._init_trace_context and self._init_trace_context.span.is_recording()'}
- {'step': 2, 'action': 'Log warning about ending previously auto-started trace', 'condition': 'Always log before cleanup'}
- {'step': 3, 'action': "Call tracer.end_trace() with context and 'Reinitialized' reason", 'condition': 'Trace is active'}
- {'step': 4, 'action': 'Set _init_trace_context to None', 'condition': 'After trace end'}
- {'step': 5, 'action': 'Set _legacy_session_for_init_trace to None', 'condition': 'After trace end'}

## Constraints

- Only execute when re-initialization with a different API key is confirmed
- Verify trace context exists and is actively recording before calling tracer.end_trace()

## Cautions

- Ending a trace prematurely may lose recorded events; ensure re-initialization intent is genuine
- Log warning before cleanup to alert operators of trace interruption

## Output Contract

- Active trace is ended with 'Reinitialized' reason
- _init_trace_context is set to None
- _legacy_session_for_init_trace is set to None
- No further trace recording occurs under the old context

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Client re-initialization detected with a different API key
- _init_trace_context is not None
- _init_trace_context.span.is_recording() returns True
