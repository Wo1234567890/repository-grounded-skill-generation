---
id: "df67ec1f-c742-5911-a969-bd427ebd604b"
name: "Term Frequency Extraction and Tabulation"
description: "Count occurrences of selected terms across a document collection and organize results into a term-document frequency matrix. This is the foundational data collection step for vector space model construction, producing raw frequency counts that serve as input to downstream weighting and normalization workflows."
version: "0.1.0"
tags:
  - "term_frequency"
  - "document_analysis"
  - "vector_space_model"
  - "indexing"
  - "information_retrieval"
triggers:
  - "Starting a vector space model workflow"
  - "Have a raw document collection and a defined term list"
  - "Need to prepare data for tf-idf weighting or vector normalization"
examples:
  - input: "Document collection: three novels (Sense and Sensibility, Pride and Prejudice, Wuthering Heights); term list: [affection, jealous, gossip]"
    output: "Matrix with affection: [115, 58, 20], jealous: [10, 7, 11], gossip: [2, 0, 6]"
    notes: "Raw counts organized by term and document; ready for normalization or weighting"
---

# Term Frequency Extraction and Tabulation

Count occurrences of selected terms across a document collection and organize results into a term-document frequency matrix. This is the foundational data collection step for vector space model construction, producing raw frequency counts that serve as input to downstream weighting and normalization workflows.

## Prompt

For each term in your selected term list, count its occurrences in each document in the collection. Organize counts into a matrix with terms as rows and documents as columns. Ensure all documents are represented and all term counts are recorded as non-negative integers. This matrix becomes the input for tf-idf weighting and vector normalization.

## Objective

build_term_frequency_matrix
## Applicable Signals

- Document collection is available
- Term vocabulary has been selected or extracted
- Downstream task requires term frequency input

## Contraindications

- Only boolean presence/absence of terms is needed (use simpler binary indexing instead)
- Term frequencies are not available or not relevant to the task
- Documents are too large or numerous for manual frequency counting without automated tools

## Workflow Steps

- Define the term vocabulary (list of terms to count)
- Initialize a matrix with terms as rows and documents as columns
- For each document, scan and count occurrences of each term
- Record counts in the corresponding matrix cell
- Verify matrix completeness: all cells populated, no missing documents or terms

## Constraints

- All selected terms must be consistently counted across all documents
- Frequency counts must be non-negative integers
- Matrix must include all documents in the collection and all terms in the vocabulary

## Cautions

- Ensure term matching is case-consistent and handles stemming/normalization uniformly if required
- Verify that the term list is complete before beginning counting to avoid incomplete matrices
- Document the counting methodology (e.g., whole-word match vs. substring) for reproducibility

## Output Contract

- A term-document frequency matrix with raw occurrence counts (rows = terms, columns = documents, cells = non-negative integer counts). Format: term 'affection' appears 115 times in document SaS, 58 times in PaP, 20 times in WH. This matrix is ready for downstream tf-idf weighting, normalization, or vector space model construction.

## Example Therapist Responses

### Example 1

- Client/Input: Document collection: three novels (Sense and Sensibility, Pride and Prejudice, Wuthering Heights); term list: [affection, jealous, gossip]
- Therapist/Output: Matrix with affection: [115, 58, 20], jealous: [10, 7, 11], gossip: [2, 0, 6]
- Notes: Raw counts organized by term and document; ready for normalization or weighting

## Triggers

- Starting a vector space model workflow
- Have a raw document collection and a defined term list
- Need to prepare data for tf-idf weighting or vector normalization

## Examples

### Example 1

Input:

  Document collection: three novels (Sense and Sensibility, Pride and Prejudice, Wuthering Heights); term list: [affection, jealous, gossip]

Output:

  Matrix with affection: [115, 58, 20], jealous: [10, 7, 11], gossip: [2, 0, 6]

Notes:

  Raw counts organized by term and document; ready for normalization or weighting
