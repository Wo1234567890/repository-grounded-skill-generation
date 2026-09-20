---
id: "4ade660e-a147-5983-b0ee-cf422dcbf2f7"
name: "Cosine Similarity Scoring via Dot Product"
description: "Compute similarity between two normalized document vectors by taking their dot product, yielding a score in [0, 1] that reflects term overlap and relative term importance."
version: "0.1.0"
tags:
  - "vector_space_model"
  - "information_retrieval"
  - "similarity_metric"
  - "dot_product"
  - "cosine_similarity"
  - "document_ranking"
triggers:
  - "Two normalized document vectors are available in the same term space"
  - "A single scalar similarity score is needed for ranking or clustering"
  - "Vectors have been preprocessed (normalized) and are ready for comparison"
examples:
  - input: "Normalized vectors for two documents: v(d1) = [0.996, 0.087, 0.017], v(d2) = [0.993, 0.120, 0.0]"
    output: "sim(d1, d2) ≈ 0.989 (high similarity)"
    notes: "Computed as dot product of normalized term frequency vectors from literary texts (Austen's Sense and Sensibility vs. Pride and Prejudice)"
  - input: "Normalized vectors: v(d1) = [0.847, 0.466, 0.254], v(d2) = [0.0, 0.0, 1.0]"
    output: "sim(d1, d2) = 0.254 (low similarity)"
    notes: "Demonstrates orthogonal or near-orthogonal term distributions (Brontë's Wuthering Heights vs. term-sparse document)"
---

# Cosine Similarity Scoring via Dot Product

Compute similarity between two normalized document vectors by taking their dot product, yielding a score in [0, 1] that reflects term overlap and relative term importance.

## Prompt

Given two normalized document vectors in the same term space, compute their dot product to obtain a scalar similarity score. The result represents the cosine of the angle between the vectors and ranges from 0 (orthogonal/dissimilar) to 1 (parallel/identical).

## Objective

compute pairwise document similarity
## Applicable Signals

- Normalized vector pair ready for scoring
- Ranking or clustering task initiated
- Term-based document comparison required

## Contraindications

- Vectors are not normalized
- Sparse representations require special handling beyond dot product
- Similarity must account for term order or syntactic structure
- Vectors are in different term spaces or have incompatible dimensions

## Workflow Steps

- {'step': 1, 'action': 'Verify both input vectors are normalized (Euclidean norm = 1)', 'validation': 'Check that |v(d1)| = 1 and |v(d2)| = 1'}
- {'step': 2, 'action': 'Compute dot product of the two vectors', 'validation': 'Sum of element-wise products across all term dimensions'}
- {'step': 3, 'action': 'Return scalar result as similarity score', 'validation': 'Score must be in range [0, 1]'}

## Constraints

- Both input vectors must be normalized (unit length)
- Both vectors must span the same term vocabulary
- Dimensionality must match across both vectors

## Cautions

- Dot product of non-normalized vectors will not yield a valid cosine similarity
- Result is symmetric: sim(d1, d2) = sim(d2, d1)
- Score of 0 indicates orthogonal vectors, not necessarily dissimilar documents in semantic terms

## Output Contract

- Scalar similarity score between 0 and 1, representing the cosine of the angle between the two normalized vectors. Score of 1 indicates identical direction; 0 indicates orthogonality.

## Example Executions

### Example 1

- Input: Normalized vectors for two documents: v(d1) = [0.996, 0.087, 0.017], v(d2) = [0.993, 0.120, 0.0]
- Output: sim(d1, d2) ≈ 0.989 (high similarity)
- Notes: Computed as dot product of normalized term frequency vectors from literary texts (Austen's Sense and Sensibility vs. Pride and Prejudice)

### Example 2

- Input: Normalized vectors: v(d1) = [0.847, 0.466, 0.254], v(d2) = [0.0, 0.0, 1.0]
- Output: sim(d1, d2) = 0.254 (low similarity)
- Notes: Demonstrates orthogonal or near-orthogonal term distributions (Brontë's Wuthering Heights vs. term-sparse document)

## Triggers

- Two normalized document vectors are available in the same term space
- A single scalar similarity score is needed for ranking or clustering
- Vectors have been preprocessed (normalized) and are ready for comparison

## Examples

### Example 1

Input:

  Normalized vectors for two documents: v(d1) = [0.996, 0.087, 0.017], v(d2) = [0.993, 0.120, 0.0]

Output:

  sim(d1, d2) ≈ 0.989 (high similarity)

Notes:

  Computed as dot product of normalized term frequency vectors from literary texts (Austen's Sense and Sensibility vs. Pride and Prejudice)

### Example 2

Input:

  Normalized vectors: v(d1) = [0.847, 0.466, 0.254], v(d2) = [0.0, 0.0, 1.0]

Output:

  sim(d1, d2) = 0.254 (low similarity)

Notes:

  Demonstrates orthogonal or near-orthogonal term distributions (Brontë's Wuthering Heights vs. term-sparse document)
