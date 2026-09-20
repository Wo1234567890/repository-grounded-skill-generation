# Feature Branch Setup Evidence

- family: 未分类技能
- skill_id: 5dcaf70a-1c40-55e6-88e0-927b2eb5e3af
- support_count: 1

## Evidence 1

- support_id: 4498154d-647a-5133-bfe8-0361695a1029
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 20407:20724
- confidence: 0.92
- quote: Before starting work on a new feature:
   ```bash
   git checkout main
   git pull upstream main
   git checkout -b feature/your-feature-name
   ```

2. **Install Dependencies**:
   ```bash
   pip install -e .
   ```

3. **Set Up Pre-commit Hooks**:
   ```bash
   pre-commit install
   ```

## Development Environment
