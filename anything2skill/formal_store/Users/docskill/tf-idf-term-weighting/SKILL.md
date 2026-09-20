---
id: "4e22b826-65c9-5565-bac4-3e59e060330b"
name: "TF-IDF Term Weighting"
description: "Compute term frequency (TF) and inverse document frequency (IDF) weights to score document relevance in information retrieval systems. Use when ranking documents by query match or constructing vector space models for similarity computation."
version: "0.1.0"
tags:
  - "information_retrieval"
  - "term_weighting"
  - "vector_space_model"
  - "document_scoring"
  - "statistical_weighting"
triggers:
  - "need to weight terms in documents for relevance ranking or vector space model construction"
---

# TF-IDF Term Weighting

Compute term frequency (TF) and inverse document frequency (IDF) weights to score document relevance in information retrieval systems. Use when ranking documents by query match or constructing vector space models for similarity computation.

## Prompt

Apply TF-IDF weighting to term occurrences in a document collection. For each term in a document, calculate term frequency (count or normalized frequency within the document) and inverse document frequency (logarithmic measure of how rare the term is across the collection). Multiply TF and IDF to produce a composite weight that emphasizes terms that are frequent in a target document but rare overall. Use these weights to build term vectors for downstream similarity or ranking operations.

## Objective

term_weighting_and_scoring
## Applicable Signals

- need to weight terms in documents for relevance ranking
- constructing vector space model for document similarity
- scoring documents against a query in a ranked retrieval task

## Contraindications

- working with unstructured narrative text without clear document boundaries
- when term frequency is not meaningful or documents lack discrete term occurrences
- when document collection is too small to compute meaningful IDF values

## Intervention Moves

- Calculate term frequency for each term in the document
- Calculate inverse document frequency across the collection
- Multiply TF and IDF to produce composite weight
- Normalize weights if needed for downstream vector operations

## Constraints

- Requires a well-defined document collection with term boundaries
- IDF calculation depends on document frequency statistics across the full collection
- Term weighting assumes terms are independent and additive in relevance contribution

## Cautions

- Very common terms (stop words) may receive low IDF weights; consider filtering or smoothing
- IDF values must be recomputed if the document collection changes significantly

## Output Contract

- Weighted term vectors (one vector per document) with TF-IDF scores for each term, suitable for similarity computation, document ranking, or input to vector space model operations.

## Triggers

- need to weight terms in documents for relevance ranking or vector space model construction
