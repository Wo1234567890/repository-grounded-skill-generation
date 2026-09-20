# Initialize AgentOps Client with API Keys Evidence

- family: 未分类技能
- skill_id: 0d3b8c73-bb09-5ca7-be2b-c651fe62185f
- support_count: 1

## Evidence 1

- support_id: 83c93129-defa-5c24-a4fb-9f8f237f6fda
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 126986:128092
- confidence: 0.85
- quote: # Next, we'll grab our API keys. You can use dotenv like below or however else you like to load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "your_openai_api_key_here")
os.environ["AGENTOPS_API_KEY"] = os.getenv("AGENTOPS_API_KEY", "your_api_key_here")

# Next we initialize the AgentOps client.
agentops.init(auto_start_session=True, trace_name="OpenAI Sync Example", tags=["openai", "sync", "agentops-example"])
tracer = agentops.start_trace(
    trace_name="OpenAI Sync Example", tags=["openai-sync-example", "openai", "agentops-example"]
)
client = OpenAI()

user_prompt = "Write a very short story about a cyber-warrior trapped in the imperial time period."
