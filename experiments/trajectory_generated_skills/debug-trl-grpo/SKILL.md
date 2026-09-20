---
name: grpo-training-debugging
description: Debug GRPO training code when rewards exist but model quality does not improve, with emphasis on advantage scaling, numerical stability, and protected training interfaces.
---

# GRPO Training Debugging

## When to Use

Use this skill when a GRPO or related reinforcement-learning training run executes but shows little or no learning, especially when the training script and reward function are fixed and the bug must be found inside the trainer/library implementation.

## Workflow

1. **Map the learning signal end to end.** Start from raw rewards and trace how they are grouped, centered, scaled, converted into advantages, and finally used in the policy loss. A run that merely completes is not evidence that gradients are meaningful.
2. **Inspect normalization denominators closely.** Compare any reward/advantage scaling expression against its intended numerical role. A stabilizing epsilon must be small enough to prevent division by zero without dominating the empirical standard deviation.
3. **Use magnitude checks, not just code reading.** Construct a tiny synthetic reward group and print the raw rewards, mean, standard deviation, normalized advantages, and resulting scale. If advantages collapse by orders of magnitude, the optimizer can receive an effectively useless signal even though the code has no exception.
4. **Search the full trainer path for related scaling.** A no-skill trajectory found a suspicious very-large additive constant in advantage normalization and received only partial credit after fixing that one site. Treat a single obvious constant as a lead, not proof that the entire trainer is correct.
5. **Respect protected files.** Do not solve a library bug by changing the supplied training script or reward function. Keep the repair inside the implementation under test.
6. **Check configuration gates.** Verify whether reward scaling is enabled by default, how grouped rewards are formed, and whether zero-variance groups have a defined fallback.
7. **Validate behavior after the patch.** Run a focused unit or synthetic check that demonstrates non-degenerate advantages, then run the provided training path far enough to confirm the repaired code is exercised.

## Good Debugging Evidence

A strong diagnosis states: the exact computation that attenuates or corrupts the learning signal; the expected numerical scale; a small reproducible example; and a minimal patch that restores the intended scale without changing experiment inputs.

## Common Failure Modes

- Treating "training runs" as equivalent to "training learns."
- Fixing only the first suspicious line and stopping without checking the rest of the reward-to-loss path.
- Changing hyperparameters or the reward function when the task asks for a trainer implementation bug.
- Using an epsilon large enough to dominate the statistic it is supposed to stabilize.
