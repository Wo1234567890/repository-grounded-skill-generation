---
id: "4f0a3132-518c-5793-a81e-0a9e22c9ec82"
name: "TF-IDF Variant Selection and Application"
description: "Select and apply an appropriate TF-IDF weighting scheme based on document term frequency distribution characteristics. Use when scoring documents with varying term frequency skewness to ensure consistent and contextually appropriate term weighting across a document collection."
version: "0.1.0"
tags:
  - "term_weighting"
  - "tf-idf"
  - "document_scoring"
  - "vector_space_model"
  - "information_retrieval"
triggers:
  - "Scoring documents with heterogeneous term distributions"
  - "Comparing documents with different frequency profiles"
  - "Implementing search ranking with weighted term importance"
---

# TF-IDF Variant Selection and Application

Select and apply an appropriate TF-IDF weighting scheme based on document term frequency distribution characteristics. Use when scoring documents with varying term frequency skewness to ensure consistent and contextually appropriate term weighting across a document collection.

## Prompt

Examine the term frequency distribution in the target document(s). Identify whether the distribution is skewed (one term dominates) or balanced (terms appear with similar frequency). Select a TF-IDF variant from the SMART notation family that matches the distribution profile. Apply the selected variant consistently across all documents in the collection. Verify that the resulting score vector reflects the chosen weighting scheme.

## Objective

Apply correct TF-IDF variant for document scoring based on term distribution characteristics
## Applicable Signals

- Document contains terms with highly skewed frequency distribution
- Query requires differentiation between documents with similar raw term counts
- Scoring system must account for term distribution variance

## Contraindications

- Raw term frequency counts are sufficient for the use case
- No weighting or normalization is required
- Binary relevance model is mandated by system constraints

## Workflow Steps

- {'step': 1, 'action': 'Analyze term frequency distribution', 'detail': 'Examine the frequency profile of terms in the document. Determine whether the distribution is skewed (one or few terms dominate) or balanced (terms appear with similar frequency).'}
- {'step': 2, 'action': 'Select TF-IDF variant', 'detail': 'Choose a variant from the SMART notation family (e.g., standard tf-idf, normalized variants, or pivoted schemes) that matches the observed distribution profile.'}
- {'step': 3, 'action': 'Apply variant formula', 'detail': 'Compute term weights using the selected TF-IDF formula for all terms in all documents.'}
- {'step': 4, 'action': 'Verify consistency', 'detail': 'Confirm that the weighting scheme has been applied uniformly across the document collection.'}

## Constraints

- Selected TF-IDF variant must be applied consistently across the entire document collection
- Variant choice must be documented for reproducibility
- Term frequency data must be available for all documents before variant selection

## Cautions

- Different TF-IDF variants produce different score magnitudes; do not compare scores across variants without normalization
- Variant selection should reflect the actual term distribution characteristics, not arbitrary preference

## Output Contract

- Document score vector computed using the selected TF-IDF variant; consistent weighting applied across the entire document collection; variant choice documented for audit and reproducibility.

## Triggers

- Scoring documents with heterogeneous term distributions
- Comparing documents with different frequency profiles
- Implementing search ranking with weighted term importance
