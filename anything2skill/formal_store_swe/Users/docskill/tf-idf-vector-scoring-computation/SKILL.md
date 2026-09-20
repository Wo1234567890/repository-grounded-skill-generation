---
id: "381c3785-2b0d-524d-a6c6-138603a5b9dd"
name: "TF-IDF Vector Scoring Computation"
description: "Compute query-document relevance scores by combining term frequency, inverse document frequency, and normalized weights in vector space, using dot product of query and document vectors."
version: "0.1.0"
tags:
  - "information_retrieval"
  - "ranking"
  - "vector_space_model"
  - "tf_idf"
  - "scoring"
  - "relevance"
triggers:
  - "Ranking documents against a query in information retrieval"
  - "Term frequency and document frequency statistics are available"
  - "Bag-of-words retrieval model is in use"
examples:
  - input: "Query: 'digital video cameras'; Document collection with tf, df statistics for each term (e.g., digital: df=10,000; video: df=100,000; cameras: df=50,000)"
    output: "Ranked documents with scores computed as dot product of normalized query and document vectors; documents with higher qi · di scores ranked first"
    notes: "Illustrates multi-term query scoring with term weighting and normalization applied uniformly across all terms"
---

# TF-IDF Vector Scoring Computation

Compute query-document relevance scores by combining term frequency, inverse document frequency, and normalized weights in vector space, using dot product of query and document vectors.

## Prompt

For each query-document pair: (1) Extract term frequency (tf) and document frequency (df) from the collection. (2) Compute inverse document frequency (idf) for each term as log(N / df) where N is total document count. (3) Calculate query weight (qi) as tf × idf for each query term. (4) Normalize document weights (di) using cosine normalization or pivoted length normalization to account for document length bias. (5) Compute final relevance score as dot product qi · di. (6) Rank documents by descending score.

## Objective

compute relevance scores for ranked retrieval
## Applicable Signals

- Query submitted with multiple terms
- Document collection indexed with tf and df statistics
- Relevance ranking required for result presentation

## Contraindications

- Semantic or neural similarity is required
- Term order or linguistic context matters
- Very small collections where idf is unreliable

## Workflow Steps

- {'step': 1, 'action': 'Extract term frequency (tf) for each query term in each document'}
- {'step': 2, 'action': 'Retrieve document frequency (df) for each term from collection statistics'}
- {'step': 3, 'action': 'Compute inverse document frequency (idf) for each term, typically as log(N / df) where N is total document count'}
- {'step': 4, 'action': 'Calculate query weight (qi) for each term as tf × idf'}
- {'step': 5, 'action': 'Normalize document weights (di) using cosine normalization or pivoted length normalization to account for document length bias'}
- {'step': 6, 'action': 'Compute relevance score as dot product of query vector and document vector: qi · di'}
- {'step': 7, 'action': 'Sort documents by descending relevance score and return ranked list'}

## Constraints

- Document frequency must be available for all terms
- Collection statistics must be pre-computed or accessible
- Normalization scheme (cosine or pivoted) must be chosen before scoring

## Cautions

- IDF values may be unstable or zero for rare terms in small collections
- Pivoted normalization requires tuning of pivot parameter (piv) and slope (a); linear approximation form is a|V(d)| + (1 − a)piv
- Dot product assumes vector representation is complete and comparable

## Output Contract

- Ranked list of documents with computed relevance scores (qi · di) for each query-document pair, ordered by descending score. Each result includes the document identifier and its numeric relevance score.

## Example Executions

### Example 1

- Input: Query: 'digital video cameras'; Document collection with tf, df statistics for each term (e.g., digital: df=10,000; video: df=100,000; cameras: df=50,000)
- Output: Ranked documents with scores computed as dot product of normalized query and document vectors; documents with higher qi · di scores ranked first
- Notes: Illustrates multi-term query scoring with term weighting and normalization applied uniformly across all terms

## Triggers

- Ranking documents against a query in information retrieval
- Term frequency and document frequency statistics are available
- Bag-of-words retrieval model is in use

## Examples

### Example 1

Input:

  Query: 'digital video cameras'; Document collection with tf, df statistics for each term (e.g., digital: df=10,000; video: df=100,000; cameras: df=50,000)

Output:

  Ranked documents with scores computed as dot product of normalized query and document vectors; documents with higher qi · di scores ranked first

Notes:

  Illustrates multi-term query scoring with term weighting and normalization applied uniformly across all terms
