# Load and Inject Environment Variables Safely Evidence

- family: 未分类技能
- skill_id: ba427050-7f6d-5312-9015-b85cded85fd1
- support_count: 1

## Evidence 1

- support_id: 53b5c31a-8dd6-5390-ba4d-d2474af5e4b8
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 126986:128092
- confidence: 0.80
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
