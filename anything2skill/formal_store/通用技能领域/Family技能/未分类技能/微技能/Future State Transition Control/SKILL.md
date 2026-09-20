---
id: "157ba223-e016-562c-b401-649bc2bf7959"
name: "Future State Transition Control"
description: "Synchronize current session and trace context state to legacy module globals for backward compatibility. Handles ImportError gracefully when legacy module is unavailable."
version: "0.1.1"
tags:
  - "backward_compatibility"
  - "state_sync"
  - "legacy_integration"
  - "initialization"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Executor implementation completes a parallel task and must record outcome"
  - "Unit test harness needs to simulate task completion"
  - "Parallel task result or exception is ready to be stored"
---

# Future State Transition Control

Synchronize current session and trace context state to legacy module globals for backward compatibility. Handles ImportError gracefully when legacy module is unavailable.

## Prompt

After client initialization completes with auto_start_session=True, update the legacy module's _current_session and _current_trace_context globals to match the client's internal state. Wrap the import and assignment in a try-except block to gracefully handle cases where the legacy module is not available.

## Objective

Ensure legacy code paths access consistent session state
## Applicable Signals

- Initialization phase entry with backward compatibility flag enabled
- Presence of legacy code paths in the codebase

## Contraindications

- Legacy module is not imported or not available
- Backward compatibility is not needed
- Direct session passing is preferred over global state mutation

## Workflow Steps

- {'step': 1, 'action': 'Attempt to import agentops.legacy module', 'condition': 'Within try block'}
- {'step': 2, 'action': 'Assign self._legacy_session_for_init_trace to agentops.legacy._current_session', 'condition': 'Import succeeds'}
- {'step': 3, 'action': 'Assign self._init_trace_context to agentops.legacy._current_trace_context', 'condition': 'Import succeeds'}
- {'step': 4, 'action': 'Catch ImportError and pass silently', 'condition': 'Legacy module not available'}

## Constraints

- Must execute after internal _legacy_session_for_init_trace and _init_trace_context are set
- ImportError must be caught and suppressed (legacy module absence is acceptable)
- State assignment must occur before returning from initialization

## Cautions

- Direct access to another module's globals is not ideal; prefer explicit calls if possible
- ImportError suppression should be logged at debug level for troubleshooting

## Output Contract

- agentops.legacy._current_session and agentops.legacy._current_trace_context are set to match client's internal state when legacy module is available; ImportError is caught and execution continues without failure

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Executor implementation completes a parallel task and must record outcome
- Unit test harness needs to simulate task completion
- Parallel task result or exception is ready to be stored
