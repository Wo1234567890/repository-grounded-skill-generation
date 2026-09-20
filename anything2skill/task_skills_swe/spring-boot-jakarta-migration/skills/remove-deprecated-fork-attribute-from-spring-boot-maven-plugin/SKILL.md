---
id: "8838139c-3528-5f7a-82ed-c462b33754d5"
name: "Remove Deprecated fork Attribute from Spring Boot Maven Plugin"
description: "Remove the deprecated `fork` attribute from `spring-boot:run` and `spring-boot:start` Maven plugin goals when migrating a Spring Boot 2.7.x project to Spring Boot 3. This attribute was removed in Spring Boot 3 and must be eliminated from pom.xml to ensure the build process functions correctly."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "maven"
  - "build-configuration"
  - "deprecation-removal"
  - "pom-xml"
triggers:
  - "Maven-based Spring Boot 2.7.x project identified"
  - "Migration to Spring Boot 3 planned or in progress"
  - "pom.xml contains spring-boot-maven-plugin configuration"
---

# Remove Deprecated fork Attribute from Spring Boot Maven Plugin

Remove the deprecated `fork` attribute from `spring-boot:run` and `spring-boot:start` Maven plugin goals when migrating a Spring Boot 2.7.x project to Spring Boot 3. This attribute was removed in Spring Boot 3 and must be eliminated from pom.xml to ensure the build process functions correctly.

## Prompt

Locate the spring-boot-maven-plugin configuration in pom.xml. Find any `<fork>` elements within the `<spring-boot:run>` and `<spring-boot:start>` goal configurations. Remove these elements entirely. Verify the pom.xml is valid XML after removal.

## Objective

Eliminate deprecated Maven plugin configuration that no longer functions in Spring Boot 3
## Applicable Signals

- Build fails with unrecognized `fork` attribute error
- Code review identifies deprecated `fork` attribute in spring-boot-maven-plugin
- Pre-migration audit of pom.xml configuration

## Contraindications

- Project uses Gradle instead of Maven
- `fork` attribute already removed from pom.xml
- Project does not use spring-boot-maven-plugin

## Workflow Steps

- {'step': 1, 'action': 'Open pom.xml in editor', 'detail': 'Locate the spring-boot-maven-plugin section'}
- {'step': 2, 'action': 'Search for `<fork>` elements', 'detail': 'Find all occurrences within spring-boot:run and spring-boot:start goal configurations'}
- {'step': 3, 'action': 'Remove `<fork>` element and its value', 'detail': 'Delete the entire line or block containing the fork attribute'}
- {'step': 4, 'action': 'Validate pom.xml syntax', 'detail': 'Ensure XML is well-formed after removal'}
- {'step': 5, 'action': 'Test Maven build', 'detail': 'Run `mvn clean verify` to confirm no build errors'}

## Constraints

- Only applies to spring-boot:run and spring-boot:start goal configurations
- pom.xml must be valid XML before and after modification
- No other plugin configuration should be altered

## Cautions

- Ensure backup of pom.xml before making changes
- Verify build succeeds after removal using `mvn clean verify`

## Output Contract

- pom.xml updated with `fork` attribute removed from spring-boot:run and spring-boot:start goal configurations; Maven build executes without fork-related errors

## Triggers

- Maven-based Spring Boot 2.7.x project identified
- Migration to Spring Boot 3 planned or in progress
- pom.xml contains spring-boot-maven-plugin configuration
