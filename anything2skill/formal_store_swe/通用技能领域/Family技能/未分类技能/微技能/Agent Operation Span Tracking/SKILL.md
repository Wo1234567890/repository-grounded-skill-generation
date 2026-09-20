---
id: "7b643d32-9ba8-5dcc-accc-a035b57be10f"
name: "Agent Operation Span Tracking"
description: "Decorator-based pattern to create an agent span for tracking individual agent operations and decisions within a session. Use when instrumenting specific agent actions or tool invocations to capture operation metadata and outcomes as distinct observability records."
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
  - "Instrumenting agent-level actions, tool calls, or decision points that need separate observability records"
examples:
  - input: "A function performing a discrete agent decision or tool call"
    output: "Child span created under session span; operation metadata logged to observability backend"
    notes: "Decorator handles span lifecycle automatically; no manual span management required"
---

# Agent Operation Span Tracking

Decorator-based pattern to create an agent span for tracking individual agent operations and decisions within a session. Use when instrumenting specific agent actions or tool invocations to capture operation metadata and outcomes as distinct observability records.

## Prompt

Apply the @agent decorator from agentops.sdk.decorators to a function or method that performs a discrete agent operation. The decorator will automatically create a child span nested under the active session span, capturing the operation's execution context, inputs, and results. Ensure the decorated function is called within an active session context.

## Objective

Track and observe individual agent operations as distinct spans nested under a session
## Applicable Signals

- Agent-level action execution
- Tool invocation or function call requiring observability
- Decision point or branching logic in agent workflow
- Need for separate operation-level telemetry within a session

## Contraindications

- Do not use for low-level utility functions unrelated to agent semantics
- Do not use outside an active session span context
- Do not use for operations that should not be separately tracked

## Intervention Moves

- Import @agent decorator from agentops.sdk.decorators
- Apply @agent decorator to the target function or method
- Ensure function executes within an active session context
- Return operation result; span closure is automatic

## Constraints

- Requires active session span (created via @session decorator)
- Function must be called within session execution scope
- Decorator must be imported from agentops.sdk.decorators

## Cautions

- Ensure session is initialized before invoking decorated agent operations
- Excessive span creation may impact observability overhead; use judiciously for semantically distinct operations

## Output Contract

- A decorated agent function that automatically creates and closes a child span under the session, with operation metadata (inputs, outputs, execution time, errors) captured in observability records.

## Example Executions

### Example 1

- Input: A function performing a discrete agent decision or tool call
- Output: Child span created under session span; operation metadata logged to observability backend
- Notes: Decorator handles span lifecycle automatically; no manual span management required

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Instrumenting agent-level actions, tool calls, or decision points that need separate observability records

## Examples

### Example 1

Input:

  A function performing a discrete agent decision or tool call

Output:

  Child span created under session span; operation metadata logged to observability backend

Notes:

  Decorator handles span lifecycle automatically; no manual span management required
