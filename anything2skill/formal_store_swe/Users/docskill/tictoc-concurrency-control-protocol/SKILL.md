---
id: "cdd22de9-5de9-5117-acad-5df117ce2e82"
name: "TicToc Concurrency Control Protocol"
description: "Multi-stage protocol for building reusable API instrumentation modules that wrap third-party service calls with consistent error handling, async support, and semantic attribute capture. Establishes a cross-phase workflow from design through testing to ensure instrumentation consistency across multiple service integrations."
version: "0.1.0"
tags:
  - "instrumentation"
  - "api_integration"
  - "observability"
  - "protocol"
  - "wrapper_pattern"
  - "async_support"
triggers:
  - "High-concurrency OLTP workload detected"
  - "Variable contention levels across transaction mix"
  - "Need to compare concurrency control protocols"
  - "In-memory database transaction management required"
examples:
  - input: "Transaction T1 reads items {A, B} at timestamp 100; concurrent transaction T2 writes to item A at timestamp 105"
    output: "T1 validation fails at step 2 (conflict detected on A); T1 aborts and returns retry signal to caller"
    notes: "Demonstrates conflict detection and abort mechanism"
  - input: "Transaction T3 reads items {C, D} at timestamp 200; no concurrent writes to C or D before commit"
    output: "T3 validation succeeds; commits at timestamp 210 with serializable guarantee; throughput incremented"
    notes: "Demonstrates successful commit path"
---

# TicToc Concurrency Control Protocol

Multi-stage protocol for building reusable API instrumentation modules that wrap third-party service calls with consistent error handling, async support, and semantic attribute capture. Establishes a cross-phase workflow from design through testing to ensure instrumentation consistency across multiple service integrations.

## Prompt

When building a new instrumentor for an external API service, follow these six stages in sequence:
1. Use Common Utilities: Leverage the common module for consistency across instrumentors
2. Follow Semantic Conventions: Apply attributes from the semantic conventions module
3. Handle Errors Gracefully: Wrap operations in try-except blocks to prevent instrumentation from breaking the wrapped service
4. Support Async: Provide both sync and async method wrapping to match the service's API surface
5. Document Attributes: Comment on what attributes are captured by each instrumentation point
6. Test Thoroughly: Write unit tests for your instrumentor to verify behavior
Reference the examples/ directory for usage patterns of each instrumentor type.

## Objective

Establish a cross-phase instrumentation workflow from design through testing
## Applicable Signals

- New API service integration required
- Multiple instrumentors being developed in parallel
- Requirement for both sync and async method support

## Contraindications

- Instrumenting internal-only functions without external API calls
- No async/sync dual support needed
- Single one-off wrapper required without reuse intent

## Workflow Steps

- {'step': 1, 'name': 'Use Common Utilities', 'action': 'Leverage the common module for consistency', 'guardrail': 'All utility imports must come from the designated common module'}
- {'step': 2, 'name': 'Follow Semantic Conventions', 'action': 'Use attributes from the semantic conventions module', 'guardrail': 'Attribute names and types must conform to the conventions specification'}
- {'step': 3, 'name': 'Handle Errors Gracefully', 'action': 'Wrap operations in try-except blocks', 'guardrail': 'Instrumentation errors must not propagate to the wrapped service; log and continue'}
- {'step': 4, 'name': 'Support Async', 'action': 'Provide both sync and async method wrapping', 'guardrail': 'Async variants must maintain the same instrumentation semantics as sync variants'}
- {'step': 5, 'name': 'Document Attributes', 'action': 'Comment on what attributes are captured', 'guardrail': 'Each instrumentation point must have inline documentation of captured attributes'}
- {'step': 6, 'name': 'Test Thoroughly', 'action': 'Write unit tests for your instrumentor', 'guardrail': 'Unit tests must cover both sync and async paths, error cases, and attribute capture'}

## Constraints

- All instrumentation must use common utilities module for consistency
- Semantic conventions must be applied from the designated conventions module
- Error handling must not propagate instrumentation failures to the wrapped service
- Both sync and async variants must be provided when the service supports both

## Cautions

- Instrumentation overhead should be monitored; avoid capturing excessive attributes that degrade performance
- Error handling must be defensive to prevent instrumentation from breaking service availability
- Async support requires careful handling of context propagation and thread safety

## Output Contract

- Completed instrumentor module with: (1) sync and async method wrapping for all service methods, (2) error handling that prevents instrumentation failures from breaking the service, (3) semantic attributes documented inline, (4) unit tests passing for all code paths, (5) integration with common utilities and semantic conventions modules

## Triggers

- High-concurrency OLTP workload detected
- Variable contention levels across transaction mix
- Need to compare concurrency control protocols
- In-memory database transaction management required

## Examples

### Example 1

Input:

  Transaction T1 reads items {A, B} at timestamp 100; concurrent transaction T2 writes to item A at timestamp 105

Output:

  T1 validation fails at step 2 (conflict detected on A); T1 aborts and returns retry signal to caller

Notes:

  Demonstrates conflict detection and abort mechanism

### Example 2

Input:

  Transaction T3 reads items {C, D} at timestamp 200; no concurrent writes to C or D before commit

Output:

  T3 validation succeeds; commits at timestamp 210 with serializable guarantee; throughput incremented

Notes:

  Demonstrates successful commit path
