---
id: "8036b7a9-9c9e-535d-b2c8-404d00f02612"
name: "Session Span Initialization"
description: "Decorator-based pattern to create a root session span that wraps and tracks all nested operations within a workflow function. Use when starting observability instrumentation for an agent workflow."
version: "0.1.0"
tags:
  - "observability"
  - "instrumentation"
  - "decorator"
  - "session_tracking"
  - "agent_workflow"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Starting a new agent workflow or task that requires end-to-end observability tracking"
examples:
  - input: "A workflow function that performs agent operations"
    output: "Function decorated with @session, creating a root span that tracks all nested operations"
    notes: "The decorator transparently wraps the function without changing its signature or return behavior"
---

# Session Span Initialization

Decorator-based pattern to create a root session span that wraps and tracks all nested operations within a workflow function. Use when starting observability instrumentation for an agent workflow.

## Prompt

Apply the @session decorator to a workflow function to initialize a root session span. This span serves as the container for all downstream observability spans and operations. The decorated function will automatically track all nested calls and operations under this session context.

## Objective

Initialize a session span as the root container for all downstream observability spans
## Applicable Signals

- Starting a new agent workflow or task
- Requiring end-to-end observability tracking
- Need to establish a root observability container

## Contraindications

- Instrumenting individual function calls or micro-operations that do not represent a complete workflow session
- Operations that are already nested under an existing session span

## Workflow Steps

- Import the session decorator from agentops.sdk.decorators
- Apply @session decorator to the workflow function
- Place all workflow code inside the decorated function
- Return the result from the function

## Constraints

- The @session decorator must be imported from agentops.sdk.decorators
- The decorated function must be the entry point for the workflow
- All nested operations should be called within the decorated function scope

## Output Contract

- A decorated function that creates and manages a session span context, with all nested operations automatically tracked under that span. The function executes normally and returns its result while maintaining observability instrumentation.

## Example Executions

### Example 1

- Input: A workflow function that performs agent operations
- Output: Function decorated with @session, creating a root span that tracks all nested operations
- Notes: The decorator transparently wraps the function without changing its signature or return behavior

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Starting a new agent workflow or task that requires end-to-end observability tracking

## Examples

### Example 1

Input:

  A workflow function that performs agent operations

Output:

  Function decorated with @session, creating a root span that tracks all nested operations

Notes:

  The decorator transparently wraps the function without changing its signature or return behavior
