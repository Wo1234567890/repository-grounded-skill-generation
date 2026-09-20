---
id: "ef111038-016e-5db2-ba06-72467dd2903d"
name: "TF-IDF Adjustment for Stemmed Terms"
description: "Reference specification for how term frequency (tf) and inverse document frequency (idf) definitions must be modified when terms are stemmed to a common root before vector space construction. Clarifies that stemming merges multiple surface forms into one canonical stem, requiring recalculation of both tf (now counting all surface form occurrences under the stem) and idf (now based on documents containing any surface form of the stem)."
version: "0.1.0"
tags:
  - "tf-idf"
  - "stemming"
  - "term_weighting"
  - "vector_space_model"
  - "information_retrieval"
  - "indexing"
triggers:
  - "Implementing tf-idf in a system that applies stemming; need to clarify how term frequency and document frequency should be recalculated"
---

# TF-IDF Adjustment for Stemmed Terms

Reference specification for how term frequency (tf) and inverse document frequency (idf) definitions must be modified when terms are stemmed to a common root before vector space construction. Clarifies that stemming merges multiple surface forms into one canonical stem, requiring recalculation of both tf (now counting all surface form occurrences under the stem) and idf (now based on documents containing any surface form of the stem).

## Prompt

When implementing tf-idf weighting in a stemming-enabled system, recognize that stemming collapses multiple term variants into a single stem before indexing. This changes how tf and idf are defined: (1) tf for a stem is the sum of frequencies of all surface forms that map to that stem within a document; (2) idf for a stem is based on the count of documents containing any surface form of that stem, not individual variants. Apply these adjusted definitions consistently when computing vector space weights.

## Objective

understand_stemming_impact
## Applicable Signals

- System applies stemming before or during indexing
- Need to clarify tf-idf formula behavior under stemming
- Multiple surface forms of a term must be consolidated

## Contraindications

- Stemming is not applied in the indexing pipeline
- Stemming is applied post-indexing (after tf-idf computation)
- Term variants are kept separate and not merged

## Constraints

- Stemming must be applied consistently across all documents and queries
- All surface forms mapping to a stem must be identified before tf-idf calculation
- Document frequency count must include all documents containing any surface form of the stem

## Output Contract

- Clear specification of adjusted tf and idf formulas that account for merged term frequencies and consolidated document counts under stemmed forms

## Triggers

- Implementing tf-idf in a system that applies stemming; need to clarify how term frequency and document frequency should be recalculated
