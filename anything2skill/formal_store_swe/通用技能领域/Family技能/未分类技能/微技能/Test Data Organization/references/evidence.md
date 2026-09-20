# Test Data Organization Evidence

- family: 未分类技能
- skill_id: 14a36ff7-af63-5da9-8793-3d2ab71ce793
- support_count: 1

## Evidence 1

- support_id: d023e9dc-172d-5762-ae88-893578b7e088
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 23865:24647
- confidence: 0.80
- quote: ### Testing Best Practices

1. **Test Categories**:
   - Unit tests: Test individual components
   - Integration tests: Test component interactions
   - End-to-end tests: Test complete workflows
   - Performance tests: Test response times and resource usage

2. **Fixtures**:
   Create reusable test fixtures in `conftest.py`:
   ```python
   @pytest.fixture
   def mock_llm_client():
       client = Mock()
       client.chat.completions.create.return_value = Mock()
       return client
   ```

3. **Test Data**:
   - Store test data in `tests/data/`
   - Use meaningful test data names
   - Document data format and purpose

4. **VCR Cassettes**:
   - Store in `tests/cassettes/`
   - Sanitize sensitive information
   - Update cassettes when API changes

### CI Testing Strategy
