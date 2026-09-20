---
id: "1f0b4cfa-7c7c-5eb8-9633-dceefe1e05a7"
name: "Migrate SAML2 Relying Party Configuration to Asserting-Party Structure"
description: "Replace deprecated SAML2 relying party identity-provider properties with new asserting-party properties structure when upgrading to Spring Security 6.0 in Spring Boot 3.0."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "spring-security-6"
  - "saml2"
  - "configuration-migration"
  - "property-schema"
triggers:
  - "Upgrading application to Spring Boot 3.0 or Spring Security 6.0"
  - "Application uses SAML2 relying party authentication"
  - "Configuration contains `spring.security.saml2.relyingparty.registration.{id}.identity-provider` properties"
---

# Migrate SAML2 Relying Party Configuration to Asserting-Party Structure

Replace deprecated SAML2 relying party identity-provider properties with new asserting-party properties structure when upgrading to Spring Security 6.0 in Spring Boot 3.0.

## Prompt

Locate all `spring.security.saml2.relyingparty.registration.{id}.identity-provider.*` properties in your application configuration (YAML, properties, or Java config). Replace each with the equivalent `spring.security.saml2.relyingparty.registration.{id}.asserting-party.*` property. Verify SAML2 authentication flow completes after migration.

## Objective

update_saml2_property_structure
## Applicable Signals

- Spring Security version upgrade from <6.0 to 6.0+
- SAML2 relying party configuration present in application
- Deprecation warnings referencing identity-provider properties

## Contraindications

- Application does not use SAML2 authentication
- No `identity-provider` properties exist in current configuration
- Application is not upgrading to Spring Security 6.0

## Workflow Steps

- {'step': 1, 'action': 'Identify all SAML2 configuration locations', 'detail': 'Search application configuration files (application.yml, application.properties, @Configuration classes) for `spring.security.saml2.relyingparty.registration.{id}.identity-provider`'}
- {'step': 2, 'action': 'Map old identity-provider properties to new asserting-party structure', 'detail': 'Replace `identity-provider.*` with `asserting-party.*` for each registration ID; consult Spring Security 6.0 migration guide for property name mappings'}
- {'step': 3, 'action': 'Update configuration files', 'detail': 'Apply property changes to all configuration sources (YAML, properties, Java config)'}
- {'step': 4, 'action': 'Validate SAML2 authentication', 'detail': 'Start application and test SAML2 relying party login flow; verify IdP communication and token exchange succeed'}

## Constraints

- Must complete property migration before application startup
- All registration IDs must be updated consistently
- Asserting-party structure must match Spring Security 6.0 schema

## Cautions

- Property name changes are breaking; old properties will not be recognized
- Test SAML2 authentication flow after migration to ensure IdP communication succeeds

## Output Contract

- All `spring.security.saml2.relyingparty.registration.{id}.identity-provider.*` properties successfully replaced with `asserting-party.*` equivalents
- SAML2 authentication flow completes without errors
- Application starts without deprecation warnings for SAML2 properties

## Triggers

- Upgrading application to Spring Boot 3.0 or Spring Security 6.0
- Application uses SAML2 relying party authentication
- Configuration contains `spring.security.saml2.relyingparty.registration.{id}.identity-provider` properties
