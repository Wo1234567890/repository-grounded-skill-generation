---
id: "e54faee0-3503-514b-8b6a-1a230b7cc9e5"
name: "Jakarta EE and Spring Framework 6.0 Compatibility Check"
description: "Validates and updates application code to align with Jakarta EE namespace changes and Spring Framework 6.0 API requirements, including javax.* to jakarta.* package migration during Spring Boot 3.0 upgrade."
version: "0.1.0"
tags:
  - "spring-boot-3"
  - "jakarta-ee"
  - "spring-framework-6"
  - "migration"
  - "namespace-update"
triggers:
  - "Initiating Spring Boot 3.0 migration"
  - "Codebase contains javax.* imports"
  - "Spring Framework version needs upgrade to 6.0 or later"
---

# Jakarta EE and Spring Framework 6.0 Compatibility Check

Validates and updates application code to align with Jakarta EE namespace changes and Spring Framework 6.0 API requirements, including javax.* to jakarta.* package migration during Spring Boot 3.0 upgrade.

## Prompt

Review all imports and API calls in the codebase. Replace javax.* package references with jakarta.* equivalents. Validate that Spring Framework 6.0 APIs are correctly invoked. Check configuration files and dependency declarations for Jakarta EE compliance.

## Objective

Ensure all Jakarta EE and Spring Framework 6.0 compatibility requirements are met before or during Spring Boot 3.0 upgrade
## Applicable Signals

- Spring Boot 3.0 upgrade in progress
- Jakarta EE adoption required
- Spring Framework 6.0 compatibility needed

## Contraindications

- Application remains on Spring Boot 2.x
- No Jakarta EE or Spring Framework direct usage
- Legacy javax.* dependencies cannot be updated

## Intervention Moves

- Identify all javax.* imports in source files, configuration, and test code
- Map javax.* to jakarta.* equivalents for servlet, persistence, validation, and other Jakarta EE packages
- Review Spring Framework 6.0 API changes and validate application code conformance
- Update dependency declarations in pom.xml or build.gradle for Jakarta EE and Spring Framework 6.0 compatibility
- Execute full build and test suite to verify no import or API resolution errors

## Workflow Steps

- {'step': 1, 'action': 'Identify all javax.* imports', 'detail': 'Search codebase for javax.* package references in source files, configuration, and test code'}
- {'step': 2, 'action': 'Map javax.* to jakarta.* equivalents', 'detail': 'Replace javax.servlet.*, javax.persistence.*, javax.validation.*, and other Jakarta EE packages with jakarta.* counterparts'}
- {'step': 3, 'action': 'Review Spring Framework 6.0 API changes', 'detail': 'Validate that Spring-specific APIs (e.g., annotations, configuration classes) conform to Spring Framework 6.0 signatures'}
- {'step': 4, 'action': 'Update dependency declarations', 'detail': 'Ensure pom.xml or build.gradle declares Jakarta EE and Spring Framework 6.0 compatible versions'}
- {'step': 5, 'action': 'Compile and test', 'detail': 'Run full build and test suite to verify no import or API resolution errors'}

## Constraints

- All javax.* imports must be systematically identified before replacement
- Spring Framework 6.0 API changes must be validated against application code
- Transitive dependencies must also support Jakarta EE

## Cautions

- Some third-party libraries may not yet support Jakarta EE; verify compatibility before migration
- Spring Framework 6.0 introduces breaking changes; review deprecation notices
- Test thoroughly after namespace migration to catch runtime issues

## Output Contract

- All javax.* imports replaced with jakarta.* equivalents
- Spring Framework 6.0 API calls validated and updated
- Build succeeds without import or API resolution errors
- Test suite passes

## Triggers

- Initiating Spring Boot 3.0 migration
- Codebase contains javax.* imports
- Spring Framework version needs upgrade to 6.0 or later
