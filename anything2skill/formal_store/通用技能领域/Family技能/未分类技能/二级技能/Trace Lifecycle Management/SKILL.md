---
id: "2088b931-a182-5233-b4ad-880545601196"
name: "Trace Lifecycle Management"
description: "Initialize, finalize, and update metadata for execution traces in agent debugging workflows. Manages trace context, state transitions, and metadata enrichment across the complete trace lifecycle."
version: "0.1.0"
tags:
  - "trace_management"
  - "agent_debugging"
  - "instrumentation"
  - "session_lifecycle"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "Agent execution begins and requires trace initialization"
  - "Metadata needs to be attached to a running trace"
  - "Trace state must be finalized at agent execution end"
---

# Trace Lifecycle Management

Initialize, finalize, and update metadata for execution traces in agent debugging workflows. Manages trace context, state transitions, and metadata enrichment across the complete trace lifecycle.

## Prompt

Use this skill to manage the full lifecycle of a trace session: (1) start a new trace with optional name and tags, (2) update metadata on the running trace as needed, (3) end the trace with a final state. Ensure trace_context is provided when available to target the correct session; if omitted, operations affect all active spans.

## Objective

Establish and close bounded trace sessions with proper state and metadata tracking
## Applicable Signals

- session_start
- metadata_enrichment_required
- session_end

## Contraindications

- Trace context is already closed
- No active session exists
- Metadata update is not required for the current operation

## Workflow Steps

- {'step': 1, 'action': 'start_trace', 'description': 'Initialize a new trace with optional trace_name and tags', 'input': 'trace_name (str, optional), tags (list, optional)', 'output': 'TraceContext object'}
- {'step': 2, 'action': 'update_trace_metadata', 'description': 'Enrich the running trace with metadata key-value pairs', 'input': "metadata (Dict[str, Any]), prefix (str, default='trace.metadata')", 'output': 'bool (success indicator)'}
- {'step': 3, 'action': 'end_trace', 'description': 'Finalize the trace and record its end state', 'input': 'trace_context (TraceContext, optional), end_state (TraceState|StatusCode|str, default=TraceState.SUCCESS)', 'output': 'None (trace finalized)'}

## Constraints

- trace_context must be valid or None (to target all active spans)
- end_state must be a valid TraceState, StatusCode, or string
- metadata dict must be serializable

## Cautions

- If trace_context is not provided to end_trace, all active spans will be terminated
- Metadata updates must occur while the trace is active; updates after end_trace will fail

## Output Contract

- On start_trace: returns a TraceContext object for downstream reference. On update_trace_metadata: returns boolean indicating success. On end_trace: trace is finalized with the specified end_state recorded; if trace_context is None, all active session spans are ended.

## 子技能目录
- [Trace Metadata Update](通用技能领域/Family技能/未分类技能/微技能/Trace Metadata Update/SKILL.md) ｜ 适用：Programmatically inject or update execution metadata into an active trace during agent processing. Enriches trace logs with runtime context such as operation name, processing stage, record counts, user ID, and custom tags for debugging and monitoring.
- [Trace State Finalization](通用技能领域/Family技能/未分类技能/微技能/Trace State Finalization/SKILL.md) ｜ 适用：Close an active trace and record its final state (success, failure, or custom status). Handles optional trace context and ensures all active session spans are properly terminated.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `Trace Metadata Update` 时，优先调用它。 线索：Agent is actively processing data, Need to log operation name, processing stage, or record count, User context or custom tags must be captured for observability, instrumentation, observability
- 当目标、阶段或方法更接近 `Trace State Finalization` 时，优先调用它。 线索：Agent execution completes, Trace must be marked as success, failure, or custom status, Session spans need termination, trace_management, debugging

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Agent execution begins and requires trace initialization
- Metadata needs to be attached to a running trace
- Trace state must be finalized at agent execution end
