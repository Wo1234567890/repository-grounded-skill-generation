---
id: "42a09e34-29e8-510d-9e27-393a902a62f1"
name: "Weighted Zone Scoring"
description: "Assign different weights to terms based on their zone or field (e.g., title, body, metadata) to boost relevance of matches in high-value zones. Apply zone-specific weight multipliers to term scores before aggregation."
version: "0.1.0"
tags:
  - "scoring"
  - "term_weighting"
  - "zone_based"
  - "field_weighting"
  - "relevance_tuning"
triggers:
  - "document has multiple structured fields or zones"
  - "zone-specific importance is known or has been learned"
  - "term relevance varies by field location"
---

# Weighted Zone Scoring

Assign different weights to terms based on their zone or field (e.g., title, body, metadata) to boost relevance of matches in high-value zones. Apply zone-specific weight multipliers to term scores before aggregation.

## Prompt

For each term in a document, identify its zone (title, body, author, metadata, etc.). Multiply the term's base score by the weight assigned to that zone. Aggregate weighted scores across all zones. Use when document structure and zone importance are known or learned.

## Objective

adjust term weights by document zone
## Applicable Signals

- document schema includes zone metadata
- zone weights are available from training or configuration
- scoring must differentiate field-level importance

## Contraindications

- documents are flat or unstructured
- all zones have equal importance
- zone metadata is unavailable or unreliable

## Workflow Steps

- Identify the zone of each term occurrence in the document
- Retrieve the weight multiplier for that zone
- Multiply the term's base score by the zone weight
- Aggregate weighted scores across all zones for final term contribution

## Constraints

- zone weights must be pre-defined or learned before application
- term must be locatable within a known zone
- weight multipliers should be normalized to avoid score inflation

## Cautions

- zone weights that are too extreme may suppress relevant terms in low-weight zones
- ensure zone definitions are consistent across the document collection

## Output Contract

- Per-zone weight multipliers applied to term scores; aggregated final score reflects zone-adjusted term contributions.

## Triggers

- document has multiple structured fields or zones
- zone-specific importance is known or has been learned
- term relevance varies by field location
