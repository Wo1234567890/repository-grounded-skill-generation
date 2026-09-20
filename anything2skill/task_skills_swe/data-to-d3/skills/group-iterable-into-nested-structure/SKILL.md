---
id: "64a5ce52-07a9-52f9-808d-dbdc2659a314"
name: "Group iterable into nested structure"
description: "Structure decorator nesting (e.g., @agent containing @operation) to create proper parent-child span relationships in observability traces, ensuring execution hierarchy is accurately reflected in debugging output."
version: "0.1.1"
tags:
  - "observability"
  - "instrumentation"
  - "span_hierarchy"
  - "decorator"
  - "tracing"
  - "debugging"
triggers:
  - "Input is an iterable; you need to organize values by one or more discrete keys; output should be nested Map or array."
examples:
  - input: "Agent class with multiple internal operations"
    output: "Hierarchical trace with agent span as parent and operation spans as children"
    notes: "Decorator nesting creates proper parent-child relationships in observability output"
---

# Group iterable into nested structure

Structure decorator nesting (e.g., @agent containing @operation) to create proper parent-child span relationships in observability traces, ensuring execution hierarchy is accurately reflected in debugging output.

## Prompt

Apply decorator nesting to establish correct span parent-child relationships. Use @agent on a class and @operation on its methods to create hierarchical traces. Ensure each nested decorator is applied in the correct order so that child operations are properly linked to parent spans.

## Objective

Establish correct span parent-child relationships through proper decorator nesting
## Applicable Signals

- Presence of nested function or method structures
- Need for hierarchical observability traces
- Agent class with internal operations

## Contraindications

- Flat function structures without nesting
- When span hierarchy is not required for debugging
- Single-level function calls without parent-child relationships

## Workflow Steps

- {'step': 1, 'action': 'Import required decorators', 'detail': 'from agentops.sdk.decorators import agent, operation'}
- {'step': 2, 'action': 'Apply @agent decorator to class', 'detail': 'Decorate the parent class or scope with @agent'}
- {'step': 3, 'action': 'Apply @operation decorator to nested methods', 'detail': 'Decorate child methods or functions within the agent with @operation'}
- {'step': 4, 'action': 'Verify span hierarchy in trace output', 'detail': 'Confirm that child operations appear as nested spans under parent agent span'}

## Constraints

- Decorators must be applied in correct nesting order (parent decorator on outer scope, child decorator on inner scope)
- Child operations must be methods or functions within the parent-decorated scope

## Cautions

- Incorrect decorator order will produce flat or inverted span hierarchies
- Ensure decorator imports are available from agentops.sdk.decorators

## Output Contract

- Correctly nested decorators producing hierarchical span traces where child operations are properly linked to parent spans, visible in observability dashboards and debugging tools.

## Example Executions

### Example 1

- Input: Agent class with multiple internal operations
- Output: Hierarchical trace with agent span as parent and operation spans as children
- Notes: Decorator nesting creates proper parent-child relationships in observability output

## Triggers

- Input is an iterable; you need to organize values by one or more discrete keys; output should be nested Map or array.

## Examples

### Example 1

Input:

  Agent class with multiple internal operations

Output:

  Hierarchical trace with agent span as parent and operation spans as children

Notes:

  Decorator nesting creates proper parent-child relationships in observability output
