# Trace and Tag Workflow Execution 子技能地图

## 子技能列表

- [Decorate Workflow Function with Trace Metadata](通用技能领域/Family技能/未分类技能/微技能/Decorate Workflow Function with Trace Metadata/SKILL.md) ｜ 微技能
  - 适用：Apply @trace decorator to a function with name and tags parameters to mark it as a traced workflow unit. Captures workflow execution context and enables filtering by metadata such as environment tags.
  - 线索：You want to trace a specific workflow function and attach metadata such as workflow name and environment tags (e.g., production, staging), tracing, instrumentation, observability, decorator
- [Session Span Initialization](通用技能领域/Family技能/未分类技能/微技能/Session Span Initialization/SKILL.md) ｜ 微技能
  - 适用：Decorator-based pattern to create a root session span that wraps and tracks all nested operations within a workflow function. Use when starting observability instrumentation for an agent workflow.
  - 线索：Starting a new agent workflow or task that requires end-to-end observability tracking, observability, instrumentation, decorator, session_tracking
