# Notebook-Based Integration Testing 子技能地图

## 子技能列表

- [LiteLLM Integration Setup](通用技能领域/Family技能/未分类技能/二级技能/LiteLLM Integration Setup/SKILL.md) ｜ 二级技能
  - 适用：Configure and install AgentOps support for LiteLLM (>=1.3.1) to enable unified access to 100+ language models through a standardized Input/Output interface.
  - 线索：User needs to integrate multiple LLM providers into an agent system and wants unified API handling, llm, integration, litellm, multi-provider
- [LLM Provider Integration Pattern](通用技能领域/Family技能/未分类技能/二级技能/LLM Provider Integration Pattern/SKILL.md) ｜ 二级技能
  - 适用：Establish a reusable provider class that inherits from BaseProvider, implements required LLM response handling methods, and manages event tracking for prompts, tokens, and errors.
  - 线索：Adding support for a new LLM provider, Extending existing provider functionality, Implementing provider-level integration with AgentOps, llm_integration, provider_pattern
- [Provider Test Coverage Checklist](通用技能领域/Family技能/未分类技能/二级技能/Provider Test Coverage Checklist/SKILL.md) ｜ 二级技能
  - 适用：Structured checklist defining required test scenarios for each LLM provider integration: basic completion calls, streaming responses, async operations, error handling, and tool usage. Use when onboarding a new provider or reviewing test completeness.
  - 线索：Onboarding a new LLM provider, Reviewing provider test completeness before PR merge, Creating or updating example notebooks for a provider, integration_testing, provider_onboarding
