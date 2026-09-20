---
id: "c33c9e56-8d98-54f3-8d73-8cbfa42e9b1e"
name: "Spring WebFlux Trailing Slash Configuration"
description: "Configure Spring WebFlux to restore trailing slash matching behavior during Spring Boot 3.0 migration. Use when URL routing fails due to removed automatic trailing slash normalization in Spring Boot 3.0."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "url-routing"
  - "trailing-slash"
  - "configuration-override"
  - "backward-compatibility"
  - "spring-webflux"
triggers:
  - "URL routes with trailing slashes return 404 after Spring Boot 3.0 upgrade"
  - "Application requires backward compatibility with slash-sensitive endpoints"
  - "Refactoring all routes to handle both slash and non-slash variants is not feasible"
  - "Spring WebFlux framework detected"
examples:
  - input: "Spring Boot 3.0 application with Spring WebFlux; endpoint /api/users/ returns 404 after upgrade"
    output: "WebFluxConfigurer bean with configurePathMatching() override deployed; /api/users/ routes successfully"
    notes: "Use this pattern for Spring WebFlux applications"
---

# Spring WebFlux Trailing Slash Configuration

Configure Spring WebFlux to restore trailing slash matching behavior during Spring Boot 3.0 migration. Use when URL routing fails due to removed automatic trailing slash normalization in Spring Boot 3.0.

## Prompt

Implement a @Configuration class that restores trailing slash matching for Spring WebFlux. Implement WebFluxConfigurer and override configurePathMatching(). Call configurer.setUseTrailingSlashMatch(true) to enable the legacy behavior. Deploy this bean to your application context.

## Objective

restore_url_matching_compatibility
## Applicable Signals

- Spring Boot 3.0 upgrade in progress
- Trailing slash requests failing with 404 errors
- Legacy endpoint contracts require slash sensitivity
- Spring WebFlux framework in use

## Contraindications

- Application has already refactored all routes to handle both slash and non-slash variants
- Using explicit @GetMapping multi-path declarations is preferred (e.g., @GetMapping({"/some/greeting", "/some/greeting/"}))
- Proxy or servlet filter already handles trailing slash rewrites
- Spring MVC is the web framework (use WebMvcConfigurer instead)

## Intervention Moves

- Create @Configuration class implementing WebFluxConfigurer
- Override configurePathMatching(PathMatchConfigurer configurer)
- Call configurer.setUseTrailingSlashMatch(true)
- Register bean in application context

## Workflow Steps

- {'step': 1, 'action': 'Verify Spring WebFlux framework', 'detail': 'Confirm application uses Spring WebFlux (not Spring MVC)'}
- {'step': 2, 'action': 'Create a @Configuration class', 'detail': 'Define a new configuration class annotated with @Configuration'}
- {'step': 3, 'action': 'Implement WebFluxConfigurer', 'detail': 'Implement the WebFluxConfigurer interface in the configuration class'}
- {'step': 4, 'action': 'Override configurePathMatching method', 'detail': 'Override configurePathMatching(PathMatchConfigurer configurer) method'}
- {'step': 5, 'action': 'Enable trailing slash matching', 'detail': 'Call configurer.setUseTrailingSlashMatch(true) within the override'}
- {'step': 6, 'action': 'Deploy and test', 'detail': 'Ensure the bean is registered in the application context and test trailing slash requests'}

## Constraints

- Configuration must be applied before request routing occurs
- Only use WebFluxConfigurer for Spring WebFlux applications; use WebMvcConfigurer for Spring MVC
- This is a temporary compatibility measure; refactoring routes is the recommended long-term solution

## Cautions

- This restores legacy behavior and defers the need to refactor endpoints; plan a migration path to explicit route declarations
- Performance impact is minimal but the configuration adds a layer of indirection to path matching

## Output Contract

- WebFluxConfigurer bean successfully deployed to application context
- Trailing slash requests route correctly without 404 errors
- Backward compatibility with slash-sensitive endpoints restored

## Example Therapist Responses

### Example 1

- Client/Input: Spring Boot 3.0 application with Spring WebFlux; endpoint /api/users/ returns 404 after upgrade
- Therapist/Output: WebFluxConfigurer bean with configurePathMatching() override deployed; /api/users/ routes successfully
- Notes: Use this pattern for Spring WebFlux applications

## Triggers

- URL routes with trailing slashes return 404 after Spring Boot 3.0 upgrade
- Application requires backward compatibility with slash-sensitive endpoints
- Refactoring all routes to handle both slash and non-slash variants is not feasible
- Spring WebFlux framework detected

## Examples

### Example 1

Input:

  Spring Boot 3.0 application with Spring WebFlux; endpoint /api/users/ returns 404 after upgrade

Output:

  WebFluxConfigurer bean with configurePathMatching() override deployed; /api/users/ routes successfully

Notes:

  Use this pattern for Spring WebFlux applications
