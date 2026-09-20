# Create OpenAI Instrumentation Metrics Evidence

- family: 未分类技能
- skill_id: ce876721-97f3-53be-9f13-b151f476dbe4
- support_count: 1

## Evidence 1

- support_id: e179380c-e5c7-5645-bce1-578ee6d58505
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 120039:124389
- confidence: 0.75
- quote: def _create_metrics(self, meter: Meter) -> Dict[str, Any]:
        """Create metrics for OpenAI instrumentation."""
        metrics = StandardMetrics.create_standard_metrics(meter)

return metrics

def _custom_unwrap(self, **kwargs):
        """Handle version-specific uninstrumentation."""
        if not is_openai_v1():
            OpenAIV0Instrumentor().uninstrument(**kwargs)

def _get_wrapped_methods(self) -> list[WrapConfig]:
        """Get all methods that should be wrapped.

Note: Chat completions and Responses API methods are NOT included here
        as they are wrapped directly in _custom_wrap to support streaming.
        """
        wrapped_methods = []

# Beta APIs - these may not be available in all versions
        beta_methods = []
