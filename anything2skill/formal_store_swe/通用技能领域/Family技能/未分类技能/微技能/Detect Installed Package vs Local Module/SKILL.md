---
id: "f47f8f37-a51c-56ae-adc6-6d703827d0d7"
name: "Detect Installed Package vs Local Module"
description: "Classify whether a Python module is an installed library (in site-packages) or a local development module by normalizing file paths and comparing against site-packages directories. Used during instrumentation initialization to decide whether to apply monitoring."
version: "0.1.0"
tags:
  - "instrumentation"
  - "module_classification"
  - "path_inspection"
  - "import_interception"
  - "site_packages_detection"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "deciding whether to instrument a dynamically imported package"
  - "called during module import interception"
  - "need to classify module as library or local before applying instrumentation"
examples:
  - input: "module_obj with __file__ = '/usr/local/lib/python3.9/site-packages/requests/__init__.py'"
    output: "True (installed library)"
    notes: "Module path starts with normalized site-packages directory"
  - input: "module_obj with __file__ = '/home/user/project/local_module.py'"
    output: "False (local module)"
    notes: "Module path does not match any site-packages directory"
---

# Detect Installed Package vs Local Module

Classify whether a Python module is an installed library (in site-packages) or a local development module by normalizing file paths and comparing against site-packages directories. Used during instrumentation initialization to decide whether to apply monitoring.

## Prompt

Check if a module's file path is located within any site-packages directory. Normalize both the module path and site-packages paths using os.path.normcase and os.path.realpath. Compare the module path prefix against all normalized site-packages directories (including user site if present). Return True if the module is in site-packages (installed library); return False if it is a local module or not found in any site-packages directory.

## Objective

classify_module_origin
## Applicable Signals

- module object with __file__ attribute available
- import hook or instrumentation initialization phase active
- package name and module path provided

## Contraindications

- module path is already known to be a built-in or third-party library from prior context
- non-Python environments or modules without __file__ attribute
- module is a namespace package without a concrete file path

## Workflow Steps

- {'step': 1, 'action': 'Normalize the module file path using os.path.normcase(os.path.realpath(os.path.abspath(module_obj.__file__)))'}
- {'step': 2, 'action': 'Retrieve site-packages directories via site.getsitepackages(); handle both string and list return types'}
- {'step': 3, 'action': 'If site.USER_SITE exists and is a valid path, append it to the site-packages directories list'}
- {'step': 4, 'action': 'Normalize all site-packages directory paths using os.path.normcase(os.path.realpath(p)) and filter out non-existent paths'}
- {'step': 5, 'action': 'Iterate through normalized site-packages directories and check if module_path starts with any of them'}
- {'step': 6, 'action': 'If a match is found, log debug message and return True (installed library)'}
- {'step': 7, 'action': 'If no match is found after checking all directories, log debug message and return False (local module)'}

## Constraints

- module must have a valid __file__ attribute
- site-packages directories must be accessible and readable
- path normalization must use os.path.normcase and os.path.realpath for cross-platform consistency

## Cautions

- site.getsitepackages() may return a string or list depending on Python version; handle both cases
- user site directory (site.USER_SITE) may be None or non-existent; check existence before use
- symlinks and relative paths must be resolved to absolute normalized paths for accurate comparison

## Output Contract

- Returns a boolean flag: True if the module is an installed library (located in site-packages), False if it is a local module or not found in any site-packages directory. Includes debug logging of the classification decision for traceability.

## Example Executions

### Example 1

- Input: module_obj with __file__ = '/usr/local/lib/python3.9/site-packages/requests/__init__.py'
- Output: True (installed library)
- Notes: Module path starts with normalized site-packages directory

### Example 2

- Input: module_obj with __file__ = '/home/user/project/local_module.py'
- Output: False (local module)
- Notes: Module path does not match any site-packages directory

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- deciding whether to instrument a dynamically imported package
- called during module import interception
- need to classify module as library or local before applying instrumentation

## Examples

### Example 1

Input:

  module_obj with __file__ = '/usr/local/lib/python3.9/site-packages/requests/__init__.py'

Output:

  True (installed library)

Notes:

  Module path starts with normalized site-packages directory

### Example 2

Input:

  module_obj with __file__ = '/home/user/project/local_module.py'

Output:

  False (local module)

Notes:

  Module path does not match any site-packages directory
