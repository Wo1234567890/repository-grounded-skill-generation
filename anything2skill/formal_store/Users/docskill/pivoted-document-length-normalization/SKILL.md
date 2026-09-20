---
id: "06de6b44-7967-5591-9794-5d7436b643c3"
name: "Pivoted Document Length Normalization"
description: "Adjust TF-IDF relevance scores to correct for document length bias using linear scaling with an empirically-determined pivot point. Apply when longer documents are artificially favored in cosine-normalized relevance ranking and length variance is high across the collection."
version: "0.1.0"
tags:
  - "tf-idf"
  - "document_length_normalization"
  - "relevance_scoring"
  - "vector_space_model"
  - "score_adjustment"
triggers:
  - "document collection has high variance in document length"
  - "cosine normalization alone over-penalizes long documents"
  - "need to balance length bias with relevance"
---

# Pivoted Document Length Normalization

Adjust TF-IDF relevance scores to correct for document length bias using linear scaling with an empirically-determined pivot point. Apply when longer documents are artificially favored in cosine-normalized relevance ranking and length variance is high across the collection.

## Prompt

Compute normalized relevance scores using pivoted document length normalization. For each document, apply the linear scaling formula: score_normalized = a|V(d)| + (1-a)piv, where |V(d)| is the cosine-normalized score, piv is the pivot point (intersection of cosine curve and y=x line), and a is the slope parameter (0 < a < 1). The pivot point is typically determined empirically from the document collection. Return adjusted scores that balance length bias with relevance.

## Objective

normalize_by_document_length
## Applicable Signals

- document collection exhibits high variance in document length
- cosine normalization alone over-penalizes longer documents
- relevance ranking shows length bias favoring short documents
- need to balance document length as a confounding factor

## Contraindications

- all documents in collection are similar length
- document length is not a confounding factor in relevance
- using BM25 or other length-aware probabilistic models already
- collection is already balanced by length normalization

## Intervention Moves

- Compute cosine-normalized score |V(d)| for each document
- Determine pivot point piv from the document collection (intersection of cosine curve and y=x line)
- Select slope parameter a (0 < a < 1) based on desired length sensitivity
- Apply linear scaling: score_adjusted = a|V(d)| + (1-a)piv
- Return adjusted scores for ranking

## Constraints

- slope parameter a must satisfy 0 < a < 1
- pivot point piv must be computed from the same document collection
- input scores must be cosine-normalized before applying pivoted scaling
- method assumes linear relationship between document length and score adjustment

## Cautions

- pivot point selection is empirical; different collections may require different piv values
- slope parameter a controls sensitivity; lower a reduces length bias more aggressively
- this is a post-processing step; apply after initial TF-IDF computation

## Output Contract

- Adjusted relevance scores with linear scaling applied. Each score is computed as a|V(d)| + (1-a)piv. Output includes the normalization factor and adjusted score for each document, suitable for downstream ranking or retrieval tasks.

## Triggers

- document collection has high variance in document length
- cosine normalization alone over-penalizes long documents
- need to balance length bias with relevance
