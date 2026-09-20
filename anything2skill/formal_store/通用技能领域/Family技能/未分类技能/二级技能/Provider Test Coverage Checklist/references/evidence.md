# Provider Test Coverage Checklist Evidence

- family: 未分类技能
- skill_id: ed255c75-c359-5a78-b92a-51cd0adcbe51
- support_count: 1

## Evidence 1

- support_id: 5e71fc80-961c-5b1f-9dd9-41546a686441
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 24649:25982
- confidence: 0.80
- quote: We use Jupyter notebooks as integration tests for LLM providers. This approach:
- Tests real-world usage patterns
- Verifies end-to-end functionality
- Ensures examples stay up-to-date
- Tests against actual LLM APIs

1. **Notebook Tests**:
   - Located in `examples/` directory
   - Each LLM provider has example notebooks
   - CI runs notebooks on PR merges to main
   - Tests run against multiple Python versions

2. **Test Workflow**:
   The `test-notebooks.yml` workflow:
   ```yaml
   name: Test Notebooks
   on:
     pull_request:
       paths:
         - "agentops/**"
         - "examples/**"
         - "tests/**"
   ```
   - Runs on PR merges and manual triggers
   - Sets up environment with provider API keys
   - Installs AgentOps from main branch
   - Executes each notebook
   - Excludes specific notebooks that require manual testing

3. **Provider Coverage**:
   Each provider should have notebooks demonstrating:
   - Basic completion calls
   - Streaming responses
   - Async operations (if supported)
   - Error handling
   - Tool usage (if applicable)

4. **Adding Provider Tests**:
   - Create notebook in `examples/provider_name/`
   - Include all provider functionality
   - Add necessary secrets to GitHub Actions
   - Update `exclude_notebooks` in workflow if manual testing needed

## Adding LLM Providers
