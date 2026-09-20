---
id: "b230ef59-f428-5b7a-9efb-61313f845c3f"
name: "HTTP Request Mocking"
description: "Mock HTTP requests at the client level using requests_mock to inject predefined responses without network calls. Use when test code calls HTTP client methods and response content or status code must be controlled deterministically."
version: "0.1.0"
tags:
  - "testing"
  - "mocking"
  - "http"
  - "isolation"
  - "pytest"
  - "requests_mock"
triggers:
  - "Test function calls HTTP client methods (e.g., requests.get, requests.post)"
  - "Response content or status code must be controlled without network I/O"
  - "Test isolation required; no external service dependency acceptable"
examples:
  - input: "Test function with requests_mock fixture; HTTP GET call to http://api.example.com"
    output: "Mock returns status 200 with json={'key': 'value'}; assertion response.json()['key'] == 'value' passes"
    notes: "Client-level stubbing; no network I/O"
---

# HTTP Request Mocking

Mock HTTP requests at the client level using requests_mock to inject predefined responses without network calls. Use when test code calls HTTP client methods and response content or status code must be controlled deterministically.

## Prompt

1. Import or receive the requests_mock fixture in your test function signature.
2. Call requests_mock.get(), .post(), .put(), .delete(), or other HTTP method to register a mock endpoint.
3. Specify the URL pattern and response payload (json, text, status_code, etc.).
4. Execute the code under test that makes the HTTP call.
5. Assert that the response matches the mocked values (status code, JSON keys, etc.).
6. Verify no actual network request was made.

## Objective

stub_http_client_calls
## Applicable Signals

- HTTP client invocation detected in test code
- Need for deterministic response injection
- Test environment lacks network access or network calls are undesirable

## Contraindications

- Actual HTTP interaction recording is preferred (use VCR instead)
- Response variability across runs is required or expected
- Integration testing with real endpoints is the goal

## Workflow Steps

- {'step': 1, 'action': 'Receive requests_mock fixture', 'detail': 'Add requests_mock parameter to test function signature'}
- {'step': 2, 'action': 'Register mock endpoint', 'detail': 'Call requests_mock.get/post/etc with URL and response dict (json, status_code, etc.)'}
- {'step': 3, 'action': 'Execute code under test', 'detail': 'Run the function or code that makes the HTTP request'}
- {'step': 4, 'action': 'Assert response', 'detail': 'Verify response.status_code, response.json(), or other response attributes match mock'}

## Constraints

- requests_mock fixture must be available (pytest plugin installed)
- Mock registration must occur before the HTTP call in test execution order
- URL pattern in mock must match the exact URL called by the client

## Cautions

- Mocking at client level does not catch network-layer issues; use VCR for end-to-end recording if needed
- Ensure mock response structure matches what the code under test expects to avoid false positives

## Output Contract

- HTTP request intercepted by requests_mock; predefined response returned with specified status code and JSON payload; assertion validates response content matches mock; no actual network call occurs.

## Example Therapist Responses

### Example 1

- Client/Input: Test function with requests_mock fixture; HTTP GET call to http://api.example.com
- Therapist/Output: Mock returns status 200 with json={'key': 'value'}; assertion response.json()['key'] == 'value' passes
- Notes: Client-level stubbing; no network I/O

## Triggers

- Test function calls HTTP client methods (e.g., requests.get, requests.post)
- Response content or status code must be controlled without network I/O
- Test isolation required; no external service dependency acceptable

## Examples

### Example 1

Input:

  Test function with requests_mock fixture; HTTP GET call to http://api.example.com

Output:

  Mock returns status 200 with json={'key': 'value'}; assertion response.json()['key'] == 'value' passes

Notes:

  Client-level stubbing; no network I/O
