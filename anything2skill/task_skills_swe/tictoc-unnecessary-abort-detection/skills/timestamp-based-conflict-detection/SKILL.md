---
id: "184110eb-6257-5f22-9325-b3b7daa3ae7f"
name: "Timestamp-Based Conflict Detection"
description: "Verify that read-write or write-read conflicting transactions commit at different logical or physical timestamps by comparing tuple read timestamps (rts) and write timestamps (wts) against transaction commit timestamps. Ensures serializability by confirming distinct commit ordering for conflicting transaction pairs."
version: "0.1.0"
tags:
  - "timestamp_ordering"
  - "conflict_detection"
  - "serializability"
  - "transaction_validation"
  - "concurrency_control"
  - "read-write_conflict"
triggers:
  - "Transaction pair identified with read-write conflict on same tuple"
  - "Transaction pair identified with write-read conflict on same tuple"
  - "Serializability verification required during validation phase"
---

# Timestamp-Based Conflict Detection

Verify that read-write or write-read conflicting transactions commit at different logical or physical timestamps by comparing tuple read timestamps (rts) and write timestamps (wts) against transaction commit timestamps. Ensures serializability by confirming distinct commit ordering for conflicting transaction pairs.

## Prompt

For a pair of transactions with read-write or write-read conflicts on the same tuple:
1. Retrieve the tuple's current rts (read timestamp) and wts (write timestamp) by atomically reading the tuple's TS_word.
2. Obtain the commit timestamp of the reading transaction and the writing transaction.
3. Verify that the reading transaction's commit timestamp is ≤ tuple's current rts.
4. Verify that the writing transaction's commit timestamp is > tuple's current rts.
5. If both conditions hold, the transactions have different commit timestamps and conflict is resolved; otherwise, flag a serializability violation and abort/retry the transaction.

## Objective

Detect and enforce timestamp ordering for conflicting transaction pairs to guarantee serializability
## Applicable Signals

- Tuple has both rts and wts available
- Transaction commit timestamps are determinable
- Conflicting tuple access detected in read and write sets
- Read-write or write-read conflict identified on same tuple

## Contraindications

- Transactions have no overlapping tuple access
- Both transactions are read-only (no write-read or read-write conflict)
- Tuple timestamps are unavailable or stale
- Write set is not yet locked during validation

## Workflow Steps

- {'step': 1, 'action': 'Identify conflicting transaction pair and tuple', 'input': 'Two transactions with overlapping tuple access (one reads, one writes)'}
- {'step': 2, 'action': "Atomically read tuple's TS_word containing rts and wts", 'input': 'Tuple reference'}
- {'step': 3, 'action': "Obtain reading transaction's commit timestamp", 'input': 'Reading transaction context'}
- {'step': 4, 'action': "Obtain writing transaction's commit timestamp", 'input': 'Writing transaction context'}
- {'step': 5, 'action': 'Compare reading transaction timestamp against tuple rts', 'condition': 'reading_ts ≤ tuple.rts'}
- {'step': 6, 'action': 'Compare writing transaction timestamp against tuple rts', 'condition': 'writing_ts > tuple.rts'}
- {'step': 7, 'action': 'Return conflict resolution status', 'output': 'Boolean: true if both conditions hold (conflict resolved), false otherwise'}

## Constraints

- Tuple wts must be updated atomically with tuple value
- Reading transaction commit timestamp must be determined after write set is locked to ensure accuracy
- Comparison must use consistent snapshot of tuple timestamps
- Write set must be locked before reading transaction's commit timestamp is finalized

## Cautions

- Do not compare timestamps before write set is locked; rts may change during validation
- Ensure tuple timestamps reflect latest committed state, not in-flight writes
- Tuple's rts in write set might be changed by different transactions; obtain approximate commit timestamp only after write set locking

## Output Contract

- Boolean confirmation that conflicting transactions have distinct commit timestamps. Success: reading transaction timestamp ≤ tuple rts AND writing transaction timestamp > tuple rts. Failure: either condition violated, indicating serializability violation or need for transaction abort/retry. On success, transactions are ordered in serial schedule with reading transaction after writing transaction.

## Triggers

- Transaction pair identified with read-write conflict on same tuple
- Transaction pair identified with write-read conflict on same tuple
- Serializability verification required during validation phase
