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
- Model Evaluation Protocol for LLM Preference Optimization ｜ 类型：model_evaluation ｜ 适用条件：Standardized workflow for evaluating language models trained with preference optimization using three benchmark suites (AlpacaEval 2, Arena-Hard, MT-Bench). Directs practitioners to official implementations and repositories for consistent evaluation across multiple benchmarks.
- SimPO Training Pipeline Configuration ｜ 类型：model_training ｜ 适用条件：Reusable macro protocol for configuring and executing Simple Preference Optimization training on language models with reproducible hyperparameters, model-specific adjustments, and benchmark validation.

## 选用规则（一级技能目录）
- 当问题命中“After training a preference-optimized language model and before reporting performance metrics、When comparing model outputs against standard benchmarks、model_evaluation、benchmark”这类线索时，优先选择 Model Evaluation Protocol for LLM Preference Optimization。
- 当问题命中“Training a language model using preference optimization、Need to reproduce paper results or adapt SimPO to new tasks、Evaluating trained models on AlpacaEval 2 or Arena-Hard benchmarks、model_training”这类线索时，优先选择 SimPO Training Pipeline Configuration。

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
