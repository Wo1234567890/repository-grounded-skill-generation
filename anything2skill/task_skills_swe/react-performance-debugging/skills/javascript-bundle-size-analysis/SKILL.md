---
id: "ff0f313d-ebd7-57f1-933c-beefb654f03a"
name: "JavaScript Bundle Size Analysis"
description: "Manage Maven classloading behavior and multi-module project structure to resolve dependency conflicts and ensure correct class resolution across module boundaries."
version: "0.1.1"
tags:
  - "maven"
  - "classloading"
  - "multi-module"
  - "dependency-management"
  - "build-configuration"
triggers:
  - "application bundle size is unknown or unquantified"
  - "bundle size is suspected to be large"
  - "before and after optimization comparison is needed"
  - "performance regression detection in CI/CD"
---

# JavaScript Bundle Size Analysis

Manage Maven classloading behavior and multi-module project structure to resolve dependency conflicts and ensure correct class resolution across module boundaries.

## Prompt

When working with multi-module Maven builds, configure parent-child pom relationships, define dependency management sections, and verify classloading order to prevent ClassNotFoundException and version conflicts. Ensure each module declares its dependencies explicitly and parent pom centralizes version management.

## Objective

Resolve classloading and multi-module dependency issues
## Applicable Signals

- Multiple pom.xml files in project hierarchy
- Runtime class resolution failures
- Conflicting transitive dependency versions

## Contraindications

- Single-module projects with no dependency conflicts
- Using alternative build systems (Gradle, Bazel)
- Projects without parent-child module relationships

## Workflow Steps

- {'step': 1, 'action': "Define parent pom.xml with packaging type 'pom' and list all child modules"}
- {'step': 2, 'action': 'Create dependencyManagement section in parent pom to centralize version declarations'}
- {'step': 3, 'action': 'Configure each child module pom.xml with parent reference and explicit dependencies'}
- {'step': 4, 'action': 'Verify classloading order by running mvn dependency:tree to inspect resolved versions'}
- {'step': 5, 'action': 'Test multi-module build with mvn clean install to confirm no ClassNotFoundException'}

## Constraints

- Parent pom must be defined before child modules reference it
- Dependency management section must precede actual dependency declarations
- Module order in parent pom affects build sequence

## Cautions

- Circular module dependencies will cause build failure
- Overriding parent dependency versions in child modules can cause unexpected behavior
- Classloader isolation may hide transitive dependency issues

## Output Contract

- Multi-module pom.xml structure with correct parent-child relationships, centralized dependency management section, and verified classloading order confirmed via dependency tree output and successful build execution.

## Triggers

- application bundle size is unknown or unquantified
- bundle size is suspected to be large
- before and after optimization comparison is needed
- performance regression detection in CI/CD
