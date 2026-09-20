---
id: "3e22b66d-a038-50aa-8d16-63975d9361be"
name: "Thread-Safe Singleton Client Retrieval"
description: "Retrieve or initialize a singleton client instance using double-checked locking pattern to ensure thread safety and prevent race conditions during concurrent access."
version: "0.1.0"
tags:
  - "concurrency"
  - "singleton"
  - "thread-safety"
  - "lazy-initialization"
  - "double-checked-locking"
triggers:
  - "Multiple threads or async tasks need to access a shared client instance"
  - "Client initialization is expensive or must occur only once"
  - "Concurrent access to a singleton resource is expected"
---

# Thread-Safe Singleton Client Retrieval

Retrieve or initialize a singleton client instance using double-checked locking pattern to ensure thread safety and prevent race conditions during concurrent access.

## Prompt

Implement a thread-safe getter function that returns a singleton Client instance. Use double-checked locking: first check if the instance exists without acquiring a lock; if null, acquire a lock and check again before initializing. Return the initialized instance on all subsequent calls without re-initialization.

## Objective

Obtain thread-safe singleton client instance
## Applicable Signals

- Multi-threaded execution environment detected
- Lazy initialization required for expensive resource
- Shared client instance requested from multiple call sites

## Contraindications

- Client instance is already guaranteed to be initialized
- Single-threaded execution with no concurrency
- Client lifecycle is managed externally or by a framework

## Workflow Steps

- {'step': 1, 'action': 'Check if singleton instance (_client) is None without lock', 'rationale': 'Avoid lock overhead on repeated calls after initialization'}
- {'step': 2, 'action': 'If None, acquire lock (_client_lock)', 'rationale': 'Serialize initialization to prevent multiple threads from creating instances'}
- {'step': 3, 'action': 'Check again if instance is None inside lock', 'rationale': 'Another thread may have initialized while waiting for lock'}
- {'step': 4, 'action': 'If still None, instantiate Client() and assign to _client', 'rationale': 'Create singleton instance exactly once'}
- {'step': 5, 'action': 'Release lock and return _client', 'rationale': 'Ensure lock is released and caller receives initialized instance'}

## Constraints

- Lock object must be initialized before first use
- Global state (_client variable) must be accessible to the function
- Lock acquisition must be reentrant-safe or used only for initialization

## Cautions

- Double-checked locking relies on memory visibility guarantees; ensure language/runtime supports volatile or atomic semantics
- Lock contention during initialization may impact performance under high concurrency
- If Client constructor raises an exception, subsequent calls will retry initialization

## Output Contract

- Returns initialized Client instance. Subsequent calls return the same instance without re-initialization. Caller is guaranteed thread-safe access to a single shared Client object.

## Triggers

- Multiple threads or async tasks need to access a shared client instance
- Client initialization is expensive or must occur only once
- Concurrent access to a singleton resource is expected
