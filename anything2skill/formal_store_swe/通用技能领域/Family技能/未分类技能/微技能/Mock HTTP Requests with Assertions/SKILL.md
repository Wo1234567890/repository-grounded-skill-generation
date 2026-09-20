---
id: "97e0c0ce-0bef-561f-93dd-06e2222c07dc"
name: "Mock HTTP Requests with Assertions"
description: "Use requests_mock to intercept and mock HTTP requests in tests, allowing assertion of request behavior and response validation without external API calls."
version: "0.1.0"
tags:
  - "testing"
  - "mocking"
  - "http"
  - "pytest"
  - "isolation"
  - "unit_test"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Test calls HTTP client methods"
  - "Need to mock specific endpoints"
  - "Validation required without external service calls"
examples:
  - input: "Test function with requests_mock fixture; HTTP client calls GET http://api.example.com"
    output: "Mock returns json={'key': 'value'}; assertion response.json()['key'] == 'value' passes"
    notes: "Endpoint mocked inline; no cassette file required"
---

# Mock HTTP Requests with Assertions

Use requests_mock to intercept and mock HTTP requests in tests, allowing assertion of request behavior and response validation without external API calls.

## Prompt

Use the requests_mock fixture to define mock responses for specific HTTP endpoints. Register the mock with the HTTP method (get, post, etc.) and endpoint URL, then provide the response payload. Execute the code under test and assert on the mocked response data. No external API call will be made.

## Objective

Isolate HTTP client code from external services and validate request/response handling
## Applicable Signals

- HTTP request interception needed
- Response payload must be controlled
- Test isolation from external dependencies

## Contraindications

- Testing actual HTTP protocol behavior
- Responses must reflect real server state
- VCR cassette replay is more appropriate for recorded interactions

## Workflow Steps

- {'step': 1, 'action': 'Inject requests_mock fixture into test function', 'detail': 'Add requests_mock parameter to test function signature'}
- {'step': 2, 'action': 'Register mock endpoint', 'detail': 'Call requests_mock.get() (or post/put/delete) with endpoint URL and response payload'}
- {'step': 3, 'action': 'Execute code under test', 'detail': 'Call the HTTP client method that will trigger the mocked request'}
- {'step': 4, 'action': 'Assert on response', 'detail': 'Validate response status code, JSON payload, or other response attributes'}

## Constraints

- requests_mock fixture must be available in test environment
- Mock endpoint URL must match the URL called by code under test
- Response payload structure must match expected client parsing

## Cautions

- Mocked responses do not validate actual server behavior
- Integration tests with real endpoints should be separate
- Ensure mock response structure matches production API contract

## Output Contract

- HTTP request intercepted and mocked response returned; test assertions on response data pass; no external API call made.

## Example Executions

### Example 1

- Input: Test function with requests_mock fixture; HTTP client calls GET http://api.example.com
- Output: Mock returns json={'key': 'value'}; assertion response.json()['key'] == 'value' passes
- Notes: Endpoint mocked inline; no cassette file required

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Test calls HTTP client methods
- Need to mock specific endpoints
- Validation required without external service calls

## Examples

### Example 1

Input:

  Test function with requests_mock fixture; HTTP client calls GET http://api.example.com

Output:

  Mock returns json={'key': 'value'}; assertion response.json()['key'] == 'value' passes

Notes:

  Endpoint mocked inline; no cassette file required
