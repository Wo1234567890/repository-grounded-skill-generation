---
id: "157d80cf-9e39-5360-93dc-64c3a207c855"
name: "SimPO Model Training Launch"
description: "Execute distributed training of SimPO preference-optimized language models using Accelerate and DeepSpeed, with model-specific configuration files and GPU resource allocation."
version: "0.1.0"
tags:
  - "model_training"
  - "distributed_training"
  - "accelerate"
  - "deepspeed"
  - "language_model"
  - "preference_optimization"
triggers:
  - "Starting a new SimPO training job for Mistral-Base, Mistral-Instruct, Llama3-Base, Llama3-Instruct, or Llama3-Instruct-v0.2 models; GPU cluster is available and configured"
examples:
  - input: "Model variant: Mistral-Base; GPU cluster: 4xH100; config files present"
    output: "Accelerate launch initiated; training loop begins; loss metrics logged to console"
    notes: "Command: ACCELERATE_LOG_LEVEL=info accelerate launch --config_file accelerate_configs/deepspeed_zero3.yaml scripts/run_simpo.py training_configs/mistral-7b-base-simpo.yaml"
  - input: "Model variant: Llama3-Instruct-v0.2; GPU cluster: 4xH100; config files present"
    output: "Accelerate launch initiated; training loop begins; loss metrics logged to console"
    notes: "Command: ACCELERATE_LOG_LEVEL=info accelerate launch --config_file accelerate_configs/deepspeed_zero3.yaml scripts/run_simpo.py training_configs/llama-3-8b-instruct-simpo-v2.yaml"
---

# SimPO Model Training Launch

Execute distributed training of SimPO preference-optimized language models using Accelerate and DeepSpeed, with model-specific configuration files and GPU resource allocation.

## Prompt

To launch a SimPO training job:
1. Verify GPU cluster availability (4xH100 or equivalent).
2. Adjust num_processes and per_device_train_batch_size in the training config if your environment differs from 4xH100.
3. Select the appropriate training config file for your model variant (Mistral-Base, Mistral-Instruct, Llama3-Base, Llama3-Instruct, or Llama3-Instruct-v0.2).
4. Execute the accelerate launch command with the corresponding config file and training script.
5. Monitor stdout for loss metrics and checkpoint creation.

## Objective

Launch and execute a complete SimPO training run for a specified model variant
## Applicable Signals

- Starting a new SimPO training job
- GPU cluster is available and configured
- Model variant is one of: Mistral-Base, Mistral-Instruct, Llama3-Base, Llama3-Instruct, Llama3-Instruct-v0.2
- Training config files are present and valid

## Contraindications

- Inference or evaluation only
- No GPU resources available
- Training config files are missing or corrupted
- Accelerate or DeepSpeed not installed

## Workflow Steps

- {'step': 1, 'action': 'Verify environment', 'detail': 'Confirm GPU availability, Accelerate installation, and DeepSpeed configuration'}
- {'step': 2, 'action': 'Select model variant', 'detail': 'Choose one of: Mistral-Base, Mistral-Instruct, Llama3-Base, Llama3-Instruct, Llama3-Instruct-v0.2'}
- {'step': 3, 'action': 'Adjust hyperparameters if needed', 'detail': 'Modify num_processes and per_device_train_batch_size in training config based on your compute environment'}
- {'step': 4, 'action': 'Execute accelerate launch command', 'detail': 'Run accelerate launch with --config_file pointing to deepspeed_zero3.yaml, scripts/run_simpo.py, and the model-specific training config'}
- {'step': 5, 'action': 'Monitor training', 'detail': 'Observe stdout for loss metrics and checkpoint creation; verify ACCELERATE_LOG_LEVEL=info output'}

## Constraints

- Requires 4xH100 GPUs or equivalent compute resources (adjustable via num_processes and per_device_train_batch_size)
- Requires accelerate_configs/deepspeed_zero3.yaml configuration file
- Requires model-specific training config file from training_configs/ directory
- Requires scripts/run_simpo.py training script

## Cautions

- Hyperparameter settings are tuned for 4xH100; adjust batch size and num_processes for different hardware
- Training may consume significant GPU memory; monitor resource usage
- Ensure checkpoint directory has sufficient disk space

## Output Contract

- Training process launched successfully with Accelerate; checkpoint directory created and loss metrics begin logging to stdout; distributed training orchestration is active across specified GPU processes

## Example Executions

### Example 1

- Input: Model variant: Mistral-Base; GPU cluster: 4xH100; config files present
- Output: Accelerate launch initiated; training loop begins; loss metrics logged to console
- Notes: Command: ACCELERATE_LOG_LEVEL=info accelerate launch --config_file accelerate_configs/deepspeed_zero3.yaml scripts/run_simpo.py training_configs/mistral-7b-base-simpo.yaml

### Example 2

- Input: Model variant: Llama3-Instruct-v0.2; GPU cluster: 4xH100; config files present
- Output: Accelerate launch initiated; training loop begins; loss metrics logged to console
- Notes: Command: ACCELERATE_LOG_LEVEL=info accelerate launch --config_file accelerate_configs/deepspeed_zero3.yaml scripts/run_simpo.py training_configs/llama-3-8b-instruct-simpo-v2.yaml

## Triggers

- Starting a new SimPO training job for Mistral-Base, Mistral-Instruct, Llama3-Base, Llama3-Instruct, or Llama3-Instruct-v0.2 models; GPU cluster is available and configured

## Examples

### Example 1

Input:

  Model variant: Mistral-Base; GPU cluster: 4xH100; config files present

Output:

  Accelerate launch initiated; training loop begins; loss metrics logged to console

Notes:

  Command: ACCELERATE_LOG_LEVEL=info accelerate launch --config_file accelerate_configs/deepspeed_zero3.yaml scripts/run_simpo.py training_configs/mistral-7b-base-simpo.yaml

### Example 2

Input:

  Model variant: Llama3-Instruct-v0.2; GPU cluster: 4xH100; config files present

Output:

  Accelerate launch initiated; training loop begins; loss metrics logged to console

Notes:

  Command: ACCELERATE_LOG_LEVEL=info accelerate launch --config_file accelerate_configs/deepspeed_zero3.yaml scripts/run_simpo.py training_configs/llama-3-8b-instruct-simpo-v2.yaml
