---
id: "52956153-19be-543e-882e-ea4d44eb1b9c"
name: "Resolve Active Span from OpenTelemetry Context"
description: "Retrieve and validate the current span from OpenTelemetry context, then locate the root trace span if the current span is a child span. Use this when instrumenting distributed tracing and need to attach operations to the correct parent trace."
version: "0.1.0"
tags:
  - "opentelemetry"
  - "distributed_tracing"
  - "span_resolution"
  - "trace_instrumentation"
triggers:
  - "Instrumenting an operation within an active OpenTelemetry trace and need to attach to the root session span rather than a child span"
---

# Resolve Active Span from OpenTelemetry Context

Retrieve and validate the current span from OpenTelemetry context, then locate the root trace span if the current span is a child span. Use this when instrumenting distributed tracing and need to attach operations to the correct parent trace.

## Prompt

1. Call get_current_span() to retrieve the active span from OpenTelemetry context.
2. Validate that the span exists and is recording (check hasattr(current_span, 'is_recording') and current_span.is_recording()).
3. Inspect the span name to determine if it is a session/trace span (ends with '.SESSION') or a child span.
4. If it is a session/trace span, use it directly as the target span.
5. If it is a child span, retrieve all active traces using tracer.get_active_traces().
6. Match the current span's trace_id (via current_span.get_span_context().trace_id) to find the parent trace.
7. If no parent trace is found or no active traces exist, fall back to the current span.
8. Return the resolved span object ready for operation attachment.

## Objective

Locate the correct parent trace span for operation instrumentation
## Applicable Signals

- Instrumenting an operation within an active OpenTelemetry trace
- Need to attach operation to root session span rather than child span
- Span recording is active and valid

## Contraindications

- No active OpenTelemetry context exists
- Span recording is disabled (is_recording() returns false)
- Operating outside a traced session
- Current span is null or invalid

## Workflow Steps

- {'step': 1, 'action': 'Retrieve current span', 'detail': 'Call get_current_span() from OpenTelemetry context'}
- {'step': 2, 'action': 'Validate span state', 'detail': 'Check span exists, has is_recording method, and is_recording() returns true'}
- {'step': 3, 'action': 'Classify span type', 'detail': "Inspect span name; if ends with '.SESSION', it is a root trace span; otherwise it is a child span"}
- {'step': 4, 'action': 'Resolve to root span', 'detail': "If child span, retrieve active traces and match current span's trace_id to find parent; if no match or no active traces, use current span"}
- {'step': 5, 'action': 'Return resolved span', 'detail': 'Return the valid, recording span object ready for operation attachment'}

## Constraints

- Span must be recording (is_recording() must return true)
- OpenTelemetry context must be active
- Span object must have name and get_span_context() methods

## Cautions

- If parent trace lookup fails, the skill falls back to the current span; verify this is acceptable for your use case
- Span name inspection relies on naming convention (ends with '.SESSION'); ensure your instrumentation follows this convention

## Output Contract

- Returns a valid, recording span object (either the current session span or the resolved root trace span) ready for operation attachment. If no valid span can be resolved, returns the current span as fallback. Caller can immediately use the returned span for attaching operations or child spans.

## Triggers

- Instrumenting an operation within an active OpenTelemetry trace and need to attach to the root session span rather than a child span
