---
id: "7f96f427-6c72-5b60-acb0-9f538df7f06b"
name: "Update MySQL JDBC Driver Coordinates"
description: "Change MySQL JDBC driver dependency coordinates from `mysql:mysql-connector-java` to `com.mysql:mysql-connector-j` when upgrading to Spring Boot 3.0."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "dependency-update"
  - "mysql"
  - "jdbc-driver"
  - "build-configuration"
triggers:
  - "Upgrading application to Spring Boot 3.0"
  - "Application uses MySQL JDBC driver"
  - "Build configuration contains mysql:mysql-connector-java dependency"
---

# Update MySQL JDBC Driver Coordinates

Change MySQL JDBC driver dependency coordinates from `mysql:mysql-connector-java` to `com.mysql:mysql-connector-j` when upgrading to Spring Boot 3.0.

## Prompt

When upgrading to Spring Boot 3.0, the MySQL JDBC driver coordinates have changed. Update your build configuration to use the new group and artifact ID. Locate the MySQL driver dependency declaration and replace the old coordinates with the new ones. Verify the application can connect to the MySQL database after the update.

## Objective

Update MySQL driver artifact coordinates
## Applicable Signals

- Spring Boot version target is 3.0 or later
- MySQL database is in use
- Dependency management file (pom.xml, build.gradle, etc.) is accessible

## Contraindications

- Application does not use MySQL database
- Application uses a different database driver
- MySQL driver is not declared as a direct dependency

## Workflow Steps

- {'step': 1, 'action': 'Locate MySQL JDBC driver dependency', 'detail': 'Find the dependency declaration in build configuration (pom.xml for Maven, build.gradle for Gradle, etc.)'}
- {'step': 2, 'action': 'Replace old coordinates', 'detail': 'Change from group:artifact `mysql:mysql-connector-java` to `com.mysql:mysql-connector-j`'}
- {'step': 3, 'action': 'Update version if needed', 'detail': 'Ensure the version is compatible with Spring Boot 3.0 and your application requirements'}
- {'step': 4, 'action': 'Rebuild and test', 'detail': 'Rebuild the application and verify MySQL database connectivity works correctly'}

## Constraints

- Build configuration must be valid and parseable
- New coordinates must be available in the configured Maven/Gradle repository
- Application must be able to connect to MySQL database after update

## Cautions

- Ensure no other dependencies explicitly reference the old mysql:mysql-connector-java coordinates
- Test database connectivity after updating coordinates
- Review any custom driver configuration that may reference the old artifact ID

## Output Contract

- MySQL JDBC driver dependency coordinates successfully updated in build configuration
- Application builds without dependency resolution errors
- Application establishes connection to MySQL database

## Triggers

- Upgrading application to Spring Boot 3.0
- Application uses MySQL JDBC driver
- Build configuration contains mysql:mysql-connector-java dependency
