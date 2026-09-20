---
name: spring-boot-3-jakarta-migration
description: Migrate Spring Boot 2/Java 8 services to Spring Boot 3/modern Java by coordinating dependency, Jakarta namespace, Security 6, Hibernate 6, and RestClient changes with compile-and-test validation.
---

# Spring Boot 3 and Jakarta Migration

## When to Use

Use this skill for coordinated migration of a Spring Boot 2.x service to Spring Boot 3.x and a modern JDK where persistence, validation, servlet APIs, security configuration, and outbound HTTP clients all need compatible updates.

## Workflow

1. **Upgrade the build baseline first.** Update the Spring Boot parent/plugin and Java version together, then review explicit dependencies for versions that conflict with the new platform.
2. **Migrate Java EE namespaces systematically.** Search all source files for `javax.persistence`, `javax.validation`, and `javax.servlet` and replace them with their `jakarta.*` equivalents. Re-scan until legacy imports are gone.
3. **Handle Hibernate through the Jakarta model.** For ordinary Spring Boot-managed JPA code, correct Jakarta persistence imports and compatible dependencies are the first requirement; avoid unnecessary custom Hibernate configuration unless the repository already depends on it.
4. **Rewrite Spring Security configuration to the component model.** Replace `WebSecurityConfigurerAdapter` with a `SecurityFilterChain` bean. Use the current lambda-style DSL, `authorizeHttpRequests`, and `requestMatchers` while preserving existing endpoint authorization behavior.
5. **Migrate outbound HTTP calls deliberately.** Replace `RestTemplate` usage with an injected `RestClient.Builder`/`RestClient`, preserving base URL, headers, HTTP methods, request bodies, response types, and exception behavior.
6. **Search for deprecated APIs after the mechanical migration.** Namespace replacement alone is not enough; compile errors often reveal renamed security/configuration APIs.
7. **Validate in two gates.** Run a clean compile first, then the full unit-test suite. Fix compilation and runtime/test regressions before adding optional modernization.

## Proven Pattern from Successful Trajectories

Across successful no-skill runs, the reliable sequence was: build-version update → `javax` to `jakarta` sweep → SecurityFilterChain migration → RestClient migration → repository-wide searches for leftovers → compile/test validation. Keeping the migration in coherent layers reduced the chance of mixing unrelated failures.

## Common Failure Modes

- Updating Spring Boot without migrating `javax.*` imports.
- Replacing security classes but not deprecated matcher/authorization methods.
- Replacing `RestTemplate` syntax without preserving the old request semantics.
- Declaring migration complete before a repository-wide search for legacy APIs.
