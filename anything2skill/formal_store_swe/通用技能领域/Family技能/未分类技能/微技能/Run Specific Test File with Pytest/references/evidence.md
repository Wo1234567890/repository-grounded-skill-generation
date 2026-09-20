# Run Specific Test File with Pytest Evidence

- family: 未分类技能
- skill_id: 607f6958-ca2b-5d5b-b3cc-8477b66d19a4
- support_count: 1

## Evidence 1

- support_id: 6b9fa913-01d5-5195-b17c-282648ed1acf
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 22522:22788
- confidence: 0.90
- quote: ### Running Tests

1. **Run All Tests**:
   ```bash
   tox
   ```

2. **Run Specific Test File**:
   ```bash
   pytest tests/llms/test_anthropic.py -v
   ```

3. **Run with Coverage**:
   ```bash
   coverage run -m pytest
   coverage report
   ```

### Writing Tests
