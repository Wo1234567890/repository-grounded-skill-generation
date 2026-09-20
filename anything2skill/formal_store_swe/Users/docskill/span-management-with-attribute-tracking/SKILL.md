---
id: "1877a7a2-355a-595d-a988-ebb2a4371467"
name: "Span Management with Attribute Tracking"
description: "Create and manage instrumentation spans with consistent attribute assignment using SpanAttributeManager and create_span context manager. Use when instrumenting operations that need distributed tracing and attribute metadata."
version: "0.1.0"
tags:
  - "instrumentation"
  - "distributed-tracing"
  - "span-management"
  - "attribute-tracking"
  - "observability"
triggers:
  - "Instrumenting a discrete operation that requires tracing context"
  - "Need to assign and track attribute metadata on a span"
  - "Require consistent span lifecycle management across operations"
examples:
  - input: "tracer object, operation name 'database.query', attributes {'db.system': 'postgresql', 'db.operation': 'select'}"
    output: "Span created with service_name set, attributes attached, operation code runs within span context, span recorded to backend"
    notes: "Typical database operation instrumentation"
  - input: "tracer object, operation name 'api.request', attributes {'http.method': 'POST', 'http.url': '/endpoint'}"
    output: "Span created with HTTP metadata, operation executes within traced context, span closed on exit"
    notes: "API call instrumentation"
---

# Span Management with Attribute Tracking

Create and manage instrumentation spans with consistent attribute assignment using SpanAttributeManager and create_span context manager. Use when instrumenting operations that need distributed tracing and attribute metadata.

## Prompt

Use the span management utilities to create a traced span with managed attributes for a single operation. Initialize a SpanAttributeManager with a service name, then use the create_span context manager to wrap your operation code. Pass custom attributes and the attribute manager to ensure consistent span lifecycle and metadata assignment.

## Objective

Create a traced span with managed attributes for a single operation
## Applicable Signals

- Operation requires distributed tracing visibility
- Custom attributes must be attached to span for observability
- Service name and operation name are known at instrumentation time

## Contraindications

- Operation does not require distributed tracing
- Span attributes are dynamic or unbounded
- Using a higher-level instrumentation framework that manages spans automatically

## Workflow Steps

- {'step': 1, 'action': 'Import span management utilities', 'detail': 'from agentops.instrumentation.common import create_span, SpanAttributeManager'}
- {'step': 2, 'action': 'Initialize SpanAttributeManager', 'detail': 'attr_manager = SpanAttributeManager(service_name="<service-name>")'}
- {'step': 3, 'action': 'Enter create_span context manager', 'detail': 'with create_span(tracer, "<operation-name>", attributes={...}, attribute_manager=attr_manager) as span:'}
- {'step': 4, 'action': 'Execute operation code within span scope', 'detail': 'Perform the instrumented operation; span context is active and attributes are tracked'}
- {'step': 5, 'action': 'Exit context manager', 'detail': 'Span is automatically closed and flushed to observability backend on context exit'}

## Constraints

- tracer object must be initialized before calling create_span
- operation_name must be a valid string identifier
- attributes dictionary must contain serializable values
- SpanAttributeManager must be instantiated with a service_name

## Cautions

- Ensure the tracer is properly configured for your observability backend
- Do not nest create_span calls without explicit span parent/child relationships
- Attribute keys should follow naming conventions (e.g., dot-separated identifiers)

## Output Contract

- Active span context with service_name and custom attributes set
- Operation code executes within span scope
- Span is closed and recorded upon context exit

## Example Executions

### Example 1

- Input: tracer object, operation name 'database.query', attributes {'db.system': 'postgresql', 'db.operation': 'select'}
- Output: Span created with service_name set, attributes attached, operation code runs within span context, span recorded to backend
- Notes: Typical database operation instrumentation

### Example 2

- Input: tracer object, operation name 'api.request', attributes {'http.method': 'POST', 'http.url': '/endpoint'}
- Output: Span created with HTTP metadata, operation executes within traced context, span closed on exit
- Notes: API call instrumentation

## Triggers

- Instrumenting a discrete operation that requires tracing context
- Need to assign and track attribute metadata on a span
- Require consistent span lifecycle management across operations

## Examples

### Example 1

Input:

  tracer object, operation name 'database.query', attributes {'db.system': 'postgresql', 'db.operation': 'select'}

Output:

  Span created with service_name set, attributes attached, operation code runs within span context, span recorded to backend

Notes:

  Typical database operation instrumentation

### Example 2

Input:

  tracer object, operation name 'api.request', attributes {'http.method': 'POST', 'http.url': '/endpoint'}

Output:

  Span created with HTTP metadata, operation executes within traced context, span closed on exit

Notes:

  API call instrumentation
