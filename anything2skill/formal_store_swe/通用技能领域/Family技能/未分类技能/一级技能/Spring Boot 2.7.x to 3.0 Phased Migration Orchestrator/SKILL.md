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
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
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

## 子技能目录
- [Add Framework Example to Repository](通用技能领域/Family技能/未分类技能/二级技能/Add Framework Example to Repository/SKILL.md) ｜ 适用：Structured workflow for integrating a new framework or provider example into the AgentOps repository. Guides contributors through creating a self-contained, documented example, generating website-visible documentation, and submitting a pull request for review and merge.
- [Initialize AgentOps Client with API Keys](通用技能领域/Family技能/未分类技能/二级技能/Initialize AgentOps Client with API Keys/SKILL.md) ｜ 适用：Load environment variables for API authentication and initialize the AgentOps client with session configuration, trace naming, and metadata tags. This skill sets up an authenticated AgentOps session for agent tracing and monitoring before any agent execution begins.
- [Logarithmic Scale Configuration](通用技能领域/Family技能/未分类技能/二级技能/Logarithmic Scale Configuration/SKILL.md) ｜ 适用：Initialize AgentOps monitoring with automatic or manual session creation, associating all subsequent events and API calls with a tracking session.
- [Start Managed Trace with Context](通用技能领域/Family技能/未分类技能/二级技能/Start Managed Trace with Context/SKILL.md) ｜ 适用：Create a new root span (trace) with optional name and tags, returning a TraceContext object for concurrent user-managed tracing sessions. Includes precondition validation and automatic initialization fallback.

## 选用规则（二级技能目录）
- 当目标、阶段或方法更接近 `Add Framework Example to Repository` 时，优先调用它。 线索：Contributor has a working framework or provider example ready to share, New integration example needs to be added to the repository, Framework support is being extended with a new provider variant, repository_contribution, example_integration
- 当目标、阶段或方法更接近 `Initialize AgentOps Client with API Keys` 时，优先调用它。 线索：Starting a new agent application that requires OpenAI and AgentOps integration, Before any agent execution or tracing begins, When environment variables are available and session is not yet initialized, initialization, authentication
- 当目标、阶段或方法更接近 `Logarithmic Scale Configuration` 时，优先调用它。 线索：Data spans multiple orders of magnitude, Logarithmic visual encoding is required, Tick labels and domain bounds need standardization, monitoring, session_management
- 当目标、阶段或方法更接近 `Start Managed Trace with Context` 时，优先调用它。 线索：Starting a new logical trace or session, Need to attach tags or custom trace names to a trace, Require concurrent independent traces managed by caller, trace_management, session_lifecycle

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Planning or executing a Spring Boot version upgrade from 2.7.x line to 3.0 or later
