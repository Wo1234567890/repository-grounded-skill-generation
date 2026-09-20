# Conditional Package Instrumentation 子技能地图

## 子技能列表

- [Dependent Package Instrumentation Trigger](通用技能领域/Family技能/未分类技能/微技能/Dependent Package Instrumentation Trigger/SKILL.md) ｜ 微技能
  - 适用：Automatically instruments dependent packages (e.g., concurrent.futures when mem0 is instrumented) to ensure complete observability of related execution contexts.
  - 线索：A package with known dependencies (e.g., mem0) is newly instrumented and the dependent module is available, instrumentation, dependency_handling, observability, concurrent_execution
- [Resolve and Import Instrumentation Module](通用技能领域/Family技能/未分类技能/微技能/Resolve and Import Instrumentation Module/SKILL.md) ｜ 微技能
  - 适用：Dynamically import an instrumentation module by name and return the module object for subsequent class instantiation or method access.
  - 线索：When you need to obtain a module object from a stored module name string, Before instantiating a class from that module, importlib, dynamic_import, module_resolution
