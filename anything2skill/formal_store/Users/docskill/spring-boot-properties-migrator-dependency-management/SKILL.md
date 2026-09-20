---
id: "fa8dce3a-1fea-5197-8d1a-cc0bd1baf072"
name: "Spring Boot Properties Migrator Dependency Management"
description: "Add the `spring-boot-properties-migrator` runtime dependency during Spring Boot 3.0 migration to identify and update deprecated configuration properties, then remove it after migration is complete."
version: "0.1.0"
tags:
  - "spring-boot"
  - "migration"
  - "configuration"
  - "properties"
  - "upgrade"
  - "dependency-management"
triggers:
  - "Upgrading application to Spring Boot 3.0"
  - "Need to identify deprecated or renamed configuration properties"
  - "Configuration properties from Spring Boot 2.x require validation"
---

# Spring Boot Properties Migrator Dependency Management

Add the `spring-boot-properties-migrator` runtime dependency during Spring Boot 3.0 migration to identify and update deprecated configuration properties, then remove it after migration is complete.

## Prompt

1. Add `spring-boot-properties-migrator` to your build configuration (Maven pom.xml or Gradle build.gradle) with runtime scope.
2. Run your application or build process to generate migration warnings for deprecated or renamed properties.
3. Review the warnings and update your configuration properties accordingly.
4. Remove the `spring-boot-properties-migrator` dependency from your project before finalizing the migration.

## Objective

Use the properties migrator tool to identify and update deprecated configuration properties during Spring Boot 3.0 upgrade
## Applicable Signals

- Spring Boot version upgrade initiated
- Configuration property migration warnings appear in build logs
- Deprecated property keys detected in application.properties or application.yml

## Contraindications

- Migration is already complete
- Application has no configuration properties to migrate
- Production build or final release phase

## Workflow Steps

- {'step': 1, 'action': 'Add migrator dependency', 'detail': 'Add `spring-boot-properties-migrator` to Maven pom.xml with `<scope>runtime</scope>` or to Gradle build.gradle as `runtimeOnly`'}
- {'step': 2, 'action': 'Run application or build', 'detail': 'Execute build or start application to trigger property migration analysis'}
- {'step': 3, 'action': 'Review migration warnings', 'detail': 'Examine logs and warnings for deprecated or renamed configuration properties'}
- {'step': 4, 'action': 'Update properties', 'detail': 'Modify application.properties or application.yml to use new property names and values'}
- {'step': 5, 'action': 'Remove dependency', 'detail': 'Delete the `spring-boot-properties-migrator` dependency from build configuration'}

## Constraints

- Dependency must be added with runtime scope only
- Dependency must be removed before final build is deployed
- Only applicable during Spring Boot 3.0 migration window

## Cautions

- Do not leave the migrator dependency in production builds
- Review all migration warnings before removing the dependency
- Ensure all property updates are tested before removing the tool

## Output Contract

- Migrator dependency is added, migration warnings are reviewed and properties are updated, then dependency is removed from final build configuration. Application configuration is compatible with Spring Boot 3.0.

## Triggers

- Upgrading application to Spring Boot 3.0
- Need to identify deprecated or renamed configuration properties
- Configuration properties from Spring Boot 2.x require validation
