# Jakarta EE Package Import Migration Evidence

- family: 未分类技能
- skill_id: be9ee306-d51d-5fa4-ae33-699cbc310f42
- support_count: 2

## Evidence 1

- support_id: 8e8cdada-7b95-5abe-827c-7b4391e7a4c7
- relation_type: support
- document: spring-boot3-migration.md
- doc_id: 8a0719aa-8715-5b31-81e8-b6b7665dcece
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/spring-boot3-migration.md
- section: Spring Boot 3.0 Migration Guide
- span: 6260:10447
- confidence: 0.92
- quote: Jakarta EE
Whenever Spring Boot depends on a Jakarta EE specification, Spring Boot 3.0 has upgraded to the version that is included in Jakarta EE 10.
For example, Spring Boot 3.0 uses the Servlet 6.0 and JPA 3.1 specifications.

As well as dependency coordinate changes, Jakarta EE now uses `jakarta` packages rather than `javax`.
Once you’ve update your dependencies you may find that `import` statements in your project need to be updated.

There are a number of tools that can help with migration, including:

-

OpenRewrite recipes.

-

The Spring Boot Migrator project.

-

Migration support in IntelliJ IDEA.

Core Changes
Several changes have been made to the core of Spring Boot that will be relevant to most applications.

Image Banner Support Removed
Support for image-based application banners has been removed. `banner.gif`, `banner.jpg`, and `banner.png` files are now ignored and should be replaced with a text-based `banner.txt` file.

If you were relying on autowiring of a dependency into the constructor of a `@ConfigurationProperties` class, you must now annotate it with `@Autowired` to prevent it being identified as a target for property binding.

YamlJsonParser Has Been Removed
`YamlJsonParser` has been removed as SnakeYAML’s JSON parsing was inconsistent with the other parser implementations.
In the unlikely event that you were using `YamlJsonParser` directly, please migrate to one of the other `JsonParser` implementations.

Libraries targeting both Spring Boot 3.x and 2.x can safely list their auto-configuration classes in both `spring.factories` and `AutoConfiguration.imports`. Spring Boot 2.7, which supports both locations, will de-duplicate any entries that are listed twice.

Web Application Changes
If you’re upgrading a web application, the following section should be reviewed.

Spring MVC and WebFlux URL Matching Changes
As of Spring Framework 6.0, the trailing slash matching configuration option has been deprecated and its default value set to `false`.
This means that previously, the following controller would match both "GET /some/greeting" and "GET /some/greeting/":

```
@RestController
public class MyController {

@GetMapping("/some/greeting")
  public String greeting() {
    return "Hello";
  }

}
```

As of this Spring Framework change, "GET /some/greeting/" doesn’t match anymore by default and will result in an HTTP 404 error.

## Evidence 2

- support_id: 115d440d-5fb5-5a4e-839c-2cacd2c619b4
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 29489:30526
- confidence: 0.75
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
