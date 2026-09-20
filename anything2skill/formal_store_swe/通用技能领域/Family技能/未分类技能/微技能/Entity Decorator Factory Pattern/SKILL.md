---
id: "d76c2816-0980-5898-a510-cbbeb12f7498"
name: "Entity Decorator Factory Pattern"
description: "Create reusable decorators for instrumentation of agent entities (agent, task, operation, workflow, session, tool, guardrail, HTTP endpoint) using a factory function that maps semantic span kinds to decorator implementations."
version: "0.1.0"
tags:
  - "instrumentation"
  - "decorator"
  - "factory_pattern"
  - "agent_system"
  - "span_kind"
  - "setup"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Need to instrument multiple entity types in an agent system with consistent span-kind-based decoration"
  - "Want to avoid repetitive decorator definitions across agent, task, operation, workflow, session, tool, guardrail, and HTTP endpoint types"
---

# Entity Decorator Factory Pattern

Create reusable decorators for instrumentation of agent entities (agent, task, operation, workflow, session, tool, guardrail, HTTP endpoint) using a factory function that maps semantic span kinds to decorator implementations.

## Prompt

Use create_entity_decorator(SpanKind.*) to generate entity-specific decorators. Each call returns a callable decorator that wraps functions and methods with span-kind-based instrumentation. Assign the result to a variable matching the entity type (e.g., agent = create_entity_decorator(SpanKind.AGENT)).

## Objective

Generate entity-specific decorators from a factory
## Applicable Signals

- Multiple entity types require instrumentation
- Span-kind semantics are available and sufficient to differentiate entity behavior
- Decorator setup phase of agent system initialization

## Contraindications

- Entity types require fundamentally different instrumentation logic beyond span-kind mapping
- Decorator behavior must vary per entity in ways not expressible via span kind
- Custom per-entity instrumentation hooks are needed

## Workflow Steps

- Import create_entity_decorator from agentops.sdk.decorators.factory
- Import SpanKind from agentops.semconv.span_kinds
- For each entity type (agent, task, operation, workflow, session, tool, guardrail, track_endpoint), call create_entity_decorator(SpanKind.<TYPE>) and assign to a variable
- Verify all decorators are callable and ready for use

## Constraints

- SpanKind enum must be imported and available
- create_entity_decorator factory function must be accessible from agentops.sdk.decorators.factory
- Each decorator assignment must use the correct SpanKind constant

## Output Contract

- Set of callable decorators (agent, task, operation, workflow, trace, tool, guardrail, track_endpoint) ready to wrap functions and methods with span-kind-based instrumentation

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Need to instrument multiple entity types in an agent system with consistent span-kind-based decoration
- Want to avoid repetitive decorator definitions across agent, task, operation, workflow, session, tool, guardrail, and HTTP endpoint types
