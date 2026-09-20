---
id: "709fb7af-4043-5b3e-8ad0-e588e22ae054"
name: "Inverse Document Frequency (IDF) Computation"
description: "Calculate inverse document frequency weights for terms to penalize overly common terms and boost rare discriminative terms. Core weighting component in TF-IDF schemes."
version: "0.1.0"
tags:
  - "term_weighting"
  - "information_retrieval"
  - "vector_space_model"
  - "idf"
  - "tf-idf"
triggers:
  - "Assigning term weights during indexing; need to reflect term rarity across collection; building vector representations"
---

# Inverse Document Frequency (IDF) Computation

Calculate inverse document frequency weights for terms to penalize overly common terms and boost rare discriminative terms. Core weighting component in TF-IDF schemes.

## Prompt

Compute the IDF weight for a term by calculating the inverse proportion of the number of documents containing that term to the total number of documents in the collection. IDF reflects term rarity: terms appearing in few documents receive higher weights, while terms appearing in many documents receive lower weights. This weight is typically combined with term frequency (TF) in downstream scoring.

## Objective

Compute IDF weight for a term
## Applicable Signals

- Assigning term weights during indexing
- Need to reflect term rarity across collection
- Building vector representations for scoring

## Contraindications

- All terms should be equally weighted
- Using probabilistic models with different frequency assumptions
- Processing single-document queries where document frequency is undefined

## Intervention Moves

- Count the number of documents containing the term
- Divide total document count by document frequency
- Apply logarithmic transformation to normalize the ratio
- Return the resulting IDF weight

## Constraints

- Requires complete collection statistics (total documents and per-term document frequencies)
- Document frequency must be greater than zero to avoid division by zero
- IDF computation should precede or accompany TF computation for full TF-IDF weighting

## Cautions

- IDF alone does not account for term frequency within documents; combine with TF for complete weighting
- Collection statistics must be up-to-date; adding or removing documents changes IDF values for all terms

## Output Contract

- IDF weight value for each term, reflecting inverse proportion to document frequency. Output is a numeric weight suitable for multiplication with term frequency in vector space scoring.

## Triggers

- Assigning term weights during indexing; need to reflect term rarity across collection; building vector representations
