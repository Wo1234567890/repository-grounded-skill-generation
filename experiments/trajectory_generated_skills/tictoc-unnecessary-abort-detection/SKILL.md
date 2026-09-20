---
name: tictoc-unnecessary-abort-analysis
description: Analyze TicToc transaction traces to distinguish necessary validation aborts from avoidable aborts using timestamp and per-key access-order evidence.
---

# TicToc Unnecessary-Abort Analysis

## When to Use

Use this skill for transaction-trace analysis where an optimistic concurrency-control system logs read/validation timestamps separately from committed writes and the goal is to decide whether an observed abort was actually required.

## Workflow

1. **Parse the trace schema exactly.** Keep transaction id, key id, local/read WTS, current WTS, candidate commit timestamp, write timestamp, and the per-key access counters as separate fields. Do not infer column meanings from position after parsing.
2. **Index writes by key and timestamp.** The write trace is the evidence for which committed write installed a particular WTS. Preserve the per-key access counter because it gives ordering information that timestamps alone may not reveal.
3. **Group abort records by transaction.** A transaction can have more than one validation failure. Make the transaction-level decision only after examining all of its abort records.
4. **Reconstruct the conflict around each aborted key.** Compare the local WTS, current WTS, candidate commit timestamp, matching committed write, and access-counter ordering. The access counters from the abort and write traces refer to the same per-key counter and should be used to reason about when the relevant write occurred.
5. **Do not reduce the policy to one timestamp inequality.** A no-skill run obtained only partial credit after classifying aborts mainly from `current_wts` versus `commit_ts`; another run tried to match `current_wts` to a write without fully using the access-order information. Treat both as warning signs that the trace must be joined and ordered, not classified from a single field.
6. **Aggregate conservatively.** If an aborting transaction has multiple recorded causes, ensure the policy for labeling the whole transaction follows the evidence for every relevant cause rather than a convenient subset.
7. **Validate output invariants.** The final transaction ids should be unique, unsigned integers, and sorted ascending. Check these properties independently from the detection logic.

## Diagnostic Checks

Before trusting the result, sample several transactions from both classes and print the complete evidence tuple for each aborted key: local WTS, current WTS, candidate commit timestamp, matching write WTS, write access counter, and abort access counter. If the explanation cannot account for the access-counter fields, the policy is probably incomplete.

## Common Failure Modes

- Ignoring `ats_at_write` and `ats_at_abort` even though the trace explicitly provides them.
- Assuming a changed WTS automatically proves a necessary conflict.
- Assuming `current_wts > commit_ts` alone proves an unnecessary abort.
- Deciding at record level when the requested output is transaction level.
- Producing a plausible count without manually checking representative cases.
