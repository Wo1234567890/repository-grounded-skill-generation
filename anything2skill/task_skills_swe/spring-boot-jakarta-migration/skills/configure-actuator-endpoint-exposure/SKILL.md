---
id: "7d4d3e6d-3038-54c6-b891-273d937c9189"
name: "Configure Actuator Endpoint Exposure"
description: "Set JMX and HTTP endpoint exposure rules for Spring Boot actuator by configuring inclusion and exclusion properties. Aligns endpoint visibility with Spring Boot 3.0 defaults where only the health endpoint is exposed over JMX by default."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "actuator"
  - "endpoint-exposure"
  - "jmx"
  - "http"
  - "configuration"
triggers:
  - "Migrating Spring Boot 2.x to 3.0 and need to control which actuator endpoints are exposed over JMX or HTTP"
examples:
  - input: "Application migrated to Spring Boot 3.0; need to expose metrics and health endpoints over JMX"
    output: "Set management.endpoints.jmx.exposure.include=health,metrics in application.properties; health endpoint is exposed by default, metrics is explicitly included"
    notes: "Only specified endpoints are exposed; all others remain hidden"
  - input: "Need to expose all endpoints over HTTP but restrict JMX to health only"
    output: "Set management.endpoints.web.exposure.include=* and management.endpoints.jmx.exposure.include=health"
    notes: "Wildcard '*' exposes all endpoints; JMX defaults to health only"
---

# Configure Actuator Endpoint Exposure

Set JMX and HTTP endpoint exposure rules for Spring Boot actuator by configuring inclusion and exclusion properties. Aligns endpoint visibility with Spring Boot 3.0 defaults where only the health endpoint is exposed over JMX by default.

## Prompt

To configure actuator endpoint exposure in Spring Boot 3.0:
1. Identify which endpoints need to be exposed over JMX and HTTP.
2. Set `management.endpoints.jmx.exposure.include` to specify endpoints to expose over JMX (comma-separated list or '*' for all).
3. Set `management.endpoints.jmx.exposure.exclude` to specify endpoints to hide from JMX exposure.
4. Apply equivalent configuration for HTTP endpoints if needed via `management.endpoints.web.exposure.include` and `management.endpoints.web.exposure.exclude`.
5. Verify that the health endpoint remains visible by default over JMX unless explicitly excluded.
6. Test endpoint accessibility after configuration changes.

## Objective

Configure actuator endpoint exposure for JMX and HTTP to control which endpoints are accessible
## Applicable Signals

- Migrating Spring Boot 2.x application to 3.0
- Need to control actuator endpoint visibility over JMX
- Need to control actuator endpoint visibility over HTTP
- Endpoint exposure defaults have changed and require explicit configuration

## Contraindications

- Application does not use Spring Boot actuator module
- Endpoint exposure is already correctly configured and does not require changes
- No actuator endpoints are needed in the application

## Intervention Moves

- Set management.endpoints.jmx.exposure.include property
- Set management.endpoints.jmx.exposure.exclude property
- Set management.endpoints.web.exposure.include property
- Set management.endpoints.web.exposure.exclude property
- Verify health endpoint is exposed by default
- Test endpoint accessibility

## Workflow Steps

- {'step': 1, 'action': 'Review current actuator endpoint usage', 'detail': 'Identify which endpoints the application currently exposes and which are required for monitoring or debugging'}
- {'step': 2, 'action': 'Configure JMX endpoint exposure', 'detail': 'Set management.endpoints.jmx.exposure.include and management.endpoints.jmx.exposure.exclude in application.properties or application.yml'}
- {'step': 3, 'action': 'Configure HTTP endpoint exposure', 'detail': 'Set management.endpoints.web.exposure.include and management.endpoints.web.exposure.exclude if HTTP endpoint visibility needs adjustment'}
- {'step': 4, 'action': 'Verify default behavior', 'detail': 'Confirm that the health endpoint is exposed by default over JMX and that other endpoints follow the configured rules'}
- {'step': 5, 'action': 'Test endpoint accessibility', 'detail': 'Access configured endpoints via JMX and HTTP to verify they are accessible or hidden as intended'}

## Constraints

- Configuration must be applied before application startup to take effect
- Only the health endpoint is exposed over JMX by default in Spring Boot 3.0
- Inclusion and exclusion properties work together; exclusion takes precedence over inclusion

## Cautions

- Exposing sensitive endpoints (e.g., /env, /configprops) over JMX or HTTP may pose security risks; ensure proper authentication and authorization are in place
- Changes to endpoint exposure affect monitoring and debugging capabilities; coordinate with operations teams

## Output Contract

- Actuator endpoints are exposed according to configured inclusion and exclusion rules
- Health endpoint is visible by default over JMX unless explicitly excluded
- HTTP endpoint exposure follows configured rules
- All other endpoints are hidden by default unless explicitly included

## Example Executions

### Example 1

- Input: Application migrated to Spring Boot 3.0; need to expose metrics and health endpoints over JMX
- Output: Set management.endpoints.jmx.exposure.include=health,metrics in application.properties; health endpoint is exposed by default, metrics is explicitly included
- Notes: Only specified endpoints are exposed; all others remain hidden

### Example 2

- Input: Need to expose all endpoints over HTTP but restrict JMX to health only
- Output: Set management.endpoints.web.exposure.include=* and management.endpoints.jmx.exposure.include=health
- Notes: Wildcard '*' exposes all endpoints; JMX defaults to health only

## Triggers

- Migrating Spring Boot 2.x to 3.0 and need to control which actuator endpoints are exposed over JMX or HTTP

## Examples

### Example 1

Input:

  Application migrated to Spring Boot 3.0; need to expose metrics and health endpoints over JMX

Output:

  Set management.endpoints.jmx.exposure.include=health,metrics in application.properties; health endpoint is exposed by default, metrics is explicitly included

Notes:

  Only specified endpoints are exposed; all others remain hidden

### Example 2

Input:

  Need to expose all endpoints over HTTP but restrict JMX to health only

Output:

  Set management.endpoints.web.exposure.include=* and management.endpoints.jmx.exposure.include=health

Notes:

  Wildcard '*' exposes all endpoints; JMX defaults to health only
