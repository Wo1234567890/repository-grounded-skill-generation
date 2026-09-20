---
id: "6d2d46bd-7e4b-58b5-bac1-1f96a73a1854"
name: "Spring Security Dispatcher Type Configuration"
description: "Configure Spring Security 6.0 filter dispatch types in Spring Boot 3.0 to ensure authorization is applied to all servlet dispatch types via the `spring.security.filter.dispatcher-types` property."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "spring-security-6"
  - "servlet-configuration"
  - "dispatcher-types"
  - "authorization"
triggers:
  - "Migrating servlet-based Spring Boot application from 2.7.x to 3.0"
  - "Spring Security 6.0 is present in the dependency tree"
  - "Authorization behavior changes are observed after upgrade"
---

# Spring Security Dispatcher Type Configuration

Configure Spring Security 6.0 filter dispatch types in Spring Boot 3.0 to ensure authorization is applied to all servlet dispatch types via the `spring.security.filter.dispatcher-types` property.

## Prompt

In Spring Boot 3.0 with Spring Security 6.0, the security filter must be explicitly configured to apply authorization to every dispatch type in servlet applications. Set the `spring.security.filter.dispatcher-types` property to specify which dispatch types (REQUEST, FORWARD, INCLUDE, ERROR) should trigger the security filter. This aligns with Spring Security 6.0's stricter authorization model.

## Objective

Align Spring Security filter dispatch behavior with Spring Boot 3.0 and Spring Security 6.0 defaults
## Applicable Signals

- Spring Boot 3.0 upgrade in progress
- Spring Security 6.0 dependency detected
- Servlet-based application (not pure WebFlux)

## Contraindications

- Application uses reactive WebFlux without servlet dispatch types
- Spring Security is not present in the project
- Application is already running Spring Boot 3.0 with correct dispatcher-types configuration

## Intervention Moves

- Identify current dispatcher-types configuration in application.properties or application.yml
- Add or update spring.security.filter.dispatcher-types property with required dispatch types
- Verify Spring Security filter is invoked for all configured dispatch types

## Workflow Steps

- {'step': 1, 'action': 'Identify current dispatcher-types configuration', 'detail': 'Check if `spring.security.filter.dispatcher-types` is already set in application.properties or application.yml'}
- {'step': 2, 'action': 'Set dispatcher-types property', 'detail': 'Add or update `spring.security.filter.dispatcher-types=REQUEST,FORWARD,INCLUDE,ERROR` (or subset as needed) in application configuration'}
- {'step': 3, 'action': 'Verify Spring Security filter is invoked', 'detail': 'Test that the security filter is called for all configured dispatch types by enabling debug logging or running integration tests'}

## Constraints

- Property must be set in application.properties or application.yml before Spring Security filter initialization
- Only applicable to servlet-based applications; reactive applications do not use dispatcher types
- Requires Spring Boot 3.0 or later and Spring Security 6.0 or later

## Cautions

- Removing or misconfiguring this property may result in authorization not being applied to certain dispatch types (FORWARD, INCLUDE, ERROR)
- Test all dispatch paths (forward, include, error handling) after configuration to ensure security is applied

## Output Contract

- Property `spring.security.filter.dispatcher-types` is set in application configuration and Spring Security filter is invoked for all required dispatch types; authorization is consistently applied across REQUEST, FORWARD, INCLUDE, and ERROR dispatch types as configured.

## Triggers

- Migrating servlet-based Spring Boot application from 2.7.x to 3.0
- Spring Security 6.0 is present in the dependency tree
- Authorization behavior changes are observed after upgrade
