---
id: "59e6dec3-97cc-542a-aded-3c467779933a"
name: "Maximum TF Normalization"
description: "Normalize term frequency weights in a document by dividing each term's frequency by the maximum term frequency in that document, using a smoothing parameter to prevent extreme score swings and mitigate bias toward longer documents."
version: "0.1.0"
tags:
  - "term_weighting"
  - "tf_normalization"
  - "vector_space_model"
  - "scoring"
  - "document_length_bias"
  - "smoothing"
triggers:
  - "computing normalized term frequencies for vector space scoring"
  - "document collection exhibits high length variation"
  - "need to prevent longer documents from dominating relevance scores due to natural term repetition"
examples:
  - input: "Document d with term frequencies: term_A=5, term_B=3, term_C=1; smoothing parameter a=0.4"
    output: "ntf_A,d = 1.0, ntf_B,d = 0.76, ntf_C,d = 0.52"
    notes: "tfmax(d) = 5; highest-frequency term normalizes to 1.0, others scale proportionally with smoothing applied"
  - input: "Document d duplicated to create d′ (d appended to itself); raw tf-idf would score d′ twice as high as d"
    output: "Maximum tf normalization prevents this anomaly; d and d′ receive comparable scores"
    notes: "Demonstrates the key benefit: eliminates document-length bias from term repetition"
---

# Maximum TF Normalization

Normalize term frequency weights in a document by dividing each term's frequency by the maximum term frequency in that document, using a smoothing parameter to prevent extreme score swings and mitigate bias toward longer documents.

## Prompt

For each term t in document d, compute normalized term frequency (ntf) using the formula: ntf_t,d = a + (1 - a) * (tf_t,d / tfmax(d)), where tfmax(d) is the maximum term frequency in d, tf_t,d is the raw frequency of term t in d, and a is a smoothing parameter (typically 0.4). The smoothing term a dampens the contribution of the second term to avoid large swings in ntf from modest changes in raw tf.

## Objective

normalize term frequencies to reduce document-length bias in scoring
## Applicable Signals

- raw tf-idf scores show bias toward longer documents
- query results dominated by documents with high absolute term frequencies
- vector space model scoring in use

## Contraindications

- stop word list is unstable or frequently changes (method is sensitive to stop word configuration)
- document contains outlier terms with unusually high occurrence counts not representative of document content
- ranking stability across different stop word configurations is required

## Workflow Steps

- Identify all terms τ in document d and their raw frequencies tf_τ,d
- Compute tfmax(d) = max(tf_τ,d) across all terms in d
- For each term t in d, apply formula: ntf_t,d = a + (1 - a) * (tf_t,d / tfmax(d))
- Use computed ntf values in place of raw tf in downstream scoring (e.g., tf-idf weighting)

## Constraints

- smoothing parameter a must be between 0 and 1; standard value is 0.4
- requires computation of tfmax(d) for each document before normalization
- method is unstable with respect to stop word list changes

## Cautions

- Changing the stop word list can dramatically alter term weightings and ranking order, making tuning difficult.
- Outlier terms with unusually large occurrence counts can skew normalization; consider preprocessing or outlier detection.

## Output Contract

- For each term t in document d, return normalized term frequency (ntf_t,d) as a real number between a and 1.0 (inclusive). This value is suitable for use in tf-idf and vector space scoring without document-length bias.

## Example Executions

### Example 1

- Input: Document d with term frequencies: term_A=5, term_B=3, term_C=1; smoothing parameter a=0.4
- Output: ntf_A,d = 1.0, ntf_B,d = 0.76, ntf_C,d = 0.52
- Notes: tfmax(d) = 5; highest-frequency term normalizes to 1.0, others scale proportionally with smoothing applied

### Example 2

- Input: Document d duplicated to create d′ (d appended to itself); raw tf-idf would score d′ twice as high as d
- Output: Maximum tf normalization prevents this anomaly; d and d′ receive comparable scores
- Notes: Demonstrates the key benefit: eliminates document-length bias from term repetition

## Triggers

- computing normalized term frequencies for vector space scoring
- document collection exhibits high length variation
- need to prevent longer documents from dominating relevance scores due to natural term repetition

## Examples

### Example 1

Input:

  Document d with term frequencies: term_A=5, term_B=3, term_C=1; smoothing parameter a=0.4

Output:

  ntf_A,d = 1.0, ntf_B,d = 0.76, ntf_C,d = 0.52

Notes:

  tfmax(d) = 5; highest-frequency term normalizes to 1.0, others scale proportionally with smoothing applied

### Example 2

Input:

  Document d duplicated to create d′ (d appended to itself); raw tf-idf would score d′ twice as high as d

Output:

  Maximum tf normalization prevents this anomaly; d and d′ receive comparable scores

Notes:

  Demonstrates the key benefit: eliminates document-length bias from term repetition
