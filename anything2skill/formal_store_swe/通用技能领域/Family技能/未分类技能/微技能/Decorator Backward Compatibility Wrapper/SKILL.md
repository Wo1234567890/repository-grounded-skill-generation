---
id: "7087fb2f-2eeb-5e8c-b7a2-03f1f776f596"
name: "Decorator Backward Compatibility Wrapper"
description: "Provide a deprecated @session decorator that delegates to @trace for backward compatibility, handling both direct decoration and parameterized invocation patterns."
version: "0.1.0"
tags:
  - "decorator"
  - "backward_compatibility"
  - "deprecation"
  - "api_migration"
  - "wrapper"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Existing code uses @session decorator and must continue to work; migration to @trace is in progress."
examples:
  - input: "@session\ndef my_function(): pass"
    output: "my_function is decorated; @trace is invoked with my_function as first argument; deprecation warning emitted"
    notes: "Bare decorator invocation"
  - input: "@session(name='custom_name')\ndef my_function(): pass"
    output: "my_function is decorated; @trace is invoked with name='custom_name'; deprecation warning emitted"
    notes: "Parameterized decorator invocation"
---

# Decorator Backward Compatibility Wrapper

Provide a deprecated @session decorator that delegates to @trace for backward compatibility, handling both direct decoration and parameterized invocation patterns.

## Prompt

Implement a @session decorator that wraps @trace to maintain legacy API compatibility. The decorator must handle two invocation styles: bare decoration (@session on a function) and parameterized decoration (@session(name=...)). Route all calls to @trace with the same arguments and emit a deprecation warning. Use the deprecated() helper to mark @session as obsolete.

## Objective

Maintain legacy @session decorator API while routing to new @trace implementation
## Applicable Signals

- Existing codebase uses @session decorator
- Migration to @trace is in progress
- Legacy code must continue to work without modification

## Contraindications

- Full removal of @session is acceptable
- No legacy code depends on @session decorator
- New code should use @trace directly

## Intervention Moves

- Detect invocation style: bare vs. parameterized
- Route to @trace with appropriate argument unpacking
- Wrap with deprecation warning via deprecated() helper

## Workflow Steps

- Import deprecated() from agentops.helpers.deprecation
- Import trace decorator from agentops.sdk.decorators.factory via create_entity_decorator(SpanKind.SESSION)
- Define session(*args, **kwargs) function
- Implement conditional routing: if not args or not callable(args[0]), invoke trace(*args, **kwargs); else invoke trace(args[0], **kwargs)
- Apply deprecated() wrapper to session function with message 'Use @trace decorator instead.'
- Return wrapped session callable

## Constraints

- Must preserve exact argument passing to @trace
- Must handle both @session and @session(...) syntax
- Deprecation warning must be emitted on every invocation
- No additional logic or transformation of arguments

## Cautions

- Ensure trace decorator is available before wrapping session
- Test both bare and parameterized invocation paths
- Verify deprecation warning is visible to end users

## Output Contract

- Callable @session decorator that accepts any arguments, transparently invokes @trace with the same arguments, and emits a deprecation warning. Callers receive the same behavior as @trace with no functional difference.

## Example Executions

### Example 1

- Input: @session
def my_function(): pass
- Output: my_function is decorated; @trace is invoked with my_function as first argument; deprecation warning emitted
- Notes: Bare decorator invocation

### Example 2

- Input: @session(name='custom_name')
def my_function(): pass
- Output: my_function is decorated; @trace is invoked with name='custom_name'; deprecation warning emitted
- Notes: Parameterized decorator invocation

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Existing code uses @session decorator and must continue to work; migration to @trace is in progress.

## Examples

### Example 1

Input:

  @session
  def my_function(): pass

Output:

  my_function is decorated; @trace is invoked with my_function as first argument; deprecation warning emitted

Notes:

  Bare decorator invocation

### Example 2

Input:

  @session(name='custom_name')
  def my_function(): pass

Output:

  my_function is decorated; @trace is invoked with name='custom_name'; deprecation warning emitted

Notes:

  Parameterized decorator invocation
