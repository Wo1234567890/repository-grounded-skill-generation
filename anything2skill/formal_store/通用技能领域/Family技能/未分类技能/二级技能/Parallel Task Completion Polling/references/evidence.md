# Parallel Task Completion Polling Evidence

- family: 未分类技能
- skill_id: ee42057a-3ada-5055-9c21-aa1f0645e482
- support_count: 3

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

## Evidence 2

- support_id: 503a8c4e-af82-5aa2-9f5a-d678ed07d70d
- relation_type: support
- document: flink-118-datastream.md
- doc_id: 8a36b10a-4e32-5b2b-bc38-0c56680e2cda
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/flink-118-datastream.md
- section: DataStream API▾
- span: 17782:20490
- confidence: 0.87
- quote: ```
getExecutionEnvironment()

createLocalEnvironment()

createRemoteEnvironment(host: String, port: Int, jarFiles: String*)

```

For specifying data sources the execution environment has several methods to
read from files using various methods: you can just read them line by line, as
CSV files, or using any of the other provided sources. To just read a text file
as a sequence of lines, you can use:

```
val env = StreamExecutionEnvironment.getExecutionEnvironment()

val text: DataStream[String] = env.readTextFile("file:///path/to/file")

```

This will give you a DataStream on which you can then apply transformations to
create new derived DataStreams.

You apply transformations by calling methods on DataStream with a
transformation functions. For example, a map transformation looks like this:

```
val input: DataSet[String] = ...

val mapped = input.map { x => x.toInt }

```

This will create a new DataStream by converting every String in the original
collection to an Integer.

Once you have a DataStream containing your final results, you can write it to
an outside system by creating a sink. These are just some example methods for
creating a sink:

```
writeAsText(path: String)

print()

```

Once you specified the complete program you need to trigger the program
execution by calling `execute()` on the `StreamExecutionEnvironment`.
Depending on the type of the `ExecutionEnvironment` the execution will be
triggered on your local machine or submit your program for execution on a
cluster.

The `execute()` method will wait for the job to finish and then return a
`JobExecutionResult`, this contains execution times and accumulator results.

```
final JobClient jobClient = env.executeAsync();

final JobExecutionResult jobExecutionResult = jobClient.getJobExecutionResult().get();

```

## Evidence 3

- support_id: 21a28cfe-50d9-5c5e-aeb4-22472184974a
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 55670:57302
- confidence: 0.80
- quote: # Update legacy module's _current_session and _current_trace_context
                    # This is tricky; direct access to another module's globals is not ideal.
                    # Prefer explicit calls if possible, but for maximum BC:
                    try:
                        import agentops.legacy

agentops.legacy._current_session = self._legacy_session_for_init_trace
                        agentops.legacy._current_trace_context = self._init_trace_context
                    except ImportError:
                        pass  # Should not happen

self._initialized = True  # Successfully initialized and auto-trace started (if configured)
            # For backward compatibility, return the legacy session wrapper when auto_start_session=True
            return self._legacy_session_for_init_trace
        else:
            logger.debug("Auto-start session is disabled. No init trace started by client.")
            self._initialized = True  # Successfully initialized, just no auto-trace
            return None  # No auto-session, so return None

def configure(self, **kwargs: Any) -> None:
        """Update client configuration"""
        self.config.configure(**kwargs)
