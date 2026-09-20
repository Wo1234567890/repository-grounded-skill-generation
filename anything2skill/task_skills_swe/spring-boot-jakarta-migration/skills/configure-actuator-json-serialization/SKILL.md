---
id: "f1818d36-d725-52d0-bf8a-678456c2532b"
name: "Configure Actuator JSON Serialization"
description: "Control whether actuator endpoints use an isolated ObjectMapper instance or the application's shared ObjectMapper for JSON response serialization. Use when custom endpoint responses need consistent JSON serialization behavior or when reverting to application-level ObjectMapper is required during Spring Boot 3.0 migration."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "actuator"
  - "json-serialization"
  - "configuration"
  - "objectmapper"
triggers:
  - "Custom actuator endpoints exist and JSON response consistency is critical"
  - "Need to revert to application ObjectMapper for actuator responses"
  - "Migrating to Spring Boot 3.0 with custom endpoint implementations"
---

# Configure Actuator JSON Serialization

Control whether actuator endpoints use an isolated ObjectMapper instance or the application's shared ObjectMapper for JSON response serialization. Use when custom endpoint responses need consistent JSON serialization behavior or when reverting to application-level ObjectMapper is required during Spring Boot 3.0 migration.

## Prompt

Set the 'management.endpoints.jackson.isolated-object-mapper' property to control JSON serialization strategy. By default, actuator endpoints use an isolated ObjectMapper instance to ensure consistent results. If you have developed custom endpoints, ensure responses implement the OperationResponseBody interface so the isolated ObjectMapper is applied during JSON serialization.

## Objective

Set actuator JSON serialization strategy
## Applicable Signals

- Custom endpoint classes extending or implementing Spring Boot actuator interfaces
- JSON serialization inconsistencies between actuator and application responses
- Spring Boot 3.0 upgrade in progress

## Contraindications

- Using only default Spring Boot actuator endpoints without custom implementations
- No custom endpoint response serialization requirements

## Intervention Moves

- Identify custom actuator endpoints in the application
- Determine serialization strategy requirement
- Set management.endpoints.jackson.isolated-object-mapper property
- Implement OperationResponseBody interface on custom endpoint responses
- Test endpoint JSON responses

## Workflow Steps

- {'step': 1, 'action': 'Identify custom actuator endpoints in the application', 'detail': 'Review code for custom endpoint classes that extend or implement Spring Boot actuator interfaces'}
- {'step': 2, 'action': 'Determine serialization strategy requirement', 'detail': 'Decide whether to use isolated ObjectMapper (default, true) or application ObjectMapper (false)'}
- {'step': 3, 'action': 'Set management.endpoints.jackson.isolated-object-mapper property', 'detail': 'Configure in application.properties or application.yml: management.endpoints.jackson.isolated-object-mapper=true|false'}
- {'step': 4, 'action': 'Implement OperationResponseBody interface on custom endpoint responses', 'detail': 'Ensure custom endpoint response classes implement OperationResponseBody for proper ObjectMapper handling'}
- {'step': 5, 'action': 'Test endpoint JSON responses', 'detail': 'Verify that actuator endpoint responses serialize correctly with the configured strategy'}

## Constraints

- Property applies only to actuator endpoints, not application-wide serialization
- Custom endpoints should implement OperationResponseBody interface for proper isolation handling

## Cautions

- Changing this property affects all actuator endpoints; test thoroughly before production deployment
- Custom endpoints without OperationResponseBody implementation may not respect the isolated ObjectMapper setting

## Output Contract

- Property 'management.endpoints.jackson.isolated-object-mapper' is set to true (default, isolated ObjectMapper) or false (application ObjectMapper); custom endpoints implement OperationResponseBody interface if present; actuator endpoint JSON responses serialize consistently with the configured strategy.

## Triggers

- Custom actuator endpoints exist and JSON response consistency is critical
- Need to revert to application ObjectMapper for actuator responses
- Migrating to Spring Boot 3.0 with custom endpoint implementations
