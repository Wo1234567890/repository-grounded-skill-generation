---
id: "8c482643-fc74-5c48-9a5f-916facd94c7a"
name: "Spring Boot 3.0 Build Tool Migration"
description: "Migrate Gradle or Maven build configurations to Spring Boot 3.0 standards, including simplified main class resolution, dependency version updates, and build-info.properties management."
version: "0.1.0"
tags:
  - "spring-boot-3"
  - "migration"
  - "gradle"
  - "maven"
  - "build-tool"
triggers:
  - "Application uses Gradle/Maven requiring Spring Boot 3.0 updates"
---

# Spring Boot 3.0 Build Tool Migration

Migrate Gradle or Maven build configurations to Spring Boot 3.0 standards, including simplified main class resolution, dependency version updates, and build-info.properties management.

## Prompt

Update your Gradle build.gradle or Maven pom.xml to Spring Boot 3.0 version. For Gradle: simplify main class resolution using Spring Boot 3.0 conventions and configure build-info.properties exclusions as needed. For Maven: update dependency versions and plugin configurations to match Spring Boot 3.0 requirements. Validate all build files are syntactically correct before proceeding to framework-specific migrations.

## Objective

Update build tool configuration to Spring Boot 3.0 compatibility standards
## Applicable Signals

- Application uses Gradle or Maven as build tool
- Target version is Spring Boot 3.0 or later
- Build files reference Spring Boot 2.7.x or earlier versions

## Contraindications

- Application does not use Gradle or Maven
- Target version is Spring Boot 2.7.x or earlier
- Build files are already Spring Boot 3.0 compliant

## Intervention Moves

- Simplify Gradle main class name resolution using Spring Boot 3.0 conventions
- Update Maven pom.xml with new dependency versions and plugin configurations
- Exclude or include build-info.properties as needed for Gradle builds
- Configure Gradle tasks according to Spring Boot 3.0 standards

## Workflow Steps

- {'step': 1, 'title': 'Update Build Tool Version', 'action': 'Update Gradle build.gradle or Maven pom.xml to Spring Boot 3.0 version; simplify main class resolution for Gradle; configure Gradle tasks and build-info.properties exclusions as needed'}
- {'step': 2, 'title': 'Validate Build Configuration', 'action': 'Verify all build files are syntactically correct; check for deprecated properties or annotations; validate configuration property names and values'}
- {'step': 3, 'title': 'Test Build', 'action': 'Build application using updated build tool; verify build completes successfully without deprecation warnings'}

## Constraints

- Build files must be syntactically valid before and after migration
- Gradle main class resolution must follow Spring Boot 3.0 conventions
- Maven plugin versions must be compatible with Spring Boot 3.0

## Cautions

- Test build tool changes in isolation before applying security and batch changes
- Verify build-info.properties configuration against deployment requirements
- Ensure Gradle wrapper and Maven wrapper versions are compatible with Spring Boot 3.0

## Output Contract

- Updated and validated build files (pom.xml or build.gradle); application builds successfully without errors or deprecation warnings

## Triggers

- Application uses Gradle/Maven requiring Spring Boot 3.0 updates
