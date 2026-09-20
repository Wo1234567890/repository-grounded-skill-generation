---
id: "8c14e62f-be01-5801-9027-2173d3c2a7ba"
name: "Inverse Document Frequency (IDF) Lookup"
description: "Retrieve or compute the idf value for a term based on its document frequency across a corpus. Use to penalize common terms and boost rare terms in relevance scoring."
version: "0.1.0"
tags:
  - "term_weighting"
  - "idf"
  - "relevance_scoring"
  - "statistical_weighting"
triggers:
  - "need to adjust term weight based on how many documents contain it"
  - "building or querying a term-document matrix"
---

# Inverse Document Frequency (IDF) Lookup

Retrieve or compute the idf value for a term based on its document frequency across a corpus. Use to penalize common terms and boost rare terms in relevance scoring.

## Prompt

Given a term t and a corpus of N documents, compute or retrieve idf(t) = log(N / df(t)), where df(t) is the number of documents containing term t. The idf value quantifies term rarity: highest for terms appearing in few documents, lowest for terms appearing in many or all documents.

## Objective

quantify_term_rarity
## Applicable Signals

- need to adjust term weight based on document frequency
- building or querying a term-document matrix
- preparing weights for tf-idf composite scoring

## Contraindications

- term appears in all documents (idf approaches 0; use stop word filtering instead)
- corpus is too small or unstable (insufficient document frequency data)
- term has not been indexed or does not exist in corpus

## Intervention Moves

- Look up or compute df(t) from corpus index
- Apply logarithmic scaling: idf(t) = log(N / df(t))
- Cache or return idf value for downstream tf-idf calculation

## Workflow Steps

- {'step': 1, 'action': 'Retrieve corpus size N (total number of documents)'}
- {'step': 2, 'action': 'Look up or compute document frequency df(t) for term t'}
- {'step': 3, 'action': 'Apply formula: idf(t) = log(N / df(t))'}
- {'step': 4, 'action': 'Return or cache idf(t) value for use in tf-idf weighting'}

## Constraints

- corpus size N must be known and stable
- document frequency df(t) must be precomputed or indexed
- idf is always finite and non-negative

## Cautions

- idf of a term that occurs in every document is zero; consider stop word lists for such terms
- idf values should be precomputed and cached for efficiency in large corpora

## Output Contract

- idf(t) value reflecting rarity of term t across corpus; a finite non-negative scalar suitable for multiplication with term frequency in tf-idf composite weighting

## Triggers

- need to adjust term weight based on how many documents contain it
- building or querying a term-document matrix
