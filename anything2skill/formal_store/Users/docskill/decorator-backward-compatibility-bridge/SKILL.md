---
id: "12c14332-2c45-5fb7-bce9-f6acd3f1a926"
name: "Decorator Backward Compatibility Bridge"
description: "Wrapper that maps a deprecated @session decorator to the new @trace decorator, handling both direct and parameterized invocation patterns while emitting deprecation warnings. Maintains API compatibility during decorator naming migration without breaking existing code."
version: "0.1.0"
tags:
  - "decorator"
  - "backward_compatibility"
  - "deprecation"
  - "api_migration"
  - "python"
triggers:
  - "Codebase still uses @session decorator; need to redirect to @trace without immediate refactoring; deprecation warning acceptable"
---

# Decorator Backward Compatibility Bridge

Wrapper that maps a deprecated @session decorator to the new @trace decorator, handling both direct and parameterized invocation patterns while emitting deprecation warnings. Maintains API compatibility during decorator naming migration without breaking existing code.

## Prompt

Implement a @session decorator wrapper that:
1. Accepts both direct invocation (@session) and parameterized invocation (@session(name=...))
2. Routes all calls to the underlying @trace decorator
3. Applies a deprecation warning to signal migration path
4. Preserves argument forwarding for kwargs and positional args
5. Check if args[0] is callable to distinguish direct vs. parameterized calls

## Objective

Maintain API compatibility during decorator naming migration without breaking existing code
## Applicable Signals

- Codebase still uses @session decorator on functions or methods
- Need to redirect to @trace without immediate refactoring
- Deprecation warnings are acceptable in logs

## Contraindications

- Full migration to @trace has been completed
- Deprecation warnings must be eliminated from output
- @session has custom behavior distinct from @trace

## Intervention Moves

- Check if args is empty or args[0] is not callable → route to trace(*args, **kwargs)
- If args[0] is callable → route to trace(args[0], **kwargs)
- Wrap the session function with deprecated() decorator to emit warning

## Workflow Steps

- Define session(*args, **kwargs) function
- Implement conditional logic: if not args or not callable(args[0]), return trace(*args, **kwargs); else return trace(args[0], **kwargs)
- Apply deprecated("Use @trace decorator instead.")(session) to wrap the function
- Return the wrapped session function for use as a decorator

## Constraints

- Must preserve the exact signature and behavior of @trace
- Deprecation warning must be emitted on every invocation
- Argument routing logic must handle both @session and @session(...) patterns

## Cautions

- If @session was intentionally distinct from @trace in the original codebase, this bridge will mask that distinction
- Callers relying on @session-specific behavior will experience silent behavioral changes

## Output Contract

- @session decorator is callable with the same signature as @trace; deprecation warning is logged on invocation; all calls are successfully routed to @trace with arguments preserved

## Triggers

- Codebase still uses @session decorator; need to redirect to @trace without immediate refactoring; deprecation warning acceptable
