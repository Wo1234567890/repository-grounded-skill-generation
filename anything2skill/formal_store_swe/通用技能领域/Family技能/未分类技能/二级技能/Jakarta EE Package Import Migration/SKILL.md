---
id: "be9ee306-d51d-5fa4-ae33-699cbc310f42"
name: "Jakarta EE Package Import Migration"
description: "Initialize and configure the AgentOps SDK by importing core tracing decorators, semantic conventions, and client infrastructure. Establishes the public API surface for agent instrumentation and tracing context setup."
version: "0.1.1"
tags:
  - "initialization"
  - "sdk_setup"
  - "instrumentation"
  - "tracing"
  - "decorators"
  - "backward_compatibility"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Upgrading Spring Boot 2.x application to 3.0"
  - "Jakarta EE 10 dependencies added to project"
  - "Import statements reference javax packages"
---

# Jakarta EE Package Import Migration

Initialize and configure the AgentOps SDK by importing core tracing decorators, semantic conventions, and client infrastructure. Establishes the public API surface for agent instrumentation and tracing context setup.

## Prompt

Import and expose AgentOps core modules: legacy session management (start_session, end_session, track_agent, track_tool, Session, ToolEvent, ErrorEvent, ActionEvent, LLMEvent), modern decorators (trace, session, agent, task, workflow, operation, tool, guardrail, track_endpoint), semantic convention attributes (AgentAttributes, ToolAttributes, WorkflowAttributes, CoreAttributes, SpanAttributes, SpanKind), client (Client), tracing utilities (TraceContext, tracer, get_current_span), enums (TraceState, SUCCESS, ERROR, UNSET, StatusCode), and logging/deprecation helpers. Ensure backward compatibility with legacy API while exposing modern instrumentation decorators.

## Objective

Set up AgentOps tracing infrastructure and expose public API for agent instrumentation
## Applicable Signals

- Application startup phase
- First import of agentops module
- Need to access decorators or session management

## Contraindications

- Already in an active tracing session (re-initialization may cause conflicts)
- Only legacy session management is required without modern decorator support

## Workflow Steps

- Import legacy session management and event types from agentops.legacy
- Import OpenTelemetry trace utilities (get_current_span, StatusCode)
- Import semantic convention classes (AgentAttributes, ToolAttributes, WorkflowAttributes, CoreAttributes, SpanKind, SpanAttributes)
- Import Client from agentops.client
- Import TraceContext and tracer from agentops.sdk.core
- Import all decorators from agentops.sdk.decorators
- Import enums (TraceState, SUCCESS, ERROR, UNSET)
- Import logging and deprecation utilities
- Re-export all imported items at module level for public API access

## Constraints

- Must import from agentops.legacy for backward compatibility
- Must expose all decorator types (trace, session, agent, task, workflow, operation, tool, guardrail, track_endpoint)
- Must include semantic convention attributes and SpanKind enums
- Must provide TraceContext and tracer for modern instrumentation

## Cautions

- Ensure OpenTelemetry dependencies are installed before importing trace utilities
- Legacy imports must remain available for backward compatibility with existing code
- Deprecation warnings should be logged for legacy APIs to guide users toward modern decorators

## Output Contract

- All core decorators (trace, session, agent, task, workflow, operation, tool, guardrail, track_endpoint), semantic attributes (AgentAttributes, ToolAttributes, WorkflowAttributes, CoreAttributes, SpanAttributes, SpanKind), Client, TraceContext, tracer, legacy session management functions, and event types are available for import from agentops module. Module initialization completes without import errors.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Upgrading Spring Boot 2.x application to 3.0
- Jakarta EE 10 dependencies added to project
- Import statements reference javax packages
