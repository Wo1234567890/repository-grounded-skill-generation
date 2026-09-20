---
id: "d20f5fd8-eabf-5fca-a641-c279d63a586f"
name: "Convert Jupyter Notebooks to MDX Documentation"
description: "Automated micro-skill to transform Jupyter notebooks into MDX-formatted documentation files. Handles frontmatter injection, GitHub link resolution, and conversion of pip install commands to CodeGroup format. Designed for batch processing example notebooks into a versioned documentation directory."
version: "0.1.0"
tags:
  - "documentation"
  - "notebook"
  - "mdx"
  - "conversion"
  - "automation"
  - "build"
triggers:
  - "New example notebook added to examples/ directory"
  - "Batch documentation build initiated"
  - "Documentation version update required"
---

# Convert Jupyter Notebooks to MDX Documentation

Automated micro-skill to transform Jupyter notebooks into MDX-formatted documentation files. Handles frontmatter injection, GitHub link resolution, and conversion of pip install commands to CodeGroup format. Designed for batch processing example notebooks into a versioned documentation directory.

## Prompt

Execute the notebook-to-MDX conversion script on the source notebook. Verify that frontmatter is correctly injected, GitHub repository links are resolved, and all %pip install commands are transformed to CodeGroup syntax. Output MDX file to the target documentation directory.

## Objective

Transform notebook source to MDX documentation artifact
## Applicable Signals

- Notebook file present in source directory
- Target documentation directory exists and is writable
- Notebook contains standard Jupyter cell structure

## Contraindications

- Source is already in MDX format
- Notebook contains non-standard or malformed cell structures
- Target documentation directory does not exist or lacks write permissions
- Notebook uses custom magic commands not supported by converter

## Workflow Steps

- {'step': 1, 'action': 'Locate source notebook in examples/ directory', 'validation': 'File exists and is readable'}
- {'step': 2, 'action': 'Parse notebook cells and extract content', 'validation': 'Cell structure is valid; no parsing errors'}
- {'step': 3, 'action': 'Inject frontmatter (metadata, title, description)', 'validation': 'Frontmatter block is well-formed YAML'}
- {'step': 4, 'action': 'Resolve and embed GitHub repository links', 'validation': 'Links are absolute and point to correct repository'}
- {'step': 5, 'action': 'Convert %pip install commands to CodeGroup format', 'validation': 'CodeGroup syntax is valid; all install commands transformed'}
- {'step': 6, 'action': 'Write MDX output to docs/v2/examples/ directory', 'validation': 'File written successfully; no I/O errors'}

## Constraints

- Source notebook must be valid Jupyter format (.ipynb)
- Target directory path must be absolute or relative to script execution context
- Frontmatter template must be available and valid
- GitHub repository URL must be resolvable

## Cautions

- Verify frontmatter metadata is complete before output
- Check that CodeGroup format is compatible with target MDX renderer
- Ensure pip install commands reference correct package versions

## Output Contract

- MDX file written to target directory with: (1) valid frontmatter block at top, (2) all GitHub links resolved and embedded, (3) all %pip install commands converted to CodeGroup format, (4) notebook content preserved in Markdown structure, (5) file encoding UTF-8

## Triggers

- New example notebook added to examples/ directory
- Batch documentation build initiated
- Documentation version update required
