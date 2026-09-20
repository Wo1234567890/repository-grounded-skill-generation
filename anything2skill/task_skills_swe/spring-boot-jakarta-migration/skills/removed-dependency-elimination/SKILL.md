---
id: "1265f599-5c76-5427-999f-ee18a3109b1f"
name: "Removed Dependency Elimination"
description: "Remove or replace unsupported dependencies when upgrading to Spring Boot 3.0. Identifies and eliminates Apache ActiveMQ, Atomikos, Ehcache 2, Hazelcast 3, and Apache Solr from build configuration and codebase, then verifies successful removal."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "dependency-management"
  - "build-configuration"
  - "upgrade"
triggers:
  - "Spring Boot 3.0 migration initiated"
  - "Project uses Apache ActiveMQ, Atomikos, Ehcache 2, Hazelcast 3, or Apache Solr"
---

# Removed Dependency Elimination

Remove or replace unsupported dependencies when upgrading to Spring Boot 3.0. Identifies and eliminates Apache ActiveMQ, Atomikos, Ehcache 2, Hazelcast 3, and Apache Solr from build configuration and codebase, then verifies successful removal.

## Prompt

1. Scan pom.xml and build.gradle for removed dependency declarations: Apache ActiveMQ, Atomikos, Ehcache 2, Hazelcast 3, Apache Solr.
2. Remove all matching dependency blocks and transitive references.
3. Search codebase for imports, class references, and configuration that depend on removed libraries.
4. Refactor or delete code that references removed dependencies; replace with Spring Boot 3.0-compatible alternatives if needed.
5. Run build (Maven or Gradle) to confirm no unresolved dependency errors.
6. Verify build artifact is created successfully.

## Objective

Eliminate incompatible dependencies and verify removal
## Applicable Signals

- Dependency resolution failure mentioning removed library
- Build log shows unsupported version of ActiveMQ, Atomikos, Ehcache 2, Hazelcast 3, or Solr
- Code contains imports from org.apache.activemq, com.atomikos, net.sf.ehcache, com.hazelcast, or org.apache.solr

## Contraindications

- Spring Boot version is 2.7.x or earlier
- Project has no dependency on any removed library
- Migration target is not Spring Boot 3.0 or later

## Workflow Steps

- {'step': 1, 'action': 'Identify removed dependencies', 'detail': 'Search pom.xml or build.gradle for declarations of Apache ActiveMQ, Atomikos, Ehcache 2, Hazelcast 3, Apache Solr'}
- {'step': 2, 'action': 'Remove dependency declarations', 'detail': 'Delete matching <dependency> blocks (Maven) or dependency entries (Gradle)'}
- {'step': 3, 'action': 'Scan codebase for references', 'detail': 'Use IDE or grep to find imports and class instantiations from removed libraries'}
- {'step': 4, 'action': 'Refactor or delete code', 'detail': 'Remove or replace code that depends on removed libraries; use Spring Boot 3.0-compatible alternatives'}
- {'step': 5, 'action': 'Build and verify', 'detail': 'Run Maven clean install or Gradle build; confirm no dependency resolution errors and artifact is created'}

## Constraints

- All removed dependencies must be completely removed from build files before proceeding to next migration phase
- Codebase must be scanned for all transitive and direct references
- Build must complete without dependency resolution errors

## Cautions

- Removing dependencies may break runtime behavior if code still references them; refactor code before removal
- Some applications may require alternative libraries; consult Spring Boot 3.0 migration guide for replacements
- Ehcache 3 with jakarta classifier is the supported replacement for Ehcache 2

## Output Contract

- All removed dependencies are deleted from build files
- Codebase contains no references to removed libraries
- Build completes successfully without dependency resolution errors
- Build artifact is generated

## Triggers

- Spring Boot 3.0 migration initiated
- Project uses Apache ActiveMQ, Atomikos, Ehcache 2, Hazelcast 3, or Apache Solr
