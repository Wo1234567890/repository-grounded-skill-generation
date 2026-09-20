# Application Performance Monitoring with OpenTelemetry Evidence

- family: 未分类技能
- skill_id: 07935192-6a9c-5de5-a763-07352cabd2fb
- support_count: 2

## Evidence 1

- support_id: 697033ee-fa78-5771-9675-f2d993238471
- relation_type: support
- document: nextjs14-optimization.md
- doc_id: 348ef37d-8f72-5077-a811-da520815fca2
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/nextjs14-optimization.md
- section: Analytics and Monitoring
- span: 2809:4615
- confidence: 0.75
- quote: - [Images](/docs/14/app/building-your-application/optimizing/images)
  - Optimize your images with the built-in `next/image` component.
- [Fonts](/docs/14/app/building-your-application/optimizing/fonts)
  - Optimize your application's web fonts with the built-in `next/font` loaders.
- [Scripts](/docs/14/app/building-your-application/optimizing/scripts)
  - Optimize 3rd party scripts with the built-in Script component.
- [Metadata](/docs/14/app/building-your-application/optimizing/metadata)
  - Use the Metadata API to define metadata in any layout or page.
- [Static Assets](/docs/14/app/building-your-application/optimizing/static-assets)
  - Next.js allows you to serve static files, like images, in the public directory. You can learn how it works here.
- [Bundle Analyzer](/docs/14/app/building-your-application/optimizing/bundle-analyzer)
  - Analyze the size of your JavaScript bundles using the @next/bundle-analyzer plugin.
- [Lazy Loading](/docs/14/app/building-your-application/optimizing/lazy-loading)
  - Lazy load imported libraries and React Components to improve your application's loading performance.
- [Analytics](/docs/14/app/building-your-application/optimizing/analytics)
  - Measure and track page performance using Next.js Speed Insights
- [Instrumentation](/docs/14/app/building-your-application/optimizing/instrumentation)
  - Learn how to use instrumentation to run code at server startup in your Next.js app
- [OpenTelemetry](/docs/14/app/building-your-application/optimizing/open-telemetry)
  - Learn how to instrument your Next.js app with OpenTelemetry.
- [Third Party Libraries](/docs/14/app/building-your-application/optimizing/third-party-libraries)
  - Optimize the performance of third-party libraries in your application with the `@next/third-parties` package.

---

## Evidence 2

- support_id: e2551d61-cd25-569c-b780-ec34a0955177
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 23865:24647
- confidence: 0.78
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
