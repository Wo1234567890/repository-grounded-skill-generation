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

## Triggers

- Python application imports an agentic library (e.g., mem0, LangChain, AutoGen)
- Import statement targets a package in PROVIDERS or AGENTIC_LIBRARIES registry
- No agentic library instrumentation is currently active
