---
id: "5822b8e3-c706-5a04-9a7e-d8de2b317877"
name: "Gradle Kotlin DSL buildInfo Exclusions Configuration for Spring Boot 3"
description: "Configure Gradle Kotlin DSL `buildInfo` exclusions to exclude properties such as 'time' for Spring Boot 3.0 compatibility."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "gradle-kotlin-dsl"
  - "build-configuration"
  - "buildinfo-exclusions"
triggers:
  - "Migrating Gradle build configuration to Spring Boot 3.0"
  - "buildInfo block present without excludes configuration"
---

# Gradle Kotlin DSL buildInfo Exclusions Configuration for Spring Boot 3

Configure Gradle Kotlin DSL `buildInfo` exclusions to exclude properties such as 'time' for Spring Boot 3.0 compatibility.

## Prompt

1. Open build.gradle.kts and locate or create the springBoot block.
2. Add or update the buildInfo block with excludes.set(setOf(...)) to exclude properties such as 'time'.
3. Verify the buildInfo block is syntactically valid.
4. Run a test build to confirm the configuration is applied correctly.

## Objective

update_build_plugin_config
## Applicable Signals

- Gradle build.gradle.kts uses buildInfo block without excludes configuration
- Gradle build targets Spring Boot 3.0 or later

## Contraindications

- Gradle build does not use buildInfo exclusions
- Build configuration is not Gradle Kotlin DSL

## Workflow Steps

- {'step': 1, 'action': 'Open build.gradle.kts and locate the springBoot block or create it if missing', 'check': 'springBoot block is found or created'}
- {'step': 2, 'action': 'Add or update buildInfo { excludes.set(setOf("time")) } block within springBoot', 'check': 'buildInfo block is syntactically valid and excludes are specified'}
- {'step': 3, 'action': 'Run gradle build to validate configuration', 'check': 'Build completes successfully with buildInfo configuration applied'}

## Constraints

- buildInfo exclusions apply only to Gradle Kotlin DSL projects
- Changes must be made before running the build

## Cautions

- Verify that excluded properties (e.g., 'time') are not required by downstream build steps or runtime configuration

## Output Contract

- build.gradle.kts is updated with buildInfo exclusions configured
- Gradle build executes successfully
- buildInfo properties are excluded as specified

## Triggers

- Migrating Gradle build configuration to Spring Boot 3.0
- buildInfo block present without excludes configuration
