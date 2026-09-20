---
id: "2fcf2c8c-ee2d-5471-a738-db6f6386065f"
name: "未分类技能"
description: "未分类技能 的总导航技能：汇总适用场景、总流程、子技能地图与选用规则。"
version: "0.1.0"
tags:
  - "未分类技能"
  - "总导航"
  - "子技能地图"
  - "kind:parent"
  - "profile:default::未分类技能"
triggers:
  - "未分类技能"
  - "未分类技能 总导航"
  - "未分类技能 子技能地图"
---

# 未分类技能

未分类技能 的总导航技能：汇总适用场景、总流程、子技能地图与选用规则。

## Prompt

## 适用场景
- 当当前问题明确属于或需要路由到 未分类技能 时，先使用本总技能决定子技能选择顺序。
- 本技能用于导航与组合，不替代子技能中的具体执行 SOP。

## 不适用/风险边界
- 不要把本技能当作具体干预脚本；真正执行时必须继续调用对应子技能。
- 如存在明显高风险或危机信号，应优先调用风险/危机类子技能。

## 总流程
1. 先判断当前问题是否适合进入该家族或领域的处理路径。
2. 再根据任务类型、阶段和风险边界选择最合适的子技能。
3. 调用对应子技能执行具体步骤、规则和输出格式。
4. 最后输出所选子技能、选择理由、执行顺序与风险提示。

## 子技能目录（一级技能目录）
- ColorBrewer Diverging Palette Selection ｜ 类型：color_selection ｜ 适用条件：Select and apply ColorBrewer diverging color schemes for visualizations encoding data with two opposing extremes and a meaningful midpoint. Diverging palettes (BrBG, PiYG, PRGn, PuOr, RdBu, RdGy, RdYlBu, RdYlGn, Spectral) are semantically distinct from sequential and categorical schemes.
- Curve Type Selection Reference ｜ 类型：curve_rendering ｜ 适用条件：Canonical reference for selecting appropriate D3 curve interpolation methods based on shape requirements. Provides lookup of curve type properties (closure, continuity, tangent behavior, monotonicity, parameters) to inform curve selection decisions during planning phase.
- D3 Axis API Reference Lookup ｜ 类型：visualization_markup ｜ 适用条件：Canonical reference for D3 axis module API surface. Provides method signatures, orientation constructors, scale binding, and tick/format customization options. Used during axis implementation design to recall available methods and their purposes.
- D3 Color Scheme Reference Lookup ｜ 类型：color_selection ｜ 适用条件：Canonical reference asset documenting D3 built-in color schemes (categorical, cyclical, diverging) with cardinality, visual properties, and recommended use cases. Enables informed color encoding strategy planning and team alignment without runtime execution.
- D3 Selection and Event Handling Reference ｜ 类型：data_visualization ｜ 适用条件：Canonical reference for D3 selection methods and event handling patterns. Provides lookup and documentation for selection operations, data binding (enter/update/exit), datum access, and event binding APIs.
- Generate random variates from statistical distributions ｜ 类型：random_sampling ｜ 适用条件：Generate pseudorandom numbers from 15+ named statistical distributions (uniform, normal, exponential, Poisson, binomial, beta, gamma, Weibull, Cauchy, logistic, geometric, Bernoulli, Bates, Irwin–Hall, log-normal, Pareto) with optional seeding via LCG source. Use when simulation, Monte Carlo sampling, or stochastic modeling requires reproducible random variates.

## 选用规则（一级技能目录）
- 当问题命中“Encoding data with a meaningful neutral midpoint、Visualizing opposing or contrasting data extremes、Selecting color scheme for diverging phenomena (anomalies, deviations, political/economic spectra)、color_scheme”这类线索时，优先选择 ColorBrewer Diverging Palette Selection。
- 当问题命中“Evaluating which curve type best fits shape requirements、Comparing monotonicity, closure, or tangent behavior、Documenting curve selection rationale、d3”这类线索时，优先选择 Curve Type Selection Reference。
- 当问题命中“Developer needs to recall axis method names, signatures, or available configuration options during implementation、d3、axis、api_reference”这类线索时，优先选择 D3 Axis API Reference Lookup。
- 当问题命中“planning color encoding strategy、comparing scheme options、documenting color choices、training team on D3 color APIs”这类线索时，优先选择 D3 Color Scheme Reference Lookup。
- 当问题命中“Need to look up D3 selection methods, event handling patterns, or data binding API signatures、d3、selection、data-binding”这类线索时，优先选择 D3 Selection and Event Handling Reference。
- 当问题命中“Need to sample from a named distribution (normal, exponential, Poisson, binomial, beta, gamma, Weibull, Cauchy, logistic, geometric, Bernoulli, Bates, Irwin–Hall, log-normal, Pareto); require reproducible randomness via seed control、random_sampling、statistical_distribution、Monte_Carlo”这类线索时，优先选择 Generate random variates from statistical distributions。

## 输出格式
- family_route:
  - family: 未分类技能
  - selected_children: [子技能名称列表]
  - rationale: 说明为什么选择这些子技能
  - cautions: 风险边界与切换条件

## Files

- `references/children_manifest.json`
- `references/children_map.md`

## Triggers

- 未分类技能
- 未分类技能 总导航
- 未分类技能 子技能地图
