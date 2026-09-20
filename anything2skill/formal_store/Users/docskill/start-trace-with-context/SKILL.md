---
id: "940d307d-ee0e-5807-8c39-4c5d23259d41"
name: "Start Trace with Context"
description: "Initiates a new root span (trace) with a user-provided name and optional tags, returning a TraceContext object for concurrent, user-managed tracing sessions."
version: "0.1.0"
tags:
  - "tracing"
  - "observability"
  - "session-management"
  - "span-creation"
  - "context-management"
triggers:
  - "User wants to start a new logical trace for a session, task, or user interaction"
  - "Multiple concurrent traces are needed and must be user-managed"
  - "A new root span is required to organize related observability events"
---

# Start Trace with Context

Initiates a new root span (trace) with a user-provided name and optional tags, returning a TraceContext object for concurrent, user-managed tracing sessions.

## Prompt

Call start_trace(trace_name, tags) to create a new trace context. Provide a descriptive trace_name (e.g., 'session', 'my_custom_task') and optional tags as a list of strings or dict. The function will attempt SDK initialization if not already initialized, then return a TraceContext object containing the span and context token, or None if initialization fails.

## Objective

Create a new trace context to group and manage related spans within a session or task.
## Applicable Signals

- Session or task boundary detected
- Request for concurrent trace management
- Need to attach metadata (tags) to a trace root

## Contraindications

- SDK is not initialized and auto-initialization fails
- Caller does not need a separate trace context
- Tracing is disabled or not required by the application

## Workflow Steps

- {'step': 1, 'action': 'Check if tracer is initialized', 'detail': 'If not initialized, attempt auto-initialization via init()'}
- {'step': 2, 'action': 'Validate initialization state', 'detail': 'If initialization fails, log error and return None'}
- {'step': 3, 'action': 'Call tracer.start_trace(trace_name, tags)', 'detail': 'Create and return TraceContext object with span and context token'}

## Constraints

- SDK must be initialized (either explicitly or via auto-initialization attempt) before trace creation
- trace_name should be a non-empty string
- tags, if provided, must be either a list of strings or a dict

## Cautions

- If SDK is not initialized, the function will attempt auto-initialization with environment variables and defaults; explicit initialization is preferred
- If auto-initialization fails, the function logs an error and returns None; caller must handle None return value
- Multiple concurrent traces may increase memory and observability overhead; use judiciously

## Output Contract

- Returns a TraceContext object containing the span and context token on success; returns None if SDK initialization fails or SDK is not initialized after auto-initialization attempt.

## Triggers

- User wants to start a new logical trace for a session, task, or user interaction
- Multiple concurrent traces are needed and must be user-managed
- A new root span is required to organize related observability events
