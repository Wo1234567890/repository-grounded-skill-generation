---
id: "55a7d65b-43e0-5944-8364-d72b07b19aab"
name: "Error Handling and Logging Protocol"
description: "Standardize error handling by using specific exception types, logging errors with meaningful messages, and including context in error reports. Apply when implementing error paths or reviewing exception handling."
version: "0.1.0"
tags:
  - "error_handling"
  - "logging"
  - "exception_management"
  - "code_quality"
triggers:
  - "writing exception handlers"
  - "debugging production issues"
  - "implementing new error paths"
---

# Error Handling and Logging Protocol

Standardize error handling by using specific exception types, logging errors with meaningful messages, and including context in error reports. Apply when implementing error paths or reviewing exception handling.

## Prompt

When catching exceptions, use specific exception types rather than generic catches. Log each error with a meaningful message that includes context: the function name, current state, and relevant input values. Ensure error messages are actionable for downstream debugging.

## Objective

implement_robust_error_handling
## Applicable Signals

- exception handler implementation
- error path review
- production issue investigation

## Contraindications

- Do not use for expected control flow; use conditional logic instead
- Do not apply in silent-fail scenarios where logging is explicitly suppressed
- Do not log sensitive data or credentials in error messages

## Intervention Moves

- Replace generic exception catches with specific exception types
- Add context-rich error logging (function name, state, input)
- Ensure error messages are actionable and include debugging hints

## Workflow Steps

- {'step': 1, 'action': 'Identify exception type', 'detail': 'Determine the specific exception class that should be caught (e.g., ValueError, IOError, KeyError)'}
- {'step': 2, 'action': 'Capture context', 'detail': 'Gather function name, current state, and relevant input values at the point of exception'}
- {'step': 3, 'action': 'Log with meaning', 'detail': 'Write error message that includes context and is actionable for debugging'}
- {'step': 4, 'action': 'Re-raise or handle', 'detail': 'Decide whether to re-raise the exception, handle it locally, or convert to a higher-level exception'}

## Constraints

- Exception types must be specific, not generic (e.g., ValueError, KeyError, not Exception)
- Error messages must include sufficient context for debugging
- Logging must not introduce performance bottlenecks in high-frequency code paths

## Cautions

- Avoid over-logging; balance verbosity with signal-to-noise ratio
- Ensure error context does not expose sensitive information

## Output Contract

- All exceptions caught with specific types; error logs include context (function, state, input); messages are actionable for debugging and downstream error handling.

## Triggers

- writing exception handlers
- debugging production issues
- implementing new error paths
