---
id: "b5de5819-3d08-5d50-b05e-8fded801a679"
name: "Agent Operation Span Tracking"
description: "Decorator-based pattern to create an agent span for tracking agent-specific operations and decisions within a session. Use when instrumenting agent behavior for observability."
version: "0.1.0"
tags:
  - "observability"
  - "instrumentation"
  - "decorator"
  - "agent_tracking"
  - "span_management"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Wrapping agent methods or decision points to capture agent behavior"
  - "Need to log agent-specific operations within an active session"
  - "Instrumenting agent state transitions or decisions for observability"
---

# Agent Operation Span Tracking

Decorator-based pattern to create an agent span for tracking agent-specific operations and decisions within a session. Use when instrumenting agent behavior for observability.

## Prompt

Apply the @agent decorator from agentops.sdk.decorators to wrap agent methods or decision points. The decorator creates a span nested under the active session span, capturing agent-level operations and state changes with full context.

## Objective

Track agent-level operations and state changes
## Applicable Signals

- Agent method invocation
- Agent decision point reached
- Active session span exists

## Contraindications

- Tracking non-agent functions; use function or tool spans instead
- Tracking external tool calls; use tool spans instead
- No active session span; create session span first

## Workflow Steps

- Import @agent decorator from agentops.sdk.decorators
- Apply @agent decorator to the target agent method or function
- Invoke the decorated method within an active session context
- Agent span is automatically created and nested under session span
- Agent operations are logged with full context

## Constraints

- Must be applied within an active session context
- Decorator must be imported from agentops.sdk.decorators
- Agent span will be nested under the parent session span

## Cautions

- Ensure session span is created before applying agent span decorator
- Do not use for non-agent function instrumentation

## Output Contract

- Agent span created and nested under session span; agent operations logged with context; span lifecycle managed automatically by decorator

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Wrapping agent methods or decision points to capture agent behavior
- Need to log agent-specific operations within an active session
- Instrumenting agent state transitions or decisions for observability
