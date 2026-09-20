---
id: "6ae95eca-2b03-52fc-bf4e-33e1e79c4fb6"
name: "Executor Failure Detection and Recovery"
description: "Consolidate duplicate global session object references into a single authoritative global (_client_legacy_session_for_init_trace) to prevent state corruption and initialization race conditions. Deprecate old _active_session references and migrate consumers to auto-init trace context."
version: "0.1.1"
tags:
  - "global_state"
  - "deprecation"
  - "session_management"
  - "refactoring"
  - "initialization"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Task submission attempt to an Executor"
  - "Executor may have been shut down, crashed, or entered an invalid state"
  - "Need to detect and recover gracefully from Executor failure"
---

# Executor Failure Detection and Recovery

Consolidate duplicate global session object references into a single authoritative global (_client_legacy_session_for_init_trace) to prevent state corruption and initialization race conditions. Deprecate old _active_session references and migrate consumers to auto-init trace context.

## Prompt

Audit the codebase for all global _active_session definitions and references. Verify auto-init trace context (_client_init_trace_context) is initialized. Consolidate legacy session into single global _client_legacy_session_for_init_trace. Update atexit handler to reference only the new consolidated global. Replace all old _active_session references with _client_legacy_session_for_init_trace and add deprecation warnings. Verify no active consumers depend on old global without migration path.

## Objective

eliminate_duplicate_global_state
## Applicable Signals

- duplicate global session variables detected
- initialization race conditions observed
- auto-init trace context available

## Contraindications

- active consumers still depend on old global _active_session API without migration path
- no auto-init trace context available
- legacy API consumers not yet migrated to agentops.start_trace()

## Workflow Steps

- {'step': 1, 'action': 'Audit codebase for all global _active_session definitions and references'}
- {'step': 2, 'action': 'Verify auto-init trace context (_client_init_trace_context) is initialized and accessible'}
- {'step': 3, 'action': 'Consolidate legacy session into single global _client_legacy_session_for_init_trace'}
- {'step': 4, 'action': 'Update atexit handler to reference only new consolidated global'}
- {'step': 5, 'action': 'Replace all old _active_session references with _client_legacy_session_for_init_trace'}
- {'step': 6, 'action': 'Add deprecation warnings to old API entry points'}
- {'step': 7, 'action': 'Verify no active consumers depend on old global without migration path'}

## Constraints

- must maintain backward compatibility during transition period
- atexit handler must use only new consolidated globals
- all old _active_session references must be explicitly deprecated

## Cautions

- This is an irreversible global state change; requires explicit deprecation sequencing.
- Verify all callers have migrated before removing old API.
- Test atexit handler behavior under concurrent initialization.

## Output Contract

- Single authoritative global _client_legacy_session_for_init_trace replaces all old _active_session references
- atexit handler uses only new consolidated globals
- no state corruption or initialization race conditions

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Task submission attempt to an Executor
- Executor may have been shut down, crashed, or entered an invalid state
- Need to detect and recover gracefully from Executor failure
