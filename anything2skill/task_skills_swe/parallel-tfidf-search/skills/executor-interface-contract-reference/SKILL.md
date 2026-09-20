---
id: "f2ac4e58-3aff-5b2a-86fd-d4143a55e639"
name: "Executor Interface Contract Reference"
description: "Canonical knowledge reference for the abstract Executor class interface. Defines the common contract (submit, map, shutdown methods) shared by ThreadPoolExecutor and ProcessPoolExecutor. Use when designing executor-agnostic code that accepts any Executor subclass."
version: "0.1.0"
tags:
  - "concurrent.futures"
  - "executor"
  - "interface"
  - "abstraction"
  - "async"
  - "threading"
triggers:
  - "Designing code that accepts any Executor subclass; need to understand common method signatures and behavior contracts."
---

# Executor Interface Contract Reference

Canonical knowledge reference for the abstract Executor class interface. Defines the common contract (submit, map, shutdown methods) shared by ThreadPoolExecutor and ProcessPoolExecutor. Use when designing executor-agnostic code that accepts any Executor subclass.

## Prompt

The Executor class is an abstract base that defines three core methods: submit(fn, *args, **kwargs) schedules a callable and returns a Future; map(fn, *iterables, timeout=None, chunksize=1) applies a function to iterables asynchronously with optional timeout; shutdown(wait=True, cancel_futures=False) frees resources and prevents new submissions. All concrete executors (ThreadPoolExecutor, ProcessPoolExecutor) implement this interface identically.

## Objective

Provide interface contract and method signatures for executor implementations
## Applicable Signals

- Designing code that accepts any Executor subclass
- Need to understand common method signatures and behavior contracts
- Writing executor-agnostic abstractions

## Contraindications

- Implementing executor directly (use concrete ThreadPoolExecutor or ProcessPoolExecutor instead)
- Need platform-specific behavior details (refer to concrete implementation docs)
- Instantiating Executor directly (it is abstract)

## Constraints

- Executor is abstract and must not be used directly
- Both ThreadPoolExecutor and ProcessPoolExecutor implement the same interface
- Not available on WebAssembly platforms (wasm32-emscripten, wasm32-wasi)

## Output Contract

- Caller gains understanding of the Executor abstract interface, method contracts (submit, map, shutdown), and is able to write executor-agnostic code that works with any concrete executor implementation.

## Triggers

- Designing code that accepts any Executor subclass; need to understand common method signatures and behavior contracts.
