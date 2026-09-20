---
id: "d036d5ff-bc2c-5958-98fa-a3c8f419300b"
name: "Deprecation Review and Removal for Spring Boot 2.x APIs"
description: "Scans codebase for deprecated Spring Boot 2.x APIs and replaces them with 3.0 equivalents, including removed classes, annotations, and utility methods. Executes as a pre-upgrade or post-upgrade remediation workflow to eliminate compilation errors and deprecation warnings."
version: "0.1.0"
tags:
  - "spring-boot"
  - "migration"
  - "deprecation"
  - "code-modernization"
  - "api-replacement"
triggers:
  - "Preparing for Spring Boot 3.0 upgrade"
  - "Post-upgrade compilation errors indicate removed APIs"
  - "Deprecation warnings present in build output"
examples:
  - input: "Codebase contains @ConstructorBinding annotation at class level in configuration properties class"
    output: "Remove @ConstructorBinding from class declaration; Spring Boot 3.0 infers constructor binding automatically"
    notes: "Common pattern in Spring Boot 2.x configuration classes"
  - input: "Code uses YamlJsonParser utility for YAML parsing"
    output: "Replace with SnakeYAML or Spring's YamlProcessor; YamlJsonParser has been removed"
    notes: "Direct removal with no direct equivalent; use standard YAML parsing library"
  - input: "@EnableBatchProcessing annotation present on configuration class"
    output: "Remove @EnableBatchProcessing; Spring Boot 3.0 auto-configures batch processing when spring-batch is on classpath"
    notes: "Annotation is now discouraged; auto-configuration handles setup"
---

# Deprecation Review and Removal for Spring Boot 2.x APIs

Scans codebase for deprecated Spring Boot 2.x APIs and replaces them with 3.0 equivalents, including removed classes, annotations, and utility methods. Executes as a pre-upgrade or post-upgrade remediation workflow to eliminate compilation errors and deprecation warnings.

## Prompt

Identify all Spring Boot 2.x deprecated APIs in the codebase. For each deprecated item (class, annotation, method, utility), locate usages and replace with the Spring Boot 3.0 equivalent. Verify compilation succeeds and no deprecation warnings remain. Common removals include @ConstructorBinding at type level, YamlJsonParser, @EnableBatchProcessing, and other framework-level APIs listed in the Spring Boot 3.0 migration guide.

## Objective

Eliminate all deprecated Spring Boot 2.x API usage before or after upgrading to 3.0
## Applicable Signals

- Spring Boot 2.7.x codebase identified
- Upgrade to Spring Boot 3.0 planned or in progress
- Compiler warnings for deprecated Spring Boot APIs

## Contraindications

- Already on Spring Boot 3.0 with clean codebase
- Using third-party libraries that have not yet migrated to Spring Boot 3.0
- Codebase does not use Spring Boot framework

## Workflow Steps

- {'step': 1, 'action': 'Scan codebase for deprecated Spring Boot 2.x APIs', 'detail': 'Use IDE inspection tools or grep-based search for known deprecated classes, annotations, and methods (e.g., @ConstructorBinding at type level, YamlJsonParser, @EnableBatchProcessing)'}
- {'step': 2, 'action': 'Catalog all deprecated usages', 'detail': 'Create inventory of deprecated items with file locations and context'}
- {'step': 3, 'action': 'Replace each deprecated API with Spring Boot 3.0 equivalent', 'detail': 'Consult Spring Boot 3.0 migration guide for each removal; apply replacement pattern'}
- {'step': 4, 'action': 'Compile and verify no deprecation warnings', 'detail': 'Run full build; confirm zero deprecation warnings and successful compilation'}
- {'step': 5, 'action': 'Execute test suite', 'detail': 'Run unit and integration tests to verify behavioral equivalence after replacements'}

## Constraints

- Must complete before final Spring Boot 3.0 upgrade
- Requires access to full source codebase
- Compilation must succeed after all replacements

## Cautions

- Some deprecated APIs may have multiple replacement paths; verify correct equivalent for your use case
- Third-party dependencies may still reference removed APIs; consider dependency updates first
- Test thoroughly after replacements to ensure behavioral equivalence

## Output Contract

- All deprecated Spring Boot 2.x API calls replaced with 3.0 equivalents; codebase compiles without errors or deprecation warnings; test suite passes.

## Example Executions

### Example 1

- Input: Codebase contains @ConstructorBinding annotation at class level in configuration properties class
- Output: Remove @ConstructorBinding from class declaration; Spring Boot 3.0 infers constructor binding automatically
- Notes: Common pattern in Spring Boot 2.x configuration classes

### Example 2

- Input: Code uses YamlJsonParser utility for YAML parsing
- Output: Replace with SnakeYAML or Spring's YamlProcessor; YamlJsonParser has been removed
- Notes: Direct removal with no direct equivalent; use standard YAML parsing library

### Example 3

- Input: @EnableBatchProcessing annotation present on configuration class
- Output: Remove @EnableBatchProcessing; Spring Boot 3.0 auto-configures batch processing when spring-batch is on classpath
- Notes: Annotation is now discouraged; auto-configuration handles setup

## Triggers

- Preparing for Spring Boot 3.0 upgrade
- Post-upgrade compilation errors indicate removed APIs
- Deprecation warnings present in build output

## Examples

### Example 1

Input:

  Codebase contains @ConstructorBinding annotation at class level in configuration properties class

Output:

  Remove @ConstructorBinding from class declaration; Spring Boot 3.0 infers constructor binding automatically

Notes:

  Common pattern in Spring Boot 2.x configuration classes

### Example 2

Input:

  Code uses YamlJsonParser utility for YAML parsing

Output:

  Replace with SnakeYAML or Spring's YamlProcessor; YamlJsonParser has been removed

Notes:

  Direct removal with no direct equivalent; use standard YAML parsing library

### Example 3

Input:

  @EnableBatchProcessing annotation present on configuration class

Output:

  Remove @EnableBatchProcessing; Spring Boot 3.0 auto-configures batch processing when spring-batch is on classpath

Notes:

  Annotation is now discouraged; auto-configuration handles setup
