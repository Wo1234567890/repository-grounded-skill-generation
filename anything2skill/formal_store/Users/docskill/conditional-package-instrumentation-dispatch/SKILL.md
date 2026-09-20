---
id: "f8ac0674-da50-5e4a-90a1-794b56c8a3ab"
name: "Conditional Package Instrumentation Dispatch"
description: "Routes a detected package import to the correct instrumentor configuration by consulting the PROVIDERS or AGENTIC_LIBRARIES registry, validates instrumentation eligibility, and instantiates the appropriate InstrumentorLoader with version checking. Handles special-case cascading (e.g., mem0 → concurrent.futures)."
version: "0.1.0"
tags:
  - "instrumentation"
  - "package_detection"
  - "import_monitoring"
  - "observability"
  - "configuration_routing"
triggers:
  - "Package name detected in import statement"
  - "Import monitor (_import_monitor) intercepts a module load"
---

# Conditional Package Instrumentation Dispatch

Routes a detected package import to the correct instrumentor configuration by consulting the PROVIDERS or AGENTIC_LIBRARIES registry, validates instrumentation eligibility, and instantiates the appropriate InstrumentorLoader with version checking. Handles special-case cascading (e.g., mem0 → concurrent.futures).

## Prompt

When a package name is detected during import monitoring, check if it should be instrumented by verifying it is not already instrumented and exists in the registry. Retrieve the configuration from PROVIDERS or AGENTIC_LIBRARIES, instantiate an InstrumentorLoader with that config, create the instrumentor instance, and store the package key on the instance for tracking. If the package is mem0 and newly added, also instrument concurrent.futures using the same pattern.

## Objective

Route a detected package import to the correct instrumentor configuration and instantiate it with version validation.
## Applicable Signals

- Package name matches entry in PROVIDERS registry
- Package name matches entry in AGENTIC_LIBRARIES registry
- Package is not yet in _instrumenting_packages
- Package is not already instrumented (_is_package_instrumented returns False)

## Contraindications

- Package is already instrumented (_is_package_instrumented returns True)
- Package is not in PROVIDERS or AGENTIC_LIBRARIES registry
- _should_instrument_package returns False for the package
- An agentic library is already instrumented (_has_agentic_library is True)

## Workflow Steps

- {'step': 1, 'action': 'Check if package should be instrumented', 'detail': 'Call _should_instrument_package(package_name); if False, return early'}
- {'step': 2, 'action': 'Retrieve instrumentor configuration', 'detail': 'Look up config = PROVIDERS.get(package_name) or AGENTIC_LIBRARIES.get(package_name); if config is None, return early'}
- {'step': 3, 'action': 'Instantiate InstrumentorLoader', 'detail': 'Create loader = InstrumentorLoader(**config) with the retrieved configuration'}
- {'step': 4, 'action': 'Create instrumentor instance', 'detail': 'Call instrument_one(loader) to instantiate the instrumentor'}
- {'step': 5, 'action': 'Store package tracking key', 'detail': 'Set instrumentor_instance._agentops_instrumented_package_key = package_name'}
- {'step': 6, 'action': 'Handle special case for mem0', 'detail': "If package_name == 'mem0' and is_newly_added, retrieve concurrent_config, create concurrent_loader = InstrumentorLoader(**concurrent_config), and call instrument_one(concurrent_loader)"}

## Constraints

- Must check _is_package_instrumented before attempting instrumentation
- Must retrieve config from PROVIDERS or AGENTIC_LIBRARIES; if neither exists, skip instrumentation
- InstrumentorLoader must be instantiated with the retrieved config
- The instrumentor_instance._agentops_instrumented_package_key must be set to the package_name for tracking
- Special case: if package_name is 'mem0' and is_newly_added, also instrument concurrent.futures with its own InstrumentorLoader

## Cautions

- Do not attempt instrumentation if _has_agentic_library is already True; defer to the original import function instead.
- Ensure version checking is performed by InstrumentorLoader during instantiation (min_version validation).
- The special case for mem0 should only trigger if is_newly_added is True to avoid redundant instrumentation.

## Output Contract

- InstrumentorLoader is successfully instantiated with correct config
- instrumentor_instance is created and stored in _active_instrumentors
- _agentops_instrumented_package_key is set on the instance for future tracking
- If mem0 is instrumented, concurrent.futures is also instrumented with its own InstrumentorLoader

## Triggers

- Package name detected in import statement
- Import monitor (_import_monitor) intercepts a module load
