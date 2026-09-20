---
id: "65c4f3e1-5962-5d47-9d5f-d9524126ed9a"
name: "Start Trace Session"
description: "Initiates a named trace with optional tags and returns a trace context for subsequent span operations. Use when beginning a new debugging or monitoring session."
version: "0.1.0"
tags:
  - "trace_lifecycle"
  - "debugging"
  - "monitoring"
  - "initialization"
triggers:
  - "starting a new trace session"
  - "beginning a debugging workflow"
  - "initializing monitoring for an agent operation"
---

# Start Trace Session

Initiates a named trace with optional tags and returns a trace context for subsequent span operations. Use when beginning a new debugging or monitoring session.

## Prompt

Call tracer.start_trace() with a trace_name and optional tags to initialize a new trace session. The returned TraceContext object is required for all subsequent span operations within this trace.

## Objective

initialize trace context
## Applicable Signals

- new session initiated
- debugging workflow started
- agent operation begins

## Contraindications

- a trace is already active in the current session
- only updating existing trace metadata

## Workflow Steps

- Prepare trace_name (string identifier for the trace)
- Optionally prepare tags (dict or list for categorization)
- Call tracer.start_trace(trace_name=trace_name, tags=tags)
- Capture and store returned TraceContext object
- Proceed with span operations using the TraceContext

## Constraints

- trace_name must be provided
- tags parameter is optional but recommended for filtering

## Output Contract

- Returns a TraceContext object that is active and ready for span operations. The caller must retain this context for use in subsequent trace operations (span creation, metadata updates, trace termination).

## Triggers

- starting a new trace session
- beginning a debugging workflow
- initializing monitoring for an agent operation
