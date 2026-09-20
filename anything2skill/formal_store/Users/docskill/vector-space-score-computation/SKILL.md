---
id: "200a86bd-d5b2-5b5e-a7c6-46e9a7afb387"
name: "Vector Space Score Computation"
description: "Compute relevance scores between document vectors and query vectors using dot products. Use when ranking a collection of documents by similarity to a free-text query and producing ranked results."
version: "0.1.0"
tags:
  - "vector_space_model"
  - "scoring"
  - "ranking"
  - "dot_product"
  - "information_retrieval"
triggers:
  - "need to rank documents against a free-text query"
  - "documents and query are already vectorized"
  - "K top results are required"
---

# Vector Space Score Computation

Compute relevance scores between document vectors and query vectors using dot products. Use when ranking a collection of documents by similarity to a free-text query and producing ranked results.

## Prompt

Given a collection of documents each represented as a vector, a query represented as a vector, and a positive integer K:
1. Compute the dot product between the query vector and each document vector.
2. Sort documents by dot product score in descending order.
3. Return the top K documents with their computed scores.
This is the basic vector space scoring algorithm for information retrieval ranking.

## Objective

compute_vector_similarity_score
## Applicable Signals

- query vector available
- document collection vectorized
- K parameter specified

## Contraindications

- documents or queries are not vectorized
- boolean or exact-match retrieval is required
- similarity scoring is not the ranking criterion

## Workflow Steps

- Receive query vector, document vector collection, and K parameter
- For each document vector, compute dot product with query vector
- Sort documents by dot product score in descending order
- Select top K documents
- Return ranked list with scores

## Constraints

- all documents and query must be represented as vectors in the same dimensional space
- vector representations must be pre-computed before invoking this skill

## Output Contract

- Ranked list of K documents with computed similarity scores, ordered by relevance (highest score first). Each result includes document identifier and dot-product score.

## Triggers

- need to rank documents against a free-text query
- documents and query are already vectorized
- K top results are required
