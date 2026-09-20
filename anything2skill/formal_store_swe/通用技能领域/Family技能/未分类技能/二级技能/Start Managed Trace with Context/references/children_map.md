# Start Managed Trace with Context 子技能地图

## 子技能列表

- [End Trace and Finalize](通用技能领域/Family技能/未分类技能/微技能/End Trace and Finalize/SKILL.md) ｜ 微技能
  - 适用：Terminates the current trace (root span) and finalizes its state. If no trace context is provided, closes all active session spans. Use when completing a debugging session or marking trace completion status.
  - 线索：Completing a trace session, Finalizing agent operation monitoring, Closing all active spans, trace_lifecycle, debugging
- [Initialize SDK with Fallback](通用技能领域/Family技能/未分类技能/微技能/Initialize SDK with Fallback/SKILL.md) ｜ 微技能
  - 适用：Automatically initialize the AgentOps SDK using environment variables or defaults if not already initialized, with error logging and graceful failure handling. Ensures the tracer is ready before downstream operations attempt to use it.
  - 线索：tracer.initialized returns False, SDK initialization status is unknown or unconfirmed before starting a trace, sdk_setup, initialization, fallback
- [Resolve Active Span from OpenTelemetry Context](通用技能领域/Family技能/未分类技能/微技能/Resolve Active Span from OpenTelemetry Context/SKILL.md) ｜ 微技能
  - 适用：Retrieve and validate the current span from OpenTelemetry context, then locate the root trace span if the current span is a child span. Use this when instrumenting distributed tracing and need to attach operations to the correct parent trace.
  - 线索：Instrumenting an operation within an active OpenTelemetry trace and need to attach to the root session span rather than a child span, opentelemetry, distributed_tracing, span_resolution, trace_instrumentation
- [Start Trace Session](通用技能领域/Family技能/未分类技能/微技能/Start Trace Session/SKILL.md) ｜ 微技能
  - 适用：Initiates a named trace with optional tags and returns a trace context for subsequent span operations. Use when beginning a new debugging or monitoring session.
  - 线索：starting a new trace session, beginning a debugging workflow, initializing monitoring for an agent operation, trace_lifecycle, debugging
- [Update legacy global references for backward compatibility](通用技能领域/Family技能/未分类技能/微技能/Update legacy global references for backward compatibility/SKILL.md) ｜ 微技能
  - 适用：Synchronize internal trace context and session objects to global module-level variables to maintain compatibility with legacy code paths using indirect access patterns.
  - 线索：Trace context created successfully, Legacy session object instantiated from trace context, Legacy code may access session via indirect module-level patterns, backward_compatibility, legacy_support
