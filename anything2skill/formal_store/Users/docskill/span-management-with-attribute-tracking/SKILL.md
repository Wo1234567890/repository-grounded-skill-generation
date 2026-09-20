---
id: "cf066521-44bd-5d3a-ba81-5603ffba695b"
name: "Span Management with Attribute Tracking"
description: "Create and manage instrumentation spans with consistent attribute assignment using SpanAttributeManager and create_span context manager. Use when instrumenting operations that need distributed tracing and attribute metadata."
version: "0.1.0"
tags:
  - "instrumentation"
  - "distributed-tracing"
  - "span-management"
  - "attribute-tracking"
  - "context-manager"
triggers:
  - "Instrumenting a discrete operation or function call that requires distributed tracing and attribute metadata capture"
examples:
  - input: "Instrumenting a database query operation with service context"
    output: "Active span named 'db.query' with attributes {service_name: 'my-service', 'db.operation': 'select'} recorded after query execution"
    notes: "Caller provides tracer and operation name; SpanAttributeManager ensures consistent service metadata"
---

# Span Management with Attribute Tracking

Create and manage instrumentation spans with consistent attribute assignment using SpanAttributeManager and create_span context manager. Use when instrumenting operations that need distributed tracing and attribute metadata.

## Prompt

To establish a span with consistent attributes:
1. Import create_span and SpanAttributeManager from agentops.instrumentation.common
2. Instantiate SpanAttributeManager with service_name
3. Use create_span as a context manager, passing tracer, operation name, attributes dict, and attribute_manager
4. Execute operation code within the span context
5. Span automatically closes on context exit

## Objective

Establish consistent span creation and attribute management for operation tracing
## Applicable Signals

- Operation requires distributed tracing instrumentation
- Custom attribute metadata must be attached to operation span
- Caller needs to track operation execution with service context

## Contraindications

- Operation does not require tracing or monitoring
- Span context is already managed by parent instrumentation
- Tracer is not initialized or available

## Intervention Moves

- Initialize SpanAttributeManager with service identifier
- Wrap operation code in create_span context manager
- Pass operation name and attribute dict to create_span
- Allow span to auto-close on context exit

## Workflow Steps

- {'step': 1, 'action': 'Import utilities', 'detail': 'from agentops.instrumentation.common import create_span, SpanAttributeManager'}
- {'step': 2, 'action': 'Create attribute manager', 'detail': 'attr_manager = SpanAttributeManager(service_name="<service-identifier>")'}
- {'step': 3, 'action': 'Enter span context', 'detail': 'with create_span(tracer, "<operation.name>", attributes={...}, attribute_manager=attr_manager) as span:'}
- {'step': 4, 'action': 'Execute operation', 'detail': 'Place operation code inside the with block'}
- {'step': 5, 'action': 'Exit and record', 'detail': 'Span automatically closes and records on context exit'}

## Constraints

- Tracer object must be available and initialized before calling create_span
- SpanAttributeManager must be instantiated with valid service_name
- Operation code must execute within the context manager block

## Cautions

- Ensure tracer lifecycle is managed by caller; create_span does not initialize tracer
- Attributes dict should contain only serializable values
- Nested spans require separate create_span calls; do not reuse span context across operations

## Output Contract

- Returns active span object with service_name and custom attributes set; operation code executes within span context; span automatically closes and records on context exit

## Example Therapist Responses

### Example 1

- Client/Input: Instrumenting a database query operation with service context
- Therapist/Output: Active span named 'db.query' with attributes {service_name: 'my-service', 'db.operation': 'select'} recorded after query execution
- Notes: Caller provides tracer and operation name; SpanAttributeManager ensures consistent service metadata

## Triggers

- Instrumenting a discrete operation or function call that requires distributed tracing and attribute metadata capture

## Examples

### Example 1

Input:

  Instrumenting a database query operation with service context

Output:

  Active span named 'db.query' with attributes {service_name: 'my-service', 'db.operation': 'select'} recorded after query execution

Notes:

  Caller provides tracer and operation name; SpanAttributeManager ensures consistent service metadata
