# OpenAI Library Instrumentation Setup 子技能地图

## 子技能列表

- [Streaming API Wrapper Registration](通用技能领域/Family技能/未分类技能/微技能/Streaming API Wrapper Registration/SKILL.md) ｜ 微技能
  - 适用：Register function wrappers for OpenAI v1 streaming endpoints to capture telemetry for sync and async calls. Attaches tracing wrappers to chat completions, beta completions, and responses API entry points.
  - 线索：OpenAI v1 is detected, Streaming telemetry is required, Tracer instance is available and initialized, openai, instrumentation
- [Streaming Response Instrumentation](通用技能领域/Family技能/未分类技能/微技能/Streaming Response Instrumentation/SKILL.md) ｜ 微技能
  - 适用：Wrap streaming methods to capture and trace chunk-by-chunk responses with consistent content extraction. Use when instrumenting APIs that return streaming or chunked responses.
  - 线索：Method returns a streaming or iterable response, Per-chunk tracing and content extraction is required, Using wrap_function_wrapper pattern for instrumentation, instrumentation, streaming
- [Version-Specific OpenAI Instrumentor Initialization](通用技能领域/Family技能/未分类技能/微技能/Version-Specific OpenAI Instrumentor Initialization/SKILL.md) ｜ 微技能
  - 适用：Detect OpenAI library version at runtime and apply the appropriate instrumentation strategy: delegate to legacy instrumentor for v0, or proceed with standard v1 initialization. Ensures instrumentation compatibility across library versions by routing initialization logic based on version detection.
  - 线索：OpenAI library version is unknown or mixed (v0 and v1 coexist), Initialization phase begins and library version must be detected, Runtime environment requires adaptive instrumentation strategy, openai, instrumentation
