---
id: "c760e181-5ed7-50d6-906d-c4ccabd12c56"
name: "Nested Operation Execution Tracking"
description: "Track and record execution flow when decorated operations call other decorated operations, preserving call hierarchy and state across nesting levels."
version: "0.1.0"
tags:
  - "observability"
  - "instrumentation"
  - "call_graph_tracking"
  - "nested_execution"
  - "debugging"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Agent code contains nested operation calls (e.g., main_operation calling nested_operation)"
  - "Full call chain visibility is needed for debugging or audit purposes"
  - "Decorated functions invoke other decorated functions within the same workflow"
examples:
  - input: "Agent with @operation decorated main_operation calling @operation decorated nested_operation(\"test message\")"
    output: "Call log shows: main_operation → nested_operation with inputs/outputs linked and execution time for each level"
    notes: "Parent-child relationship preserved; both operations' I/O recorded separately"
---

# Nested Operation Execution Tracking

Track and record execution flow when decorated operations call other decorated operations, preserving call hierarchy and state across nesting levels.

## Prompt

When a decorated operation invokes another decorated operation, ensure the call chain is captured with parent-child relationships. Record each nested call's inputs, outputs, and exceptions individually, linking them to their parent operation. Use decorator metadata to maintain call hierarchy without manual intervention.

## Objective

Maintain observability across nested function calls within instrumented agent workflows
## Applicable Signals

- Nested decorated function call detected
- Parent operation context is active
- Child operation begins execution

## Contraindications

- Only top-level operation visibility is required
- Decorator overhead for deeply nested calls is unacceptable
- Operations are dynamically generated or reflection-based
- Call chain recording would violate privacy or performance constraints

## Intervention Moves

- Capture parent operation context before child invocation
- Record child operation inputs and link to parent
- Log child operation outputs and exceptions with parent reference
- Maintain call stack depth and hierarchy metadata

## Workflow Steps

- {'step': 1, 'action': 'Detect decorated operation invocation', 'detail': 'Identify when a decorated function calls another decorated function'}
- {'step': 2, 'action': 'Capture parent context', 'detail': "Store current operation's execution context (ID, inputs, state)"}
- {'step': 3, 'action': 'Record child invocation', 'detail': 'Log child operation name, inputs, and parent reference'}
- {'step': 4, 'action': 'Execute child operation', 'detail': 'Allow child operation to run with parent context available'}
- {'step': 5, 'action': 'Capture child results', 'detail': 'Record child operation outputs, exceptions, and execution metadata'}
- {'step': 6, 'action': 'Link results to parent', 'detail': 'Associate child results with parent operation in call hierarchy'}
- {'step': 7, 'action': 'Return to parent context', 'detail': 'Restore parent operation state and continue execution'}

## Constraints

- Decorator must be applied to all operations in the call chain for full tracking
- Parent operation context must remain accessible during child execution
- Exception handling must preserve parent-child linkage even on failure

## Cautions

- Deep nesting levels may increase memory overhead; monitor call stack depth
- Ensure decorator order does not interfere with other instrumentation
- Verify that nested call recording does not introduce circular references

## Output Contract

- Call hierarchy is recorded with parent-child relationships; each nested call's inputs, outputs, and exceptions are individually logged and linked to their parent operation. The complete call chain is available for inspection, debugging, and audit purposes.

## Example Therapist Responses

### Example 1

- Client/Input: Agent with @operation decorated main_operation calling @operation decorated nested_operation("test message")
- Therapist/Output: Call log shows: main_operation → nested_operation with inputs/outputs linked and execution time for each level
- Notes: Parent-child relationship preserved; both operations' I/O recorded separately

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Agent code contains nested operation calls (e.g., main_operation calling nested_operation)
- Full call chain visibility is needed for debugging or audit purposes
- Decorated functions invoke other decorated functions within the same workflow

## Examples

### Example 1

Input:

  Agent with @operation decorated main_operation calling @operation decorated nested_operation("test message")

Output:

  Call log shows: main_operation → nested_operation with inputs/outputs linked and execution time for each level

Notes:

  Parent-child relationship preserved; both operations' I/O recorded separately
