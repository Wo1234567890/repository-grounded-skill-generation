---
id: "df5ba5a4-e5af-5af4-9d48-740d751e9ca4"
name: "Decorate Workflow Function with Trace Metadata"
description: "Apply @trace decorator to a function with name and tags parameters to mark it as a traced workflow unit. Captures workflow execution context and enables filtering by metadata such as environment tags."
version: "0.1.0"
tags:
  - "tracing"
  - "instrumentation"
  - "observability"
  - "decorator"
  - "workflow"
  - "metadata"
triggers:
  - "You want to trace a specific workflow function and attach metadata such as workflow name and environment tags (e.g., production, staging)"
examples:
  - input: "Function my_workflow() with no decorator"
    output: "@trace(name=\"my-workflow\", tags=[\"production\"]) applied; function now emits trace events"
    notes: "Decorator captures workflow name and production environment tag"
---

# Decorate Workflow Function with Trace Metadata

Apply @trace decorator to a function with name and tags parameters to mark it as a traced workflow unit. Captures workflow execution context and enables filtering by metadata such as environment tags.

## Prompt

Use the @trace decorator from agentops.sdk.decorators on a function definition. Provide a name parameter (string) to identify the workflow and a tags parameter (list of strings) to attach metadata such as environment or execution context. The decorator will instrument the function to emit trace events on invocation.

## Objective

Annotate a function with tracing metadata for observability and filtering
## Applicable Signals

- Function requires workflow-level observability
- Need to attach environment or execution context tags
- Workflow execution must be filterable by metadata

## Contraindications

- Function is a utility or helper with no observable workflow semantics
- Tracing overhead is unacceptable for high-frequency calls
- Function does not represent a discrete workflow unit

## Intervention Moves

- Import @trace from agentops.sdk.decorators
- Apply @trace decorator above function definition
- Set name parameter to workflow identifier
- Set tags parameter to list of metadata strings

## Workflow Steps

- Import @trace decorator from agentops.sdk.decorators
- Define or identify the function to be traced
- Apply @trace decorator with name and tags arguments
- Verify function executes and emits trace events

## Constraints

- agentops SDK must be initialized before decorator is applied
- name parameter must be a non-empty string
- tags parameter must be a list of strings

## Cautions

- Decorator adds runtime overhead; use only for workflow-level functions
- Trace events are emitted on every function invocation

## Output Contract

- Function is decorated and will emit trace events with specified name and tags on each invocation. Trace metadata becomes available for filtering and observability downstream.

## Example Executions

### Example 1

- Input: Function my_workflow() with no decorator
- Output: @trace(name="my-workflow", tags=["production"]) applied; function now emits trace events
- Notes: Decorator captures workflow name and production environment tag

## Triggers

- You want to trace a specific workflow function and attach metadata such as workflow name and environment tags (e.g., production, staging)

## Examples

### Example 1

Input:

  Function my_workflow() with no decorator

Output:

  @trace(name="my-workflow", tags=["production"]) applied; function now emits trace events

Notes:

  Decorator captures workflow name and production environment tag
