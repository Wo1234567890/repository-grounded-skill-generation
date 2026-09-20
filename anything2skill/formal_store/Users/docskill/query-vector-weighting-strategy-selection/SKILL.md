---
id: "9976a13f-e55c-52ac-9885-28a9cbf0756f"
name: "Query Vector Weighting Strategy Selection"
description: "Choose and apply a query term weighting scheme (binary presence or Euclidean-normalized idf) to construct query vectors for scoring against document vectors in vector space model retrieval."
version: "0.1.0"
tags:
  - "vector_space_model"
  - "query_processing"
  - "term_weighting"
  - "information_retrieval"
  - "scoring"
triggers:
  - "Preparing a query for vector space model retrieval"
  - "Need to decide query term weighting scheme before scoring"
  - "Query vector construction required for dot-product similarity computation"
---

# Query Vector Weighting Strategy Selection

Choose and apply a query term weighting scheme (binary presence or Euclidean-normalized idf) to construct query vectors for scoring against document vectors in vector space model retrieval.

## Prompt

When preparing a query for vector space scoring, decide whether to weight query terms using: (1) binary presence (weight=1 if term present, 0 otherwise), or (2) Euclidean-normalized idf weights. Apply the selected scheme to construct the query vector, ensuring it is compatible with the document vector representation already computed. The choice affects ranking outcomes and should align with document weighting strategy.

## Objective

construct_query_vector
## Applicable Signals

- Query terms identified and matched against vocabulary
- Document vectors already computed with known weighting (tf-idf or other)
- Retrieval task requires ranking documents by vector similarity

## Contraindications

- Using non-vector-based retrieval models (e.g., Boolean, probabilistic)
- Query term weights are externally specified or fixed by system policy
- Query representation is not vector-compatible

## Workflow Steps

- {'step': 1, 'action': 'Identify query terms and check presence in vocabulary'}
- {'step': 2, 'action': 'Select weighting strategy: binary presence or Euclidean-normalized idf'}
- {'step': 3, 'action': 'If binary: assign weight 1 to present terms, 0 to absent terms'}
- {'step': 4, 'action': 'If Euclidean-normalized idf: retrieve idf value for each query term and apply normalization'}
- {'step': 5, 'action': 'Construct query vector with selected weights, aligned to document vector dimensions'}
- {'step': 6, 'action': 'Verify vector is ready for dot-product scoring against document vectors'}

## Constraints

- Query vector dimensionality must match document vector dimensionality
- Weighting scheme must be consistent with or complementary to document weighting
- If Euclidean normalization is chosen, idf values must be available for all query terms

## Cautions

- Binary weighting loses term frequency information; suitable for short queries or when term presence matters more than frequency
- Euclidean-normalized idf weighting requires pre-computed idf values; ensure idf computation matches document collection
- Mismatch between query and document weighting strategies may degrade ranking quality

## Output Contract

- Query vector with selected weighting scheme applied, dimensionally aligned with document vectors, ready for dot-product similarity scoring and document ranking

## Triggers

- Preparing a query for vector space model retrieval
- Need to decide query term weighting scheme before scoring
- Query vector construction required for dot-product similarity computation
