---
id: "60422189-34e8-502f-a32d-8e5aef027a7c"
name: "System Requirements Verification for Spring Boot 3.0"
description: "Validates that the runtime environment meets Spring Boot 3.0 minimum requirements before upgrade. Checks that Java version is 17 or later and Spring Framework 6.0 is available."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "environment-check"
  - "prerequisite"
  - "java-version"
  - "spring-framework"
triggers:
  - "Before initiating Spring Boot 3.0 upgrade"
  - "When verifying environment readiness for migration"
---

# System Requirements Verification for Spring Boot 3.0

Validates that the runtime environment meets Spring Boot 3.0 minimum requirements before upgrade. Checks that Java version is 17 or later and Spring Framework 6.0 is available.

## Prompt

Verify the following prerequisites before proceeding with Spring Boot 3.0 upgrade:
1. Check Java version is 17 or later (Java 8 is no longer supported).
2. Confirm Spring Framework 6.0 is available in the project.
3. If either requirement is not met, halt upgrade and remediate the environment.

## Objective

Prevent upgrade attempts on incompatible Java or Spring Framework versions
## Applicable Signals

- Upgrade to Spring Boot 3.0 planned
- Migration workflow initiated

## Contraindications

- Java 17+ and Spring Framework 6.0 already confirmed in use

## Intervention Moves

- Halt upgrade process if Java version is below 17
- Halt upgrade process if Spring Framework 6.0 is not available
- Provide remediation guidance: upgrade Java to 17+ or update Spring Framework dependency

## Workflow Steps

- {'step': 1, 'action': 'Check Java version', 'detail': 'Run `java -version` or inspect project build configuration to confirm Java 17 or later is in use.'}
- {'step': 2, 'action': 'Verify Spring Framework 6.0 availability', 'detail': 'Review project dependencies (pom.xml or build.gradle) to confirm Spring Framework 6.0 is declared or will be pulled by Spring Boot 3.0.'}
- {'step': 3, 'action': 'Gate decision', 'detail': 'If both checks pass, proceed to upgrade. If either fails, halt and remediate environment before retry.'}

## Constraints

- Java version must be 17 or later
- Spring Framework 6.0 must be available
- Check must complete before any dependency or code changes

## Cautions

- Java 8 is no longer supported in Spring Boot 3.0
- Older Spring Framework versions are incompatible

## Output Contract

- Boolean confirmation: true if Java 17+ and Spring Framework 6.0 are available; false otherwise. If false, upgrade must not proceed until environment is remediated.

## Triggers

- Before initiating Spring Boot 3.0 upgrade
- When verifying environment readiness for migration
