# LLM Provider Integration Pattern 子技能地图

## 子技能列表

- [Provider Method Override and Restoration](通用技能领域/Family技能/未分类技能/微技能/Provider Method Override and Restoration/SKILL.md) ｜ 微技能
  - 适用：Patch and restore LLM provider methods to enable transparent event capture (prompts, completions, tokens, timestamps, errors, tool usage) without modifying client code. Implements override() to inject wrapper functions and undo_override() to restore original methods.
  - 线索：Provider class instantiation requires method interception, LLM call event capture is needed without client code modification, Session setup phase for transparent provider instrumentation, llm_integration, method_patching
