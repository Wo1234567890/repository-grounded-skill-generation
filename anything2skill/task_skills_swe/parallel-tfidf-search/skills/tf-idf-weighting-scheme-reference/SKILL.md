---
id: "e09c1822-2358-538a-8224-1117669fb5c9"
name: "TF-IDF Weighting Scheme Reference"
description: "Reference guide for understanding and applying tf-idf (term frequency–inverse document frequency) weighting. Explains how to combine normalized term frequency with log-scaled inverse document frequency to balance common and rare terms in document scoring and vector space models."
version: "0.1.0"
tags:
  - "tf-idf"
  - "term_weighting"
  - "document_scoring"
  - "vector_space_model"
  - "information_retrieval"
  - "euclidean_normalization"
triggers:
  - "selecting a term weighting strategy for document representation"
  - "need to understand trade-offs between raw frequency, normalized frequency, and inverse document frequency"
examples:
  - input: "Three novels: Sense and Sensibility (SaS), Pride and Prejudice (PaP), Wuthering Heights (WH). Raw term frequencies for 'affection': SaS=115, PaP=58, WH=20."
    output: "After Euclidean normalization: SaS≈0.996, PaP≈0.993, WH≈0.847. These normalized values are then multiplied by IDF(affection) to produce final tf-idf scores."
    notes: "Normalization reduces the impact of document length; IDF further adjusts based on term rarity across the corpus."
---

# TF-IDF Weighting Scheme Reference

Reference guide for understanding and applying tf-idf (term frequency–inverse document frequency) weighting. Explains how to combine normalized term frequency with log-scaled inverse document frequency to balance common and rare terms in document scoring and vector space models.

## Prompt

Use this reference to understand tf-idf weighting rationale and formulas. TF-IDF combines term frequency (how often a term appears in a document) with inverse document frequency (how rare the term is across all documents). Raw term frequency counts are normalized by document length (e.g., Euclidean normalization), then multiplied by IDF (typically log-scaled) to down-weight globally common terms and up-weight rare, discriminative terms. Refer to section 6.2.1 for IDF definition and section 6.2.2 for complete tf-idf formulas and worked examples.

## Objective

provide tf-idf weighting rationale, formula reference, and normalization trade-offs
## Applicable Signals

- selecting a term weighting strategy for document representation
- need to understand trade-offs between raw frequency, normalized frequency, and inverse document frequency
- designing a scoring function for document retrieval or similarity
- implementing vector space model document scoring

## Contraindications

- weighting scheme is already fixed by system requirements
- domain-specific weighting (e.g., zone-based or learned weights) is mandated
- real-time performance constraints prohibit IDF computation

## Constraints

- IDF requires corpus-level statistics; must be computed or pre-computed before application
- normalized term frequencies assume document length normalization (e.g., Euclidean normalization)
- log-scaling of IDF assumes positive document counts

## Output Contract

- Clear understanding of when and how to apply tf-idf
- Ability to reference detailed formulas and worked examples from section 6.2.1 (Inverse document frequency) and section 6.2.2 (Tf-idf weighting)
- Understanding of normalized vs. raw term frequency trade-offs
- Ability to apply Euclidean normalization to raw term frequencies before IDF multiplication

## Example Executions

### Example 1

- Input: Three novels: Sense and Sensibility (SaS), Pride and Prejudice (PaP), Wuthering Heights (WH). Raw term frequencies for 'affection': SaS=115, PaP=58, WH=20.
- Output: After Euclidean normalization: SaS≈0.996, PaP≈0.993, WH≈0.847. These normalized values are then multiplied by IDF(affection) to produce final tf-idf scores.
- Notes: Normalization reduces the impact of document length; IDF further adjusts based on term rarity across the corpus.

## Triggers

- selecting a term weighting strategy for document representation
- need to understand trade-offs between raw frequency, normalized frequency, and inverse document frequency

## Examples

### Example 1

Input:

  Three novels: Sense and Sensibility (SaS), Pride and Prejudice (PaP), Wuthering Heights (WH). Raw term frequencies for 'affection': SaS=115, PaP=58, WH=20.

Output:

  After Euclidean normalization: SaS≈0.996, PaP≈0.993, WH≈0.847. These normalized values are then multiplied by IDF(affection) to produce final tf-idf scores.

Notes:

  Normalization reduces the impact of document length; IDF further adjusts based on term rarity across the corpus.
