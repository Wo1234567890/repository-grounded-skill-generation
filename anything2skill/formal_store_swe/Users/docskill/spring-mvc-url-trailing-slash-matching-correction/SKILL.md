---
id: "7d0f5760-3df7-5ee9-847e-b1cc32c352d2"
name: "Spring MVC URL Trailing Slash Matching Correction"
description: "Update Spring MVC and WebFlux route definitions to account for Spring Framework 6.0's disabled trailing slash matching by default. Explicitly configure trailing slash behavior or update controller mappings to match expected request patterns without trailing slashes."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "spring-framework-6"
  - "web-routing"
  - "url-matching"
  - "trailing-slash"
triggers:
  - "Spring Boot 3.0 upgrade initiated"
  - "Web application uses Spring MVC or WebFlux"
  - "Routes previously matched both with and without trailing slashes"
  - "HTTP 404 errors appear on requests with trailing slashes after upgrade"
---

# Spring MVC URL Trailing Slash Matching Correction

Update Spring MVC and WebFlux route definitions to account for Spring Framework 6.0's disabled trailing slash matching by default. Explicitly configure trailing slash behavior or update controller mappings to match expected request patterns without trailing slashes.

## Prompt

After upgrading to Spring Boot 3.0, trailing slash matching is disabled by default in Spring Framework 6.0. Review controller route mappings and test requests with and without trailing slashes. Update @GetMapping, @PostMapping, and other route annotations to explicitly match intended patterns, or configure trailing slash matching behavior globally if needed.

## Objective

Ensure URL routes match intended request patterns after trailing slash matching deprecation
## Applicable Signals

- Upgrade to Spring Boot 3.0 or Spring Framework 6.0
- Unexpected HTTP 404 responses on previously working URLs with trailing slashes
- Test failures on routes that worked in Spring Boot 2.x

## Contraindications

- Application does not use Spring MVC or WebFlux
- Trailing slash matching is not a concern for the application
- Routes are already explicitly configured for exact matching

## Intervention Moves

- Remove trailing slashes from route definitions to match Spring Framework 6.0 default behavior
- Add explicit routes for both trailing and non-trailing slash variants if backward compatibility is required
- Configure global trailing slash matching behavior via WebMvcConfigurer bean

## Workflow Steps

- {'step': 1, 'action': 'Identify affected controller routes', 'detail': 'Review all @GetMapping, @PostMapping, @PutMapping, @DeleteMapping, and other route annotations in the application'}
- {'step': 2, 'action': 'Test current behavior', 'detail': 'Send requests with and without trailing slashes to each route; document which now return HTTP 404'}
- {'step': 3, 'action': 'Choose trailing slash strategy', 'detail': 'Decide whether to: (a) remove trailing slashes from route definitions, (b) add explicit routes for both variants, or (c) configure global trailing slash matching behavior'}
- {'step': 4, 'action': 'Update route definitions or configuration', 'detail': 'Modify controller mappings or add WebMvcConfigurer bean to set trailing slash matching policy'}
- {'step': 5, 'action': 'Validate and test', 'detail': 'Verify all routes return expected HTTP 200 responses; confirm no unexpected HTTP 404 errors'}

## Constraints

- Spring Framework 6.0 or later required
- Changes apply only to Spring MVC and WebFlux applications
- Configuration must be applied consistently across all affected controllers

## Cautions

- Changing trailing slash behavior may affect existing client requests; coordinate with API consumers
- Test both trailing and non-trailing slash variants after changes
- Document the chosen trailing slash policy for future maintenance

## Output Contract

- All controller route mappings produce consistent HTTP 200 responses for intended request patterns; no unexpected HTTP 404 errors on valid routes; trailing slash behavior is explicit and documented in code or configuration

## Triggers

- Spring Boot 3.0 upgrade initiated
- Web application uses Spring MVC or WebFlux
- Routes previously matched both with and without trailing slashes
- HTTP 404 errors appear on requests with trailing slashes after upgrade
