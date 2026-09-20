---
id: "399dc8a2-8f3b-5eb6-8dc8-042250fabbb6"
name: "Filesystem Mocking"
description: "Create and manipulate fake filesystem objects in tests using pyfakefs to avoid side effects on real disk. Isolates filesystem operations by intercepting file I/O calls and routing them to an in-memory fake filesystem."
version: "0.1.0"
tags:
  - "testing"
  - "isolation"
  - "filesystem"
  - "pyfakefs"
  - "mock"
  - "pytest"
triggers:
  - "test code reads, writes, or checks file existence"
  - "real filesystem side effects must be prevented"
  - "test setup requires temporary file structures"
examples:
  - input: "Test function with fs fixture parameter; code under test calls os.path.exists() and open()"
    output: "Fake filesystem is initialized; os.path.exists() returns True for created fake files; open() reads from fake file contents"
    notes: "pyfakefs automatically patches os and built-in file functions"
  - input: "fs.create_file('/config/app.json', contents='{\"key\": \"value\"}')"
    output: "Fake file created at /config/app.json with specified content; subsequent open('/config/app.json').read() returns the content"
    notes: "Directory structure is created automatically if it does not exist"
---

# Filesystem Mocking

Create and manipulate fake filesystem objects in tests using pyfakefs to avoid side effects on real disk. Isolates filesystem operations by intercepting file I/O calls and routing them to an in-memory fake filesystem.

## Prompt

Use the pyfakefs fixture (fs) to create fake files and directories in your test. Call fs.create_file() or fs.create_dir() to set up test data. All subsequent os.path and file operations in the test will operate against the fake filesystem, not the real disk. After the test completes, the fake filesystem is automatically torn down.

## Objective

isolate_filesystem_operations
## Applicable Signals

- test function uses os.path.exists(), open(), or file I/O calls
- test needs to verify file operations without disk I/O
- test isolation requirement is high

## Contraindications

- actual file I/O to real disk is required
- test validates real disk behavior or persistence
- test depends on actual filesystem permissions or OS-specific behavior

## Workflow Steps

- {'step': 1, 'action': 'Inject fs fixture into test function signature', 'detail': 'def test_function(fs):'}
- {'step': 2, 'action': 'Create fake files or directories using fs.create_file() or fs.create_dir()', 'detail': "fs.create_file('/fake/file.txt', contents='test data')"}
- {'step': 3, 'action': 'Execute code under test that performs file operations', 'detail': 'Call functions that read, write, or check file existence'}
- {'step': 4, 'action': 'Assert on file state or operations', 'detail': "assert os.path.exists('/fake/file.txt')"}

## Constraints

- pyfakefs library must be installed and available
- fs fixture must be injected as a test function parameter
- fake filesystem is scoped to the test function; state does not persist across tests

## Cautions

- Ensure fake file paths match the expected structure for the code under test
- File contents must be explicitly set via fs.create_file(contents=...) if the test reads file data
- Permissions and ownership on fake files may differ from real filesystem; do not rely on permission checks in isolated tests

## Output Contract

- Fake filesystem is created and active for the duration of the test
- All file I/O operations are intercepted and routed to the fake filesystem
- No real files are created or modified on disk
- Test assertions can verify file existence, content, and operations without side effects

## Example Therapist Responses

### Example 1

- Client/Input: Test function with fs fixture parameter; code under test calls os.path.exists() and open()
- Therapist/Output: Fake filesystem is initialized; os.path.exists() returns True for created fake files; open() reads from fake file contents
- Notes: pyfakefs automatically patches os and built-in file functions

### Example 2

- Client/Input: fs.create_file('/config/app.json', contents='{"key": "value"}')
- Therapist/Output: Fake file created at /config/app.json with specified content; subsequent open('/config/app.json').read() returns the content
- Notes: Directory structure is created automatically if it does not exist

## Triggers

- test code reads, writes, or checks file existence
- real filesystem side effects must be prevented
- test setup requires temporary file structures

## Examples

### Example 1

Input:

  Test function with fs fixture parameter; code under test calls os.path.exists() and open()

Output:

  Fake filesystem is initialized; os.path.exists() returns True for created fake files; open() reads from fake file contents

Notes:

  pyfakefs automatically patches os and built-in file functions

### Example 2

Input:

  fs.create_file('/config/app.json', contents='{"key": "value"}')

Output:

  Fake file created at /config/app.json with specified content; subsequent open('/config/app.json').read() returns the content

Notes:

  Directory structure is created automatically if it does not exist
