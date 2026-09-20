---
id: "fd735f30-d667-526a-8776-2f02c0e9b302"
name: "Actuator JSON Serialization Isolation"
description: "Ensure actuator endpoint responses use isolated ObjectMapper for consistent JSON serialization in Spring Boot 3.0. When developing custom actuator endpoints, implement the OperationResponseBody interface to ensure the isolated ObjectMapper is applied. Optionally revert to application ObjectMapper behavior by configuration."
version: "0.1.0"
tags:
  - "spring-boot-3"
  - "actuator"
  - "json-serialization"
  - "objectmapper"
  - "custom-endpoints"
triggers:
  - "developing custom actuator endpoints in Spring Boot 3.0"
  - "need consistent JSON response formatting"
  - "want to verify serialization behavior"
---

# Actuator JSON Serialization Isolation

Ensure actuator endpoint responses use isolated ObjectMapper for consistent JSON serialization in Spring Boot 3.0. When developing custom actuator endpoints, implement the OperationResponseBody interface to ensure the isolated ObjectMapper is applied. Optionally revert to application ObjectMapper behavior by configuration.

## Prompt

When implementing custom actuator endpoints in Spring Boot 3.0:
1. Ensure custom endpoint response classes implement the OperationResponseBody interface.
2. This guarantees the isolated ObjectMapper instance is used for JSON serialization.
3. If you need to revert to the application's ObjectMapper instead, set management.endpoints.jackson.isolated-object-mapper to false.
4. Verify that responses are serialized consistently across all actuator endpoints.

## Objective

ensure_consistent_actuator_json_serialization
## Applicable Signals

- developing custom actuator endpoints in Spring Boot 3.0
- need consistent JSON response formatting across actuator endpoints
- want to verify or control actuator endpoint serialization behavior

## Contraindications

- using only built-in actuator endpoints without custom endpoint development
- application does not require isolated ObjectMapper behavior
- no custom actuator endpoint responses being serialized

## Intervention Moves

- implement OperationResponseBody interface on custom endpoint response classes
- verify isolated ObjectMapper is applied to endpoint responses
- configure management.endpoints.jackson.isolated-object-mapper property if reverting to application ObjectMapper

## Constraints

- Spring Boot 3.0 or later required
- applies only to actuator endpoint JSON responses
- custom endpoints must explicitly implement OperationResponseBody for isolation to apply

## Cautions

- reverting to application ObjectMapper (isolated-object-mapper=false) may cause inconsistency with built-in endpoint responses
- custom endpoints without OperationResponseBody interface will not benefit from isolated ObjectMapper

## Output Contract

- custom endpoint response classes implement OperationResponseBody interface; isolated ObjectMapper applied to responses; or management.endpoints.jackson.isolated-object-mapper explicitly set to false if application ObjectMapper is required

## Triggers

- developing custom actuator endpoints in Spring Boot 3.0
- need consistent JSON response formatting
- want to verify serialization behavior
