---
id: "289afdbb-dcb2-5d9f-bb8d-c989b9727366"
name: "Read-Set Validation with Timestamp Overflow Handling"
description: "Validates read-set entries against write-set conflicts and extends read timestamps with delta overflow correction using compare-and-swap atomicity during optimistic concurrency control commit phase."
version: "0.1.0"
tags:
  - "optimistic_concurrency_control"
  - "timestamp_validation"
  - "atomic_operation"
  - "overflow_handling"
  - "commit_phase"
triggers:
  - "Transaction enters commit validation phase"
  - "Read-set entry must be checked against current tuple state"
  - "Tuple timestamp word requires extension due to delta accumulation"
examples:
  - input: "read-set entry r with r.wts=100, tuple with v1.wts=100, v1.rts=50, commit_ts=120, tuple not locked, not in write-set"
    output: "delta=20, shift=0, v2.wts=100, v2.delta=20, compare-and-swap succeeds, validation passes"
    notes: "No overflow; delta fits in 15-bit field"
  - input: "read-set entry r with r.wts=100, tuple with v1.wts=100, v1.rts=120, commit_ts=120, tuple not locked"
    output: "v1.rts ≤ commit_ts is false, skip delta handling, validation passes without timestamp update"
    notes: "Read timestamp already at or beyond commit timestamp; no extension needed"
  - input: "read-set entry r with r.wts=100, tuple with v1.wts=105, v1.rts=50, commit_ts=120"
    output: "r.wts ≠ v1.wts (100 ≠ 105), Abort()"
    notes: "Write timestamp mismatch indicates tuple was modified by another transaction"
---

# Read-Set Validation with Timestamp Overflow Handling

Validates read-set entries against write-set conflicts and extends read timestamps with delta overflow correction using compare-and-swap atomicity during optimistic concurrency control commit phase.

## Prompt

For each read-set entry, check if the tuple's write timestamp matches the entry's recorded write timestamp, or if the tuple is locked and not in the write-set (abort condition). If the read timestamp is less than or equal to the commit timestamp, compute the delta between commit timestamp and write timestamp, extract the overflow portion, update the write timestamp with the shifted delta, and atomically swap the timestamp word using compare-and-swap. Retry the loop until the swap succeeds.

## Objective

Atomically validate and update tuple read timestamps without conflicts
## Applicable Signals

- commit_ts provided and read_ts_word accessible
- read-set entry r with tuple reference and recorded write timestamp r.wts
- write-set W available for membership check

## Contraindications

- Tuple is locked by another transaction AND entry is not in write-set (abort immediately)
- Write timestamp mismatch detected (r.wts ≠ v1.wts) (abort immediately)
- Pessimistic locking is active on the tuple

## Workflow Steps

- {'step': 1, 'action': 'Read tuple timestamp word (v1 = v2 = r.tuple.read_ts_word())'}
- {'step': 2, 'action': 'Check abort conditions: if r.wts ≠ v1.wts OR (v1.rts ≤ commit_ts AND tuple is locked AND r.tuple not in W), then Abort()'}
- {'step': 3, 'action': 'If v1.rts ≤ commit_ts, compute delta = commit_ts − v1.wts'}
- {'step': 4, 'action': 'Extract overflow: shift = delta − (delta AND 0x7fff)'}
- {'step': 5, 'action': 'Update v2: v2.wts = v2.wts + shift; v2.delta = delta − shift'}
- {'step': 6, 'action': 'Atomically swap: success = compare_and_swap(r.tuple.ts_word, v1, v2)'}
- {'step': 7, 'action': 'If success is false, retry from step 1; if true, validation complete'}

## Constraints

- Timestamp word must support atomic compare-and-swap operation
- Delta overflow correction requires bit-masking with 0x7fff boundary
- Loop must retry until compare-and-swap succeeds (no early exit on contention)

## Cautions

- If validation aborts, transaction must roll back all changes
- Timestamp overflow handling assumes fixed bit-width representation (15-bit delta field)
- Physical time ordering is used only when commit timestamps are equal; this validation does not enforce physical time ordering

## Output Contract

- Validation succeeds with read timestamp extended and timestamp word atomically updated, or validation aborts with transaction rollback. Compare-and-swap loop guarantees eventual success or explicit abort signal.

## Example Executions

### Example 1

- Input: read-set entry r with r.wts=100, tuple with v1.wts=100, v1.rts=50, commit_ts=120, tuple not locked, not in write-set
- Output: delta=20, shift=0, v2.wts=100, v2.delta=20, compare-and-swap succeeds, validation passes
- Notes: No overflow; delta fits in 15-bit field

### Example 2

- Input: read-set entry r with r.wts=100, tuple with v1.wts=100, v1.rts=120, commit_ts=120, tuple not locked
- Output: v1.rts ≤ commit_ts is false, skip delta handling, validation passes without timestamp update
- Notes: Read timestamp already at or beyond commit timestamp; no extension needed

### Example 3

- Input: read-set entry r with r.wts=100, tuple with v1.wts=105, v1.rts=50, commit_ts=120
- Output: r.wts ≠ v1.wts (100 ≠ 105), Abort()
- Notes: Write timestamp mismatch indicates tuple was modified by another transaction

## Triggers

- Transaction enters commit validation phase
- Read-set entry must be checked against current tuple state
- Tuple timestamp word requires extension due to delta accumulation

## Examples

### Example 1

Input:

  read-set entry r with r.wts=100, tuple with v1.wts=100, v1.rts=50, commit_ts=120, tuple not locked, not in write-set

Output:

  delta=20, shift=0, v2.wts=100, v2.delta=20, compare-and-swap succeeds, validation passes

Notes:

  No overflow; delta fits in 15-bit field

### Example 2

Input:

  read-set entry r with r.wts=100, tuple with v1.wts=100, v1.rts=120, commit_ts=120, tuple not locked

Output:

  v1.rts ≤ commit_ts is false, skip delta handling, validation passes without timestamp update

Notes:

  Read timestamp already at or beyond commit timestamp; no extension needed

### Example 3

Input:

  read-set entry r with r.wts=100, tuple with v1.wts=105, v1.rts=50, commit_ts=120

Output:

  r.wts ≠ v1.wts (100 ≠ 105), Abort()

Notes:

  Write timestamp mismatch indicates tuple was modified by another transaction
