---
id: "29316ecf-db6d-5948-a0c4-f62e05e7acc6"
name: "Async-Sync Method Wrapping"
description: "Micro-skill for wrapping both synchronous and asynchronous versions of an API method using wrapt.wrap_function_wrapper, ensuring consistent instrumentation across sync and async call paths."
version: "0.1.0"
tags:
  - "instrumentation"
  - "async"
  - "sync"
  - "function_wrapping"
  - "api_instrumentation"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "API library exposes both sync and async versions of the same method"
  - "Need identical instrumentation logic for both sync and async paths"
  - "Implementing comprehensive API instrumentation"
---

# Async-Sync Method Wrapping

Micro-skill for wrapping both synchronous and asynchronous versions of an API method using wrapt.wrap_function_wrapper, ensuring consistent instrumentation across sync and async call paths.

## Prompt

Use wrapt.wrap_function_wrapper to instrument both sync and async method variants with identical logic. Wrap the target module path and method name, then apply the same callback to both sync and async versions. Ensure metrics and traces are collected identically regardless of call path.

## Objective

Instrument both sync and async method variants with a single reusable wrapping pattern
## Applicable Signals

- Dual method signatures (sync and async) detected in target API
- Instrumentation requirement spans both call paths
- Need for consistent metrics collection across sync/async

## Contraindications

- Only sync or only async methods exist in the API
- Wrapping logic differs significantly between sync and async paths
- Async implementation requires fundamentally different instrumentation approach

## Intervention Moves

- Identify target module and method names for both sync and async variants
- Define unified callback function that handles both paths
- Apply wrapt.wrap_function_wrapper to sync method variant
- Apply wrapt.wrap_function_wrapper to async method variant with same callback
- Verify metrics and traces are collected identically

## Workflow Steps

- {'step': 1, 'action': 'Locate sync and async method variants in target API module', 'detail': 'Identify the fully qualified module path and method names for both versions'}
- {'step': 2, 'action': 'Define unified instrumentation callback', 'detail': 'Create a wrapper function that captures metrics and traces; callback signature must accept (wrapped, instance, args, kwargs)'}
- {'step': 3, 'action': 'Wrap sync method variant', 'detail': "Call wrapt.wrap_function_wrapper(module_path, 'sync_method_name', callback)"}
- {'step': 4, 'action': 'Wrap async method variant', 'detail': "Call wrapt.wrap_function_wrapper(module_path, 'async_method_name', callback) with same callback"}
- {'step': 5, 'action': 'Validate instrumentation', 'detail': 'Execute both sync and async calls; verify metrics and traces are collected identically'}

## Constraints

- Callback must be compatible with both sync and async execution contexts
- wrapt.wrap_function_wrapper must target correct module path and method name
- Both variants must use identical attribute capture and metric collection logic

## Cautions

- Ensure callback does not introduce blocking operations in async context
- Test both sync and async paths independently to verify instrumentation
- Verify that exception handling works correctly for both call types

## Output Contract

- Both sync and async method variants are instrumented and callable; metrics and traces are collected identically for both paths; downstream callers receive consistent observability regardless of sync or async invocation.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- API library exposes both sync and async versions of the same method
- Need identical instrumentation logic for both sync and async paths
- Implementing comprehensive API instrumentation
