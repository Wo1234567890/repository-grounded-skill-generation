---
id: "ceab02d7-1cd5-5af7-a05c-1b77f2831231"
name: "Downgrade Servlet API for Jetty Compatibility"
description: "Set the `jakarta-servlet.version` property to 5.0 when using Jetty with Spring Boot 3.0, since Jetty does not yet support Servlet 6.0. This is a targeted workaround to enable Jetty as the embedded server during Spring Boot 3.0 migration."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "jetty"
  - "servlet-api"
  - "version-downgrade"
  - "embedded-server"
  - "jakarta-ee"
triggers:
  - "Spring Boot 3.0 migration initiated with Jetty as embedded server"
  - "Servlet 6.0 incompatibility error occurs at runtime or build time"
  - "Jetty dependency is present in project"
---

# Downgrade Servlet API for Jetty Compatibility

Set the `jakarta-servlet.version` property to 5.0 when using Jetty with Spring Boot 3.0, since Jetty does not yet support Servlet 6.0. This is a targeted workaround to enable Jetty as the embedded server during Spring Boot 3.0 migration.

## Prompt

If your Spring Boot 3.0 application uses Jetty as the embedded server and encounters Servlet 6.0 compatibility errors, configure the `jakarta-servlet.version` property to 5.0 in your build configuration (Maven pom.xml or Gradle build.gradle) to downgrade the Servlet API version. This allows Jetty to run on the older Servlet 5.0 API until Jetty adds Servlet 6.0 support.

## Objective

Enable Jetty support in Spring Boot 3.0 by downgrading Servlet API version
## Applicable Signals

- Jetty selected as embedded web server
- Build or runtime error mentioning Servlet 6.0 incompatibility
- Spring Boot 3.0 upgrade in progress

## Contraindications

- Using Tomcat or other servers that support Servlet 6.0
- Jetty is not a project dependency
- Application requires Servlet 6.0 features not available in 5.0

## Intervention Moves

- Override jakarta-servlet.version property to 5.0
- Rebuild application with downgraded Servlet API
- Verify Jetty startup without compatibility errors

## Workflow Steps

- {'step': 1, 'action': 'Identify that Jetty is the embedded server in your Spring Boot 3.0 project'}
- {'step': 2, 'action': 'Locate your build configuration file (pom.xml for Maven or build.gradle for Gradle)'}
- {'step': 3, 'action': 'Add or override the `jakarta-servlet.version` property to `5.0`'}
- {'step': 4, 'action': 'Rebuild and restart the application'}
- {'step': 5, 'action': 'Verify that Jetty starts without Servlet 6.0 compatibility errors'}

## Constraints

- Property must be set before application startup
- Applies only to Jetty; other servers should use Servlet 6.0
- Servlet 5.0 API may lack features introduced in Servlet 6.0

## Cautions

- This is a temporary workaround; monitor Jetty releases for Servlet 6.0 support
- Ensure application code does not depend on Servlet 6.0-specific features
- Downgrading may affect compatibility with other Spring Boot 3.0 components

## Output Contract

- Jetty starts successfully with Spring Boot 3.0; no Servlet 6.0 compatibility errors; application runs on Servlet 5.0 API without runtime failures.

## Triggers

- Spring Boot 3.0 migration initiated with Jetty as embedded server
- Servlet 6.0 incompatibility error occurs at runtime or build time
- Jetty dependency is present in project
