# LLM Alignment Method Comparative Evaluation 子技能地图

## 子技能列表

- [Async-Sync Method Wrapping](通用技能领域/Family技能/未分类技能/微技能/Async-Sync Method Wrapping/SKILL.md) ｜ 微技能
  - 适用：Micro-skill for wrapping both synchronous and asynchronous versions of an API method using wrapt.wrap_function_wrapper, ensuring consistent instrumentation across sync and async call paths.
  - 线索：API library exposes both sync and async versions of the same method, Need identical instrumentation logic for both sync and async paths, Implementing comprehensive API instrumentation, instrumentation, async
- [Bind Tools to LLM with Callback Tracking](通用技能领域/Family技能/未分类技能/微技能/Bind Tools to LLM with Callback Tracking/SKILL.md) ｜ 微技能
  - 适用：Attach tool definitions to an LLM instance and ensure each tool has the AgentOps callback handler assigned so that tool invocations are recorded as observable spans during agent execution.
  - 线索：Configuring an LLM-based agent that uses external tools, Before agent execution begins, When tools need to be bound to an LLM instance, agent_instrumentation, tool_binding
