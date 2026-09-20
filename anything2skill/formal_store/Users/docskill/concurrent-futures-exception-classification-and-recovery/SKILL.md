---
id: "acc58e44-5bef-5e3e-a6cf-bc06657894c8"
name: "Concurrent Futures Exception Classification and Recovery"
description: "Enforces strictly increasing commit timestamps for all transactions writing to the same tuple by acquiring exclusive locks during write phase and atomically updating both write timestamp (wts) and read timestamp (rts) to the transaction's commit timestamp. Guarantees a total order among all writers to the same tuple."
version: "0.1.0"
tags:
  - "write_locking"
  - "timestamp_ordering"
  - "conflict_prevention"
  - "serializability"
  - "concurrency_control"
  - "exclusive_locking"
triggers:
  - "Executor or Future operation raises an exception"
  - "Caller must decide whether to retry, escalate, or abort"
---

# Concurrent Futures Exception Classification and Recovery

Enforces strictly increasing commit timestamps for all transactions writing to the same tuple by acquiring exclusive locks during write phase and atomically updating both write timestamp (wts) and read timestamp (rts) to the transaction's commit timestamp. Guarantees a total order among all writers to the same tuple.

## Prompt

When a transaction enters its write phase for a tuple, acquire an exclusive lock on that tuple. Once locked, read the current wts and rts from the tuple's metadata. Set both the write timestamp (wts) and read timestamp (rts) of the tuple to the transaction's commit timestamp. Release the lock after the write completes. This ensures that any subsequent transaction writing to the same tuple will have a strictly greater commit timestamp, preventing write-write conflicts and maintaining serializability.

## Objective

prevent_write_conflicts
## Applicable Signals

- write operation on tuple detected
- tuple not yet locked by current transaction
- commit timestamp assigned to transaction

## Contraindications

- tuple is already locked by another transaction (must wait or abort)
- read-only transactions (no write phase)
- scenarios where equal commit timestamps across writers are acceptable

## Workflow Steps

- {'step': 1, 'action': 'Acquire exclusive lock on tuple', 'condition': 'tuple not locked by another transaction'}
- {'step': 2, 'action': 'Read current wts and rts from tuple metadata', 'condition': 'lock acquired'}
- {'step': 3, 'action': 'Set tuple.wts = commit_ts', 'condition': 'commit_ts assigned to transaction'}
- {'step': 4, 'action': 'Set tuple.rts = commit_ts', 'condition': 'wts update complete'}
- {'step': 5, 'action': 'Release lock after write completes', 'condition': 'write phase finished'}

## Constraints

- tuple must be locked before write begins
- both wts and rts must be atomically updated to commit_ts
- rts never decreases; only increases or stays equal during write
- only one transaction can write to a tuple at any time due to exclusive locking

## Cautions

- lock contention may reduce parallelism if many transactions write to the same tuple
- deadlock risk if multiple transactions lock tuples in different orders

## Output Contract

- Tuple is locked during write
- Both wts and rts are atomically set to the transaction's commit_ts
- Any subsequent transaction writing to the same tuple will have a strictly greater commit_ts than the current transaction
- A total order is established among all writers to that tuple
- Write-write conflicts are prevented and serializability is maintained

## Triggers

- Executor or Future operation raises an exception
- Caller must decide whether to retry, escalate, or abort
