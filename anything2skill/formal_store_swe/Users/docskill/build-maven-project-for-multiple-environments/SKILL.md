---
id: "99e36fa3-e639-56e3-83ce-1d0978b0e87b"
name: "Build Maven Project for Multiple Environments"
description: "Configure Maven profiles and toolchains to build and package applications for different target environments (dev, staging, production). Use when deploying to heterogeneous infrastructure or requiring environment-specific binaries."
version: "0.1.0"
tags:
  - "maven"
  - "build"
  - "profiles"
  - "toolchains"
  - "environment-specific"
  - "multi-environment"
triggers:
  - "Preparing releases for multiple platforms"
  - "Configuring CI/CD for environment-specific builds"
  - "Managing toolchain versions per environment"
---

# Build Maven Project for Multiple Environments

Configure Maven profiles and toolchains to build and package applications for different target environments (dev, staging, production). Use when deploying to heterogeneous infrastructure or requiring environment-specific binaries.

## Prompt

1. Define Maven profiles in pom.xml for each target environment, specifying environment-specific properties, dependencies, and plugin configurations.
2. Create or update toolchains.xml to map tool versions (compiler, JDK, etc.) per environment.
3. Activate the appropriate profile during build using -P flag or settings.xml activation rules.
4. Validate that the generated artifacts (JAR, WAR, etc.) contain correct environment-specific configurations.
5. Test artifacts in their target environment to confirm correctness before release.

## Objective

Generate environment-specific build artifacts
## Applicable Signals

- Multiple deployment targets identified
- Environment-specific configuration requirements
- Heterogeneous infrastructure or toolchain versions

## Contraindications

- Single-environment deployments
- Environment differences handled at runtime only

## Workflow Steps

- {'step': 1, 'action': 'Define Maven profiles in pom.xml', 'detail': 'Create <profile> blocks for each environment (dev, staging, production) with environment-specific properties and plugin configurations'}
- {'step': 2, 'action': 'Configure toolchains.xml', 'detail': 'Map tool versions (JDK, compiler, etc.) per environment to ensure consistent build tooling'}
- {'step': 3, 'action': 'Activate profile during build', 'detail': 'Use -P flag (mvn clean package -P production) or settings.xml activation rules'}
- {'step': 4, 'action': 'Validate generated artifacts', 'detail': 'Verify that artifacts contain correct environment-specific configurations'}
- {'step': 5, 'action': 'Test in target environment', 'detail': 'Deploy and test artifacts in their intended environment before release'}

## Constraints

- Profiles must be defined in pom.xml or settings.xml
- Toolchains.xml must exist and be properly configured
- Profile activation must be explicit or rule-based

## Cautions

- Ensure profile names are consistent across CI/CD and local builds
- Validate toolchain availability on all build agents
- Test artifacts in target environment before production release

## Output Contract

- Maven profiles and toolchain configuration (toolchains.xml) producing validated artifacts for each target environment, with confirmed environment-specific properties embedded in each artifact

## Triggers

- Preparing releases for multiple platforms
- Configuring CI/CD for environment-specific builds
- Managing toolchain versions per environment
