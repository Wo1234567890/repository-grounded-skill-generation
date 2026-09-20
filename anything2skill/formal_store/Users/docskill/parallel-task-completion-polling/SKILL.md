---
id: "ee42057a-3ada-5055-9c21-aa1f0645e482"
name: "Parallel Task Completion Polling"
description: "Initialize AgentOps client with optional automatic session and trace startup. Configures internal state, optionally starts tracing, and returns a session handle or None based on auto_start_session setting."
version: "0.1.2"
tags:
  - "initialization"
  - "session_management"
  - "auto_trace"
  - "backward_compatibility"
  - "client_setup"
triggers:
  - "Caller submits multiple tasks to an Executor and needs to block until one or more reach a terminal state"
  - "Timeout or early-exit strategy is required to avoid indefinite blocking"
  - "Caller must partition results into completed and pending sets for downstream handling"
---

# Parallel Task Completion Polling

Initialize AgentOps client with optional automatic session and trace startup. Configures internal state, optionally starts tracing, and returns a session handle or None based on auto_start_session setting.

## Prompt

1. Check if auto_start_session is enabled in configuration.
2. If enabled: initialize legacy session wrapper, set trace context, mark client as initialized, and return the legacy session object.
3. If disabled: mark client as initialized without starting trace, and return None.
4. Ensure backward compatibility by updating legacy module globals when auto-trace is active.

## Objective

Set up client with configurable auto-trace behavior and return appropriate session handle
## Applicable Signals

- Client constructor invoked with auto_start_session=True or False
- Initialization phase of client lifecycle

## Contraindications

- Do not use if client is already initialized; use configure() for post-init updates instead
- Do not invoke multiple times on same client instance

## Workflow Steps

- {'step': 1, 'action': 'Check auto_start_session configuration flag'}
- {'step': 2, 'action': 'If auto_start_session is True: initialize legacy session wrapper and trace context'}
- {'step': 3, 'action': 'Attempt to update legacy module globals for backward compatibility; catch ImportError if legacy module unavailable'}
- {'step': 4, 'action': 'Set self._initialized = True'}
- {'step': 5, 'action': 'Return legacy session wrapper if auto_start_session=True; return None otherwise'}

## Constraints

- Legacy module import may fail; handle ImportError gracefully
- Backward compatibility must be maintained for legacy session wrapper
- State synchronization with legacy module globals required when auto-trace enabled

## Cautions

- Direct access to another module's globals is not ideal; prefer explicit calls where possible
- ImportError on legacy module access should not occur in normal operation but is handled defensively

## Output Contract

- self._initialized flag is set to True; returns legacy session wrapper object if auto_start_session=True, otherwise returns None. Caller receives a usable session handle or explicit None to indicate no auto-session.

## Triggers

- Caller submits multiple tasks to an Executor and needs to block until one or more reach a terminal state
- Timeout or early-exit strategy is required to avoid indefinite blocking
- Caller must partition results into completed and pending sets for downstream handling
