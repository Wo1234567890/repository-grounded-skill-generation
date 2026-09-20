# Initialize AgentOps Session Evidence

- family: 未分类技能
- skill_id: 0fc63f00-75b2-5224-9651-74825cf60b50
- support_count: 1

## Evidence 1

- support_id: 0cdc8483-a2ac-52c1-8959-582bdba91a4b
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 75639:76148
- confidence: 0.75
- quote: AgentOps is built on [OpenTelemetry](https://opentelemetry.io/), a widely-adopted standard for observability instrumentation. This provides a robust and standardized approach to collecting, processing, and exporting telemetry data.

# Sessions

A [Session](https://github.com/AgentOps-AI/agentops/blob/main/v2/concepts/sessions) represents a single user interaction with your agent. When you initialize AgentOps using the `init` function, a session is automatically created for you:

```python
import agentops
