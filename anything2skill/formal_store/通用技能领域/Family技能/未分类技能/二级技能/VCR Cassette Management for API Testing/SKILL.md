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
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
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

## 子技能目录
- [HTTP Interaction Recording and Replay with VCR](通用技能领域/Family技能/未分类技能/微技能/HTTP Interaction Recording and Replay with VCR/SKILL.md) ｜ 适用：Record and replay HTTP interactions in tests using VCR to eliminate external API calls and ensure test reproducibility. Captures request/response pairs on first run and replays them in subsequent runs without making network calls.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `HTTP Interaction Recording and Replay with VCR` 时，优先调用它。 线索：Test function makes HTTP requests to external APIs, Reproducibility across test runs is required, Offline test execution is needed, testing, http_mocking

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Testing code that makes external API calls
- Need to avoid live API dependencies
- Reduce test latency and flakiness
- Ensure test reproducibility across environments
