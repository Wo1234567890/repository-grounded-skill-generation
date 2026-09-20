---
id: "283b7445-cd6a-5f23-8774-ae5511f71bbb"
name: "InstrumentorLoader Configuration"
description: "Encapsulates metadata and instantiation contract for dynamically loading instrumentor classes. Validates package version constraints and provides module name, class name, and minimum version required for safe instrumentation."
version: "0.1.0"
tags:
  - "instrumentation"
  - "configuration"
  - "metadata"
  - "version_constraint"
  - "dynamic_loading"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "An instrumentor must be loaded dynamically and version constraints must be checked before instantiation"
---

# InstrumentorLoader Configuration

Encapsulates metadata and instantiation contract for dynamically loading instrumentor classes. Validates package version constraints and provides module name, class name, and minimum version required for safe instrumentation.

## Prompt

Create an InstrumentorLoader instance by providing module_name, class_name, min_version, and optional package_name. This configuration object serves as a contract for downstream code to instantiate the actual instrumentor while respecting version constraints.

## Objective

Provide a reusable configuration schema and instantiation contract for instrumentor classes
## Applicable Signals

- An instrumentor must be loaded dynamically
- Version constraints must be checked before instantiation
- Package configuration is retrieved from PROVIDERS or AGENTIC_LIBRARIES registry

## Contraindications

- Instrumentor class is already instantiated
- Version check fails or minimum version constraint is not met
- module_name or class_name is not resolvable in the runtime environment

## Workflow Steps

- Retrieve configuration from PROVIDERS or AGENTIC_LIBRARIES registry by package_name
- Instantiate InstrumentorLoader with module_name, class_name, min_version, and optional package_name
- Pass configuration object to downstream code for actual instrumentor instantiation

## Constraints

- module_name must reference a valid importable Python module
- class_name must exist within the specified module
- min_version must be a valid semantic version string
- package_name is optional; if omitted, module_name is used as the package identifier

## Output Contract

- InstrumentorLoader instance is created with module_name, class_name, min_version, and optional package_name. Caller receives a configuration object that can be passed to InstrumentorLoader(**config) to instantiate the actual instrumentor.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- An instrumentor must be loaded dynamically and version constraints must be checked before instantiation
