---
id: "77456f75-5da3-5604-bfcb-ec247cd860d5"
name: "Weighted Zone Scoring"
description: "Assign differential weights to term occurrences across document zones (title, abstract, body, keywords, metadata) to reflect structural importance and relevance signals. Applies zone-specific multipliers to term frequencies and combines weighted contributions into a normalized relevance score."
version: "0.1.0"
tags:
  - "term_weighting"
  - "document_structure"
  - "relevance_scoring"
  - "zone_based"
  - "information_retrieval"
triggers:
  - "documents have structured zones (title, abstract, body, keywords)"
  - "terms in certain zones are more indicative of relevance"
  - "need to boost or suppress zone-specific matches"
---

# Weighted Zone Scoring

Assign differential weights to term occurrences across document zones (title, abstract, body, keywords, metadata) to reflect structural importance and relevance signals. Applies zone-specific multipliers to term frequencies and combines weighted contributions into a normalized relevance score.

## Prompt

For each term in the query, identify which document zones it appears in (title, abstract, body, keywords, etc.). Apply zone-specific weights to the term frequency in each zone. Combine weighted contributions across zones to produce a final relevance score that reflects the structural importance of term matches.

## Objective

weight_terms_by_zone
## Applicable Signals

- document zone boundaries are clearly defined
- zone-specific term frequency data is available
- relevance varies significantly by zone

## Contraindications

- documents are unstructured or flat
- zone boundaries are unclear or unreliable
- computational cost of zone parsing is prohibitive

## Workflow Steps

- Parse document into zones (title, abstract, body, keywords, metadata)
- For each query term, identify zone occurrences and extract term frequency per zone
- Apply zone-specific weight multiplier to each zone's term frequency
- Combine weighted contributions across all zones
- Return normalized weighted score

## Constraints

- zone weights must be pre-defined or learned from training data
- zone boundaries must be reliably extractable from document structure

## Output Contract

- Weighted term frequency values per zone; combined score reflecting zone-weighted contributions to overall relevance score

## Triggers

- documents have structured zones (title, abstract, body, keywords)
- terms in certain zones are more indicative of relevance
- need to boost or suppress zone-specific matches
