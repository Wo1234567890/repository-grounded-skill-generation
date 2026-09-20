---
id: "77301bc9-1895-5903-85d4-c09b6dabca74"
name: "Completion Batch Generation"
description: "Sample a batch of prompts and generate G completions per prompt during each GRPO training step. This grouped generation is the core mechanism that enables relative policy optimization by creating multiple candidate outputs for each prompt."
version: "0.1.0"
tags:
  - "grpo"
  - "batch_generation"
  - "policy_optimization"
  - "sampling"
  - "training_step"
triggers:
  - "Start of each GRPO training step"
  - "Batch of prompts loaded and ready for processing"
  - "Policy model available for inference"
---

# Completion Batch Generation

Sample a batch of prompts and generate G completions per prompt during each GRPO training step. This grouped generation is the core mechanism that enables relative policy optimization by creating multiple candidate outputs for each prompt.

## Prompt

At each training step, sample a batch of prompts from the dataset. For each prompt, generate G completions using the current policy model. Index and organize completions by prompt to prepare for downstream reward scoring and advantage computation.

## Objective

Generate multiple candidate completions for policy optimization
## Applicable Signals

- Training loop iteration begins
- Prompt batch size and G (completions per prompt) configured
- Model in inference mode

## Contraindications

- Inference-only mode without training objective
- Single completion per prompt is sufficient for the use case
- Computational budget does not support G > 1 completions per prompt

## Workflow Steps

- {'step': 1, 'action': 'Load batch of prompts from training dataset'}
- {'step': 2, 'action': 'Set model to inference mode (no gradients)'}
- {'step': 3, 'action': 'For each prompt in batch, generate G completions using the policy model'}
- {'step': 4, 'action': 'Index and organize completions by source prompt'}
- {'step': 5, 'action': 'Return structured batch: {prompt_id: [completion_1, ..., completion_G]}'}

## Constraints

- G must be >= 1 (number of completions per prompt)
- All completions must be indexed by source prompt
- Completion length and format must be consistent for downstream reward scoring

## Cautions

- Generating G completions per prompt increases computational cost linearly with G
- Ensure model is in evaluation mode to avoid unintended gradient accumulation during generation

## Output Contract

- Structured batch of completions indexed by prompt. Each prompt has exactly G completions. Completions are ready for reward scoring and advantage computation in the next training step.

## Triggers

- Start of each GRPO training step
- Batch of prompts loaded and ready for processing
- Policy model available for inference
