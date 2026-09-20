---
id: "e1c33881-5c6b-5405-8b21-a771ac02a898"
name: "Instrumentation Error Handling and Graceful Degradation"
description: "Safety rule that wraps instrumentation operations in try-except blocks to prevent instrumentation failures from breaking the underlying API call. Ensures errors are logged but not propagated to the caller, preserving original API behavior."
version: "0.1.0"
tags:
  - "error_handling"
  - "instrumentation"
  - "graceful_degradation"
  - "api_safety"
  - "observability"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Wrapping any external API call"
  - "Instrumentation code may raise exceptions"
  - "Need to preserve original API behavior"
examples:
  - input: "Instrumenting OpenAI API call; instrumentation code raises AttributeError"
    output: "OpenAI API call returns response normally; AttributeError logged with context; caller receives API response unchanged"
    notes: "Instrumentation failure is isolated and does not affect API functionality"
  - input: "Wrapping async method instrumentation; timeout occurs during metric collection"
    output: "Async method completes; timeout exception caught and logged; caller receives method result"
    notes: "Graceful degradation allows async operations to proceed despite instrumentation issues"
---

# Instrumentation Error Handling and Graceful Degradation

Safety rule that wraps instrumentation operations in try-except blocks to prevent instrumentation failures from breaking the underlying API call. Ensures errors are logged but not propagated to the caller, preserving original API behavior.

## Prompt

When instrumenting external API calls, wrap instrumentation code in try-except blocks. Catch exceptions raised during instrumentation, log them for debugging, and allow the original API call to complete successfully. Do not re-raise instrumentation errors to the caller.

## Objective

Ensure instrumentation never causes application failure or data loss
## Applicable Signals

- Wrapping any external API call
- Instrumentation code may raise exceptions
- Need to preserve original API behavior

## Contraindications

- Do not use when instrumentation errors should halt execution
- Do not use when original API call should not proceed if instrumentation fails
- Do not use when error suppression violates compliance or audit requirements

## Intervention Moves

- Wrap instrumentation operation in try-except block
- Log exception details (type, message, traceback) for debugging
- Allow original API call to complete and return normally
- Do not re-raise instrumentation exception to caller

## Workflow Steps

- Identify instrumentation operation to be wrapped
- Enclose instrumentation code in try-except block
- Capture exception details in except clause
- Log exception with full context (type, message, traceback)
- Allow original API call to proceed and return result
- Return original API result to caller unchanged

## Constraints

- Instrumentation errors must be caught and logged, never silently ignored
- Original API call must complete and return its result unchanged
- Logging must include sufficient context for post-incident debugging

## Cautions

- Ensure logging does not itself raise exceptions or cause performance degradation
- Monitor instrumentation error logs to detect systematic failures
- Consider circuit-breaker patterns if instrumentation errors become frequent

## Output Contract

- API call completes successfully with original result; instrumentation error is logged but not propagated to caller; application continues normal execution

## Example Executions

### Example 1

- Input: Instrumenting OpenAI API call; instrumentation code raises AttributeError
- Output: OpenAI API call returns response normally; AttributeError logged with context; caller receives API response unchanged
- Notes: Instrumentation failure is isolated and does not affect API functionality

### Example 2

- Input: Wrapping async method instrumentation; timeout occurs during metric collection
- Output: Async method completes; timeout exception caught and logged; caller receives method result
- Notes: Graceful degradation allows async operations to proceed despite instrumentation issues

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Wrapping any external API call
- Instrumentation code may raise exceptions
- Need to preserve original API behavior

## Examples

### Example 1

Input:

  Instrumenting OpenAI API call; instrumentation code raises AttributeError

Output:

  OpenAI API call returns response normally; AttributeError logged with context; caller receives API response unchanged

Notes:

  Instrumentation failure is isolated and does not affect API functionality

### Example 2

Input:

  Wrapping async method instrumentation; timeout occurs during metric collection

Output:

  Async method completes; timeout exception caught and logged; caller receives method result

Notes:

  Graceful degradation allows async operations to proceed despite instrumentation issues
