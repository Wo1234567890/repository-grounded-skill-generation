---
id: "d102b88a-5f27-500a-96bd-345c1e571d0c"
name: "Spring Data Property Prefix Migration"
description: "Migrate application configuration properties from legacy spring.data.* prefixes to module-specific prefixes (e.g., spring.cassandra.*, spring.redis.*) when upgrading to Spring Boot 3.0. The spring.data prefix is now reserved for Spring Data framework use, and properties under it imply Spring Data is required on the classpath."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "configuration-management"
  - "spring-data"
  - "property-migration"
triggers:
  - "Upgrading Spring Boot application from 2.x to 3.0"
  - "Application uses Spring Data modules (Cassandra, Redis, MongoDB, etc.)"
  - "Configuration files contain spring.data.* property prefixes"
---

# Spring Data Property Prefix Migration

Migrate application configuration properties from legacy spring.data.* prefixes to module-specific prefixes (e.g., spring.cassandra.*, spring.redis.*) when upgrading to Spring Boot 3.0. The spring.data prefix is now reserved for Spring Data framework use, and properties under it imply Spring Data is required on the classpath.

## Prompt

Review all application.properties or application.yml files for properties using spring.data.* prefixes. For each data module (Cassandra, Redis, MongoDB, etc.), relocate properties to their module-specific prefix. Validate that the application context loads without configuration errors and that data connectivity is restored.

## Objective

migrate_data_configuration
## Applicable Signals

- Build or startup logs show unrecognized spring.data.* properties
- Spring Data module is on classpath but configuration is not being picked up
- Migration checklist or upgrade guide references data property changes

## Contraindications

- Application does not use Spring Data modules or data access layer
- No spring.data.* properties present in configuration
- Application is not upgrading to Spring Boot 3.0

## Workflow Steps

- {'step': 1, 'action': 'Identify all spring.data.* properties in application.properties or application.yml'}
- {'step': 2, 'action': 'Map each property to its module-specific prefix (e.g., spring.data.cassandra.* → spring.cassandra.*)'}
- {'step': 3, 'action': 'Update configuration files with new prefixes'}
- {'step': 4, 'action': 'Rebuild and start application; verify no configuration errors in logs'}
- {'step': 5, 'action': 'Test data connectivity for each affected module (Cassandra, Redis, etc.)'}

## Constraints

- All spring.data.* properties must be identified before migration begins
- Module-specific prefix mappings must be verified against Spring Data release notes
- Application context must successfully load after property migration

## Cautions

- Incomplete migration may cause silent configuration failures; validate all data modules after relocation
- Some properties may have been renamed or removed in Spring Data; consult release notes for each module

## Output Contract

- All spring.data.* properties successfully remapped to module-specific prefixes; application configuration loads without errors; data module connectivity verified.

## Triggers

- Upgrading Spring Boot application from 2.x to 3.0
- Application uses Spring Data modules (Cassandra, Redis, MongoDB, etc.)
- Configuration files contain spring.data.* property prefixes
