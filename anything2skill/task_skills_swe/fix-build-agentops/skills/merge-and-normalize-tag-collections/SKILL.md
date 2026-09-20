---
id: "5a6fb1c5-9833-5a9c-82ec-fc347161461e"
name: "Merge and Normalize Tag Collections"
description: "Combine user-provided tags with default tags into a single deduplicated collection. Handles cases where one or both tag sources are present, absent, or null. Prepares normalized tag input for downstream session initialization."
version: "0.1.0"
tags:
  - "initialization"
  - "data_preparation"
  - "collection_merge"
  - "deduplication"
  - "configuration"
triggers:
  - "Initializing a tracing or monitoring session with optional user tags and system default tags"
  - "Both tag sources may be None, one, or both present"
examples:
  - input: "{'tags': ['user_tag_1', 'user_tag_2'], 'default_tags': ['default_tag_1', 'user_tag_1']}"
    output: "{'merged_tags': ['user_tag_1', 'user_tag_2', 'default_tag_1']}"
    notes: "Duplicates removed; order may vary due to set conversion"
  - input: "{'tags': ['user_tag_1'], 'default_tags': None}"
    output: "{'merged_tags': ['user_tag_1']}"
    notes: "Only user tags provided"
  - input: "{'tags': None, 'default_tags': None}"
    output: "{'merged_tags': None}"
    notes: "No tags provided; returns None"
---

# Merge and Normalize Tag Collections

Combine user-provided tags with default tags into a single deduplicated collection. Handles cases where one or both tag sources are present, absent, or null. Prepares normalized tag input for downstream session initialization.

## Prompt

Merge two optional tag lists (tags and default_tags) into a single deduplicated collection. If both are provided, combine and remove duplicates. If only one is provided, use it. If neither is provided, return None. The result is ready for downstream configuration.

## Objective

Normalize tag input for downstream initialization
## Applicable Signals

- tags parameter is provided
- default_tags parameter is provided
- Either or both parameters are None

## Contraindications

- Tags are already merged
- Tag deduplication is not required
- Tags are immutable or order-sensitive

## Workflow Steps

- {'step': 1, 'action': 'Check if both tags and default_tags are provided and non-empty', 'condition': 'tags is not None and default_tags is not None'}
- {'step': 2, 'action': 'If both present, concatenate and deduplicate using set conversion', 'condition': 'Both inputs are truthy', 'operation': 'merged_tags = list(set(tags + default_tags))'}
- {'step': 3, 'action': 'If only tags is provided, assign it directly', 'condition': 'tags is not None and default_tags is None', 'operation': 'merged_tags = tags'}
- {'step': 4, 'action': 'If only default_tags is provided, assign it directly', 'condition': 'tags is None and default_tags is not None', 'operation': 'merged_tags = default_tags'}
- {'step': 5, 'action': 'If neither is provided, set to None', 'condition': 'tags is None and default_tags is None', 'operation': 'merged_tags = None'}

## Constraints

- Input tags must be iterable (list or None)
- Input default_tags must be iterable (list or None)
- Output must be a list or None, never an empty list when both inputs are absent

## Cautions

- Set conversion removes order; if tag order is significant, preserve original order during merge
- Empty lists are treated as falsy; verify intended behavior for empty input lists

## Output Contract

- A single merged_tags list (or None if both inputs are absent) with duplicates removed and ready for downstream configuration. Output is always either a deduplicated list or None.

## Example Executions

### Example 1

- Input: {'tags': ['user_tag_1', 'user_tag_2'], 'default_tags': ['default_tag_1', 'user_tag_1']}
- Output: {'merged_tags': ['user_tag_1', 'user_tag_2', 'default_tag_1']}
- Notes: Duplicates removed; order may vary due to set conversion

### Example 2

- Input: {'tags': ['user_tag_1'], 'default_tags': None}
- Output: {'merged_tags': ['user_tag_1']}
- Notes: Only user tags provided

### Example 3

- Input: {'tags': None, 'default_tags': None}
- Output: {'merged_tags': None}
- Notes: No tags provided; returns None

## Triggers

- Initializing a tracing or monitoring session with optional user tags and system default tags
- Both tag sources may be None, one, or both present

## Examples

### Example 1

Input:

  {'tags': ['user_tag_1', 'user_tag_2'], 'default_tags': ['default_tag_1', 'user_tag_1']}

Output:

  {'merged_tags': ['user_tag_1', 'user_tag_2', 'default_tag_1']}

Notes:

  Duplicates removed; order may vary due to set conversion

### Example 2

Input:

  {'tags': ['user_tag_1'], 'default_tags': None}

Output:

  {'merged_tags': ['user_tag_1']}

Notes:

  Only user tags provided

### Example 3

Input:

  {'tags': None, 'default_tags': None}

Output:

  {'merged_tags': None}

Notes:

  No tags provided; returns None
