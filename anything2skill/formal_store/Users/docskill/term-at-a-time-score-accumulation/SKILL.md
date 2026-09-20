---
id: "7f9f9df7-b179-5977-baf3-083d978c314f"
name: "Term-at-a-Time Score Accumulation"
description: "Micro-procedure to iteratively update document scores by processing one query term at a time, adding the weighted contribution of each term to accumulators. Reduces redundant storage by computing inverse document frequency on-the-fly and storing only term frequency in postings entries."
version: "0.1.0"
tags:
  - "vector_space_model"
  - "scoring"
  - "term_weighting"
  - "accumulator"
  - "memory_optimization"
  - "information_retrieval"
triggers:
  - "iterating over query terms in vector space scoring"
  - "need to minimize memory footprint for postings storage"
  - "computing vector space scores for top-K document retrieval"
---

# Term-at-a-Time Score Accumulation

Micro-procedure to iteratively update document scores by processing one query term at a time, adding the weighted contribution of each term to accumulators. Reduces redundant storage by computing inverse document frequency on-the-fly and storing only term frequency in postings entries.

## Prompt

For each query term t in turn, calculate its weight in the query vector. Then iterate over all documents in the postings list for term t and update each document's score by adding the contribution from term t. Store term frequency tft,d in postings entries and compute idft on-the-fly as N/dft rather than precomputing weights. Accumulate scores in the Scores array (accumulators) until all query terms are processed.

## Objective

efficiently accumulate document scores term-by-term while minimizing memory footprint
## Applicable Signals

- query contains multiple terms
- postings list available for each query term
- document collection size N is known

## Contraindications

- all document scores must be computed in parallel without term-by-term iteration
- term weights are pre-computed and stored in postings (defeats space optimization)
- single-term queries (no accumulation benefit)

## Workflow Steps

- {'step': 1, 'action': 'Initialize Scores array to zero for all N documents'}
- {'step': 2, 'action': 'For each query term t (outermost loop)'}
- {'step': 3, 'action': 'Calculate weight wt in query vector for term t'}
- {'step': 4, 'action': 'For each document d in postings list of term t'}
- {'step': 5, 'action': 'Retrieve term frequency tft,d from postings entry'}
- {'step': 6, 'action': 'Compute or retrieve idft (as N/dft from postings head)'}
- {'step': 7, 'action': 'Calculate contribution: wt × tft,d × idft (or equivalent weight function)'}
- {'step': 8, 'action': 'Add contribution to Scores[d]'}
- {'step': 9, 'action': 'After all query terms processed, normalize scores using Length array if required'}

## Constraints

- Scores array must be initialized to zero for all N documents before processing
- Length array (document normalization factors) must be available
- Term frequency tft,d must be stored in postings entries
- Inverse document frequency computed as N/dft at postings head

## Cautions

- Floating-point precision may accumulate across multiple term contributions; consider rounding strategy for final scores
- Memory access patterns are sequential over Scores array; cache efficiency depends on N and available memory

## Output Contract

- Scores array with accumulated contributions from all query terms, ready for top-K extraction. Each Scores[d] contains the final vector space score for document d.

## Triggers

- iterating over query terms in vector space scoring
- need to minimize memory footprint for postings storage
- computing vector space scores for top-K document retrieval
