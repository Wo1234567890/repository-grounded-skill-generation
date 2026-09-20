---
id: "83c71ae7-c88d-5e1b-974c-51a60333a86f"
name: "Maven Project Setup and Configuration"
description: "Establish a Maven project structure, configure the POM file, and apply build profiles. Use this when initializing a new Maven project or reconfiguring an existing one."
version: "0.1.0"
tags:
  - "maven"
  - "project-setup"
  - "pom-configuration"
  - "build-profiles"
  - "initialization"
triggers:
  - "Starting a new Maven project"
  - "Migrating an existing project to Maven"
  - "Reconfiguring project structure and build profiles"
---

# Maven Project Setup and Configuration

Establish a Maven project structure, configure the POM file, and apply build profiles. Use this when initializing a new Maven project or reconfiguring an existing one.

## Prompt

Follow these steps to set up and configure a Maven project:
1. Create or verify the project directory structure with src/main/java, src/test/java, src/main/resources, src/test/resources, and pom.xml at the root.
2. Define the POM file with project coordinates (groupId, artifactId, version), packaging type, name, and description.
3. Configure dependencies in the POM with appropriate scopes (compile, test, provided, runtime) and version specifications.
4. Set up build profiles in the POM to support different build scenarios (e.g., development, testing, production) with activation conditions.
5. Configure plugins in the POM for compilation, testing, packaging, and other build phases.
6. Review the Settings descriptor (settings.xml) to ensure repository URLs, credentials, and local repository path are correct.
7. Validate the POM syntax and structure using mvn validate before proceeding to build execution.

## Objective

Set up and configure a Maven project with correct POM and profile settings
## Applicable Signals

- Project initialization request
- POM file missing or incomplete
- Build profile requirements identified
- Plugin configuration needed

## Contraindications

- Troubleshooting runtime errors
- Debugging plugin execution during active builds
- Modifying plugin behavior mid-build cycle

## Workflow Steps

- {'step': 1, 'action': 'Create or verify Maven project directory structure', 'details': 'Ensure src/main/java, src/test/java, src/main/resources, and src/test/resources directories exist; place pom.xml at project root'}
- {'step': 2, 'action': 'Define POM project coordinates and metadata', 'details': 'Set groupId, artifactId, version, name, description, and packaging type in the POM'}
- {'step': 3, 'action': 'Configure dependencies in POM', 'details': 'Add required dependencies with scope (compile, test, provided, runtime) and version specifications'}
- {'step': 4, 'action': 'Set up build profiles', 'details': 'Define profiles for different build scenarios (e.g., dev, test, prod) with activation conditions and profile-specific configurations'}
- {'step': 5, 'action': 'Configure plugins in POM', 'details': 'Add and configure plugins for compilation, testing, packaging, and other build phases'}
- {'step': 6, 'action': 'Review Settings descriptor', 'details': 'Verify repository URLs, credentials, and local repository path in settings.xml'}
- {'step': 7, 'action': 'Validate POM and settings', 'details': 'Check XML syntax and structure; run mvn validate to confirm POM correctness'}

## Constraints

- POM file must be valid XML
- Project coordinates (groupId, artifactId, version) must be defined
- Directory structure must follow Maven conventions

## Cautions

- Ensure all dependencies are available in configured repositories before proceeding to build
- Validate profile activation conditions to avoid unintended build variations
- Review plugin versions for compatibility with the target Java version

## Output Contract

- Valid POM file with correct project descriptor, profiles, and plugin configurations ready for build execution. The project structure conforms to Maven conventions, all dependencies are declared, and the POM passes validation.

## Triggers

- Starting a new Maven project
- Migrating an existing project to Maven
- Reconfiguring project structure and build profiles
