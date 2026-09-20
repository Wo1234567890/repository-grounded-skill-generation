---
id: "1b393658-6561-5a40-a7d1-03be45e195d3"
name: "Term-at-a-Time Score Accumulation"
description: "Iteratively update document scores by processing one query term at a time, adding weighted contributions from each term to accumulators. This micro-skill implements the inner loop of vector space scoring, where each query term's weight is multiplied by its term weight in each document and accumulated into a score array."
version: "0.1.0"
tags:
  - "vector_space_model"
  - "scoring"
  - "accumulation"
  - "term_weighting"
  - "document_ranking"
  - "information_retrieval"
triggers:
  - "Processing multiple query terms and need to update scores for all documents in a single pass; memory-efficient approach when postings lists are available"
examples:
  - input: "Query: ['cat', 'dog']; Postings: {cat: {doc1: tf=2, doc2: tf=1}, dog: {doc1: tf=1, doc2: tf=3}}; Query weights: {cat: 0.5, dog: 0.3}"
    output: "Scores: {doc1: 2*0.5 + 1*0.3 = 1.3, doc2: 1*0.5 + 3*0.3 = 1.4}"
    notes: "Simple term frequency accumulation; scores ready for normalization and top-K selection"
---

# Term-at-a-Time Score Accumulation

Iteratively update document scores by processing one query term at a time, adding weighted contributions from each term to accumulators. This micro-skill implements the inner loop of vector space scoring, where each query term's weight is multiplied by its term weight in each document and accumulated into a score array.

## Prompt

For each query term t in sequence: (1) Calculate the weight of term t in the query vector. (2) For each document d in the collection: retrieve the term frequency or tf-idf weight of term t in document d from the postings list, multiply by the query term weight, and add the result to the accumulator (score) for document d. Repeat until all query terms have been processed. The Scores array now holds the accumulated contributions ready for top-K extraction.

## Objective

Accumulate document scores by iterating over query terms and updating score array in a single pass
## Applicable Signals

- Multiple query terms present in the query
- Postings lists with term frequency or tf-idf weights are available
- Need to rank all documents in the collection against the query
- Memory efficiency is a priority

## Contraindications

- Single-term queries (document-at-a-time processing is more efficient)
- When postings lists do not store term weights (tf or tf-idf)
- When only a small subset of documents need scoring (use inverted index directly)

## Intervention Moves

- Initialize Scores array with zeros for each document
- Iterate over each query term t
- Calculate query vector weight for term t
- For each document, retrieve term weight from postings and multiply by query weight
- Add weighted contribution to document accumulator
- Proceed to next query term

## Workflow Steps

- {'step': 1, 'action': 'Initialize Scores array with zero for each of N documents'}
- {'step': 2, 'action': 'For each query term t in the query (outermost loop)'}
- {'step': 3, 'action': 'Calculate weight of term t in the query vector'}
- {'step': 4, 'action': 'For each document d in the collection (inner loop)'}
- {'step': 5, 'action': 'Retrieve term weight (tf or tf-idf) for term t in document d from postings'}
- {'step': 6, 'action': 'Multiply query term weight by document term weight'}
- {'step': 7, 'action': 'Add result to Scores[d] accumulator'}
- {'step': 8, 'action': 'Proceed to next document'}
- {'step': 9, 'action': 'Proceed to next query term'}

## Constraints

- Postings entries must include term frequency or pre-computed weight for each term-document pair
- Length array (document normalization factors) must be available for final score normalization
- Query term weights must be pre-calculated before accumulation begins

## Cautions

- Storing floating-point weights in postings can be space-inefficient; consider storing N/dft (inverse document frequency) at the head of postings and term frequency per entry instead
- Ensure accumulators are initialized to zero before processing begins
- Document length normalization should be applied after all terms have been accumulated

## Output Contract

- Scores array with accumulated contributions from all query terms, normalized by document length factors, ready for top-K extraction. Each Scores[d] contains the dot product of the query vector and document d vector.

## Example Executions

### Example 1

- Input: Query: ['cat', 'dog']; Postings: {cat: {doc1: tf=2, doc2: tf=1}, dog: {doc1: tf=1, doc2: tf=3}}; Query weights: {cat: 0.5, dog: 0.3}
- Output: Scores: {doc1: 2*0.5 + 1*0.3 = 1.3, doc2: 1*0.5 + 3*0.3 = 1.4}
- Notes: Simple term frequency accumulation; scores ready for normalization and top-K selection

## Triggers

- Processing multiple query terms and need to update scores for all documents in a single pass; memory-efficient approach when postings lists are available

## Examples

### Example 1

Input:

  Query: ['cat', 'dog']; Postings: {cat: {doc1: tf=2, doc2: tf=1}, dog: {doc1: tf=1, doc2: tf=3}}; Query weights: {cat: 0.5, dog: 0.3}

Output:

  Scores: {doc1: 2*0.5 + 1*0.3 = 1.3, doc2: 1*0.5 + 3*0.3 = 1.4}

Notes:

  Simple term frequency accumulation; scores ready for normalization and top-K selection
