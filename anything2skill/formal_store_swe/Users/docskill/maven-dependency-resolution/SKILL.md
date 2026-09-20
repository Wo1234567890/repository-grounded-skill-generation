---
id: "fa11744d-3317-5b61-9bc3-1be7bb6a91a0"
name: "Maven Dependency Resolution"
description: "Workflow to declare, manage, and resolve project dependencies using Maven's dependency mechanism, including optional dependencies and exclusions."
version: "0.1.0"
tags:
  - "maven"
  - "dependency-management"
  - "pom-configuration"
  - "build-configuration"
triggers:
  - "Adding a new dependency to a Maven project"
  - "Updating an existing dependency version"
  - "Excluding transitive dependencies to resolve conflicts"
  - "Marking a dependency as optional"
---

# Maven Dependency Resolution

Workflow to declare, manage, and resolve project dependencies using Maven's dependency mechanism, including optional dependencies and exclusions.

## Prompt

Use this skill when you need to add, update, or configure dependencies in a Maven project. Follow the dependency mechanism to declare dependencies in pom.xml, apply optional flags when appropriate, and use exclusion rules to prevent unwanted transitive dependencies. Verify the dependency tree resolves correctly after configuration.

## Objective

Manage and resolve project dependencies correctly
## Applicable Signals

- New library or framework requirement identified
- Dependency version upgrade needed
- Transitive dependency conflict detected
- Optional dependency use case identified

## Contraindications

- Do not use for resolving transitive dependency conflicts at runtime
- Do not use for debugging repository connectivity issues
- Do not use for managing repository mirrors or authentication

## Workflow Steps

- {'step': 1, 'action': 'Identify the dependency to add or modify', 'detail': 'Determine groupId, artifactId, and version from the library documentation or Maven Central Repository'}
- {'step': 2, 'action': 'Declare the dependency in pom.xml', 'detail': 'Add a <dependency> block in the <dependencies> section with groupId, artifactId, and version'}
- {'step': 3, 'action': 'Apply optional or exclusion rules if needed', 'detail': 'Mark dependency as <optional>true</optional> if it should not be transitive, or add <exclusions> to block unwanted transitive dependencies'}
- {'step': 4, 'action': 'Verify dependency resolution', 'detail': 'Run Maven dependency tree command to confirm all dependencies resolve correctly and no conflicts remain'}

## Constraints

- pom.xml must be valid XML
- Dependency coordinates (groupId, artifactId, version) must be correct
- Maven must have access to configured repositories

## Cautions

- Excluding too many transitive dependencies may break functionality
- Optional dependencies still require explicit declaration in dependent projects
- Version conflicts in transitive dependencies may require additional exclusion rules

## Output Contract

- pom.xml with correctly declared dependencies, optional flags, and exclusion rules; successful dependency tree resolution with no unresolved or conflicting dependencies

## Triggers

- Adding a new dependency to a Maven project
- Updating an existing dependency version
- Excluding transitive dependencies to resolve conflicts
- Marking a dependency as optional
