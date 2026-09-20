---
id: "6dd07394-16b3-556f-9416-14758ccf43ba"
name: "GRPO Loss Formulation Selection"
description: "Select and apply the appropriate GRPO loss formulation (standard or DR-GRPO) based on task requirements and completion length normalization strategy. Computes scalar loss value from scaled advantages and KL divergence penalty for policy gradient updates."
version: "0.1.0"
tags:
  - "GRPO"
  - "loss_function"
  - "policy_gradient"
  - "training"
  - "configuration"
triggers:
  - "During backward pass in training loop; need to compute loss from scaled advantages and KL divergence penalty"
---

# GRPO Loss Formulation Selection

Select and apply the appropriate GRPO loss formulation (standard or DR-GRPO) based on task requirements and completion length normalization strategy. Computes scalar loss value from scaled advantages and KL divergence penalty for policy gradient updates.

## Prompt

During the backward pass in a GRPO training loop, choose between two loss formulations:
1. Standard GRPO: L_GRPO(θ) = -1/G ∑(i=1 to G) 1/|o_i| ∑(t=1 to |o_i|) l_{i,t}
2. DR-GRPO: Uses maximum completion length as normalization constant (set loss_type="dr_grpo" in GRPOConfig)

The loss combines scaled advantage (first term) and KL divergence penalty (second term). Ensure completion lengths are normalized and KL penalty weight is non-zero before applying.

## Objective

Apply correct loss function variant to compute policy gradient updates
## Applicable Signals

- Backward pass initiated in training loop
- Scaled advantages and KL divergence estimates available
- Batch of completions with varying lengths ready for loss computation

## Contraindications

- Do not mix loss formulations within a single training run
- Do not apply if completion lengths are not normalized
- Do not apply if KL penalty weight is zero
- Do not use without verified advantage scaling

## Intervention Moves

- Verify completion length normalization is applied
- Select loss formulation: standard GRPO or DR-GRPO variant
- Set loss_type parameter in GRPOConfig accordingly
- Compute scalar loss per batch
- Ensure gradient flow is ready for optimizer step

## Constraints

- Maximum completion length must be defined for DR-GRPO formulation
- Batch size G must be consistent across loss computation
- KL divergence penalty term must be non-zero

## Cautions

- Scaling by std(r) may cause question-level difficulty bias; disable with scale_rewards=False if needed
- Loss formulation choice affects gradient magnitude and training dynamics

## Output Contract

- Scalar loss value per batch; gradients computed and ready for optimizer step; loss value logged for monitoring

## Triggers

- During backward pass in training loop; need to compute loss from scaled advantages and KL divergence penalty
