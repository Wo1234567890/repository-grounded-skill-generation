---
id: "0dcd2700-9c6b-59d4-b856-10fd3a379cff"
name: "Spring Data Properties Prefix Migration"
description: "Migrate application properties from `spring.data.*` prefix to service-specific prefixes during Spring Boot 3.0 upgrade. The `spring.data` prefix is now reserved for Spring Data only; data service configurations (Cassandra, Redis, etc.) must be relocated to their respective prefixes (e.g., `spring.cassandra.*`)."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "configuration"
  - "data-services"
  - "property-migration"
triggers:
  - "Upgrading Spring Boot 2.x to 3.0"
  - "Application uses Cassandra, Redis, MongoDB, or other data services"
  - "Configuration contains `spring.data.*` properties"
  - "Spring Data is a classpath dependency"
examples:
  - input: "application.yml with `spring.data.cassandra.contact-points: localhost`"
    output: "application.yml updated to `spring.cassandra.contact-points: localhost`"
    notes: "Cassandra properties moved from spring.data.cassandra.* to spring.cassandra.*"
  - input: "application.properties with `spring.data.redis.host=localhost`"
    output: "application.properties updated to `spring.redis.host=localhost`"
    notes: "Redis properties moved from spring.data.redis.* to spring.redis.*"
---

# Spring Data Properties Prefix Migration

Migrate application properties from `spring.data.*` prefix to service-specific prefixes during Spring Boot 3.0 upgrade. The `spring.data` prefix is now reserved for Spring Data only; data service configurations (Cassandra, Redis, etc.) must be relocated to their respective prefixes (e.g., `spring.cassandra.*`).

## Prompt

Identify all `spring.data.*` properties in your application configuration files. For each data service (Cassandra, Redis, MongoDB, etc.), move its properties to the service-specific prefix. Validate that the application loads without property-not-found errors after migration.

## Objective

Relocate data service configuration properties to correct service-specific prefixes
## Applicable Signals

- Build or startup logs show property-not-found warnings for `spring.data.*` keys
- Application configuration files contain `spring.data.cassandra.*`, `spring.data.redis.*`, or similar prefixes
- Spring Data dependency is declared in pom.xml or build.gradle

## Contraindications

- Application does not use any data services
- No `spring.data.*` properties are present in configuration
- Spring Data is not a dependency

## Workflow Steps

- {'step': 1, 'action': 'Scan configuration files', 'detail': 'Search all application.properties, application.yml, and environment-specific config files for `spring.data.*` prefixes'}
- {'step': 2, 'action': 'Identify data services', 'detail': 'Group properties by service type (Cassandra, Redis, MongoDB, etc.)'}
- {'step': 3, 'action': 'Map to service-specific prefixes', 'detail': 'For each service, determine the correct Spring Boot 3.0 prefix (e.g., `spring.cassandra.*` for Cassandra)'}
- {'step': 4, 'action': 'Relocate properties', 'detail': 'Move property blocks from `spring.data.<service>.*` to `spring.<service>.*`'}
- {'step': 5, 'action': 'Validate configuration', 'detail': 'Start application and verify no property-not-found errors; confirm data service connectivity'}

## Constraints

- Must complete before application startup in Spring Boot 3.0
- All data service properties must be moved; partial migration will cause runtime errors
- Service-specific prefix names must match Spring Boot 3.0 documentation (e.g., `spring.cassandra.*`, not `spring.data.cassandra.*`)

## Cautions

- Verify the correct target prefix for each data service before migration
- Test application startup after property relocation to catch missing or misnamed properties
- Review Spring Data release notes for additional breaking changes in repository interfaces

## Output Contract

- All data service properties successfully migrated to service-specific prefixes; application configuration loads without property-not-found errors; data service connections are established and functional.

## Example Executions

### Example 1

- Input: application.yml with `spring.data.cassandra.contact-points: localhost`
- Output: application.yml updated to `spring.cassandra.contact-points: localhost`
- Notes: Cassandra properties moved from spring.data.cassandra.* to spring.cassandra.*

### Example 2

- Input: application.properties with `spring.data.redis.host=localhost`
- Output: application.properties updated to `spring.redis.host=localhost`
- Notes: Redis properties moved from spring.data.redis.* to spring.redis.*

## Triggers

- Upgrading Spring Boot 2.x to 3.0
- Application uses Cassandra, Redis, MongoDB, or other data services
- Configuration contains `spring.data.*` properties
- Spring Data is a classpath dependency

## Examples

### Example 1

Input:

  application.yml with `spring.data.cassandra.contact-points: localhost`

Output:

  application.yml updated to `spring.cassandra.contact-points: localhost`

Notes:

  Cassandra properties moved from spring.data.cassandra.* to spring.cassandra.*

### Example 2

Input:

  application.properties with `spring.data.redis.host=localhost`

Output:

  application.properties updated to `spring.redis.host=localhost`

Notes:

  Redis properties moved from spring.data.redis.* to spring.redis.*
