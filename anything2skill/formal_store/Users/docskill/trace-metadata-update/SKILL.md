---
id: "3196bcac-f0d9-56c4-9f76-d7964def7deb"
name: "Trace Metadata Update"
description: "Programmatically inject or update execution metadata into an active trace during agent processing. Enriches trace logs with runtime context such as operation name, processing stage, record counts, user ID, and custom tags for debugging and monitoring."
version: "0.1.0"
tags:
  - "instrumentation"
  - "observability"
  - "trace_enrichment"
  - "debugging"
  - "metadata"
triggers:
  - "Agent is actively processing data"
  - "Need to log operation name, processing stage, or record count"
  - "User context or custom tags must be captured for observability"
---

# Trace Metadata Update

Programmatically inject or update execution metadata into an active trace during agent processing. Enriches trace logs with runtime context such as operation name, processing stage, record counts, user ID, and custom tags for debugging and monitoring.

## Prompt

Call update_trace_metadata() with a dictionary containing runtime context fields. Pass operation_name (string), processing_stage (string), records_processed (integer), user_id (string), and tags (list of strings). The metadata is recorded in the active trace and becomes available for inspection or export.

## Objective

Inject runtime context into trace execution
## Applicable Signals

- Active trace execution in progress
- Runtime data available (stage, count, user context)
- Observability or debugging requirement

## Contraindications

- Trace has not been initialized
- Metadata is static and known at trace start
- No active agent execution context

## Workflow Steps

- Verify trace is initialized and active
- Prepare metadata dictionary with operation_name, processing_stage, records_processed, user_id, and tags
- Call update_trace_metadata() with the dictionary
- Confirm metadata is recorded in the active trace

## Constraints

- Trace must be active before calling update_trace_metadata()
- Metadata dictionary keys must match expected field names

## Output Contract

- Metadata fields are recorded in the active trace and available for later inspection or export

## Triggers

- Agent is actively processing data
- Need to log operation name, processing stage, or record count
- User context or custom tags must be captured for observability
