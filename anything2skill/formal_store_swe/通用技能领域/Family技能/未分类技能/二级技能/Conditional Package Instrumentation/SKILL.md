---
id: "c4301c20-1a1c-5e6e-8227-1dde6375d2be"
name: "Conditional Package Instrumentation"
description: "Evaluates whether a package should be instrumented based on eligibility checks and prior state, then loads and instantiates the appropriate instrumentor. Handles special cases such as dependent package instrumentation (e.g., concurrent.futures when mem0 is instrumented)."
version: "0.1.0"
tags:
  - "instrumentation"
  - "package_loading"
  - "import_monitoring"
  - "dynamic_instrumentation"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "Package import is detected via _import_monitor"
  - "Package name is not yet in _instrumenting_packages"
  - "Package is not already marked as instrumented"
---

# Conditional Package Instrumentation

Evaluates whether a package should be instrumented based on eligibility checks and prior state, then loads and instantiates the appropriate instrumentor. Handles special cases such as dependent package instrumentation (e.g., concurrent.futures when mem0 is instrumented).

## Prompt

Check if the package should be instrumented using _should_instrument_package(). If eligible, retrieve its configuration from PROVIDERS or AGENTIC_LIBRARIES, instantiate an InstrumentorLoader, and create the instrumentor instance. Mark the instance with _agentops_instrumented_package_key for tracking. For special cases (e.g., mem0), also instrument dependent packages.

## Objective

Safely instrument a single package by checking eligibility, loading its instrumentor, and registering it for monitoring
## Applicable Signals

- Import event for a target package
- Configuration entry exists in PROVIDERS or AGENTIC_LIBRARIES
- Prior instrumentation state allows new instrumentation

## Contraindications

- Package is already instrumented (_is_package_instrumented returns True)
- _should_instrument_package returns False for the package
- An agentic library is already instrumented (_has_agentic_library is True)

## Workflow Steps

- {'step': 1, 'action': 'Check eligibility', 'detail': 'Call _should_instrument_package(package_name). If False, return early.'}
- {'step': 2, 'action': 'Retrieve configuration', 'detail': 'Look up package_name in PROVIDERS, then AGENTIC_LIBRARIES. If not found, return early.'}
- {'step': 3, 'action': 'Instantiate loader', 'detail': 'Create InstrumentorLoader instance with retrieved configuration.'}
- {'step': 4, 'action': 'Create instrumentor', 'detail': 'Call instrument_one(loader) to instantiate the instrumentor.'}
- {'step': 5, 'action': 'Mark and register', 'detail': 'Set instrumentor_instance._agentops_instrumented_package_key = package_name. Add to _active_instrumentors.'}
- {'step': 6, 'action': 'Handle special cases', 'detail': "If package_name == 'mem0' and is_newly_added, check concurrent.futures availability and instrument it using concurrent_config."}

## Constraints

- Must check _should_instrument_package before proceeding
- Must retrieve configuration from PROVIDERS or AGENTIC_LIBRARIES
- Must instantiate InstrumentorLoader with valid configuration
- Must mark instrumentor instance with _agentops_instrumented_package_key
- Special case: if package_name is 'mem0' and newly added, also instrument concurrent.futures

## Cautions

- Do not instrument if _has_agentic_library is already True; defer to original import
- Verify concurrent.futures module availability before attempting special-case instrumentation
- Handle missing or incomplete configuration gracefully

## Output Contract

- Instrumentor instance is created, stored in _active_instrumentors, and marked with _agentops_instrumented_package_key for future lookup. For special cases, dependent packages are also instrumented. Caller receives confirmation that the package is now instrumented and ready for monitoring.

## 子技能目录
- [Dependent Package Instrumentation Trigger](通用技能领域/Family技能/未分类技能/微技能/Dependent Package Instrumentation Trigger/SKILL.md) ｜ 适用：Automatically instruments dependent packages (e.g., concurrent.futures when mem0 is instrumented) to ensure complete observability of related execution contexts.
- [Resolve and Import Instrumentation Module](通用技能领域/Family技能/未分类技能/微技能/Resolve and Import Instrumentation Module/SKILL.md) ｜ 适用：Dynamically import an instrumentation module by name and return the module object for subsequent class instantiation or method access.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `Dependent Package Instrumentation Trigger` 时，优先调用它。 线索：A package with known dependencies (e.g., mem0) is newly instrumented and the dependent module is available, instrumentation, dependency_handling, observability, concurrent_execution
- 当目标、阶段或方法更接近 `Resolve and Import Instrumentation Module` 时，优先调用它。 线索：When you need to obtain a module object from a stored module name string, Before instantiating a class from that module, importlib, dynamic_import, module_resolution

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Package import is detected via _import_monitor
- Package name is not yet in _instrumenting_packages
- Package is not already marked as instrumented
