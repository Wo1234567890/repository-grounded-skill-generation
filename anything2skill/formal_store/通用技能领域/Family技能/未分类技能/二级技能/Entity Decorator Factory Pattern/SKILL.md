---
id: "453f771d-10b8-57c4-bb54-b12321a1b7b8"
name: "Entity Decorator Factory Pattern"
description: "Factory-based system for creating reusable decorators that instrument agent operations (agents, tasks, workflows, tools, guardrails, HTTP endpoints) with semantic span kinds for observability and tracing."
version: "0.1.0"
tags:
  - "observability"
  - "instrumentation"
  - "decorator"
  - "factory_pattern"
  - "span_semantics"
  - "tracing"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Initializing agent framework; need to instrument multiple entity types (agent, task, workflow, tool, guardrail, HTTP) with consistent span semantics"
---

# Entity Decorator Factory Pattern

Factory-based system for creating reusable decorators that instrument agent operations (agents, tasks, workflows, tools, guardrails, HTTP endpoints) with semantic span kinds for observability and tracing.

## Prompt

Use create_entity_decorator(SpanKind.*) to generate callable decorators for each entity type. Each decorator wraps functions to emit semantic spans. Supported entity types: AGENT, TASK, OPERATION, WORKFLOW, SESSION, TOOL, GUARDRAIL, HTTP. Assign decorators to module-level variables (agent, task, workflow, tool, guardrail, track_endpoint) for caller access.

## Objective

Standardize decorator creation and span instrumentation across heterogeneous entity types
## Applicable Signals

- Agent framework initialization
- Multi-entity type instrumentation required
- Need consistent span semantics across operations
- Observability setup phase

## Contraindications

- Single one-off decorator needed without factory pattern
- No multi-entity instrumentation required
- Span kind not defined in SpanKind enum
- Custom span semantics incompatible with predefined SpanKind values

## Intervention Moves

- Call create_entity_decorator(SpanKind.AGENT) to create agent decorator
- Call create_entity_decorator(SpanKind.TASK) to create task decorator
- Call create_entity_decorator(SpanKind.WORKFLOW) to create workflow decorator
- Call create_entity_decorator(SpanKind.TOOL) to create tool decorator
- Call create_entity_decorator(SpanKind.GUARDRAIL) to create guardrail decorator
- Call create_entity_decorator(SpanKind.HTTP) to create HTTP endpoint decorator
- Assign each decorator to module-level variable for caller access

## Workflow Steps

- {'step': 1, 'action': 'Import factory and SpanKind', 'detail': 'from agentops.sdk.decorators.factory import create_entity_decorator; from agentops.semconv.span_kinds import SpanKind'}
- {'step': 2, 'action': 'Create decorators for each entity type', 'detail': 'Call create_entity_decorator(SpanKind.*) for AGENT, TASK, WORKFLOW, TOOL, GUARDRAIL, HTTP'}
- {'step': 3, 'action': 'Assign decorators to module-level variables', 'detail': 'agent = create_entity_decorator(SpanKind.AGENT); task = create_entity_decorator(SpanKind.TASK); workflow = create_entity_decorator(SpanKind.WORKFLOW); tool = create_entity_decorator(SpanKind.TOOL); guardrail = create_entity_decorator(SpanKind.GUARDRAIL); track_endpoint = create_entity_decorator(SpanKind.HTTP)'}
- {'step': 4, 'action': 'Expose decorators for caller use', 'detail': 'Ensure all decorator variables are accessible at module scope for downstream imports'}

## Constraints

- SpanKind must be defined in agentops.semconv.span_kinds
- create_entity_decorator must be imported from agentops.sdk.decorators.factory
- Decorators must be assigned to module-level variables for external caller access
- Each entity type maps to exactly one SpanKind

## Cautions

- Ensure SpanKind enum is up-to-date before factory calls
- Verify decorator assignments match caller expectations for naming
- Operation decorator aliasing (operation = task) may cause confusion; document intent clearly
- SESSION decorator is deprecated; use TRACE decorator instead for backward compatibility

## Output Contract

- Set of callable decorators (agent, task, workflow, tool, guardrail, track_endpoint) ready to wrap functions and emit semantic spans. Each decorator is a function that accepts a target function and returns an instrumented version.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Initializing agent framework; need to instrument multiple entity types (agent, task, workflow, tool, guardrail, HTTP) with consistent span semantics
