---
id: "8d014104-7fc2-512e-b2a3-b3a520e8b034"
name: "SimPO Training Pipeline Configuration"
description: "Reusable macro protocol for configuring and executing Simple Preference Optimization training on language models with reproducible hyperparameters, model-specific adjustments, and benchmark validation."
version: "0.1.0"
tags:
  - "model_training"
  - "preference_optimization"
  - "language_model"
  - "hyperparameter_tuning"
  - "reproducibility"
  - "benchmark_evaluation"
triggers:
  - "Training a language model using preference optimization"
  - "Need to reproduce paper results or adapt SimPO to new tasks"
  - "Evaluating trained models on AlpacaEval 2 or Arena-Hard benchmarks"
---

# SimPO Training Pipeline Configuration

Reusable macro protocol for configuring and executing Simple Preference Optimization training on language models with reproducible hyperparameters, model-specific adjustments, and benchmark validation.

## Prompt

Configure and execute SimPO training pipeline with reproducible hyperparameters and model-specific adjustments. When training Llama3, use the pre-update tokenizer version (before the PR). For math-heavy tasks, prefer Gemma models (e.g., google/gemma-2-9b-it) to minimize catastrophic forgetting on benchmarks like GSM and MMLU. SimPO is simpler and less resource-intensive than DPO while achieving comparable performance across benchmarks.

## Objective

Configure and execute SimPO training pipeline with reproducible hyperparameters and model-specific adjustments
## Applicable Signals

- Preference-based training objective selected
- Target benchmarks identified (AlpacaEval 2, Arena-Hard, or task-specific metrics)
- Base model selected (Llama3, Gemma, or other)

## Contraindications

- Inference-only workflows
- Models already fine-tuned via other methods
- Non-preference-based training objectives
- Supervised fine-tuning (SFT) without preference signal

## Workflow Steps

- {'step': 1, 'action': 'Select base model and verify tokenizer version', 'detail': 'If using Llama3, confirm pre-update tokenizer is installed. If training on math tasks, consider Gemma-2-9b-it.'}
- {'step': 2, 'action': 'Prepare preference dataset', 'detail': 'Ensure dataset contains chosen and rejected response pairs; verify alignment with model tokenizer.'}
- {'step': 3, 'action': 'Configure hyperparameters', 'detail': 'Tune learning rate, batch size, and other parameters; reference paper defaults as starting point.'}
- {'step': 4, 'action': 'Execute SimPO training', 'detail': 'Run training script with configured hyperparameters; monitor for catastrophic forgetting on benchmark tasks.'}
- {'step': 5, 'action': 'Evaluate on target benchmarks', 'detail': 'Use provided evaluation templates; ensure tokenizer version consistency with training.'}
- {'step': 6, 'action': 'Validate checkpoint performance', 'detail': 'Confirm trained model meets target metrics on AlpacaEval 2, Arena-Hard, or task-specific benchmarks.'}

## Constraints

- Llama3 training requires pre-update tokenizer version (before PR) for AlpacaEval 2 and Arena-Hard evaluation
- Gemma models recommended for math-heavy tasks to reduce catastrophic forgetting
- Dataset must include preference pairs (chosen vs. rejected responses)
- Evaluation templates must match training tokenizer version

## Cautions

- Tokenizer version mismatch between training and evaluation can invalidate benchmark results
- Ultrafeedback dataset has limited math-related data; Gemma models mitigate this better than Llama3
- Hyperparameter tuning required for task-specific adaptation

## Output Contract

- Trained model checkpoint with validated performance on target benchmarks (AlpacaEval 2, Arena-Hard, or task-specific metrics); checkpoint includes model weights, tokenizer configuration, and training hyperparameters for reproducibility.

## Triggers

- Training a language model using preference optimization
- Need to reproduce paper results or adapt SimPO to new tasks
- Evaluating trained models on AlpacaEval 2 or Arena-Hard benchmarks
