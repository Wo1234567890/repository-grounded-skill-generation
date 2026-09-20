---
id: "f7f4d305-3894-5d88-8f74-41d498d0b6e8"
name: "Active Span Resolution in Distributed Tracing"
description: "Retrieve and validate the current OpenTelemetry span from context, then resolve it to the appropriate session or root trace span for logging and debugging."
version: "0.1.0"
tags:
  - "opentelemetry"
  - "distributed_tracing"
  - "span_resolution"
  - "instrumentation"
  - "debugging"
  - "telemetry"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "A logging or debugging operation needs to attach telemetry data to the correct trace context"
  - "The current execution context may be a child span or a root session span"
  - "Span attachment is required before recording events or attributes"
---

# Active Span Resolution in Distributed Tracing

Retrieve and validate the current OpenTelemetry span from context, then resolve it to the appropriate session or root trace span for logging and debugging.

## Prompt

1. Call get_current_span() to retrieve the span from OpenTelemetry context.
2. Validate that the span exists and is recording (check is_recording() method).
3. Inspect the span name to determine if it is a session/trace span (ends with .SESSION) or a child span.
4. If it is a session span, use it directly.
5. If it is a child span, attempt to retrieve active traces via tracer.get_active_traces().
6. Match the current span's trace_id against active traces to find the parent trace span.
7. If no parent trace is found or no active traces exist, fall back to the current span.
8. Return the resolved span object.

## Objective

resolve_active_span
## Applicable Signals

- OpenTelemetry context is active
- get_current_span() returns a non-null span
- Span has is_recording() method available

## Contraindications

- No OpenTelemetry context is available in the current execution
- The span is not recording (is_recording() returns false)
- Offline or non-instrumented execution paths
- Tracer instance is unavailable or uninitialized

## Workflow Steps

- {'step': 1, 'action': 'Retrieve current span', 'detail': 'Call get_current_span() from OpenTelemetry context'}
- {'step': 2, 'action': 'Validate span', 'detail': 'Check that span is not null, has is_recording method, and is_recording() returns true'}
- {'step': 3, 'action': 'Determine span type', 'detail': 'Extract span name and check if it ends with .SESSION to identify session/trace span'}
- {'step': 4, 'action': 'Resolve to appropriate span', 'detail': 'If session span, use directly; if child span, query active traces and match by trace_id'}
- {'step': 5, 'action': 'Fallback handling', 'detail': 'If parent trace not found or no active traces, use current span as fallback'}

## Constraints

- The span object must have a name attribute or default to empty string
- The span context must expose a trace_id for parent matching
- Active traces must be queryable via tracer.get_active_traces()

## Cautions

- If no parent trace is found, the fallback to current span may not represent the full session context
- Span name matching relies on exact suffix comparison; naming conventions must be consistent

## Output Contract

- A valid, recording span object (either the current session span or the resolved root trace span) ready for event or attribute attachment. The returned span must satisfy: span is not null, span.is_recording() == true, and span has a valid trace_id.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- A logging or debugging operation needs to attach telemetry data to the correct trace context
- The current execution context may be a child span or a root session span
- Span attachment is required before recording events or attributes
