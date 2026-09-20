---
id: "42a24866-f9b3-5c9c-bee0-568131b255b8"
name: "Collect DataStream Results via Iterator Sink"
description: "Compute cosine similarity scores between query and document vectors in vector space model. Produces ranked retrieval results based on vector dot products of normalized term weight vectors."
version: "0.1.1"
tags:
  - "vector_space_model"
  - "information_retrieval"
  - "scoring"
  - "ranking"
  - "dot_product"
  - "similarity_metric"
triggers:
  - "need to inspect or validate DataStream output in test or debug context"
  - "results are small enough to fit in memory"
examples:
  - input: "val myResult: DataStream[(String, Int)] = ..."
    output: "val myOutput: Iterator[(String, Int)] = myResult.collectAsync()"
    notes: "Scala example; Java syntax is similar with generic type parameters."
  - input: "DataStream<Tuple2<String, Integer>> myResult = ...;"
    output: "Iterator<Tuple2<String, Integer>> myOutput = myResult.collectAsync();"
    notes: "Java example with generic type parameters."
---

# Collect DataStream Results via Iterator Sink

Compute cosine similarity scores between query and document vectors in vector space model. Produces ranked retrieval results based on vector dot products of normalized term weight vectors.

## Prompt

Given a query vector and document vectors (each represented as term weights), calculate the cosine similarity score for each query-document pair using dot product normalization. The score ranges from 0.0 to 1.0, where 1.0 indicates perfect similarity. Use this score to rank documents by relevance to the query.

## Objective

Calculate cosine similarity score for query-document pair to enable ranked retrieval
## Applicable Signals

- Query evaluation phase initiated
- Documents and queries represented as term weight vectors
- Ranked retrieval results required
- Vector space model in use

## Contraindications

- Boolean retrieval required (use exact matching instead)
- Non-vector document representations (convert or use alternative scoring)
- Real-time constraints prohibit dot product computation (use approximate methods)

## Intervention Moves

- Normalize query vector to unit length
- Normalize document vector to unit length
- Compute dot product of normalized vectors
- Return cosine similarity score in range [0.0, 1.0]

## Constraints

- Both query and document must be represented as term weight vectors
- Vectors must have consistent dimensionality (same term vocabulary)
- Term weights must be pre-computed (e.g., via tf-idf)

## Cautions

- Ensure term weights are normalized before dot product to avoid bias toward longer documents
- Verify vector dimensionality consistency across query and document collections

## Output Contract

- Cosine similarity score (floating-point value in range [0.0, 1.0]) for each query-document pair, enabling downstream ranking and result presentation.

## Triggers

- need to inspect or validate DataStream output in test or debug context
- results are small enough to fit in memory

## Examples

### Example 1

Input:

  val myResult: DataStream[(String, Int)] = ...

Output:

  val myOutput: Iterator[(String, Int)] = myResult.collectAsync()

Notes:

  Scala example; Java syntax is similar with generic type parameters.

### Example 2

Input:

  DataStream<Tuple2<String, Integer>> myResult = ...;

Output:

  Iterator<Tuple2<String, Integer>> myOutput = myResult.collectAsync();

Notes:

  Java example with generic type parameters.
