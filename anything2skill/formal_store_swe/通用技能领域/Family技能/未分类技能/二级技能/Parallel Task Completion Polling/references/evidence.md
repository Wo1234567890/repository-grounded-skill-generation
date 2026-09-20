# Parallel Task Completion Polling Evidence

- family: 未分类技能
- skill_id: 5a63d94f-55c3-5860-b386-acd57dbebc38
- support_count: 1

## Evidence 1

- support_id: a6e83dc0-2ffc-5f61-b7a6-4ebe0a0042dd
- relation_type: support
- document: python312-parallelism.md
- doc_id: 771b7202-2a1d-5eea-bda3-df5cd4ea6620
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/python312-parallelism.md
- section: `concurrent.futures` — Launching parallel tasks¶
- span: 16073:19491
- confidence: 0.88
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
