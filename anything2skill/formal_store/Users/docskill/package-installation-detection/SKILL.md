---
id: "b97a82ff-caa3-5758-b4a0-2cf5db1a9d5b"
name: "Package Installation Detection"
description: "Determine whether a Python module is an installed library (in site-packages) or a local module, to decide whether to apply instrumentation. Uses normalized path comparison against site-packages directories."
version: "0.1.0"
tags:
  - "path_inspection"
  - "module_classification"
  - "instrumentation_gating"
  - "initialization"
triggers:
  - "module import interception during dynamic package loading"
  - "need to decide whether to apply instrumentation to a package"
---

# Package Installation Detection

Determine whether a Python module is an installed library (in site-packages) or a local module, to decide whether to apply instrumentation. Uses normalized path comparison against site-packages directories.

## Prompt

Check if a module's file path is located within any site-packages directory. Normalize both the module path and site-packages directories using os.path.normcase and os.path.realpath. Compare the module path against all normalized site-packages directories (including user site if present). Return True if the module is found in any site-packages directory; return False if it is a local module or not in any site-packages location.

## Objective

classify_module_origin
## Applicable Signals

- module object with __file__ attribute available
- package name to be classified

## Contraindications

- module path already known to be local or excluded
- built-in modules (skip instrumentation detection)
- module __file__ attribute is None or unavailable

## Workflow Steps

- Retrieve site-packages directories using site.getsitepackages() and site.USER_SITE
- Normalize module path: os.path.normcase(os.path.realpath(os.path.abspath(module_obj.__file__)))
- Normalize each site-packages directory path
- Iterate through normalized site-packages directories
- Check if module_path starts with any site-packages directory path
- Return True if match found; return False if no match after all directories checked

## Constraints

- module_path must be normalized using os.path.normcase and os.path.realpath
- site-packages directories must be retrieved via site.getsitepackages() and site.USER_SITE
- all path comparisons must use normalized paths
- handle case where site.getsitepackages() returns a string instead of list

## Cautions

- Path normalization is critical for cross-platform compatibility
- site.USER_SITE may be None; check existence before adding to list
- site.getsitepackages() may return string or list; handle both cases

## Output Contract

- Boolean return value: True if module is an installed library in site-packages; False if module is local or not in any site-packages directory.

## Triggers

- module import interception during dynamic package loading
- need to decide whether to apply instrumentation to a package
