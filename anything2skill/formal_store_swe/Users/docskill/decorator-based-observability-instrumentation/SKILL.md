---
id: "a1a7e0ae-7044-57cb-acba-af065d511fe0"
name: "Decorator-based Observability Instrumentation"
description: "Apply decorator patterns (@workflow, @agent, @operation) to instrument functions and classes with observability spans, enabling hierarchical tracing of agent execution with minimal code overhead."
version: "0.1.0"
tags:
  - "observability"
  - "instrumentation"
  - "decorator_pattern"
  - "agent_tracing"
  - "span_hierarchy"
triggers:
  - "Adding tracing to agent workflows"
  - "Instrumenting nested operations in class-based agents"
  - "Requiring minimal code changes for observability"
  - "Need for hierarchical span hierarchy in agent execution"
examples:
  - input: "Standalone workflow function requiring observability"
    output: "@workflow decorator applied; function emits workflow-level span on execution"
    notes: "Minimal code change: single decorator line added"
  - input: "Agent class with nested operation methods"
    output: "@agent on class, @operation on methods; hierarchical spans emitted with agent span as parent"
    notes: "Proper nesting establishes parent-child span relationships"
---

# Decorator-based Observability Instrumentation

Apply decorator patterns (@workflow, @agent, @operation) to instrument functions and classes with observability spans, enabling hierarchical tracing of agent execution with minimal code overhead.

## Prompt

Use @workflow, @agent, and @operation decorators from agentops.sdk.decorators to wrap functions and class methods. Nest decorators to establish proper span hierarchy: @agent wraps classes, @operation wraps methods within agent classes, @workflow wraps standalone workflow functions. Each decorator automatically emits observability spans during execution without requiring manual span management code.

## Objective

Instrument agent code with observability decorators to enable hierarchical execution tracing
## Applicable Signals

- Agent workflow implementation starting
- Class-based agent definition
- Nested operation methods being added
- Observability requirement identified

## Contraindications

- Non-Python codebases
- Target functions or classes that cannot accept decorators
- Span hierarchy not required or desired
- Existing instrumentation that conflicts with decorator application

## Intervention Moves

- Import decorators from agentops.sdk.decorators
- Apply @workflow decorator to workflow functions
- Apply @agent decorator to agent class definition
- Apply @operation decorator to methods within agent class
- Verify decorator nesting order for proper span hierarchy

## Workflow Steps

- Identify target functions or classes requiring observability
- Import decorators from agentops.sdk.decorators
- Apply appropriate decorator based on target type (@workflow for functions, @agent for classes)
- Apply @operation decorators to methods within agent classes
- Verify decorator nesting order and span hierarchy
- Test instrumented code to confirm span emission

## Constraints

- Decorators must be imported from agentops.sdk.decorators
- Decorator nesting order must follow: @agent (class level) → @operation (method level) or @workflow (function level)
- Decorated functions and methods must be callable with their original signatures

## Cautions

- Ensure decorator import path is correct for the agentops version in use
- Verify that decorator application does not conflict with other decorators on the same target
- Test span hierarchy output to confirm proper nesting before production deployment

## Output Contract

- Instrumented code with decorator-applied functions and classes that emit hierarchical observability spans during execution. Spans are automatically created and linked according to decorator nesting hierarchy.

## Example Executions

### Example 1

- Input: Standalone workflow function requiring observability
- Output: @workflow decorator applied; function emits workflow-level span on execution
- Notes: Minimal code change: single decorator line added

### Example 2

- Input: Agent class with nested operation methods
- Output: @agent on class, @operation on methods; hierarchical spans emitted with agent span as parent
- Notes: Proper nesting establishes parent-child span relationships

## Triggers

- Adding tracing to agent workflows
- Instrumenting nested operations in class-based agents
- Requiring minimal code changes for observability
- Need for hierarchical span hierarchy in agent execution

## Examples

### Example 1

Input:

  Standalone workflow function requiring observability

Output:

  @workflow decorator applied; function emits workflow-level span on execution

Notes:

  Minimal code change: single decorator line added

### Example 2

Input:

  Agent class with nested operation methods

Output:

  @agent on class, @operation on methods; hierarchical spans emitted with agent span as parent

Notes:

  Proper nesting establishes parent-child span relationships
