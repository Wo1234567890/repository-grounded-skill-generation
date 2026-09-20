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
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
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

## 子技能目录
- [Reduce iterable into aggregated nested structure](通用技能领域/Family技能/未分类技能/微技能/Reduce iterable into aggregated nested structure/SKILL.md) ｜ 适用：Reduce an iterable into a nested Map or array by applying an aggregation function to grouped values. Combines grouping with reduction in a single operation, producing summary statistics or aggregate measures per group.
- [Select binning threshold rule](通用技能领域/Family技能/未分类技能/微技能/Select binning threshold rule/SKILL.md) ｜ 适用：Choose and apply one of three automatic binning rules (Freedman–Diaconis, Scott, or Sturges) to determine optimal bin boundaries for a sample dataset.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `Reduce iterable into aggregated nested structure` 时，优先调用它。 线索：Input is an iterable (array, set, or other iterable collection), You need to group data by one or more keys, You need to apply a reducer function (sum, count, mean, custom aggregation) to each group, Output should be a nested structure (Map or array) with one aggregated value per group, data_transformation
- 当目标、阶段或方法更接近 `Select binning threshold rule` 时，优先调用它。 线索：automatic threshold calculation is preferred, sample size and distribution are known, need reproducible binning, binning, threshold

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- need to convert continuous numeric samples into categorical bins
- preparing histogram data or frequency analysis
- discretizing measurement data for aggregation
