---
id: "6c329aa8-3870-56d8-8428-f616f68a8393"
name: "TF Normalization Stability Assessment"
description: "Evaluate whether maximum tf normalization is suitable for a given retrieval system by assessing stop word list stability and presence of outlier terms. Identify when the method may cause ranking instability or misrepresentation of document content."
version: "0.1.0"
tags:
  - "term_weighting"
  - "tf_normalization"
  - "stability_check"
  - "information_retrieval"
  - "scoring"
triggers:
  - "Before deploying maximum tf normalization in a retrieval system"
  - "When stop word lists are subject to change or revision"
  - "When documents may contain outlier terms with unusually high frequencies"
---

# TF Normalization Stability Assessment

Evaluate whether maximum tf normalization is suitable for a given retrieval system by assessing stop word list stability and presence of outlier terms. Identify when the method may cause ranking instability or misrepresentation of document content.

## Prompt

Before deploying maximum tf normalization, check two stability conditions: (1) Is the stop word list fixed and unlikely to change? A change in stop word list can dramatically alter term weightings and ranking. (2) Are there outlier terms with unusually high frequencies that do not represent the document's actual content? If either condition is violated, maximum tf normalization is not recommended. Document your decision and reasoning.

## Objective

assess_tf_normalization_suitability
## Applicable Signals

- System design phase for term weighting
- Stop word list maintenance or updates planned
- Document collection with known high-frequency outlier terms

## Contraindications

- Stop word list is fixed and stable
- Document content is known to be uniform in term distribution
- Length normalization is already applied elsewhere in the pipeline

## Workflow Steps

- {'step': 1, 'action': 'Check stop word list stability', 'detail': 'Verify whether the stop word list is fixed and unlikely to change. Document the stability status.'}
- {'step': 2, 'action': 'Inspect document collection for outlier terms', 'detail': 'Sample documents and identify terms with unusually high frequencies that do not represent typical content.'}
- {'step': 3, 'action': 'Make go/no-go decision', 'detail': 'If both conditions are satisfied (stable stop word list and no problematic outliers), proceed with maximum tf normalization. Otherwise, recommend alternative normalization method.'}

## Constraints

- Assessment must occur before normalization is applied
- Stop word list stability must be explicitly verified
- Document sample must be reviewed for outlier term patterns

## Cautions

- Maximum tf normalization can cause ranking instability if stop word list changes
- Outlier terms with unusually high occurrences may not represent true document content
- The method is difficult to tune once deployed due to sensitivity to stop word changes

## Output Contract

- Go/no-go decision on whether to apply maximum tf normalization, with documented reasons. Examples: 'Stop word list is stable and no outlier terms detected—proceed with maximum tf normalization' or 'Stop word list subject to change—use alternative length normalization method' or 'Outlier terms present in collection—apply outlier detection before normalization'.

## Triggers

- Before deploying maximum tf normalization in a retrieval system
- When stop word lists are subject to change or revision
- When documents may contain outlier terms with unusually high frequencies
