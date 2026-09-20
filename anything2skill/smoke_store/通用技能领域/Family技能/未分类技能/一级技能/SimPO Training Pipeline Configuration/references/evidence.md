# SimPO Training Pipeline Configuration Evidence

- family: 未分类技能
- skill_id: 8d014104-7fc2-512e-b2a3-b3a520e8b034
- support_count: 1

## Evidence 1

- support_id: 98c9ac01-a28d-5833-acd0-f3e331ccd983
- relation_type: support
- document: simpo-repository-docs.md
- doc_id: 1a328841-b24a-5f7c-8bd5-fb7199a95935
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/simpo-repository-docs.md
- section: # Simple Preference Optimization (SimPO)
- span: 635:9650
- confidence: 0.75
- quote: <img src="./SimPO.png" width="1000px"></img>

## Tips for Running SimPO
Given the various inquiries about SimPO, we provide a list of tips to help you reproduce our paper results and achieve better outcomes for running SimPO on your own tasks.

*Notably, if you are training Llama3 and evaluating the trained models on AlpacaEval 2 and Arena-Hard using the templates provided in this repo, please make sure to use the pre-update Llama3 tokenizer (i.e., the one before the PR).*

- Compared to the llama3 models, we found that the gemma models exhibit significantly less catastrophic forgetting on math tasks (e.g., GSM) and MMLU, despite the ultrafeedback dataset having limited math-related data. This demonstrates that the [google/gemma-2-9b-it](https://huggingface.co/google/gemma-2-9b-it) model is more suitable for continued preference optimization.
- SimPO and DPO perform comparably across all benchmarks, but SimPO is inherently simpler and less resource-intensive.
