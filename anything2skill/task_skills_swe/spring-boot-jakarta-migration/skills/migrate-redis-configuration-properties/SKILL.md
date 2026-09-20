---
id: "582e5f58-b181-560e-8bcf-25ea98f1c657"
name: "Migrate Redis Configuration Properties"
description: "Update Redis configuration property paths from `spring.redis.*` to `spring.data.redis.*` when upgrading to Spring Boot 3.0. Redis auto-configuration now requires Spring Data to be present on the classpath, necessitating this namespace migration."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "configuration"
  - "redis"
  - "property-migration"
  - "namespace-update"
triggers:
  - "Upgrading Spring Boot application from 2.7.x to 3.0 or later"
  - "Redis auto-configuration is active in the application"
  - "Application uses Spring Data Redis"
---

# Migrate Redis Configuration Properties

Update Redis configuration property paths from `spring.redis.*` to `spring.data.redis.*` when upgrading to Spring Boot 3.0. Redis auto-configuration now requires Spring Data to be present on the classpath, necessitating this namespace migration.

## Prompt

Locate all Redis configuration properties in your application configuration files (application.properties, application.yml, or environment-specific variants). Replace all occurrences of the `spring.redis.` prefix with `spring.data.redis.`. Verify that Spring Data Redis is present on the classpath after the upgrade. Test Redis connectivity to confirm the migration is successful.

## Objective

Update property namespace for Redis configuration
## Applicable Signals

- Spring Boot version upgrade initiated to 3.0+
- Redis dependency present in classpath
- Configuration files contain `spring.redis.*` properties

## Contraindications

- Application does not use Redis
- Spring Data Redis is not on the classpath
- Redis configuration is managed externally (e.g., environment variables only)

## Workflow Steps

- {'step': 1, 'action': 'Identify all Redis configuration properties', 'detail': 'Search application configuration files (application.properties, application.yml, application-*.properties) for all keys starting with spring.redis.'}
- {'step': 2, 'action': 'Replace property namespace', 'detail': 'Update all `spring.redis.*` property keys to `spring.data.redis.*`. Property values and structure remain unchanged.'}
- {'step': 3, 'action': 'Verify Spring Data Redis dependency', 'detail': 'Confirm that Spring Data Redis (spring-boot-starter-data-redis or equivalent) is declared in build configuration (pom.xml or build.gradle).'}
- {'step': 4, 'action': 'Test Redis connectivity', 'detail': 'Start the application and verify that Redis auto-configuration is recognized and Redis connections function correctly.'}

## Constraints

- Spring Data Redis must be present on the classpath for auto-configuration to apply
- All property references must be updated consistently across all configuration sources
- Property names and values remain unchanged; only the namespace prefix changes

## Cautions

- Ensure no hardcoded property name strings in application code reference the old `spring.redis.` prefix
- Test Redis connectivity after migration to confirm configuration is correctly recognized
- If using property profiles or environment-specific configurations, update all variants

## Output Contract

- All Redis configuration properties successfully remapped from `spring.redis.*` to `spring.data.redis.*` in application configuration files. Redis auto-configuration is recognized by Spring Boot 3.0, and Redis connectivity is verified.

## Triggers

- Upgrading Spring Boot application from 2.7.x to 3.0 or later
- Redis auto-configuration is active in the application
- Application uses Spring Data Redis
