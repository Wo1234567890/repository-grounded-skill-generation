---
id: "5b89c0b3-be95-5d38-bd12-c76c956f8ce5"
name: "Spring Boot 2.7.x to 3.0 Phased Migration Orchestrator"
description: "Orchestrates a multi-phase, staged migration of Spring Boot applications from 2.7.x to 3.0, covering pre-upgrade validation, core upgrade execution, and post-upgrade verification. Ensures safe handling of Java 17+ requirement, Jakarta EE namespace migration, Spring Framework 6.0 API changes, and dependency compatibility."
version: "0.1.0"
tags:
  - "spring-boot"
  - "version-upgrade"
  - "migration"
  - "framework"
  - "java"
  - "jakarta-ee"
triggers:
  - "Planning or executing a Spring Boot version upgrade from 2.7.x line to 3.0 or later"
---

# Spring Boot 2.7.x to 3.0 Phased Migration Orchestrator

Orchestrates a multi-phase, staged migration of Spring Boot applications from 2.7.x to 3.0, covering pre-upgrade validation, core upgrade execution, and post-upgrade verification. Ensures safe handling of Java 17+ requirement, Jakarta EE namespace migration, Spring Framework 6.0 API changes, and dependency compatibility.

## Prompt

Execute a phased Spring Boot version upgrade from 2.7.x to 3.0. Follow the sequence: (1) upgrade to latest 2.7.x, (2) review and update dependencies, (3) validate system requirements (Java 17+), (4) review and address deprecations, (5) update Spring Boot version in build configuration, (6) migrate configuration properties (application.yml/properties), (7) update Spring Framework 6.0 and Jakarta EE imports (javax.* to jakarta.*), (8) address core changes (image banner, logging date format, YAML parser removal), (9) update web application configuration (URL matching, HTTP headers, graceful shutdown), (10) migrate actuator and metrics configuration, (11) update data access layer (Hibernate, R2DBC, Elasticsearch, database drivers), (12) update Spring Security, Batch, and Session configurations, (13) run full test suite and verify all deprecated APIs are replaced.

## Objective

Complete a safe, phased migration from Spring Boot 2.x to 3.0 with zero deprecated API usage and full test coverage
## Applicable Signals

- Planning a Spring Boot version upgrade from 2.7.x line
- Executing a Spring Boot version upgrade from 2.7.x line
- Application currently on Spring Boot 2.7.x
- Need to adopt Spring Boot 3.0 features or security updates

## Contraindications

- Application already on Spring Boot 3.0 or later
- Upgrading within 2.x minor versions only
- Performing a downgrade to earlier Spring Boot versions
- Application has custom Spring Boot core modifications

## Workflow Steps

- {'phase': 'pre_upgrade', 'step': 1, 'action': 'Upgrade to latest 2.7.x version', 'rationale': 'Ensures all 2.x deprecation warnings are visible before major version jump'}
- {'phase': 'pre_upgrade', 'step': 2, 'action': 'Review and document all dependencies', 'rationale': 'Identify which dependencies have 3.0-compatible versions'}
- {'phase': 'pre_upgrade', 'step': 3, 'action': 'Validate system requirements (Java version, OS compatibility)', 'rationale': 'Spring Boot 3.0 requires Java 17+; earlier versions not supported'}
- {'phase': 'pre_upgrade', 'step': 4, 'action': 'Review and address all deprecations from Spring Boot 2.x', 'rationale': 'Deprecated APIs are removed in 3.0; must be replaced before upgrade'}
- {'phase': 'upgrade', 'step': 5, 'action': 'Update Spring Boot version to 3.0 in build configuration', 'rationale': 'Primary version bump; triggers dependency resolution'}
- {'phase': 'upgrade', 'step': 6, 'action': 'Migrate configuration properties (application.yml/properties)', 'rationale': 'Property names and structures changed; must align with 3.0 schema'}
- {'phase': 'upgrade', 'step': 7, 'action': 'Update Spring Framework 6.0 and Jakarta EE imports', 'rationale': 'javax.* packages replaced with jakarta.*; Spring Framework 6.0 API changes'}
- {'phase': 'upgrade', 'step': 8, 'action': 'Address core changes (image banner, logging date format, YAML parser removal)', 'rationale': 'Specific APIs and behaviors removed or changed in 3.0'}
- {'phase': 'upgrade', 'step': 9, 'action': 'Update web application configuration (URL matching, HTTP headers, graceful shutdown)', 'rationale': 'Spring MVC/WebFlux behavior changes; server configuration updates required'}
- {'phase': 'upgrade', 'step': 10, 'action': 'Migrate actuator and metrics configuration', 'rationale': 'Endpoint names changed, sanitization rules updated, Micrometer instrumentation deprecated'}
- {'phase': 'upgrade', 'step': 11, 'action': 'Update data access layer (Hibernate, R2DBC, Elasticsearch, database drivers)', 'rationale': 'ORM and database client versions updated; property names changed'}
- {'phase': 'upgrade', 'step': 12, 'action': 'Update Spring Security, Batch, and Session configurations', 'rationale': 'Reactive user details, SAML2, batch processing, and session store changes'}

## Constraints

- Java 17 or later must be available
- All transitive dependencies must have 3.0-compatible versions
- Custom Spring Boot extensions must be reviewed for compatibility
- Database schema and migration tools must support target database versions

## Cautions

- Jakarta EE namespace change (javax.* to jakarta.*) affects all enterprise libraries
- Spring Framework 6.0 introduces breaking changes in core APIs
- Micrometer instrumentation deprecation requires metrics configuration review
- Graceful shutdown phases changed; review server shutdown behavior
- Some dependencies may not have 3.0 versions; evaluate alternatives or stay on 2.x

## Output Contract

- Application successfully compiles
- All unit and integration tests pass
- No deprecated Spring Boot 2.x or Spring Framework 5.x APIs remain in codebase
- Application runs on Spring Boot 3.0 with expected behavior

## Triggers

- Planning or executing a Spring Boot version upgrade from 2.7.x line to 3.0 or later
