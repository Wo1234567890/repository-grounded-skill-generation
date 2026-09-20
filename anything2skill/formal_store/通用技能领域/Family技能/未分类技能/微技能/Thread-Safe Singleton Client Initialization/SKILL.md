---
id: "7655f671-96be-54c9-b5e0-5f633cc55350"
name: "Thread-Safe Singleton Client Initialization"
description: "Implements double-checked locking pattern to safely instantiate and return a singleton Client instance across multiple threads without race conditions."
version: "0.1.0"
tags:
  - "concurrency"
  - "singleton"
  - "thread-safety"
  - "double-checked-locking"
  - "initialization"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Application requires a single shared Client instance"
  - "Multiple concurrent threads or async contexts need access to the same client"
  - "Lazy initialization is preferred (create on first use)"
---

# Thread-Safe Singleton Client Initialization

Implements double-checked locking pattern to safely instantiate and return a singleton Client instance across multiple threads without race conditions.

## Prompt

Use this pattern when you need to initialize a shared resource (Client instance) that must be created exactly once and safely accessed from multiple concurrent threads. The pattern checks if the instance exists (first check without lock), acquires a lock only if needed, then checks again inside the lock (second check) before creating the instance. This minimizes lock contention while guaranteeing thread safety.

## Objective

Ensure thread-safe lazy initialization of a shared client resource
## Applicable Signals

- Multi-threaded or async application architecture
- Need for singleton pattern with thread safety
- Resource creation is expensive and should happen once

## Contraindications

- Client instances must be isolated per thread
- Thread safety is not a requirement
- Eager initialization is mandated by design

## Workflow Steps

- {'step': 1, 'action': 'Check if singleton instance is None (first check without lock)', 'rationale': 'Avoid lock acquisition on every call after initialization'}
- {'step': 2, 'action': 'Acquire lock if instance is None', 'rationale': 'Serialize access during initialization'}
- {'step': 3, 'action': 'Check again if instance is None inside lock (second check)', 'rationale': 'Prevent race condition where multiple threads passed first check before lock was acquired'}
- {'step': 4, 'action': 'Create Client instance if still None', 'rationale': 'Initialize exactly once'}
- {'step': 5, 'action': 'Return the singleton instance', 'rationale': 'Provide caller with consistent reference'}

## Constraints

- A module-level lock object must be available (e.g., _client_lock)
- A module-level variable must hold the singleton reference (e.g., _client)
- The Client class must be instantiable without required arguments or with defaults

## Cautions

- Ensure the lock object is created before any thread accesses get_client()
- Do not modify the global _client reference outside this function
- If Client initialization has side effects, they will occur on first call only

## Output Contract

- Returns a single Client instance that is guaranteed to be the same across all callers; no duplicate instances are created; no race conditions occur during initialization

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Application requires a single shared Client instance
- Multiple concurrent threads or async contexts need access to the same client
- Lazy initialization is preferred (create on first use)
