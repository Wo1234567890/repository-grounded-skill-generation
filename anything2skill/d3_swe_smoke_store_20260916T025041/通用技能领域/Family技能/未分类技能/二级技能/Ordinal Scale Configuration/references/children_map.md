# Ordinal Scale Configuration 子技能地图

## 子技能列表

- [Declare and Manage Local Variables](通用技能领域/Family技能/未分类技能/微技能/Declare and Manage Local Variables/SKILL.md) ｜ 微技能
  - 适用：Create, set, retrieve, and remove scoped local variables in D3 contexts. Use when you need isolated state that does not pollute global scope or require explicit lifecycle management.
  - 线索：Need to store data bound to a specific D3 selection or DOM node, Require isolated state without global side effects, Managing per-element or per-context metadata, d3, state_management
- [Scale Instance Duplication](通用技能领域/Family技能/未分类技能/微技能/Scale Instance Duplication/SKILL.md) ｜ 微技能
  - 适用：Create an independent copy of an existing ordinal scale, preserving its domain, range, and unknown-value configuration. Use this when you need a variant with the same initial settings but allow independent modifications without affecting the original.
  - 线索：You have a configured ordinal scale and need to create a variant with the same initial settings, You need to allow independent modifications without affecting the original scale, scale, ordinal, duplication
- [Unknown Value Fallback Policy](通用技能领域/Family技能/未分类技能/微技能/Unknown Value Fallback Policy/SKILL.md) ｜ 微技能
  - 适用：Define and apply a fallback output value for domain inputs that are not explicitly mapped in an ordinal scale. When an ordinal scale receives a domain value outside its registered set, return a configured unknown value instead of undefined output.
  - 线索：An ordinal scale receives a domain value that was not included in the initial domain definition; you need predictable behavior instead of undefined output., ordinal-scale, fallback, error-handling, d3-scale
