---
id: "21c3f0fd-443e-5dba-918f-69fe0e2b5d96"
name: "Configure Actuator Endpoint Value Sanitization"
description: "Establish sanitization policy for Spring Boot actuator endpoints (/env and /configprops) to control visibility of sensitive configuration values. Apply NEVER (default, all masked), ALWAYS (all visible), or WHEN_AUTHORIZED (conditional on user authorization) modes to protect sensitive data exposure."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "actuator-security"
  - "sensitive-data-protection"
  - "configuration-exposure"
  - "authorization-control"
triggers:
  - "Spring Boot 3.0 migration in progress"
  - "Actuator endpoints (/env, /configprops) are exposed"
  - "Application contains sensitive configuration values"
  - "Need to control visibility of unmasked configuration to users"
---

# Configure Actuator Endpoint Value Sanitization

Establish sanitization policy for Spring Boot actuator endpoints (/env and /configprops) to control visibility of sensitive configuration values. Apply NEVER (default, all masked), ALWAYS (all visible), or WHEN_AUTHORIZED (conditional on user authorization) modes to protect sensitive data exposure.

## Prompt

When migrating to Spring Boot 3.0, configure the sanitization policy for actuator endpoints to protect sensitive configuration values. Set the sanitization mode using management.endpoints.jackson.sanitization.mode or management.endpoint.quartz.show-values. Choose NEVER (all values masked by default), ALWAYS (all values visible, user-defined sanitizers still apply), or WHEN_AUTHORIZED (values visible only to authenticated, authorized users). For JMX, users are always considered authorized; for HTTP, authorization requires authentication and specified roles.

## Objective

protect_sensitive_actuator_endpoint_values
## Applicable Signals

- management.endpoints.jmx.exposure.include or management.endpoints.jmx.exposure.exclude configured
- actuator module is active
- sensitive keys or values present in application configuration

## Contraindications

- Actuator endpoints are not exposed or disabled
- Application contains no sensitive configuration data
- All users are untrusted and should never see any unmasked values (use NEVER mode exclusively)

## Workflow Steps

- Identify which actuator endpoints are exposed (typically /env and /configprops)
- Determine sensitivity level of configuration values in the application
- Select appropriate sanitization mode: NEVER (default, safest), ALWAYS (least safe), or WHEN_AUTHORIZED (conditional)
- Configure management.endpoints.jackson.sanitization.mode property with chosen mode
- If using QuartzEndpoint, configure management.endpoint.quartz.show-values with same mode
- For WHEN_AUTHORIZED mode, verify role-based access control is properly configured

## Constraints

- Sanitization mode applies to both /env and /configprops endpoints
- For JMX access, users are always considered authorized regardless of mode
- For HTTP access, WHEN_AUTHORIZED mode requires both authentication and specified role membership
- User-defined sanitizing functions apply in addition to mode-based sanitization

## Cautions

- ALWAYS mode exposes all values; use only if all users are trusted
- WHEN_AUTHORIZED mode requires proper role-based access control configuration
- QuartzEndpoint sanitization must be configured separately using management.endpoint.quartz.show-values

## Output Contract

- Sanitization policy applied to actuator endpoints; sensitive values masked by default (NEVER mode) or conditionally exposed based on user authorization level (WHEN_AUTHORIZED mode); all values visible if ALWAYS mode selected; QuartzEndpoint sanitization configured if applicable; downstream callers can rely on consistent value masking behavior across endpoints.

## Triggers

- Spring Boot 3.0 migration in progress
- Actuator endpoints (/env, /configprops) are exposed
- Application contains sensitive configuration values
- Need to control visibility of unmasked configuration to users
