# Executor Failure Detection and Recovery Evidence

- family: 未分类技能
- skill_id: 6ae95eca-2b03-52fc-bf4e-33e1e79c4fb6
- support_count: 2

## Evidence 1

- support_id: df62d6da-afcc-55b3-ac11-05f6d6ed4b64
- relation_type: constraint
- document: python312-parallelism.md
- doc_id: 771b7202-2a1d-5eea-bda3-df5cd4ea6620
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/python312-parallelism.md
- section: `concurrent.futures` — Launching parallel tasks¶
- span: 16073:19491
- confidence: 0.82
- quote: This method can only be called once and cannot be called after
`Future.set_result()` or `Future.set_exception()` have been
called.

set_result(result)¶

Sets the result of the work associated with the `Future` to
result.

This method should only be used by `Executor` implementations and
unit tests.

Changed in version 3.8: This method raises
`concurrent.futures.InvalidStateError` if the `Future` is
already done.

set_exception(exception)¶

Sets the result of the work associated with the `Future` to the
`Exception` exception.

This method should only be used by `Executor` implementations and
unit tests.

Changed in version 3.8: This method raises
`concurrent.futures.InvalidStateError` if the `Future` is
already done.

Module Functions¶
concurrent.futures.wait(fs, timeout=None, return_when=ALL_COMPLETED)¶

timeout can be used to control the maximum number of seconds to wait before
returning. timeout can be an int or float. If timeout is not specified
or `None`, there is no limit to the wait time.

return_when indicates when this function should return. It must be one of
the following constants:

Constant

Description

concurrent.futures.FIRST_COMPLETED¶

The function will return when any future finishes or is cancelled.

concurrent.futures.FIRST_EXCEPTION¶

The function will return when any future finishes by raising an
exception. If no future raises an exception
then it is equivalent to `ALL_COMPLETED`.

concurrent.futures.ALL_COMPLETED¶

The function will return when all futures finish or are cancelled.

concurrent.futures.as_completed(fs, timeout=None)¶

See also

PEP 3148 – futures - execute computations asynchronously

The proposal which described this feature for inclusion in the Python
standard library.

Exception classes¶
exception concurrent.futures.CancelledError¶

Raised when a future is cancelled.

exception concurrent.futures.TimeoutError¶

A deprecated alias of `TimeoutError`,
raised when a future operation exceeds the given timeout.

Changed in version 3.11: This class was made an alias of `TimeoutError`.

exception concurrent.futures.BrokenExecutor¶

Derived from `RuntimeError`, this exception class is raised
when an executor is broken for some reason, and cannot be used
to submit or execute new tasks.

Added in version 3.7.

exception concurrent.futures.InvalidStateError¶

## Evidence 2

- support_id: d11a2365-4bb8-5402-95ee-c784d2c8db81
- relation_type: constraint
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 57729:59031
- confidence: 0.72
- quote: # ------------------------------------------------------------
    # Remove the old __instance = None at the end of the class definition if it's a repeat
    # __instance = None # This was a class variable, should be defined once

# Make _init_trace_context and _legacy_session_for_init_trace accessible
    # to the atexit handler if it becomes a static/class method or needs access
    # For now, the atexit handler is global and uses global vars copied from these.

# Deprecate and remove the old global _active_session from this module.
    # Consumers should use agentops.start_trace() or rely on the auto-init trace.
    # For a transition, the auto-init trace's legacy wrapper is set to legacy module's globals.

# Ensure the global _active_session (if needed for some very old compatibility) points to the client's legacy session for init trace.
# This specific global _active_session in client.py is problematic and should be phased out.
# For now, _client_legacy_session_for_init_trace is the primary global for the auto-init trace's legacy Session.

# Remove the old global _active_session defined at the top of this file if it's no longer the primary mechanism.
# The new globals _client_init_trace_context and _client_legacy_session_for_init_trace handle the auto-init trace.

```
