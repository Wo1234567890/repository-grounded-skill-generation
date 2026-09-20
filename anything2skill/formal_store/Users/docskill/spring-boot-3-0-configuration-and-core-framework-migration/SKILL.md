---
id: "51e48ec6-d069-5ff6-941e-a29a859f0b32"
name: "Spring Boot 3.0 Configuration and Core Framework Migration"
description: "Structured session-level workflow to systematically migrate Spring Boot 2.x applications to 3.0 by updating configuration properties, auto-configuration files, replacing javax.* with jakarta.* imports, removing deprecated annotations, and validating successful startup."
version: "0.1.0"
tags:
  - "spring-boot"
  - "migration"
  - "configuration"
  - "jakarta-ee"
  - "framework-upgrade"
  - "refactoring"
triggers:
  - "Actively migrating configuration files, application properties, and core Spring annotations to Spring Boot 3.0"
---

# Spring Boot 3.0 Configuration and Core Framework Migration

Structured session-level workflow to systematically migrate Spring Boot 2.x applications to 3.0 by updating configuration properties, auto-configuration files, replacing javax.* with jakarta.* imports, removing deprecated annotations, and validating successful startup.

## Prompt

Execute the following configuration and core framework updates in sequence:
1. Audit all configuration property files (application.properties/yml) and document current keys and values.
2. Update configuration property keys to Spring Boot 3.0 equivalents using the official migration guide.
3. Migrate auto-configuration files to Spring Boot 3.0 format and naming conventions.
4. Replace all javax.* imports with jakarta.* equivalents throughout the codebase via bulk find-and-replace with verification.
5. Remove @ConstructorBinding annotations from type-level class declarations.
6. Remove or refactor YamlJsonParser usage (removed in Spring Boot 3.0).
7. Run application startup and configuration loading tests to validate successful migration.

## Objective

Execute configuration and core framework updates required for Spring Boot 3.0 compatibility
## Applicable Signals

- Active migration from Spring Boot 2.x to 3.0 underway
- Configuration files (application.properties or application.yml) present in project
- Auto-configuration files exist and require format updates
- Source code contains javax.* imports or deprecated Spring annotations
- Team is at the configuration and core framework migration phase

## Contraindications

- Application has no configuration properties or uses only external configuration management systems
- Migration to Spring Boot 3.0 is already complete
- Project is still on Spring Boot 2.x and not yet ready for migration
- Configuration is managed entirely by third-party tools outside the application codebase

## Intervention Moves

- Systematically scan and update all configuration property keys to Spring Boot 3.0 equivalents
- Perform bulk find-and-replace of javax.* with jakarta.* across all source files
- Remove @ConstructorBinding annotations from type-level class declarations
- Identify and remove or refactor YamlJsonParser usage
- Review and update auto-configuration file structure and naming conventions
- Run application tests to validate configuration loading and startup

## Workflow Steps

- {'step': 1, 'action': 'Audit configuration files', 'detail': 'Identify all application.properties and application.yml files; document current property keys and values'}
- {'step': 2, 'action': 'Update configuration properties', 'detail': 'Replace deprecated or renamed property keys with Spring Boot 3.0 equivalents; consult official migration guide for each change'}
- {'step': 3, 'action': 'Migrate auto-configuration files', 'detail': 'Update auto-configuration file structure, naming, and location to match Spring Boot 3.0 conventions'}
- {'step': 4, 'action': 'Replace javax.* imports', 'detail': 'Perform bulk find-and-replace of javax.* with jakarta.* across all source files; verify each replacement'}
- {'step': 5, 'action': 'Remove deprecated annotations', 'detail': 'Remove @ConstructorBinding from type-level declarations; remove or refactor YamlJsonParser usage'}
- {'step': 6, 'action': 'Validate and test', 'detail': 'Run application startup tests and configuration loading tests to confirm successful migration'}

## Constraints

- All javax.* to jakarta.* replacements must be completed before application startup
- Auto-configuration files must conform to Spring Boot 3.0 file naming and location conventions
- Deprecated annotations must be removed or replaced; they will cause compilation or runtime errors in Spring Boot 3.0
- Configuration property changes must be validated against Spring Boot 3.0 documentation

## Cautions

- Bulk find-and-replace of javax.* to jakarta.* may affect non-Spring dependencies; verify each replacement
- Some configuration properties may have been renamed or restructured; consult official migration guide for each property
- YamlJsonParser removal may require alternative YAML parsing strategies; review usage context before refactoring
- Test application thoroughly after configuration migration to catch runtime property binding issues

## Output Contract

- Deliverable: Updated application.properties/yml files, auto-configuration files, and source code with all javax.* imports replaced by jakarta.*, deprecated annotations removed, and configuration properties aligned with Spring Boot 3.0 specification. Application successfully starts and loads configuration without errors.

## Triggers

- Actively migrating configuration files, application properties, and core Spring annotations to Spring Boot 3.0
