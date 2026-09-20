---
id: "843818d8-b862-5b46-a9e7-e6a2400b0f87"
name: "Jupyter Notebook to MDX Documentation Conversion"
description: "Automated workflow to convert Jupyter notebooks into MDX documentation files, handling frontmatter, GitHub links, code formatting, and installation sections. Orchestrates notebook transformation from examples/ directory into publishable docs/v2/examples/ MDX files."
version: "0.1.0"
tags:
  - "documentation"
  - "notebook_conversion"
  - "mdx"
  - "automation"
  - "content_generation"
  - "jupyter"
  - "markdown"
  - "content_conversion"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "New example Jupyter notebook added to examples/ directory"
  - "Existing notebook requires documentation update"
  - "Batch documentation generation requested"
  - "Need to publish Jupyter notebook examples as website documentation"
  - "Batch processing multiple notebooks for a documentation site"
  - "Converting technical examples to static site generator format"
---

# Jupyter Notebook to MDX Documentation Conversion

Automated workflow to convert Jupyter notebooks into MDX documentation files, handling frontmatter, GitHub links, code formatting, and installation sections. Orchestrates notebook transformation from examples/ directory into publishable docs/v2/examples/ MDX files.

## Prompt

Execute the notebook-to-MDX conversion pipeline: (1) Load Jupyter notebook from examples/ directory; (2) Extract and format frontmatter; (3) Convert notebook cells to MDX content; (4) Transform %pip install commands to CodeGroup format; (5) Generate GitHub links to source notebook; (6) Write output MDX file to docs/v2/examples/. Ensure all installation sections are properly formatted and all cross-references are valid.

## Objective

convert_notebook_to_documentation
## Applicable Signals

- Notebook file present in examples/ with .ipynb extension
- Documentation target directory docs/v2/examples/ exists and is writable
- Notebook contains standard AgentOps example structure
- Notebook file exists and is valid
- Target documentation site uses MDX format
- Source notebooks are in examples/ directory structure

## Contraindications

- Source is not a valid Jupyter notebook (.ipynb)
- Target format requirement is not MDX
- Documentation structure deviates from standard AgentOps layout
- Notebook lacks required metadata or example structure
- Notebook contains sensitive credentials or proprietary code
- Documentation target is not a static site generator (non-MDX-based)
- Notebook has unresolved dependencies or broken cells

## Intervention Moves

- Parse notebook metadata and extract title, description, and tags
- Convert notebook cells to MDX-compatible markdown
- Reformat pip install commands from %pip syntax to CodeGroup blocks
- Inject GitHub repository links to source notebook
- Validate frontmatter structure and completeness

## Workflow Steps

- {'step': 1, 'action': 'Load notebook', 'detail': 'Read .ipynb file from examples/ directory and parse JSON structure'}
- {'step': 2, 'action': 'Extract frontmatter', 'detail': 'Extract title, description, author, date, and tags from notebook metadata'}
- {'step': 3, 'action': 'Convert cells to MDX', 'detail': 'Transform markdown cells and code cells into MDX-compatible format'}
- {'step': 4, 'action': 'Format installation commands', 'detail': 'Convert %pip install commands to CodeGroup format for proper rendering'}
- {'step': 5, 'action': 'Generate GitHub links', 'detail': 'Create links to source notebook in repository'}
- {'step': 6, 'action': 'Write MDX output', 'detail': 'Write converted content to docs/v2/examples/ with proper file naming'}
- {'step': 1, 'action': 'Extract notebook content', 'detail': 'Read Jupyter notebook file and extract code cells, markdown cells, and outputs'}
- {'step': 2, 'action': 'Convert to Markdown', 'detail': 'Transform notebook structure into Markdown format with proper syntax'}
- {'step': 3, 'action': 'Add frontmatter and metadata', 'detail': 'Prepend YAML frontmatter with title, description, and metadata fields'}
- {'step': 4, 'action': 'Transform installation commands', 'detail': 'Convert pip/conda commands into user-friendly installation instructions'}
- {'step': 5, 'action': 'Generate GitHub source links', 'detail': 'Create links to original notebook in source repository'}
- {'step': 6, 'action': 'Output MDX file', 'detail': 'Write final MDX file to docs/v2/examples/ directory'}

## Constraints

- Input notebook must be valid JSON-serializable .ipynb format
- Output directory docs/v2/examples/ must exist and be writable
- Frontmatter must conform to MDX documentation standards
- GitHub links must point to correct repository branch and file path
- Notebook must be in valid Jupyter format (.ipynb)
- GitHub repository context must be available for source link generation

## Cautions

- Verify notebook execution state before conversion; stale outputs may be included
- Check for relative imports or local file references that may not resolve in documentation context
- Validate CodeGroup formatting for pip install commands to ensure proper syntax highlighting

## Output Contract

- MDX file written to docs/v2/examples/ with: (1) valid frontmatter block; (2) converted notebook content; (3) properly formatted CodeGroup installation sections; (4) valid GitHub source links; (5) all code blocks syntax-highlighted; (6) file ready for documentation build pipeline.
- MDX files written to docs/v2/examples/ directory with correct frontmatter, converted Markdown content, and working GitHub source links. Each output file is ready for static site generation.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- New example Jupyter notebook added to examples/ directory
- Existing notebook requires documentation update
- Batch documentation generation requested
- Need to publish Jupyter notebook examples as website documentation
- Batch processing multiple notebooks for a documentation site
- Converting technical examples to static site generator format
