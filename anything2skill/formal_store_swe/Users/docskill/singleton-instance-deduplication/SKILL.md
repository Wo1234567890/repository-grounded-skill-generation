---
id: "afacfee3-2f37-5749-8466-43fae31d33f8"
name: "Singleton Instance Deduplication"
description: "Remove duplicate class variable definitions (e.g., __instance = None) that appear multiple times in a class definition. Apply when consolidating singleton initialization to prevent accidental re-initialization or state corruption."
version: "0.1.0"
tags:
  - "singleton_pattern"
  - "code_cleanup"
  - "class_structure"
  - "deduplication"
  - "refactoring"
triggers:
  - "class definition contains repeated __instance or similar singleton marker variables at module or class scope"
  - "code review or linting detects duplicate class variable assignments"
  - "singleton initialization logic is being consolidated or refactored"
---

# Singleton Instance Deduplication

Remove duplicate class variable definitions (e.g., __instance = None) that appear multiple times in a class definition. Apply when consolidating singleton initialization to prevent accidental re-initialization or state corruption.

## Prompt

Scan the class definition for all occurrences of __instance = None or similar singleton marker variables. Identify and remove all duplicate declarations, keeping only one definition at the appropriate scope (typically at class level, before or after __init__). Verify that singleton initialization logic remains unchanged after deduplication.

## Objective

deduplicate_class_variables
## Applicable Signals

- multiple __instance = None declarations in same class
- duplicate singleton marker variable definitions
- class consolidation or refactoring in progress

## Contraindications

- intentional multiple definitions for version compatibility or feature flags
- class uses factory pattern instead of singleton
- duplicate definitions serve as fallback or conditional initialization

## Intervention Moves

- Locate all occurrences of __instance = None (or equivalent singleton marker) in the class definition
- Identify the primary definition location (typically early in class body)
- Remove all duplicate declarations
- Verify singleton initialization logic (__new__, __init__) is intact
- Run unit tests to confirm singleton behavior is preserved

## Workflow Steps

- Locate all occurrences of __instance = None (or equivalent singleton marker) in the class definition
- Identify the primary definition location (typically early in class body)
- Remove all duplicate declarations
- Verify singleton initialization logic (__new__, __init__) is intact
- Run unit tests to confirm singleton behavior is preserved

## Constraints

- preserve exactly one __instance = None definition
- do not alter singleton initialization logic or __new__ method
- maintain class scope and visibility of remaining definition

## Cautions

- verify no code path depends on the removed duplicate definitions
- test singleton behavior after deduplication to ensure no re-initialization occurs
- check for any conditional logic that may have relied on duplicate definitions

## Output Contract

- Single __instance = None definition remains in the class; all duplicate declarations removed; singleton initialization logic unchanged; class instantiation behavior verified to match pre-refactor state.

## Triggers

- class definition contains repeated __instance or similar singleton marker variables at module or class scope
- code review or linting detects duplicate class variable assignments
- singleton initialization logic is being consolidated or refactored
