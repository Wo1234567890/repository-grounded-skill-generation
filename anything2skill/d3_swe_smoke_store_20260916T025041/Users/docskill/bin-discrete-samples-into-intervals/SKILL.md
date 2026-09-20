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

Use this skill to convert continuous numeric samples into categorical bins for histogram preparation or frequency analysis. Configure the bin generator with a value accessor, observable domain, and threshold strategy (manual or automatic rule). Execute to obtain an array of bin objects containing sample values and boundaries.

## Objective

partition samples into bins
## Applicable Signals

- continuous numeric array provided
- histogram or frequency distribution required
- sample data ready for binning

## Contraindications

- data is already categorical
- bins must overlap
- sample array is empty or unsorted

## Workflow Steps

- {'step': 1, 'action': 'Create bin generator', 'detail': 'Instantiate a new bin generator object.'}
- {'step': 2, 'action': 'Configure value accessor', 'detail': 'Specify bin.value to extract numeric values from each sample if samples are objects.'}
- {'step': 3, 'action': 'Set observable domain', 'detail': 'Define bin.domain with [min, max] interval of observable values.'}
- {'step': 4, 'action': 'Choose threshold strategy', 'detail': 'Select bin.thresholds using manual array, thresholdFreedmanDiaconis, thresholdScott, or thresholdSturges.'}
- {'step': 5, 'action': 'Execute binning', 'detail': 'Call bin() on the sample array to produce array of bin objects.'}

## Constraints

- input must be a numeric array
- domain interval must encompass all sample values
- thresholds must be monotonically increasing

## Cautions

- Ensure domain covers all sample values to avoid samples falling outside bins.
- Automatic threshold rules (Freedman–Diaconis, Scott, Sturges) assume approximately normal distributions; verify appropriateness for skewed data.
- Empty bins are included in output; filter if needed downstream.

## Output Contract

- Array of bin objects, each containing sample values assigned to that bin and bin boundary information (lower and upper thresholds).

## Triggers

- need to convert continuous numeric samples into categorical bins
- preparing histogram data or frequency analysis
- discretizing measurement data for aggregation
