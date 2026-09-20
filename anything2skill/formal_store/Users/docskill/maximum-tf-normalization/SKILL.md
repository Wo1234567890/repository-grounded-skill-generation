---
id: "fcee8af2-1df2-5395-a35d-aa4572a0f71a"
name: "Maximum TF Normalization"
description: "Normalize term frequency weights in a document by dividing each term's frequency by the maximum term frequency in that document, using a smoothing parameter to prevent extreme score swings. Apply this to mitigate bias toward longer documents that repeat terms more frequently."
version: "0.1.0"
tags:
  - "term_frequency"
  - "normalization"
  - "vector_space_model"
  - "document_length_bias"
  - "tf_idf"
triggers:
  - "Computing term weights for documents of varying length"
  - "Raw tf scores show bias toward longer documents"
  - "Building vector space model scores for ranking"
examples:
  - input: "Document d with terms: 'algorithm' (tf=5), 'data' (tf=3), 'search' (tf=2); tfmax(d)=5; a=0.4"
    output: "ntf_algorithm,d = 0.4 + 0.6 * (5/5) = 1.0; ntf_data,d = 0.4 + 0.6 * (3/5) = 0.76; ntf_search,d = 0.4 + 0.6 * (2/5) = 0.64"
    notes: "Smoothing prevents the highest-frequency term from dominating; lower-frequency terms retain meaningful weight"
  - input: "Document d' created by appending a copy of document d to itself; all raw tf values doubled"
    output: "ntf values remain unchanged because both numerator and denominator scale proportionally"
    notes: "This demonstrates the key benefit: document duplication does not inflate scores, eliminating the length bias anomaly"
---

# Maximum TF Normalization

Normalize term frequency weights in a document by dividing each term's frequency by the maximum term frequency in that document, using a smoothing parameter to prevent extreme score swings. Apply this to mitigate bias toward longer documents that repeat terms more frequently.

## Prompt

For each document d, compute the normalized term frequency (ntf) for each term t using the formula: ntf_t,d = a + (1 - a) * (tf_t,d / tfmax(d)), where tfmax(d) is the maximum term frequency in document d, tf_t,d is the raw term frequency of term t in document d, and a is a smoothing parameter (typically 0.4). The smoothing term a dampens the contribution of the scaling factor to avoid large swings in ntf from modest changes in raw tf.

## Objective

normalize_term_frequency_by_document_length
## Applicable Signals

- Computing term weights for documents of varying length
- Raw tf scores show bias toward longer documents
- Building vector space model scores for ranking
- Need to prevent document length from inflating relevance scores

## Contraindications

- Document length is already controlled or normalized upstream
- Stop word list is unstable or frequently changing (method is sensitive to stop word changes)
- Document contains outlier terms with unusually high frequencies not representative of content

## Intervention Moves

- Identify tfmax(d) for the document
- For each term t in the document, retrieve tf_t,d
- Apply the normalization formula with chosen smoothing parameter a
- Use resulting ntf values in downstream scoring (e.g., tf-idf computation)

## Workflow Steps

- {'step': 1, 'action': 'Compute tfmax(d)', 'detail': 'Scan all terms in document d and identify the maximum term frequency value'}
- {'step': 2, 'action': 'For each term t in document d, retrieve tf_t,d', 'detail': 'Access the raw term frequency count for term t'}
- {'step': 3, 'action': 'Apply normalization formula', 'detail': 'Compute ntf_t,d = a + (1 - a) * (tf_t,d / tfmax(d)) using smoothing parameter a (default 0.4)'}
- {'step': 4, 'action': 'Return normalized frequencies', 'detail': 'Pass ntf values to downstream scoring or weighting steps'}

## Constraints

- Smoothing parameter a must be between 0 and 1; typically set to 0.4
- tfmax(d) must be computed over all terms in the document before normalization begins
- Method assumes raw term frequencies are available for all terms in the document

## Cautions

- The method is unstable: changes to the stop word list can dramatically alter term weightings and ranking order, making tuning difficult
- Outlier terms with unusually large occurrence counts can skew the maximum and reduce normalization effectiveness

## Output Contract

- For each term t in document d, return a normalized term frequency value ntf_t,d in the range [a, 1]. This value is suitable for use in downstream tf-idf or vector space scoring formulas. The output eliminates the anomaly where duplicating a document would double its score.

## Example Therapist Responses

### Example 1

- Client/Input: Document d with terms: 'algorithm' (tf=5), 'data' (tf=3), 'search' (tf=2); tfmax(d)=5; a=0.4
- Therapist/Output: ntf_algorithm,d = 0.4 + 0.6 * (5/5) = 1.0; ntf_data,d = 0.4 + 0.6 * (3/5) = 0.76; ntf_search,d = 0.4 + 0.6 * (2/5) = 0.64
- Notes: Smoothing prevents the highest-frequency term from dominating; lower-frequency terms retain meaningful weight

### Example 2

- Client/Input: Document d' created by appending a copy of document d to itself; all raw tf values doubled
- Therapist/Output: ntf values remain unchanged because both numerator and denominator scale proportionally
- Notes: This demonstrates the key benefit: document duplication does not inflate scores, eliminating the length bias anomaly

## Triggers

- Computing term weights for documents of varying length
- Raw tf scores show bias toward longer documents
- Building vector space model scores for ranking

## Examples

### Example 1

Input:

  Document d with terms: 'algorithm' (tf=5), 'data' (tf=3), 'search' (tf=2); tfmax(d)=5; a=0.4

Output:

  ntf_algorithm,d = 0.4 + 0.6 * (5/5) = 1.0; ntf_data,d = 0.4 + 0.6 * (3/5) = 0.76; ntf_search,d = 0.4 + 0.6 * (2/5) = 0.64

Notes:

  Smoothing prevents the highest-frequency term from dominating; lower-frequency terms retain meaningful weight

### Example 2

Input:

  Document d' created by appending a copy of document d to itself; all raw tf values doubled

Output:

  ntf values remain unchanged because both numerator and denominator scale proportionally

Notes:

  This demonstrates the key benefit: document duplication does not inflate scores, eliminating the length bias anomaly
