---
id: "12888375-7271-5bd8-a3ad-cde4deb2c5cf"
name: "Time Format and Parse Operations"
description: "Automates extraction of Jupyter notebook content and conversion to Markdown documentation with frontmatter, metadata, and MDX file generation for website publishing."
version: "0.1.1"
tags:
  - "documentation"
  - "notebook"
  - "markdown"
  - "mdx"
  - "automation"
  - "content_generation"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "Need to format Date objects to strings or parse time strings to Date objects; working with locale-specific or UTC timestamps"
examples:
  - input: "python examples/generate_documentation.py examples/langchain/langchain_examples.ipynb"
    output: "MDX file created at docs/v2/examples/langchain_examples.mdx with extracted content, frontmatter, and GitHub source link"
    notes: "Standard usage pattern for single notebook conversion"
---

# Time Format and Parse Operations

Automates extraction of Jupyter notebook content and conversion to Markdown documentation with frontmatter, metadata, and MDX file generation for website publishing.

## Prompt

Execute the generate_documentation.py script to convert a Jupyter notebook into a publishable MDX file. The script extracts notebook content, converts it to Markdown, adds frontmatter and metadata, transforms installation commands into user-friendly format, generates GitHub links to source notebooks, and outputs MDX files to docs/v2/examples/.

## Objective

Convert notebook examples into publishable documentation
## Applicable Signals

- Jupyter notebook file exists and is accessible
- Target documentation directory (docs/v2/examples/) is writable
- Notebook contains executable code cells and markdown cells suitable for documentation

## Contraindications

- Notebook contains sensitive credentials or proprietary code
- Documentation target is not MDX-based
- Manual formatting is preferred over automated conversion
- Notebook structure is non-standard or heavily customized

## Workflow Steps

- {'step': 1, 'action': 'Invoke generate_documentation.py with notebook file path as argument', 'input': 'Path to Jupyter notebook file'}
- {'step': 2, 'action': 'Extract notebook content including code cells, markdown cells, and outputs', 'input': 'Parsed notebook structure'}
- {'step': 3, 'action': 'Convert notebook content to Markdown format', 'input': 'Extracted notebook cells'}
- {'step': 4, 'action': 'Transform installation commands into user-friendly format', 'input': 'Markdown with installation instructions'}
- {'step': 5, 'action': 'Generate GitHub links for source notebooks', 'input': 'Repository metadata and notebook path'}
- {'step': 6, 'action': 'Add frontmatter and metadata to documentation', 'input': 'Converted Markdown content'}
- {'step': 7, 'action': 'Write MDX file to docs/v2/examples/ directory', 'input': 'Complete MDX content with frontmatter'}

## Constraints

- Input must be a valid Jupyter notebook file (.ipynb)
- Output directory docs/v2/examples/ must exist and be writable
- GitHub repository context must be available for source link generation

## Cautions

- Verify notebook content does not contain sensitive information before conversion
- Ensure GitHub repository context is correctly configured for accurate source link generation
- Review generated MDX files for formatting accuracy, especially for complex code blocks or embedded outputs

## Output Contract

- MDX files generated in docs/v2/examples/ with proper frontmatter, converted Markdown content, and GitHub source links; file naming follows convention derived from notebook name; all code cells and markdown cells successfully converted; installation commands formatted for end-user clarity.

## Example Executions

### Example 1

- Input: python examples/generate_documentation.py examples/langchain/langchain_examples.ipynb
- Output: MDX file created at docs/v2/examples/langchain_examples.mdx with extracted content, frontmatter, and GitHub source link
- Notes: Standard usage pattern for single notebook conversion

## 子技能目录
- [Locale-Specific Time Formatter Creation](通用技能领域/Family技能/未分类技能/微技能/Locale-Specific Time Formatter Creation/SKILL.md) ｜ 适用：Invoke the generate_documentation.py script to automatically create documentation files from example notebooks. Use this micro operation after creating or updating notebooks and before publishing to the website.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `Locale-Specific Time Formatter Creation` 时，优先调用它。 线索：Formatting or parsing multiple timestamps with the same locale, Need to switch between default and custom locales, documentation, automation, notebook_processing

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Need to format Date objects to strings or parse time strings to Date objects; working with locale-specific or UTC timestamps

## Examples

### Example 1

Input:

  python examples/generate_documentation.py examples/langchain/langchain_examples.ipynb

Output:

  MDX file created at docs/v2/examples/langchain_examples.mdx with extracted content, frontmatter, and GitHub source link

Notes:

  Standard usage pattern for single notebook conversion
