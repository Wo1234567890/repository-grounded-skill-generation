---
id: "89b44c8e-50e7-51ec-9cf2-7c1f777b8317"
name: "Query Term Weighting Scheme Selection"
description: "Choose and apply a principled weighting scheme (e.g., nnn.atc, ntc.atc) for query terms in vector space scoring. Use this when deciding how to weight individual query terms before computing similarity scores against documents."
version: "0.1.0"
tags:
  - "vector_space_model"
  - "query_representation"
  - "term_weighting"
  - "information_retrieval"
  - "scoring"
triggers:
  - "Transforming a query into a unit vector for similarity computation"
  - "Comparing multiple weighting schemes on the same query"
  - "Standardizing query representation before scoring against document vectors"
examples:
  - input: "Query: 'best car insurance'; scheme: ntc.atc"
    output: "Query vector with term weights computed using ntc scheme (no augmentation, term frequency, cosine normalization); scheme identifier 'ntc' recorded"
    notes: "ntc applies raw term frequency without augmentation and normalizes by cosine"
  - input: "Query: 'affection'; scheme: atc"
    output: "Query vector with single term 'affection' weighted using atc scheme; scheme identifier 'atc' recorded"
    notes: "Single-term query still benefits from consistent scheme application for comparison with other queries"
  - input: "Query: 'coyote insurance'; out-of-vocabulary term 'coyote'"
    output: "Query vector computed using ntc.atc scheme; 'coyote' assigned zero weight or default idf value; scheme identifier 'ntc.atc' recorded"
    notes: "Out-of-vocabulary terms must be handled explicitly to avoid scoring errors"
---

# Query Term Weighting Scheme Selection

Choose and apply a principled weighting scheme (e.g., nnn.atc, ntc.atc) for query terms in vector space scoring. Use this when deciding how to weight individual query terms before computing similarity scores against documents.

## Prompt

Select a weighting scheme for query terms based on the retrieval task and collection characteristics. Common schemes use notation like 'atc' (augmented term frequency, term frequency weighting, cosine normalization). Apply the chosen scheme consistently to all query terms to produce a normalized query vector. Document which scheme was selected for reproducibility.

## Objective

Assign consistent weights to query terms according to a selected weighting scheme
## Applicable Signals

- Query ready for vector space model scoring
- Need to justify term weight assignment in query
- Comparing retrieval effectiveness across weighting schemes

## Contraindications

- Using equal weights for all query terms without principled justification
- Applying document-specific weighting schemes directly to query terms
- Handling out-of-vocabulary query terms without fallback strategy

## Workflow Steps

- {'step': 1, 'action': 'Identify candidate weighting schemes', 'detail': 'List plausible schemes (e.g., nnn, ntc, atc, atn) based on task requirements and collection statistics'}
- {'step': 2, 'action': 'Select one scheme', 'detail': 'Choose a scheme based on principled reasoning (e.g., augmented term frequency for robustness, cosine normalization for length independence)'}
- {'step': 3, 'action': 'Apply scheme to each query term', 'detail': "Compute weight for each term using the selected scheme's formula (e.g., augmented tf, idf, normalization)"}
- {'step': 4, 'action': 'Normalize query vector', 'detail': 'Apply final normalization (e.g., cosine normalization to unit length) if required by scheme'}
- {'step': 5, 'action': 'Document scheme identifier', 'detail': "Record the scheme code (e.g., 'atc') for downstream scoring and reproducibility"}

## Constraints

- Weighting scheme must be applied uniformly to all query terms
- Scheme identifier must be documented for reproducibility
- Query vector should be normalized (e.g., unit vector) after weighting

## Cautions

- Different weighting schemes may produce different relative orderings of document scores
- Scheme choice should align with document weighting scheme for consistency
- Out-of-vocabulary terms require special handling (e.g., zero weight or default idf)

## Output Contract

- Query vector with assigned term weights; documented weighting scheme identifier (e.g., 'atc' for augmented term frequency with cosine normalization); ready for dot-product scoring against document vectors

## Example Executions

### Example 1

- Input: Query: 'best car insurance'; scheme: ntc.atc
- Output: Query vector with term weights computed using ntc scheme (no augmentation, term frequency, cosine normalization); scheme identifier 'ntc' recorded
- Notes: ntc applies raw term frequency without augmentation and normalizes by cosine

### Example 2

- Input: Query: 'affection'; scheme: atc
- Output: Query vector with single term 'affection' weighted using atc scheme; scheme identifier 'atc' recorded
- Notes: Single-term query still benefits from consistent scheme application for comparison with other queries

### Example 3

- Input: Query: 'coyote insurance'; out-of-vocabulary term 'coyote'
- Output: Query vector computed using ntc.atc scheme; 'coyote' assigned zero weight or default idf value; scheme identifier 'ntc.atc' recorded
- Notes: Out-of-vocabulary terms must be handled explicitly to avoid scoring errors

## Triggers

- Transforming a query into a unit vector for similarity computation
- Comparing multiple weighting schemes on the same query
- Standardizing query representation before scoring against document vectors

## Examples

### Example 1

Input:

  Query: 'best car insurance'; scheme: ntc.atc

Output:

  Query vector with term weights computed using ntc scheme (no augmentation, term frequency, cosine normalization); scheme identifier 'ntc' recorded

Notes:

  ntc applies raw term frequency without augmentation and normalizes by cosine

### Example 2

Input:

  Query: 'affection'; scheme: atc

Output:

  Query vector with single term 'affection' weighted using atc scheme; scheme identifier 'atc' recorded

Notes:

  Single-term query still benefits from consistent scheme application for comparison with other queries

### Example 3

Input:

  Query: 'coyote insurance'; out-of-vocabulary term 'coyote'

Output:

  Query vector computed using ntc.atc scheme; 'coyote' assigned zero weight or default idf value; scheme identifier 'ntc.atc' recorded

Notes:

  Out-of-vocabulary terms must be handled explicitly to avoid scoring errors
