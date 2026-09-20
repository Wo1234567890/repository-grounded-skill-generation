---
id: "96533ad8-b5f6-5dc1-8164-65943fa56047"
name: "Organize Test Data with Documentation"
description: "Create and maintain a dedicated test data directory structure with meaningful naming conventions and format documentation to ensure test data is discoverable, maintainable, and accessible across test suites."
version: "0.1.0"
tags:
  - "testing"
  - "test_infrastructure"
  - "data_organization"
  - "test_setup"
  - "best_practices"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Preparing test suites that require external data files"
  - "Setting up sample payloads or reference datasets shared across multiple tests"
  - "Establishing test data structure for a new test module or integration test suite"
---

# Organize Test Data with Documentation

Create and maintain a dedicated test data directory structure with meaningful naming conventions and format documentation to ensure test data is discoverable, maintainable, and accessible across test suites.

## Prompt

Store test data files in tests/data/ directory. Use meaningful, descriptive names for each test data file. Document the format and purpose of each dataset in a README or inline comments. Ensure file paths are relative and standardized so test functions can reliably locate and load data.

## Objective

Maintain organized, documented test data for reproducible testing
## Applicable Signals

- Multiple tests need access to the same reference data
- Test data is too large or complex to embed inline
- Test suite requires reproducible, versioned datasets

## Contraindications

- Test data is generated dynamically at runtime
- Data is embedded inline within test code
- Data sensitivity or size makes file storage impractical
- Test requires real-time or streaming data that cannot be pre-stored

## Workflow Steps

- Create or verify tests/data/ directory exists
- Name test data files with clear, descriptive identifiers (e.g., sample_llm_response.json, mock_user_payload.yaml)
- Document the format (JSON, CSV, YAML, etc.) and purpose of each file
- Ensure test functions reference data via standardized relative paths
- Verify all test data is accessible and correctly formatted before test execution

## Constraints

- All test data must be stored under tests/data/ directory
- File names must be descriptive and follow a consistent naming convention
- Format and purpose of each dataset must be documented
- Paths must be relative and platform-independent

## Cautions

- Sanitize sensitive information (API keys, credentials, PII) from test data files before committing
- Keep test data files small enough to avoid repository bloat; use fixtures or mocking for large datasets
- Update documentation when data format or structure changes

## Output Contract

- Test data files are stored in tests/data/ with clear naming, documented format, and accessible to test functions via standard relative paths. Test suite can reliably load and use data without modification.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Preparing test suites that require external data files
- Setting up sample payloads or reference datasets shared across multiple tests
- Establishing test data structure for a new test module or integration test suite
