# LangChain Agent Integration with AgentOps Callback Handler Evidence

- family: 未分类技能
- skill_id: 9414dd2d-c870-517a-bca5-3f031cafdbe2
- support_count: 1

## Evidence 1

- support_id: 46755a36-9c41-52d7-800b-62e79f6be335
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 138023:143864
- confidence: 0.85
- quote: # Create Agents
researcher_agent = agents.research_agent()
writer_agent = agents.writer_agent()
review_agent = agents.review_agent()

result = crew.kickoff()
print("Job Posting Creation Process Completed.")
print("Final Job Posting:")
print(result)

agentops.end_trace(tracer, end_state="Success")

```

### examples/langchain/langchain_examples.py

# The only difference with using AgentOps is that we'll also import this special Callback Handler
from agentops.integration.callbacks.langchain import (
    LangchainCallbackHandler as AgentOpsLangchainCallbackHandler,
)

# This is where AgentOps comes into play. Before creating our LLM instance via Langchain, first we'll create an instance of the AO LangchainCallbackHandler. After the handler is initialized, a session will be recorded automatically.
#
# Pass in your API key, and optionally any tags to describe this session for easier lookup in the AO dashboard.
agentops_handler = AgentOpsLangchainCallbackHandler(tags=["Langchain Example", "agentops-example"])

llm = ChatOpenAI(callbacks=[agentops_handler], model="gpt-3.5-turbo")

# You must pass in a callback handler to record your agent
llm.callbacks = [agentops_handler]

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Respond only in Spanish."),
        ("human", "{input}"),
        # Placeholders fill up a **list** of messages
        ("placeholder", "{agent_scratchpad}"),
        # ("tool_names", "find_movie")
    ]
)

# Agents generally use tools. Let's define a simple tool here. Tool usage is also recorded.
@tool
def find_movie(genre: str) -> str:
    """Find available movies"""
    if genre == "drama":
        return "Dune 2"
    else:
        return "Pineapple Express"

tools = [find_movie]

# For each tool, you need to also add the callback handler
for t in tools:
    t.callbacks = [agentops_handler]

# Add the tools to our LLM
llm_with_tools = llm.bind_tools([find_movie])

# ## Check your session
# Finally, check your run on [AgentOps](https://app.agentops.ai). You will see a session recorded with the LLM calls and tool usage.

# Let's check programmatically that spans were recorded in AgentOps
print("\n" + "=" * 50)
print("Now let's verify that our LLM calls were tracked properly...")
try:
    import agentops

```

### examples/README.md

# AgentOps Examples
