# Custom Reward Function Signature Compliance Evidence

- family: 未分类技能
- skill_id: 0aa5626c-5ed7-50e1-87ed-4d879e19901d
- support_count: 2

## Evidence 1

- support_id: dbcfa06e-3c41-5e17-9eec-16c82d420ae7
- relation_type: support
- document: trl-grpo-017.md
- doc_id: 1b1cfe5e-1be5-5bc1-9b07-6e37f39e1ae1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/trl-grpo-017.md
- section: GRPO Trainer
- span: 18499:18952
- confidence: 0.85
- quote: The function must accept the following as keyword arguments:

- `prompts` (contains the prompts), 
- `completions` (contains the generated completions), 
- All columns names (but `prompt`) that the dataset may have. For example, if the dataset contains a column named `ground_truth`, the function will be called with `ground_truth` as a keyword argument.

The easiest way to comply with this requirement is to use `**kwargs` in the function signature.

## Evidence 2

- support_id: 26815d11-4fdd-59b0-8460-0464dd85640e
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 81765:82282
- confidence: 0.85
- quote: ## More basic functionality

You can instrument functions inside your code with the `@operation` decorator, which will create spans that track function execution, parameters, and return values. These operations will be displayed in your session visualization alongside LLM calls.
  ```python python
  # Instrument a function as an operation
  from agentops.sdk.decorators import operation

@operation
  def process_data(data):
      # Your function logic here
      result = data.upper()
      return result
```
