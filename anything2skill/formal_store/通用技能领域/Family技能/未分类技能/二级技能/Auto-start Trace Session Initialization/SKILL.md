---
id: "d5bcd64f-230a-531e-a11f-ede793929a13"
name: "Auto-start Trace Session Initialization"
description: "Automatically initialize and start a tracing session when configured, registering exit handlers and creating trace contexts for observability."
version: "0.1.0"
tags:
  - "observability"
  - "tracing"
  - "session_initialization"
  - "auto_start"
  - "infrastructure"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "System startup or client initialization"
  - "auto_start_session config is True"
  - "No active trace context exists or trace context is not recording"
---

# Auto-start Trace Session Initialization

Automatically initialize and start a tracing session when configured, registering exit handlers and creating trace contexts for observability.

## Prompt

Check if auto_start_session is enabled and no active trace context exists. If conditions are met, register an atexit handler, start a new trace with the configured trace_name and default_tags, create a legacy session reference for backward compatibility, and update global references.

## Objective

Initialize tracing infrastructure with auto-start capability
## Applicable Signals

- config.auto_start_session == True
- _init_trace_context is None or not recording
- Client initialization phase

## Contraindications

- Trace context already actively recording
- auto_start_session is False
- Manual trace control is required by caller

## Workflow Steps

- Check if atexit handler is already registered; if not, register _end_init_trace_atexit and set _atexit_registered to True
- Verify auto_start_session is enabled and trace context is inactive
- Retrieve trace_name from config or use default value
- Call tracer.start_trace() with trace_name, default_tags, and is_init_trace=True
- If trace context created successfully, instantiate legacy Session object
- Update global references for backward compatibility with legacy code paths

## Constraints

- atexit handler must be registered only once (check _atexit_registered flag)
- Legacy session reference must be established after trace context creation
- Global references (_client_init_trace_context, _client_legacy_session_for_init_trace) must be updated for backward compatibility

## Cautions

- Ensure atexit handler is idempotent to prevent duplicate registrations
- Verify tracer.start_trace() is available and properly configured before invocation
- Legacy session creation depends on successful trace context initialization

## Output Contract

- Returns active trace context with trace_name and default_tags applied; legacy session reference established; atexit handler registered for cleanup; global references updated for downstream callers.

## 子技能目录
- [Exit Handler Registration for Trace Cleanup](通用技能领域/Family技能/未分类技能/微技能/Exit Handler Registration for Trace Cleanup/SKILL.md) ｜ 适用：Register a single atexit handler to ensure trace cleanup occurs on process termination, preventing duplicate handler registration through idempotent flag checking.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `Exit Handler Registration for Trace Cleanup` 时，优先调用它。 线索：Client or session initialization begins, Trace context setup required, lifecycle, cleanup, idempotent

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- System startup or client initialization
- auto_start_session config is True
- No active trace context exists or trace context is not recording
