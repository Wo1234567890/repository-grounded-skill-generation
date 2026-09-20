---
id: "a26898f3-52b3-5b50-b6c8-6fca8104230d"
name: "Gradle Main Class Resolution and BootJar Configuration"
description: "Update Gradle build configuration to explicitly set main class name and configure BootJar layering using the springBoot DSL and task-specific properties for Spring Boot 3.0 compatibility."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "gradle"
  - "build-configuration"
  - "dsl-migration"
  - "bootjar"
  - "main-class-resolution"
triggers:
  - "Migrating Spring Boot 2.x to 3.0 with Gradle build system"
  - "Main class resolution was previously implicit or relied on non-standard source set locations"
  - "BootJar layering needs explicit configuration"
  - "Build tasks (bootJar, bootRun, bootWar) show inconsistent main class resolution"
examples:
  - input: "Gradle build.gradle.kts with implicit main class resolution and legacy BootJar syntax"
    output: "springBoot { mainClass = \"com.example.Application\" } added; tasks.named<BootJar>(\"bootJar\") { layered { enabled.set(false) } } configured"
    notes: "Explicit mainClass property ensures consistent resolution; enabled.set() replaces isEnabled for Spring Boot 3.0 compatibility"
  - input: "Build configuration relying on non-standard source set location for main class"
    output: "tasks.named(\"resolveMainClassName\") { classpath.setFrom(...) } configured to search custom locations; springBoot { mainClass = \"...\" } set as fallback"
    notes: "Custom classpath resolution allows flexibility while maintaining explicit configuration"
---

# Gradle Main Class Resolution and BootJar Configuration

Update Gradle build configuration to explicitly set main class name and configure BootJar layering using the springBoot DSL and task-specific properties for Spring Boot 3.0 compatibility.

## Prompt

When migrating to Spring Boot 3.0 with Gradle, main class resolution has been simplified and made consistent across bootJar, bootRun, and bootWar tasks. If your build previously relied on implicit resolution or non-standard source set locations, you must now explicitly configure the main class name using the `mainClass` property in the `springBoot` DSL block. Additionally, BootJar task configuration syntax has changed: replace `isEnabled = false` with `enabled.set(false)` for layering control. Review your current Gradle configuration and apply these updates to ensure consistent builds.

## Objective

Ensure consistent main class resolution and correct BootJar task configuration in Gradle builds for Spring Boot 3.0
## Applicable Signals

- Gradle build configuration file (build.gradle or build.gradle.kts) exists
- springBoot DSL block is present or needs to be added
- BootJar task configuration uses legacy isEnabled property syntax
- Main class name is not explicitly set in springBoot block

## Contraindications

- Using Maven build system instead of Gradle
- Main class is already explicitly configured in springBoot DSL with mainClass property
- BootJar task configuration already uses enabled.set() syntax
- No custom classpath resolution or non-standard source set locations are in use

## Intervention Moves

- Add or update mainClass property in springBoot DSL block
- Replace isEnabled = false with enabled.set(false) in BootJar task configuration
- Configure resolveMainClassName task classpath for non-standard source set locations if needed

## Workflow Steps

- {'step': 1, 'action': 'Review current Gradle build configuration', 'detail': 'Open build.gradle or build.gradle.kts and locate the springBoot DSL block and any BootJar task configuration'}
- {'step': 2, 'action': 'Add or update mainClass property in springBoot DSL', 'detail': 'If not present, add springBoot { mainClass = "com.example.Application" } with the correct fully-qualified class name'}
- {'step': 3, 'action': 'Update BootJar task layering syntax', 'detail': 'Replace isEnabled = false with enabled.set(false) in tasks.named<BootJar>("bootJar") { layered { ... } } block'}
- {'step': 4, 'action': 'If using custom classpath resolution, update resolveMainClassName task', 'detail': 'Configure the classpath property of resolveMainClassName task to search in non-standard locations if needed'}
- {'step': 5, 'action': 'Test build and execution', 'detail': 'Run ./gradlew bootJar, ./gradlew bootRun, and ./gradlew bootWar to verify consistent main class resolution and correct JAR structure'}

## Constraints

- Changes apply only to Gradle-based Spring Boot projects
- springBoot DSL must be available (requires Spring Boot Gradle plugin)
- Task-specific configuration must use Kotlin DSL syntax (tasks.named<BootJar>(...)) or Groovy equivalent
- Main class name must be a valid fully-qualified class name

## Cautions

- Ensure the specified main class exists in the main source set output
- If using custom classpath resolution, update resolveMainClassName task classpath property accordingly
- Test all three tasks (bootJar, bootRun, bootWar) to verify consistent main class resolution
- Layering configuration changes affect JAR structure; verify application startup behavior after changes

## Output Contract

- Gradle build successfully resolves main class consistently across bootJar, bootRun, and bootWar tasks
- BootJar task configuration uses enabled.set() syntax
- Build completes without main class resolution warnings or errors
- Generated JAR has correct layering configuration

## Example Executions

### Example 1

- Input: Gradle build.gradle.kts with implicit main class resolution and legacy BootJar syntax
- Output: springBoot { mainClass = "com.example.Application" } added; tasks.named<BootJar>("bootJar") { layered { enabled.set(false) } } configured
- Notes: Explicit mainClass property ensures consistent resolution; enabled.set() replaces isEnabled for Spring Boot 3.0 compatibility

### Example 2

- Input: Build configuration relying on non-standard source set location for main class
- Output: tasks.named("resolveMainClassName") { classpath.setFrom(...) } configured to search custom locations; springBoot { mainClass = "..." } set as fallback
- Notes: Custom classpath resolution allows flexibility while maintaining explicit configuration

## Triggers

- Migrating Spring Boot 2.x to 3.0 with Gradle build system
- Main class resolution was previously implicit or relied on non-standard source set locations
- BootJar layering needs explicit configuration
- Build tasks (bootJar, bootRun, bootWar) show inconsistent main class resolution

## Examples

### Example 1

Input:

  Gradle build.gradle.kts with implicit main class resolution and legacy BootJar syntax

Output:

  springBoot { mainClass = "com.example.Application" } added; tasks.named<BootJar>("bootJar") { layered { enabled.set(false) } } configured

Notes:

  Explicit mainClass property ensures consistent resolution; enabled.set() replaces isEnabled for Spring Boot 3.0 compatibility

### Example 2

Input:

  Build configuration relying on non-standard source set location for main class

Output:

  tasks.named("resolveMainClassName") { classpath.setFrom(...) } configured to search custom locations; springBoot { mainClass = "..." } set as fallback

Notes:

  Custom classpath resolution allows flexibility while maintaining explicit configuration
