---
id: "ec0993c4-75d0-57c2-9ff0-d5dab9023303"
name: "VCR Cassette Management for API Testing"
description: "Record, sanitize, and manage HTTP interactions using VCR cassettes stored in tests/cassettes/. Enables reproducible API testing without live external calls by capturing request/response pairs, removing sensitive data, and versioning cassettes to track API changes."
version: "0.1.0"
tags:
  - "testing"
  - "api_testing"
  - "vcr"
  - "cassettes"
  - "test_infrastructure"
  - "reproducibility"
triggers:
  - "Testing code that makes external API calls"
  - "Need to avoid live API dependencies"
  - "Reduce test latency and flakiness"
  - "Ensure test reproducibility across environments"
---

# VCR Cassette Management for API Testing

Record, sanitize, and manage HTTP interactions using VCR cassettes stored in tests/cassettes/. Enables reproducible API testing without live external calls by capturing request/response pairs, removing sensitive data, and versioning cassettes to track API changes.

## Prompt

1. Store cassettes in tests/cassettes/ directory.
2. Record HTTP interactions by running tests against live API once.
3. Sanitize sensitive information (API keys, tokens, credentials) from cassette files before committing.
4. Update cassettes when API contract changes or responses differ from recorded state.
5. Verify cassette replay works without external API calls in subsequent test runs.

## Objective

Enable reproducible API testing without live external calls
## Applicable Signals

- HTTP requests to external services in test suite
- Test execution time concerns
- API availability or rate-limiting constraints
- CI/CD pipeline isolation requirements

## Contraindications

- Testing real-time API behavior or live integration scenarios
- Cassette data is stale and API contract has changed significantly
- Sensitive data cannot be adequately sanitized from cassette files

## Workflow Steps

- {'step': 1, 'action': 'Create cassettes directory', 'detail': 'Ensure tests/cassettes/ exists and is tracked in version control'}
- {'step': 2, 'action': 'Record interactions', 'detail': 'Run tests against live API to capture HTTP request/response pairs'}
- {'step': 3, 'action': 'Sanitize sensitive data', 'detail': 'Remove or mask API keys, authentication tokens, and credentials from cassette files'}
- {'step': 4, 'action': 'Commit cassettes', 'detail': 'Add sanitized cassettes to version control'}
- {'step': 5, 'action': 'Verify replay', 'detail': 'Run tests offline to confirm cassettes replay without external API calls'}
- {'step': 6, 'action': 'Update on API changes', 'detail': 'Re-record cassettes when API contract or responses change'}

## Constraints

- Cassettes must be stored in tests/cassettes/ directory
- All sensitive information (API keys, tokens, credentials) must be sanitized before version control
- Cassettes must be updated when upstream API changes

## Cautions

- Ensure sanitization is complete; do not commit credentials or tokens
- Monitor cassette staleness; outdated cassettes may mask API contract violations
- Document cassette format and purpose for team maintenance

## Output Contract

- Cassette file created in tests/cassettes/ with sanitized sensitive data; test replays recorded interactions without external API calls; test suite runs reproducibly in isolated environments.

## Triggers

- Testing code that makes external API calls
- Need to avoid live API dependencies
- Reduce test latency and flakiness
- Ensure test reproducibility across environments
