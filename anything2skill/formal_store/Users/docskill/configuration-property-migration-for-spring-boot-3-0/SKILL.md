---
id: "2da653be-d18d-513b-88b4-d17b59cc285b"
name: "Configuration Property Migration for Spring Boot 3.0"
description: "Identify and update deprecated or relocated configuration properties during Spring Boot 3.0 upgrade. Handles property schema changes across subsystems (Redis, data access, Spring Security) to ensure application configuration aligns with Spring Boot 3.0 requirements."
version: "0.1.0"
tags:
  - "spring-boot-3.0"
  - "migration"
  - "configuration"
  - "property-mapping"
  - "deprecation-handling"
triggers:
  - "Upgrading application from Spring Boot 2.x to 3.0"
  - "Reviewing application.properties or application.yml files during migration"
  - "Encountering configuration warnings or property-not-found errors after upgrade"
examples:
  - input: "application.yml contains: spring.redis.host: localhost"
    output: "Updated to: spring.data.redis.host: localhost"
    notes: "Redis properties moved from spring.redis.* to spring.data.redis.* namespace"
  - input: "application.properties contains: spring.security.saml2.relyingparty.registration.myapp.identity-provider.entity-id=..."
    output: "Updated to: spring.security.saml2.relyingparty.registration.myapp.asserting-party.entity-id=..."
    notes: "SAML2 identity-provider properties replaced with asserting-party"
---

# Configuration Property Migration for Spring Boot 3.0

Identify and update deprecated or relocated configuration properties during Spring Boot 3.0 upgrade. Handles property schema changes across subsystems (Redis, data access, Spring Security) to ensure application configuration aligns with Spring Boot 3.0 requirements.

## Prompt

Review application.properties and application.yml files for deprecated or relocated properties. Cross-reference against Spring Boot 3.0 migration guide sections for Redis, data access, and Spring Security. Replace old property paths with new ones. Validate that all property keys match the new schema and that no deprecated keys remain. Test application startup to confirm configuration is accepted without warnings.

## Objective

migrate_configuration_properties
## Applicable Signals

- Spring Boot 3.0 upgrade in progress
- External property files present (application.properties or application.yml)
- Configuration subsystems in use: Redis, data access (JPA, R2DBC), or Spring Security

## Contraindications

- Application uses only hardcoded configuration with no external property files
- No Spring Data Redis, JPA, or Spring Security dependencies present

## Workflow Steps

- {'step': 1, 'action': 'Locate all external configuration files', 'detail': 'Identify application.properties and application.yml files in the project'}
- {'step': 2, 'action': 'Search for deprecated property patterns', 'detail': 'Scan for old property keys: spring.redis.*, spring.security.saml2.relyingparty.registration.{id}.identity-provider, spring.jpa.hibernate.use-new-id-generator-mappings'}
- {'step': 3, 'action': 'Map old properties to new schema', 'detail': 'Replace spring.redis.* with spring.data.redis.*; replace identity-provider with asserting-party; remove use-new-id-generator-mappings'}
- {'step': 4, 'action': 'Validate property syntax and completeness', 'detail': 'Ensure all property keys match Spring Boot 3.0 schema; verify no deprecated keys remain'}
- {'step': 5, 'action': 'Test application startup', 'detail': 'Start application and confirm no configuration warnings or property-not-found errors occur'}

## Constraints

- Property file syntax must be valid YAML or properties format
- All property replacements must follow Spring Boot 3.0 schema exactly
- Application must start without configuration-related warnings after migration

## Cautions

- Some property relocations (e.g., spring.redis.* to spring.data.redis.*) require Spring Data to be on the classpath
- SAML2 configuration changes are breaking; old identity-provider properties will not be recognized
- Verify dependent libraries (Hibernate, Flyway, Liquibase) versions align with Spring Boot 3.0 defaults

## Output Contract

- All deprecated properties removed or replaced with Spring Boot 3.0 equivalents
- Application starts without configuration warnings
- Property validation passes
- Configuration file is valid YAML or properties format

## Example Therapist Responses

### Example 1

- Client/Input: application.yml contains: spring.redis.host: localhost
- Therapist/Output: Updated to: spring.data.redis.host: localhost
- Notes: Redis properties moved from spring.redis.* to spring.data.redis.* namespace

### Example 2

- Client/Input: application.properties contains: spring.security.saml2.relyingparty.registration.myapp.identity-provider.entity-id=...
- Therapist/Output: Updated to: spring.security.saml2.relyingparty.registration.myapp.asserting-party.entity-id=...
- Notes: SAML2 identity-provider properties replaced with asserting-party

## Triggers

- Upgrading application from Spring Boot 2.x to 3.0
- Reviewing application.properties or application.yml files during migration
- Encountering configuration warnings or property-not-found errors after upgrade

## Examples

### Example 1

Input:

  application.yml contains: spring.redis.host: localhost

Output:

  Updated to: spring.data.redis.host: localhost

Notes:

  Redis properties moved from spring.redis.* to spring.data.redis.* namespace

### Example 2

Input:

  application.properties contains: spring.security.saml2.relyingparty.registration.myapp.identity-provider.entity-id=...

Output:

  Updated to: spring.security.saml2.relyingparty.registration.myapp.asserting-party.entity-id=...

Notes:

  SAML2 identity-provider properties replaced with asserting-party
