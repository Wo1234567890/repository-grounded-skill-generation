---
id: "2fefe2f0-790d-5e47-99c5-c441046648cf"
name: "Start Managed Trace with Context"
description: "Create a new root span (trace) with optional name and tags, returning a TraceContext object for concurrent user-managed tracing sessions. Includes precondition validation and automatic initialization fallback."
version: "0.1.0"
tags:
  - "trace_management"
  - "session_lifecycle"
  - "span_creation"
  - "concurrent_tracing"
  - "context_management"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "Starting a new logical trace or session"
  - "Need to attach tags or custom trace names to a trace"
  - "Require concurrent independent traces managed by caller"
---

# Start Managed Trace with Context

Create a new root span (trace) with optional name and tags, returning a TraceContext object for concurrent user-managed tracing sessions. Includes precondition validation and automatic initialization fallback.

## Prompt

Call start_trace(trace_name, tags) to initiate a named trace session. If SDK is not initialized, the function attempts auto-initialization with environment defaults before creating the trace. Returns a TraceContext object on success, or None if initialization fails. Use this to establish independent, concurrent trace sessions with custom metadata.

## Objective

Establish a named trace session with optional metadata and return its context for downstream span operations
## Applicable Signals

- User initiates a new task or session boundary
- Caller needs to track a named workflow or user interaction
- Multiple concurrent traces must be managed independently

## Contraindications

- Tracing is not enabled or SDK is not initialized
- User does not need trace context or span management
- Caller cannot handle None return value (initialization failure)

## Workflow Steps

- {'step': 1, 'action': 'Check if tracer is initialized', 'condition': 'if not tracer.initialized'}
- {'step': 2, 'action': 'Log warning and attempt auto-initialization', 'condition': 'SDK not initialized', 'detail': 'Call init() with environment variables and defaults'}
- {'step': 3, 'action': 'Verify initialization success', 'condition': 'After init() call', 'detail': 'Check tracer.initialized; log error and return None if still False'}
- {'step': 4, 'action': 'Catch and log initialization exceptions', 'condition': 'If init() raises exception', 'detail': 'Log error with exception details and return None'}
- {'step': 5, 'action': 'Invoke tracer.start_trace()', 'condition': 'tracer.initialized is True', 'detail': 'Pass trace_name and tags; return TraceContext object'}

## Constraints

- SDK must be initialized before or during start_trace call
- trace_name should be a non-empty string (default: 'session')
- tags must be either a list of strings or a dict; other types are rejected

## Cautions

- If SDK auto-initialization fails, function returns None; caller must handle gracefully
- Concurrent traces require caller to manage context tokens separately
- Trace context is valid only if tracer.initialized is True after initialization attempt

## Output Contract

- Returns a TraceContext object containing the span and context token on success. Returns None if SDK initialization fails or is not available. Caller must check for None before using the returned context.

## 子技能目录
- [End Trace and Finalize](通用技能领域/Family技能/未分类技能/微技能/End Trace and Finalize/SKILL.md) ｜ 适用：Terminates the current trace (root span) and finalizes its state. If no trace context is provided, closes all active session spans. Use when completing a debugging session or marking trace completion status.
- [Initialize SDK with Fallback](通用技能领域/Family技能/未分类技能/微技能/Initialize SDK with Fallback/SKILL.md) ｜ 适用：Automatically initialize the AgentOps SDK using environment variables or defaults if not already initialized, with error logging and graceful failure handling. Ensures the tracer is ready before downstream operations attempt to use it.
- [Resolve Active Span from OpenTelemetry Context](通用技能领域/Family技能/未分类技能/微技能/Resolve Active Span from OpenTelemetry Context/SKILL.md) ｜ 适用：Retrieve and validate the current span from OpenTelemetry context, then locate the root trace span if the current span is a child span. Use this when instrumenting distributed tracing and need to attach operations to the correct parent trace.
- [Start Trace Session](通用技能领域/Family技能/未分类技能/微技能/Start Trace Session/SKILL.md) ｜ 适用：Initiates a named trace with optional tags and returns a trace context for subsequent span operations. Use when beginning a new debugging or monitoring session.
- [Update legacy global references for backward compatibility](通用技能领域/Family技能/未分类技能/微技能/Update legacy global references for backward compatibility/SKILL.md) ｜ 适用：Synchronize internal trace context and session objects to global module-level variables to maintain compatibility with legacy code paths using indirect access patterns.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `End Trace and Finalize` 时，优先调用它。 线索：Completing a trace session, Finalizing agent operation monitoring, Closing all active spans, trace_lifecycle, debugging
- 当目标、阶段或方法更接近 `Initialize SDK with Fallback` 时，优先调用它。 线索：tracer.initialized returns False, SDK initialization status is unknown or unconfirmed before starting a trace, sdk_setup, initialization, fallback
- 当目标、阶段或方法更接近 `Resolve Active Span from OpenTelemetry Context` 时，优先调用它。 线索：Instrumenting an operation within an active OpenTelemetry trace and need to attach to the root session span rather than a child span, opentelemetry, distributed_tracing, span_resolution, trace_instrumentation
- 当目标、阶段或方法更接近 `Start Trace Session` 时，优先调用它。 线索：starting a new trace session, beginning a debugging workflow, initializing monitoring for an agent operation, trace_lifecycle, debugging
- 当目标、阶段或方法更接近 `Update legacy global references for backward compatibility` 时，优先调用它。 线索：Trace context created successfully, Legacy session object instantiated from trace context, Legacy code may access session via indirect module-level patterns, backward_compatibility, legacy_support

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Starting a new logical trace or session
- Need to attach tags or custom trace names to a trace
- Require concurrent independent traces managed by caller
