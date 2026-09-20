# AgentOps Session Initialization 子技能地图

## 子技能列表

- [AgentOps Client Configuration Validation](通用技能领域/Family技能/未分类技能/微技能/AgentOps Client Configuration Validation/SKILL.md) ｜ 微技能
  - 适用：Validates configuration parameters against a whitelist of supported parameters during AgentOps client initialization or reconfiguration. Logs warnings for invalid parameters and applies only valid parameters to the global client instance.
  - 线索：AgentOps client instantiation with kwargs, Client reconfiguration request with configuration parameters, configure() function invoked with keyword arguments, configuration, validation
- [Update Ehcache to Jakarta EE 9 Classifier](通用技能领域/Family技能/未分类技能/微技能/Update Ehcache to Jakarta EE 9 Classifier/SKILL.md) ｜ 微技能
  - 适用：Initialize the AgentOps client in 2 lines of code to automatically capture and replay LLM session analytics and call traces.
  - 线索：Migrating Spring Boot application to version 3.0, Ehcache is declared as a project dependency, Target environment requires Jakarta EE 9 or later support, llm_monitoring, observability
