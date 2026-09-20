---
id: "def55c39-1bed-5c99-b81b-669ca51b7ce6"
name: "HTTP Interaction Recording and Replay with VCR"
description: "Record and replay HTTP interactions in tests using VCR to eliminate external API calls and ensure test reproducibility. Captures request/response pairs on first run and replays them in subsequent runs without making network calls."
version: "0.1.0"
tags:
  - "testing"
  - "http_mocking"
  - "test_isolation"
  - "vcr"
  - "reproducibility"
  - "pytest"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Test function makes HTTP requests to external APIs"
  - "Reproducibility across test runs is required"
  - "Offline test execution is needed"
---

# HTTP Interaction Recording and Replay with VCR

Record and replay HTTP interactions in tests using VCR to eliminate external API calls and ensure test reproducibility. Captures request/response pairs on first run and replays them in subsequent runs without making network calls.

## Prompt

Use @pytest.mark.vcr() decorator on test functions that make HTTP requests. On first execution, VCR records all HTTP interactions to a cassette file. Subsequent test runs replay responses from the cassette, eliminating external API dependencies and ensuring deterministic test behavior.

## Objective

isolate_http_dependencies
## Applicable Signals

- Presence of HTTP client calls (requests, httpx, etc.) in test code
- Need for deterministic test results
- CI/CD environment without external network access

## Contraindications

- Live API testing is mandatory
- HTTP response variability is intentional or required
- Real-time API behavior validation is the test goal

## Workflow Steps

- {'step': 1, 'action': 'Decorate test function with @pytest.mark.vcr()', 'detail': 'Apply decorator to any test that makes HTTP requests'}
- {'step': 2, 'action': 'Run test for the first time', 'detail': 'VCR intercepts HTTP calls and records request/response pairs to a cassette file (typically YAML or JSON)'}
- {'step': 3, 'action': 'Verify cassette file creation', 'detail': 'Confirm cassette file exists in configured cassette library directory'}
- {'step': 4, 'action': 'Run test again', 'detail': 'VCR replays responses from cassette; no network calls are made'}
- {'step': 5, 'action': 'Commit cassette to version control', 'detail': 'Ensure cassette is available for all test runs in CI/CD and local environments'}

## Constraints

- Cassette files must be committed to version control for reproducibility
- Cassette files may contain sensitive data (API keys, tokens); review before committing
- VCR library must be installed and configured in test environment

## Cautions

- First test run will make actual network calls; ensure network access is available during initial cassette recording
- Stale cassettes may mask real API changes; periodically regenerate cassettes to validate against live API
- Cassette matching is sensitive to request parameters; ensure request construction is deterministic

## Output Contract

- HTTP request/response pair recorded in cassette file; subsequent test runs replay from cassette without making network calls. Test assertions pass consistently across runs.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Test function makes HTTP requests to external APIs
- Reproducibility across test runs is required
- Offline test execution is needed
