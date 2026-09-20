---
id: "08414f30-e515-5bed-86e6-2b78fc22c07b"
name: "Mock Filesystem Operations"
description: "Use pyfakefs fixture to create and manipulate a fake filesystem in tests, isolating file I/O operations from the real filesystem without affecting actual disk state."
version: "0.1.0"
tags:
  - "testing"
  - "mocking"
  - "filesystem"
  - "isolation"
  - "pyfakefs"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Tests perform file creation, deletion, or reading; you need fast, safe tests that do not modify actual filesystem."
examples:
  - input: "Test function with fs fixture parameter; code creates and reads a file"
    output: "File created in fake filesystem; read operation returns expected contents; no real disk I/O occurs"
    notes: "def test_file_operations(fs): fs.create_file('/fake/file.txt', contents='test'); assert os.path.exists('/fake/file.txt')"
---

# Mock Filesystem Operations

Use pyfakefs fixture to create and manipulate a fake filesystem in tests, isolating file I/O operations from the real filesystem without affecting actual disk state.

## Prompt

Invoke this skill when your test needs to perform file creation, deletion, or reading operations in isolation. Use the `fs` fixture provided by pyfakefs to create fake files, directories, and verify file operations. All operations occur in memory; no real filesystem is modified.

## Objective

Isolate file system operations in tests without affecting real disk state
## Applicable Signals

- Test performs file creation, deletion, or reading
- Need fast, safe tests that do not modify actual filesystem
- Test requires isolated file I/O without side effects

## Contraindications

- Testing actual filesystem behavior or permissions
- Tests require real disk I/O performance characteristics
- Validating real filesystem state or access control

## Workflow Steps

- {'step': 1, 'action': 'Accept fs fixture parameter in test function', 'detail': 'The pyfakefs library automatically provides the `fs` fixture to your test function'}
- {'step': 2, 'action': 'Create fake files or directories using fs methods', 'detail': 'Use fs.create_file() or fs.create_dir() to set up test file structure'}
- {'step': 3, 'action': 'Execute file operations under test', 'detail': 'Call the code being tested; it will interact with the fake filesystem'}
- {'step': 4, 'action': 'Assert file state using standard os or pathlib calls', 'detail': 'Verify file existence, contents, or structure using os.path.exists(), open(), etc.'}

## Constraints

- pyfakefs must be installed and pytest must be configured to recognize it
- All file paths in the test operate within the fake filesystem scope
- Real filesystem is not accessible during test execution

## Cautions

- Ensure test cleanup is automatic; pyfakefs resets after each test
- Do not mix real and fake filesystem operations in the same test

## Output Contract

- Fake filesystem created and isolated; file operations succeed in isolated environment; no changes to real filesystem; test assertions pass or fail based on fake filesystem state only.

## Example Executions

### Example 1

- Input: Test function with fs fixture parameter; code creates and reads a file
- Output: File created in fake filesystem; read operation returns expected contents; no real disk I/O occurs
- Notes: def test_file_operations(fs): fs.create_file('/fake/file.txt', contents='test'); assert os.path.exists('/fake/file.txt')

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Tests perform file creation, deletion, or reading; you need fast, safe tests that do not modify actual filesystem.

## Examples

### Example 1

Input:

  Test function with fs fixture parameter; code creates and reads a file

Output:

  File created in fake filesystem; read operation returns expected contents; no real disk I/O occurs

Notes:

  def test_file_operations(fs): fs.create_file('/fake/file.txt', contents='test'); assert os.path.exists('/fake/file.txt')
