---
id: "bdc15fe0-09b2-59ba-ad62-43dde6a0a2d1"
name: "Spring MVC/WebFlux URL Trailing Slash Matching Configuration"
description: "Correct URL route matching behavior after trailing slash default change in Spring Framework 6.0. Resolves 404 errors on trailing slash URL variants by either re-enabling trailing slash matching via WebMvcConfigurer configuration or updating route definitions to match the new default (trailing slash matching disabled)."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "spring-framework-6"
  - "url-routing"
  - "web-configuration"
  - "breaking-change"
triggers:
  - "Web application upgraded to Spring Boot 3.0"
  - "Controller endpoints receive HTTP 404 errors on URLs with trailing slashes"
  - "Testing reveals URL matching regressions after upgrade"
---

# Spring MVC/WebFlux URL Trailing Slash Matching Configuration

Correct URL route matching behavior after trailing slash default change in Spring Framework 6.0. Resolves 404 errors on trailing slash URL variants by either re-enabling trailing slash matching via WebMvcConfigurer configuration or updating route definitions to match the new default (trailing slash matching disabled).

## Prompt

After upgrading to Spring Boot 3.0 with Spring Framework 6.0, trailing slash matching is disabled by default. Review controller endpoint definitions and test URL routing. If endpoints previously matched both '/path' and '/path/', configure trailing slash matching explicitly or update route definitions to match the new default behavior.

## Objective

Correct URL route matching behavior after trailing slash default change in Spring Framework 6.0
## Applicable Signals

- Spring Framework 6.0 dependency detected
- WebMvcConfigurer or WebFluxConfigurer configuration present
- Test failures on trailing slash URL variants
- HTTP 404 errors on URLs with trailing slashes after upgrade

## Contraindications

- Application intentionally requires trailing slash matching behavior
- Non-web application or no REST/MVC controllers
- Spring Boot 2.x or earlier (trailing slash matching still enabled by default)

## Intervention Moves

- Override configurePathMatch() in WebMvcConfigurer to re-enable trailing slash matching
- Update @RequestMapping, @GetMapping, @PostMapping route definitions to explicitly include or exclude trailing slash variants
- Add integration tests to validate both trailing and non-trailing slash URL patterns

## Workflow Steps

- {'step': 1, 'action': 'Identify affected controller endpoints', 'detail': 'Review all @RestController and @Controller classes for @RequestMapping, @GetMapping, @PostMapping, and similar annotations'}
- {'step': 2, 'action': 'Test current URL matching behavior', 'detail': 'Run integration or end-to-end tests to confirm which URLs return 404 errors after upgrade'}
- {'step': 3, 'action': 'Choose resolution strategy', 'detail': 'Either (a) explicitly configure trailing slash matching in WebMvcConfigurer, or (b) update route definitions to match new default'}
- {'step': 4, 'action': 'Implement configuration or route updates', 'detail': 'If re-enabling trailing slash matching: override configurePathMatch() in WebMvcConfigurer; if updating routes: add trailing slash variants or remove them consistently'}
- {'step': 5, 'action': 'Validate routing in test suite', 'detail': 'Run full test suite to confirm endpoints match expected URL patterns and no new 404 errors are introduced'}

## Constraints

- Change applies only to Spring Framework 6.0+ (Spring Boot 3.0+)
- Affects both Spring MVC and WebFlux applications
- Requires review of all @RequestMapping, @GetMapping, @PostMapping, etc. definitions

## Cautions

- Changing trailing slash matching behavior may affect existing client code or API contracts
- Test all URL patterns thoroughly before deploying to production
- Document any intentional changes to routing behavior for API consumers

## Output Contract

- Controller endpoints match both trailing and non-trailing slash URLs as intended
- HTTP 404 errors on trailing slash variants are resolved
- Routing behavior is validated in test suite and documented

## Triggers

- Web application upgraded to Spring Boot 3.0
- Controller endpoints receive HTTP 404 errors on URLs with trailing slashes
- Testing reveals URL matching regressions after upgrade
