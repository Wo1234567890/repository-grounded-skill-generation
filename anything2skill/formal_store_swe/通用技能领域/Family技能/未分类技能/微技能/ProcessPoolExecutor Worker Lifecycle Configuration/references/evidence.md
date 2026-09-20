# ProcessPoolExecutor Worker Lifecycle Configuration Evidence

- family: 未分类技能
- skill_id: e3db3ce1-4c46-5250-8cf3-b6d590656c9e
- support_count: 2

## Evidence 1

- support_id: f44c195f-82c0-5417-ba9f-a7bff2574b86
- relation_type: support
- document: python312-parallelism.md
- doc_id: 771b7202-2a1d-5eea-bda3-df5cd4ea6620
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/python312-parallelism.md
- section: `concurrent.futures` — Launching parallel tasks¶
- span: 11065:13779
- confidence: 0.85
- quote: Changed in version 3.3: When one of the worker processes terminates abruptly, a
`BrokenProcessPool` error is now raised.
Previously, behaviour
was undefined but operations on the executor or its futures would often
freeze or deadlock.

Changed in version 3.7: The mp_context argument was added to allow users to control the
start_method for worker processes created by the pool.

Added the initializer and initargs arguments.

Note

The default `multiprocessing` start method
(see Contexts and start methods) will change away from
fork in Python 3.14. Code that requires fork be used for their
`ProcessPoolExecutor` should explicitly specify that by
passing a `mp_context=multiprocessing.get_context("fork")`
parameter.

Changed in version 3.11: The max_tasks_per_child argument was added to allow users to
control the lifetime of workers in the pool.

ProcessPoolExecutor Example¶
```
import concurrent.futures
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))

if __name__ == '__main__':
    main()

```

Future Objects¶
The `Future` class encapsulates the asynchronous execution of a callable.
`Future` instances are created by `Executor.submit()`.

class concurrent.futures.Future¶

Encapsulates the asynchronous execution of a callable. `Future`
instances are created by `Executor.submit()` and should not be created
directly except for testing.

cancel()¶

Attempt to cancel the call. If the call is currently being executed or
finished running and cannot be cancelled then the method will return
`False`, otherwise the call will be cancelled and the method will
return `True`.

cancelled()¶

Return `True` if the call was successfully cancelled.

running()¶

Return `True` if the call is currently being executed and cannot be
cancelled.

done()¶

## Evidence 2

- support_id: 11aa7168-c478-53e8-abe4-48959aee874b
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 49011:49970
- confidence: 0.75
- quote: # Single atexit handler registered flag
_atexit_registered = False

def _end_init_trace_atexit():
    """Global atexit handler to end the client's auto-initialized trace during shutdown."""
    global _client_init_trace_context, _client_legacy_session_for_init_trace
    if _client_init_trace_context is not None:
        logger.debug("Auto-ending client's init trace during shutdown.")
        try:
            # Use global tracer to end the trace directly
            if tracer.initialized and _client_init_trace_context.span.is_recording():
                tracer.end_trace(_client_init_trace_context, end_state="Shutdown")
        except Exception as e:
            logger.warning(f"Error ending client's init trace during shutdown: {e}")
        finally:
            _client_init_trace_context = None
            _client_legacy_session_for_init_trace = None  # Clear its legacy wrapper too

class Client:
    """Singleton client for AgentOps service"""
