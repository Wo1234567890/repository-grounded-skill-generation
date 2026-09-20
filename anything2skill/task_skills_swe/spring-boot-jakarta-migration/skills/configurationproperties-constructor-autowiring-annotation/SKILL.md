---
id: "5ad715e1-3e6e-5d91-a72b-ee51041a0f17"
name: "ConfigurationProperties Constructor Autowiring Annotation"
description: "Add explicit `@Autowired` annotation to constructor parameters in `@ConfigurationProperties` classes that rely on dependency injection. This prevents constructor parameters from being misidentified as property binding targets during Spring Boot 3.0 migration."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "configuration-properties"
  - "dependency-injection"
  - "annotation"
  - "constructor-injection"
triggers:
  - "Spring Boot 3.0 upgrade in progress"
  - "@ConfigurationProperties class uses constructor-based dependency injection"
  - "Constructor parameters lack explicit @Autowired annotation"
examples:
  - input: "@ConfigurationProperties(prefix=\"app\")\npublic class AppConfig {\n  private String name;\n  private SomeService service;\n  \n  public AppConfig(SomeService service) {\n    this.service = service;\n  }\n}"
    output: "@ConfigurationProperties(prefix=\"app\")\npublic class AppConfig {\n  private String name;\n  private SomeService service;\n  \n  public AppConfig(@Autowired SomeService service) {\n    this.service = service;\n  }\n}"
    notes: "Constructor parameter service is now explicitly marked for autowiring, preventing misidentification as a property binding target"
---

# ConfigurationProperties Constructor Autowiring Annotation

Add explicit `@Autowired` annotation to constructor parameters in `@ConfigurationProperties` classes that rely on dependency injection. This prevents constructor parameters from being misidentified as property binding targets during Spring Boot 3.0 migration.

## Prompt

Locate all `@ConfigurationProperties` classes that use constructor-based dependency injection. For each constructor parameter that requires autowiring, add the `@Autowired` annotation explicitly. This ensures the Spring container treats the parameter as a dependency to inject rather than as a property binding target.

## Objective

Disambiguate constructor dependency injection from property binding in configuration classes
## Applicable Signals

- Compilation or runtime error: constructor parameter treated as property binding target
- Configuration property binding failure in @ConfigurationProperties class
- Spring context initialization warning about ambiguous constructor parameter resolution

## Contraindications

- Configuration class does not use constructor injection
- All dependencies are field-injected or setter-injected
- @Autowired annotation already present on all constructor parameters
- Class is not annotated with @ConfigurationProperties

## Workflow Steps

- {'step': 1, 'action': 'Identify all @ConfigurationProperties classes in the codebase'}
- {'step': 2, 'action': 'For each class, check if it has a constructor with parameters'}
- {'step': 3, 'action': 'Determine which constructor parameters are dependencies (not configuration properties)'}
- {'step': 4, 'action': 'Add @Autowired annotation to each dependency parameter'}
- {'step': 5, 'action': 'Compile and test application startup to verify no binding errors occur'}

## Constraints

- Only apply to @ConfigurationProperties classes
- Only annotate constructor parameters that represent dependencies, not configuration properties
- Ensure the dependency type is resolvable in the Spring context

## Cautions

- Do not confuse constructor parameters for dependency injection with constructor parameters for property binding
- Verify that adding @Autowired does not create circular dependencies
- Test application startup after annotation changes to confirm context initialization succeeds

## Output Contract

- All constructor parameters in @ConfigurationProperties classes that require dependency injection are annotated with @Autowired; application context initializes without binding errors; configuration properties are correctly populated from external sources

## Example Executions

### Example 1

- Input: @ConfigurationProperties(prefix="app")
public class AppConfig {
  private String name;
  private SomeService service;
  
  public AppConfig(SomeService service) {
    this.service = service;
  }
}
- Output: @ConfigurationProperties(prefix="app")
public class AppConfig {
  private String name;
  private SomeService service;
  
  public AppConfig(@Autowired SomeService service) {
    this.service = service;
  }
}
- Notes: Constructor parameter service is now explicitly marked for autowiring, preventing misidentification as a property binding target

## Triggers

- Spring Boot 3.0 upgrade in progress
- @ConfigurationProperties class uses constructor-based dependency injection
- Constructor parameters lack explicit @Autowired annotation

## Examples

### Example 1

Input:

  @ConfigurationProperties(prefix="app")
  public class AppConfig {
    private String name;
    private SomeService service;
    
    public AppConfig(SomeService service) {
      this.service = service;
    }
  }

Output:

  @ConfigurationProperties(prefix="app")
  public class AppConfig {
    private String name;
    private SomeService service;
    
    public AppConfig(@Autowired SomeService service) {
      this.service = service;
    }
  }

Notes:

  Constructor parameter service is now explicitly marked for autowiring, preventing misidentification as a property binding target
