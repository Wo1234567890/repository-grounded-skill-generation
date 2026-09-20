---
id: "09aa55aa-db0f-5da2-8ffd-1f0419fa5518"
name: "Jakarta EE Package Migration"
description: "Systematic migration of javax.* imports to jakarta.* packages when upgrading to Spring Boot 3.0 and Jakarta EE 10. Updates dependency coordinates and replaces import statements to align with Jakarta EE 10 specifications (Servlet 6.0, JPA 3.1)."
version: "0.1.0"
tags:
  - "spring-boot-3.0"
  - "jakarta-ee-10"
  - "package-migration"
  - "dependency-upgrade"
  - "automated-refactoring"
triggers:
  - "Upgrading Spring Boot application to version 3.0 or later; project contains javax.* imports or dependencies"
---

# Jakarta EE Package Migration

Systematic migration of javax.* imports to jakarta.* packages when upgrading to Spring Boot 3.0 and Jakarta EE 10. Updates dependency coordinates and replaces import statements to align with Jakarta EE 10 specifications (Servlet 6.0, JPA 3.1).

## Prompt

When upgrading a Spring Boot application to version 3.0 or later, migrate all javax.* package imports and dependencies to jakarta.* equivalents. Update dependency coordinates to Jakarta EE 10 versions. Use automated tooling (OpenRewrite recipes, Spring Boot Migrator, or IntelliJ IDEA migration support) to identify and replace import statements. Verify that all javax.* references are replaced and the project compiles without import-related errors.

## Objective

Complete javax-to-jakarta package namespace migration for Spring Boot 3.0 upgrade
## Applicable Signals

- Spring Boot upgrade to version 3.0 or later initiated
- Project contains javax.* imports or dependencies
- Jakarta EE 10 adoption required

## Contraindications

- Application already uses jakarta.* packages exclusively
- Targeting Spring Boot 2.x or earlier versions
- Project dependencies do not include Jakarta EE specifications

## Intervention Moves

- Run OpenRewrite recipes to identify and replace javax.* imports
- Use Spring Boot Migrator project for systematic migration
- Leverage IntelliJ IDEA migration support for import statement updates
- Update dependency coordinates to Jakarta EE 10 versions
- Verify compilation and resolve any remaining import conflicts

## Workflow Steps

- {'step': 1, 'action': 'Identify all javax.* imports and dependencies in the project'}
- {'step': 2, 'action': 'Select and apply automated migration tool (OpenRewrite, Spring Boot Migrator, or IntelliJ IDEA)'}
- {'step': 3, 'action': 'Update dependency coordinates to Jakarta EE 10 versions'}
- {'step': 4, 'action': 'Verify all javax.* imports are replaced with jakarta.* equivalents'}
- {'step': 5, 'action': 'Compile project and resolve any remaining import-related errors'}

## Constraints

- Migration must be completed before upgrading to Spring Boot 3.0
- All javax.* imports must be replaced; partial migration will cause compilation errors
- Dependency coordinates must align with Jakarta EE 10 specifications

## Output Contract

- All javax.* imports replaced with jakarta.* equivalents
- Project compiles without import-related errors
- Dependency coordinates updated to Jakarta EE 10 versions (Servlet 6.0, JPA 3.1)
- Ready for Spring Boot 3.0 upgrade

## Triggers

- Upgrading Spring Boot application to version 3.0 or later; project contains javax.* imports or dependencies
