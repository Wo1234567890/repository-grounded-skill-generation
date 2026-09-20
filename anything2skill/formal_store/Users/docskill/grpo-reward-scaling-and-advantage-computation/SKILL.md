---
id: "7bfb3e92-d1fa-551f-b5de-0cb4c8a2a54a"
name: "GRPO Reward Scaling and Advantage Computation"
description: "Compute scaled advantages for each completion by normalizing rewards using standard deviation, with optional disable flag to prevent question-level difficulty bias. This skill normalizes reward signals across a group of G completions per prompt to ensure fair advantage estimates."
version: "0.1.0"
tags:
  - "grpo"
  - "reward_scaling"
  - "advantage_estimation"
  - "training_pipeline"
  - "reinforcement_learning"
triggers:
  - "After generating G completions per prompt"
  - "When reward scores are available for all completions in a batch"
  - "Before loss computation in GRPO training loop"
examples:
  - input: "G=4 completions with rewards [0.8, 0.5, 0.9, 0.6]; scale_rewards=True"
    output: "mean(r)=0.7, std(r)≈0.15; scaled advantages ≈ [0.67, -1.33, 1.33, -0.67] broadcast to token level"
    notes: "Normalization centers rewards and scales by variance, reducing bias from question difficulty"
  - input: "G=4 completions with rewards [0.8, 0.5, 0.9, 0.6]; scale_rewards=False"
    output: "Advantages = [0.8, 0.5, 0.9, 0.6] broadcast to token level without normalization"
    notes: "Raw rewards used directly; useful when reward distribution is already calibrated or uniform weighting is desired"
---

# GRPO Reward Scaling and Advantage Computation

Compute scaled advantages for each completion by normalizing rewards using standard deviation, with optional disable flag to prevent question-level difficulty bias. This skill normalizes reward signals across a group of G completions per prompt to ensure fair advantage estimates.

## Prompt

For each prompt with G completions and their corresponding reward scores:
1. Compute the mean and standard deviation of rewards across the completion group.
2. If scale_rewards=True (default), normalize each reward by subtracting the mean and dividing by std(r) to produce scaled advantages.
3. If scale_rewards=False, use raw rewards as advantages without normalization.
4. Output the advantage matrix indexed by completion and token position for downstream loss computation.

## Objective

Normalize and scale reward signals to compute fair advantage estimates across completion groups
## Applicable Signals

- Completion batch with reward scores assigned
- Training step ready to compute advantages
- GRPOConfig specifies scale_rewards setting

## Contraindications

- Do not apply if scale_rewards=False is set in GRPOConfig
- Do not use if reward distribution is already normalized upstream
- Do not apply if uniform weighting across completions is required by policy

## Workflow Steps

- {'step': 1, 'action': 'Collect reward scores for all G completions of a given prompt'}
- {'step': 2, 'action': 'Compute mean(r) and std(r) across the completion group'}
- {'step': 3, 'action': 'Check GRPOConfig.scale_rewards flag'}
- {'step': 4, 'action': 'If scale_rewards=True: normalize each reward as (r_i - mean(r)) / std(r)'}
- {'step': 5, 'action': 'If scale_rewards=False: use raw rewards r_i as advantages'}
- {'step': 6, 'action': 'Expand advantages to token level: replicate advantage value across all tokens in completion o_i'}

## Constraints

- Scaling by std(r) may introduce question-level difficulty bias; use scale_rewards=False to disable if bias is detected
- Standard deviation must be computed over the completion group, not globally across batches
- Advantage values must be computed per token position within each completion

## Cautions

- Verify that reward scores are valid and non-degenerate before computing std(r)
- If std(r) is zero or near-zero, scaling may produce NaN or Inf; handle gracefully or fall back to unscaled advantages

## Output Contract

- Scaled advantage matrix with shape [G, max_completion_length], where each entry a_{i,t} represents the advantage for token t in completion i. Advantages are ready for use in loss computation (e.g., GRPO loss or KL-penalized loss). Output must be numerically valid (no NaN or Inf unless explicitly handled).

## Example Therapist Responses

### Example 1

- Client/Input: G=4 completions with rewards [0.8, 0.5, 0.9, 0.6]; scale_rewards=True
- Therapist/Output: mean(r)=0.7, std(r)≈0.15; scaled advantages ≈ [0.67, -1.33, 1.33, -0.67] broadcast to token level
- Notes: Normalization centers rewards and scales by variance, reducing bias from question difficulty

### Example 2

- Client/Input: G=4 completions with rewards [0.8, 0.5, 0.9, 0.6]; scale_rewards=False
- Therapist/Output: Advantages = [0.8, 0.5, 0.9, 0.6] broadcast to token level without normalization
- Notes: Raw rewards used directly; useful when reward distribution is already calibrated or uniform weighting is desired

## Triggers

- After generating G completions per prompt
- When reward scores are available for all completions in a batch
- Before loss computation in GRPO training loop

## Examples

### Example 1

Input:

  G=4 completions with rewards [0.8, 0.5, 0.9, 0.6]; scale_rewards=True

Output:

  mean(r)=0.7, std(r)≈0.15; scaled advantages ≈ [0.67, -1.33, 1.33, -0.67] broadcast to token level

Notes:

  Normalization centers rewards and scales by variance, reducing bias from question difficulty

### Example 2

Input:

  G=4 completions with rewards [0.8, 0.5, 0.9, 0.6]; scale_rewards=False

Output:

  Advantages = [0.8, 0.5, 0.9, 0.6] broadcast to token level without normalization

Notes:

  Raw rewards used directly; useful when reward distribution is already calibrated or uniform weighting is desired
