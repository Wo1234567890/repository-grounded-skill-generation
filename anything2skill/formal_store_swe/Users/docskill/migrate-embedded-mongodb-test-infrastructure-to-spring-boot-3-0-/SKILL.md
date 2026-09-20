---
id: "079594cb-b319-567b-80f9-73e63b02264c"
name: "Migrate Embedded MongoDB Test Infrastructure to Spring Boot 3.0 Compatible Alternative"
description: "Complete workflow for migrating embedded MongoDB test infrastructure from Spring Boot 3.0's removed auto-configuration to either Flapdoodle's standalone auto-configuration library or Testcontainers project. Handles dependency removal, alternative selection, and test code refactoring."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "embedded-mongodb"
  - "test-infrastructure"
  - "dependency-management"
  - "flapdoodle"
  - "testcontainers"
triggers:
  - "Upgrading to Spring Boot 3.0 and application uses embedded MongoDB for testing"
examples:
  - input: "Spring Boot 2.7.x application with test class using @DataMongoTest and embedded MongoDB auto-configuration"
    output: "Test class refactored to use Testcontainers @Testcontainers annotation and MongoDBContainer; embedded MongoDB instance provisioned by Testcontainers; test passes"
    notes: "Testcontainers approach requires Docker availability but provides more control over container lifecycle"
  - input: "Spring Boot 2.7.x application with Flapdoodle embedded MongoDB dependency managed by Spring Boot"
    output: "Dependency updated to Flapdoodle's standalone auto-configuration library; test configuration updated to use Flapdoodle's @EnableEmbeddedMongoDB or equivalent; test passes"
    notes: "Flapdoodle approach is lighter weight and does not require container runtime"
---

# Migrate Embedded MongoDB Test Infrastructure to Spring Boot 3.0 Compatible Alternative

Complete workflow for migrating embedded MongoDB test infrastructure from Spring Boot 3.0's removed auto-configuration to either Flapdoodle's standalone auto-configuration library or Testcontainers project. Handles dependency removal, alternative selection, and test code refactoring.

## Prompt

When upgrading to Spring Boot 3.0, Spring Boot no longer provides auto-configuration and dependency management for Flapdoodle embedded MongoDB. If your application uses embedded MongoDB for testing, you must migrate to one of two supported alternatives: (1) Use Flapdoodle's own auto-configuration library, or (2) Refactor tests to use Testcontainers. Follow the steps below to complete the migration.

## Objective

Migrate embedded MongoDB test infrastructure to supported alternatives during Spring Boot 3.0 upgrade
## Applicable Signals

- Upgrading application to Spring Boot 3.0
- Application currently uses embedded MongoDB for testing
- Build configuration includes Flapdoodle embedded MongoDB dependency
- Test suite relies on Spring Boot's auto-configuration for embedded MongoDB

## Contraindications

- Application does not use embedded MongoDB
- Application uses production MongoDB instances only
- Tests do not require embedded database instances

## Workflow Steps

- {'step': 1, 'action': 'Identify embedded MongoDB usage', 'detail': 'Scan test code and build configuration for Flapdoodle embedded MongoDB dependencies and auto-configuration references'}
- {'step': 2, 'action': 'Remove Spring Boot auto-configuration', 'detail': 'Remove spring-boot-starter-data-mongodb-embedded or equivalent from build configuration; remove any Spring Boot-provided Flapdoodle auto-configuration'}
- {'step': 3, 'action': 'Select migration path', 'detail': 'Choose between Flapdoodle auto-configuration library (lighter weight, no container runtime required) or Testcontainers (more flexible, requires Docker)'}
- {'step': 4, 'action': 'Add alternative dependency', 'detail': "If Flapdoodle: add Flapdoodle's standalone auto-configuration library to test dependencies. If Testcontainers: add Testcontainers MongoDB module to test dependencies"}
- {'step': 5, 'action': 'Refactor test configuration', 'detail': "Update test setup code to use chosen alternative's configuration and lifecycle management instead of Spring Boot auto-configuration"}
- {'step': 6, 'action': 'Verify test execution', 'detail': 'Run full test suite to confirm embedded MongoDB instance starts correctly and tests pass with new configuration'}

## Constraints

- Spring Boot 3.0 no longer provides Flapdoodle auto-configuration or dependency management
- Must select exactly one alternative: Flapdoodle auto-configuration library OR Testcontainers
- Test code must be refactored to work with chosen alternative
- Dependency coordinates must be updated in build configuration

## Cautions

- Flapdoodle auto-configuration library and Testcontainers have different setup and lifecycle management patterns
- Testcontainers requires Docker or container runtime availability in test environment
- Flapdoodle auto-configuration library may have different version compatibility requirements
- Existing test fixtures and setup code may require refactoring

## Output Contract

- Embedded MongoDB auto-configuration removed from Spring Boot configuration
- Tests refactored to use either Flapdoodle auto-configuration library or Testcontainers
- Test suite executes successfully with embedded MongoDB instance provisioned by chosen alternative
- No Spring Boot embedded MongoDB auto-configuration references remain in codebase

## Example Executions

### Example 1

- Input: Spring Boot 2.7.x application with test class using @DataMongoTest and embedded MongoDB auto-configuration
- Output: Test class refactored to use Testcontainers @Testcontainers annotation and MongoDBContainer; embedded MongoDB instance provisioned by Testcontainers; test passes
- Notes: Testcontainers approach requires Docker availability but provides more control over container lifecycle

### Example 2

- Input: Spring Boot 2.7.x application with Flapdoodle embedded MongoDB dependency managed by Spring Boot
- Output: Dependency updated to Flapdoodle's standalone auto-configuration library; test configuration updated to use Flapdoodle's @EnableEmbeddedMongoDB or equivalent; test passes
- Notes: Flapdoodle approach is lighter weight and does not require container runtime

## Triggers

- Upgrading to Spring Boot 3.0 and application uses embedded MongoDB for testing

## Examples

### Example 1

Input:

  Spring Boot 2.7.x application with test class using @DataMongoTest and embedded MongoDB auto-configuration

Output:

  Test class refactored to use Testcontainers @Testcontainers annotation and MongoDBContainer; embedded MongoDB instance provisioned by Testcontainers; test passes

Notes:

  Testcontainers approach requires Docker availability but provides more control over container lifecycle

### Example 2

Input:

  Spring Boot 2.7.x application with Flapdoodle embedded MongoDB dependency managed by Spring Boot

Output:

  Dependency updated to Flapdoodle's standalone auto-configuration library; test configuration updated to use Flapdoodle's @EnableEmbeddedMongoDB or equivalent; test passes

Notes:

  Flapdoodle approach is lighter weight and does not require container runtime
