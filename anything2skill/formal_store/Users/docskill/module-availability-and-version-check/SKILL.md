---
id: "c3904908-74ec-5bc8-a110-9b9c50374155"
name: "Module Availability and Version Check"
description: "Verify that a required Python package or module is installed and meets minimum version requirements before attempting to use it. Returns a boolean indicating readiness for instrumentation or import."
version: "0.1.0"
tags:
  - "dependency_check"
  - "version_validation"
  - "module_readiness"
  - "instrumentation_guard"
  - "pre_flight_check"
triggers:
  - "Before instrumenting or importing a module"
  - "When deciding whether to activate an instrumentation handler"
  - "When gating downstream operations on module readiness"
---

# Module Availability and Version Check

Verify that a required Python package or module is installed and meets minimum version requirements before attempting to use it. Returns a boolean indicating readiness for instrumentation or import.

## Prompt

Check if a module is available and its version meets the minimum requirement. For stdlib modules (e.g., concurrent.futures), compare against sys.version_info. For third-party packages, use the package_name if provided; otherwise derive from module_name. Call get_library_version to retrieve the installed version. Compare the installed version against min_version using semantic versioning. Return True if available and version >= min_version; return False if unavailable or version is insufficient. Catch and suppress exceptions, returning False on any error.

## Objective

pre-flight validation of module availability and version compatibility
## Applicable Signals

- instrumentation_request
- module_import_attempt
- handler_activation_decision

## Contraindications

- Module is already confirmed to be loaded and in use
- Version constraints are not applicable or undefined
- Runtime environment does not support version introspection

## Workflow Steps

- {'step': 1, 'action': "Check if package_name is 'python' (stdlib special case)", 'detail': "If true, extract sys.version_info.major, minor, micro and format as 'X.Y.Z'"}
- {'step': 2, 'action': 'Determine provider_name for version lookup', 'detail': 'Use explicit package_name if provided; otherwise split module_name and take the last component'}
- {'step': 3, 'action': 'Retrieve installed version', 'detail': 'Call get_library_version(provider_name) to obtain the version string'}
- {'step': 4, 'action': 'Compare versions', 'detail': 'Parse both installed version and min_version using semantic versioning; return True if installed >= min_version'}
- {'step': 5, 'action': 'Handle errors gracefully', 'detail': 'Wrap entire logic in try-except; return False on any exception'}

## Constraints

- min_version must be a valid semantic version string
- package_name or module_name must be provided
- Exceptions during version lookup must be caught and treated as unavailable

## Cautions

- Special handling required for stdlib modules (package_name == 'python'); use sys.version_info instead of get_library_version
- Version comparison is strict (>=); pre-release or development versions may not match expected semantics
- get_library_version may return 'unknown' if the package is not installed or introspection fails

## Output Contract

- Boolean result: True if package is available and version >= min_version; False if unavailable, version is insufficient, or any error occurs. No exception is raised; all errors are suppressed and treated as unavailable.

## Triggers

- Before instrumenting or importing a module
- When deciding whether to activate an instrumentation handler
- When gating downstream operations on module readiness
