# Trace Lifecycle Management 子技能地图

## 子技能列表

- [Trace Metadata Update](通用技能领域/Family技能/未分类技能/微技能/Trace Metadata Update/SKILL.md) ｜ 微技能
  - 适用：Programmatically inject or update execution metadata into an active trace during agent processing. Enriches trace logs with runtime context such as operation name, processing stage, record counts, user ID, and custom tags for debugging and monitoring.
  - 线索：Agent is actively processing data, Need to log operation name, processing stage, or record count, User context or custom tags must be captured for observability, instrumentation, observability
- [Trace State Finalization](通用技能领域/Family技能/未分类技能/微技能/Trace State Finalization/SKILL.md) ｜ 微技能
  - 适用：Close an active trace and record its final state (success, failure, or custom status). Handles optional trace context and ensures all active session spans are properly terminated.
  - 线索：Agent execution completes, Trace must be marked as success, failure, or custom status, Session spans need termination, trace_management, debugging
