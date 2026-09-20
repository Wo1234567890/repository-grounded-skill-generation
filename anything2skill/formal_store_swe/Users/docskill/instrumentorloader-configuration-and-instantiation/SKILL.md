---
id: "896eab1f-9bf8-5782-a197-b6ec97efa6ca"
name: "InstrumentorLoader Configuration and Instantiation"
description: "Encapsulates metadata and instantiation logic for dynamically loading instrumentor classes. Provides a reusable dataclass and factory pattern that stores module name, class name, minimum version, and optional package name mapping for later instrumentor creation with version validation."
version: "0.1.0"
tags:
  - "instrumentation"
  - "loader"
  - "configuration"
  - "factory_pattern"
  - "version_validation"
  - "dynamic_loading"
triggers:
  - "Instrumentor configuration needs to be stored, validated, or instantiated dynamically"
---

# InstrumentorLoader Configuration and Instantiation

Encapsulates metadata and instantiation logic for dynamically loading instrumentor classes. Provides a reusable dataclass and factory pattern that stores module name, class name, minimum version, and optional package name mapping for later instrumentor creation with version validation.

## Prompt

Use this reference to understand the InstrumentorLoader contract: it is a dataclass that holds configuration for a single instrumentor. Fields include module_name (str), class_name (str), min_version (str), and optional package_name (str). When instantiating an instrumentor, pass a config dict matching these fields to InstrumentorLoader(**config). The loader validates version constraints before instantiation and supports optional package name mapping for cases where the pip package name differs from the module name.

## Objective

Provide a reusable data structure and factory pattern for instrumentor creation with version validation
## Applicable Signals

- Instrumentor configuration needs to be stored
- Instrumentor needs to be validated before instantiation
- Instrumentor must be instantiated dynamically at runtime

## Contraindications

- Instrumentor is already instantiated
- Version constraints are not applicable or enforced
- Static instrumentor binding is preferred over dynamic loading

## Workflow Steps

- Receive config dict with module_name, class_name, min_version, and optional package_name
- Instantiate InstrumentorLoader with config parameters
- Validate version constraints against installed package
- Pass loader instance to instrument_one() or equivalent factory method for instantiation

## Constraints

- module_name and class_name must be valid Python identifiers
- min_version must be a valid semantic version string
- package_name, when provided, must match an installed pip package

## Output Contract

- InstrumentorLoader instance holds module_name, class_name, min_version, and optional package_name; ready for downstream instantiation via instrument_one() or equivalent factory method

## Triggers

- Instrumentor configuration needs to be stored, validated, or instantiated dynamically
