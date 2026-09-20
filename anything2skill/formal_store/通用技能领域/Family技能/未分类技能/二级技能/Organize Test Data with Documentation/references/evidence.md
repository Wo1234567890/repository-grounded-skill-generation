# Organize Test Data with Documentation Evidence

- family: 未分类技能
- skill_id: 96533ad8-b5f6-5dc1-8164-65943fa56047
- support_count: 1

## Evidence 1

- support_id: c03d0eb9-d152-5f6a-a207-438a628e94c0
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
