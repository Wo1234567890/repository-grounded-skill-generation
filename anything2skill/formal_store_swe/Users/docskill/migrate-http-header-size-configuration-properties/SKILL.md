---
id: "203dd67d-baea-527b-ba53-14dbd8f55ebf"
name: "Migrate HTTP Header Size Configuration Properties"
description: "Replace deprecated `server.max-http-header-size` with `server.max-http-request-header-size` for request headers during Spring Boot 3.0 migration. For response header limits on Tomcat or Jetty, use WebServerFactoryCustomizer instead."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "configuration-properties"
  - "server-configuration"
  - "http-headers"
  - "deprecation-handling"
triggers:
  - "Spring Boot 3.0 migration in progress"
  - "Application uses server.max-http-header-size property"
  - "Need to control request or response header sizes"
examples:
  - input: "application.properties contains: server.max-http-header-size=16384"
    output: "application.properties updated to: server.max-http-request-header-size=16384; WebServerFactoryCustomizer added if response header limit is also needed"
    notes: "Both request and response header sizes were previously controlled by the single deprecated property; now they require separate configuration"
  - input: "Spring Boot 3.0 migration with Tomcat and response header size limit requirement"
    output: "@Configuration class with WebServerFactoryCustomizer<TomcatServletWebServerFactory> bean that calls customizer.getProtocol().setMaxHttpHeaderSize()"
    notes: "Response header customization is server-specific; Jetty uses similar pattern with JettyServletWebServerFactory"
---

# Migrate HTTP Header Size Configuration Properties

Replace deprecated `server.max-http-header-size` with `server.max-http-request-header-size` for request headers during Spring Boot 3.0 migration. For response header limits on Tomcat or Jetty, use WebServerFactoryCustomizer instead.

## Prompt

1. Locate any `server.max-http-header-size` property in application.properties or application.yml.
2. Replace it with `server.max-http-request-header-size` to control request header size.
3. If response header size limits are needed on Tomcat or Jetty, create a WebServerFactoryCustomizer bean to set the response header limit.
4. Remove the deprecated property entirely.
5. Test that header size constraints are enforced as expected.

## Objective

Update HTTP header size configuration to Spring Boot 3.0 property model
## Applicable Signals

- Deprecated property warning during build or startup
- Configuration file contains server.max-http-header-size
- Header size constraints are part of application requirements

## Contraindications

- Application does not set HTTP header size limits
- Using non-Tomcat/Jetty servers for response header customization (not supported)

## Workflow Steps

- {'step': 1, 'action': 'Identify deprecated property', 'detail': 'Search application.properties or application.yml for server.max-http-header-size'}
- {'step': 2, 'action': 'Replace with new request header property', 'detail': 'Change server.max-http-header-size to server.max-http-request-header-size with the same value'}
- {'step': 3, 'action': 'Add response header customizer if needed', 'detail': 'If response header limits are required, create a @Configuration class with WebServerFactoryCustomizer<TomcatServletWebServerFactory> or <JettyServletWebServerFactory>'}
- {'step': 4, 'action': 'Remove deprecated property', 'detail': 'Delete server.max-http-header-size from configuration'}
- {'step': 5, 'action': 'Validate configuration', 'detail': 'Build and test application to confirm header size constraints are enforced'}

## Constraints

- server.max-http-request-header-size applies only to request headers
- Response header size customization is only supported on Tomcat and Jetty
- WebServerFactoryCustomizer must be used for response header limits

## Cautions

- Ensure WebServerFactoryCustomizer is only applied when using Tomcat or Jetty
- Test header size enforcement after migration to confirm behavior is preserved

## Output Contract

- Deprecated property removed from configuration; request header size controlled via server.max-http-request-header-size; response header size (if needed) configured via WebServerFactoryCustomizer; application builds and runs without deprecation warnings related to this property.

## Example Executions

### Example 1

- Input: application.properties contains: server.max-http-header-size=16384
- Output: application.properties updated to: server.max-http-request-header-size=16384; WebServerFactoryCustomizer added if response header limit is also needed
- Notes: Both request and response header sizes were previously controlled by the single deprecated property; now they require separate configuration

### Example 2

- Input: Spring Boot 3.0 migration with Tomcat and response header size limit requirement
- Output: @Configuration class with WebServerFactoryCustomizer<TomcatServletWebServerFactory> bean that calls customizer.getProtocol().setMaxHttpHeaderSize()
- Notes: Response header customization is server-specific; Jetty uses similar pattern with JettyServletWebServerFactory

## Triggers

- Spring Boot 3.0 migration in progress
- Application uses server.max-http-header-size property
- Need to control request or response header sizes

## Examples

### Example 1

Input:

  application.properties contains: server.max-http-header-size=16384

Output:

  application.properties updated to: server.max-http-request-header-size=16384; WebServerFactoryCustomizer added if response header limit is also needed

Notes:

  Both request and response header sizes were previously controlled by the single deprecated property; now they require separate configuration

### Example 2

Input:

  Spring Boot 3.0 migration with Tomcat and response header size limit requirement

Output:

  @Configuration class with WebServerFactoryCustomizer<TomcatServletWebServerFactory> bean that calls customizer.getProtocol().setMaxHttpHeaderSize()

Notes:

  Response header customization is server-specific; Jetty uses similar pattern with JettyServletWebServerFactory
