---
id: "92ed35c6-913a-5714-a07d-66723714d806"
name: "Update legacy global references for backward compatibility"
description: "Synchronize internal trace context and session objects to global module-level variables to maintain compatibility with legacy code paths using indirect access patterns."
version: "0.1.0"
tags:
  - "backward_compatibility"
  - "legacy_support"
  - "global_state"
  - "initialization"
  - "session_management"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Trace context created successfully"
  - "Legacy session object instantiated from trace context"
  - "Legacy code may access session via indirect module-level patterns"
---

# Update legacy global references for backward compatibility

Synchronize internal trace context and session objects to global module-level variables to maintain compatibility with legacy code paths using indirect access patterns.

## Prompt

After successfully creating a trace context and legacy session object, update the global module-level variables _client_init_trace_context and _client_legacy_session_for_init_trace to reference the newly created instance state. This ensures that legacy code accessing sessions via indirect patterns (e.g., agentops.legacy.get_session()) receives the current trace context without requiring refactoring.

## Objective

Maintain backward compatibility with legacy session access patterns
## Applicable Signals

- self._init_trace_context is not None
- self._legacy_session_for_init_trace is not None
- Legacy integration is active in the codebase

## Contraindications

- No legacy code integration required
- Direct context passing is enforced throughout the codebase
- Trace context creation failed or is None

## Workflow Steps

- {'step': 1, 'action': 'Verify trace context is not None and is recording', 'condition': 'self._init_trace_context is not None'}
- {'step': 2, 'action': 'Verify legacy session object exists', 'condition': 'self._legacy_session_for_init_trace is not None'}
- {'step': 3, 'action': 'Assign self._init_trace_context to global _client_init_trace_context', 'operation': '_client_init_trace_context = self._init_trace_context'}
- {'step': 4, 'action': 'Assign self._legacy_session_for_init_trace to global _client_legacy_session_for_init_trace', 'operation': '_client_legacy_session_for_init_trace = self._legacy_session_for_init_trace'}

## Constraints

- Must execute only after trace context and legacy session are successfully initialized
- Global variables must be updated atomically to avoid inconsistent state
- Update must occur before any legacy code path attempts to access the session

## Cautions

- Global state mutation; ensure thread-safety if multi-threaded access is possible
- Legacy code may cache references; updates may not be visible to already-initialized legacy modules

## Output Contract

- Global variables _client_init_trace_context and _client_legacy_session_for_init_trace are updated to match instance state
- Legacy code paths can now access the current trace context via indirect module-level access

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Trace context created successfully
- Legacy session object instantiated from trace context
- Legacy code may access session via indirect module-level patterns
