---
id: "96727506-a6cb-5116-8c91-d2e2654fb438"
name: "Spring Boot 3.0 Migration Sequencing"
description: "Orchestrates the multi-phase upgrade from Spring Boot 2.7.x to 3.0, ensuring prerequisite checks, dependency alignment, and deprecation removal before final upgrade. Validates system requirements (Java 17+, Spring Framework 6.0), reviews and resolves dependencies, removes deprecated code, and executes the upgrade in a safe, ordered sequence."
version: "0.1.0"
tags:
  - "spring-boot"
  - "migration"
  - "upgrade"
  - "framework"
  - "version-management"
  - "dependency-resolution"
triggers:
  - "Planning or executing a Spring Boot version upgrade from 2.7.x line to 3.0 or later"
---

# Spring Boot 3.0 Migration Sequencing

Orchestrates the multi-phase upgrade from Spring Boot 2.7.x to 3.0, ensuring prerequisite checks, dependency alignment, and deprecation removal before final upgrade. Validates system requirements (Java 17+, Spring Framework 6.0), reviews and resolves dependencies, removes deprecated code, and executes the upgrade in a safe, ordered sequence.

## Prompt

Execute the Spring Boot 3.0 migration in the following order: (1) Upgrade to latest 2.7.x version; (2) Review and align dependencies against 3.0.x; (3) Verify system requirements (Java 17+, Spring Framework 6.0); (4) Remove deprecated methods and properties from Spring Boot 2.x; (5) Add spring-boot-properties-migrator to runtime scope; (6) Upgrade to Spring Boot 3.0 maintenance release; (7) Remove migrator dependency after migration completes. Review Spring Framework 6.0 upgrade guide before proceeding.

## Objective

Execute a safe, ordered migration from Spring Boot 2.7.x to 3.0 with dependency and system requirement validation.
## Applicable Signals

- Planning or executing a Spring Boot version upgrade from 2.7.x line to 3.0 or later
- Application currently running on Spring Boot 2.7.x
- Need to coordinate multiple prerequisite checks before upgrade

## Contraindications

- Already on Spring Boot 3.0 or later
- Upgrading from versions earlier than 2.7.x without intermediate steps
- Java version below 17 (Spring Boot 3.0 requires Java 17+)
- Spring Framework version below 6.0

## Intervention Moves

- Upgrade to latest 2.7.x version before proceeding
- Compare dependency management between 2.7.x and 3.0.x
- Identify and resolve non-managed dependencies (e.g., Spring Cloud)
- Verify Java 17+ and Spring Framework 6.0 availability
- Audit and remove deprecated Spring Boot 2.x methods and properties
- Add spring-boot-properties-migrator to Maven pom.xml or Gradle build
- Upgrade to latest Spring Boot 3.0 maintenance release
- Remove spring-boot-properties-migrator after migration completes

## Workflow Steps

- {'phase': 'pre_upgrade', 'step': 1, 'action': 'Upgrade to latest 2.7.x version', 'rationale': 'Ensures building against most recent dependencies of 2.7.x line'}
- {'phase': 'pre_upgrade', 'step': 2, 'action': 'Review dependencies: compare 2.7.x and 3.0.x dependency management', 'rationale': 'Identifies breaking changes and required version updates'}
- {'phase': 'pre_upgrade', 'step': 3, 'action': 'Identify compatible versions for non-managed dependencies', 'rationale': 'Prevents upgrade failures due to incompatible transitive dependencies'}
- {'phase': 'pre_upgrade', 'step': 4, 'action': 'Verify system requirements: Java 17+, Spring Framework 6.0', 'rationale': 'Spring Boot 3.0 requires Java 17+ and Spring Framework 6.0; Java 8 no longer supported'}
- {'phase': 'pre_upgrade', 'step': 5, 'action': 'Audit and remove deprecated Spring Boot 2.x methods and properties', 'rationale': 'Deprecated classes and methods removed in 3.0; must be cleaned before upgrade'}
- {'phase': 'upgrade', 'step': 6, 'action': 'Add spring-boot-properties-migrator to runtime scope (Maven or Gradle)', 'rationale': 'Assists with configuration property migration during upgrade'}
- {'phase': 'upgrade', 'step': 7, 'action': 'Upgrade to latest Spring Boot 3.0 maintenance release', 'rationale': 'Completes the version upgrade with latest patches'}
- {'phase': 'post_upgrade', 'step': 8, 'action': 'Remove spring-boot-properties-migrator from dependencies', 'rationale': 'Migrator is temporary; must be removed after migration completes'}
- {'phase': 'post_upgrade', 'step': 9, 'action': 'Validate application startup and core functionality', 'rationale': 'Confirms successful migration and identifies any runtime issues'}

## Constraints

- Must complete pre_upgrade phase (latest 2.7.x, dependency review, system requirements check) before upgrade phase
- Deprecated code must be removed before upgrading to 3.0
- spring-boot-properties-migrator must be removed from dependencies after migration
- Dispatch type configuration (spring.security.filter.dispatcher-types) required for Spring Security 6.0 alignment in Servlet applications

## Cautions

- Non-managed dependencies (e.g., Spring Cloud) require explicit version identification before upgrade
- Review Spring Framework 6.0 upgrade guide to understand breaking changes
- Ensure all deprecated methods and properties are removed to avoid runtime failures

## Output Contract

- Application successfully running on Spring Boot 3.0 with all dependencies resolved, deprecations removed, and system requirements met (Java 17+, Spring Framework 6.0). spring-boot-properties-migrator removed from project dependencies. All configuration properties migrated and application passes functional validation.

## Triggers

- Planning or executing a Spring Boot version upgrade from 2.7.x line to 3.0 or later
