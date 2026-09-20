# Application Performance Monitoring with OpenTelemetry 子技能地图

## 子技能列表

- [Implement Contextual Error Logging](通用技能领域/Family技能/未分类技能/微技能/Implement Contextual Error Logging/SKILL.md) ｜ 微技能
  - 适用：Implement specific exception types with meaningful error messages and contextual logging to ensure errors are logged with sufficient context for debugging and production issue resolution.
  - 线索：Writing exception handlers or error paths, Debugging production issues or test failures, Implementing error recovery logic, error_handling, logging
- [Record and Replay HTTP Interactions with pytest-vcr](通用技能领域/Family技能/未分类技能/微技能/Record and Replay HTTP Interactions with pytest-vcr/SKILL.md) ｜ 微技能
  - 适用：Use pytest-vcr to record HTTP requests and responses during test execution, then replay them in subsequent runs to avoid external API calls. Enables deterministic, fast test runs by isolating tests from external HTTP dependencies.
  - 线索：Test function makes HTTP requests to external APIs, Need deterministic test runs independent of external service availability, Require fast test execution without network latency, testing, http_mocking
- [Test Fixture Setup](通用技能领域/Family技能/未分类技能/微技能/Test Fixture Setup/SKILL.md) ｜ 微技能
  - 适用：Create and manage reusable pytest fixtures in conftest.py for consistent test initialization. Fixtures provide mock objects, stubs, and test dependencies that can be injected across unit, integration, and end-to-end test cases.
  - 线索：Multiple test cases require the same mock client or external service stub, Test suite initialization needs consistent, reusable test dependencies, Fixture-based dependency injection is preferred over inline mock creation, pytest, testing
