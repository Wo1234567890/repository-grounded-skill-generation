---
id: "3c711241-b72c-597d-8f37-2bdd990f0b5b"
name: "Migrate Embedded MongoDB Test Setup from Spring Boot 3.0"
description: "Evaluate and migrate embedded MongoDB test infrastructure from removed Spring Boot 3.0 auto-configuration to either Flapdoodle library auto-configuration or Testcontainers alternative."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "test-infrastructure"
  - "embedded-mongodb"
  - "dependency-migration"
triggers:
  - "Application uses embedded MongoDB for integration tests"
  - "Spring Boot 3.0 upgrade in progress"
  - "Flapdoodle auto-configuration no longer available"
---

# Migrate Embedded MongoDB Test Setup from Spring Boot 3.0

Evaluate and migrate embedded MongoDB test infrastructure from removed Spring Boot 3.0 auto-configuration to either Flapdoodle library auto-configuration or Testcontainers alternative.

## Prompt

When upgrading to Spring Boot 3.0, auto-configuration and dependency management for Flapdoodle embedded MongoDB has been removed. If your application uses embedded MongoDB for testing, you must choose between: (1) using the auto-configuration library provided by the Flapdoodle project directly, or (2) modifying tests to use the Testcontainers project instead. Evaluate your test infrastructure requirements and select the appropriate replacement.

## Objective

replace_embedded_mongodb_setup
## Applicable Signals

- Test suite fails due to missing embedded MongoDB auto-configuration
- Dependency on spring-boot-starter-data-mongodb with embedded mode
- Integration tests reference embedded MongoDB instance

## Contraindications

- Application does not use MongoDB
- Production MongoDB is used instead of embedded
- No integration tests present

## Workflow Steps

- {'step': 1, 'action': 'Identify all test classes and configurations using embedded MongoDB', 'output': 'List of affected test files and current MongoDB setup code'}
- {'step': 2, 'action': 'Evaluate Flapdoodle auto-configuration library vs. Testcontainers based on infrastructure constraints', 'output': 'Decision: Flapdoodle or Testcontainers selected'}
- {'step': 3, 'action': 'Add chosen replacement library to test dependencies (remove spring-boot-starter-data-mongodb embedded mode if applicable)', 'output': 'Updated build configuration (pom.xml or build.gradle)'}
- {'step': 4, 'action': 'Refactor test setup code to use new embedded MongoDB provider', 'output': 'Modified test classes with new initialization and teardown logic'}
- {'step': 5, 'action': 'Run full test suite and verify embedded MongoDB instance lifecycle', 'output': 'All tests pass; embedded MongoDB starts and stops correctly'}

## Constraints

- Must choose exactly one replacement strategy: Flapdoodle or Testcontainers
- Replacement must support the same test lifecycle (startup and teardown)
- Test suite must pass with new embedded MongoDB setup

## Cautions

- Flapdoodle and Testcontainers have different configuration and lifecycle management patterns
- Testcontainers requires Docker or compatible container runtime
- Verify test isolation and data cleanup between test runs

## Output Contract

- Test suite runs successfully with either Flapdoodle auto-configuration library or Testcontainers
- Embedded MongoDB instance starts and tears down correctly between test runs
- No test failures due to missing auto-configuration

## Triggers

- Application uses embedded MongoDB for integration tests
- Spring Boot 3.0 upgrade in progress
- Flapdoodle auto-configuration no longer available
