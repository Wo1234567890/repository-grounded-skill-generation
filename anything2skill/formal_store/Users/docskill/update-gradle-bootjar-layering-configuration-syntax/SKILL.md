---
id: "5d6c51f6-1bfa-5275-8a8e-ab77fe20c06b"
name: "Update Gradle BootJar Layering Configuration Syntax"
description: "Migrate BootJar task layering configuration from deprecated isEnabled boolean property to enabled.set() method call when upgrading to Spring Boot 3.0 with Gradle."
version: "0.1.0"
tags:
  - "gradle"
  - "spring-boot-3.0"
  - "build-configuration"
  - "dsl-migration"
  - "bootjar"
triggers:
  - "migrating to Spring Boot 3.0 with Gradle"
  - "BootJar task uses isEnabled property for layering configuration"
examples:
  - input: "tasks.named<BootJar>(\"bootJar\") {\n  layered {\n    isEnabled = false\n  }\n}"
    output: "tasks.named<BootJar>(\"bootJar\") {\n  layered {\n    enabled.set(false)\n  }\n}"
    notes: "Direct property-to-method migration for disabling layering"
  - input: "tasks.named<BootJar>(\"bootJar\") {\n  layered {\n    isEnabled = true\n  }\n}"
    output: "tasks.named<BootJar>(\"bootJar\") {\n  layered {\n    enabled.set(true)\n  }\n}"
    notes: "Migration when layering is explicitly enabled"
---

# Update Gradle BootJar Layering Configuration Syntax

Migrate BootJar task layering configuration from deprecated isEnabled boolean property to enabled.set() method call when upgrading to Spring Boot 3.0 with Gradle.

## Prompt

In Spring Boot 3.0, the BootJar Gradle task layering configuration syntax has changed. Replace the isEnabled property with the enabled.set() method. Locate the BootJar task configuration block in build.gradle.kts and update the layered section accordingly.

## Objective

update_gradle_bootjar_layering_syntax
## Applicable Signals

- migrating project to Spring Boot 3.0
- BootJar task configured with layering
- isEnabled property present in layered block
- Gradle build system in use

## Contraindications

- layering is not configured in BootJar task
- Maven build system used instead of Gradle
- Spring Boot version is 2.7.x or earlier
- no BootJar task customization present

## Intervention Moves

- Locate tasks.named<BootJar> block in build.gradle.kts
- Find layered { isEnabled = false } or layered { isEnabled = true }
- Replace with layered { enabled.set(false) } or layered { enabled.set(true) }
- Verify Gradle build completes without deprecation warnings

## Workflow Steps

- {'step': 1, 'action': 'Open build.gradle.kts file', 'detail': 'Locate the Gradle build configuration file'}
- {'step': 2, 'action': 'Find BootJar task configuration', 'detail': 'Search for tasks.named<BootJar> block'}
- {'step': 3, 'action': 'Identify layering configuration', 'detail': 'Locate layered { ... } block within BootJar task'}
- {'step': 4, 'action': 'Replace isEnabled property', 'detail': 'Change isEnabled = <boolean> to enabled.set(<boolean>)'}
- {'step': 5, 'action': 'Validate syntax', 'detail': 'Run gradle build or gradle bootJar to verify no errors'}

## Constraints

- Only applies to Gradle-based Spring Boot projects
- Only applies to Spring Boot 3.0 and later
- Requires BootJar task to be explicitly configured with layering

## Cautions

- Ensure the boolean value (true/false) is preserved during migration
- Test the build after applying the change to confirm layering behavior is unchanged

## Output Contract

- BootJar layering configuration syntax updated from isEnabled property to enabled.set() method
- Gradle build executes successfully without deprecation warnings
- layering behavior remains functionally equivalent

## Example Therapist Responses

### Example 1

- Client/Input: tasks.named<BootJar>("bootJar") {
  layered {
    isEnabled = false
  }
}
- Therapist/Output: tasks.named<BootJar>("bootJar") {
  layered {
    enabled.set(false)
  }
}
- Notes: Direct property-to-method migration for disabling layering

### Example 2

- Client/Input: tasks.named<BootJar>("bootJar") {
  layered {
    isEnabled = true
  }
}
- Therapist/Output: tasks.named<BootJar>("bootJar") {
  layered {
    enabled.set(true)
  }
}
- Notes: Migration when layering is explicitly enabled

## Triggers

- migrating to Spring Boot 3.0 with Gradle
- BootJar task uses isEnabled property for layering configuration

## Examples

### Example 1

Input:

  tasks.named<BootJar>("bootJar") {
    layered {
      isEnabled = false
    }
  }

Output:

  tasks.named<BootJar>("bootJar") {
    layered {
      enabled.set(false)
    }
  }

Notes:

  Direct property-to-method migration for disabling layering

### Example 2

Input:

  tasks.named<BootJar>("bootJar") {
    layered {
      isEnabled = true
    }
  }

Output:

  tasks.named<BootJar>("bootJar") {
    layered {
      enabled.set(true)
    }
  }

Notes:

  Migration when layering is explicitly enabled
