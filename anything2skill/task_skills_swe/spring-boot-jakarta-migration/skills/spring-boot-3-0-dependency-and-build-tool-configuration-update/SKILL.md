---
id: "76b1b2de-e3bc-54c8-9f27-4177e88a5ed3"
name: "Spring Boot 3.0 Dependency and Build Tool Configuration Update"
description: "Consolidates Maven and Gradle build configuration updates, dependency version management, and plugin compatibility verification for Spring Boot 3.0 migration. Handles removed dependencies (JSON-B, ANTLR 2, RxJava, Hazelcast Hibernate, Ehcache3), relocated packages, and ensures all transitive dependencies resolve without conflicts."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "maven"
  - "gradle"
  - "dependency-management"
  - "build-configuration"
  - "version-upgrade"
triggers:
  - "Updating pom.xml or build.gradle during Spring Boot 3.0 migration"
  - "Build fails due to missing or incompatible dependencies"
  - "Dependency resolution errors after version bump"
examples:
  - input: "pom.xml with Spring Boot 2.7.x and direct dependency on 'javax.json:javax.json-api'"
    output: "pom.xml updated to Spring Boot 3.0.x; javax.json-api removed or replaced with jakarta.json:jakarta.json-api; build succeeds"
    notes: "JSON-B moved from javax to jakarta namespace in Spring Boot 3.0"
  - input: "build.gradle with RxJava 2.x dependency and Spring Boot 2.7.x"
    output: "RxJava dependency removed or updated to 3.x; Spring Boot bumped to 3.0.x; gradle build completes successfully"
    notes: "RxJava is no longer auto-configured in Spring Boot 3.0"
---

# Spring Boot 3.0 Dependency and Build Tool Configuration Update

Consolidates Maven and Gradle build configuration updates, dependency version management, and plugin compatibility verification for Spring Boot 3.0 migration. Handles removed dependencies (JSON-B, ANTLR 2, RxJava, Hazelcast Hibernate, Ehcache3), relocated packages, and ensures all transitive dependencies resolve without conflicts.

## Prompt

Review and update pom.xml or build.gradle to ensure all dependencies and plugins are compatible with Spring Boot 3.0. Identify and remove or replace deprecated libraries. Update Spring Boot to 3.0.x, Spring Framework to 6.0+, and other dependencies to 3.0-compatible releases. Validate dependency resolution and test the build.

## Objective

Ensure build tool configuration and dependency management are compatible with Spring Boot 3.0
## Applicable Signals

- Spring Boot version target is 3.0 or later
- Build tool is Maven or Gradle
- Dependency conflict or resolution failure detected

## Contraindications

- Build configuration is already validated as 3.0-compatible
- Using a build tool other than Maven or Gradle
- Application code migration is not yet complete

## Intervention Moves

- Review current pom.xml or build.gradle and list all direct dependencies with versions
- Identify and remove or replace removed dependencies: JSON-B, ANTLR 2, RxJava, Hazelcast Hibernate, Ehcache3
- Update Spring Boot to 3.0.x and Spring Framework to 6.0+
- Update build plugin versions for Maven and Gradle compatibility
- Run dependency tree analysis to detect conflicts and missing transitive dependencies
- Execute full build test to validate resolution and success

## Workflow Steps

- {'step': 1, 'action': 'Review current pom.xml or build.gradle', 'detail': 'List all direct dependencies and their versions; note any deprecated or removed libraries'}
- {'step': 2, 'action': 'Check for removed dependencies', 'detail': 'Identify and remove or replace: JSON-B, ANTLR 2, RxJava, Hazelcast Hibernate, Ehcache3, and other Spring Boot 2.x-only libraries'}
- {'step': 3, 'action': 'Update dependency versions', 'detail': 'Bump Spring Boot to 3.0.x; update Spring Framework to 6.0+; update other dependencies to 3.0-compatible releases'}
- {'step': 4, 'action': 'Update build plugins', 'detail': 'For Maven: update maven-compiler-plugin, maven-shade-plugin, etc. For Gradle: update plugin versions in build.gradle'}
- {'step': 5, 'action': 'Validate dependency resolution', 'detail': "Run 'mvn dependency:tree' or 'gradle dependencies' to check for conflicts and missing transitive dependencies"}
- {'step': 6, 'action': 'Test build', 'detail': "Execute 'mvn clean install' or 'gradle build' to confirm all dependencies resolve and build succeeds"}

## Constraints

- Must review all direct and transitive dependencies
- Must handle removed dependencies: JSON-B, ANTLR 2, RxJava, Hazelcast Hibernate, Ehcache3
- Plugin versions must be compatible with Spring Boot 3.0 and Java 17+
- Gradle and Maven syntax must remain valid after updates

## Cautions

- Removing dependencies without checking for indirect usage may break runtime behavior
- Plugin version changes may affect build reproducibility; test locally before committing
- Some dependencies may have been relocated to different group IDs; verify artifact coordinates

## Output Contract

- Build succeeds without errors; all dependencies resolve to 3.0-compatible versions; no plugin conflicts or missing transitive dependencies; pom.xml or build.gradle is valid and ready for application code migration

## Example Executions

### Example 1

- Input: pom.xml with Spring Boot 2.7.x and direct dependency on 'javax.json:javax.json-api'
- Output: pom.xml updated to Spring Boot 3.0.x; javax.json-api removed or replaced with jakarta.json:jakarta.json-api; build succeeds
- Notes: JSON-B moved from javax to jakarta namespace in Spring Boot 3.0

### Example 2

- Input: build.gradle with RxJava 2.x dependency and Spring Boot 2.7.x
- Output: RxJava dependency removed or updated to 3.x; Spring Boot bumped to 3.0.x; gradle build completes successfully
- Notes: RxJava is no longer auto-configured in Spring Boot 3.0

## Triggers

- Updating pom.xml or build.gradle during Spring Boot 3.0 migration
- Build fails due to missing or incompatible dependencies
- Dependency resolution errors after version bump

## Examples

### Example 1

Input:

  pom.xml with Spring Boot 2.7.x and direct dependency on 'javax.json:javax.json-api'

Output:

  pom.xml updated to Spring Boot 3.0.x; javax.json-api removed or replaced with jakarta.json:jakarta.json-api; build succeeds

Notes:

  JSON-B moved from javax to jakarta namespace in Spring Boot 3.0

### Example 2

Input:

  build.gradle with RxJava 2.x dependency and Spring Boot 2.7.x

Output:

  RxJava dependency removed or updated to 3.x; Spring Boot bumped to 3.0.x; gradle build completes successfully

Notes:

  RxJava is no longer auto-configured in Spring Boot 3.0
