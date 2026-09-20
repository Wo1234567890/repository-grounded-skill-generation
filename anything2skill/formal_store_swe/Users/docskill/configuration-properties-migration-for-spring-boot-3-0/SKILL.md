---
id: "9d9280ad-da31-5dcd-b42e-7af702e842e9"
name: "Configuration Properties Migration for Spring Boot 3.0"
description: "Identifies and updates deprecated or renamed configuration properties in application.properties or application.yml files to match Spring Boot 3.0 schema. Ensures all property keys, values, and formats conform to Spring Boot 3.0 requirements."
version: "0.1.0"
tags:
  - "spring-boot"
  - "migration"
  - "configuration"
  - "properties"
  - "upgrade"
triggers:
  - "Updating application.properties or application.yml during Spring Boot 3.0 migration"
  - "Configuration validation fails post-upgrade with unrecognized property warnings"
  - "Application startup logs indicate deprecated property usage"
examples:
  - input: "application.yml contains 'spring.datasource.hikari.maximum-pool-size: 10' and 'management.endpoints.web.exposure.include: httptrace'"
    output: "Property 'management.endpoints.web.exposure.include' updated to 'httpexchanges'; Hikari property remains valid in 3.0"
    notes: "httptrace endpoint renamed to httpexchanges in Spring Boot 3.0"
  - input: "application.properties contains 'spring.elasticsearch.rest.uris=http://localhost:9200'"
    output: "Property updated to 'spring.elasticsearch.uris' (rest prefix removed)"
    notes: "Elasticsearch client configuration simplified in Spring Boot 3.0"
---

# Configuration Properties Migration for Spring Boot 3.0

Identifies and updates deprecated or renamed configuration properties in application.properties or application.yml files to match Spring Boot 3.0 schema. Ensures all property keys, values, and formats conform to Spring Boot 3.0 requirements.

## Prompt

Review application.properties and application.yml files for deprecated or renamed properties. Cross-reference against Spring Boot 3.0 property schema. Replace or remove deprecated entries. Validate that all properties are recognized by Spring Boot 3.0 and that the application starts without configuration warnings.

## Objective

Migrate all configuration properties to Spring Boot 3.0 equivalents
## Applicable Signals

- Spring Boot 2.x configuration files present in project
- Build or startup logs contain property deprecation warnings
- Configuration schema validation reports unknown properties

## Contraindications

- Configuration files are already validated as 3.0-compatible
- Using external configuration management (e.g., Spring Cloud Config) that abstracts property names
- Properties are dynamically generated or injected at runtime

## Workflow Steps

- {'step': 1, 'action': 'Locate all configuration files', 'detail': 'Identify application.properties, application.yml, and profile-specific variants (application-dev.yml, etc.)'}
- {'step': 2, 'action': 'Extract all property keys', 'detail': 'List all properties currently defined in configuration files'}
- {'step': 3, 'action': 'Cross-reference against Spring Boot 3.0 schema', 'detail': 'Check each property against official Spring Boot 3.0 documentation and deprecation notices for data access, actuator, metrics, security, and web properties'}
- {'step': 4, 'action': 'Identify deprecated or renamed properties', 'detail': 'Flag properties that have been removed, renamed, or changed in structure (e.g., Cassandra, Redis, Flyway, Liquibase, Hibernate, Elasticsearch properties)'}
- {'step': 5, 'action': 'Update or remove deprecated properties', 'detail': 'Replace old property names with new equivalents; remove properties no longer supported; update values if format has changed'}
- {'step': 6, 'action': 'Validate configuration', 'detail': 'Start application and verify no configuration warnings or errors appear; check logs for unrecognized properties'}
- {'step': 7, 'action': 'Test application behavior', 'detail': 'Verify that configuration changes do not break application functionality or integrations'}

## Constraints

- Must review all property sources: application.properties, application.yml, environment variables, and system properties
- Property changes must be applied consistently across all profiles (dev, test, prod)
- Must validate that renamed or removed properties do not break dependent services or integrations

## Cautions

- Some properties may have changed data types or accepted values; verify format compatibility
- Removal of a property may require fallback configuration or code changes
- Property name changes are case-sensitive; ensure exact matching

## Output Contract

- All deprecated properties removed or renamed to Spring Boot 3.0 equivalents; application starts without configuration warnings or errors; configuration validation passes

## Example Executions

### Example 1

- Input: application.yml contains 'spring.datasource.hikari.maximum-pool-size: 10' and 'management.endpoints.web.exposure.include: httptrace'
- Output: Property 'management.endpoints.web.exposure.include' updated to 'httpexchanges'; Hikari property remains valid in 3.0
- Notes: httptrace endpoint renamed to httpexchanges in Spring Boot 3.0

### Example 2

- Input: application.properties contains 'spring.elasticsearch.rest.uris=http://localhost:9200'
- Output: Property updated to 'spring.elasticsearch.uris' (rest prefix removed)
- Notes: Elasticsearch client configuration simplified in Spring Boot 3.0

## Triggers

- Updating application.properties or application.yml during Spring Boot 3.0 migration
- Configuration validation fails post-upgrade with unrecognized property warnings
- Application startup logs indicate deprecated property usage

## Examples

### Example 1

Input:

  application.yml contains 'spring.datasource.hikari.maximum-pool-size: 10' and 'management.endpoints.web.exposure.include: httptrace'

Output:

  Property 'management.endpoints.web.exposure.include' updated to 'httpexchanges'; Hikari property remains valid in 3.0

Notes:

  httptrace endpoint renamed to httpexchanges in Spring Boot 3.0

### Example 2

Input:

  application.properties contains 'spring.elasticsearch.rest.uris=http://localhost:9200'

Output:

  Property updated to 'spring.elasticsearch.uris' (rest prefix removed)

Notes:

  Elasticsearch client configuration simplified in Spring Boot 3.0
