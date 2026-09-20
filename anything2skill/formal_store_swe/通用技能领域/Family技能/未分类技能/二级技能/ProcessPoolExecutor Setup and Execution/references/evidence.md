# ProcessPoolExecutor Setup and Execution Evidence

- family: 未分类技能
- skill_id: 1aaea44c-47b6-537f-99b8-44c0de67c697
- support_count: 3

## Evidence 1

- support_id: a3bf87df-924f-51cc-be2c-18d28f167040
- relation_type: support
- document: python312-parallelism.md
- doc_id: 771b7202-2a1d-5eea-bda3-df5cd4ea6620
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/python312-parallelism.md
- section: `concurrent.futures` — Launching parallel tasks¶
- span: 11065:13779
- confidence: 0.92
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

- support_id: 2582a0bf-b2e7-5be5-b667-a4af4b3c9328
- relation_type: support
- document: tfidf-reference.txt
- doc_id: fc9056b5-59f5-5e1a-9452-59d955d52e19
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/tfidf-reference.txt
- section: 6    Scoring, term weighting and the
- span: 74579:76173
- confidence: 0.85
- quote: Exercise 6.20
                 Show that for the query affection, the relative ordering of the scores of the three doc-
                 uments in Figure 6.13 is the reverse of the ordering of the scores for the query jealous
                 gossip.

Exercise 6.21
                 In turning a query into a unit vector in Figure 6.13, we assigned equal weights to each
                 of the query terms. What other principled approaches are plausible?

Exercise 6.23
                 Refer to the tf and idf values for four terms and three documents in Exercise 6.10.
                 Compute the two top scoring documents on the query best car insurance for each of
                 the following weighing schemes: (i) nnn.atc; (ii) ntc.atc.

Exercise 6.24
                 Suppose that the word coyote does not occur in the collection used in Exercises 6.10
                 and 6.23. How would one compute ntc.atc scores for the query coyote insurance?

Online edition (c) 2009 Cambridge UP
            6.5 References and further reading                                         133

## Evidence 3

- support_id: 62f3fe85-9c34-5f96-870d-562a7f319adb
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 83534:83923
- confidence: 0.78
- quote: @operation
    def perform_task(self, task):
        # Agent task logic here
        return f"Completed {task}"

# Create a session
@session
def my_workflow():
    # Your session code here
    agent = MyAgent("research-agent")
    result = agent.perform_task("data analysis")
    return result

# Run the session
my_workflow()
```

Jupyter Notebook with sample code that you can run!
