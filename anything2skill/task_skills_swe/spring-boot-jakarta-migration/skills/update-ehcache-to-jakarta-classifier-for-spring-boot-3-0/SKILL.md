---
id: "dff8b63b-98fa-5d5d-b3b9-28d58301872c"
name: "Update Ehcache to Jakarta Classifier for Spring Boot 3.0"
description: "Update Ehcache dependency declarations in Maven pom.xml and Gradle build.gradle to use the jakarta classifier, ensuring compatibility with Jakarta EE 9 and later when migrating to Spring Boot 3.0+."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "dependency-management"
  - "jakarta-ee"
  - "ehcache"
  - "build-configuration"
triggers:
  - "Spring Boot 2.x to 3.0 migration initiated"
  - "Project uses Ehcache for caching"
  - "Jakarta EE 9+ support required"
---

# Update Ehcache to Jakarta Classifier for Spring Boot 3.0

Update Ehcache dependency declarations in Maven pom.xml and Gradle build.gradle to use the jakarta classifier, ensuring compatibility with Jakarta EE 9 and later when migrating to Spring Boot 3.0+.

## Prompt

When migrating to Spring Boot 3.0 and using Ehcache for caching, update the dependency declarations for ehcache and ehcache-transactions modules to include the jakarta classifier. This ensures compatibility with Jakarta EE 9 and later. Update both pom.xml and build.gradle scripts accordingly.

## Objective

Declare Ehcache dependencies with Jakarta classifier for Spring Boot 3.0+ compatibility
## Applicable Signals

- Ehcache dependency present in pom.xml or build.gradle
- Target Spring Boot version is 3.0 or later
- Build fails with Jakarta EE compatibility errors

## Contraindications

- Using Ehcache 2.x without Jakarta EE requirement
- Spring Boot version is 2.7.x or earlier
- Project does not use Ehcache

## Intervention Moves

- Locate ehcache and ehcache-transactions dependency declarations
- Add jakarta classifier to Maven dependencies or equivalent Gradle configuration
- Apply classifier change consistently across all build files
- Rebuild and verify Jakarta EE compatibility

## Workflow Steps

- {'step': 1, 'action': 'Locate Ehcache dependency declarations', 'detail': 'Find ehcache and ehcache-transactions entries in pom.xml or build.gradle'}
- {'step': 2, 'action': 'Add jakarta classifier', 'detail': 'Append classifier="jakarta" to Maven dependency or equivalent Gradle configuration'}
- {'step': 3, 'action': 'Update all build files', 'detail': 'Apply classifier change to both pom.xml and build.gradle if both exist'}
- {'step': 4, 'action': 'Rebuild and verify', 'detail': 'Run build command and confirm no Jakarta EE conflicts; test application startup'}

## Constraints

- Both ehcache and ehcache-transactions modules must be updated together
- Jakarta classifier must be applied consistently across all build files

## Cautions

- Verify build succeeds after classifier addition to confirm Jakarta EE compatibility
- Test application startup and cache functionality after dependency update

## Output Contract

- pom.xml or build.gradle updated with jakarta-classified Ehcache and ehcache-transactions dependencies; build succeeds without Jakarta EE conflicts; application starts without dependency resolution errors

## Triggers

- Spring Boot 2.x to 3.0 migration initiated
- Project uses Ehcache for caching
- Jakarta EE 9+ support required
