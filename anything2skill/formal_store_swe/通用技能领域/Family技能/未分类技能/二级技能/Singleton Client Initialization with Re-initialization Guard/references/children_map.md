# Singleton Client Initialization with Re-initialization Guard 子技能地图

## 子技能列表

- [ProcessPoolExecutor Worker Lifecycle Configuration](通用技能领域/Family技能/未分类技能/微技能/ProcessPoolExecutor Worker Lifecycle Configuration/SKILL.md) ｜ 微技能
  - 适用：Register and execute a global atexit handler that safely ends the client's auto-initialized trace context during application shutdown, with error recovery and resource cleanup.
  - 线索：Need to control fork vs. spawn behavior for worker processes, Require setup code (e.g., database connection) to run in each worker, Want to limit worker lifetime to prevent memory leaks, Must ensure consistent worker state across task batches, shutdown
- [Singleton Client Initialization](通用技能领域/Family技能/未分类技能/微技能/Singleton Client Initialization/SKILL.md) ｜ 微技能
  - 适用：Initialize and manage a singleton Client instance for AgentOps service, ensuring only one active client exists throughout the application lifecycle.
  - 线索：Application startup requires AgentOps client connection, First invocation of Client() constructor, singleton, initialization, client_lifecycle
- [Trace Context Cleanup on Re-initialization](通用技能领域/Family技能/未分类技能/微技能/Trace Context Cleanup on Re-initialization/SKILL.md) ｜ 微技能
  - 适用：Ends any active trace recording and clears trace context when Client is re-initialized with a different API key, preventing orphaned or misattributed traces.
  - 线索：Client re-initialization detected with a different API key, _init_trace_context is not None, _init_trace_context.span.is_recording() returns True, trace_cleanup, re-initialization
