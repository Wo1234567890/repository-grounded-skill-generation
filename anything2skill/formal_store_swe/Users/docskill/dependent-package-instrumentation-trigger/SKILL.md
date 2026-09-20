---
id: "ea776e3a-114c-52e7-8cf1-04d141bb7c88"
name: "Dependent Package Instrumentation Trigger"
description: "Automatically instruments dependent packages (e.g., concurrent.futures when mem0 is instrumented) to ensure complete observability of related execution contexts."
version: "0.1.0"
tags:
  - "instrumentation"
  - "dependency_handling"
  - "observability"
  - "concurrent_execution"
  - "post_instrumentation"
triggers:
  - "A package with known dependencies (e.g., mem0) is newly instrumented and the dependent module is available"
examples:
  - input: "Parent package 'mem0' is newly instrumented; concurrent.futures module is available in sys.modules"
    output: "InstrumentorLoader for concurrent.futures is instantiated and instrument_one() is called; concurrent_instrumentor is registered with _agentops_instrumented_package_key = 'concurrent.futures'"
    notes: "Special case handling ensures concurrent execution visibility when mem0 is active"
---

# Dependent Package Instrumentation Trigger

Automatically instruments dependent packages (e.g., concurrent.futures when mem0 is instrumented) to ensure complete observability of related execution contexts.

## Prompt

When a parent package with known dependencies is newly instrumented, check if the dependent module is available in sys.modules. If available, create and register an instrumentor for the dependent package using the same loader pattern as the parent. This ensures concurrent execution within the parent package becomes observable.

## Objective

Instrument a dependent package when its parent package is newly instrumented
## Applicable Signals

- Parent package (e.g., mem0) is newly instrumented
- Dependent module (e.g., concurrent.futures) is available in sys.modules
- Parent package has a known dependency mapping in configuration

## Contraindications

- Dependent package is not available in sys.modules
- Parent package was already instrumented in a prior session
- Dependent package configuration is missing or malformed

## Intervention Moves

- Check if parent package matches a known dependency trigger (e.g., package_name == 'mem0')
- Verify dependent module is available via sys.modules.get()
- Retrieve dependent package configuration from config store
- Instantiate InstrumentorLoader with dependent package config
- Call instrument_one() to create and register the dependent instrumentor
- Store instrumentor reference with _agentops_instrumented_package_key

## Workflow Steps

- {'step': 1, 'action': 'Check parent package identity', 'detail': "Verify if package_name matches a known dependency trigger (e.g., 'mem0')"}
- {'step': 2, 'action': 'Verify is_newly_added flag', 'detail': 'Confirm parent package was just instrumented in this session'}
- {'step': 3, 'action': 'Check dependent module availability', 'detail': 'Call sys.modules.get() for dependent package name; proceed only if not None'}
- {'step': 4, 'action': 'Retrieve dependent package config', 'detail': 'Look up dependent package in PROVIDERS or AGENTIC_LIBRARIES'}
- {'step': 5, 'action': 'Instantiate InstrumentorLoader', 'detail': 'Create loader with dependent package config (module_name, class_name, min_version, package_name)'}
- {'step': 6, 'action': 'Instrument dependent package', 'detail': 'Call instrument_one(loader) to create and register instrumentor instance'}
- {'step': 7, 'action': 'Register package key', 'detail': 'Set instrumentor_instance._agentops_instrumented_package_key to dependent package name'}

## Constraints

- Only trigger when is_newly_added flag is True for parent package
- Dependent module must exist and be importable
- InstrumentorLoader must succeed without raising exceptions

## Cautions

- Wrap dependent package instrumentation in try-except to handle missing modules gracefully
- Verify dependent package config exists before instantiating loader

## Output Contract

- Dependent package instrumentor is created, registered, and marked with _agentops_instrumented_package_key; concurrent execution within the parent package is now observable. If dependent module is unavailable, operation is skipped without error.

## Example Executions

### Example 1

- Input: Parent package 'mem0' is newly instrumented; concurrent.futures module is available in sys.modules
- Output: InstrumentorLoader for concurrent.futures is instantiated and instrument_one() is called; concurrent_instrumentor is registered with _agentops_instrumented_package_key = 'concurrent.futures'
- Notes: Special case handling ensures concurrent execution visibility when mem0 is active

## Triggers

- A package with known dependencies (e.g., mem0) is newly instrumented and the dependent module is available

## Examples

### Example 1

Input:

  Parent package 'mem0' is newly instrumented; concurrent.futures module is available in sys.modules

Output:

  InstrumentorLoader for concurrent.futures is instantiated and instrument_one() is called; concurrent_instrumentor is registered with _agentops_instrumented_package_key = 'concurrent.futures'

Notes:

  Special case handling ensures concurrent execution visibility when mem0 is active
