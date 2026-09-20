# Mock Filesystem Operations Evidence

- family: 未分类技能
- skill_id: 08414f30-e515-5bed-86e6-2b78fc22c07b
- support_count: 1

## Evidence 1

- support_id: e2a3cbb8-67ec-5c2d-b4af-8146841d615c
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 23038:23891
- confidence: 0.87
- quote: @pytest.mark.depends(on=['test_prerequisite'])  # Declare test dependencies
   def test_dependent_function():
       # Test implementation
   ```

2. **Recording HTTP Interactions**:
   ```python
   @pytest.mark.vcr()  # Records HTTP interactions
   def test_api_call():
       response = client.make_request()
       assert response.status_code == 200
   ```

3. **Mocking Filesystem**:
   ```python
   def test_file_operations(fs):  # fs fixture provided by pyfakefs
       fs.create_file('/fake/file.txt', contents='test')
       assert os.path.exists('/fake/file.txt')
   ```

4. **Mocking HTTP Requests**:
   ```python
   def test_http_client(requests_mock):
       requests_mock.get('http://api.example.com', json={'key': 'value'})
       response = make_request()
       assert response.json()['key'] == 'value'
   ```

### Testing Best Practices
