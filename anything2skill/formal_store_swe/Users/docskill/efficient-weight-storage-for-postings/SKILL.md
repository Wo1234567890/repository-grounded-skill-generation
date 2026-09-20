---
id: "7f0e6591-1ab5-5d39-aac9-db36b49ec6dc"
name: "Efficient Weight Storage for Postings"
description: "Store term frequency and inverse document frequency compactly in postings entries to avoid redundant floating-point storage of precomputed weights. This micro-skill optimizes index storage by storing only tf and N/df instead of full precomputed weight values."
version: "0.1.0"
tags:
  - "index_optimization"
  - "storage_efficiency"
  - "postings_encoding"
  - "tf-idf"
  - "inverted_index"
triggers:
  - "Building or maintaining inverted index with tf-idf or similar weighting; space efficiency is a concern"
---

# Efficient Weight Storage for Postings

Store term frequency and inverse document frequency compactly in postings entries to avoid redundant floating-point storage of precomputed weights. This micro-skill optimizes index storage by storing only tf and N/df instead of full precomputed weight values.

## Prompt

When constructing or maintaining an inverted index with tf-idf or similar weighting schemes, store term frequency (tf) and the ratio N/df (total documents divided by document frequency) at the head of each postings entry. This avoids the space overhead of precomputing and storing floating-point weight values wf(t,d) for every term-document pair.

## Objective

Minimize storage overhead by storing only tf and N/df instead of precomputed weights
## Applicable Signals

- Building or maintaining an inverted index
- Using tf-idf or similar term weighting schemes
- Space efficiency is a primary concern
- Postings entries are being created or updated

## Contraindications

- Weights are already precomputed and storage is not a constraint
- Real-time weight updates are required during index maintenance
- Query-time performance is more critical than index storage size

## Intervention Moves

- Store term frequency tf(t,d) for each postings entry
- Store N/df ratio at the head of postings for term t instead of precomputing idf
- Defer weight computation to retrieval time

## Workflow Steps

- {'step': 1, 'action': 'For each term t in the index, compute and store N/df(t) at the head of its postings list'}
- {'step': 2, 'action': 'For each postings entry (t, d), store only the term frequency tf(t,d)'}
- {'step': 3, 'action': 'During query scoring, retrieve N/df(t) and tf(t,d) from postings and compute weight on-the-fly'}

## Constraints

- Applicable only when using inverse document frequency weighting or similar schemes
- Requires that N (total document count) and df (document frequency) are available at retrieval time
- Weight computation must be deferred to query scoring phase

## Cautions

- Storing N/df at postings head requires space for one additional value per term
- Retrieval algorithms must compute weights on-the-fly; ensure scoring logic accounts for this

## Output Contract

- Postings entries containing term frequency and N/df ratio, reducing storage footprint compared to storing full precomputed weights. Each postings list for term t has N/df at its head, and each entry contains tf(t,d) for document d.

## Triggers

- Building or maintaining inverted index with tf-idf or similar weighting; space efficiency is a concern
