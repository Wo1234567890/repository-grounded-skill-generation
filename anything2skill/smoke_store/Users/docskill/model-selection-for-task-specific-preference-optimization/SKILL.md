---
id: "7ad13a21-b8ef-5920-b321-2e3ea8b3b420"
name: "Model Selection for Task-Specific Preference Optimization"
description: "Micro-skill for selecting the optimal base model (Llama3 vs. Gemma) when training with SimPO, based on task characteristics. Gemma-2-9b-it is preferred for tasks involving math reasoning or knowledge-intensive benchmarks (GSM, MMLU) due to lower catastrophic forgetting despite limited math data in training datasets."
version: "0.1.0"
tags:
  - "model_selection"
  - "preference_optimization"
  - "catastrophic_forgetting"
  - "math_reasoning"
  - "knowledge_retention"
triggers:
  - "Initiating SimPO training workflow"
  - "Task includes math reasoning benchmarks (GSM, MMLU)"
  - "Knowledge retention is a primary evaluation criterion"
---

# Model Selection for Task-Specific Preference Optimization

Micro-skill for selecting the optimal base model (Llama3 vs. Gemma) when training with SimPO, based on task characteristics. Gemma-2-9b-it is preferred for tasks involving math reasoning or knowledge-intensive benchmarks (GSM, MMLU) due to lower catastrophic forgetting despite limited math data in training datasets.

## Prompt

When preparing to train a preference optimization model, evaluate whether your task includes math reasoning or knowledge-intensive evaluation benchmarks. If yes, select google/gemma-2-9b-it as the base model; otherwise, Llama3 models are acceptable. Document the task characteristics and model choice rationale.

## Objective

Choose optimal base model to minimize catastrophic forgetting during preference optimization training
## Applicable Signals

- Presence of math-heavy evaluation tasks
- Knowledge-intensive benchmark requirements
- Need to minimize performance degradation on existing capabilities

## Contraindications

- Base model already selected and locked
- Task has no math or knowledge-intensive components
- Resource constraints prohibit model comparison or multi-model training

## Workflow Steps

- {'step': 1, 'action': 'Identify task evaluation benchmarks', 'detail': 'List all primary evaluation benchmarks (e.g., GSM, MMLU, AlpacaEval 2)'}
- {'step': 2, 'action': 'Assess math and knowledge intensity', 'detail': 'Determine if task includes math reasoning or knowledge-intensive components'}
- {'step': 3, 'action': 'Select base model', 'detail': 'If math/knowledge-intensive: select google/gemma-2-9b-it; otherwise, Llama3 models acceptable'}
- {'step': 4, 'action': 'Document selection rationale', 'detail': 'Record task characteristics and model choice justification for reproducibility'}

## Constraints

- Gemma-2-9b-it selection applies specifically to preference optimization workflows
- Decision should be made before training begins
- Evaluation templates and tokenizers must be compatible with selected model

## Cautions

- Llama3 models require pre-update tokenizer when evaluating on AlpacaEval 2 and Arena-Hard
- Gemma advantage is empirically demonstrated on math tasks despite limited math data in ultrafeedback dataset

## Output Contract

- Selected base model identifier (e.g., 'google/gemma-2-9b-it' or 'meta-llama/Llama-3-*') with documented task characteristics and selection rationale. Downstream training workflow receives model choice and can proceed with configuration.

## Triggers

- Initiating SimPO training workflow
- Task includes math reasoning benchmarks (GSM, MMLU)
- Knowledge retention is a primary evaluation criterion
