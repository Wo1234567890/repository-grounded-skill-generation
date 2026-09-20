---
id: "9d36d38a-138b-50cc-a1f9-4952a1a50161"
name: "Training Error Calculation for Zone Weight Validation"
description: "Evaluate classification error across all training examples by comparing weighted zone scores against binary relevance labels, accounting for all four combinations of Boolean match outcomes. Use to validate or tune zone weight parameters."
version: "0.1.0"
tags:
  - "zone_scoring"
  - "parameter_validation"
  - "error_aggregation"
  - "training_evaluation"
triggers:
  - "training set with relevance judgments exists"
  - "zone weight candidate needs evaluation"
  - "error-driven weight optimization is in progress"
---

# Training Error Calculation for Zone Weight Validation

Evaluate classification error across all training examples by comparing weighted zone scores against binary relevance labels, accounting for all four combinations of Boolean match outcomes. Use to validate or tune zone weight parameters.

## Prompt

For each training example (document, query) pair:
1. Compute the weighted zone score using the candidate zone weight g.
2. Compare the score against the binary relevance label (relevant=1, not relevant=0).
3. Record the error contribution for each of the four match combinations: (match in both zones, match in first only, match in second only, match in neither).
4. Aggregate all error contributions using the formula: (n01r + n10n) * g^2 + (n10r + n01n) * (1 - g)^2 + n00r + n11n.
5. Return the total error value for comparison across weight candidates.

## Objective

quantify total training error for a given zone weight
## Applicable Signals

- labeled training data available
- binary relevance judgments (0/1)
- candidate zone weight parameter ready for testing

## Contraindications

- no labeled training data
- real-time scoring without offline validation
- continuous relevance scores instead of binary labels

## Workflow Steps

- {'step': 1, 'action': 'Iterate over all training examples (d, q)'}
- {'step': 2, 'action': 'Compute weighted zone score for each example using candidate weight g'}
- {'step': 3, 'action': 'Compare score against binary relevance label; classify as correct or incorrect'}
- {'step': 4, 'action': 'Tally error contributions by match combination: n01r, n10n, n10r, n01n, n00r, n11n'}
- {'step': 5, 'action': 'Apply aggregation formula: (n01r + n10n) * g^2 + (n10r + n01n) * (1 - g)^2 + n00r + n11n'}
- {'step': 6, 'action': 'Return total error value'}

## Constraints

- training examples must have binary relevance labels
- zone weight g must be a scalar in valid range
- all four match combinations must be counted from training set

## Cautions

- error formula assumes exactly two zones; extend notation for more zones
- training set size and label distribution affect error magnitude

## Output Contract

- Total error count or error formula value (Equation 6.5 form) for the given weight; enables comparison across weight candidates and supports downstream weight optimization decisions.

## Triggers

- training set with relevance judgments exists
- zone weight candidate needs evaluation
- error-driven weight optimization is in progress
