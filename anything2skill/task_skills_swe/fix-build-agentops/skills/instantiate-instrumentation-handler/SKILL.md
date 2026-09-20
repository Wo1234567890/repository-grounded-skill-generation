---
id: "2b6408f4-01bf-5c99-933b-b180669bc621"
name: "Instantiate Instrumentation Handler"
description: "Create a new instance of a specified instrumentor class from a loaded module, returning a ready-to-use BaseInstrumentor object."
version: "0.1.0"
tags:
  - "instrumentation"
  - "factory"
  - "object_creation"
  - "handler"
  - "module_loading"
triggers:
  - "Module is successfully loaded and imported"
  - "Version check (should_activate) returned True"
  - "Need a fresh instrumentor instance for a specific package or module"
---

# Instantiate Instrumentation Handler

Create a new instance of a specified instrumentor class from a loaded module, returning a ready-to-use BaseInstrumentor object.

## Prompt

Call get_instance() after confirming the module is loaded and version requirements are met. The method uses getattr to retrieve the class by name from the module, then instantiates it with no arguments. Returns a BaseInstrumentor instance ready for configuration.

## Objective

create_instrumentor_instance
## Applicable Signals

- module property is accessible
- class_name attribute is set
- caller has confirmed module availability

## Contraindications

- Module has not been imported or is unavailable
- class_name does not exist in the module
- should_activate returned False
- Module version does not meet minimum requirements

## Workflow Steps

- {'step': 1, 'action': 'Retrieve the loaded module via self.module property', 'detail': 'Uses importlib.import_module(self.module_name) internally'}
- {'step': 2, 'action': 'Look up the class by name using getattr()', 'detail': 'getattr(self.module, self.class_name) retrieves the class object'}
- {'step': 3, 'action': 'Instantiate the class with no arguments', 'detail': 'Calls the class constructor: getattr(self.module, self.class_name)()'}
- {'step': 4, 'action': 'Return the BaseInstrumentor instance', 'detail': 'Instance is ready for configuration and activation by caller'}

## Constraints

- Requires module to be pre-loaded via importlib.import_module()
- class_name must match an actual class in the module
- Instantiation assumes the class constructor takes no required arguments

## Cautions

- If class_name is incorrect or missing, getattr will raise AttributeError
- If the class constructor has required parameters, instantiation will fail
- No error handling is performed; caller must catch exceptions

## Output Contract

- Returns a BaseInstrumentor instance with no initialization errors. Instance is ready for downstream configuration and activation. If instantiation fails, an exception is raised to the caller.

## Triggers

- Module is successfully loaded and imported
- Version check (should_activate) returned True
- Need a fresh instrumentor instance for a specific package or module
