---
id: "94e67c82-e0ad-51fa-9954-33586fd4a1ca"
name: "Read-Set Validation with Timestamp Overflow Handling"
description: "Validates read-set entries against write-set and commit timestamp, extending read timestamps with delta overflow correction to prevent stale reads in optimistic concurrency control."
version: "0.1.0"
tags:
  - "optimistic_concurrency_control"
  - "timestamp_validation"
  - "overflow_handling"
  - "read_consistency"
  - "atomic_operation"
triggers:
  - "transaction enters read-set validation during commit phase"
  - "read tuple timestamp word must be checked against write-set membership"
  - "commit timestamp bounds require validation"
examples:
  - input: "read-set entry r with r.tuple.read_ts_word() = {wts: 100, rts: 105}, commit_ts = 120, r.tuple not in write-set"
    output: "delta = 20, shift = 4, v2.wts = 104, v2.delta = 16; compare_and_swap succeeds"
    notes: "Overflow correction applied; read timestamp extended to accommodate commit timestamp."
  - input: "read-set entry r with r.wts ≠ v1.wts"
    output: "Abort() called"
    notes: "Write timestamp mismatch indicates conflict; transaction aborted."
---

# Read-Set Validation with Timestamp Overflow Handling

Validates read-set entries against write-set and commit timestamp, extending read timestamps with delta overflow correction to prevent stale reads in optimistic concurrency control.

## Prompt

For each read-set entry r with write-set W and commit_ts:
1. Read the tuple's timestamp word (v1 = v2 = r.tuple.read_ts_word()).
2. Check if write timestamp (wts) matches or if tuple is locked and not in write-set; abort if violated.
3. If read timestamp (rts) ≤ commit_ts, compute delta overflow: delta = commit_ts − v1.wts, shift = delta − (delta ∧ 0x7fff).
4. Update v2.wts += shift and v2.delta = delta − shift.
5. Atomically swap the timestamp word; retry on failure until success.

## Objective

validate_read_consistency
## Applicable Signals

- read-set entry r with associated tuple and timestamp word
- write-set W membership status
- commit_ts value derived from accessed tuples

## Contraindications

- do not invoke during write phase
- do not invoke if read-set is empty
- do not invoke if tuple is not locked during write

## Workflow Steps

- {'step': 1, 'action': 'Read tuple timestamp word', 'detail': 'v2 = v1 = r.tuple.read_ts_word()'}
- {'step': 2, 'action': 'Validate write timestamp and lock status', 'detail': 'If r.wts ≠ v1.wts or (v1.rts ≤ commit_ts and isLocked(r.tuple)) and r.tuple not in W, abort transaction'}
- {'step': 3, 'action': 'Extend read timestamp if needed', 'detail': 'If v1.rts ≤ commit_ts, compute delta = commit_ts − v1.wts'}
- {'step': 4, 'action': 'Handle delta overflow', 'detail': 'shift = delta − (delta ∧ 0x7fff); v2.wts += shift; v2.delta = delta − shift'}
- {'step': 5, 'action': 'Atomic timestamp word update', 'detail': 'success = compare_and_swap(r.tuple.ts_word, v1, v2); retry if not success'}

## Constraints

- tuple must be locked while being written
- read timestamp (rts) never decreases in the algorithm
- compare_and_swap must succeed atomically; retry on failure

## Cautions

- delta overflow correction requires bitwise masking (0x7fff) to prevent timestamp wraparound
- concurrent modifications to timestamp word may cause retry loop; ensure bounded retry count

## Output Contract

- Read timestamp extended with overflow correction applied, or validation aborted; compare_and_swap succeeds and retry loop completes with success = true.

## Example Therapist Responses

### Example 1

- Client/Input: read-set entry r with r.tuple.read_ts_word() = {wts: 100, rts: 105}, commit_ts = 120, r.tuple not in write-set
- Therapist/Output: delta = 20, shift = 4, v2.wts = 104, v2.delta = 16; compare_and_swap succeeds
- Notes: Overflow correction applied; read timestamp extended to accommodate commit timestamp.

### Example 2

- Client/Input: read-set entry r with r.wts ≠ v1.wts
- Therapist/Output: Abort() called
- Notes: Write timestamp mismatch indicates conflict; transaction aborted.

## Triggers

- transaction enters read-set validation during commit phase
- read tuple timestamp word must be checked against write-set membership
- commit timestamp bounds require validation

## Examples

### Example 1

Input:

  read-set entry r with r.tuple.read_ts_word() = {wts: 100, rts: 105}, commit_ts = 120, r.tuple not in write-set

Output:

  delta = 20, shift = 4, v2.wts = 104, v2.delta = 16; compare_and_swap succeeds

Notes:

  Overflow correction applied; read timestamp extended to accommodate commit timestamp.

### Example 2

Input:

  read-set entry r with r.wts ≠ v1.wts

Output:

  Abort() called

Notes:

  Write timestamp mismatch indicates conflict; transaction aborted.
