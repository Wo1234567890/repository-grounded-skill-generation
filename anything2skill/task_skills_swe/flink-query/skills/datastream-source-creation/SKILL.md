---
id: "2935ec44-11f2-5783-9921-cc4837088279"
name: "DataStream Source Creation"
description: "Compute composite term weight in a document by multiplying term frequency by inverse document frequency. Use when scoring document relevance or ranking search results based on term importance."
version: "0.1.1"
tags:
  - "term_weighting"
  - "statistical_scoring"
  - "information_retrieval"
  - "document_ranking"
  - "vector_space_model"
triggers:
  - "Starting a new Flink streaming job and need to bind data from memory, iterators, sequences, or external systems like Kafka"
---

# DataStream Source Creation

Compute composite term weight in a document by multiplying term frequency by inverse document frequency. Use when scoring document relevance or ranking search results based on term importance.

## Prompt

Calculate tf-idf weight for a single term in a document using the formula: tf-idf(t,d) = tf(t,d) × idf(t), where tf(t,d) is the term frequency of term t in document d, and idf(t) is the inverse document frequency of term t across the collection.

## Objective

Calculate tf-idf weight for a single term in a document
## Applicable Signals

- Term frequency (tf) value for the term in the document is available
- Inverse document frequency (idf) value for the term is pre-computed
- Document collection size and term occurrence counts are known

## Contraindications

- Term occurs in virtually all documents (idf approaches zero; weight becomes negligible)
- Term is a stop word or has been filtered from the collection
- Term frequency or idf values are not yet computed or unavailable

## Workflow Steps

- {'step': 1, 'action': 'Retrieve or compute tf(t,d): term frequency of term t in document d'}
- {'step': 2, 'action': 'Retrieve or compute idf(t): inverse document frequency of term t across the collection'}
- {'step': 3, 'action': 'Multiply tf(t,d) by idf(t) to obtain tf-idf(t,d)'}
- {'step': 4, 'action': 'Return numeric weight tf-idf(t,d) for use in document scoring or ranking'}

## Constraints

- Both tf(t,d) and idf(t) must be non-negative numeric values
- idf(t) is always finite and typically decreases as term frequency in collection increases
- Result is a single numeric weight; no further normalization is applied at this step

## Cautions

- High tf-idf weight indicates high discriminating power for that document; use in ranking contexts
- Lower weight when term occurs fewer times in document or in many documents; less pronounced relevance signal
- Lowest weight when term occurs in virtually all documents; consider filtering such terms upstream

## Output Contract

- Numeric weight tf-idf(t,d) = tf(t,d) × idf(t) for term t in document d. Weight is highest when term occurs many times within a small number of documents (high discriminating power); lower when term occurs fewer times or in many documents; lowest when term occurs in virtually all documents.

## Triggers

- Starting a new Flink streaming job and need to bind data from memory, iterators, sequences, or external systems like Kafka
