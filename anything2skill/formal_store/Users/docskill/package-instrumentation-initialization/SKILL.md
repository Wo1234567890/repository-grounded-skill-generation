---
id: "8ab6381a-e2f5-5666-8d1e-85fa59b9301a"
name: "Package Instrumentation Initialization"
description: "Conditionally start monitoring and instrumenting Python packages using import hooks, with safeguards to prevent redundant or conflicting instrumentation of agentic libraries."
version: "0.1.0"
tags:
  - "instrumentation"
  - "initialization"
  - "import_hook"
  - "package_monitoring"
  - "conflict_prevention"
triggers:
  - "AgentOps monitoring is first activated"
  - "No active instrumentors are currently running (_active_instrumentors is empty)"
  - "Agentic library detection is needed to avoid double-instrumentation"
---

# Package Instrumentation Initialization

Conditionally start monitoring and instrumenting Python packages using import hooks, with safeguards to prevent redundant or conflicting instrumentation of agentic libraries.

## Prompt

Check if instrumentation is already active by examining _active_instrumentors. If empty, install the import hook (_import_monitor) to begin package monitoring. During iteration over sys.modules, check _has_agentic_library flag; if set, stop instrumentation to avoid double-instrumenting agentic libraries. Populate _active_instrumentors and set _has_agentic_library correctly based on detected libraries.

## Objective

Initialize and manage package-level instrumentation state with conflict prevention
## Applicable Signals

- _active_instrumentors list is empty
- Import monitoring has not yet been installed
- System module scan is required to detect agentic libraries

## Contraindications

- Instrumentation is already active (_active_instrumentors is non-empty)
- An agentic library has already been instrumented (_has_agentic_library is True)

## Workflow Steps

- {'step': 1, 'action': 'Check if _active_instrumentors is empty', 'condition': 'If empty, proceed; if non-empty, return without action'}
- {'step': 2, 'action': 'Install import hook by setting builtins.__import__ = _import_monitor', 'condition': 'Only if _active_instrumentors was empty'}
- {'step': 3, 'action': 'Iterate over sys.modules.keys() to scan for agentic libraries', 'condition': 'Continue until _has_agentic_library is set or all modules are scanned'}
- {'step': 4, 'action': 'For each module, validate type and check if it is an agentic library', 'condition': 'Skip non-ModuleType entries; break if agentic library detected'}
- {'step': 5, 'action': 'Populate _active_instrumentors and set _has_agentic_library flag', 'condition': 'Based on scan results'}

## Constraints

- Must check _has_agentic_library flag before instrumenting each package
- Must break iteration loop if agentic library is detected during scan
- Must validate module type before processing (isinstance check for ModuleType)
- Must not instrument packages already in _instrumenting_packages list

## Cautions

- Installing import hook affects all subsequent module imports; ensure no other instrumentation is active first
- Agentic library detection must complete before instrumenting non-agentic packages to prevent conflicts

## Output Contract

- Import hook (_import_monitor) is installed
- _active_instrumentors list is populated with detected instrumentors
- _has_agentic_library flag is set correctly to prevent further instrumentation of conflicting libraries

## Triggers

- AgentOps monitoring is first activated
- No active instrumentors are currently running (_active_instrumentors is empty)
- Agentic library detection is needed to avoid double-instrumentation
