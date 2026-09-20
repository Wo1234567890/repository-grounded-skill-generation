---
id: "c651de49-0a54-5af6-ac24-547343a892d1"
name: "Dataset trace filtering and preparation"
description: "Inject or update structured metadata into an active trace session during agent or workflow execution to enrich observability and debugging context with operation name, processing stage, record counts, user context, and execution tags."
version: "0.1.1"
tags:
  - "observability"
  - "debugging"
  - "trace_enrichment"
  - "metadata_injection"
  - "execution_context"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Evaluating cache eviction algorithms on historical trace data; need to exclude sparse or incomplete traces before benchmarking"
examples:
  - input: "Agent processing 1500 records in validation stage for user_123"
    output: "Metadata {operation_name: 'AI Agent Processing', processing_stage: 'data_validation', records_processed: 1500, user_id: 'user_123', tags: ['validation', 'production']} attached to trace"
    notes: "Metadata is immediately available in trace logs for downstream analysis"
---

# Dataset trace filtering and preparation

Inject or update structured metadata into an active trace session during agent or workflow execution to enrich observability and debugging context with operation name, processing stage, record counts, user context, and execution tags.

## Prompt

Call update_trace_metadata() with a dictionary containing operation_name, processing_stage, records_processed, user_id, tags, or other contextual fields. The metadata is immediately attached to the active trace and included in subsequent trace logs.

## Objective

Enrich active trace with contextual metadata
## Applicable Signals

- Trace session is initialized and active
- Execution checkpoint reached where metadata is relevant
- Observability enrichment is required mid-execution

## Contraindications

- Trace session has not been initialized
- Metadata contains sensitive information that should not be logged
- Execution is in pre-initialization or setup phase

## Workflow Steps

- Verify trace session is active
- Prepare metadata dictionary with operation_name, processing_stage, records_processed, user_id, tags, or other contextual fields
- Call update_trace_metadata(metadata_dict)
- Confirm metadata is attached to active trace

## Constraints

- Trace must be active before calling update_trace_metadata
- Metadata dictionary keys should be non-sensitive and audit-safe
- Call should occur during execution, not before trace initialization

## Cautions

- Do not inject personally identifiable information or secrets into trace metadata
- Ensure trace session is properly initialized before calling this skill

## Output Contract

- Metadata dictionary successfully attached to active trace; subsequent trace logs include the injected fields and are available for debugging and audit.

## Example Executions

### Example 1

- Input: Agent processing 1500 records in validation stage for user_123
- Output: Metadata {operation_name: 'AI Agent Processing', processing_stage: 'data_validation', records_processed: 1500, user_id: 'user_123', tags: ['validation', 'production']} attached to trace
- Notes: Metadata is immediately available in trace logs for downstream analysis

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Evaluating cache eviction algorithms on historical trace data; need to exclude sparse or incomplete traces before benchmarking

## Examples

### Example 1

Input:

  Agent processing 1500 records in validation stage for user_123

Output:

  Metadata {operation_name: 'AI Agent Processing', processing_stage: 'data_validation', records_processed: 1500, user_id: 'user_123', tags: ['validation', 'production']} attached to trace

Notes:

  Metadata is immediately available in trace logs for downstream analysis
