---
id: "c101555d-ef0e-5d4e-b321-4067b6a85ebe"
name: "Configure Actuator Endpoint Value Sanitization"
description: "Set sanitization policy for sensitive values in /env and /configprops endpoints using NEVER, ALWAYS, or WHEN_AUTHORIZED modes to control exposure of configuration secrets in Spring Boot 3.0."
version: "0.1.0"
tags:
  - "spring-boot-3"
  - "actuator"
  - "security"
  - "sanitization"
  - "configuration"
  - "migration"
triggers:
  - "Migrating application to Spring Boot 3.0"
  - "/env or /configprops endpoints are exposed"
  - "Sensitive configuration values (passwords, keys, tokens) present in application properties"
examples:
  - input: "Spring Boot 3.0 application with /env endpoint exposed; management.endpoints.web.exposure.include=env,health"
    output: "Set management.endpoints.web.exposure.sanitization-mode=NEVER; all configuration values masked by default when /env is accessed"
    notes: "Default behavior; no additional configuration needed unless ALWAYS or WHEN_AUTHORIZED is required"
  - input: "Development environment requiring full visibility of configuration for debugging"
    output: "Set management.endpoints.web.exposure.sanitization-mode=ALWAYS; all values visible in /env and /configprops responses"
    notes: "Use only in development; never in production"
  - input: "Production environment with authenticated users; sensitive values should be visible only to authorized admins"
    output: "Set management.endpoints.web.exposure.sanitization-mode=WHEN_AUTHORIZED; values visible only if user is authenticated and has required role"
    notes: "Requires proper Spring Security configuration and role-based access control"
---

# Configure Actuator Endpoint Value Sanitization

Set sanitization policy for sensitive values in /env and /configprops endpoints using NEVER, ALWAYS, or WHEN_AUTHORIZED modes to control exposure of configuration secrets in Spring Boot 3.0.

## Prompt

Apply sanitization policy to actuator endpoints by setting management.endpoints.web.exposure.include or management.endpoints.web.exposure.exclude, then configure the sanitization level via management.endpoints.web.exposure.sanitization-mode (or equivalent property). For QuartzEndpoint, use management.endpoint.quartz.show-values. Verify that sensitive keys (passwords, tokens, API keys) are masked according to the chosen policy before exposing endpoints to untrusted users.

## Objective

Enforce value masking policy for sensitive actuator endpoints to prevent credential leakage
## Applicable Signals

- Spring Boot version upgrade to 3.0+
- Actuator module enabled and endpoints exposed
- Configuration contains credential-like values

## Contraindications

- Actuator endpoints are not exposed or disabled
- No sensitive values in application configuration
- Application runs in fully isolated environment with no external access

## Workflow Steps

- {'step': 1, 'action': 'Identify which actuator endpoints are exposed', 'detail': 'Check management.endpoints.web.exposure.include and management.endpoints.web.exposure.exclude properties'}
- {'step': 2, 'action': 'Choose sanitization mode', 'detail': 'Select NEVER (all values masked), ALWAYS (all values visible), or WHEN_AUTHORIZED (conditional visibility)'}
- {'step': 3, 'action': 'Configure sanitization property', 'detail': 'Set management.endpoints.web.exposure.sanitization-mode or equivalent to chosen mode'}
- {'step': 4, 'action': 'If using QuartzEndpoint, configure its sanitization', 'detail': 'Set management.endpoint.quartz.show-values to NEVER, ALWAYS, or WHEN_AUTHORIZED'}
- {'step': 5, 'action': 'Test endpoint access and verify masking', 'detail': 'Call /env and /configprops endpoints; confirm sensitive values are masked or visible per policy'}

## Constraints

- Sanitization policy applies only to /env and /configprops endpoints by default
- For JMX, users are always considered authorized; for HTTP, authorization depends on authentication and role
- User-defined sanitizing functions still apply regardless of policy mode

## Cautions

- ALWAYS mode exposes all values; use only in development or fully trusted environments
- WHEN_AUTHORIZED requires proper authentication and role configuration to be effective
- NEVER (default) masks all values; verify this does not break legitimate monitoring or debugging workflows

## Output Contract

- Sanitization policy applied and verified: sensitive values in /env and /configprops endpoints are masked (NEVER), visible (ALWAYS), or conditionally visible (WHEN_AUTHORIZED) according to configuration; QuartzEndpoint sanitization configured if endpoint is used.

## Example Executions

### Example 1

- Input: Spring Boot 3.0 application with /env endpoint exposed; management.endpoints.web.exposure.include=env,health
- Output: Set management.endpoints.web.exposure.sanitization-mode=NEVER; all configuration values masked by default when /env is accessed
- Notes: Default behavior; no additional configuration needed unless ALWAYS or WHEN_AUTHORIZED is required

### Example 2

- Input: Development environment requiring full visibility of configuration for debugging
- Output: Set management.endpoints.web.exposure.sanitization-mode=ALWAYS; all values visible in /env and /configprops responses
- Notes: Use only in development; never in production

### Example 3

- Input: Production environment with authenticated users; sensitive values should be visible only to authorized admins
- Output: Set management.endpoints.web.exposure.sanitization-mode=WHEN_AUTHORIZED; values visible only if user is authenticated and has required role
- Notes: Requires proper Spring Security configuration and role-based access control

## Triggers

- Migrating application to Spring Boot 3.0
- /env or /configprops endpoints are exposed
- Sensitive configuration values (passwords, keys, tokens) present in application properties

## Examples

### Example 1

Input:

  Spring Boot 3.0 application with /env endpoint exposed; management.endpoints.web.exposure.include=env,health

Output:

  Set management.endpoints.web.exposure.sanitization-mode=NEVER; all configuration values masked by default when /env is accessed

Notes:

  Default behavior; no additional configuration needed unless ALWAYS or WHEN_AUTHORIZED is required

### Example 2

Input:

  Development environment requiring full visibility of configuration for debugging

Output:

  Set management.endpoints.web.exposure.sanitization-mode=ALWAYS; all values visible in /env and /configprops responses

Notes:

  Use only in development; never in production

### Example 3

Input:

  Production environment with authenticated users; sensitive values should be visible only to authorized admins

Output:

  Set management.endpoints.web.exposure.sanitization-mode=WHEN_AUTHORIZED; values visible only if user is authenticated and has required role

Notes:

  Requires proper Spring Security configuration and role-based access control
