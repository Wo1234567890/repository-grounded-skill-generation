---
id: "456ab70d-5672-585b-8d16-a5ffad1d03ff"
name: "Collection Frequency vs Document Frequency Distinction"
description: "Canonical reference for D3 selection methods and event handling patterns. Provides lookup documentation for selection operations, data binding (enter/update/exit), datum access, and event binding APIs."
version: "0.1.1"
tags:
  - "d3"
  - "selection"
  - "data-binding"
  - "event-handling"
  - "api-reference"
triggers:
  - "Choosing between collection-wide term frequency and document-specific term frequency for weighting"
  - "Debugging unexpected ranking differences between cf-based and df-based scoring"
  - "Evaluating why two terms with similar collection frequencies rank differently"
examples:
  - input: "Term 'try' in Reuters collection"
    output: "cf=10422 (total occurrences), df=8760 (documents containing it). High cf with high df indicates common term across many documents."
    notes: "Suggests moderate discriminative power for ranking"
  - input: "Term 'insurance' in Reuters collection"
    output: "cf=10440 (total occurrences), df=3997 (documents containing it). Similar cf to 'try' but much lower df indicates concentrated occurrence."
    notes: "Suggests higher discriminative power; term appears intensely in fewer documents"
---

# Collection Frequency vs Document Frequency Distinction

Canonical reference for D3 selection methods and event handling patterns. Provides lookup documentation for selection operations, data binding (enter/update/exit), datum access, and event binding APIs.

## Prompt

Use this reference to identify and understand D3 selection API methods (data binding, enter/update/exit patterns, datum access) and event handling patterns. Look up method signatures and usage contexts for selection operations.

## Objective

Provide reusable reference for D3 selection and event APIs
## Applicable Signals

- Developer needs to look up D3 selection method signatures
- Need to understand data binding patterns (enter, update, exit)
- Require event handling API documentation
- Seeking correct method for element-data association

## Contraindications

- Do not use for executing a specific visualization task
- Do not use as a procedural workflow; this is documentation only
- Do not use for implementation guidance beyond API signatures

## Workflow Steps

- Identify the selection operation needed (data binding, enter/update/exit, datum access, or event handling)
- Locate the corresponding D3 API method in the reference
- Return method signature and usage context

## Constraints

- Reference is limited to D3 selection and event handling APIs
- Does not include implementation examples or procedural workflows

## Output Contract

- Correct API method identified and documented for developer reference
- Includes method name, purpose, and applicable context
- Covers selection.data, selection.join, selection.enter, selection.exit, selection.datum, and event handling patterns

## Triggers

- Choosing between collection-wide term frequency and document-specific term frequency for weighting
- Debugging unexpected ranking differences between cf-based and df-based scoring
- Evaluating why two terms with similar collection frequencies rank differently

## Examples

### Example 1

Input:

  Term 'try' in Reuters collection

Output:

  cf=10422 (total occurrences), df=8760 (documents containing it). High cf with high df indicates common term across many documents.

Notes:

  Suggests moderate discriminative power for ranking

### Example 2

Input:

  Term 'insurance' in Reuters collection

Output:

  cf=10440 (total occurrences), df=3997 (documents containing it). Similar cf to 'try' but much lower df indicates concentrated occurrence.

Notes:

  Suggests higher discriminative power; term appears intensely in fewer documents
