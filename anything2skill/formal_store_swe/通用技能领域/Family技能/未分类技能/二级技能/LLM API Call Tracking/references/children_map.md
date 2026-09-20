# LLM API Call Tracking 子技能地图

## 子技能列表

- [Anthropic Streaming Message Handler](通用技能领域/Family技能/未分类技能/微技能/Anthropic Streaming Message Handler/SKILL.md) ｜ 微技能
  - 适用：Consume streamed message tokens from Anthropic Claude API within an AgentOps session. Handles incremental token delivery for real-time agent response processing.
  - 线索：Anthropic integration requires low-latency token streaming, Agent needs to process partial responses in real-time, AgentOps session is active and initialized, anthropic, streaming
- [Extract LLM Call Attributes](通用技能领域/Family技能/未分类技能/微技能/Extract LLM Call Attributes/SKILL.md) ｜ 微技能
  - 适用：Extract structured attributes (model, tokens, usage) from LLM method calls and return values for telemetry recording. Maps call arguments and responses to OpenTelemetry attribute keys.
  - 线索：Intercepting LLM provider method calls (OpenAI, Anthropic, Google GenAI, IBM WatsonX, CrewAI, AG2/AutoGen, etc.), Need to extract model name, token usage, or response metadata for observability, Preparing telemetry data for OpenTelemetry span attachment, telemetry, instrumentation
- [LLM Chat Completion with AgentOps Tracking](通用技能领域/Family技能/未分类技能/微技能/LLM Chat Completion with AgentOps Tracking/SKILL.md) ｜ 微技能
  - 适用：Execute a chat completion request to an LLM endpoint with AgentOps session tracking enabled. Captures the API call, model selection, and response for observability and debugging.
  - 线索：LLM response needed for agent task, User query requires LLM inference, AgentOps session is active and initialized, llm, chat_completion
