---
id: "a63768e2-4dd5-5894-ac7b-0ea5e7a8d0db"
name: "Spring Boot 3.0 Data Access Layer Migration"
description: "Comprehensive workflow to identify, review, and upgrade all data access technologies, database drivers, ORM frameworks, and related dependencies to versions compatible with Spring Boot 3.0. Covers Hibernate, R2DBC, database drivers, migration tools (Flyway, Liquibase), Elasticsearch, and embedded databases."
version: "0.1.0"
tags:
  - "spring-boot-3"
  - "migration"
  - "data-access"
  - "dependencies"
  - "hibernate"
  - "r2dbc"
triggers:
  - "Application uses databases, ORMs, or data access frameworks that require version updates for Spring Boot 3.0"
---

# Spring Boot 3.0 Data Access Layer Migration

Comprehensive workflow to identify, review, and upgrade all data access technologies, database drivers, ORM frameworks, and related dependencies to versions compatible with Spring Boot 3.0. Covers Hibernate, R2DBC, database drivers, migration tools (Flyway, Liquibase), Elasticsearch, and embedded databases.

## Prompt

Review and update all data access technologies and external dependencies in your Spring Boot application to versions compatible with Spring Boot 3.0. This includes database drivers, ORM frameworks, migration tools, and related libraries. Update pom.xml or build.gradle with compatible versions and refactor data access code to align with new driver and ORM APIs.

## Objective

Migrate data access technologies and external dependencies to Spring Boot 3.0-compatible versions
## Applicable Signals

- Application uses relational or NoSQL databases
- ORM frameworks (Hibernate) are in use
- Reactive data access (R2DBC) is configured
- Database migration tools (Flyway, Liquibase) are present
- Elasticsearch or other search engines are integrated
- Custom JDBC drivers or connection pooling is configured

## Contraindications

- Application has no data access layer
- All dependencies are already verified as Spring Boot 3.0 compatible
- Data access layer is being removed or replaced entirely

## Workflow Steps

- {'step': 1, 'action': 'Review data access dependencies', 'detail': 'Identify all ORM, database driver, and data access framework dependencies in pom.xml or build.gradle'}
- {'step': 2, 'action': 'Update Hibernate to 6.1 or later', 'detail': 'Upgrade Hibernate version and review entity annotations and configuration for compatibility'}
- {'step': 3, 'action': 'Update R2DBC to 1.0 or later if used', 'detail': 'Upgrade R2DBC driver and reactive data access configurations'}
- {'step': 4, 'action': 'Update database drivers', 'detail': 'Upgrade MySQL JDBC driver and other database-specific drivers to Spring Boot 3.0-compatible versions'}
- {'step': 5, 'action': 'Update migration tools', 'detail': 'Upgrade Flyway and Liquibase to versions compatible with Spring Boot 3.0'}
- {'step': 6, 'action': 'Update Elasticsearch and search dependencies', 'detail': 'Upgrade Elasticsearch client and template versions if used'}
- {'step': 7, 'action': 'Review data access properties', 'detail': 'Check application.properties or application.yml for Cassandra, Redis, MongoDB, and other data source configurations; update property names and values as needed'}
- {'step': 8, 'action': 'Refactor data access code', 'detail': 'Update data access code to use new ORM and driver APIs; test database connections and queries'}
- {'step': 9, 'action': 'Verify embedded databases', 'detail': 'If using embedded MongoDB or H2, verify versions are compatible and update if necessary'}
- {'step': 10, 'action': 'Test data access layer', 'detail': 'Run integration tests to confirm all database operations, migrations, and queries work correctly'}

## Constraints

- Must review and update all data-related properties in configuration files
- Hibernate must be upgraded to 6.1 or later
- R2DBC must be upgraded to 1.0 or later
- MySQL JDBC driver version must be compatible with Spring Boot 3.0
- Cassandra and Redis property configurations must be reviewed for breaking changes
- Embedded MongoDB dependencies must be updated if used

## Output Contract

- Updated pom.xml or build.gradle with all data access and dependency versions compatible with Spring Boot 3.0
- Data access code refactored and tested
- All database connections, migrations, and queries verified to work correctly

## Triggers

- Application uses databases, ORMs, or data access frameworks that require version updates for Spring Boot 3.0
