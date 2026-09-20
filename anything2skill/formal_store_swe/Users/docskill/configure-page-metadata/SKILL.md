---
id: "09ce233c-5aa4-597c-9eef-504f22c29721"
name: "Configure Page Metadata"
description: "Apply OpenTelemetry decorators to instrument functions and methods with automatic span creation and lifecycle management. Use when adding tracing to agent operations, tool calls, workflows, or endpoints without manual span control."
version: "0.1.1"
tags:
  - "tracing"
  - "instrumentation"
  - "opentelemetry"
  - "decorator"
  - "observability"
  - "agent_operations"
triggers:
  - "Building a new page or layout that needs SEO optimization"
  - "Customizing social media preview for a page"
  - "Configuring custom head element content"
---

# Configure Page Metadata

Apply OpenTelemetry decorators to instrument functions and methods with automatic span creation and lifecycle management. Use when adding tracing to agent operations, tool calls, workflows, or endpoints without manual span control.

## Prompt

Import decorators from agentops.sdk.decorators (@trace, @session, @agent, @task, @workflow, @operation, @tool, @guardrail, @track_endpoint). Apply the appropriate decorator to the target function or method. The decorator automatically creates an OpenTelemetry span, sets the span kind and semantic attributes, and manages the span lifecycle (start, end, status). No manual span creation or closure is required.

## Objective

Enable declarative span creation and lifecycle management via decorators for agent operations
## Applicable Signals

- Function or method requires distributed tracing
- Agent operation needs observability context
- Workflow or task execution must be traced

## Contraindications

- Manual span control is required
- Decorators conflict with existing instrumentation
- Custom span lifecycle logic is needed

## Workflow Steps

- Import the appropriate decorator from agentops.sdk.decorators
- Apply the decorator to the target function or method
- Decorator automatically creates and manages the OpenTelemetry span
- Span kind and semantic attributes are set based on decorator type
- Function executes within the span context
- Span lifecycle (start, end, status) is managed automatically

## Constraints

- Decorator must be imported from agentops.sdk.decorators
- Target function must be compatible with decorator wrapping
- OpenTelemetry context must be initialized before decorator application

## Cautions

- Ensure OpenTelemetry SDK is properly initialized before using decorators
- Decorator stacking may create nested spans; verify intended span hierarchy
- Exception handling within decorated functions is automatically captured in span status

## Output Contract

- Decorated functions automatically create and manage OpenTelemetry spans with appropriate span kind and attributes. Spans are properly closed and status is recorded upon function completion or exception.

## Triggers

- Building a new page or layout that needs SEO optimization
- Customizing social media preview for a page
- Configuring custom head element content
