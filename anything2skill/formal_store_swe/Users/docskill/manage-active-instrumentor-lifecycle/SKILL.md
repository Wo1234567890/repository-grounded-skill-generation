---
id: "0d976330-bcf0-57fd-96db-19a0cfb1e9a5"
name: "Manage Active Instrumentor Lifecycle"
description: "Track and maintain the list of active BaseInstrumentor instances during runtime, enabling selective activation, deactivation, and cleanup of instrumentation for monitored packages."
version: "0.1.0"
tags:
  - "instrumentation"
  - "lifecycle_management"
  - "state_tracking"
  - "runtime_monitoring"
  - "cleanup"
triggers:
  - "instrumentation initialization phase"
  - "new package import detected during runtime"
  - "shutdown or cleanup signal received"
examples:
  - input: "Import hook detects new target package during runtime"
    output: "New BaseInstrumentor created, initialized, and appended to _active_instrumentors; instrumentation active for that package"
    notes: "Assumes package is in TARGET_PACKAGES and not already instrumented"
  - input: "Shutdown signal received"
    output: "_active_instrumentors iterated, cleanup called on each instrumentor, list cleared"
    notes: "Cleanup must be idempotent to handle partial failures"
---

# Manage Active Instrumentor Lifecycle

Track and maintain the list of active BaseInstrumentor instances during runtime, enabling selective activation, deactivation, and cleanup of instrumentation for monitored packages.

## Prompt

Maintain the _active_instrumentors module-level list as the single source of truth for all currently active instrumentation instances. On initialization, populate this list with BaseInstrumentor instances for target packages. When adding new instrumentors during import hooks, append to the list and initialize. On shutdown or cleanup, iterate the list, call cleanup methods on each instrumentor, and clear the list. Ensure thread-safe access if instrumentation occurs across multiple threads.

## Objective

maintain_instrumentation_state
## Applicable Signals

- module import hook triggered
- target package detected in TARGET_PACKAGES set
- instrumentation manager instantiation
- cleanup or teardown phase initiated

## Contraindications

- instrumentation is globally disabled
- no packages in TARGET_PACKAGES require monitoring
- instrumentor instances are managed externally by caller
- agentic library detection is incomplete or failed

## Workflow Steps

- {'step': 1, 'action': 'Initialize _active_instrumentors as empty list at module load', 'condition': 'Module is loaded for first time'}
- {'step': 2, 'action': 'On import hook or package detection, create BaseInstrumentor instance for target package', 'condition': 'Package is in TARGET_PACKAGES and not already instrumented'}
- {'step': 3, 'action': 'Call instrumentor.instrument() or equivalent initialization method', 'condition': 'Instrumentor instance created successfully'}
- {'step': 4, 'action': 'Append initialized instrumentor to _active_instrumentors list', 'condition': 'Initialization completed without error'}
- {'step': 5, 'action': 'On shutdown signal, iterate _active_instrumentors and call cleanup on each', 'condition': 'Shutdown or cleanup phase initiated'}
- {'step': 6, 'action': 'Clear _active_instrumentors list after all cleanups complete', 'condition': 'All instrumentors cleaned up successfully'}

## Constraints

- Must use module-level _active_instrumentors list as single source of truth
- All BaseInstrumentor instances must be properly initialized before adding to list
- Cleanup must be idempotent and handle already-removed instrumentors gracefully
- Do not create a centralized InstrumentationManager instance; rely on list-based state

## Cautions

- Concurrent import hooks may attempt simultaneous list modifications; use locking if multi-threaded
- Removing an instrumentor without calling cleanup may leave dangling hooks or references
- Clearing the list without notifying dependent code may cause orphaned instrumentation

## Output Contract

- _active_instrumentors list reflects the current set of active BaseInstrumentor instances
- All instrumentors are properly initialized on addition and fully cleaned up on removal
- List is empty after shutdown
- No dangling or orphaned instrumentor references remain

## Example Executions

### Example 1

- Input: Import hook detects new target package during runtime
- Output: New BaseInstrumentor created, initialized, and appended to _active_instrumentors; instrumentation active for that package
- Notes: Assumes package is in TARGET_PACKAGES and not already instrumented

### Example 2

- Input: Shutdown signal received
- Output: _active_instrumentors iterated, cleanup called on each instrumentor, list cleared
- Notes: Cleanup must be idempotent to handle partial failures

## Triggers

- instrumentation initialization phase
- new package import detected during runtime
- shutdown or cleanup signal received

## Examples

### Example 1

Input:

  Import hook detects new target package during runtime

Output:

  New BaseInstrumentor created, initialized, and appended to _active_instrumentors; instrumentation active for that package

Notes:

  Assumes package is in TARGET_PACKAGES and not already instrumented

### Example 2

Input:

  Shutdown signal received

Output:

  _active_instrumentors iterated, cleanup called on each instrumentor, list cleared

Notes:

  Cleanup must be idempotent to handle partial failures
