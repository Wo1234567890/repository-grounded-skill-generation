---
id: "29ebd77d-cce6-5100-b5cc-15d9408a1608"
name: "TF-IDF Computation Under Morphological Stemming"
description: "Reference specification for modifying term frequency (tf) and inverse document frequency (idf) definitions when multiple surface forms are stemmed to a common root before vector space model setup. Provides canonical formulas for aggregating term frequencies across stemmed variants and counting document occurrences at the stem level."
version: "0.1.0"
tags:
  - "tf-idf"
  - "stemming"
  - "term_weighting"
  - "vector_space_model"
  - "text_preprocessing"
  - "information_retrieval"
triggers:
  - "implementing vector space model with stemming enabled; need to clarify how term frequency and inverse document frequency are computed when multiple surface forms map to one stem"
---

# TF-IDF Computation Under Morphological Stemming

Reference specification for modifying term frequency (tf) and inverse document frequency (idf) definitions when multiple surface forms are stemmed to a common root before vector space model setup. Provides canonical formulas for aggregating term frequencies across stemmed variants and counting document occurrences at the stem level.

## Prompt

When implementing a vector space model with stemming enabled, tf and idf calculations must account for merged term frequencies. For tf: sum the frequencies of all surface forms that map to the same stem within a document. For idf: count a document as containing the stem if any of its surface forms appears in that document, then compute idf based on the number of documents containing the stem (in any surface form). This ensures that stemmed terms are treated as a single logical term in the vector space.

## Objective

document how tf-idf formulas change under morphological stemming
## Applicable Signals

- implementing vector space model with stemming enabled
- need to clarify term frequency computation when multiple surface forms map to one stem
- need to clarify inverse document frequency computation under stemming

## Contraindications

- no stemming is applied to the corpus
- working with pre-computed tf-idf weights that already account for stemming
- using character-level or subword tokenization instead of morphological stemming

## Constraints

- applies only to morphological stemming workflows
- assumes all surface form variants are mapped to a common stem before tf-idf computation

## Output Contract

- clear specification of how tf counts aggregate across stemmed term variants and how idf calculations incorporate document-level stem occurrence, enabling correct vector space setup

## Triggers

- implementing vector space model with stemming enabled; need to clarify how term frequency and inverse document frequency are computed when multiple surface forms map to one stem
