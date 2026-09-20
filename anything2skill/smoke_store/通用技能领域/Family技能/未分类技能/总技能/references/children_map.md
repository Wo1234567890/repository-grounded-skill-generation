# 未分类技能 子技能地图

- parent: `未分类技能/总技能/SKILL.md`

## 子技能列表

1. [Model Evaluation Protocol for LLM Preference Optimization](通用技能领域/Family技能/未分类技能/一级技能/Model Evaluation Protocol for LLM Preference Optimization/SKILL.md)
   - 层级：一级技能
   - 类型：model_evaluation
   - 适用条件：Standardized workflow for evaluating language models trained with preference optimization using three benchmark suites (AlpacaEval 2, Arena-Hard, MT-Bench). Directs practitioners to official implementations and repositories for consistent evaluation across multiple benchmarks.
2. [Model Selection for Task-Specific Preference Optimization](通用技能领域/Family技能/未分类技能/微技能/Model Selection for Task-Specific Preference Optimization/SKILL.md)
   - 层级：微技能
   - 类型：model_selection
   - 适用条件：Micro-skill for selecting the optimal base model (Llama3 vs. Gemma) when training with SimPO, based on task characteristics. Gemma-2-9b-it is preferred for tasks involving math reasoning or knowledge-intensive benchmarks (GSM, MMLU) due to lower catastrophic forgetting despite limited math data in training datasets.
3. [SimPO Training Pipeline Configuration](通用技能领域/Family技能/未分类技能/一级技能/SimPO Training Pipeline Configuration/SKILL.md)
   - 层级：一级技能
   - 类型：model_training
   - 适用条件：Reusable macro protocol for configuring and executing Simple Preference Optimization training on language models with reproducible hyperparameters, model-specific adjustments, and benchmark validation.
