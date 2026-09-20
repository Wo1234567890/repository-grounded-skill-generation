# Custom Reward Function Design Evidence

- family: 未分类技能
- skill_id: a600fbef-41ac-5267-a405-97b2503d08a6
- support_count: 2

## Evidence 1

- support_id: 75a1663e-b07e-58d8-bebd-3c70a8e7beb3
- relation_type: support
- document: trl-grpo-017.md
- doc_id: 1b1cfe5e-1be5-5bc1-9b07-6e37f39e1ae1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/trl-grpo-017.md
- section: GRPO Trainer
- span: 2527:4917
- confidence: 0.80
- quote: Overview
TRL supports the GRPO Trainer for training language models, as described in the paper DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models by Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Mingchuan Zhang, Y. K. Li, Y. Wu, Daya Guo.

The abstract from the paper is the following:

Mathematical reasoning poses a significant challenge for language models due to its complex and structured nature. In this paper, we introduce DeepSeekMath 7B, which continues pre-training DeepSeek-Coder-Base-v1.5 7B with 120B math-related tokens sourced from Common Crawl, together with natural language and code data. DeepSeekMath 7B has achieved an impressive score of 51.7% on the competition-level MATH benchmark without relying on external toolkits and voting techniques, approaching the performance level of Gemini-Ultra and GPT-4. Self-consistency over 64 samples from DeepSeekMath 7B achieves 60.9% on MATH. The mathematical reasoning capability of DeepSeekMath is attributed to two key factors: First, we harness the significant potential of publicly available web data through a meticulously engineered data selection pipeline. Second, we introduce Group Relative Policy Optimization (GRPO), a variant of Proximal Policy Optimization (PPO), that enhances mathematical reasoning abilities while concurrently optimizing the memory usage of PPO.

This post-training method was contributed by Quentin Gallouédec.

Quick start
This example demonstrates how to train a model using the GRPO method. We train a Qwen 0.5B Instruct model with the prompts from the TLDR dataset (completion column is ignored!). You can view the data in the dataset here:

Below is the script to train the model.

Copied

```

train_grpo.py
from datasets import load_dataset
from trl import GRPOConfig, GRPOTrainer

dataset = load_dataset("trl-lib/tldr", split="train")

# Define the reward function, which rewards completions that are close to 20 characters
def reward_len(completions, **kwargs):
    return [-abs(20 - len(completion)) for completion in completions]

training_args = GRPOConfig(output_dir="Qwen2-0.5B-GRPO", logging_steps=10)
trainer = GRPOTrainer(
    model="Qwen/Qwen2-0.5B-Instruct",
    reward_funcs=reward_len,
    args=training_args,
    train_dataset=dataset,
)
trainer.train()
```

Execute the script using the following command:

Copied

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
