---
id: "f95b9e13-ee5f-5c20-a489-bd9ad30d0485"
name: "No-Wait Locking in Validation Phase"
description: "Prevents lock thrashing during transaction validation by immediately aborting validation if a required write-set lock is unavailable, then retrying after a short sleep. Allows concurrent validation of non-conflicting transactions without blocking waits."
version: "0.1.0"
tags:
  - "concurrency_control"
  - "transaction_validation"
  - "lock_management"
  - "performance_optimization"
  - "deadlock_prevention"
triggers:
  - "Validation phase begins for a transaction with a non-empty write set"
  - "Write-intensive workload detected"
  - "High core count system (multi-socket environment)"
examples:
  - input: "Transaction D holds locks on tuples {x, y}; transactions A, B, C waiting for locks held by each other"
    output: "With no-wait: A or B may run in parallel with D instead of sequential validation; when D commits, C acquires lock and progresses"
    notes: "Contrasts with pathological 2PL case where all four transactions validate sequentially"
---

# No-Wait Locking in Validation Phase

Prevents lock thrashing during transaction validation by immediately aborting validation if a required write-set lock is unavailable, then retrying after a short sleep. Allows concurrent validation of non-conflicting transactions without blocking waits.

## Prompt

During the validation phase, attempt to lock tuples in the transaction's write set in primary key order. If a lock cannot be acquired immediately, abort the validation (releasing any locks already held), sleep for a short period (approximately 1 microsecond), and retry the validation phase. This non-waiting approach minimizes blocking and allows more transactions to validate simultaneously.

## Objective

Minimize blocking and contention during multi-transaction validation by eliminating lock waits
## Applicable Signals

- Lock contention observed during write-set locking
- Multiple transactions competing for overlapping tuple locks
- Thrashing behavior detected (transactions holding locks while waiting for others)

## Contraindications

- Read-only transactions (no write set to lock)
- Systems with guaranteed low contention or immediate lock availability
- Workloads where blocking lock acquisition is more efficient than abort-retry cycles

## Intervention Moves

- Attempt to acquire locks on write-set tuples in primary key order
- Upon lock acquisition failure, immediately abort validation and release held locks
- Sleep for a brief period (1 microsecond) to reduce restart frequency
- Retry the validation phase

## Workflow Steps

- Lock write-set tuples in primary key order
- On lock acquisition failure: abort validation and release held locks
- Sleep for approximately 1 microsecond
- Retry validation phase

## Constraints

- Must lock write-set tuples in primary key order to maintain consistency
- Sleep duration should be tuned to workload characteristics; too long increases latency, too short increases restart overhead
- Applicable only within TicToc's validation phase algorithm

## Cautions

- Abort-and-retry approach may increase CPU usage in high-contention scenarios if sleep time is too short
- Performance is sensitive to sleep duration; requires empirical tuning per deployment
- Not suitable for systems where lock wait times are typically very short

## Output Contract

- Validation phase completes without blocking other transactions. Transaction either commits with all write-set locks held, or validation is aborted and retried. Observable success: reduced lock thrashing, lower restart rate compared to blocking lock acquisition, and increased concurrent validation throughput.

## Example Therapist Responses

### Example 1

- Client/Input: Transaction D holds locks on tuples {x, y}; transactions A, B, C waiting for locks held by each other
- Therapist/Output: With no-wait: A or B may run in parallel with D instead of sequential validation; when D commits, C acquires lock and progresses
- Notes: Contrasts with pathological 2PL case where all four transactions validate sequentially

## Triggers

- Validation phase begins for a transaction with a non-empty write set
- Write-intensive workload detected
- High core count system (multi-socket environment)

## Examples

### Example 1

Input:

  Transaction D holds locks on tuples {x, y}; transactions A, B, C waiting for locks held by each other

Output:

  With no-wait: A or B may run in parallel with D instead of sequential validation; when D commits, C acquires lock and progresses

Notes:

  Contrasts with pathological 2PL case where all four transactions validate sequentially
