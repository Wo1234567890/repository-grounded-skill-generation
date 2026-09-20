---
id: "9ba1cd5c-fe0c-5a8b-a9fe-04e5e58a18f9"
name: "Migrate Spring Boot Actuator Infrastructure Classes to 3.0"
description: "Canonical skill for identifying and updating renamed actuator infrastructure classes during Spring Boot 2.x to 3.0 migration. Handles class name changes (e.g., HttpTraceRepository → HttpExchangeRepository), package relocations, and import statement updates to resolve compilation errors and ensure code compatibility."
version: "0.1.0"
tags:
  - "spring_boot_3"
  - "actuator"
  - "class_rename"
  - "migration"
  - "infrastructure"
  - "api_deprecation"
triggers:
  - "migrating Spring Boot 2.x to 3.0"
  - "application code directly uses actuator infrastructure classes"
  - "compilation errors reference HttpTraceRepository or similar renamed classes"
examples:
  - input: "Code contains: import org.springframework.boot.actuate.trace.http.HttpTraceRepository;"
    output: "Updated to: import org.springframework.boot.actuate.web.exchanges.HttpExchangeRepository;"
    notes: "Class name and package both changed in Spring Boot 3.0"
---

# Migrate Spring Boot Actuator Infrastructure Classes to 3.0

Canonical skill for identifying and updating renamed actuator infrastructure classes during Spring Boot 2.x to 3.0 migration. Handles class name changes (e.g., HttpTraceRepository → HttpExchangeRepository), package relocations, and import statement updates to resolve compilation errors and ensure code compatibility.

## Prompt

When migrating Spring Boot 2.x code to 3.0, identify actuator infrastructure classes that have been renamed. Locate all references to HttpTraceRepository and similar renamed classes in the codebase. Replace with their new names (e.g., HttpExchangeRepository) and update import statements to use new package locations (e.g., org.springframework.boot.actuate.web.exchanges). Verify all references compile without deprecation warnings.

## Objective

reference_actuator_class_renames
## Applicable Signals

- Migrating Spring Boot 2.x application to 3.0
- Application code directly references actuator infrastructure classes
- Compilation errors mentioning HttpTraceRepository or similar renamed classes
- Need to update package imports for actuator classes

## Contraindications

- Application does not directly reference actuator infrastructure classes
- Using only public actuator endpoints without direct class dependencies
- Already on Spring Boot 3.0 or later

## Intervention Moves

- Locate all references to HttpTraceRepository in codebase
- Replace with HttpExchangeRepository
- Update import statements to org.springframework.boot.actuate.web.exchanges
- Verify compilation and test affected functionality

## Workflow Steps

- Search codebase for imports from org.springframework.boot.actuate.trace.http package
- Identify all usages of HttpTraceRepository and related infrastructure classes
- Replace class names with new equivalents (HttpTraceRepository → HttpExchangeRepository)
- Update import statements to new package location (org.springframework.boot.actuate.web.exchanges)
- Run compilation and verify no deprecation warnings remain
- Execute unit tests for affected actuator functionality

## Constraints

- Changes apply only to actuator module infrastructure classes
- Package location changes must be reflected in all import statements
- Renamed classes maintain functional compatibility with previous versions

## Output Contract

- All references to renamed actuator infrastructure classes updated
- Imports corrected to new package locations (e.g., org.springframework.boot.actuate.web.exchanges)
- Code compiles without deprecation warnings
- Affected actuator functionality verified through testing

## Example Therapist Responses

### Example 1

- Client/Input: Code contains: import org.springframework.boot.actuate.trace.http.HttpTraceRepository;
- Therapist/Output: Updated to: import org.springframework.boot.actuate.web.exchanges.HttpExchangeRepository;
- Notes: Class name and package both changed in Spring Boot 3.0

## Triggers

- migrating Spring Boot 2.x to 3.0
- application code directly uses actuator infrastructure classes
- compilation errors reference HttpTraceRepository or similar renamed classes

## Examples

### Example 1

Input:

  Code contains: import org.springframework.boot.actuate.trace.http.HttpTraceRepository;

Output:

  Updated to: import org.springframework.boot.actuate.web.exchanges.HttpExchangeRepository;

Notes:

  Class name and package both changed in Spring Boot 3.0
