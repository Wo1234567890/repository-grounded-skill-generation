# HTTP Request Mocking Evidence

- family: 未分类技能
- skill_id: b230ef59-f428-5b7a-9efb-61313f845c3f
- support_count: 1

## Evidence 1

- support_id: 4384aed2-62d6-5139-9e47-976587d42f2e
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 23038:23891
- confidence: 0.86
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
