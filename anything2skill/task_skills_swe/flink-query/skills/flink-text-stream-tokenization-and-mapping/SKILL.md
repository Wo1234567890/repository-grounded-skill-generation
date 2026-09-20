---
id: "31671217-0e8c-5d85-87b1-5df615dd24fc"
name: "Flink Text Stream Tokenization and Mapping"
description: "Apply flatMap to split incoming text by word boundaries (non-word characters), filter empty tokens, normalize to lowercase, and map each word to a (word, count) tuple. Use this micro-operation to normalize and structure raw text input for downstream aggregation in streaming pipelines."
version: "0.1.0"
tags:
  - "text_processing"
  - "tokenization"
  - "flatmap"
  - "stream_transformation"
  - "data_normalization"
triggers:
  - "Receive unstructured text from a socket or file source; need to extract individual words or tokens; must prepare data for key-based grouping"
examples:
  - input: "\"hello world\""
    output: "[(\"hello\", 1), (\"world\", 1)]"
    notes: "Single line split into two word tuples"
  - input: "\"hello, world! hello.\""
    output: "[(\"hello\", 1), (\"world\", 1), (\"hello\", 1)]"
    notes: "Punctuation removed by \\W+ boundary; duplicate words emit separate tuples"
  - input: "\"\""
    output: "[]"
    notes: "Empty line produces no output after filtering"
---

# Flink Text Stream Tokenization and Mapping

Apply flatMap to split incoming text by word boundaries (non-word characters), filter empty tokens, normalize to lowercase, and map each word to a (word, count) tuple. Use this micro-operation to normalize and structure raw text input for downstream aggregation in streaming pipelines.

## Prompt

Split each incoming text line by non-word character boundaries (\W+), filter out empty strings, convert to lowercase, and emit (word, 1) tuples. This prepares raw text for keying and windowed aggregation.

## Objective

Transform raw text stream into structured (key, value) tuples suitable for keying and windowing
## Applicable Signals

- Receive unstructured text from socket or file source
- Need to extract individual words or tokens from raw text
- Must prepare data for key-based grouping and windowing
- Input is line-delimited text requiring word-level decomposition

## Contraindications

- Input is already tokenized or structured as tuples
- Require custom tokenization logic beyond word-boundary splitting
- Need to preserve whitespace, punctuation, or case sensitivity
- Processing binary or non-text data streams

## Workflow Steps

- {'step': 1, 'action': 'Apply flatMap to incoming text stream', 'detail': 'For each line, split by non-word character boundary (\\W+)'}
- {'step': 2, 'action': 'Filter empty tokens', 'detail': 'Remove zero-length strings resulting from consecutive delimiters'}
- {'step': 3, 'action': 'Normalize case', 'detail': 'Convert each token to lowercase for consistent grouping'}
- {'step': 4, 'action': 'Map to tuple', 'detail': 'Emit (word, 1) tuple for each token'}

## Constraints

- Input must be text-based (String or line-delimited format)
- Output tuple structure is fixed as (String, Integer)
- Tokenization uses standard regex word boundary; custom delimiters require separate skill
- Operates on individual lines; does not preserve cross-line context

## Cautions

- Large vocabularies may cause memory pressure in downstream keying; consider vocabulary pruning for high-cardinality streams
- Case normalization is applied; preserve original case if needed by using a separate variant
- Empty input lines produce no output tuples; verify source does not rely on line-count preservation

## Output Contract

- DataStream<Tuple2<String, Integer>> where each tuple is (word, 1), ready for keyBy and windowed aggregation operations

## Example Executions

### Example 1

- Input: "hello world"
- Output: [("hello", 1), ("world", 1)]
- Notes: Single line split into two word tuples

### Example 2

- Input: "hello, world! hello."
- Output: [("hello", 1), ("world", 1), ("hello", 1)]
- Notes: Punctuation removed by \W+ boundary; duplicate words emit separate tuples

### Example 3

- Input: ""
- Output: []
- Notes: Empty line produces no output after filtering

## Triggers

- Receive unstructured text from a socket or file source; need to extract individual words or tokens; must prepare data for key-based grouping

## Examples

### Example 1

Input:

  "hello world"

Output:

  [("hello", 1), ("world", 1)]

Notes:

  Single line split into two word tuples

### Example 2

Input:

  "hello, world! hello."

Output:

  [("hello", 1), ("world", 1), ("hello", 1)]

Notes:

  Punctuation removed by \W+ boundary; duplicate words emit separate tuples

### Example 3

Input:

  ""

Output:

  []

Notes:

  Empty line produces no output after filtering
