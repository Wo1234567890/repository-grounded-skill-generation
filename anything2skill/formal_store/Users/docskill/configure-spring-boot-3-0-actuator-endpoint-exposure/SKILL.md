---
id: "1674de73-fd00-544c-98aa-ed7a22b6bd9f"
name: "Configure Spring Boot 3.0 Actuator Endpoint Exposure"
description: "Configure which actuator endpoints are exposed over JMX and HTTP in Spring Boot 3.0. By default, only the health endpoint is exposed over JMX. Use this skill when migrating from Spring Boot 2.x to align endpoint exposure with new defaults and control access via inclusion/exclusion properties."
version: "0.1.0"
tags:
  - "spring-boot-3.0"
  - "actuator"
  - "configuration"
  - "jmx"
  - "endpoint-exposure"
  - "migration"
triggers:
  - "migrating Spring Boot application from 2.x to 3.0"
  - "actuator module is in use"
  - "need to control endpoint exposure over JMX or HTTP"
  - "validating actuator configuration after upgrade"
---

# Configure Spring Boot 3.0 Actuator Endpoint Exposure

Configure which actuator endpoints are exposed over JMX and HTTP in Spring Boot 3.0. By default, only the health endpoint is exposed over JMX. Use this skill when migrating from Spring Boot 2.x to align endpoint exposure with new defaults and control access via inclusion/exclusion properties.

## Prompt

1. Review current actuator endpoint exposure settings in your Spring Boot 2.x application.
2. Identify which endpoints need to be exposed over JMX and HTTP.
3. Set `management.endpoints.jmx.exposure.include` and `management.endpoints.jmx.exposure.exclude` properties to control JMX exposure.
4. Set corresponding HTTP exposure properties if needed.
5. Verify that only intended endpoints are accessible after configuration.
6. Test endpoint access via JMX and HTTP to confirm alignment with Spring Boot 3.0 defaults.

## Objective

align_actuator_endpoint_exposure
## Applicable Signals

- Spring Boot 3.0 upgrade in progress
- actuator endpoints currently exposed beyond health endpoint over JMX
- custom endpoint exposure requirements exist
- security or compliance requires restricted endpoint access

## Contraindications

- application does not use Spring Boot actuator module
- endpoint exposure is already correctly configured for Spring Boot 3.0
- no custom endpoint exposure requirements

## Workflow Steps

- {'step': 1, 'action': 'Review current actuator configuration', 'detail': 'Check existing management.endpoints.jmx.exposure and management.endpoints.http.exposure settings.'}
- {'step': 2, 'action': 'Identify required endpoints', 'detail': 'Determine which actuator endpoints (health, metrics, env, configprops, etc.) must be exposed.'}
- {'step': 3, 'action': 'Configure JMX exposure', 'detail': 'Set management.endpoints.jmx.exposure.include and management.endpoints.jmx.exposure.exclude properties.'}
- {'step': 4, 'action': 'Configure HTTP exposure if needed', 'detail': 'Set management.endpoints.web.exposure.include and management.endpoints.web.exposure.exclude properties.'}
- {'step': 5, 'action': 'Validate configuration', 'detail': 'Start application and verify that only intended endpoints are accessible via JMX and HTTP.'}

## Constraints

- Spring Boot 3.0 or later must be in use
- actuator dependency must be present in project
- configuration properties must be set before application startup

## Cautions

- Changing endpoint exposure may affect monitoring and management tools that depend on specific endpoints.
- Restricting endpoint exposure too aggressively may limit operational visibility.
- Test endpoint access after configuration to ensure intended behavior.

## Output Contract

- Actuator endpoints are exposed only as intended
- health endpoint is exposed by default over JMX
- custom inclusion/exclusion properties are applied and verified
- endpoint access aligns with Spring Boot 3.0 defaults

## Triggers

- migrating Spring Boot application from 2.x to 3.0
- actuator module is in use
- need to control endpoint exposure over JMX or HTTP
- validating actuator configuration after upgrade
