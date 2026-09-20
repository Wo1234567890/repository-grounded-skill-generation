---
id: "5ebd86ca-a2fc-50e7-a728-868be97b707d"
name: "TF-IDF Weighting Reference"
description: "Canonical reference knowledge on term frequency–inverse document frequency (tf-idf) weighting, including maximum tf normalization, smoothing parameters, and documented failure modes such as length bias, stop word sensitivity, and outlier term instability."
version: "0.1.0"
tags:
  - "tf-idf"
  - "term_weighting"
  - "normalization"
  - "smoothing"
  - "vector_space_model"
  - "length_bias"
triggers:
  - "Designing or reviewing term weighting schemes"
  - "Troubleshooting ranking anomalies or relevance issues"
  - "Learning or teaching tf-idf and normalization techniques"
  - "Evaluating document length bias in scoring"
examples:
  - input: "Reviewing a ranking system where longer documents consistently score higher despite lower relevance."
    output: "Reference explains that raw tf scoring inflates scores for longer documents due to word repetition. Maximum tf normalization mitigates this by dividing tf by the maximum tf in the document, scaled by smoothing parameter a (typically 0.4)."
    notes: "Illustrates the length bias anomaly and the normalization solution."
  - input: "Troubleshooting why changing the stop word list causes dramatic shifts in term weightings."
    output: "Reference documents that maximum tf normalization is unstable under stop word list changes because tfmax(d) can shift significantly, altering the normalized weights for all terms in the document."
    notes: "Highlights a known tuning difficulty with the method."
---

# TF-IDF Weighting Reference

Canonical reference knowledge on term frequency–inverse document frequency (tf-idf) weighting, including maximum tf normalization, smoothing parameters, and documented failure modes such as length bias, stop word sensitivity, and outlier term instability.

## Prompt

This asset provides conceptual and historical context for tf-idf weighting schemes. It documents the rationale for smoothing terms, the vector space model foundation, and known failure modes. Use this to inform design decisions, troubleshoot ranking anomalies, or teach tf-idf principles. Do not use this for immediate operational scoring; instead, delegate to micro_skill or safety_rule for live execution.

## Objective

provide_tf_idf_weighting_context
## Applicable Signals

- Query relevance ranking appears skewed by document length
- Need to understand smoothing parameter role in normalization
- Reviewing vector space model implementation
- Assessing stability of weighting under stop word list changes

## Contraindications

- When immediate operational scoring decisions are needed (delegate to micro_skill or safety_rule instead)
- When domain-specific weighting schemes override tf-idf
- When live ranking must be executed without design review

## Constraints

- This is a reference asset; it informs design but does not directly execute scoring
- Smoothing parameter a is typically set to 0.4 (some early work used 0.5)
- Maximum tf normalization formula: ntf_t,d = a + (1 - a) * (tf_t,d / tfmax(d))

## Cautions

- Maximum tf normalization is unstable: changes to stop word lists can dramatically alter term weightings and ranking
- Outlier terms with unusually large occurrence counts may not be representative of document content and can distort normalization
- Raw tf scoring assigns higher frequencies to longer documents merely because they repeat words; this can inflate relevance scores inappropriately

## Output Contract

- Documented understanding of tf-idf principles, smoothing rationale, maximum tf normalization formula, and known failure modes (length bias, stop word sensitivity, outlier term instability). Caller receives conceptual grounding for design or troubleshooting decisions.

## Example Therapist Responses

### Example 1

- Client/Input: Reviewing a ranking system where longer documents consistently score higher despite lower relevance.
- Therapist/Output: Reference explains that raw tf scoring inflates scores for longer documents due to word repetition. Maximum tf normalization mitigates this by dividing tf by the maximum tf in the document, scaled by smoothing parameter a (typically 0.4).
- Notes: Illustrates the length bias anomaly and the normalization solution.

### Example 2

- Client/Input: Troubleshooting why changing the stop word list causes dramatic shifts in term weightings.
- Therapist/Output: Reference documents that maximum tf normalization is unstable under stop word list changes because tfmax(d) can shift significantly, altering the normalized weights for all terms in the document.
- Notes: Highlights a known tuning difficulty with the method.

## Triggers

- Designing or reviewing term weighting schemes
- Troubleshooting ranking anomalies or relevance issues
- Learning or teaching tf-idf and normalization techniques
- Evaluating document length bias in scoring

## Examples

### Example 1

Input:

  Reviewing a ranking system where longer documents consistently score higher despite lower relevance.

Output:

  Reference explains that raw tf scoring inflates scores for longer documents due to word repetition. Maximum tf normalization mitigates this by dividing tf by the maximum tf in the document, scaled by smoothing parameter a (typically 0.4).

Notes:

  Illustrates the length bias anomaly and the normalization solution.

### Example 2

Input:

  Troubleshooting why changing the stop word list causes dramatic shifts in term weightings.

Output:

  Reference documents that maximum tf normalization is unstable under stop word list changes because tfmax(d) can shift significantly, altering the normalized weights for all terms in the document.

Notes:

  Highlights a known tuning difficulty with the method.
