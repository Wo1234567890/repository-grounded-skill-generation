---
id: "29a11ed8-ec21-523b-b958-fe7cd7c939c6"
name: "Resolve Spring Boot 3 Dependency Management Gaps"
description: "Identify and declare explicit versions for libraries whose dependency management was removed in Spring Boot 3 (JSON-B/Apache Johnzon, ANTLR 2, RxJava 1.x/2.x, Hazelcast Hibernate). Ensures build compatibility and prevents resolution errors during migration."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "dependency-management"
  - "maven"
  - "gradle"
  - "version-declaration"
  - "jakarta-ee-10"
triggers:
  - "Upgrading Spring Boot project to version 3.x"
  - "Build fails with missing dependency management entries"
  - "Project uses JSON-B, ANTLR 2, RxJava 1.x/2.x, or Hazelcast Hibernate"
---

# Resolve Spring Boot 3 Dependency Management Gaps

Identify and declare explicit versions for libraries whose dependency management was removed in Spring Boot 3 (JSON-B/Apache Johnzon, ANTLR 2, RxJava 1.x/2.x, Hazelcast Hibernate). Ensures build compatibility and prevents resolution errors during migration.

## Prompt

Review your project's pom.xml or build.gradle for usage of JSON-B (Apache Johnzon), ANTLR 2, RxJava 1.x or 2.x, or Hazelcast Hibernate. For each library found, add an explicit version declaration to your dependency management section. For JSON-B, migrate to Eclipse Yasson if possible; for RxJava, upgrade to version 3. For ANTLR 2 and Hazelcast Hibernate, specify a version that meets your application needs.

## Objective

Resolve dependency management gaps introduced by Spring Boot 3 removals
## Applicable Signals

- Spring Boot 3.x migration initiated
- Dependency resolution errors for removed managed libraries
- Pre-migration audit of pom.xml or build.gradle

## Contraindications

- Project does not use any of the affected libraries (JSON-B, ANTLR 2, RxJava 1.x/2.x, Hazelcast Hibernate)
- Already on Spring Boot 3.x with all dependencies explicitly declared

## Intervention Moves

- Audit project dependencies for affected libraries
- Add explicit version declarations in dependencyManagement (Maven) or constraints (Gradle)
- Validate version compatibility with Spring Boot 3.x and Jakarta EE 10
- Execute build validation

## Workflow Steps

- {'step': 1, 'action': 'Audit project dependencies', 'detail': 'Search pom.xml or build.gradle for usage of org.apache.johnzon, antlr:antlr, io.reactivex (1.x or 2.x), or com.hazelcast:hazelcast-hibernate'}
- {'step': 2, 'action': 'Identify affected libraries', 'detail': 'List all found dependencies and their current versions'}
- {'step': 3, 'action': 'Add explicit version declarations', 'detail': 'For each affected library, add a version tag in the dependencyManagement section (Maven) or constraints block (Gradle)'}
- {'step': 4, 'action': 'Validate compatibility', 'detail': 'Ensure declared versions are compatible with Spring Boot 3.x and Jakarta EE 10'}
- {'step': 5, 'action': 'Test build', 'detail': 'Run mvn clean install or gradle build to verify dependency resolution'}

## Constraints

- Must audit all transitive dependencies to identify affected libraries
- Version declarations must be compatible with Spring Boot 3.x and Jakarta EE 10
- RxJava 1.x and 2.x have no direct upgrade path; RxJava 3 is the replacement

## Cautions

- Apache Johnzon (JSON-B) is no longer managed; Eclipse Yasson is the preferred alternative
- ANTLR 2 is legacy; consider upgrading to ANTLR 4 if feasible
- Hazelcast Hibernate integration may require additional configuration changes beyond version declaration

## Output Contract

- Updated pom.xml or build.gradle with explicit version declarations for all previously managed but now removed dependencies
- Successful build without dependency resolution errors
- Documented version choices for each affected library

## Triggers

- Upgrading Spring Boot project to version 3.x
- Build fails with missing dependency management entries
- Project uses JSON-B, ANTLR 2, RxJava 1.x/2.x, or Hazelcast Hibernate
