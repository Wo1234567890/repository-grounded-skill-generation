# Version-Specific OpenAI Instrumentor Initialization Evidence

- family: 未分类技能
- skill_id: cd0bfed4-59ec-5259-90fd-1903beb88f0e
- support_count: 1

## Evidence 1

- support_id: dd882379-cd9c-5791-b685-dfb72fe096ff
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 115165:119390
- confidence: 0.80
- quote: from opentelemetry.metrics import Meter

_instruments = ("openai >= 0.27.0",)

class OpenaiInstrumentor(CommonInstrumentor):
    """An instrumentor for OpenAI's client library with comprehensive coverage."""

# Create instrumentor config
        config = InstrumentorConfig(
            library_name=LIBRARY_NAME,
            library_version=LIBRARY_VERSION,
            wrapped_methods=self._get_wrapped_methods(),
            metrics_enabled=True,
            dependencies=_instruments,
        )

super().__init__(config)

def _initialize(self, **kwargs):
        """Handle version-specific initialization."""
        if not is_openai_v1():
            # For v0, use the legacy instrumentor
            OpenAIV0Instrumentor().instrument(**kwargs)
            # Skip normal instrumentation
            self.config.wrapped_methods = []

def _custom_wrap(self, **kwargs):
        """Add custom wrappers for streaming functionality."""
        if is_openai_v1() and self._tracer:
            # from wrapt import wrap_function_wrapper
            # # Add streaming wrappers for v1
            try:
                # Chat completion streaming wrappers

wrap_function_wrapper(
                    "openai.resources.chat.completions",
                    "Completions.create",
                    chat_completion_stream_wrapper(self._tracer),
                )

wrap_function_wrapper(
                    "openai.resources.chat.completions",
                    "AsyncCompletions.create",
                    async_chat_completion_stream_wrapper(self._tracer),
                )

# Beta chat completion streaming wrappers
                wrap_function_wrapper(
                    "openai.resources.beta.chat.completions",
                    "Completions.parse",
                    chat_completion_stream_wrapper(self._tracer),
                )

wrap_function_wrapper(
                    "openai.resources.beta.chat.completions",
                    "AsyncCompletions.parse",
                    async_chat_completion_stream_wrapper(self._tracer),
                )

# Responses API streaming wrappers
                wrap_function_wrapper(
                    "openai.resources.responses",
                    "Responses.create",
                    responses_stream_wrapper(self._tracer),
                )
