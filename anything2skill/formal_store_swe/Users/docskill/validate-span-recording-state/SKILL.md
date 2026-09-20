---
id: "482c8c63-8631-5580-8087-30e268523611"
name: "Validate Span Recording State"
description: "Check whether the current span exists, has the is_recording attribute, and is actively recording. Use this as a guard before attempting to attach operations or metadata to a span."
version: "0.1.0"
tags:
  - "opentelemetry"
  - "distributed_tracing"
  - "span_validation"
  - "safety_guard"
  - "pre_operation_check"
triggers:
  - "Before attaching any operation, event, or attribute to a span in an OpenTelemetry instrumentation"
---

# Validate Span Recording State

Check whether the current span exists, has the is_recording attribute, and is actively recording. Use this as a guard before attempting to attach operations or metadata to a span.

## Prompt

Before attaching any operation, event, or attribute to a span in an OpenTelemetry instrumentation, validate that the current span is valid and recording. Check three conditions in sequence: (1) span object exists, (2) span has the is_recording attribute, (3) is_recording() returns true. If all conditions pass, the span is safe to use. If any condition fails, return false or use a safe fallback.

## Objective

Prevent invalid or non-recording span operations
## Applicable Signals

- Before attaching any operation, event, or attribute to a span
- Before calling span methods in OpenTelemetry instrumentation
- When span source is uncertain or may be inactive

## Contraindications

- Span is known to be valid and recording from prior checks
- Operating in a non-instrumented context
- Span validation has already been performed in the call chain

## Workflow Steps

- {'step': 1, 'action': 'Retrieve current span from OpenTelemetry context', 'detail': 'Call get_current_span() to obtain the active span'}
- {'step': 2, 'action': 'Check span existence', 'detail': 'Verify current_span is not None or falsy'}
- {'step': 3, 'action': 'Check is_recording attribute presence', 'detail': "Use hasattr(current_span, 'is_recording') to confirm attribute exists"}
- {'step': 4, 'action': 'Check recording state', 'detail': 'Call current_span.is_recording() and verify it returns true'}
- {'step': 5, 'action': 'Return validation result', 'detail': 'Return true if all three conditions pass; return false or fallback otherwise'}

## Constraints

- Must check span existence before accessing attributes
- Must verify is_recording attribute presence before calling it
- Must call is_recording() as a method, not access as property

## Cautions

- A span may exist but not be recording; both conditions are required
- hasattr() check is necessary to avoid AttributeError on spans without is_recording
- Fallback behavior (no-op or current span) should be defined by caller

## Output Contract

- Boolean confirmation that the span is valid and recording (true), or false/fallback indicator (e.g., no-op, current span, or null) when validation fails. Caller must check this result before proceeding with span operations.

## Triggers

- Before attaching any operation, event, or attribute to a span in an OpenTelemetry instrumentation
