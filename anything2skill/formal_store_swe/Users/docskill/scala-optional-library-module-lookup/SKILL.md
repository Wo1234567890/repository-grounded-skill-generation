---
id: "2d1cdb6d-c06f-5d28-b1ea-74ede162924c"
name: "Scala Optional Library Module Lookup"
description: "Canonical reference skill for identifying removed dependency management entries in Spring Boot 3 and determining which dependencies require explicit version declarations. Covers JSON-B (Apache Johnzon → Eclipse Yasson), ANTLR 2, RxJava (1.x/2.x → 3.x), and Hazelcast Hibernate removal."
version: "0.1.1"
tags:
  - "spring-boot"
  - "spring-boot-3"
  - "migration"
  - "dependency-management"
  - "maven"
  - "gradle"
triggers:
  - "Setting up Scala project dependencies"
  - "Configuring classpath for Scala runtime"
  - "Verifying available standard library modules"
---

# Scala Optional Library Module Lookup

Canonical reference skill for identifying removed dependency management entries in Spring Boot 3 and determining which dependencies require explicit version declarations. Covers JSON-B (Apache Johnzon → Eclipse Yasson), ANTLR 2, RxJava (1.x/2.x → 3.x), and Hazelcast Hibernate removal.

## Prompt

When planning or auditing a Spring Boot 3 migration, consult this reference to identify which dependencies no longer have managed versions in Spring Boot 3 and which require explicit version declarations in your project. Use this to cross-check your dependency tree against known removals and compatibility changes.

## Objective

Provide lookup reference for dependency management changes during Spring Boot 3 migration
## Applicable Signals

- Planning Spring Boot 3 migration
- Auditing project dependencies for compatibility
- Troubleshooting missing dependency management errors
- Reviewing build configuration for version conflicts

## Contraindications

- Already completed Spring Boot 3 migration
- Using only Gradle without Maven (partial applicability)

## Workflow Steps

- Identify dependencies in project that may be affected by Spring Boot 3 changes
- Cross-reference against known removals: JSON-B, ANTLR 2, RxJava, Hazelcast Hibernate
- Determine which dependencies require explicit version declarations
- Consult reference to confirm compatibility status and migration path

## Constraints

- Reference is specific to Spring Boot 3.0+ dependency management changes
- Does not cover transitive dependency resolution or version conflict resolution strategies

## Output Contract

- Caller identifies affected dependencies in their project and determines which require explicit version declarations
- Reference consulted to confirm compatibility status and migration path for each affected dependency

## Triggers

- Setting up Scala project dependencies
- Configuring classpath for Scala runtime
- Verifying available standard library modules
