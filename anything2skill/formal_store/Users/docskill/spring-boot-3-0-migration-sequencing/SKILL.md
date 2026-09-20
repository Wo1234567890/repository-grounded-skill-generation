---
id: "e17409f4-1716-5822-936c-5369b1ca8adb"
name: "Spring Boot 3.0 Migration Sequencing"
description: "Ordered macro-protocol for migrating a Spring Boot 2.7.x application to 3.0. Executes pre-flight validation (latest 2.7.x version, dependency review, system requirements), deprecation removal, and incremental upgrade steps with properties migration support."
version: "0.1.0"
tags:
  - "spring-boot"
  - "migration"
  - "framework-upgrade"
  - "dependency-management"
  - "java-17"
triggers:
  - "Team is planning or executing a Spring Boot 2.7.x to 3.0 upgrade"
---

# Spring Boot 3.0 Migration Sequencing

Ordered macro-protocol for migrating a Spring Boot 2.7.x application to 3.0. Executes pre-flight validation (latest 2.7.x version, dependency review, system requirements), deprecation removal, and incremental upgrade steps with properties migration support.

## Prompt

Execute the following phases in order:
1. Upgrade to the latest 2.7.x version to ensure current dependencies.
2. Review and align dependencies: compare 2.7.x and 3.0.x dependency management; identify compatible versions for unmanaged dependencies (e.g., Spring Cloud).
3. Validate system requirements: confirm Java 17+ and Spring Framework 6.0 compatibility.
4. Remove deprecated code: audit and remove all methods, classes, and properties deprecated in Spring Boot 2.x.
5. Upgrade to Spring Boot 3.0 latest maintenance release.
6. Add spring-boot-properties-migrator (Maven or Gradle) to assist with configuration property migration.
7. Review and migrate configuration properties as flagged by the migrator.
8. Remove the properties-migrator dependency after migration is complete.
9. Validate build and runtime behavior; address any remaining breaking changes (e.g., dispatch types, Jakarta EE, Micrometer).

## Objective

Complete a safe, phased migration from Spring Boot 2.7.x to 3.0 with all dependencies resolved and deprecated code removed
## Applicable Signals

- Team is planning or executing a Spring Boot 2.7.x to 3.0 upgrade
- Application currently runs on Spring Boot 2.7.x
- Deprecation warnings appear in build logs or IDE

## Contraindications

- Application is already on Spring Boot 3.0 or later
- Team is not using Spring Boot framework
- Java version is below 17 (Spring Boot 3.0 requires Java 17+)

## Workflow Steps

- {'step': 1, 'name': 'Upgrade to Latest 2.7.x', 'action': 'Update Spring Boot version to the latest available 2.7.x release in pom.xml or build.gradle'}
- {'step': 2, 'name': 'Review Dependencies', 'action': 'Compare dependency management between 2.7.x and 3.0.x; identify compatible versions for unmanaged dependencies'}
- {'step': 3, 'name': 'Validate System Requirements', 'action': 'Confirm Java 17+ is available and Spring Framework 6.0 compatibility is met'}
- {'step': 4, 'name': 'Remove Deprecated Code', 'action': 'Audit codebase for deprecated methods, classes, and properties from Spring Boot 2.x; remove or replace all occurrences'}
- {'step': 5, 'name': 'Upgrade to Spring Boot 3.0', 'action': 'Update Spring Boot version to latest 3.0.x maintenance release'}
- {'step': 6, 'name': 'Add Properties Migrator', 'action': 'Add spring-boot-properties-migrator dependency (Maven: <scope>runtime</scope>; Gradle: runtimeOnly)'}
- {'step': 7, 'name': 'Migrate Configuration Properties', 'action': 'Build and run application; review migrator output and update application.properties or application.yml accordingly'}
- {'step': 8, 'name': 'Remove Properties Migrator', 'action': 'Delete spring-boot-properties-migrator from project dependencies'}
- {'step': 9, 'name': 'Validate and Test', 'action': 'Build application, run unit and integration tests, verify runtime behavior on Spring Boot 3.0'}

## Constraints

- Must complete pre-flight checks before attempting upgrade
- Deprecated code must be removed before upgrading to 3.0
- spring-boot-properties-migrator must be removed after migration is complete
- Unmanaged dependencies (e.g., Spring Cloud) require explicit version alignment before upgrade

## Cautions

- Spring Security 6.0 now applies authorization to every dispatch type; configure spring.security.filter.dispatcher-types if needed
- Jakarta EE replaces javax packages; review Spring Framework 6.0 upgrade guide for namespace changes
- Review breaking changes in Micrometer, Actuator, data access layers, and Gradle/Maven tooling

## Output Contract

- Application successfully builds and runs on Spring Boot 3.0 with all deprecated code removed, dependencies resolved, and configuration properties migrated. No spring-boot-properties-migrator dependency remains in the final build.

## Triggers

- Team is planning or executing a Spring Boot 2.7.x to 3.0 upgrade
