---
id: "0d6c35fd-5388-5dcf-afca-2d31a26a512b"
name: "Inverse Document Frequency Calculation"
description: "Compute idf weights for terms based on their rarity across the document collection, giving higher weight to terms that appear in fewer documents. IDF reflects how discriminative a term is: rare terms receive higher weights, common terms receive lower weights."
version: "0.1.0"
tags:
  - "term_weighting"
  - "vector_space_model"
  - "information_retrieval"
  - "tf-idf"
  - "scoring"
triggers:
  - "computing term importance in a document collection"
  - "when term frequency alone is insufficient to distinguish discriminative terms"
  - "in tf-idf weighting pipelines"
---

# Inverse Document Frequency Calculation

Compute idf weights for terms based on their rarity across the document collection, giving higher weight to terms that appear in fewer documents. IDF reflects how discriminative a term is: rare terms receive higher weights, common terms receive lower weights.

## Prompt

For each term in the vocabulary, calculate its inverse document frequency (idf) as log(N / df), where N is the total number of documents in the collection and df is the number of documents containing that term.

## Objective

weight terms by collection rarity
## Applicable Signals

- term frequency computed but not yet weighted by rarity
- document collection size and document frequencies known
- vector space model scoring in progress

## Contraindications

- all terms are equally important in the domain
- domain-specific stopword lists where rarity is not a proxy for relevance
- external term importance weights are already provided

## Workflow Steps

- {'step': 1, 'action': 'Obtain total document count N and document frequency df for each term'}
- {'step': 2, 'action': 'For each term, compute idf = log(N / df)'}
- {'step': 3, 'action': 'Store or return idf weights indexed by term'}

## Constraints

- document frequency (df) must be greater than zero for all terms
- total document count (N) must be known and fixed
- logarithm base (typically natural log or log10) should be consistent across the collection

## Cautions

- terms with df = 0 will cause division by zero; filter or handle separately
- idf values are collection-dependent; recalculate if the collection changes

## Output Contract

- IDF weight for each term, typically log(N / df) where N is total documents and df is document frequency. Output is a mapping of term → idf_weight, ready for multiplication with term frequency in tf-idf scoring.

## Triggers

- computing term importance in a document collection
- when term frequency alone is insufficient to distinguish discriminative terms
- in tf-idf weighting pipelines
