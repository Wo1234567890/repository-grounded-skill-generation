---
id: "e6154a17-8de7-5c0e-a52e-7c4bef23ae8d"
name: "Select binning threshold rule"
description: "Choose and apply one of three automatic binning rules (Freedman–Diaconis, Scott, or Sturges) to determine optimal bin boundaries for a sample dataset."
version: "0.1.0"
tags:
  - "binning"
  - "threshold"
  - "statistical_rule"
  - "data_preparation"
triggers:
  - "automatic threshold calculation is preferred"
  - "sample size and distribution are known"
  - "need reproducible binning"
---

# Select binning threshold rule

Choose and apply one of three automatic binning rules (Freedman–Diaconis, Scott, or Sturges) to determine optimal bin boundaries for a sample dataset.

## Prompt

Invoke this skill when you need to compute bin thresholds automatically. Provide the sample array and select one of three statistical rules: Freedman–Diaconis (robust for skewed data), Scott (assumes normality), or Sturges (simple, works for small samples). The skill returns an array of numeric threshold values ready for use with bin.thresholds().

## Objective

compute bin thresholds
## Applicable Signals

- automatic threshold calculation is preferred
- sample size and distribution are known
- reproducible binning is required
- bin boundaries need statistical justification

## Contraindications

- custom thresholds are already defined
- bin count is fixed by external requirement
- data distribution is highly non-normal and standard rules fail

## Workflow Steps

- {'step': 1, 'action': 'Assess sample characteristics', 'detail': 'Examine sample size, distribution shape, and presence of outliers.'}
- {'step': 2, 'action': 'Select rule', 'detail': 'Choose Freedman–Diaconis for robustness to skew, Scott for near-normal data, or Sturges for small samples.'}
- {'step': 3, 'action': 'Compute thresholds', 'detail': 'Apply the selected rule to the sample array to generate threshold values.'}
- {'step': 4, 'action': 'Validate output', 'detail': 'Confirm thresholds are numeric, sorted, and span the data range.'}

## Constraints

- Sample array must be numeric and non-empty.
- Rule selection must be one of: thresholdFreedmanDiaconis, thresholdScott, thresholdSturges.
- Output thresholds must be compatible with bin.thresholds() API.

## Cautions

- Sturges rule may underestimate bins for large samples.
- Scott rule assumes approximate normality; use Freedman–Diaconis for skewed data.
- Extreme outliers can distort threshold calculations; consider data cleaning first.

## Output Contract

- Array of numeric threshold values suitable for bin.thresholds(), ordered ascending, spanning the observable data range.

## Triggers

- automatic threshold calculation is preferred
- sample size and distribution are known
- need reproducible binning
