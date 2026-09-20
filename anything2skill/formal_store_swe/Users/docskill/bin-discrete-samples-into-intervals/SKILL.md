---
id: "4191ada7-49db-519c-9a22-369a1e0a83fa"
name: "Bin discrete samples into intervals"
description: "Create and configure a bin generator to partition continuous sample data into non-overlapping intervals using specified thresholds or automatic binning rules."
version: "0.1.0"
tags:
  - "data_preparation"
  - "discretization"
  - "histogram"
  - "binning"
  - "frequency_analysis"
triggers:
  - "need to convert continuous numeric samples into categorical bins"
  - "preparing histogram data or frequency analysis"
  - "discretizing measurement data for aggregation"
---

# Bin discrete samples into intervals

Create and configure a bin generator to partition continuous sample data into non-overlapping intervals using specified thresholds or automatic binning rules.

## Prompt

Use this skill to convert continuous numeric samples into categorical bins for histogram preparation or frequency analysis. Configure the bin generator with a value accessor, observable domain, and threshold strategy (manual or automatic rule). Execute the generator on your sample array to produce bin objects with boundaries and contained values.

## Objective

partition samples into bins
## Applicable Signals

- input is array of continuous numeric samples
- downstream task requires categorical or grouped data
- histogram or frequency distribution is the goal

## Contraindications

- data is already categorical
- bins must overlap
- sample array is empty or unsorted

## Workflow Steps

- Create a new bin generator instance
- Configure value accessor to extract numeric values from each sample
- Specify the observable domain (min and max values)
- Select threshold strategy: manual array, Freedman–Diaconis rule, Scott's rule, or Sturges' formula
- Execute the generator on the sample array
- Collect output bin objects containing boundaries and grouped samples

## Constraints

- samples must be numeric
- domain must encompass all observable values
- thresholds must be monotonically increasing

## Cautions

- Ensure domain bounds are inclusive of all sample values to avoid samples falling outside bins
- Automatic threshold rules (Freedman–Diaconis, Scott, Sturges) assume approximately normal distributions; verify appropriateness for skewed data
- Large sample arrays may produce many bins; consider threshold strategy to balance granularity and interpretability

## Output Contract

- Array of bin objects, each containing sample values and bin boundaries; bins are continuous and non-overlapping; all input samples are assigned to exactly one bin.

## Triggers

- need to convert continuous numeric samples into categorical bins
- preparing histogram data or frequency analysis
- discretizing measurement data for aggregation
