---
id: "a2669a09-9c8a-5963-b000-43f3926bfa24"
name: "Weighted Zone Scoring Parameter Optimization"
description: "Compute the optimal zone weight parameter g for two-zone document scoring by minimizing classification error on training data. Use this micro-skill when you have binary relevance judgments and zone-based Boolean match scores, and need to learn a single weight parameter that balances contributions from two document zones (T and B)."
version: "0.1.0"
tags:
  - "information_retrieval"
  - "scoring"
  - "parameter_learning"
  - "zone_weighting"
  - "training"
  - "optimization"
triggers:
  - "Training data with binary relevance judgments and zone-based Boolean match scores are available"
  - "Need to learn single weight parameter g for two-zone scoring"
---

# Weighted Zone Scoring Parameter Optimization

Compute the optimal zone weight parameter g for two-zone document scoring by minimizing classification error on training data. Use this micro-skill when you have binary relevance judgments and zone-based Boolean match scores, and need to learn a single weight parameter that balances contributions from two document zones (T and B).

## Prompt

Given training examples with binary relevance judgments (relevant=1 or not relevant=0) and zone-based Boolean match scores for two zones T and B, derive the optimal weight parameter g that minimizes total classification error. Count training examples by (s_T, s_B, relevance) combination into eight categories: n00r, n00n, n01r, n01n, n10r, n10n, n11r, n11n. Apply Equation 6.6: g = (n10r + n01n) / (n10r + n10n + n01r + n01n). Verify g ∈ [0, 1]. The resulting parameter is used in weighted zone scoring: score(d, q) = g × s_T(d, q) + (1 − g) × s_B(d, q).

## Objective

derive_optimal_weight_parameter
## Applicable Signals

- Training dataset with binary relevance judgments is available
- Zone-based Boolean match scores (s_T and s_B) computed for all training examples
- Need to learn single weight parameter for two-zone weighted scoring

## Contraindications

- Do not use if zones require independent weights (use multi-parameter learning instead)
- Do not use if no training data with relevance judgments is available
- Do not use if relevance judgments are continuous rather than binary
- Do not use if Boolean match functions differ significantly across zones in ways that require separate calibration

## Intervention Moves

- Count training examples by (s_T, s_B, relevance) combination: n00r, n00n, n01r, n01n, n10r, n10n, n11r, n11n
- Apply differentiation of error function (Equation 6.5) with respect to g
- Compute g using the closed-form formula from Equation 6.6

## Workflow Steps

- {'step': 1, 'action': 'Prepare training data', 'detail': 'Ensure all training examples have binary relevance judgments (0/1) and computed zone-based Boolean match scores for zones T and B'}
- {'step': 2, 'action': 'Count error contributions', 'detail': 'For each training example, record the combination of (s_T value, s_B value, relevance label) and count occurrences in each of the eight categories: n00r, n00n, n01r, n01n, n10r, n10n, n11r, n11n'}
- {'step': 3, 'action': 'Apply formula', 'detail': 'Compute g = (n10r + n01n) / (n10r + n10n + n01r + n01n) using the counts from step 2'}
- {'step': 4, 'action': 'Validate result', 'detail': 'Verify that g is in [0, 1]; if denominator is zero, flag as indeterminate and consider alternative weighting strategy'}

## Constraints

- Parameter g must be in range [0, 1]
- Training set must include examples covering all four combinations of (s_T, s_B) values
- Relevance judgments must be quantized to binary (0/1) before counting

## Cautions

- If denominator in Equation 6.6 is zero, all training examples have matching zone scores; parameter is indeterminate
- Small training sets may produce unstable g estimates; consider cross-validation

## Output Contract

- Scalar parameter g in range [0, 1] that minimizes total classification error on the training set. This parameter is then used in weighted zone scoring formula: score(d, q) = g × s_T(d, q) + (1 − g) × s_B(d, q).

## Triggers

- Training data with binary relevance judgments and zone-based Boolean match scores are available
- Need to learn single weight parameter g for two-zone scoring
