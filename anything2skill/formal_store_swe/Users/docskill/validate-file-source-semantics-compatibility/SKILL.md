---
id: "648c7587-0e39-525a-93e8-5962fdace0d7"
name: "Validate File Source Semantics Compatibility"
description: "Validates that transactions writing to the same tuple maintain strictly increasing commit timestamps by enforcing tuple locking and read-timestamp monotonicity. Serves as a safety invariant in optimistic concurrency control to prevent write-write conflicts and ensure serializable execution."
version: "0.1.1"
tags:
  - "timestamp_ordering"
  - "write_write_conflict"
  - "optimistic_concurrency_control"
  - "tuple_locking"
  - "invariant_verification"
  - "serialization"
triggers:
  - "File-based source is configured with watchType=PROCESS_CONTINUOUSLY"
  - "Application requires exactly-once delivery guarantee"
examples:
  - input: "Transaction T1 writes tuple X with commit_ts=100; tuple X now has wts=100, rts=100. Transaction T2 later attempts to write tuple X."
    output: "T2's commit_ts must be > 100 (e.g., 101 or higher). If T2's commit_ts ≤ 100, the write is rejected to maintain timestamp monotonicity."
    notes: "Tuple locking ensures T1 and T2 do not write concurrently; timestamp check ensures serial order."
  - input: "Tuple Y has wts=50, rts=50. Transaction T3 with commit_ts=50 attempts to write tuple Y."
    output: "Write is rejected because commit_ts(T3) is not strictly greater than rts(Y). T3 must abort or retry with a higher timestamp."
    notes: "Equality is not allowed; strict inequality is required to maintain total order."
---

# Validate File Source Semantics Compatibility

Validates that transactions writing to the same tuple maintain strictly increasing commit timestamps by enforcing tuple locking and read-timestamp monotonicity. Serves as a safety invariant in optimistic concurrency control to prevent write-write conflicts and ensure serializable execution.

## Prompt

When a transaction enters the write phase for a tuple, verify: (1) the tuple is locked (only one writer at a time), (2) the tuple's read-timestamp (rts) never decreases, and (3) any subsequent transaction writing to the same tuple has a commit timestamp strictly greater than the current tuple's rts. If all conditions hold, the write-write conflict invariant is maintained and the write may proceed.

## Objective

Guarantee write-write conflict prevention through timestamp ordering and tuple locking
## Applicable Signals

- Multiple transactions in flight targeting the same tuple
- Write-phase entry for a tuple with existing write-timestamp (wts)
- Transaction attempting to write to a tuple previously written by another transaction

## Contraindications

- Tuple locking is disabled or not enforced during write phase
- Read-timestamp can decrease (violates monotonicity assumption)
- Pessimistic write locks are not held during write phase
- Global timestamp coordination is used instead of per-tuple timestamps

## Workflow Steps

- {'step': 1, 'action': 'Check tuple lock status', 'detail': 'Verify that the tuple is locked and only one transaction holds the write lock'}
- {'step': 2, 'action': 'Retrieve current tuple timestamps', 'detail': "Read the tuple's current write-timestamp (wts) and read-timestamp (rts)"}
- {'step': 3, 'action': 'Verify rts monotonicity', 'detail': 'Confirm that rts has not decreased since the last write to this tuple'}
- {'step': 4, 'action': 'Compare commit timestamps', 'detail': "Ensure the current transaction's commit_ts is strictly greater than the tuple's current rts"}
- {'step': 5, 'action': 'Update tuple timestamps', 'detail': "If all checks pass, set both wts and rts of the modified tuple to the transaction's commit_ts"}

## Constraints

- Tuple must be locked while being written (only one transaction can hold write lock at a time)
- Read-timestamp of a tuple must never decrease across transactions
- Commit timestamp of a later-writing transaction must be strictly greater than the earlier transaction's commit timestamp

## Cautions

- This invariant assumes optimistic concurrency control with per-tuple timestamp tracking
- Requires that tuple locking is correctly implemented and enforced
- Does not apply if global timestamp coordination is used instead of derived timestamps

## Output Contract

- Invariant verified: if transaction A writes tuple at logical time t1 and transaction B writes the same tuple at logical time t2 > t1, then commit_ts(B) > commit_ts(A). Write-write conflict is prevented.
- If verification fails, transaction aborts and must retry with a higher timestamp

## Example Executions

### Example 1

- Input: Transaction T1 writes tuple X with commit_ts=100; tuple X now has wts=100, rts=100. Transaction T2 later attempts to write tuple X.
- Output: T2's commit_ts must be > 100 (e.g., 101 or higher). If T2's commit_ts ≤ 100, the write is rejected to maintain timestamp monotonicity.
- Notes: Tuple locking ensures T1 and T2 do not write concurrently; timestamp check ensures serial order.

### Example 2

- Input: Tuple Y has wts=50, rts=50. Transaction T3 with commit_ts=50 attempts to write tuple Y.
- Output: Write is rejected because commit_ts(T3) is not strictly greater than rts(Y). T3 must abort or retry with a higher timestamp.
- Notes: Equality is not allowed; strict inequality is required to maintain total order.

## Triggers

- File-based source is configured with watchType=PROCESS_CONTINUOUSLY
- Application requires exactly-once delivery guarantee

## Examples

### Example 1

Input:

  Transaction T1 writes tuple X with commit_ts=100; tuple X now has wts=100, rts=100. Transaction T2 later attempts to write tuple X.

Output:

  T2's commit_ts must be > 100 (e.g., 101 or higher). If T2's commit_ts ≤ 100, the write is rejected to maintain timestamp monotonicity.

Notes:

  Tuple locking ensures T1 and T2 do not write concurrently; timestamp check ensures serial order.

### Example 2

Input:

  Tuple Y has wts=50, rts=50. Transaction T3 with commit_ts=50 attempts to write tuple Y.

Output:

  Write is rejected because commit_ts(T3) is not strictly greater than rts(Y). T3 must abort or retry with a higher timestamp.

Notes:

  Equality is not allowed; strict inequality is required to maintain total order.
