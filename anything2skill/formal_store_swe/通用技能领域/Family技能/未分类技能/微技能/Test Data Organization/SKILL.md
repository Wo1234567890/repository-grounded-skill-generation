---
id: "14a36ff7-af63-5da9-8793-3d2ab71ce793"
name: "Test Data Organization"
description: "Organize and maintain test data assets in a standardized directory structure with clear naming conventions and format documentation. This micro-skill ensures test data is discoverable, reusable, and well-documented for reproducible test execution across multiple test suites."
version: "0.1.0"
tags:
  - "testing"
  - "test_data"
  - "data_management"
  - "test_preparation"
  - "best_practice"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Preparing test suites that require external data files, sample payloads, or reference datasets"
  - "When multiple tests share common data and need centralized access"
---

# Test Data Organization

Organize and maintain test data assets in a standardized directory structure with clear naming conventions and format documentation. This micro-skill ensures test data is discoverable, reusable, and well-documented for reproducible test execution across multiple test suites.

## Prompt

1. Create a tests/data/ directory at the project root.
2. Store all test data files (sample payloads, reference datasets, fixtures) in this directory.
3. Use meaningful, descriptive file names that indicate content type and purpose (e.g., sample_llm_response.json, mock_user_payload.yaml).
4. Create a README or inline documentation describing each data file's format, schema, and intended use case.
5. Organize subdirectories by data type or test category if the volume grows (e.g., tests/data/payloads/, tests/data/responses/).
6. Verify that all test files can locate and load data from this centralized location.

## Objective

Organize and maintain test data assets in a standardized, discoverable, and reusable structure
## Applicable Signals

- Test suite requires external data files or sample payloads
- Multiple tests share common reference datasets
- Test data is scattered across multiple locations
- New test data needs to be added to the project

## Contraindications

- Do not store sensitive credentials, API keys, or authentication tokens in test data files; use environment variables or secure vaults instead
- Do not commit unencrypted personally identifiable information (PII) or production secrets to the repository

## Workflow Steps

- {'step': 1, 'action': 'Create tests/data/ directory structure', 'detail': 'Establish the root directory for all test data assets'}
- {'step': 2, 'action': 'Name test data files descriptively', 'detail': 'Use clear, purpose-driven names (e.g., sample_llm_response.json, mock_user_payload.yaml)'}
- {'step': 3, 'action': 'Document data format and purpose', 'detail': 'Create README or inline comments describing schema, content type, and intended test use case'}
- {'step': 4, 'action': 'Organize by category if needed', 'detail': 'Create subdirectories (e.g., payloads/, responses/) as data volume grows'}
- {'step': 5, 'action': 'Verify test data accessibility', 'detail': 'Confirm all test files can locate and load data from the centralized location'}

## Constraints

- Test data directory must be at tests/data/ or a documented alternative location
- All data files must have meaningful, self-documenting names
- Format and purpose of each data file must be documented

## Cautions

- Ensure test data does not contain real credentials or sensitive information
- Keep test data files small and focused to avoid test suite bloat
- Update documentation when data schema or format changes

## Output Contract

- A well-organized tests/data/ directory with meaningfully named files and accompanying documentation describing data format and purpose. All test data is discoverable, reusable, and accessible to test suites.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Preparing test suites that require external data files, sample payloads, or reference datasets
- When multiple tests share common data and need centralized access
