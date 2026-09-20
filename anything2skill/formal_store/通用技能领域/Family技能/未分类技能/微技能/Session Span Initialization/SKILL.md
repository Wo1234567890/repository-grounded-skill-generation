---
id: "58f1d777-5d14-5893-b5da-1edab414b682"
name: "Session Span Initialization"
description: "Decorator-based pattern to create a root session span that wraps and tracks all nested operations within a workflow function. Establishes the observability root context for end-to-end operation tracking."
version: "0.1.0"
tags:
  - "observability"
  - "decorator"
  - "session"
  - "span"
  - "initialization"
  - "root_context"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Beginning a new workflow or agent session"
  - "Starting execution that requires end-to-end operation tracking"
  - "Initializing a new observable execution context"
---

# Session Span Initialization

Decorator-based pattern to create a root session span that wraps and tracks all nested operations within a workflow function. Establishes the observability root context for end-to-end operation tracking.

## Prompt

Apply the @session decorator to your workflow function to initialize a root session span. This span serves as the parent context for all nested agent, tool, and function spans. Import from agentops.sdk.decorators and decorate your main workflow function.

## Objective

Initialize observability root span for a workflow
## Applicable Signals

- Workflow entry point identified
- Session-level observability required
- Root span context needed for nested operations

## Contraindications

- Tracking individual function calls within an already-active session; use agent or function spans instead
- Nested session initialization within an active session

## Workflow Steps

- Import @session decorator from agentops.sdk.decorators
- Apply @session decorator to the workflow function definition
- Execute the decorated function; the session span is automatically created and activated
- All nested operations (agent spans, function spans, tool calls) are automatically nested under this root span
- Session span closes when the decorated function returns

## Constraints

- Must be applied at the workflow function level, not within nested function calls
- Requires agentops.sdk.decorators import
- Session span must wrap the entire workflow lifecycle

## Cautions

- Do not create multiple root session spans for a single workflow execution
- Ensure the decorated function returns a result to complete the span

## Output Contract

- Active session span created and established as root context; all subsequent operations within the decorated function are nested under this root span; span lifecycle is tied to function execution

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Beginning a new workflow or agent session
- Starting execution that requires end-to-end operation tracking
- Initializing a new observable execution context
