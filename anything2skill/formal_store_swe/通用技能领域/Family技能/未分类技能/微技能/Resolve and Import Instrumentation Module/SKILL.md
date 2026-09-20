---
id: "10aa8713-a166-5f8d-b6b3-2a22e1c25c7b"
name: "Resolve and Import Instrumentation Module"
description: "Dynamically import an instrumentation module by name and return the module object for subsequent class instantiation or method access."
version: "0.1.0"
tags:
  - "importlib"
  - "dynamic_import"
  - "module_resolution"
  - "instrumentation"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "When you need to obtain a module object from a stored module name string"
  - "Before instantiating a class from that module"
examples:
  - input: "module_name = 'concurrent.futures'"
    output: "<module 'concurrent.futures' from '...'>"
    notes: "Standard library module import succeeds; caller can now access classes like ThreadPoolExecutor"
  - input: "module_name = 'custom.instrumentation'"
    output: "<module 'custom.instrumentation' from '...'>"
    notes: "Custom module import; caller can now instantiate classes defined in that module"
---

# Resolve and Import Instrumentation Module

Dynamically import an instrumentation module by name and return the module object for subsequent class instantiation or method access.

## Prompt

Use importlib.import_module() to load the module specified by module_name. Return the ModuleType object. This operation assumes the module name is valid and the module exists in the environment.

## Objective

load_instrumentation_module
## Applicable Signals

- module_name string is available and non-empty
- module existence has been pre-validated or version check passed
- caller needs ModuleType object for attribute access or class instantiation

## Contraindications

- module_name is invalid, malformed, or refers to a non-existent module
- version validation has not been performed before this operation
- module import would raise ImportError or ModuleNotFoundError

## Workflow Steps

- {'step': 1, 'action': 'Receive module_name as input', 'detail': "module_name is a string representing the dotted module path (e.g., 'concurrent.futures', 'custom.instrumentation')"}
- {'step': 2, 'action': 'Call importlib.import_module(module_name)', 'detail': 'Dynamically load and return the ModuleType object'}
- {'step': 3, 'action': 'Return ModuleType object', 'detail': 'Caller can now use getattr() or direct attribute access on the module'}

## Constraints

- module_name must be a valid dotted module path string
- the target module must be installed and importable in the current environment
- this operation does not perform version checking; assume pre-validation

## Cautions

- importlib.import_module() will raise ImportError if the module cannot be found
- side effects may occur during module import (e.g., module-level code execution)
- ensure module_name is trusted and does not come from untrusted user input

## Output Contract

- Returns a ModuleType object corresponding to module_name. The object is ready for attribute access (e.g., getattr(module, class_name) for class instantiation). If import fails, raises ImportError.

## Example Executions

### Example 1

- Input: module_name = 'concurrent.futures'
- Output: <module 'concurrent.futures' from '...'>
- Notes: Standard library module import succeeds; caller can now access classes like ThreadPoolExecutor

### Example 2

- Input: module_name = 'custom.instrumentation'
- Output: <module 'custom.instrumentation' from '...'>
- Notes: Custom module import; caller can now instantiate classes defined in that module

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- When you need to obtain a module object from a stored module name string
- Before instantiating a class from that module

## Examples

### Example 1

Input:

  module_name = 'concurrent.futures'

Output:

  <module 'concurrent.futures' from '...'>

Notes:

  Standard library module import succeeds; caller can now access classes like ThreadPoolExecutor

### Example 2

Input:

  module_name = 'custom.instrumentation'

Output:

  <module 'custom.instrumentation' from '...'>

Notes:

  Custom module import; caller can now instantiate classes defined in that module
