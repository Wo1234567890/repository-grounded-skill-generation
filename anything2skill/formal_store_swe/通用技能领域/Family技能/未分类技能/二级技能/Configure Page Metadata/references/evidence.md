# Configure Page Metadata Evidence

- family: 未分类技能
- skill_id: 09ce233c-5aa4-597c-9eef-504f22c29721
- support_count: 2

## Evidence 1

- support_id: e59edc42-c110-5954-bffa-869ac2a7e914
- relation_type: support
- document: nextjs14-optimization.md
- doc_id: 348ef37d-8f72-5077-a811-da520815fca2
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/nextjs14-optimization.md
- section: Metadata
- span: 1553:2220
- confidence: 0.85
- quote: The Metadata API in Next.js allows you to modify the `<head>` element of a page. You can configure metadata in two ways:

* **Config-based Metadata**: Export a [static `metadata` object](/docs/app/api-reference/functions/generate-metadata#metadata-object) or a dynamic [`generateMetadata` function](/docs/app/api-reference/functions/generate-metadata#generatemetadata-function) in a `layout.js` or `page.js` file.
* **File-based Metadata**: Add static or dynamically generated special files to route segments.

Additionally, you can create dynamic Open Graph Images using JSX and CSS with [imageResponse](/docs/app/api-reference/functions/image-response) constructor.

## Evidence 2

- support_id: 234395fe-ec37-5de5-b92f-55c77fed9ac6
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 29489:30526
- confidence: 0.78
- quote: ### agentops/__init__.py

```python
# For backwards compatibility
from agentops.legacy import (
    start_session,
    end_session,
    track_agent,
    track_tool,
    end_all_sessions,
    Session,
    ToolEvent,
    ErrorEvent,
    ActionEvent,
    LLMEvent,
)  # type: ignore

# Import all required modules at the top
from opentelemetry.trace import get_current_span
from agentops.semconv import (
    AgentAttributes,
    ToolAttributes,
    WorkflowAttributes,
    CoreAttributes,
    SpanKind,
    SpanAttributes,
)
import json
from typing import List, Optional, Union, Dict, Any
from agentops.client import Client
from agentops.sdk.core import TraceContext, tracer
from agentops.sdk.decorators import trace, session, agent, task, workflow, operation, tool, guardrail, track_endpoint
from agentops.enums import TraceState, SUCCESS, ERROR, UNSET
from opentelemetry.trace.status import StatusCode

from agentops.logging.config import logger
from agentops.helpers.deprecation import deprecated, warn_deprecated_param
import threading
