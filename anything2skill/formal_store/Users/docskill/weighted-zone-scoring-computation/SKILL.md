---
id: "af6320bc-1ac2-5054-999c-eadf0d98b82c"
name: "Weighted Zone Scoring Computation"
description: "Combine Boolean match scores from multiple document zones using learned or preset weights to produce a single relevance score for ranking. Apply during query evaluation when documents have structured zones (e.g., title, body, metadata)."
version: "0.1.0"
tags:
  - "information_retrieval"
  - "scoring"
  - "zone_weighting"
  - "ranking"
  - "Boolean_matching"
triggers:
  - "document has multiple structured zones (title, body, anchor text, etc.)"
  - "zone weights are known or have been learned from training data"
  - "need to produce single combined relevance score for ranking"
examples:
  - input: "Query: 'machine learning'; Document with zones: title (match=1), body (match=1), metadata (match=0); weights: g1=0.2, g2=0.5, g3=0.3"
    output: "Score = 1*0.2 + 1*0.5 + 0*0.3 = 0.7"
    notes: "Document ranks higher when query matches high-weight zones."
  - input: "Query: 'neural networks'; Document with zones: title (match=0), body (match=1), metadata (match=1); weights: g1=0.4, g2=0.4, g3=0.2"
    output: "Score = 0*0.4 + 1*0.4 + 1*0.2 = 0.6"
    notes: "Title mismatch reduces score despite body and metadata matches."
---

# Weighted Zone Scoring Computation

Combine Boolean match scores from multiple document zones using learned or preset weights to produce a single relevance score for ranking. Apply during query evaluation when documents have structured zones (e.g., title, body, metadata).

## Prompt

For each query-document pair with multiple zones: (1) Obtain Boolean match indicator (0 or 1) for each zone. (2) Multiply each zone's match indicator by its corresponding weight. (3) Sum weighted contributions to produce final score. (4) Use this score for document ranking in result set.

## Objective

compute_zone_weighted_score
## Applicable Signals

- Boolean match indicators per zone available
- zone weight parameters established
- query-document pair ready for scoring

## Contraindications

- document is unstructured or single-zone only
- zones require different Boolean match functions
- continuous relevance scores required instead of weighted Boolean combination
- zone weights are unknown and cannot be estimated

## Workflow Steps

- {'step': 1, 'action': 'Extract Boolean match indicator for each zone', 'detail': 'For each zone in the document, determine if query terms match (1) or do not match (0).'}
- {'step': 2, 'action': 'Retrieve zone weights', 'detail': 'Obtain pre-computed or learned weight for each zone (e.g., g1 for title, g2 for body).'}
- {'step': 3, 'action': 'Compute weighted sum', 'detail': "Multiply each zone's Boolean indicator by its weight and sum all contributions."}
- {'step': 4, 'action': 'Return combined score', 'detail': 'Output numeric score for use in document ranking.'}

## Constraints

- All zones must use compatible Boolean match functions (same or equivalent logic).
- Zone weights must sum to a meaningful total (typically 1.0 or normalized).
- Boolean match indicators must be binary (0 or 1) per zone.

## Cautions

- Ensure zone weights reflect actual relevance contribution; poorly calibrated weights degrade ranking quality.
- Verify that zone definitions are consistent across all documents in the collection.

## Output Contract

- Numeric score (typically in range [0, sum_of_weights]) combining all zone contributions; suitable for sorting documents by relevance in result set.

## Example Therapist Responses

### Example 1

- Client/Input: Query: 'machine learning'; Document with zones: title (match=1), body (match=1), metadata (match=0); weights: g1=0.2, g2=0.5, g3=0.3
- Therapist/Output: Score = 1*0.2 + 1*0.5 + 0*0.3 = 0.7
- Notes: Document ranks higher when query matches high-weight zones.

### Example 2

- Client/Input: Query: 'neural networks'; Document with zones: title (match=0), body (match=1), metadata (match=1); weights: g1=0.4, g2=0.4, g3=0.2
- Therapist/Output: Score = 0*0.4 + 1*0.4 + 1*0.2 = 0.6
- Notes: Title mismatch reduces score despite body and metadata matches.

## Triggers

- document has multiple structured zones (title, body, anchor text, etc.)
- zone weights are known or have been learned from training data
- need to produce single combined relevance score for ranking

## Examples

### Example 1

Input:

  Query: 'machine learning'; Document with zones: title (match=1), body (match=1), metadata (match=0); weights: g1=0.2, g2=0.5, g3=0.3

Output:

  Score = 1*0.2 + 1*0.5 + 0*0.3 = 0.7

Notes:

  Document ranks higher when query matches high-weight zones.

### Example 2

Input:

  Query: 'neural networks'; Document with zones: title (match=0), body (match=1), metadata (match=1); weights: g1=0.4, g2=0.4, g3=0.2

Output:

  Score = 0*0.4 + 1*0.4 + 1*0.2 = 0.6

Notes:

  Title mismatch reduces score despite body and metadata matches.
