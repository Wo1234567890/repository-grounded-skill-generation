---
id: "eace1bd8-b8f0-5539-bde6-e9f7deaa0c40"
name: "Decorator-Based Observability Instrumentation"
description: "Apply Python decorators (@workflow, @agent, @operation) to functions and classes to automatically capture execution spans and observability data with minimal code overhead."
version: "0.1.0"
tags:
  - "observability"
  - "instrumentation"
  - "decorator"
  - "agent"
  - "workflow"
  - "span_capture"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Developer needs to add observability to a workflow function"
  - "Agent class requires execution span capture"
  - "Operation method needs automatic instrumentation"
---

# Decorator-Based Observability Instrumentation

Apply Python decorators (@workflow, @agent, @operation) to functions and classes to automatically capture execution spans and observability data with minimal code overhead.

## Prompt

Use @workflow decorator on workflow functions, @agent on agent classes, and @operation on operation methods. Nest decorators to establish proper span hierarchy. Each decorator automatically emits execution spans to the observability backend without additional instrumentation code.

## Objective

Enable observability instrumentation of agent workflows and operations
## Applicable Signals

- Workflow function definition
- Agent class definition
- Operation method within agent class

## Contraindications

- Legacy code without decorator support
- Real-time streaming contexts where decorator overhead is prohibitive

## Workflow Steps

- Import decorators from agentops.sdk.decorators
- Apply @workflow decorator to workflow function or @agent to agent class
- Apply @operation decorator to operation methods within agent class
- Ensure decorator nesting follows proper span hierarchy
- Execute decorated code; spans are automatically emitted

## Constraints

- Decorators must be applied in correct hierarchy: @agent wraps class, @operation wraps methods, @workflow wraps functions
- Requires agentops.sdk.decorators module availability

## Output Contract

- Decorated function or class that automatically emits execution spans to observability backend; no manual span creation required

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Developer needs to add observability to a workflow function
- Agent class requires execution span capture
- Operation method needs automatic instrumentation
