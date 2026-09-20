---
id: "291617a0-293a-55d3-b5bb-fc9486e4bf69"
name: "Instrumentor Instance Factory"
description: "Create and return a new instance of a specified instrumentor class from a dynamically loaded module. Encapsulates the instantiation logic for instrumentation handlers."
version: "0.1.0"
tags:
  - "instrumentation"
  - "dynamic_loading"
  - "factory_pattern"
  - "initialization"
triggers:
  - "Module availability confirmed via should_activate check"
  - "Version requirements validated and met"
  - "Need to create a live instrumentor instance for monitoring or patching"
---

# Instrumentor Instance Factory

Create and return a new instance of a specified instrumentor class from a dynamically loaded module. Encapsulates the instantiation logic for instrumentation handlers.

## Prompt

Call get_instance() after confirming module availability and version requirements. The method retrieves the instrumentor class by name from the loaded module and instantiates it with no arguments. If the class_name does not exist in the module, an AttributeError will be raised.

## Objective

instantiate an instrumentor handler from module metadata
## Applicable Signals

- should_activate property returns True
- module property successfully imports the target module
- Caller ready to begin instrumentation workflow

## Contraindications

- Module is not available or should_activate returned False
- Version check failed or minimum version requirement not met
- class_name does not exist in the loaded module
- Module import raised an exception

## Workflow Steps

- Retrieve the loaded module via self.module property
- Use getattr() to fetch the class object by class_name
- Call the class constructor with no arguments
- Return the new instance

## Constraints

- Must be called after module availability is confirmed
- Instrumentor class must exist in the module with the specified class_name
- Instantiation assumes zero-argument constructor

## Cautions

- Will raise AttributeError if class_name is not found in module
- No validation of instrumentor instance state after creation; caller must verify readiness

## Output Contract

- Returns a new instance of BaseInstrumentor (or subclass) ready for use in instrumentation workflow. Raises AttributeError if class_name not found in module.

## Triggers

- Module availability confirmed via should_activate check
- Version requirements validated and met
- Need to create a live instrumentor instance for monitoring or patching
