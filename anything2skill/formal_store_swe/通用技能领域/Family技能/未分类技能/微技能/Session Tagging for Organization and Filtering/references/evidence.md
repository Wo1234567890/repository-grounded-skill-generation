# Session Tagging for Organization and Filtering Evidence

- family: 未分类技能
- skill_id: ae4e8bc5-4993-5ebb-8b0e-8a67099bc41b
- support_count: 1

## Evidence 1

- support_id: 3975b647-4a86-5a18-a65d-5f78daa633b6
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 78528:78959
- confidence: 0.75
- quote: # Tags

[Tags](https://github.com/AgentOps-AI/agentops/blob/main/v2/concepts/tags) help you organize and filter your sessions. You can add tags when initializing AgentOps or when starting a session:

```python
# Add tags when initializing
agentops.init(api_key="YOUR_API_KEY", tags=["production", "web-app"])

# Or when manually starting a session
agentops.start_session(tags=["customer-service", "tier-1"])
```

# Host Environment
