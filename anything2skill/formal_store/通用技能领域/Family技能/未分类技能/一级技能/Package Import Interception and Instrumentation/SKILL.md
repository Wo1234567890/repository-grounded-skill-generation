---
id: "2142ee5d-6d0f-5077-9736-8fbf5a8844d3"
name: "Package Import Interception and Instrumentation"
description: "Intercepts Python module imports and dynamically instruments matching packages with observability hooks. Replaces the built-in import function to detect and configure instrumentors for agentic libraries and their dependencies without modifying user code."
version: "0.1.0"
tags:
  - "import_hooking"
  - "observability"
  - "instrumentation"
  - "agentic_libraries"
  - "initialization"
  - "dynamic_loading"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "Python application imports an agentic library (e.g., mem0, LangChain, AutoGen)"
  - "Import statement targets a package in PROVIDERS or AGENTIC_LIBRARIES registry"
  - "No agentic library instrumentation is currently active"
---

# Package Import Interception and Instrumentation

Intercepts Python module imports and dynamically instruments matching packages with observability hooks. Replaces the built-in import function to detect and configure instrumentors for agentic libraries and their dependencies without modifying user code.

## Prompt

When a Python application imports a target package, intercept the import, check if the package matches a supported provider or agentic library, instantiate the appropriate instrumentor via InstrumentorLoader, apply instrumentation hooks, and return the instrumented module. Handle cascading dependencies (e.g., if mem0 is instrumented, also instrument concurrent.futures). Track instrumentation state in global _instrumenting_packages and _active_instrumentors. Skip instrumentation if an agentic library is already instrumented or if the package is not in the supported registry.

## Objective

Enable transparent instrumentation of third-party packages at import time without modifying user code.
## Applicable Signals

- Import event for a registered package name
- _has_agentic_library flag is False
- Package not already in _instrumenting_packages or _is_package_instrumented()

## Contraindications

- An agentic library is already instrumented (_has_agentic_library is True)
- User has explicitly disabled instrumentation
- Target package is not in PROVIDERS or AGENTIC_LIBRARIES registry
- InstrumentorLoader instantiation fails due to version mismatch or missing class

## Workflow Steps

- {'step': 1, 'action': 'Check if agentic library is already instrumented', 'detail': 'If _has_agentic_library is True, delegate to original import and return early'}
- {'step': 2, 'action': 'Perform the actual import', 'detail': 'Call _original_builtins_import(name, globals_dict, locals_dict, fromlist, level) to load the module'}
- {'step': 3, 'action': 'Identify packages to instrument', 'detail': 'Check if the imported name or any of its items match entries in PROVIDERS or AGENTIC_LIBRARIES; build packages_to_check set'}
- {'step': 4, 'action': 'Instrument matching packages', 'detail': 'For each package in packages_to_check: if not already instrumented, retrieve config from PROVIDERS or AGENTIC_LIBRARIES, instantiate InstrumentorLoader, call instrument_one(), and store _agentops_instrumented_package_key'}
- {'step': 5, 'action': 'Handle cascading dependencies', 'detail': "If package_name is 'mem0' and newly added, attempt to instrument concurrent.futures using concurrent_config"}
- {'step': 6, 'action': 'Update global state', 'detail': 'Add package to _instrumenting_packages and _active_instrumentors; set _has_agentic_library if an agentic library was instrumented'}
- {'step': 7, 'action': 'Return instrumented module', 'detail': 'Return the module object to the caller with all instrumentation applied'}

## Constraints

- Must preserve original import behavior; return the module to caller after instrumentation
- Global state (_instrumenting_packages, _active_instrumentors, _has_agentic_library) must be thread-safe or protected
- Special case: if mem0 is instrumented, concurrent.futures must also be instrumented if available
- Version checking via InstrumentorLoader.min_version must pass before instantiation

## Cautions

- Replacing the built-in import function is a global hook; ensure no circular dependencies or import loops
- Instrumentor instantiation may fail silently if the target module or class is not found; log failures
- Cascading instrumentation (mem0 → concurrent.futures) may introduce unexpected side effects if concurrent.futures is not available

## Output Contract

- Target package is instrumented with observability hooks
- _instrumenting_packages and _active_instrumentors are updated to reflect the new instrumentor instance
- _agentops_instrumented_package_key is set on the instrumentor
- Module is returned to caller ready for use
- Cascading dependencies (if applicable) are also instrumented

## 子技能目录
- [CommonInstrumentor Configuration and Wrapping](通用技能领域/Family技能/未分类技能/二级技能/CommonInstrumentor Configuration and Wrapping/SKILL.md) ｜ 适用：Configure and instantiate a CommonInstrumentor with InstrumentorConfig and WrapConfig to create reusable instrumentation templates for LLM providers and agentic frameworks.
- [Conditional Package Instrumentation Dispatch](通用技能领域/Family技能/未分类技能/二级技能/Conditional Package Instrumentation Dispatch/SKILL.md) ｜ 适用：Routes a detected package import to the correct instrumentor configuration by consulting the PROVIDERS or AGENTIC_LIBRARIES registry, validates instrumentation eligibility, and instantiates the appropriate InstrumentorLoader with version checking. Handles special-case cascading (e.g., mem0 → concurrent.futures).
- [Decorator-Based Observability Instrumentation](通用技能领域/Family技能/未分类技能/二级技能/Decorator-Based Observability Instrumentation/SKILL.md) ｜ 适用：Apply Python decorators (@workflow, @agent, @operation) to functions and classes to automatically capture execution spans and observability data with minimal code overhead.
- [Entity Decorator Factory Pattern](通用技能领域/Family技能/未分类技能/二级技能/Entity Decorator Factory Pattern/SKILL.md) ｜ 适用：Factory-based system for creating reusable decorators that instrument agent operations (agents, tasks, workflows, tools, guardrails, HTTP endpoints) with semantic span kinds for observability and tracing.
- [Package Instrumentation Initialization](通用技能领域/Family技能/未分类技能/二级技能/Package Instrumentation Initialization/SKILL.md) ｜ 适用：Conditionally start monitoring and instrumenting Python packages using import hooks, with safeguards to prevent redundant or conflicting instrumentation of agentic libraries.

## 选用规则（二级技能目录）
- 当目标、阶段或方法更接近 `CommonInstrumentor Configuration and Wrapping` 时，优先调用它。 线索：Adding support for a new LLM provider (OpenAI, Anthropic, Google GenAI, IBM WatsonX, etc.), Adding support for a new agentic framework (CrewAI, AutoGen, Agno, Mem0, smolagents, etc.), A standardized instrumentation pattern is needed for telemetry collection, instrumentation, opentelemetry
- 当目标、阶段或方法更接近 `Conditional Package Instrumentation Dispatch` 时，优先调用它。 线索：Package name detected in import statement, Import monitor (_import_monitor) intercepts a module load, instrumentation, package_detection, import_monitoring
- 当目标、阶段或方法更接近 `Decorator-Based Observability Instrumentation` 时，优先调用它。 线索：Developer needs to add observability to a workflow function, Agent class requires execution span capture, Operation method needs automatic instrumentation, observability, instrumentation
- 当目标、阶段或方法更接近 `Entity Decorator Factory Pattern` 时，优先调用它。 线索：Initializing agent framework; need to instrument multiple entity types (agent, task, workflow, tool, guardrail, HTTP) with consistent span semantics, observability, instrumentation, decorator, factory_pattern
- 当目标、阶段或方法更接近 `Package Instrumentation Initialization` 时，优先调用它。 线索：AgentOps monitoring is first activated, No active instrumentors are currently running (_active_instrumentors is empty), Agentic library detection is needed to avoid double-instrumentation, instrumentation, initialization

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Python application imports an agentic library (e.g., mem0, LangChain, AutoGen)
- Import statement targets a package in PROVIDERS or AGENTIC_LIBRARIES registry
- No agentic library instrumentation is currently active
