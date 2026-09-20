---
id: "e3893ef5-8d06-5356-8a44-7ed3b1cca418"
name: "Nested Operation Execution Pattern"
description: "Structure agent operations as nested method calls where parent operations invoke child operations, enabling hierarchical observability and execution tracing."
version: "0.1.0"
tags:
  - "observability"
  - "operation_composition"
  - "hierarchical_execution"
  - "agent_instrumentation"
  - "tracing"
triggers:
  - "Agent logic requires multi-level operation calls"
  - "Need to trace execution hierarchy from parent to child operations"
  - "Operations are composed hierarchically within a session"
examples:
  - input: "Parent operation main_operation() calls child operation nested_operation('test message')"
    output: "Result from nested_operation returned to parent; both operations logged with parent→child relationship in observability trace"
    notes: "Demonstrates single-level nesting with argument passing and result capture"
---

# Nested Operation Execution Pattern

Structure agent operations as nested method calls where parent operations invoke child operations, enabling hierarchical observability and execution tracing.

## Prompt

Execute a parent operation that calls one or more child operations. Ensure the parent method is decorated with @operation, invokes child operations via self.child_operation(...), captures the result, and returns it. Both parent and child calls will be automatically recorded in the observability log with full hierarchy tracing.

## Objective

Execute and trace nested operation calls within a single agent session
## Applicable Signals

- Parent operation method decorated with @operation
- Child operation invoked via self.child_operation_name(...)
- Result capture and return from parent method

## Contraindications

- Operations are independent and do not require hierarchical tracing
- Circular dependencies exist between operations
- Child operations should not be invoked from outside the parent context

## Workflow Steps

- {'step': 1, 'action': 'Define parent operation method with @operation decorator', 'detail': 'Ensure method is part of agent class and decorated with @operation'}
- {'step': 2, 'action': 'Invoke child operation via self.child_operation_name(args)', 'detail': 'Pass required arguments; child must also be decorated with @operation'}
- {'step': 3, 'action': 'Capture result from child operation call', 'detail': 'Store return value in a variable for further processing or return'}
- {'step': 4, 'action': 'Return result from parent operation', 'detail': 'Complete parent method execution; observability system records both levels'}

## Constraints

- Parent operation must be a method within an agent class
- Child operations must be accessible via self reference
- Both parent and child must use @operation decorator for full tracing

## Cautions

- Ensure no circular invocation patterns (parent → child → parent)
- Verify child operation signatures match invocation arguments
- Monitor execution depth to avoid stack overflow in deeply nested calls

## Output Contract

- Parent operation completes with child operation result returned and both levels recorded in observability log with full execution hierarchy and timing metadata.

## Example Executions

### Example 1

- Input: Parent operation main_operation() calls child operation nested_operation('test message')
- Output: Result from nested_operation returned to parent; both operations logged with parent→child relationship in observability trace
- Notes: Demonstrates single-level nesting with argument passing and result capture

## Triggers

- Agent logic requires multi-level operation calls
- Need to trace execution hierarchy from parent to child operations
- Operations are composed hierarchically within a session

## Examples

### Example 1

Input:

  Parent operation main_operation() calls child operation nested_operation('test message')

Output:

  Result from nested_operation returned to parent; both operations logged with parent→child relationship in observability trace

Notes:

  Demonstrates single-level nesting with argument passing and result capture
