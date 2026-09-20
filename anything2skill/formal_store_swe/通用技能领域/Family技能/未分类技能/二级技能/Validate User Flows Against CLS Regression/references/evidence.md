# Validate User Flows Against CLS Regression Evidence

- family: 未分类技能
- skill_id: 41c6a6ea-b987-52fa-80ec-8b0d93030270
- support_count: 2

## Evidence 1

- support_id: 3e502dce-4188-5f47-abe1-dfcfe1291b68
- relation_type: support
- document: cls-guidance.md
- doc_id: 0551d67e-cae4-5d1f-804a-e4046e4b8739
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/cls-guidance.md
- section: Understand the causes of layout shifts
- span: 12737:14335
- confidence: 0.82
- quote: The live metrics view of the Performance Panel allows monitoring of a web page's CLS score while interacting with the page.

As an alternative to using the DevTools, you can browse your web page while recording layout shifts using a Performance Observer pasted into the console.

For more information, see Debug layout shifts.

After you've identified any common causes of CLS, the timespans user flow mode of Lighthouse can also be used to ensure typical user flows don't regress by introducing layout shifts.

The `web-vitals` library has attribution functions that let you collect this additional information. For more information, see Debug performance in the field. Other RUM providers have also started collecting and presenting this data similarly.

## Evidence 2

- support_id: b1f6205f-15fd-5529-89e9-ef5a975da0b8
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 22522:22788
- confidence: 0.85
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
