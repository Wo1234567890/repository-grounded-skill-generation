---
id: "b4c9fc6a-1f05-51ad-b9af-555a91583de9"
name: "StreamExecutionEnvironment Setup"
description: "Compose @agent and @operation decorators in proper nesting order to establish correct parent-child span relationships and execution context hierarchy in observability instrumentation."
version: "0.1.2"
tags:
  - "observability"
  - "instrumentation"
  - "span_hierarchy"
  - "decorator_composition"
  - "agent_operations"
triggers:
  - "Starting a new Flink streaming application"
  - "Need to configure execution context before reading data sources"
  - "Initializing program foundation for DataStream operations"
examples:
  - input: "Class-based agent with multiple methods that need observability tracking"
    output: "@agent decorator on class, @operation decorators on methods, resulting in hierarchical span structure"
    notes: "Operation spans are correctly nested under agent span in observability output"
---

# StreamExecutionEnvironment Setup

Compose @agent and @operation decorators in proper nesting order to establish correct parent-child span relationships and execution context hierarchy in observability instrumentation.

## Prompt

When instrumenting class-based agents with nested methods, apply decorators in the correct nesting order: place @agent on the class definition and @operation on individual methods. This ensures that operation spans are correctly registered as children of the agent span, preserving the execution context hierarchy for observability analysis.

## Objective

Maintain correct span hierarchy in nested agent and operation contexts
## Applicable Signals

- Class-based agent definition requiring observability
- Nested method calls within agent classes
- Need for parent-child span relationship tracking

## Contraindications

- Flat, non-nested function calls without hierarchical context requirements
- Contexts where span hierarchy is not required for observability analysis
- Standalone functions that do not require parent-child span relationships

## Intervention Moves

- Apply @agent decorator to the class definition
- Apply @operation decorator to individual methods within the class
- Verify decorator nesting order matches execution hierarchy

## Workflow Steps

- {'step': 1, 'action': 'Identify the class definition that represents the agent', 'detail': 'Locate the class that contains the operations to be instrumented'}
- {'step': 2, 'action': 'Apply @agent decorator to the class definition', 'detail': 'Place @agent decorator immediately before the class keyword'}
- {'step': 3, 'action': 'Apply @operation decorator to each method requiring observability', 'detail': 'Place @operation decorator immediately before each method definition within the class'}
- {'step': 4, 'action': 'Verify span hierarchy in observability output', 'detail': 'Confirm that operation spans appear as children of the agent span in observability logs or traces'}

## Constraints

- Decorators must be applied in correct nesting order: @agent on class, @operation on methods
- Parent decorator (@agent) must wrap the class before child decorators (@operation) are applied to methods
- Execution context must support decorator composition

## Cautions

- Incorrect decorator order will result in flat span structure instead of hierarchical relationships
- Missing decorators on nested methods will break span hierarchy chain
- Verify observability output to confirm parent-child span relationships are established

## Output Contract

- Properly nested decorators that produce correct parent-child span relationships in observability output, with operation spans registered as children of agent spans.

## Example Therapist Responses

### Example 1

- Client/Input: Class-based agent with multiple methods that need observability tracking
- Therapist/Output: @agent decorator on class, @operation decorators on methods, resulting in hierarchical span structure
- Notes: Operation spans are correctly nested under agent span in observability output

## Triggers

- Starting a new Flink streaming application
- Need to configure execution context before reading data sources
- Initializing program foundation for DataStream operations

## Examples

### Example 1

Input:

  Class-based agent with multiple methods that need observability tracking

Output:

  @agent decorator on class, @operation decorators on methods, resulting in hierarchical span structure

Notes:

  Operation spans are correctly nested under agent span in observability output
