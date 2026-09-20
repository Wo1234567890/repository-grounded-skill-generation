---
id: "9d0949ea-a568-554d-b433-8b794d40fc69"
name: "Out-of-Vocabulary Query Term Scoring"
description: "Compute TF-IDF scores for query terms absent from the indexed document collection using a fallback IDF convention, enabling valid scoring without collection statistics for novel or rare terms."
version: "0.1.0"
tags:
  - "tf-idf"
  - "term_weighting"
  - "out-of-vocabulary"
  - "query_scoring"
  - "information_retrieval"
triggers:
  - "Query contains a term not in the indexed collection"
  - "Need to score queries with novel or rare terms"
  - "Applying weighting schemes (e.g., ntc.atc) to incomplete term data"
examples:
  - input: "Query: 'coyote insurance'; collection contains 'insurance' but not 'coyote'"
    output: "Score for 'coyote' = 0 (or minimal fallback IDF); score for 'insurance' computed normally from collection statistics; final query vector includes both terms with consistent weighting scheme"
    notes: "Demonstrates fallback IDF assignment for missing term while preserving standard scoring for in-vocabulary terms"
---

# Out-of-Vocabulary Query Term Scoring

Compute TF-IDF scores for query terms absent from the indexed document collection using a fallback IDF convention, enabling valid scoring without collection statistics for novel or rare terms.

## Prompt

When a query term does not occur in the collection, assign it an IDF value using a fallback convention (typically IDF = 0 or a minimal default). Compute the weighted score for that term consistently with the chosen weighting scheme (e.g., ntc.atc). Ensure all out-of-vocabulary terms in the query are handled uniformly.

## Objective

Produce valid scores for out-of-vocabulary query terms without collection statistics
## Applicable Signals

- Term lookup returns no document frequency
- IDF table has no entry for query term
- Query includes out-of-vocabulary words

## Contraindications

- All query terms exist in the collection
- Using only in-vocabulary terms for scoring
- Ignoring out-of-vocabulary terms entirely

## Workflow Steps

- {'step': 1, 'action': "Check if query term exists in the collection's term-document frequency table"}
- {'step': 2, 'action': 'If term is absent, apply the fallback IDF convention (e.g., IDF = 0 or minimal default value)'}
- {'step': 3, 'action': 'Compute the weighted score for the out-of-vocabulary term using the selected weighting scheme and the fallback IDF'}
- {'step': 4, 'action': 'Aggregate scores across all query terms (in-vocabulary and out-of-vocabulary) to produce the final query vector'}

## Constraints

- Fallback IDF convention must be applied consistently across all out-of-vocabulary terms
- Weighting scheme (e.g., ntc.atc) must be preserved during fallback computation
- Out-of-vocabulary handling must not break downstream vector normalization or similarity computation

## Cautions

- Assigning IDF = 0 to out-of-vocabulary terms may suppress their contribution; consider alternative fallback values if term presence is semantically important
- Ensure the chosen fallback convention is documented and consistent across all queries in the same session

## Output Contract

- Computed score for out-of-vocabulary term using fallback IDF value or zero-IDF convention
- Consistent handling across all out-of-vocabulary terms in the query
- Valid query vector suitable for downstream similarity computation

## Example Executions

### Example 1

- Input: Query: 'coyote insurance'; collection contains 'insurance' but not 'coyote'
- Output: Score for 'coyote' = 0 (or minimal fallback IDF); score for 'insurance' computed normally from collection statistics; final query vector includes both terms with consistent weighting scheme
- Notes: Demonstrates fallback IDF assignment for missing term while preserving standard scoring for in-vocabulary terms

## Triggers

- Query contains a term not in the indexed collection
- Need to score queries with novel or rare terms
- Applying weighting schemes (e.g., ntc.atc) to incomplete term data

## Examples

### Example 1

Input:

  Query: 'coyote insurance'; collection contains 'insurance' but not 'coyote'

Output:

  Score for 'coyote' = 0 (or minimal fallback IDF); score for 'insurance' computed normally from collection statistics; final query vector includes both terms with consistent weighting scheme

Notes:

  Demonstrates fallback IDF assignment for missing term while preserving standard scoring for in-vocabulary terms
