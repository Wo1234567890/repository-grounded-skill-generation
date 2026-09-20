---
id: "f2930544-a6e7-58c2-beb2-0dcabd03a5d6"
name: "Preemptive Abort Decision"
description: "Determines whether a transaction should abort before acquiring write-set locks by checking tuple timestamps (wts, rts) against the transaction's approximate commit timestamp. This reduces unnecessary lock acquisition and contention in validation phases."
version: "0.1.0"
tags:
  - "concurrency_control"
  - "transaction_validation"
  - "lock_contention_reduction"
  - "timestamp_based_validation"
  - "optimization"
triggers:
  - "Transaction enters validation phase with read set and write set"
  - "Tuple timestamps (wts, rts) are atomically readable from TS_word"
  - "Transaction's approximate commit timestamp can be determined"
---

# Preemptive Abort Decision

Determines whether a transaction should abort before acquiring write-set locks by checking tuple timestamps (wts, rts) against the transaction's approximate commit timestamp. This reduces unnecessary lock acquisition and contention in validation phases.

## Prompt

Before locking tuples in the transaction's write set, atomically read each tuple's TS_word to extract wts and rts. Compare the transaction's approximate commit timestamp against these values. If validation will fail (e.g., tuple's local rts is less than commit timestamp and local wts does not match tuple's latest wts), abort immediately without acquiring locks. Sleep briefly (e.g., 1 µs) before retry to reduce restart overhead.

## Objective

Reduce lock contention by detecting transaction abort eligibility before write-set locking
## Applicable Signals

- Read-set tuple's local rts is less than transaction commit timestamp
- Read-set tuple's local wts does not match tuple's latest wts
- Write-set tuple timestamps indicate potential conflict

## Contraindications

- Commit timestamp cannot be accurately approximated before write-set locking
- Tuple timestamps are not reliably accessible or atomic
- Abort rate is already low (optimization provides diminishing returns)
- Transaction has no read set to validate early

## Workflow Steps

- {'step': 1, 'action': "Atomically read TS_word from each tuple in transaction's read set", 'output': 'Extract wts and rts for each read-set tuple'}
- {'step': 2, 'action': 'Determine approximate commit timestamp for the transaction', 'output': 'Commit timestamp estimate (may be conservative)'}
- {'step': 3, 'action': "For each read-set tuple, check if validation will fail: rts < commit_timestamp AND wts ≠ tuple's latest wts", 'output': 'Boolean abort decision'}
- {'step': 4, 'action': 'If abort decision is true, release any held locks and abort transaction immediately', 'output': 'Transaction aborted; no write-set locks acquired'}
- {'step': 5, 'action': 'If abort decision is false, proceed to write-set locking and full validation', 'output': 'Continue to next validation phase step'}
- {'step': 6, 'action': 'On abort, sleep briefly (e.g., 1 µs) before retry', 'output': 'Reduced restart contention'}

## Constraints

- Tuple TS_word must support atomic reads of both wts and rts
- Approximate commit timestamp must be conservative (not overly optimistic)
- Abort decision must be made without holding any locks

## Cautions

- Early abort decision is based on approximate commit timestamp; false negatives are acceptable but false positives (aborting when validation would succeed) must be avoided
- Sleep duration before retry should be tuned to workload; too short increases restart overhead, too long reduces parallelism

## Output Contract

- Transaction abort decision made before write-set lock acquisition. On abort: transaction released without holding locks, sleep period applied, and retry signaled. On continue: transaction proceeds to write-set locking with reduced abort probability. Observable success: reduced lock hold time and contention in validation phase.

## Triggers

- Transaction enters validation phase with read set and write set
- Tuple timestamps (wts, rts) are atomically readable from TS_word
- Transaction's approximate commit timestamp can be determined
