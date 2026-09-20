---
id: "c9a27bca-e2b2-5437-9e32-4ca968a54dad"
name: "Spring Boot 3.0 Web and Actuator Migration"
description: "Comprehensive workflow to migrate web application routing, servlet configuration, actuator endpoints, metrics export, and graceful shutdown behavior to Spring Boot 3.0 standards. Covers Spring MVC/WebFlux URL matching changes, actuator endpoint renaming, Micrometer configuration updates, and HTTP server settings."
version: "0.1.0"
tags:
  - "spring-boot-3.0"
  - "migration"
  - "web-framework"
  - "actuator"
  - "metrics"
  - "monitoring"
triggers:
  - "Application uses Spring MVC, WebFlux, actuator endpoints, or metrics export that require Spring Boot 3.0 updates"
examples:
  - input: "Spring Boot 2.7.x application with actuator enabled, using 'httptrace' endpoint for HTTP request logging, and Micrometer metrics export configured."
    output: "Actuator configuration updated with 'httpexchanges' endpoint name; Micrometer tag providers migrated; metrics export properties aligned with Spring Boot 3.0; application tested and deployed."
    notes: "Endpoint renaming requires updates to any monitoring dashboards or log aggregation systems that reference 'httptrace'."
  - input: "Spring MVC application with custom URL patterns and graceful shutdown enabled."
    output: "URL matching rules reviewed and updated for Spring Boot 3.0 compatibility; graceful shutdown phases reconfigured; application tested with new routing behavior."
    notes: "Test all routes thoroughly to ensure no unexpected routing changes occur."
---

# Spring Boot 3.0 Web and Actuator Migration

Comprehensive workflow to migrate web application routing, servlet configuration, actuator endpoints, metrics export, and graceful shutdown behavior to Spring Boot 3.0 standards. Covers Spring MVC/WebFlux URL matching changes, actuator endpoint renaming, Micrometer configuration updates, and HTTP server settings.

## Prompt

Review and update web layer components (Spring MVC/WebFlux URL matching, server headers, graceful shutdown phases), actuator endpoint configurations (endpoint renaming, JMX exposure, sanitization), and metrics export properties (Micrometer tag providers, instrumentation deprecations) to meet Spring Boot 3.0 standards.

## Objective

Migrate web layer, actuator endpoints, and monitoring configuration to Spring Boot 3.0 standards
## Applicable Signals

- Application uses Spring MVC or WebFlux routing
- Actuator endpoints are enabled and exposed
- Metrics export or Micrometer instrumentation is configured
- Graceful shutdown or HTTP header size limits are in use
- RestTemplate or HTTP client configuration is present

## Contraindications

- Application is not a web application or does not use web frameworks
- Actuator is disabled and no monitoring is required
- No HTTP endpoints or metrics export are configured
- Application targets Spring Boot 2.x or earlier versions

## Intervention Moves

- Review and update URL matching rules for Spring MVC and WebFlux changes
- Rename 'httptrace' endpoint to 'httpexchanges' in actuator configuration
- Update JMX endpoint exposure settings
- Migrate Micrometer tag providers and instrumentation from Spring Boot 2.x deprecations
- Review and update metrics export properties for Micrometer
- Update graceful shutdown phase configuration
- Review 'server.max-http-header-size' property usage
- Update Apache HttpClient or RestTemplate configuration if applicable
- Apply actuator endpoint sanitization rules
- Update Jetty-specific web server configuration if in use

## Workflow Steps

- {'step': 1, 'title': 'Review Web Application Changes', 'description': 'Examine Spring MVC and WebFlux URL matching changes; update routing rules and path patterns as needed.'}
- {'step': 2, 'title': 'Update Server Configuration', 'description': "Review 'server.max-http-header-size' property; update graceful shutdown phases; configure Jetty or other web server settings if applicable."}
- {'step': 3, 'title': 'Migrate Actuator Endpoints', 'description': "Rename 'httptrace' to 'httpexchanges'; update JMX endpoint exposure; apply endpoint sanitization rules; update actuator JSON configuration."}
- {'step': 4, 'title': 'Update Metrics and Micrometer Configuration', 'description': "Migrate tag providers and contributors from Spring Boot 2.x; update metrics export properties; review auto-configuration of Micrometer's JvmInfoMetrics."}
- {'step': 5, 'title': 'Update HTTP Client Configuration', 'description': 'Review and update Apache HttpClient or RestTemplate configuration for Spring Boot 3.0 compatibility.'}
- {'step': 6, 'title': 'Test and Validate', 'description': 'Test all web endpoints, actuator endpoints, metrics export, and graceful shutdown behavior in a staging environment.'}

## Constraints

- Must complete core Spring Boot 3.0 upgrade (Java 17+, Jakarta EE migration) before applying this workflow
- Requires review of Spring Framework 6.0 changes for web layer compatibility
- Actuator endpoint changes must be tested against client integrations

## Cautions

- Endpoint renaming ('httptrace' → 'httpexchanges') may break monitoring dashboards or scripts that depend on the old name
- URL matching changes in Spring MVC/WebFlux may alter routing behavior; test all routes thoroughly
- Graceful shutdown phase updates may affect application shutdown timing; validate in staging environment
- Metrics export property changes may require updates to external monitoring systems

## Output Contract

- Updated web application configuration files (application.properties or application.yml) with corrected URL matching rules, actuator endpoint names and exposure settings, metrics export properties, graceful shutdown phases, and HTTP server configuration
- All web endpoints and actuator endpoints functional and tested
- Metrics export working with updated Micrometer configuration

## Example Therapist Responses

### Example 1

- Client/Input: Spring Boot 2.7.x application with actuator enabled, using 'httptrace' endpoint for HTTP request logging, and Micrometer metrics export configured.
- Therapist/Output: Actuator configuration updated with 'httpexchanges' endpoint name; Micrometer tag providers migrated; metrics export properties aligned with Spring Boot 3.0; application tested and deployed.
- Notes: Endpoint renaming requires updates to any monitoring dashboards or log aggregation systems that reference 'httptrace'.

### Example 2

- Client/Input: Spring MVC application with custom URL patterns and graceful shutdown enabled.
- Therapist/Output: URL matching rules reviewed and updated for Spring Boot 3.0 compatibility; graceful shutdown phases reconfigured; application tested with new routing behavior.
- Notes: Test all routes thoroughly to ensure no unexpected routing changes occur.

## Triggers

- Application uses Spring MVC, WebFlux, actuator endpoints, or metrics export that require Spring Boot 3.0 updates

## Examples

### Example 1

Input:

  Spring Boot 2.7.x application with actuator enabled, using 'httptrace' endpoint for HTTP request logging, and Micrometer metrics export configured.

Output:

  Actuator configuration updated with 'httpexchanges' endpoint name; Micrometer tag providers migrated; metrics export properties aligned with Spring Boot 3.0; application tested and deployed.

Notes:

  Endpoint renaming requires updates to any monitoring dashboards or log aggregation systems that reference 'httptrace'.

### Example 2

Input:

  Spring MVC application with custom URL patterns and graceful shutdown enabled.

Output:

  URL matching rules reviewed and updated for Spring Boot 3.0 compatibility; graceful shutdown phases reconfigured; application tested with new routing behavior.

Notes:

  Test all routes thoroughly to ensure no unexpected routing changes occur.
