---
id: "65286d8c-4994-55fa-8fd2-b4ffad35b6cc"
name: "Trace Grouping for Operation Sequencing"
description: "Use @trace decorator or manual trace management to group and record sequences of agent operations as logical units of work. Essential when auto_start_session=False to ensure data capture."
version: "0.1.0"
tags:
  - "instrumentation"
  - "tracing"
  - "operation_grouping"
  - "debugging"
  - "session_management"
triggers:
  - "Agent performs multi-step operations that should be grouped"
  - "auto_start_session is False in agentops.init()"
  - "Need to record logical work units for debugging or audit"
---

# Trace Grouping for Operation Sequencing

Use @trace decorator or manual trace management to group and record sequences of agent operations as logical units of work. Essential when auto_start_session=False to ensure data capture.

## Prompt

Apply @trace decorator to a function or use agentops.start_trace() manually to wrap a sequence of operations. This creates a logical boundary around multi-step work, ensuring all operations within that scope are grouped and recorded together. When auto_start_session=False, explicit trace management is required for any data to be captured.

## Objective

group_and_record_operation_sequences
## Applicable Signals

- Multiple sequential operations within a single logical task
- Session initialization with auto_start_session=False
- Requirement to isolate and review operation groups

## Contraindications

- Session auto-starts and all operations are already captured
- Tracing overhead is unacceptable for performance-critical paths
- Single isolated operations that do not require grouping

## Workflow Steps

- Import trace decorator: from agentops.sdk.decorators import trace
- Apply @trace decorator to function or call agentops.start_trace() before operation sequence
- Execute the sequence of operations within the trace scope
- Trace automatically closes at function end or manual agentops.end_trace() call
- Grouped trace record is recorded and available for review

## Constraints

- If auto_start_session=False, @trace or agentops.start_trace() must be used for data to be recorded
- Trace boundaries must wrap the complete operation sequence intended as a logical unit

## Output Contract

- Grouped trace record containing all operations within the decorated or manually-managed scope, ready for debugging or audit review

## Triggers

- Agent performs multi-step operations that should be grouped
- auto_start_session is False in agentops.init()
- Need to record logical work units for debugging or audit
