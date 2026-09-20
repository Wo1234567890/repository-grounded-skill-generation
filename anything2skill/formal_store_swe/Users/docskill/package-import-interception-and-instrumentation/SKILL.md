---
id: "5cb1141a-bd9a-5686-a22e-969b744a44a8"
name: "Package Import Interception and Instrumentation"
description: "Intercepts Python module imports at runtime and dynamically instruments matching packages with observability hooks. Replaces the built-in import function to detect packages against configured registries (PROVIDERS, AGENTIC_LIBRARIES) and instantiate instrumentors transparently, enabling monitoring of external package calls without modifying user code."
version: "0.1.0"
tags:
  - "import_interception"
  - "instrumentation"
  - "observability"
  - "runtime_initialization"
  - "package_monitoring"
  - "agent_ops"
triggers:
  - "AgentOps runtime initialization begins"
  - "User code imports a monitored package (e.g., LLM client, memory system, concurrent execution library)"
examples:
  - input: "User code: import openai"
    output: "openai module is loaded, InstrumentorLoader for openai is instantiated with config from PROVIDERS, instrumentor is registered in _active_instrumentors, openai module is returned to user code. Subsequent openai.ChatCompletion.create() calls are now monitored."
    notes: "Standard case: package name matches PROVIDERS registry exactly."
  - input: "User code: from google.adk import something"
    output: "google module is imported, full_item_name_candidate 'google.adk' is checked against registries, InstrumentorLoader for google.adk is instantiated if found, instrumentor is registered, module is returned. Subsequent google.adk calls are monitored."
    notes: "Nested package case: fromlist item is combined with parent name to form full candidate."
  - input: "User code: import mem0; then import concurrent.futures"
    output: "mem0 is instrumented and registered. Because package_name == 'mem0' and is_newly_added, concurrent.futures is also instrumented with concurrent_config. Both instrumentors are active."
    notes: "Special case: mem0 triggers automatic instrumentation of concurrent.futures dependency."
---

# Package Import Interception and Instrumentation

Intercepts Python module imports at runtime and dynamically instruments matching packages with observability hooks. Replaces the built-in import function to detect packages against configured registries (PROVIDERS, AGENTIC_LIBRARIES) and instantiate instrumentors transparently, enabling monitoring of external package calls without modifying user code.

## Prompt

When AgentOps runtime initializes, install an import monitor that intercepts all module imports. For each import, check if the package matches a configured instrumentor target. If matched and not already instrumented, instantiate the appropriate instrumentor and register it. Handle special cases (e.g., concurrent.futures when mem0 is instrumented). Skip instrumentation if an agentic library is already active to prevent double-instrumentation.

## Objective

Transparently instrument third-party packages at import time without modifying user code
## Applicable Signals

- Runtime startup signal
- Module import event intercepted by custom import hook
- Package name matches configured PROVIDERS or AGENTIC_LIBRARIES registry

## Contraindications

- User explicitly disables instrumentation via configuration
- An agentic library is already instrumented (flag _has_agentic_library is True)
- Package is already in _instrumenting_packages or marked as instrumented

## Workflow Steps

- {'step': 1, 'action': 'Install custom import monitor', 'detail': 'Replace built-in __import__ with _import_monitor function to intercept all module imports'}
- {'step': 2, 'action': 'Check agentic library flag', 'detail': 'If _has_agentic_library is True, delegate to original import and skip instrumentation'}
- {'step': 3, 'action': 'Perform actual import', 'detail': 'Call _original_builtins_import to load the module normally'}
- {'step': 4, 'action': 'Identify matching packages', 'detail': 'Check imported name and fromlist items against PROVIDERS and AGENTIC_LIBRARIES registries; build set of packages_to_check'}
- {'step': 5, 'action': 'Instrument matching packages', 'detail': 'For each package in packages_to_check: verify not already instrumented, retrieve config, instantiate InstrumentorLoader, call instrument_one, register in _active_instrumentors'}
- {'step': 6, 'action': 'Handle special cases', 'detail': "If package_name is 'mem0' and newly added, also instrument concurrent.futures with concurrent_config"}
- {'step': 7, 'action': 'Return instrumented module', 'detail': 'Return the module object to caller; instrumentation is now active for subsequent calls'}

## Constraints

- Must preserve original import behavior; return the actual module object after instrumentation
- Must check version compatibility before instantiating instrumentor
- Must handle optional package_name field in InstrumentorLoader config
- Must detect and handle special cases (e.g., concurrent.futures dependency on mem0)

## Cautions

- Double-instrumentation can cause performance degradation or conflicting hooks; enforce single-instrumentation per package
- Import interception is global; ensure no circular dependencies or import-time side effects break the chain
- Version mismatches between instrumentor and target package may cause runtime errors; validate min_version before instantiation

## Output Contract

- Target packages are instrumented and registered in _active_instrumentors; the original module object is returned to the caller; subsequent calls to instrumented packages are monitored and logged by AgentOps.

## Example Executions

### Example 1

- Input: User code: import openai
- Output: openai module is loaded, InstrumentorLoader for openai is instantiated with config from PROVIDERS, instrumentor is registered in _active_instrumentors, openai module is returned to user code. Subsequent openai.ChatCompletion.create() calls are now monitored.
- Notes: Standard case: package name matches PROVIDERS registry exactly.

### Example 2

- Input: User code: from google.adk import something
- Output: google module is imported, full_item_name_candidate 'google.adk' is checked against registries, InstrumentorLoader for google.adk is instantiated if found, instrumentor is registered, module is returned. Subsequent google.adk calls are monitored.
- Notes: Nested package case: fromlist item is combined with parent name to form full candidate.

### Example 3

- Input: User code: import mem0; then import concurrent.futures
- Output: mem0 is instrumented and registered. Because package_name == 'mem0' and is_newly_added, concurrent.futures is also instrumented with concurrent_config. Both instrumentors are active.
- Notes: Special case: mem0 triggers automatic instrumentation of concurrent.futures dependency.

## Triggers

- AgentOps runtime initialization begins
- User code imports a monitored package (e.g., LLM client, memory system, concurrent execution library)

## Examples

### Example 1

Input:

  User code: import openai

Output:

  openai module is loaded, InstrumentorLoader for openai is instantiated with config from PROVIDERS, instrumentor is registered in _active_instrumentors, openai module is returned to user code. Subsequent openai.ChatCompletion.create() calls are now monitored.

Notes:

  Standard case: package name matches PROVIDERS registry exactly.

### Example 2

Input:

  User code: from google.adk import something

Output:

  google module is imported, full_item_name_candidate 'google.adk' is checked against registries, InstrumentorLoader for google.adk is instantiated if found, instrumentor is registered, module is returned. Subsequent google.adk calls are monitored.

Notes:

  Nested package case: fromlist item is combined with parent name to form full candidate.

### Example 3

Input:

  User code: import mem0; then import concurrent.futures

Output:

  mem0 is instrumented and registered. Because package_name == 'mem0' and is_newly_added, concurrent.futures is also instrumented with concurrent_config. Both instrumentors are active.

Notes:

  Special case: mem0 triggers automatic instrumentation of concurrent.futures dependency.
