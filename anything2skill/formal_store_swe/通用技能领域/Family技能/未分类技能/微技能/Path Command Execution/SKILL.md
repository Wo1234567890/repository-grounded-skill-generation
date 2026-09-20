---
id: "9a735def-26bd-5987-8dc2-f353083096d9"
name: "Path Command Execution"
description: "Wraps an agent method with @operation decorator to enable automatic logging and monitoring of task execution. Use when instrumenting agent methods for observability and debugging."
version: "0.1.1"
tags:
  - "instrumentation"
  - "observability"
  - "agent"
  - "decorator"
  - "logging"
  - "debugging"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "adding a line segment to an active path"
  - "adding a curve (quadratic or cubic Bézier) to an active path"
  - "adding a circular arc to an active path"
  - "adding a rectangle to an active path"
  - "repositioning the path cursor"
examples:
  - input: "Agent class with perform_task method requiring instrumentation"
    output: "Method decorated with @operation; when called within a session, execution is logged with task details"
    notes: "Decorator captures method name, arguments, and return value automatically"
---

# Path Command Execution

Wraps an agent method with @operation decorator to enable automatic logging and monitoring of task execution. Use when instrumenting agent methods for observability and debugging.

## Prompt

Apply the @operation decorator to an agent method that performs a discrete task. The decorator automatically captures execution events and logs them to the active session. Ensure the method has clear input parameters and a return value.

## Objective

Instrument a single agent method for task execution tracking
## Applicable Signals

- Defining an agent method that performs a discrete task
- Requirement for execution visibility and observability
- Need to track task completion and intermediate steps

## Contraindications

- Task is a simple utility function without agent semantics
- Operation decorator is already applied to the method
- Method is a private helper or internal utility

## Workflow Steps

- Import or ensure @operation decorator is available from the instrumentation framework
- Apply @operation decorator directly above the agent method definition
- Verify the method has clear input parameters and a return value
- Ensure the method is called within an active @session context
- Confirm execution events are captured in the session log

## Constraints

- Decorator must be applied within an active session context to log events
- Method must be part of an agent class or callable object
- Return value should be meaningful for downstream tracking

## Cautions

- Decorator overhead may impact performance for high-frequency calls; consider batching if needed
- Ensure session is initialized before calling decorated methods

## Output Contract

- Method is decorated and callable; execution events are logged to the active session with task name, parameters, and result.

## Example Executions

### Example 1

- Input: Agent class with perform_task method requiring instrumentation
- Output: Method decorated with @operation; when called within a session, execution is logged with task details
- Notes: Decorator captures method name, arguments, and return value automatically

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- adding a line segment to an active path
- adding a curve (quadratic or cubic Bézier) to an active path
- adding a circular arc to an active path
- adding a rectangle to an active path
- repositioning the path cursor

## Examples

### Example 1

Input:

  Agent class with perform_task method requiring instrumentation

Output:

  Method decorated with @operation; when called within a session, execution is logged with task details

Notes:

  Decorator captures method name, arguments, and return value automatically
