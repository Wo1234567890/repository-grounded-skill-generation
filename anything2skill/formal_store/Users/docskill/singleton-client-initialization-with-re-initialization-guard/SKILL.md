---
id: "048797be-e3b0-5c18-81d2-f1ef6e933f06"
name: "Singleton Client Initialization with Re-initialization Guard"
description: "Enforces single-instance Client lifecycle per process. Detects and safely handles re-initialization attempts with different API keys by resetting state and ending active traces. Manages trace context lifecycle across initialization cycles."
version: "0.1.0"
tags:
  - "singleton"
  - "initialization"
  - "lifecycle_management"
  - "state_reset"
  - "trace_context"
  - "api_key_validation"
triggers:
  - "Client instantiation or __init__ call"
  - "Re-initialization attempt with different API key detected"
  - "Trace context lifecycle boundary crossed"
---

# Singleton Client Initialization with Re-initialization Guard

Enforces single-instance Client lifecycle per process. Detects and safely handles re-initialization attempts with different API keys by resetting state and ending active traces. Manages trace context lifecycle across initialization cycles.

## Prompt

When instantiating or re-initializing the Client:
1. Check if __instance exists; if not, create it and initialize trace context holders (_init_trace_context and _legacy_session_for_init_trace) to None.
2. In __init__, verify _initialized flag; if not set, initialize config and set _initialized to False.
3. Detect if a different non-None API key is provided while already initialized; if so, log warning, end any active trace with reason 'Reinitialized', reset _initialized and trace context holders.
4. If already initialized and auto_start_session is true, return the existing legacy session wrapper; otherwise return None.
5. If no API key is configured, raise NoApiKeyException.
6. Return the single Client instance.

## Objective

Enforce single-instance client lifecycle and safe re-initialization with trace context management
## Applicable Signals

- cls.__instance is None (first instantiation)
- provided_api_key differs from self.config.api_key and self.initialized is True
- self._init_trace_context exists and span.is_recording() returns True

## Contraindications

- Multi-instance clients are intentionally required
- API key rotation is not a concern
- Trace context lifecycle is managed externally

## Intervention Moves

- Log warning when re-initialization with different API key is detected
- End active trace context before state reset
- Reset _initialized flag to False to allow re-initialization
- Clear trace context holders to prevent stale references

## Workflow Steps

- {'step': 1, 'action': 'Check singleton instance in __new__', 'detail': 'If cls.__instance is None, create new instance and initialize _init_trace_context and _legacy_session_for_init_trace to None'}
- {'step': 2, 'action': 'Initialize config in __init__', 'detail': 'If _initialized is not set or False, create Config() and set _initialized to False'}
- {'step': 3, 'action': 'Detect re-initialization with different API key', 'detail': 'Extract provided_api_key from kwargs; if self.initialized is True and provided_api_key is not None and differs from self.config.api_key, log warning'}
- {'step': 4, 'action': 'Reset state on key change', 'detail': "Set _initialized to False; if _init_trace_context exists and span.is_recording(), call tracer.end_trace() with reason 'Reinitialized'; set _init_trace_context and _legacy_session_for_init_trace to None"}
- {'step': 5, 'action': 'Return or skip initialization if already initialized', 'detail': 'If self.initialized is True, log debug message; if auto_start_session is True, return _legacy_session_for_init_trace; otherwise return None'}
- {'step': 6, 'action': 'Validate API key', 'detail': 'If self.config.api_key is not set, raise NoApiKeyException'}
- {'step': 7, 'action': 'Return Client instance', 'detail': 'Return the single Client instance (cls.__instance)'}

## Constraints

- Only one Client instance may exist per process
- Re-initialization with a different API key triggers state reset
- Active trace must be ended before re-initialization with new key
- API key must be provided; missing key raises NoApiKeyException

## Cautions

- Re-initialization with a different API key is logged as unusual and may indicate misconfiguration
- Ending a previously auto-started trace due to re-initialization may interrupt ongoing monitoring

## Output Contract

- Single Client instance is returned
- _initialized flag is set to True after successful initialization
- Trace context is either preserved (same API key) or ended and reset (different API key)
- No duplicate initialization side effects occur
- NoApiKeyException is raised if API key is missing

## Triggers

- Client instantiation or __init__ call
- Re-initialization attempt with different API key detected
- Trace context lifecycle boundary crossed
