---
id: "64a2c03d-4ee8-568b-b516-015944fb9eca"
name: "Weighted Zone Scoring"
description: "Assign differential weights to document zones (title, body, metadata, etc.) to amplify relevance of matches in high-value regions during scoring. Apply zone-based parametric indexing to reflect document structure in relevance ranking."
version: "0.1.0"
tags:
  - "information_retrieval"
  - "document_scoring"
  - "parametric_indexing"
  - "zone_weighting"
  - "relevance_ranking"
triggers:
  - "Document has structured zones or fields with varying importance"
  - "Need to prioritize matches in certain regions (e.g., title matches over body matches)"
  - "Relevance ranking should reflect document structure"
---

# Weighted Zone Scoring

Assign differential weights to document zones (title, body, metadata, etc.) to amplify relevance of matches in high-value regions during scoring. Apply zone-based parametric indexing to reflect document structure in relevance ranking.

## Prompt

Apply zone-based weights to document fields during scoring. Identify document zones (title, body, metadata, etc.), assign importance weights to each zone based on field-level priorities, and compute relevance scores that reflect the relative contribution of matches in each zone. Higher weights amplify the contribution of matches in high-value zones.

## Objective

zone_based_relevance_weighting
## Applicable Signals

- Document has explicit zones or field boundaries
- Caller specifies zone importance hierarchy
- Relevance ranking needs to account for field-level structure

## Contraindications

- Documents are unstructured or lack clear zone boundaries
- Zone boundaries are ambiguous or inconsistently defined
- Uniform weighting across all fields is required

## Workflow Steps

- Identify and define zone boundaries within each document
- Assign importance weights to each zone
- Compute zone-weighted relevance scores for query matches
- Aggregate scores across zones to produce final document ranking

## Constraints

- Zone definitions must be consistent across the document collection
- Weights must be assigned before scoring begins
- Zone boundaries must not overlap

## Output Contract

- Zone-weighted relevance scores for each document reflecting the importance of matches in each field
- Scores must be comparable across documents and suitable for ranking

## Triggers

- Document has structured zones or fields with varying importance
- Need to prioritize matches in certain regions (e.g., title matches over body matches)
- Relevance ranking should reflect document structure
