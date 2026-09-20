# Reward Function Contract Definition Evidence

- family: 未分类技能
- skill_id: 8612fede-8fc7-5e43-bf65-c945865f7b6f
- support_count: 3

## Evidence 1

- support_id: d2dcb409-3261-5343-8307-ab33e2a92411
- relation_type: support
- document: trl-grpo-017.md
- doc_id: 1b1cfe5e-1be5-5bc1-9b07-6e37f39e1ae1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/trl-grpo-017.md
- section: GRPO Trainer
- span: 18958:19320
- confidence: 0.85
- quote: Depending on the dataset format, the input will vary:

- For standard format, `prompts` and `completions` will be lists of strings. 
- For conversational format, `prompts` and `completions` will be lists of message dictionaries. 
-

Return value: The function must return a list of floats. Each float represents the reward corresponding to a single completion.

## Evidence 2

- support_id: b8e5ba30-e118-5ec1-8fd1-1d738853e778
- relation_type: support
- document: python312-parallelism.md
- doc_id: 771b7202-2a1d-5eea-bda3-df5cd4ea6620
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/python312-parallelism.md
- section: `concurrent.futures` — Launching parallel tasks¶
- span: 13782:16070
- confidence: 0.82
- quote: Return `True` if the call was successfully cancelled or finished
running.

result(timeout=None)¶

Return the value returned by the call. If the call hasn’t yet completed
then this method will wait up to timeout seconds. If the call hasn’t
completed in timeout seconds, then a
`TimeoutError` will be raised. timeout can be
an int or float. If timeout is not specified or `None`, there is no
limit to the wait time.

If the future is cancelled before completing then `CancelledError`
will be raised.

If the call raised an exception, this method will raise the same exception.

exception(timeout=None)¶

Return the exception raised by the call. If the call hasn’t yet
completed then this method will wait up to timeout seconds. If the
call hasn’t completed in timeout seconds, then a
`TimeoutError` will be raised. timeout can be
an int or float. If timeout is not specified or `None`, there is no
limit to the wait time.

If the future is cancelled before completing then `CancelledError`
will be raised.

If the call completed without raising, `None` is returned.

add_done_callback(fn)¶

Attaches the callable fn to the future. fn will be called, with the
future as its only argument, when the future is cancelled or finishes
running.

Added callables are called in the order that they were added and are
always called in a thread belonging to the process that added them. If
the callable raises an `Exception` subclass, it will be logged and
ignored. If the callable raises a `BaseException` subclass, the
behavior is undefined.

If the future has already completed or been cancelled, fn will be
called immediately.

The following `Future` methods are meant for use in unit tests and
`Executor` implementations.

set_running_or_notify_cancel()¶

This method should only be called by `Executor` implementations
before executing the work associated with the `Future` and by unit
tests.

If the method returns `False` then the `Future` was cancelled,
i.e. `Future.cancel()` was called and returned `True`. Any threads
waiting on the `Future` completing (i.e. through
`as_completed()` or `wait()`) will be woken up.

If the method returns `True` then the `Future` was not cancelled
and has been put in the running state, i.e. calls to
`Future.running()` will return `True`.

## Evidence 3

- support_id: 7beab44a-1169-54c0-930a-dc2d41b3ebaa
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 72711:73841
- confidence: 0.85
- quote: # Define a tool
@tool(name="AdvancedSearch", cost=0.02)
def advanced_web_search(query: str) -> str:
    # Simulate a more advanced search
    return f"Advanced search results for '{query}': [Details...]"

# Define an agent class
@agent(name="ResearchSpecialistAgent")
class ResearchAgent:
    def __init__(self, agent_id: str):
        self.agent_id = agent_id # This will be used as the agent_id in AgentOps

# Define a workflow using the @trace decorator
@trace(name="FullResearchWorkflow", tags=["research", "analysis", "example"])
def run_full_research_workflow(topic: str) -> str:
    specialist_agent = ResearchAgent(agent_id="researcher-alpha-007")
    research_findings = specialist_agent.conduct_research(topic)
