---
id: "109f7fdc-2a70-5dc6-9793-d4076b4988b8"
name: "Configure Gradle Main Class Resolution for Spring Boot 3.0"
description: "Explicitly configure the main class name in Gradle build when default resolution from main source set output is insufficient during Spring Boot 3.0 migration. Applies to bootJar, bootRun, and bootWar tasks."
version: "0.1.0"
tags:
  - "gradle"
  - "spring-boot-3"
  - "build-configuration"
  - "dsl"
  - "main-class"
triggers:
  - "Migrating to Spring Boot 3.0 with Gradle"
  - "Main class resolution from default source set output is incorrect"
  - "Custom main class location required outside standard source set output"
examples:
  - input: "Spring Boot 3.0 Gradle project with main class in non-standard location; bootJar task fails to resolve main class"
    output: "Add springBoot { mainClass = \"com.example.MyApplication\" } to build.gradle.kts; bootJar task now correctly identifies and packages the application with correct entry point"
    notes: "Standard approach for most cases; simplest configuration method"
  - input: "Gradle project requiring custom classpath search for main class resolution"
    output: "Configure tasks.named<BootJar>(\"bootJar\") { ... } with custom classpath property pointing to alternative output directories; resolveMainClassName task searches specified locations"
    notes: "Advanced approach for complex build layouts"
---

# Configure Gradle Main Class Resolution for Spring Boot 3.0

Explicitly configure the main class name in Gradle build when default resolution from main source set output is insufficient during Spring Boot 3.0 migration. Applies to bootJar, bootRun, and bootWar tasks.

## Prompt

When migrating to Spring Boot 3.0 with Gradle, if the default main class resolution from the main source set output is incorrect or insufficient, explicitly configure the main class name using the `mainClass` property in the `springBoot` DSL block. Alternatively, configure the `classpath` property of the `resolveMainClassName` task to search in custom locations.

## Objective

configure_gradle_main_class_resolution
## Applicable Signals

- Migrating to Spring Boot 3.0 with Gradle build system
- Main class resolution from default source set output is incorrect
- Custom main class location required outside standard source set output
- bootJar, bootRun, or bootWar tasks not resolving correct main class

## Contraindications

- Main class is located in standard main source set output (use default resolution)
- Maven build system is used (not applicable to Gradle)
- Spring Boot 2.x or earlier (no DSL syntax change required)

## Intervention Moves

- Add springBoot DSL block with mainClass property to build.gradle.kts
- Configure resolveMainClassName task classpath property for custom locations
- Verify bootJar, bootRun, and bootWar tasks resolve correct main class

## Workflow Steps

- {'step': 1, 'action': 'Identify if main class resolution is failing or incorrect', 'condition': 'bootJar, bootRun, or bootWar tasks do not resolve the correct main class'}
- {'step': 2, 'action': 'Add springBoot DSL block with mainClass property', 'detail': 'springBoot { mainClass = "com.example.Application" }'}
- {'step': 3, 'action': 'Alternatively, configure resolveMainClassName task classpath property', 'detail': 'tasks.named<BootJar>("bootJar") { ... } with custom classpath configuration'}
- {'step': 4, 'action': 'Verify bootJar, bootRun, and bootWar tasks resolve the correct main class', 'condition': 'Build succeeds and application starts with correct entry point'}

## Constraints

- Must use `mainClass` property within `springBoot` DSL block in build.gradle.kts or build.gradle
- If using `resolveMainClassName` task customization, ensure `classpath` property is correctly configured
- Configuration must be applied before bootJar, bootRun, or bootWar task execution

## Cautions

- In Spring Boot 3.0, DSL syntax changed: use `enabled.set(false)` instead of `isEnabled = false` for layered configuration
- Ensure main class fully qualified name is correct (e.g., com.example.Application)
- Custom classpath configuration for resolveMainClassName must point to valid output directories

## Output Contract

- mainClass property is set in springBoot DSL block
- bootJar, bootRun, and bootWar tasks resolve and use the correct main class
- Build completes successfully with correct application entry point

## Example Therapist Responses

### Example 1

- Client/Input: Spring Boot 3.0 Gradle project with main class in non-standard location; bootJar task fails to resolve main class
- Therapist/Output: Add springBoot { mainClass = "com.example.MyApplication" } to build.gradle.kts; bootJar task now correctly identifies and packages the application with correct entry point
- Notes: Standard approach for most cases; simplest configuration method

### Example 2

- Client/Input: Gradle project requiring custom classpath search for main class resolution
- Therapist/Output: Configure tasks.named<BootJar>("bootJar") { ... } with custom classpath property pointing to alternative output directories; resolveMainClassName task searches specified locations
- Notes: Advanced approach for complex build layouts

## Triggers

- Migrating to Spring Boot 3.0 with Gradle
- Main class resolution from default source set output is incorrect
- Custom main class location required outside standard source set output

## Examples

### Example 1

Input:

  Spring Boot 3.0 Gradle project with main class in non-standard location; bootJar task fails to resolve main class

Output:

  Add springBoot { mainClass = "com.example.MyApplication" } to build.gradle.kts; bootJar task now correctly identifies and packages the application with correct entry point

Notes:

  Standard approach for most cases; simplest configuration method

### Example 2

Input:

  Gradle project requiring custom classpath search for main class resolution

Output:

  Configure tasks.named<BootJar>("bootJar") { ... } with custom classpath property pointing to alternative output directories; resolveMainClassName task searches specified locations

Notes:

  Advanced approach for complex build layouts
