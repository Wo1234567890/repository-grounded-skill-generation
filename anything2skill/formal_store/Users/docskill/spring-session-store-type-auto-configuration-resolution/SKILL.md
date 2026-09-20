---
id: "4089d29e-9661-5e67-875e-a5f1c99d7ec9"
name: "Spring Session Store Type Auto-Configuration Resolution"
description: "Migrate Spring Session configuration from deprecated spring.session.store-type property to Spring Boot 3.0 auto-configuration with fixed ordering. Enables selection of SessionRepository implementation via classpath detection or custom bean override."
version: "0.1.0"
tags:
  - "spring-boot-3.0"
  - "spring-session"
  - "auto-configuration"
  - "migration"
  - "session-store"
  - "deprecation"
triggers:
  - "Migrating application to Spring Boot 3.0"
  - "Spring Session is in use"
  - "Multiple session store implementations detected on classpath"
  - "spring.session.store-type property currently configured"
---

# Spring Session Store Type Auto-Configuration Resolution

Migrate Spring Session configuration from deprecated spring.session.store-type property to Spring Boot 3.0 auto-configuration with fixed ordering. Enables selection of SessionRepository implementation via classpath detection or custom bean override.

## Prompt

When migrating to Spring Boot 3.0 with Spring Session:
1. Remove any spring.session.store-type property from configuration files (application.properties or application.yml).
2. Spring Boot will auto-detect and select a SessionRepository implementation using fixed ordering based on classpath availability.
3. If the auto-selected store does not meet requirements, define a custom SessionRepository bean to override auto-configuration and cause it to back off.

## Objective

resolve_session_store_repository_selection
## Applicable Signals

- Spring Boot version upgrade from 2.x to 3.0
- Spring Session dependency present
- Multiple SessionRepository implementations available on classpath (e.g., Redis, JDBC, MongoDB)
- Configuration file contains spring.session.store-type property

## Contraindications

- Single session store implementation available on classpath
- Spring Session not used in application
- No need to override auto-selected store type

## Intervention Moves

- Remove spring.session.store-type property from configuration
- Verify SessionRepository auto-selection via fixed ordering
- Define custom SessionRepository bean if auto-selection is unsuitable

## Workflow Steps

- {'step': 1, 'action': 'Identify all session store implementations on the classpath', 'detail': 'Review dependencies (pom.xml, build.gradle) for Redis, JDBC, MongoDB, or other SessionRepository implementations'}
- {'step': 2, 'action': 'Remove spring.session.store-type property', 'detail': 'Delete or comment out spring.session.store-type from application.properties or application.yml'}
- {'step': 3, 'action': 'Test auto-configuration', 'detail': 'Run application and verify that Spring Boot auto-selects a SessionRepository using fixed ordering'}
- {'step': 4, 'action': 'If auto-selection is unsuitable, define custom SessionRepository bean', 'detail': 'Create a @Configuration class with @Bean method returning the desired SessionRepository implementation'}
- {'step': 5, 'action': 'Verify auto-configuration backs off', 'detail': 'Confirm that custom bean is used and auto-configuration does not override it'}

## Constraints

- spring.session.store-type property is no longer supported and must be removed
- Custom SessionRepository bean definition must be provided if auto-selection is unsuitable
- Fixed ordering is applied; caller cannot configure selection order via properties

## Cautions

- Removing spring.session.store-type without providing a custom bean may result in unexpected store selection if multiple implementations exist
- Custom bean definition must be valid and properly registered in the Spring context

## Output Contract

- SessionRepository bean is successfully auto-configured using fixed ordering, or custom SessionRepository bean is defined and auto-configuration backs off. Application starts without errors related to session store type resolution.

## Triggers

- Migrating application to Spring Boot 3.0
- Spring Session is in use
- Multiple session store implementations detected on classpath
- spring.session.store-type property currently configured
