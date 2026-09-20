---
id: "db5c7243-ab3f-5ca6-a8a4-f7f4da5dbf60"
name: "Spring Boot 3.0 Core Deprecation Remediation"
description: "Identify and resolve three core deprecations removed in Spring Boot 3.0: image banner removal, YamlJsonParser removal, and @ConstructorBinding annotation changes. Replaces removed functionality with supported alternatives to unblock upgrade."
version: "0.1.0"
tags:
  - "spring-boot-3.0"
  - "migration"
  - "deprecation"
  - "core-changes"
  - "code-remediation"
triggers:
  - "Upgrading Spring Boot 2.x application to 3.0"
  - "Codebase contains image banner files (banner.gif, banner.jpg, banner.png)"
  - "Direct usage of YamlJsonParser detected"
  - "@ConstructorBinding annotation found at type level on @ConfigurationProperties classes"
---

# Spring Boot 3.0 Core Deprecation Remediation

Identify and resolve three core deprecations removed in Spring Boot 3.0: image banner removal, YamlJsonParser removal, and @ConstructorBinding annotation changes. Replaces removed functionality with supported alternatives to unblock upgrade.

## Prompt

When upgrading a Spring Boot 2.x application to 3.0, scan the codebase for three core removals: (1) image-based banners (banner.gif, banner.jpg, banner.png) — replace with text-based banner.txt; (2) direct YamlJsonParser usage — migrate to alternative JsonParser implementations; (3) @ConstructorBinding at type level on @ConfigurationProperties classes with autowired constructor dependencies — add @Autowired annotation to the constructor parameter. Validate that the application compiles and runs without deprecation errors.

## Objective

Eliminate core deprecations and removed features blocking Spring Boot 3.0 upgrade
## Applicable Signals

- Build failure due to removed YamlJsonParser class
- Image banner files present in resources directory
- @ConstructorBinding deprecation warning in IDE or build log
- Autowiring of dependencies into @ConfigurationProperties constructor

## Contraindications

- Application already uses banner.txt exclusively
- No YamlJsonParser usage in codebase
- @Autowired already applied to @ConfigurationProperties constructor parameters
- Application targets Spring Boot 2.7.x or earlier (no migration needed)

## Workflow Steps

- {'step': 1, 'action': 'Scan project resources for image banner files', 'detail': 'Search for banner.gif, banner.jpg, banner.png in src/main/resources and subdirectories'}
- {'step': 2, 'action': 'Replace image banners with text-based banner.txt', 'detail': 'Create banner.txt with equivalent ASCII art or text content; delete image banner files'}
- {'step': 3, 'action': 'Search codebase for YamlJsonParser usage', 'detail': 'Use IDE search or grep to find direct instantiation or import of YamlJsonParser'}
- {'step': 4, 'action': 'Migrate YamlJsonParser to alternative JsonParser', 'detail': 'Replace with StandardJsonParser, GsonJsonParser, or other JsonParser implementation compatible with use case'}
- {'step': 5, 'action': 'Identify @ConfigurationProperties classes with constructor injection', 'detail': 'Find @ConfigurationProperties classes that autowire dependencies into constructor'}
- {'step': 6, 'action': 'Add @Autowired annotation to constructor parameters', 'detail': 'Annotate constructor parameters with @Autowired to prevent property binding misidentification'}
- {'step': 7, 'action': 'Compile and test application', 'detail': 'Run full build and integration tests to confirm no deprecation errors and functionality preserved'}

## Constraints

- Must complete before upgrading Spring Boot version in pom.xml or build.gradle
- All three remediation steps must be validated independently
- Replacement JsonParser must be compatible with existing JSON parsing logic

## Cautions

- Image banner removal is non-functional; ensure banner.txt provides equivalent visual output
- JsonParser replacement may require testing if custom parsing behavior was relied upon
- @Autowired addition changes constructor binding semantics; verify property binding still works as expected

## Output Contract

- Image banners replaced with banner.txt; YamlJsonParser calls migrated to alternative JsonParser implementations; @Autowired annotations added to @ConfigurationProperties constructor dependencies; application compiles without errors and runs without deprecation warnings.

## Triggers

- Upgrading Spring Boot 2.x application to 3.0
- Codebase contains image banner files (banner.gif, banner.jpg, banner.png)
- Direct usage of YamlJsonParser detected
- @ConstructorBinding annotation found at type level on @ConfigurationProperties classes
