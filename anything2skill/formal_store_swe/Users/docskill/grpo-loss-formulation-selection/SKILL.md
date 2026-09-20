---
id: "59e2d07f-8b62-5796-bcfb-b3020644e76d"
name: "GRPO Loss Formulation Selection"
description: "Normalize document scores by document length to prevent bias toward longer documents. Apply pivoted normalization or length-aware weighting when term frequency distributions are skewed by document size."
version: "0.1.1"
tags:
  - "tf-idf"
  - "scoring"
  - "normalization"
  - "document-length"
  - "bias-correction"
triggers:
  - "Initializing GRPOConfig for training"
  - "Need to choose between standard GRPO and DR-GRPO loss formulations"
  - "Maximum completion length is known or available"
---

# GRPO Loss Formulation Selection

Normalize document scores by document length to prevent bias toward longer documents. Apply pivoted normalization or length-aware weighting when term frequency distributions are skewed by document size.

## Prompt

When scoring documents with variable lengths, apply length normalization to prevent longer documents from receiving artificially higher scores due to higher term frequencies. Use pivoted normalization or a length-aware weighting scheme that accounts for document length (CharLength) as a parameter in the scoring function.

## Objective

Correct length bias in TF-IDF scoring
## Applicable Signals

- Length variance detected in document collection
- Score distribution skewed by document size
- Need for fair cross-length document comparison

## Contraindications

- All documents are uniform length
- Length bias is intentional for the use case
- Cosine normalization already applied to scores

## Workflow Steps

- Measure document length (CharLength) for each document in collection
- Identify length bias in raw TF-IDF scores (e.g., correlation analysis)
- Select normalization scheme: pivoted normalization or length-aware weighting
- Apply normalization factor to TF-IDF scores based on document length
- Validate that length bias is eliminated and ranking quality is maintained

## Constraints

- Document length (CharLength) must be available or computable
- Normalization must not eliminate legitimate term frequency signals
- Pivoted normalization parameters must be tuned to collection characteristics

## Cautions

- Over-normalization can suppress legitimate longer-document relevance
- Normalization scheme choice depends on term frequency distribution shape
- Verify that normalized scores still rank relevant documents higher

## Output Contract

- Length-normalized score for each document; bias toward longer documents eliminated; scores remain comparable across documents of different lengths

## Triggers

- Initializing GRPOConfig for training
- Need to choose between standard GRPO and DR-GRPO loss formulations
- Maximum completion length is known or available
