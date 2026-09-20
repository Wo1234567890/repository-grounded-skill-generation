---
id: "4b64cad2-1d18-5b49-8859-e7f28fc60dd2"
name: "Record and Replay HTTP Interactions with pytest-vcr"
description: "Use pytest-vcr to record HTTP requests and responses during test execution, then replay them in subsequent runs to avoid external API calls. Enables deterministic, fast test runs by isolating tests from external HTTP dependencies."
version: "0.1.0"
tags:
  - "testing"
  - "http_mocking"
  - "pytest"
  - "vcr"
  - "test_isolation"
  - "deterministic_testing"
triggers:
  - "Test function makes HTTP requests to external APIs"
  - "Need deterministic test runs independent of external service availability"
  - "Require fast test execution without network latency"
examples:
  - input: "Test function with HTTP request: def test_api_call(): response = client.make_request(); assert response.status_code == 200"
    output: "First run: cassette file created with recorded request/response pair. Second run: same test replays cassette; assertion passes without network call."
    notes: "Cassette filename typically derived from test module and function name"
---

# Record and Replay HTTP Interactions with pytest-vcr

Use pytest-vcr to record HTTP requests and responses during test execution, then replay them in subsequent runs to avoid external API calls. Enables deterministic, fast test runs by isolating tests from external HTTP dependencies.

## Prompt

Apply @pytest.mark.vcr() decorator to test functions that make HTTP requests. On first execution, the decorator records all HTTP interactions into a cassette file. On subsequent runs, recorded interactions are replayed automatically, eliminating external API calls. Verify that test assertions pass using replayed responses.

## Objective

Isolate tests from external HTTP dependencies by recording and replaying interactions
## Applicable Signals

- HTTP client calls within test code
- External API dependency detected
- Test performance degradation due to network calls

## Contraindications

- Testing actual API integration behavior requiring real-time responses
- API responses must reflect current server state
- Recorded cassettes are stale or known to be unreliable
- Testing authentication flows with time-sensitive tokens

## Workflow Steps

- {'step': 1, 'action': 'Decorate test function with @pytest.mark.vcr()', 'detail': 'Apply decorator to any test that makes HTTP requests'}
- {'step': 2, 'action': 'Run test suite for first time', 'detail': 'pytest records all HTTP interactions into cassette file (YAML format by default)'}
- {'step': 3, 'action': 'Verify cassette creation', 'detail': 'Confirm cassette file exists in configured cassette library directory'}
- {'step': 4, 'action': 'Run tests subsequently', 'detail': 'pytest-vcr replays recorded interactions; no external API calls made'}
- {'step': 5, 'action': 'Validate test assertions', 'detail': 'Confirm all assertions pass using replayed response data'}

## Constraints

- Cassette files must be version-controlled and kept in sync with API contract changes
- First test run requires external API availability to record interactions
- Cassettes may contain sensitive data (API keys, tokens); sanitize before committing

## Cautions

- Stale cassettes can mask real API changes; periodically refresh recordings
- Ensure cassette directory is writable on first run
- Review recorded cassettes for sensitive information before version control

## Output Contract

- HTTP cassette file created and persisted on first run; subsequent test executions replay recorded interactions without external API calls; all test assertions pass deterministically; no network requests made after initial recording.

## Example Executions

### Example 1

- Input: Test function with HTTP request: def test_api_call(): response = client.make_request(); assert response.status_code == 200
- Output: First run: cassette file created with recorded request/response pair. Second run: same test replays cassette; assertion passes without network call.
- Notes: Cassette filename typically derived from test module and function name

## Triggers

- Test function makes HTTP requests to external APIs
- Need deterministic test runs independent of external service availability
- Require fast test execution without network latency

## Examples

### Example 1

Input:

  Test function with HTTP request: def test_api_call(): response = client.make_request(); assert response.status_code == 200

Output:

  First run: cassette file created with recorded request/response pair. Second run: same test replays cassette; assertion passes without network call.

Notes:

  Cassette filename typically derived from test module and function name
