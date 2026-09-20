---
id: "e7308f6d-3afc-58b8-9cc8-ce069b1e7c5f"
name: "TF-IDF Term Weighting Scheme Selection"
description: "Select and apply appropriate TF-IDF weighting notation and parameters based on document collection characteristics and retrieval goals. Guides choice among established schemes documented in SMART notation."
version: "0.1.0"
tags:
  - "tf-idf"
  - "term_weighting"
  - "vector_space_model"
  - "information_retrieval"
  - "indexing"
  - "smart_notation"
triggers:
  - "Building a new vector space retrieval system"
  - "Tuning an existing retrieval index"
  - "Collection characteristics are known and documented"
  - "Need to decide between competing TF-IDF variants"
---

# TF-IDF Term Weighting Scheme Selection

Select and apply appropriate TF-IDF weighting notation and parameters based on document collection characteristics and retrieval goals. Guides choice among established schemes documented in SMART notation.

## Prompt

When building or tuning a vector space retrieval system, determine the optimal TF-IDF weighting configuration. Review collection characteristics (term frequency distribution, document length variance, term rarity patterns). Consult SMART notation (Salton and Buckley 1988; Singhal et al. 1995, 1996b) to map your constraints to a feasible weighting scheme. Document the selected scheme notation and apply it consistently across the entire document collection during indexing preparation.

## Objective

Choose optimal term weighting configuration for vector space retrieval
## Applicable Signals

- Document collection statistics available (term frequency distribution, document lengths)
- Retrieval performance baseline or target defined
- Index control and configuration authority present

## Contraindications

- Using probabilistic language models (alternative weighting framework)
- Applying non-TF-IDF weighting schemes
- Real-time query-only scenarios without index control
- Streaming or dynamic collections requiring online weight adaptation

## Workflow Steps

- {'step': 1, 'action': 'Analyze collection characteristics', 'detail': 'Examine term frequency distribution, document length variance, and term rarity patterns in the collection'}
- {'step': 2, 'action': 'Review SMART notation options', 'detail': 'Consult established TF-IDF weighting schemes in SMART notation (Salton and Buckley 1988; Singhal et al. 1995, 1996b)'}
- {'step': 3, 'action': 'Map constraints to scheme', 'detail': 'Match collection characteristics and retrieval goals to a feasible weighting function'}
- {'step': 4, 'action': 'Document scheme selection', 'detail': 'Record the selected SMART notation specification and rationale'}
- {'step': 5, 'action': 'Apply consistently', 'detail': 'Implement the chosen scheme uniformly across all documents during indexing'}

## Constraints

- SMART notation scheme must be selected before weight computation begins
- Chosen scheme must be applied consistently across all documents in the collection
- Collection characteristics must be stable or re-evaluated if collection composition changes significantly

## Cautions

- Hill-climbing optimization of weighting schemes may not converge to best combinations (Moffat and Zobel 1998)
- Not all SMART notation versions are consistent; align on a single reference (e.g., Singhal et al. 1996b)
- Medium-frequency terms are often more informative than rare or very common terms; scheme should reflect this

## Output Contract

- Documented weighting scheme selection (expressed in SMART notation) that is applied consistently across the entire document collection. Output includes: (1) scheme notation specification, (2) rationale linking collection characteristics to scheme choice, (3) confirmation of uniform application during indexing.

## Triggers

- Building a new vector space retrieval system
- Tuning an existing retrieval index
- Collection characteristics are known and documented
- Need to decide between competing TF-IDF variants
