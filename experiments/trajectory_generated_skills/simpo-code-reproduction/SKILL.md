---
name: paper-to-code-simpo-loss
description: Reproduce a paper-defined preference-optimization loss from local paper evidence while preserving test inputs, checking log-probability semantics, and recording a reproducible environment.
---

# Paper-to-Code Reproduction for SimPO-Style Losses

## When to Use

Use this skill when implementing a mathematical loss from a paper inside an existing training repository and the result is checked with fixed tensors.

## Workflow

1. **Locate the exact equation in the supplied paper.** Write down every term and map each symbol to the repository/config variable before editing code.
2. **Inspect the call site and fixed test tensors.** Determine whether chosen/rejected log probabilities are token sums, sequence averages, or already length-normalized. Do not normalize twice.
3. **Resolve configuration semantics.** Identify the policy-temperature/scaling parameter and how the target margin is represented. Compute derived quantities from the config rather than hard-coding them.
4. **Use numerically stable primitives.** Implement the pairwise logistic objective with a stable log-sigmoid style operation rather than manually composing `log(sigmoid(...))` when the framework provides a stable primitive.
5. **Match the repository return contract.** If the trainer expects per-example losses plus chosen/rejected rewards, preserve their shapes, device, and dtype.
6. **Do not modify the supplied unit test.** Compatibility problems should be repaired in the implementation/environment, not hidden by rewriting the oracle.
7. **Run the provided fixed-input test and inspect the saved artifact.** Verify the required key exists, the array has the expected number of examples, and all values are finite.
8. **Record the environment.** Save the exact Python version and installed package versions after the final successful run so the numerical result can be reproduced.

## Trajectory-Derived Caution

A no-skill run derived a plausible paper equation, repaired several environment/import issues, and reported its local test as passing, yet the external task reward remained zero. Therefore do not treat a locally passing path as sufficient evidence. Re-check the paper equation, the meaning of the supplied log probabilities, and the expected interface before finalizing.

## Common Failure Modes

- Applying sequence-length normalization when the inputs are already averaged.
- Copying an equation without mapping paper notation to code variables.
- Editing the test to accommodate an implementation mismatch.
- Producing the output file but not checking its key, shape, dtype, and finiteness.
