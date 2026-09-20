---
id: "97a2c7b0-2c4a-5b03-b2db-32b1f161e0ae"
name: "Maven Build Configuration Update for Spring Boot 3"
description: "Remove the deprecated `fork` attribute from `spring-boot:run` and `spring-boot:start` Maven plugin goals to achieve Spring Boot 3.0 compatibility."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "maven-plugin-configuration"
  - "build-configuration"
  - "deprecation-removal"
triggers:
  - "Migrating Maven build configuration to Spring Boot 3.0"
  - "`fork` attribute present in spring-boot:run or spring-boot:start goals"
  - "Build log shows deprecation warnings for fork attribute"
---

# Maven Build Configuration Update for Spring Boot 3

Remove the deprecated `fork` attribute from `spring-boot:run` and `spring-boot:start` Maven plugin goals to achieve Spring Boot 3.0 compatibility.

## Prompt

1. Locate `spring-boot:run` and `spring-boot:start` plugin goal configurations in pom.xml.
2. Remove any `fork` attribute declarations (deprecated in Spring Boot 2.7, removed in 3.0).
3. Verify the build configuration file syntax is valid.
4. Run a test build to confirm no deprecation warnings are emitted.

## Objective

update_build_plugin_config
## Applicable Signals

- pom.xml contains <fork>true</fork> or <fork>false</fork> in spring-boot-maven-plugin configuration
- Maven build targets Spring Boot 3.0 or later
- Build log shows deprecation warnings for fork attribute

## Contraindications

- Already using Spring Boot 3.0 or later without fork attribute
- Build configuration is not Maven

## Workflow Steps

- {'step': 1, 'action': 'Open pom.xml and locate spring-boot-maven-plugin configuration', 'check': 'Plugin block is found and readable'}
- {'step': 2, 'action': 'Remove <fork>true</fork> or <fork>false</fork> from spring-boot:run and spring-boot:start goal configurations', 'check': 'No fork attribute remains in the plugin configuration'}
- {'step': 3, 'action': 'Run mvn clean build to validate configuration', 'check': 'Build completes without deprecation warnings related to fork attribute'}

## Constraints

- fork attribute removal applies only to Maven spring-boot-maven-plugin
- Changes must be made before running the build

## Cautions

- Removing fork attribute may change process isolation behavior; test application startup in the Maven process

## Output Contract

- pom.xml is updated with fork attribute removed
- Maven build executes successfully without deprecation warnings
- Application starts in the Maven process without errors

## Triggers

- Migrating Maven build configuration to Spring Boot 3.0
- `fork` attribute present in spring-boot:run or spring-boot:start goals
- Build log shows deprecation warnings for fork attribute
