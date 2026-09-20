---
id: "78bc835d-8aaf-5956-93db-9f22c46d5a61"
name: "Async and Generator Function Instrumentation"
description: "Enable observability decorators to correctly instrument async/await and generator functions, capturing execution state at each await or yield boundary without introducing performance overhead or altering function semantics."
version: "0.1.0"
tags:
  - "observability"
  - "instrumentation"
  - "async"
  - "generator"
  - "decorator"
  - "execution_tracking"
triggers:
  - "Agent operation uses async/await syntax"
  - "Function contains yield or yield from statements"
  - "Observability must capture intermediate states or streaming outputs"
---

# Async and Generator Function Instrumentation

Enable observability decorators to correctly instrument async/await and generator functions, capturing execution state at each await or yield boundary without introducing performance overhead or altering function semantics.

## Prompt

Apply decorators to async functions and generators to record input/output and exceptions at each suspension point. Ensure the decorator preserves the original function's async or generator semantics and does not block or alter control flow.

## Objective

Extend observability to asynchronous and streaming execution patterns
## Applicable Signals

- async def function signature detected
- generator function (contains yield) detected
- caller requires state snapshots at suspension boundaries

## Contraindications

- Synchronous-only operations where async overhead is unacceptable
- Generator state snapshots are not required or not feasible
- Decorator must not introduce latency or change function semantics

## Workflow Steps

- {'step': 1, 'action': 'Detect function type (async, generator, or synchronous)', 'detail': 'Inspect function signature and bytecode for async def or yield keywords'}
- {'step': 2, 'action': 'Wrap async functions with async decorator', 'detail': 'Preserve await chain; record input, output, and exceptions at each await boundary'}
- {'step': 3, 'action': 'Wrap generator functions with generator-aware decorator', 'detail': 'Capture state at each yield; record input to next() and output from yield'}
- {'step': 4, 'action': 'Record execution metadata', 'detail': 'Log suspension points, resumption points, and any exceptions raised during iteration'}
- {'step': 5, 'action': 'Return instrumented function with original semantics intact', 'detail': 'Caller receives async coroutine or generator object; no behavioral changes'}

## Constraints

- Decorator must preserve async/await semantics and not block execution
- Generator yields must be captured without consuming or modifying the yielded value
- Exception handling must work across await and yield boundaries

## Cautions

- Async instrumentation may introduce subtle timing changes; test with concurrent workloads
- Generator state snapshots can increase memory usage for long-running generators; monitor resource consumption

## Output Contract

- Async function completes with full await chain recorded in observability log; generator yields are captured with execution state at each suspension and resumption boundary. All exceptions are logged with context.

## Triggers

- Agent operation uses async/await syntax
- Function contains yield or yield from statements
- Observability must capture intermediate states or streaming outputs
