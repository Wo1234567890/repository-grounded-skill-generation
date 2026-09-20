---
id: "64cce2b8-b74d-5be9-98d6-e4ea5687643a"
name: "Euclidean Normalization of Term Frequency Vectors"
description: "Normalize raw term frequency vectors by dividing each component by the vector's Euclidean norm. Produces unit-length vectors suitable for scale-invariant dot-product similarity computation across documents of different lengths."
version: "0.1.0"
tags:
  - "vector_space_model"
  - "term_weighting"
  - "normalization"
  - "preprocessing"
  - "information_retrieval"
  - "cosine_similarity"
triggers:
  - "Raw term frequency counts are available for one or more documents"
  - "Documents have different lengths and need fair comparison"
  - "Dot-product similarity will be computed downstream"
examples:
  - input: "Raw term frequency vector for document: affection=115, jealous=10, gossip=2"
    output: "Normalized vector: affection≈0.996, jealous≈0.087, gossip≈0.017 (unit Euclidean length)"
    notes: "Normalization makes documents of different lengths comparable; longer documents no longer dominate similarity scores. Example from three novels: Sense and Sensibility, Pride and Prejudice, and Wuthering Heights."
---

# Euclidean Normalization of Term Frequency Vectors

Normalize raw term frequency vectors by dividing each component by the vector's Euclidean norm. Produces unit-length vectors suitable for scale-invariant dot-product similarity computation across documents of different lengths.

## Prompt

Given a raw term frequency vector ~v(d) with components for each term in a document, compute the Euclidean norm |~v(d)| = sqrt(sum of squared components). Divide each component by this norm to produce a unit-length normalized vector ~v(d) / |~v(d)|. This normalized vector is then suitable for dot-product similarity computation.

## Objective

normalize_term_vectors
## Applicable Signals

- have raw term frequency counts
- need to compare documents of different lengths fairly
- preparing vectors for cosine similarity or dot-product scoring

## Contraindications

- Vectors are already normalized
- Only raw frequency ranking is acceptable without normalization
- Scale-invariance is not required for the use case

## Workflow Steps

- {'step': 1, 'action': 'Extract raw term frequency vector ~v(d) from document', 'detail': 'Collect term occurrence counts for all terms in vocabulary'}
- {'step': 2, 'action': 'Compute Euclidean norm', 'detail': 'Calculate |~v(d)| = sqrt(sum of v_i^2 for all components v_i)'}
- {'step': 3, 'action': 'Normalize each component', 'detail': 'Divide each component by the norm: v_i_normalized = v_i / |~v(d)|'}
- {'step': 4, 'action': 'Verify unit length', 'detail': 'Confirm that the normalized vector has Euclidean length 1.0 (within numerical precision)'}

## Constraints

- Input must be a valid term frequency vector with non-negative numeric components
- Euclidean norm must be non-zero (empty or zero-only vectors cannot be normalized)

## Cautions

- Ensure all term frequencies are non-negative before normalization
- Handle zero-norm vectors explicitly (e.g., documents with no terms) to avoid division by zero

## Output Contract

- A normalized vector with unit Euclidean length, ready for dot-product similarity computation. Each component is scaled such that the vector's magnitude equals 1.0. Output enables direct dot-product similarity via sim(d1, d2) = ~v(d1) · ~v(d2).

## Example Therapist Responses

### Example 1

- Client/Input: Raw term frequency vector for document: affection=115, jealous=10, gossip=2
- Therapist/Output: Normalized vector: affection≈0.996, jealous≈0.087, gossip≈0.017 (unit Euclidean length)
- Notes: Normalization makes documents of different lengths comparable; longer documents no longer dominate similarity scores. Example from three novels: Sense and Sensibility, Pride and Prejudice, and Wuthering Heights.

## Triggers

- Raw term frequency counts are available for one or more documents
- Documents have different lengths and need fair comparison
- Dot-product similarity will be computed downstream

## Examples

### Example 1

Input:

  Raw term frequency vector for document: affection=115, jealous=10, gossip=2

Output:

  Normalized vector: affection≈0.996, jealous≈0.087, gossip≈0.017 (unit Euclidean length)

Notes:

  Normalization makes documents of different lengths comparable; longer documents no longer dominate similarity scores. Example from three novels: Sense and Sensibility, Pride and Prejudice, and Wuthering Heights.
