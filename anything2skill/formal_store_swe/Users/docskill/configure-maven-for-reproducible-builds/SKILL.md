---
id: "9806488c-6fd5-5a4d-8932-6fe7569fa9a5"
name: "Configure Maven for Reproducible Builds"
description: "Review and selectively override default versions for Flyway, Liquibase, Hibernate, and R2DBC drivers when upgrading to Spring Boot 3.0 to address known compatibility issues and ensure database framework stability."
version: "0.1.1"
tags:
  - "spring-boot-3-migration"
  - "dependency-management"
  - "database-frameworks"
  - "version-override"
  - "compatibility"
  - "flyway"
triggers:
  - "Initiating a new Maven project requiring build consistency"
  - "Enforcing build consistency across CI/CD pipelines"
  - "Preparing artifacts for release or distribution"
examples:
  - input: "Application uses Liquibase and encounters migration errors after Spring Boot 3.0 upgrade"
    output: "Override Liquibase version from 4.17.x to 4.16.x in pom.xml <properties>; rebuild and re-run migrations; confirm success"
    notes: "Addresses reported 4.17.x compatibility issues"
  - input: "Application uses Hibernate and Spring Data JPA; dependency group ID changed"
    output: "Update Hibernate dependency from org.hibernate to org.hibernate.orm; review Hibernate 6.1 migration guide for breaking changes; test ORM initialization"
    notes: "Reflects Spring Boot 3.0 dependency management update"
  - input: "Application uses MySQL JDBC driver"
    output: "Update MySQL JDBC driver coordinates from mysql:mysql-connector-java to com.mysql:mysql-connector-j in build configuration; rebuild and test database connectivity"
    notes: "Coordinates changed in Spring Boot 3.0"
---

# Configure Maven for Reproducible Builds

Review and selectively override default versions for Flyway, Liquibase, Hibernate, and R2DBC drivers when upgrading to Spring Boot 3.0 to address known compatibility issues and ensure database framework stability.

## Prompt

When upgrading to Spring Boot 3.0, validate the default versions of database frameworks against your application's requirements and known issues. For each framework in use, check the release notes, identify any reported problems, and override versions in your build configuration if needed. Test that the application builds and database migrations execute without errors.

## Objective

Validate and adjust database framework versions for Spring Boot 3.0 compatibility
## Applicable Signals

- Spring Boot version target is 3.0 or later
- pom.xml or build.gradle declares Flyway, Liquibase, Hibernate, or R2DBC dependencies
- Database migration or ORM initialization errors in logs

## Contraindications

- Application does not use any of these database frameworks
- Database dependency versions are already explicitly pinned and tested
- No database layer present in application

## Intervention Moves

- Override Liquibase version from 4.17.x to 4.16.x if compatibility issues detected
- Update Hibernate dependency group ID from org.hibernate to org.hibernate.orm
- Verify R2DBC driver artifact IDs match database-specific coordinates
- Update MySQL JDBC driver coordinates from mysql:mysql-connector-java to com.mysql:mysql-connector-j

## Workflow Steps

- {'step': 1, 'action': 'Identify database frameworks in use', 'detail': 'Check pom.xml or build.gradle for Flyway, Liquibase, Hibernate, and R2DBC dependencies'}
- {'step': 2, 'action': 'Review default versions in Spring Boot 3.0', 'detail': 'Flyway 9.0, Liquibase 4.17.x, Hibernate 6.1; note any known issues'}
- {'step': 3, 'action': 'Consult release notes and migration guides', 'detail': 'Check official documentation for breaking changes and compatibility warnings'}
- {'step': 4, 'action': 'Determine override requirements', 'detail': 'Decide whether to accept defaults or pin alternative versions based on application needs'}
- {'step': 5, 'action': 'Apply version overrides in build configuration', 'detail': 'Update pom.xml <properties> or build.gradle version declarations'}
- {'step': 6, 'action': 'Build and test', 'detail': 'Verify application builds successfully and database migrations execute without errors'}

## Constraints

- Must review official release notes for each framework before overriding
- Version overrides must be tested in a non-production environment first
- Overrides should be documented with rationale and issue tracking reference

## Cautions

- Liquibase 4.17.x has reported compatibility issues; consider downgrade if affected
- Hibernate 6.1 introduces breaking changes; review migration guide thoroughly
- R2DBC driver coordinates and versions vary by database; verify correct artifact IDs
- MySQL JDBC driver coordinates changed from mysql:mysql-connector-java to com.mysql:mysql-connector-j

## Output Contract

- Dependency versions verified or overridden in build configuration
- Application builds without dependency conflicts
- Database migrations and ORM initialization complete successfully
- No version-related runtime errors

## Example Executions

### Example 1

- Input: Application uses Liquibase and encounters migration errors after Spring Boot 3.0 upgrade
- Output: Override Liquibase version from 4.17.x to 4.16.x in pom.xml <properties>; rebuild and re-run migrations; confirm success
- Notes: Addresses reported 4.17.x compatibility issues

### Example 2

- Input: Application uses Hibernate and Spring Data JPA; dependency group ID changed
- Output: Update Hibernate dependency from org.hibernate to org.hibernate.orm; review Hibernate 6.1 migration guide for breaking changes; test ORM initialization
- Notes: Reflects Spring Boot 3.0 dependency management update

### Example 3

- Input: Application uses MySQL JDBC driver
- Output: Update MySQL JDBC driver coordinates from mysql:mysql-connector-java to com.mysql:mysql-connector-j in build configuration; rebuild and test database connectivity
- Notes: Coordinates changed in Spring Boot 3.0

## Triggers

- Initiating a new Maven project requiring build consistency
- Enforcing build consistency across CI/CD pipelines
- Preparing artifacts for release or distribution

## Examples

### Example 1

Input:

  Application uses Liquibase and encounters migration errors after Spring Boot 3.0 upgrade

Output:

  Override Liquibase version from 4.17.x to 4.16.x in pom.xml <properties>; rebuild and re-run migrations; confirm success

Notes:

  Addresses reported 4.17.x compatibility issues

### Example 2

Input:

  Application uses Hibernate and Spring Data JPA; dependency group ID changed

Output:

  Update Hibernate dependency from org.hibernate to org.hibernate.orm; review Hibernate 6.1 migration guide for breaking changes; test ORM initialization

Notes:

  Reflects Spring Boot 3.0 dependency management update

### Example 3

Input:

  Application uses MySQL JDBC driver

Output:

  Update MySQL JDBC driver coordinates from mysql:mysql-connector-java to com.mysql:mysql-connector-j in build configuration; rebuild and test database connectivity

Notes:

  Coordinates changed in Spring Boot 3.0
