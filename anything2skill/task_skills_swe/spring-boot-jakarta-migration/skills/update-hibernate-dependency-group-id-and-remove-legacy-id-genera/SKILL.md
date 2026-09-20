---
id: "f6aea865-8786-54e6-95ca-fd542067ce9d"
name: "Update Hibernate Dependency Group ID and Remove Legacy ID Generator Configuration"
description: "Update Hibernate dependency coordinates from the old group ID to `org.hibernate.orm` and remove the deprecated `spring.jpa.hibernate.use-new-id-generator-mappings` configuration property when upgrading to Spring Boot 3.0 with Hibernate 6.1."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "hibernate-6-upgrade"
  - "dependency-management"
  - "configuration-removal"
triggers:
  - "Upgrading to Spring Boot 3.0"
  - "Using spring-boot-starter-data-jpa"
  - "Targeting Hibernate 6.1 or later"
examples:
  - input: "Maven pom.xml with Hibernate dependency using old group ID and application.properties containing `spring.jpa.hibernate.use-new-id-generator-mappings=true`"
    output: "pom.xml updated with `<groupId>org.hibernate.orm</groupId>` for Hibernate artifacts; `spring.jpa.hibernate.use-new-id-generator-mappings` property removed; application starts successfully with Hibernate 6.1"
    notes: "Typical scenario for Spring Boot 2.x to 3.0 migration with JPA"
---

# Update Hibernate Dependency Group ID and Remove Legacy ID Generator Configuration

Update Hibernate dependency coordinates from the old group ID to `org.hibernate.orm` and remove the deprecated `spring.jpa.hibernate.use-new-id-generator-mappings` configuration property when upgrading to Spring Boot 3.0 with Hibernate 6.1.

## Prompt

When upgrading to Spring Boot 3.0 with JPA support: (1) Update all Hibernate dependencies in your build configuration to use the new `org.hibernate.orm` group ID instead of the previous group ID. (2) Locate and remove the `spring.jpa.hibernate.use-new-id-generator-mappings` property from your application configuration files (application.properties or application.yml), as Hibernate 6.1 no longer supports this legacy setting. (3) Verify that your application compiles and that JPA entities initialize correctly after the changes.

## Objective

Align Hibernate dependencies and remove unsupported configuration
## Applicable Signals

- Build configuration contains Hibernate dependencies with old group ID
- Application configuration includes `spring.jpa.hibernate.use-new-id-generator-mappings` property
- Migration guide review identifies Hibernate version bump to 6.1

## Contraindications

- Application does not use JPA or Hibernate
- Hibernate version is pinned below 6.0
- Custom Hibernate configuration that explicitly requires legacy ID generator mappings

## Workflow Steps

- {'step': 1, 'action': 'Locate Hibernate dependencies in build configuration', 'detail': 'Search for Hibernate artifact declarations in pom.xml (Maven) or build.gradle (Gradle)'}
- {'step': 2, 'action': 'Update group ID to org.hibernate.orm', 'detail': 'Replace old Hibernate group ID with `org.hibernate.orm` for all Hibernate artifacts'}
- {'step': 3, 'action': 'Remove deprecated configuration property', 'detail': 'Delete `spring.jpa.hibernate.use-new-id-generator-mappings` from application.properties or application.yml'}
- {'step': 4, 'action': 'Verify compilation and initialization', 'detail': 'Rebuild project and start application to confirm JPA entities initialize without errors'}

## Constraints

- Must update all Hibernate dependencies consistently across build configuration
- Property removal must be completed before application startup
- JPA entity initialization must succeed after changes

## Cautions

- Removing the configuration property is mandatory; Hibernate 6.1 does not support the legacy setting
- Verify all transitive Hibernate dependencies use the new group ID
- Test entity ID generation behavior after upgrade to ensure correct mapping strategy

## Output Contract

- Hibernate dependencies successfully updated to `org.hibernate.orm` group ID; deprecated `spring.jpa.hibernate.use-new-id-generator-mappings` property removed from configuration; application compiles and JPA entities initialize correctly on startup.

## Example Executions

### Example 1

- Input: Maven pom.xml with Hibernate dependency using old group ID and application.properties containing `spring.jpa.hibernate.use-new-id-generator-mappings=true`
- Output: pom.xml updated with `<groupId>org.hibernate.orm</groupId>` for Hibernate artifacts; `spring.jpa.hibernate.use-new-id-generator-mappings` property removed; application starts successfully with Hibernate 6.1
- Notes: Typical scenario for Spring Boot 2.x to 3.0 migration with JPA

## Triggers

- Upgrading to Spring Boot 3.0
- Using spring-boot-starter-data-jpa
- Targeting Hibernate 6.1 or later

## Examples

### Example 1

Input:

  Maven pom.xml with Hibernate dependency using old group ID and application.properties containing `spring.jpa.hibernate.use-new-id-generator-mappings=true`

Output:

  pom.xml updated with `<groupId>org.hibernate.orm</groupId>` for Hibernate artifacts; `spring.jpa.hibernate.use-new-id-generator-mappings` property removed; application starts successfully with Hibernate 6.1

Notes:

  Typical scenario for Spring Boot 2.x to 3.0 migration with JPA
