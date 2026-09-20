---
id: "1f439a5d-179b-50ba-a142-15dbb4e7950a"
name: "VCR Cassette Management"
description: "Record, store, and maintain HTTP interaction cassettes for deterministic testing. Sanitize sensitive data from recorded interactions and update cassettes when API contracts change."
version: "0.1.0"
tags:
  - "testing"
  - "integration_testing"
  - "vcr"
  - "cassette"
  - "api_mocking"
  - "test_data"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Integration or end-to-end tests require external API calls"
  - "Need for reproducible offline test execution"
  - "CI/CD pipeline requires deterministic test behavior"
examples:
  - input: "Integration test calls external payment API; VCR records the interaction"
    output: "Cassette file tests/cassettes/payment_api_charge.yaml with sanitized request/response; sensitive fields replaced with placeholders"
    notes: "Cassette can be replayed offline in CI without exposing real API credentials"
  - input: "External API response format changes; existing cassette is stale"
    output: "Cassette regenerated with new response structure; old version archived or replaced"
    notes: "Tests now pass with updated API contract; stale cassette would have masked the breaking change"
---

# VCR Cassette Management

Record, store, and maintain HTTP interaction cassettes for deterministic testing. Sanitize sensitive data from recorded interactions and update cassettes when API contracts change.

## Prompt

Use this skill to manage recorded API interactions stored in tests/cassettes/. Before committing cassettes, sanitize all sensitive information (tokens, keys, IDs). When external APIs change their response format or behavior, regenerate and update the corresponding cassette files. Cassettes enable offline test execution and reproducible CI/CD runs.

## Objective

Manage recorded API interactions for deterministic and reproducible testing
## Applicable Signals

- Test suite depends on external service responses
- Reproducibility across environments is required
- Offline test execution is a requirement

## Contraindications

- Testing real-time API behavior changes or live service state
- Validating live service health or current availability
- Testing time-sensitive or session-dependent interactions

## Workflow Steps

- {'step': 1, 'action': 'Record HTTP interactions', 'detail': 'Configure VCR to record API calls during test execution; store raw cassettes in tests/cassettes/'}
- {'step': 2, 'action': 'Sanitize sensitive data', 'detail': 'Remove or mask authentication tokens, API keys, user IDs, and other sensitive fields from recorded cassettes'}
- {'step': 3, 'action': 'Document cassette purpose and format', 'detail': 'Add comments or metadata describing the API endpoint, expected response structure, and any known limitations'}
- {'step': 4, 'action': 'Commit sanitized cassettes', 'detail': 'Version-control cassette files; include in code review to verify no sensitive data is present'}
- {'step': 5, 'action': 'Monitor and update on API changes', 'detail': 'When external API contracts change, regenerate affected cassettes and commit updated versions'}

## Constraints

- All sensitive information must be sanitized before cassette storage
- Cassettes must be version-controlled and reviewed for data leaks
- Cassettes must be regenerated when external API contracts change

## Cautions

- Do not commit cassettes containing API keys, authentication tokens, or personally identifiable information
- Stale cassettes may mask real API failures; update regularly when dependencies change
- Cassette replay does not validate live API availability; use live tests in production validation

## Output Contract

- Sanitized cassette files stored in tests/cassettes/ directory, ready for replay in CI/CD pipelines. Each cassette contains recorded HTTP request-response pairs with all sensitive information removed, enabling deterministic offline test execution.

## Example Executions

### Example 1

- Input: Integration test calls external payment API; VCR records the interaction
- Output: Cassette file tests/cassettes/payment_api_charge.yaml with sanitized request/response; sensitive fields replaced with placeholders
- Notes: Cassette can be replayed offline in CI without exposing real API credentials

### Example 2

- Input: External API response format changes; existing cassette is stale
- Output: Cassette regenerated with new response structure; old version archived or replaced
- Notes: Tests now pass with updated API contract; stale cassette would have masked the breaking change

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Integration or end-to-end tests require external API calls
- Need for reproducible offline test execution
- CI/CD pipeline requires deterministic test behavior

## Examples

### Example 1

Input:

  Integration test calls external payment API; VCR records the interaction

Output:

  Cassette file tests/cassettes/payment_api_charge.yaml with sanitized request/response; sensitive fields replaced with placeholders

Notes:

  Cassette can be replayed offline in CI without exposing real API credentials

### Example 2

Input:

  External API response format changes; existing cassette is stale

Output:

  Cassette regenerated with new response structure; old version archived or replaced

Notes:

  Tests now pass with updated API contract; stale cassette would have masked the breaking change
