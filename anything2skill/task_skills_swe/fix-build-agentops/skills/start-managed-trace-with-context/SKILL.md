---
id: "2fefe2f0-790d-5e47-99c5-c441046648cf"
name: "Start Managed Trace with Context"
description: "Create a new root span (trace) with optional name and tags, returning a TraceContext object for concurrent user-managed tracing sessions. Includes precondition validation and automatic initialization fallback."
version: "0.1.0"
tags:
  - "trace_management"
  - "session_lifecycle"
  - "span_creation"
  - "concurrent_tracing"
  - "context_management"
triggers:
  - "Starting a new logical trace or session"
  - "Need to attach tags or custom trace names to a trace"
  - "Require concurrent independent traces managed by caller"
---

# Start Managed Trace with Context

Create a new root span (trace) with optional name and tags, returning a TraceContext object for concurrent user-managed tracing sessions. Includes precondition validation and automatic initialization fallback.

## Prompt

Call start_trace(trace_name, tags) to initiate a named trace session. If SDK is not initialized, the function attempts auto-initialization with environment defaults before creating the trace. Returns a TraceContext object on success, or None if initialization fails. Use this to establish independent, concurrent trace sessions with custom metadata.

## Objective

Establish a named trace session with optional metadata and return its context for downstream span operations
## Applicable Signals

- User initiates a new task or session boundary
- Caller needs to track a named workflow or user interaction
- Multiple concurrent traces must be managed independently

## Contraindications

- Tracing is not enabled or SDK is not initialized
- User does not need trace context or span management
- Caller cannot handle None return value (initialization failure)

## Workflow Steps

- {'step': 1, 'action': 'Check if tracer is initialized', 'condition': 'if not tracer.initialized'}
- {'step': 2, 'action': 'Log warning and attempt auto-initialization', 'condition': 'SDK not initialized', 'detail': 'Call init() with environment variables and defaults'}
- {'step': 3, 'action': 'Verify initialization success', 'condition': 'After init() call', 'detail': 'Check tracer.initialized; log error and return None if still False'}
- {'step': 4, 'action': 'Catch and log initialization exceptions', 'condition': 'If init() raises exception', 'detail': 'Log error with exception details and return None'}
- {'step': 5, 'action': 'Invoke tracer.start_trace()', 'condition': 'tracer.initialized is True', 'detail': 'Pass trace_name and tags; return TraceContext object'}

## Constraints

- SDK must be initialized before or during start_trace call
- trace_name should be a non-empty string (default: 'session')
- tags must be either a list of strings or a dict; other types are rejected

## Cautions

- If SDK auto-initialization fails, function returns None; caller must handle gracefully
- Concurrent traces require caller to manage context tokens separately
- Trace context is valid only if tracer.initialized is True after initialization attempt

## Output Contract

- Returns a TraceContext object containing the span and context token on success. Returns None if SDK initialization fails or is not available. Caller must check for None before using the returned context.

## Triggers

- Starting a new logical trace or session
- Need to attach tags or custom trace names to a trace
- Require concurrent independent traces managed by caller
