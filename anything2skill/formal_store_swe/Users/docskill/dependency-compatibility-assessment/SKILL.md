---
id: "74d1515b-7065-54b8-b35b-2520eb505ac3"
name: "Dependency Compatibility Assessment"
description: "Identifies and resolves version mismatches between Spring Boot 2.7.x and 3.0.x managed dependencies, including third-party libraries (e.g., Spring Cloud) not managed by Spring Boot. Ensures all project dependencies are aligned to compatible versions before upgrading to Spring Boot 3.0."
version: "0.1.0"
tags:
  - "spring-boot-migration"
  - "dependency-management"
  - "version-compatibility"
  - "pre-upgrade"
triggers:
  - "Preparing for Spring Boot 3.0 migration; comparing dependency management between 2.7.x and 3.0.x versions."
---

# Dependency Compatibility Assessment

Identifies and resolves version mismatches between Spring Boot 2.7.x and 3.0.x managed dependencies, including third-party libraries (e.g., Spring Cloud) not managed by Spring Boot. Ensures all project dependencies are aligned to compatible versions before upgrading to Spring Boot 3.0.

## Prompt

Review and audit all project dependencies against Spring Boot 3.0.x dependency management. Compare your current 2.7.x managed dependencies with 3.0.x versions. For unmanaged dependencies (e.g., Spring Cloud), identify the compatible version before upgrading. Document all version changes and resolve conflicts.

## Objective

Audit and align all project dependencies to compatible versions before upgrading to Spring Boot 3.0.
## Applicable Signals

- Preparing for Spring Boot 3.0 migration
- Comparing dependency management between 2.7.x and 3.0.x versions
- Project has external dependencies not managed by Spring Boot

## Contraindications

- Project has no external dependencies
- All dependencies are already Spring Boot managed and confirmed compatible

## Workflow Steps

- {'step': 1, 'action': 'Obtain dependency management lists', 'detail': 'Access Spring Boot 2.7.x and 3.0.x dependency management documentation or pom.xml/gradle files.'}
- {'step': 2, 'action': 'Compare managed dependencies', 'detail': 'Review version changes for all Spring Boot managed libraries between 2.7.x and 3.0.x.'}
- {'step': 3, 'action': 'Identify unmanaged dependencies', 'detail': 'List all third-party libraries (e.g., Spring Cloud) that your project explicitly versions.'}
- {'step': 4, 'action': 'Resolve version compatibility', 'detail': 'For each unmanaged dependency, identify the compatible version for Spring Boot 3.0.x.'}
- {'step': 5, 'action': 'Document findings', 'detail': 'Create a compatibility matrix or migration checklist with all version changes and conflicts resolved.'}

## Constraints

- Must complete before upgrading to Spring Boot 3.0
- Requires access to both 2.7.x and 3.0.x dependency management references

## Cautions

- Third-party libraries may have breaking changes; verify release notes for each dependency upgrade
- Some dependencies may not yet support Spring Boot 3.0; plan for alternatives if needed

## Output Contract

- Documented list of compatible dependency versions for all managed and unmanaged libraries; no version conflicts remain. Output should include a migration checklist or compatibility matrix ready for implementation.

## Triggers

- Preparing for Spring Boot 3.0 migration; comparing dependency management between 2.7.x and 3.0.x versions.
