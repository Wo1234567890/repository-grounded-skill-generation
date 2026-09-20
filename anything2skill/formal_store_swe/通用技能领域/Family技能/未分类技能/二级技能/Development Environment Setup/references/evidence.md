# Development Environment Setup Evidence

- family: 未分类技能
- skill_id: e90c2a8f-194e-5fb1-99e3-7a99328214fe
- support_count: 1

## Evidence 1

- support_id: b1b974bb-6ba0-5557-ad1b-59cf3c92e0cc
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 20698:21455
- confidence: 0.85
- quote: ## Development Environment

1. **Environment Variables**:
   Create a `.env` file:
   ```
   AGENTOPS_API_KEY=your_api_key
   OPENAI_API_KEY=your_openai_key  # For testing
   ANTHROPIC_API_KEY=your_anthropic_key  # For testing
   # Other keys...
   ```

2. **Virtual Environment**:
   We recommend using `poetry` or `venv`:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Unix
   .\venv\Scripts\activate   # Windows
   ```

3. **Pre-commit Setup**:
   We use pre-commit hooks to automatically format and lint code. Set them up with:
   ```bash
   pip install pre-commit
   pre-commit install
   ```

That's it! The hooks will run automatically when you commit. To manually check all files:
   ```bash
   pre-commit run --all-files
   ```
