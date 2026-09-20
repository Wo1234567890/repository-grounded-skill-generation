---
id: "d83d810d-3d1a-5dc4-8322-6ade71d4e374"
name: "Update Actuator Infrastructure Class References"
description: "Rename and relocate actuator infrastructure classes during Spring Boot 2.x to 3.0 migration. Specifically updates HttpTraceRepository to HttpExchangeRepository and relocates it to the org.springframework.boot.actuate.web.exchanges package. Apply when code directly imports or instantiates renamed actuator infrastructure classes."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "actuator"
  - "class-refactoring"
  - "import-update"
triggers:
  - "Code directly imports or instantiates HttpTraceRepository or other renamed actuator infrastructure classes; migrating from Spring Boot 2.x to 3.0"
examples:
  - input: "import org.springframework.boot.actuate.trace.http.HttpTraceRepository;"
    output: "import org.springframework.boot.actuate.web.exchanges.HttpExchangeRepository;"
    notes: "Direct import statement update for renamed class"
  - input: "HttpTraceRepository repository = new HttpTraceRepository();"
    output: "HttpExchangeRepository repository = new HttpExchangeRepository();"
    notes: "Class instantiation reference update"
---

# Update Actuator Infrastructure Class References

Rename and relocate actuator infrastructure classes during Spring Boot 2.x to 3.0 migration. Specifically updates HttpTraceRepository to HttpExchangeRepository and relocates it to the org.springframework.boot.actuate.web.exchanges package. Apply when code directly imports or instantiates renamed actuator infrastructure classes.

## Prompt

Identify all code references to deprecated actuator infrastructure class names (e.g., HttpTraceRepository). Replace with new class names (e.g., HttpExchangeRepository) and update import statements to point to org.springframework.boot.actuate.web.exchanges package. Verify all usages are updated before testing.

## Objective

Update actuator class imports and references to align with Spring Boot 3.0 class naming and package structure
## Applicable Signals

- Code contains import statements for HttpTraceRepository or similar actuator infrastructure classes
- Migration from Spring Boot 2.x to 3.0 is in progress
- Compilation errors reference old actuator class names

## Contraindications

- Codebase uses only high-level actuator endpoints without direct infrastructure class dependencies
- No direct instantiation or import of actuator infrastructure classes present

## Intervention Moves

- Search codebase for references to HttpTraceRepository
- Replace class name with HttpExchangeRepository
- Update import statement to org.springframework.boot.actuate.web.exchanges
- Verify no remaining references to old class name
- Run compilation check to confirm resolution

## Workflow Steps

- {'step': 1, 'action': 'Identify all imports and usages of HttpTraceRepository in codebase'}
- {'step': 2, 'action': 'Replace HttpTraceRepository with HttpExchangeRepository in all locations'}
- {'step': 3, 'action': 'Update import statement from old package to org.springframework.boot.actuate.web.exchanges'}
- {'step': 4, 'action': 'Compile and verify no class resolution errors'}

## Constraints

- Must update all occurrences of old class name in single pass to avoid partial migration
- Package path must be exactly org.springframework.boot.actuate.web.exchanges

## Cautions

- Ensure IDE refactoring tools are used to catch all references, including indirect usages
- Test actuator functionality after class reference updates to confirm behavior is preserved

## Output Contract

- All references to old actuator infrastructure class names (e.g., HttpTraceRepository) are replaced with new names (e.g., HttpExchangeRepository); all import statements updated to org.springframework.boot.actuate.web.exchanges package; codebase compiles without class-not-found errors related to actuator infrastructure classes.

## Example Executions

### Example 1

- Input: import org.springframework.boot.actuate.trace.http.HttpTraceRepository;
- Output: import org.springframework.boot.actuate.web.exchanges.HttpExchangeRepository;
- Notes: Direct import statement update for renamed class

### Example 2

- Input: HttpTraceRepository repository = new HttpTraceRepository();
- Output: HttpExchangeRepository repository = new HttpExchangeRepository();
- Notes: Class instantiation reference update

## Triggers

- Code directly imports or instantiates HttpTraceRepository or other renamed actuator infrastructure classes; migrating from Spring Boot 2.x to 3.0

## Examples

### Example 1

Input:

  import org.springframework.boot.actuate.trace.http.HttpTraceRepository;

Output:

  import org.springframework.boot.actuate.web.exchanges.HttpExchangeRepository;

Notes:

  Direct import statement update for renamed class

### Example 2

Input:

  HttpTraceRepository repository = new HttpTraceRepository();

Output:

  HttpExchangeRepository repository = new HttpExchangeRepository();

Notes:

  Class instantiation reference update
