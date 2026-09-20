---
id: "80a47fe9-16ce-5e87-add1-c3e9abf4e9e5"
name: "Properties Migrator Dependency Lifecycle Management"
description: "Manage the temporary addition and removal of the spring-boot-properties-migrator dependency during Spring Boot 3.0 upgrade to identify and migrate deprecated configuration properties."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "configuration-migration"
  - "dependency-management"
  - "properties-migrator"
  - "upgrade-tooling"
triggers:
  - "During Spring Boot 3.0 upgrade to assist with property migration"
  - "After upgrade completes and migration is verified"
examples:
  - input: "Spring Boot 2.7.x application with unknown deprecated properties"
    output: "Migrator added → deprecated properties logged → properties updated → migrator removed"
    notes: "Maven example: add dependency with runtime scope, run build, review logs, remove dependency."
  - input: "Gradle-based Spring Boot 2.7.x project"
    output: "runtimeOnly dependency added → application started → property warnings reviewed → dependency removed"
    notes: "Gradle example: use runtimeOnly() configuration, execute gradle build, clean up after migration."
---

# Properties Migrator Dependency Lifecycle Management

Manage the temporary addition and removal of the spring-boot-properties-migrator dependency during Spring Boot 3.0 upgrade to identify and migrate deprecated configuration properties.

## Prompt

1. Add spring-boot-properties-migrator to your build configuration with runtime scope.
2. Run your application or build to identify deprecated properties.
3. Review and update configuration properties as needed.
4. Remove the migrator dependency from your project before finalizing the upgrade.

## Objective

Manage the lifecycle of the properties migrator tool: add it to assist migration, then remove it post-migration.
## Applicable Signals

- Spring Boot 3.0 upgrade initiated
- Configuration properties need review and migration
- Deprecated property detection required

## Contraindications

- No configuration properties require migration
- Properties migrator is already removed from final build
- Application is not upgrading to Spring Boot 3.0

## Intervention Moves

- Add spring-boot-properties-migrator dependency with runtime scope to Maven pom.xml or Gradle build.gradle
- Execute build or application startup to trigger property migration detection
- Review identified deprecated properties and update configuration
- Remove spring-boot-properties-migrator dependency from project

## Workflow Steps

- {'step': 1, 'action': 'Add dependency to build configuration', 'detail': 'For Maven: add spring-boot-properties-migrator to pom.xml with scope=runtime. For Gradle: add runtimeOnly("org.springframework.boot:spring-boot-properties-migrator").'}
- {'step': 2, 'action': 'Run application or build', 'detail': 'Execute build or start application to trigger property migration detection and logging.'}
- {'step': 3, 'action': 'Review and update properties', 'detail': 'Examine identified deprecated properties and update configuration files accordingly.'}
- {'step': 4, 'action': 'Remove migrator dependency', 'detail': 'Delete the spring-boot-properties-migrator dependency from pom.xml or build.gradle.'}

## Constraints

- Dependency must be added with runtime scope only
- Migrator must be removed before finalizing the upgrade
- Only use during active migration phase

## Cautions

- Do not leave the migrator dependency in production builds
- Ensure all identified deprecated properties are addressed before removal

## Output Contract

- Properties migrator dependency successfully added to build configuration; deprecated properties identified and migrated; dependency removed from final project configuration; application ready for Spring Boot 3.0 deployment.

## Example Executions

### Example 1

- Input: Spring Boot 2.7.x application with unknown deprecated properties
- Output: Migrator added → deprecated properties logged → properties updated → migrator removed
- Notes: Maven example: add dependency with runtime scope, run build, review logs, remove dependency.

### Example 2

- Input: Gradle-based Spring Boot 2.7.x project
- Output: runtimeOnly dependency added → application started → property warnings reviewed → dependency removed
- Notes: Gradle example: use runtimeOnly() configuration, execute gradle build, clean up after migration.

## Triggers

- During Spring Boot 3.0 upgrade to assist with property migration
- After upgrade completes and migration is verified

## Examples

### Example 1

Input:

  Spring Boot 2.7.x application with unknown deprecated properties

Output:

  Migrator added → deprecated properties logged → properties updated → migrator removed

Notes:

  Maven example: add dependency with runtime scope, run build, review logs, remove dependency.

### Example 2

Input:

  Gradle-based Spring Boot 2.7.x project

Output:

  runtimeOnly dependency added → application started → property warnings reviewed → dependency removed

Notes:

  Gradle example: use runtimeOnly() configuration, execute gradle build, clean up after migration.
