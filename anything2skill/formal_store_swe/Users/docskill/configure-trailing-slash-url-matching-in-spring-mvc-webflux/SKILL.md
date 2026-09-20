---
id: "3f5e0e83-f308-5ccd-9232-7a63a98b7348"
name: "Configure Trailing Slash URL Matching in Spring MVC/WebFlux"
description: "Restore Spring Boot 2.x trailing-slash matching behavior by configuring PathMatchConfigurer in WebMvcConfigurer or WebFluxConfigurer. Use when migrating to Spring Boot 3.0 and existing routes depend on trailing-slash tolerance."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "url-routing"
  - "backward-compatibility"
  - "spring-mvc"
  - "spring-webflux"
  - "configuration"
triggers:
  - "Spring Boot 3.0 migration initiated"
  - "Existing application routes fail with 404 on trailing-slash variants"
  - "Routes were previously matched with or without trailing slash in Spring Boot 2.x"
examples:
  - input: "Spring MVC application with route /api/users that previously matched both /api/users and /api/users/ in Spring Boot 2.x"
    output: "After configuration, both /api/users and /api/users/ invoke the same handler without 404 error"
    notes: "Configuration class implements WebMvcConfigurer and sets setUseTrailingSlashMatch(true)"
  - input: "Spring WebFlux application with route /api/data that fails with 404 when accessed as /api/data/ after Spring Boot 3.0 upgrade"
    output: "After configuration, /api/data/ resolves successfully to the same handler as /api/data"
    notes: "Configuration class implements WebFluxConfigurer and sets setUseTrailingSlashMatch(true)"
---

# Configure Trailing Slash URL Matching in Spring MVC/WebFlux

Restore Spring Boot 2.x trailing-slash matching behavior by configuring PathMatchConfigurer in WebMvcConfigurer or WebFluxConfigurer. Use when migrating to Spring Boot 3.0 and existing routes depend on trailing-slash tolerance.

## Prompt

To enable trailing-slash URL matching for backward compatibility during Spring Boot 3.0 migration:

1. For Spring MVC: Create a @Configuration class implementing WebMvcConfigurer and override configurePathMatch() to call configurer.setUseTrailingSlashMatch(true).
2. For Spring WebFlux: Create a @Configuration class implementing WebFluxConfigurer and override configurePathMatching() to call configurer.setUseTrailingSlashMatch(true).
3. This allows routes to match both with and without trailing slashes, preventing 404 errors on slash-variant requests.
4. Apply this only as a temporary migration bridge; consider explicit route declarations (@GetMapping with multiple paths) for new code.

## Objective

Enable trailing-slash URL matching for backward compatibility
## Applicable Signals

- HTTP 404 errors on URLs with trailing slashes after upgrade
- Application logs show path mismatch errors
- Controller handlers not invoked for slash-variant requests

## Contraindications

- New application design intentionally enforces strict URL matching
- Trailing-slash inconsistency is desired behavior for API versioning or routing logic
- Application has already migrated routes to explicit multi-path declarations

## Workflow Steps

- {'step': 1, 'action': 'Identify framework in use', 'detail': 'Determine whether application uses Spring MVC or Spring WebFlux'}
- {'step': 2, 'action': 'Create configuration class', 'detail': 'Declare a new @Configuration class implementing WebMvcConfigurer (MVC) or WebFluxConfigurer (WebFlux)'}
- {'step': 3, 'action': 'Override path match configuration method', 'detail': 'For MVC: override configurePathMatch(PathMatchConfigurer configurer); for WebFlux: override configurePathMatching(PathMatchConfigurer configurer)'}
- {'step': 4, 'action': 'Enable trailing-slash matching', 'detail': 'Call configurer.setUseTrailingSlashMatch(true) within the override method'}
- {'step': 5, 'action': 'Test route resolution', 'detail': 'Verify that routes resolve correctly both with and without trailing slashes; confirm no 404 errors on slash variants'}

## Constraints

- Configuration must be applied at application startup
- Requires @Configuration annotation and appropriate WebMvcConfigurer or WebFluxConfigurer interface implementation
- Only affects request path matching; does not modify response headers or redirect behavior

## Cautions

- This is a temporary migration bridge; consider refactoring to explicit route declarations for long-term maintainability
- Enabling trailing-slash matching may mask URL design inconsistencies that should be addressed in the application
- Do not use this as a permanent solution for new Spring Boot 3.0 applications

## Output Contract

- Routes with and without trailing slashes both resolve to the same handler
- No 404 errors on trailing-slash variants
- Application behavior matches Spring Boot 2.x trailing-slash tolerance during migration window

## Example Executions

### Example 1

- Input: Spring MVC application with route /api/users that previously matched both /api/users and /api/users/ in Spring Boot 2.x
- Output: After configuration, both /api/users and /api/users/ invoke the same handler without 404 error
- Notes: Configuration class implements WebMvcConfigurer and sets setUseTrailingSlashMatch(true)

### Example 2

- Input: Spring WebFlux application with route /api/data that fails with 404 when accessed as /api/data/ after Spring Boot 3.0 upgrade
- Output: After configuration, /api/data/ resolves successfully to the same handler as /api/data
- Notes: Configuration class implements WebFluxConfigurer and sets setUseTrailingSlashMatch(true)

## Triggers

- Spring Boot 3.0 migration initiated
- Existing application routes fail with 404 on trailing-slash variants
- Routes were previously matched with or without trailing slash in Spring Boot 2.x

## Examples

### Example 1

Input:

  Spring MVC application with route /api/users that previously matched both /api/users and /api/users/ in Spring Boot 2.x

Output:

  After configuration, both /api/users and /api/users/ invoke the same handler without 404 error

Notes:

  Configuration class implements WebMvcConfigurer and sets setUseTrailingSlashMatch(true)

### Example 2

Input:

  Spring WebFlux application with route /api/data that fails with 404 when accessed as /api/data/ after Spring Boot 3.0 upgrade

Output:

  After configuration, /api/data/ resolves successfully to the same handler as /api/data

Notes:

  Configuration class implements WebFluxConfigurer and sets setUseTrailingSlashMatch(true)
