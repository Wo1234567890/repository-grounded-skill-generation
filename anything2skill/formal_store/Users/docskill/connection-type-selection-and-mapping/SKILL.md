---
id: "f10424df-933b-51bb-8ca1-ad9d207806ef"
name: "Connection Type Selection and Mapping"
description: "Validates and ensures a custom reward function accepts required keyword arguments (prompts, completions, and dataset columns) to integrate correctly with GRPO training pipeline without raising TypeError or missing argument errors."
version: "0.1.1"
tags:
  - "grpo"
  - "reward_function"
  - "training_integration"
  - "function_signature"
  - "custom_logic"
triggers:
  - "User is deciding which connection type to use"
  - "User needs to understand the four connection options"
  - "User is beginning virtual hub connection setup"
---

# Connection Type Selection and Mapping

Validates and ensures a custom reward function accepts required keyword arguments (prompts, completions, and dataset columns) to integrate correctly with GRPO training pipeline without raising TypeError or missing argument errors.

## Prompt

When implementing a custom reward function for GRPO training, the function must accept the following as keyword arguments:
- `prompts` (contains the prompts)
- `completions` (contains the generated completions)
- All column names (except `prompt`) that the dataset may have

The easiest way to comply with this requirement is to use `**kwargs` in the function signature. This ensures the trainer can call your function with any dataset columns without raising errors.

## Objective

validate_reward_function_interface
## Applicable Signals

- Custom reward function is being defined
- Dataset contains additional columns beyond prompts and completions
- Training pipeline will invoke reward function with variable keyword arguments

## Contraindications

- Using built-in reward functions provided by the framework
- Not integrating custom logic into the training loop
- Reward function is stateless and requires no dataset context

## Workflow Steps

- {'step': 1, 'action': 'Define custom reward function with **kwargs in signature', 'detail': 'def custom_reward_fn(prompts, completions, **kwargs):'}
- {'step': 2, 'action': 'Extract dataset-specific columns from kwargs as needed', 'detail': "Access additional columns like ground_truth via kwargs.get('ground_truth') or direct parameter binding"}
- {'step': 3, 'action': 'Implement reward computation logic', 'detail': 'Use prompts, completions, and any dataset columns to compute scalar or vector rewards'}
- {'step': 4, 'action': 'Return reward tensor or array', 'detail': 'Ensure output shape and type match trainer expectations'}

## Constraints

- Function signature must include `**kwargs` to accept arbitrary keyword arguments
- Function must accept at minimum: `prompts`, `completions`
- Function must accept all dataset column names as keyword arguments
- Column name `prompt` (singular) is excluded; use `prompts` (plural) instead

## Cautions

- Forgetting **kwargs will cause trainer to fail when passing dataset columns
- Mismatching parameter names (e.g., `prompt` vs `prompts`) will cause binding errors
- Reward function must be deterministic or handle randomness consistently across batches

## Output Contract

- Custom reward function is defined with **kwargs in signature and correctly receives prompts, completions, and all dataset columns as keyword arguments during training without raising TypeError or missing argument errors.

## Triggers

- User is deciding which connection type to use
- User needs to understand the four connection options
- User is beginning virtual hub connection setup
