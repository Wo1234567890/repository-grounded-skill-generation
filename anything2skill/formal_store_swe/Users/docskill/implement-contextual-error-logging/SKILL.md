---
id: "95ddd09b-9769-50a1-a64e-1a492c1561d0"
name: "Implement Contextual Error Logging"
description: "Implement specific exception types with meaningful error messages and contextual logging to ensure errors are logged with sufficient context for debugging and production issue resolution."
version: "0.1.0"
tags:
  - "error_handling"
  - "logging"
  - "debugging"
  - "exception_management"
triggers:
  - "Writing exception handlers or error paths"
  - "Debugging production issues or test failures"
  - "Implementing error recovery logic"
---

# Implement Contextual Error Logging

Implement specific exception types with meaningful error messages and contextual logging to ensure errors are logged with sufficient context for debugging and production issue resolution.

## Prompt

When implementing error handlers or debugging failures: (1) Use specific exception types instead of generic Exception; (2) Log errors with meaningful messages that include context (function name, state, input values); (3) Ensure error logs are searchable and contain sufficient detail for root cause analysis.

## Objective

Ensure errors are logged with sufficient context for debugging and production issue resolution
## Applicable Signals

- Code path contains try-except blocks
- Error condition detected during execution
- Test failure or production incident investigation initiated

## Contraindications

- Handling third-party library exceptions that already provide comprehensive context
- Scenarios where silent failures are explicitly acceptable by design
- System-level exceptions that should propagate unmodified

## Intervention Moves

- Identify the exception type that best matches the error condition
- Construct error message with function name, current state, and relevant input values
- Log the error with appropriate severity level and context
- Ensure the exception is raised or handled according to the calling contract

## Workflow Steps

- Identify the exception type that best matches the error condition
- Construct error message with function name, current state, and relevant input values
- Log the error with appropriate severity level and context
- Ensure the exception is raised or handled according to the calling contract

## Constraints

- Must use specific exception types (not generic Exception)
- Error messages must include contextual information (function, state, input)
- Logs must be structured for searchability and analysis

## Cautions

- Avoid logging sensitive data (credentials, tokens, PII) in error messages
- Ensure error context does not introduce performance overhead in high-frequency paths

## Output Contract

- All exceptions use specific types (not generic Exception); error logs include context (function, state, input) and are searchable; downstream handlers receive sufficient information for diagnosis and recovery.

## Triggers

- Writing exception handlers or error paths
- Debugging production issues or test failures
- Implementing error recovery logic
