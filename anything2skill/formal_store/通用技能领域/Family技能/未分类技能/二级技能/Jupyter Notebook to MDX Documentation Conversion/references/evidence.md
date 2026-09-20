# Jupyter Notebook to MDX Documentation Conversion Evidence

- family: 未分类技能
- skill_id: 843818d8-b862-5b46-a9e7-e6a2400b0f87
- support_count: 2

## Evidence 1

- support_id: f2be2c32-ebad-5c87-8b36-1db9d79fe785
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 147416:147820
- confidence: 0.75
- quote: ### Utility Scripts

- **[`generate_documentation.py`](https://github.com/AgentOps-AI/agentops/blob/main/generate_documentation.py)** - Script to convert Jupyter notebooks to MDX documentation files
  - Converts notebooks from `examples/` to `docs/v2/examples/`
  - Handles frontmatter, GitHub links, and installation sections
  - Transforms `%pip install` commands to CodeGroup format

##  Prerequisites

## Evidence 2

- support_id: f54067a4-a514-5c16-bbb6-85155bbcad94
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 148042:148536
- confidence: 0.75
- quote: The `generate_documentation.py` script automatically converts these Jupyter notebook examples into documentation for the AgentOps website. It:

- Extracts notebook content and converts to Markdown
- Adds proper frontmatter and metadata
- Transforms installation commands into user-friendly format
- Generates GitHub links for source notebooks
- Creates MDX files in `docs/v2/examples/`

### Usage
```bash
python examples/generate_documentation.py examples/langchain/langchain_examples.ipynb
```
