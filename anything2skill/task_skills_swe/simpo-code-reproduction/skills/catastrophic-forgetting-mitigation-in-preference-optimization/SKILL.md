---
id: "78dbc066-a6f1-52e1-987d-2b0215b284ff"
name: "Catastrophic Forgetting Mitigation in Preference Optimization"
description: "Select Gemma-2-9b-it over Llama3 models when training preference optimization on datasets with limited math or knowledge coverage to minimize performance degradation on specialized benchmarks (GSM, MMLU)."
version: "0.1.0"
tags:
  - "model_selection"
  - "catastrophic_forgetting"
  - "preference_optimization"
  - "math_preservation"
  - "knowledge_retention"
  - "gemma"
triggers:
  - "Training preference optimization on datasets with limited math or knowledge task coverage"
  - "Need to preserve performance on GSM, MMLU, or similar specialized benchmarks"
  - "Evaluating model selection for continued preference optimization"
examples:
  - input: "Training SimPO on ultrafeedback dataset (limited math examples) with Llama3-8b baseline"
    output: "Switch to Gemma-2-9b-it; train with same SimPO hyperparameters; evaluate on GSM8K and MMLU"
    notes: "Gemma-2-9b-it exhibits significantly less performance drop on math tasks post-training"
  - input: "Preference optimization task requires MMLU score preservation above 70%"
    output: "Select Gemma-2-9b-it as base model; validate MMLU retention after preference training"
    notes: "Gemma models show better MMLU retention despite sparse math coverage in preference data"
---

# Catastrophic Forgetting Mitigation in Preference Optimization

Select Gemma-2-9b-it over Llama3 models when training preference optimization on datasets with limited math or knowledge coverage to minimize performance degradation on specialized benchmarks (GSM, MMLU).

## Prompt

When training preference optimization models on datasets with limited math or knowledge coverage, choose Gemma-2-9b-it instead of Llama3 to reduce catastrophic forgetting on GSM and MMLU benchmarks. Gemma models demonstrate significantly better retention of math and knowledge performance despite ultrafeedback dataset limitations.

## Objective

Reduce performance degradation on math and knowledge tasks when applying preference optimization
## Applicable Signals

- Preference dataset has sparse math-related examples
- Baseline model shows performance drop on math or knowledge tasks post-training
- Target benchmarks include GSM or MMLU evaluation

## Contraindications

- Using Llama3 models without explicit catastrophic forgetting mitigation
- Task does not require math or knowledge task preservation
- Resource constraints prohibit model switching or Gemma-2-9b-it deployment
- Inference latency or model size constraints favor smaller alternatives

## Intervention Moves

- Switch base model from Llama3 to Gemma-2-9b-it
- Validate math and knowledge task retention post-training

## Workflow Steps

- {'step': 1, 'action': 'Assess preference dataset coverage', 'detail': 'Identify math and knowledge task representation in training data; flag if coverage is limited'}
- {'step': 2, 'action': 'Evaluate baseline model options', 'detail': 'Compare Gemma-2-9b-it against Llama3 candidates for your task; prioritize Gemma if math/knowledge preservation is critical'}
- {'step': 3, 'action': 'Configure training with selected model', 'detail': 'Use Gemma-2-9b-it as base model for preference optimization; apply standard hyperparameter tuning'}
- {'step': 4, 'action': 'Validate on math and knowledge benchmarks', 'detail': 'Evaluate trained model on GSM, MMLU, and other specialized tasks; confirm performance retention vs. baseline'}

## Constraints

- Gemma-2-9b-it must be available in training environment
- Preference optimization method (e.g., SimPO, DPO) must be compatible with selected model
- Evaluation must include math and knowledge benchmarks to validate forgetting mitigation

## Cautions

- Gemma-2-9b-it shows better math retention but may have different performance characteristics on other tasks; validate across full benchmark suite
- Catastrophic forgetting mitigation is model-dependent; results may not transfer to other Gemma or Llama variants

## Output Contract

- Trained model with maintained or improved performance on math and knowledge benchmarks (GSM, MMLU) compared to baseline, demonstrating reduced catastrophic forgetting

## Example Executions

### Example 1

- Input: Training SimPO on ultrafeedback dataset (limited math examples) with Llama3-8b baseline
- Output: Switch to Gemma-2-9b-it; train with same SimPO hyperparameters; evaluate on GSM8K and MMLU
- Notes: Gemma-2-9b-it exhibits significantly less performance drop on math tasks post-training

### Example 2

- Input: Preference optimization task requires MMLU score preservation above 70%
- Output: Select Gemma-2-9b-it as base model; validate MMLU retention after preference training
- Notes: Gemma models show better MMLU retention despite sparse math coverage in preference data

## Triggers

- Training preference optimization on datasets with limited math or knowledge task coverage
- Need to preserve performance on GSM, MMLU, or similar specialized benchmarks
- Evaluating model selection for continued preference optimization

## Examples

### Example 1

Input:

  Training SimPO on ultrafeedback dataset (limited math examples) with Llama3-8b baseline

Output:

  Switch to Gemma-2-9b-it; train with same SimPO hyperparameters; evaluate on GSM8K and MMLU

Notes:

  Gemma-2-9b-it exhibits significantly less performance drop on math tasks post-training

### Example 2

Input:

  Preference optimization task requires MMLU score preservation above 70%

Output:

  Select Gemma-2-9b-it as base model; validate MMLU retention after preference training

Notes:

  Gemma models show better MMLU retention despite sparse math coverage in preference data
