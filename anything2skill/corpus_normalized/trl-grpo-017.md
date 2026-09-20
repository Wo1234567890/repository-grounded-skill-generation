GRPO Trainer · Hugging Face


  

 


 


 Hugging Face 

   

-  Models 
-  Datasets 
-  Spaces 
-  Buckets new
-  Docs 
-  Enterprise  
- Pricing 
- 


- 
Website 

-  Tasks 
-  HuggingChat 
-  Collections 
-  Languages 
-  Organizations  
- 
Community 

-  Blog 
-  Posts 
-  Daily Papers 
-  Hardware 
-  Learn 
-  Discord 
-  Forum 
-  GitHub  
- 
Solutions 

-  Team & Enterprise 
-  Hugging Face PRO 
-  Enterprise Support 
-  Inference Providers 
-  Inference Endpoints 
-  Storage Buckets   
-  
- Log In 
- Sign Up    


 


TRL documentation


GRPO Trainer


# TRL
  🏡 View all docsAWS Trainium & InferentiaAccelerateArgillaAutoTrainBitsandbytesCLIChat UIDataset viewerDatasetsDeploying on AWSDiffusersDistilabelEvaluateGoogle CloudGoogle TPUsGradioHubHub Python LibraryHuggingface.jsInference Endpoints (dedicated)Inference ProvidersKernelsLeRobotLeaderboardsLightevalMicrosoft AzureOpenEnvOptimumPEFTReachy MiniSafetensorsSentence TransformersTRLTasksText Embeddings InferenceText Generation InferenceTokenizersTrackioTransformersTransformers.jsXetsmolagentstimm  
Search documentation  
mainv1.13.0v1.12.0v1.11.0v1.10.0v1.9.2v1.8.0v1.7.1v1.6.0v1.5.1v1.4.0v1.3.0v1.2.0v1.1.0v1.0.0v0.29.1v0.28.0v0.27.2v0.26.2v0.25.1v0.24.0v0.23.1v0.22.2v0.21.0v0.20.0v0.19.1v0.18.1v0.17.0v0.16.1v0.15.2v0.14.0v0.13.0v0.12.2v0.11.4v0.10.1v0.9.6v0.8.6v0.7.11v0.6.0v0.5.0v0.4.7v0.3.1v0.2.1v0.1.1 EN 

    

Getting started  
TRLInstallationQuickstart

Conceptual Guides  
Dataset FormatsTraining FAQUnderstanding Logs

How-to guides  
Command Line Interface (CLI)Customizing the TrainingReducing Memory UsageSpeeding Up TrainingDistributing TrainingUsing Trained Models

Integrations  
DeepSpeedLiger KernelPEFTUnslothvLLM

Examples  
Example OverviewCommunity TutorialsSentiment TuningTraining StackLlamaDetoxifying a Language ModelLearning to Use ToolsMulti Adapter RLHFFine-tuning a Multimodal Model Using SFT (Single or Multi-Image Dataset)

API  


Trainers  
AlignPropBCOCPODDPODPOOnline DPOGKDGRPOKTONash-MDORPOPPOPRMRewardRLOOSFTIterative SFTXPOModel ClassesBest of N SamplingJudgesCallbacksData UtilitiesText EnvironmentsScript UtilitiesOthers 


You are viewing v0.17.0 version. A newer version v1.13.0 is available. 


Join the Hugging Face community 

and get access to the augmented documentation experience


Collaborate on models, datasets and Spaces 


Faster examples with accelerated inference 


Switch between documentation themes 
Sign Up 

to get started

 

 

 

 

 

 

 

 


#  GRPO Trainer


##  Overview


TRL supports the GRPO Trainer for training language models, as described in the paper DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models by Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Mingchuan Zhang, Y. K. Li, Y. Wu, Daya Guo.


The abstract from the paper is the following:


Mathematical reasoning poses a significant challenge for language models due to its complex and structured nature. In this paper, we introduce DeepSeekMath 7B, which continues pre-training DeepSeek-Coder-Base-v1.5 7B with 120B math-related tokens sourced from Common Crawl, together with natural language and code data. DeepSeekMath 7B has achieved an impressive score of 51.7% on the competition-level MATH benchmark without relying on external toolkits and voting techniques, approaching the performance level of Gemini-Ultra and GPT-4. Self-consistency over 64 samples from DeepSeekMath 7B achieves 60.9% on MATH. The mathematical reasoning capability of DeepSeekMath is attributed to two key factors: First, we harness the significant potential of publicly available web data through a meticulously engineered data selection pipeline. Second, we introduce Group Relative Policy Optimization (GRPO), a variant of Proximal Policy Optimization (PPO), that enhances mathematical reasoning abilities while concurrently optimizing the memory usage of PPO.


This post-training method was contributed by Quentin Gallouédec.


##  Quick start


This example demonstrates how to train a model using the GRPO method. We train a Qwen 0.5B Instruct model with the prompts from the TLDR dataset (completion column is ignored!). You can view the data in the dataset here:


Below is the script to train the model.


 Copied 

```
# train_grpo.py
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

```
accelerate launch train_grpo.py
```


Distributed across 8 GPUs, the training takes approximately 1 day.


##  Looking deeper into the GRPO method


GRPO is an online learning algorithm, meaning it improves iteratively by using the data generated by the trained model itself during training. The intuition behind GRPO objective is to maximize the advantage of the generated completions, while ensuring that the model remains close to the reference policy. To understand how GRPO works, it can be broken down into four main steps: Generating completions, computing the advantage, estimating the KL divergence, and computing the loss.


###  Generating completions


At each training step, we sample a batch of prompts and generate a set of G G G completions for each prompt (denoted as oi o_i oi​).


###  Computing the advantage


For each of the G G G sequences, we compute the reward using a reward model. To align with the comparative nature of reward models—typically trained on datasets of comparisons between outputs for the same question—the advantage is calculated to reflect these relative comparisons. It is normalized as follows:
A^i,t=ri−mean(r)std(r)\hat{A}_{i,t} = \frac{r_i - \text{mean}(\mathbf{r})}{\text{std}(\mathbf{r})}A^i,t​=std(r)ri​−mean(r)​


This approach gives the method its name: Group Relative Policy Optimization (GRPO).


It was shown in the paper Understanding R1-Zero-Like Training: A Critical Perspective that scaling by std(r) \text{std}(\mathbf{r}) std(r) may cause a question-level difficulty bias. You can disable this scaling by setting `scale_rewards=False` in GRPOConfig.


###  Estimating the KL divergence


KL divergence is estimated using the approximator introduced by Schulman et al. (2020). The approximator is defined as follows:
DKL[πθ∥πref]=πref(oi,t∣q,oi,<t)πθ(oi,t∣q,oi,<t)−log⁡πref(oi,t∣q,oi,<t)πθ(oi,t∣q,oi,<t)−1,\mathbb{D}_{\text{KL}}\left[\pi_\theta \|\pi_{\text{ref}}\right] = \frac{\pi_{\text{ref}}(o_{i,t} \mid q, o_{i,<t})}{\pi_\theta(o_{i,t} \mid q, o_{i,<t})} - \log \frac{\pi_{\text{ref}}(o_{i,t} \mid q, o_{i,<t})}{\pi_\theta(o_{i,t} \mid q, o_{i,<t})} - 1,
DKL​[πθ​∥πref​]=πθ​(oi,t​∣q,oi,<t​)πref​(oi,t​∣q,oi,<t​)​−logπθ​(oi,t​∣q,oi,<t​)πref​(oi,t​∣q,oi,<t​)​−1,


###  Computing the loss


The objective is to maximize the advantage while ensuring that the model remains close to the reference policy. Consequently, the loss is defined as follows:
LGRPO(θ)=−1∑i=1G∣oi∣∑i=1G∑t=1∣oi∣[πθ(oi,t∣q,oi,<t)[πθ(oi,t∣q,oi,<t)]no gradA^i,t−βDKL[πθ∥πref]],
\mathcal{L}_{\text{GRPO}}(\theta) = -\frac{1}{\sum_{i=1}^G |o_i|} \sum_{i=1}^G \sum_{t=1}^{|o_i|} \left[ \frac{\pi_\theta(o_{i,t} \mid q, o_{i,< t})}{\left[\pi_\theta(o_{i,t} \mid q, o_{i,< t})\right]_{\text{no grad}}} \hat{A}_{i,t} - \beta \mathbb{D}_{\text{KL}}\left[\pi_\theta \| \pi_{\text{ref}}\right] \right],
LGRPO​(θ)=−∑i=1G​∣oi​∣1​i=1∑G​t=1∑∣oi​∣​[[πθ​(oi,t​∣q,oi,<t​)]no grad​πθ​(oi,t​∣q,oi,<t​)​A^i,t​−βDKL​[πθ​∥πref​]],


where the first term represents the scaled advantage and the second term penalizes deviations from the reference policy through KL divergence.


Note that compared to the original formulation in DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models, we don’t scale by 1∣oi∣ \frac{1}{|o_i|} ∣oi​∣1​ because it was shown in the paper Understanding R1-Zero-Like Training: A Critical Perspective that this introduces a response-level length bias. More details in loss types.


In the original paper, this formulation is generalized to account for multiple updates after each generation (denoted μ \mu μ, can be set with `num_iterations` in GRPOConfig) by leveraging the clipped surrogate objective:
LGRPO(θ)=−1∑i=1G∣oi∣∑i=1G∑t=1∣oi∣[min⁡(πθ(oi,t∣q,oi,<t)πθold(oi,t∣q,oi,<t)A^i,t, clip(πθ(oi,t∣q,oi,<t)πθold(oi,t∣q,oi,<t),1−ϵ,1+ϵ)A^i,t)−βDKL[πθ∥πref]],
\mathcal{L}_{\text{GRPO}}(\theta) = - \frac{1}{\sum_{i=1}^G |o_i|} \sum_{i=1}^G \sum_{t=1}^{|o_i|} \left[ \min \left( \frac{\pi_\theta(o_{i,t} \mid q, o_{i,< t})}{\pi_{\theta_{\text{old}}}(o_{i,t} \mid q, o_{i,< t})} \hat{A}_{i,t}, \, \text{clip}\left( \frac{\pi_\theta(o_{i,t} \mid q, o_{i,< t})}{\pi_{\theta_{\text{old}}}(o_{i,t} \mid q, o_{i,< t})}, 1 - \epsilon, 1 + \epsilon \right) \hat{A}_{i,t} \right) - \beta \mathbb{D}_{\text{KL}}\left[\pi_\theta \| \pi_{\text{ref}}\right] \right],
LGRPO​(θ)=−∑i=1G​∣oi​∣1​i=1∑G​t=1∑∣oi​∣​[min(πθold​​(oi,t​∣q,oi,<t​)πθ​(oi,t​∣q,oi,<t​)​A^i,t​,clip(πθold​​(oi,t​∣q,oi,<t​)πθ​(oi,t​∣q,oi,<t​)​,1−ϵ,1+ϵ)A^i,t​)−βDKL​[πθ​∥πref​]],


where clip(⋅,1−ϵ,1+ϵ)\text{clip}(\cdot, 1 - \epsilon, 1 + \epsilon) clip(⋅,1−ϵ,1+ϵ) ensures that updates do not deviate excessively from the reference policy by bounding the policy ratio between 1−ϵ 1 - \epsilon 1−ϵ and 1+ϵ 1 + \epsilon 1+ϵ.
When μ=1 \mu = 1 μ=1 (default in TRL), the clipped surrogate objective simplifies to the original objective.


####  Loss Types


Several formulations of the objective have been proposed in the literature. Initially, the objective of GRPO was defined as follows:
LGRPO(θ)=−1G∑i=1G1∣oi∣∑t=1∣oi∣li,t,
\mathcal{L}_{\text{GRPO}}(\theta) = - \frac{1}{G} \sum_{i=1}^G \frac{1}{|o_i|} \sum_{t=1}^{|o_i|} l_{i,t},
LGRPO​(θ)=−G1​i=1∑G​∣oi​∣1​t=1∑∣oi​∣​li,t​,


where
li,t=πθ(oi,t∣q,oi,<t)[πθ(oi,t∣q,oi,<t)]no gradA^i,t−βDKL[πθ∥πref].
l_{i,t} = \frac{\pi_\theta(o_{i,t} \mid q, o_{i,< t})}{\left[\pi_\theta(o_{i,t} \mid q, o_{i,< t})\right]_{\text{no grad}}} \hat{A}_{i,t} - \beta \mathbb{D}_{\text{KL}}\left[\pi_\theta \| \pi_{\text{ref}}\right].
li,t​=[πθ​(oi,t​∣q,oi,<t​)]no grad​πθ​(oi,t​∣q,oi,<t​)​A^i,t​−βDKL​[πθ​∥πref​].


The DAPO paper highlights the limitations of the GRPO algorithm’s sample-level loss in long-CoT scenarios, where longer responses are under-penalized, leading to poorer quality outputs. The proposed solution is a token-level normalization, which better handles longer sequences by assigning more balanced rewards to individual tokens, regardless of response length:
LDAPO(θ)=−1∑i=1G∣oi∣∑i=1G∑t=1∣oi∣li,t,
\mathcal{L}_{\text{DAPO}}(\theta) = - \frac{1}{\sum_{i=1}^G |o_i|} \sum_{i=1}^G \sum_{t=1}^{|o_i|} l_{i,t},
LDAPO​(θ)=−∑i=1G​∣oi​∣1​i=1∑G​t=1∑∣oi​∣​li,t​,


Furthermore, it was demonstrated in the paper Understanding R1-Zero-Like Training: A Critical Perspective that the initial GRPO formulation introduces a response length bias. They show that while the DAPO formulation reduces this bias, it does not eliminate it completely. To fully remove this bias, they propose dividing by a constant instead of the sequence length, resulting in the following formulation:
LDr. GRPO(θ)=−1LG∑i=1G∑t=1∣oi∣li,t,
\mathcal{L}_{\text{Dr. GRPO}}(\theta) = - \frac{1}{LG} \sum_{i=1}^G \sum_{t=1}^{|o_i|} l_{i,t},
LDr. GRPO​(θ)=−LG1​i=1∑G​t=1∑∣oi​∣​li,t​,


This constant is recommended to be the maximum completion length. To use this formulation, set `loss_type="dr_grpo"` in the GRPOConfig.


##  Logged metrics


- `num_tokens`: The total number of tokens processed so far, including both prompts and completions. 
- `completions/mean_length`: The average length of generated completions. 
- `completions/min_length`: The minimun length of generated completions. 
- `completions/max_length`: The maximum length of generated completions. 
- `completions/mean_terminated_length`: The average length of generated completions that terminate with EOS. 
- `completions/min_terminated_length`: The minimun length of generated completions that terminate with EOS. 
- `completions/max_terminated_length`: The maximum length of generated completions that terminate with EOS. 
- `completions/clipped_ratio` : The ratio of truncated (clipped) completions. 
- `reward/{reward_func_name}/mean`: The average reward from a specific reward function. 
- `reward/{reward_func_name}/std`: The standard deviation of the reward from a specific reward function. 
- `reward`: The overall average reward after applying reward weights. 
- `reward_std`: The standard deviation of the overall reward within each batch after applying reward weights. 
- `kl`: The average KL divergence between the model and the reference model, calculated over generated completions. Logged only if `beta` is nonzero. 
- `clip_ratio/region_mean`: The ratio of token probabilities where the GRPO objective is clipped to stay within the trust region:clip(ri,t(θ),1−ϵlow,1+ϵhigh) ,ri,t(θ)=πθ(oi,t∣q,oi,<t)πθold(oi,t∣q,oi,<t) .
\text{clip}\left( r_{i,t}(\theta), 1 - \epsilon_\mathrm{low}, 1 + \epsilon_\mathrm{high} \right)\,, \qquad r_{i,t}(\theta) = \frac{\pi_\theta(o_{i,t} \mid q, o_{i,< t})}{\pi_{\theta_{\text{old}}}(o_{i,t} \mid q, o_{i,< t})}\,.
clip(ri,t​(θ),1−ϵlow​,1+ϵhigh​),ri,t​(θ)=πθold​​(oi,t​∣q,oi,<t​)πθ​(oi,t​∣q,oi,<t​)​.
A higher value means more tokens are clipped, which constrains how much the policy $\pi_\theta$ can change. 
- `clip_ratio/low_mean`: The average ratio of token probabilities that were clipped on the lower bound of the trust region: ri,t(θ)<1−ϵlowr_{i,t}(\theta) < 1 - \epsilon_\mathrm{low}ri,t​(θ)<1−ϵlow​ 
- `clip_ratio/low_min`: The minimum ratio of token probabilities that were clipped on the lower bound of the trust region: ri,t(θ)<1−ϵlowr_{i,t}(\theta) < 1 - \epsilon_\mathrm{low}ri,t​(θ)<1−ϵlow​ 
- `clip_ratio/high_mean`: The average ratio of token probabilities that were clipped on the upper bound of the trust region: ri,t(θ)>1+ϵhighr_{i,t}(\theta) > 1 + \epsilon_\mathrm{high}ri,t​(θ)>1+ϵhigh​ 
- `clip_ratio/high_max`: The maximum ratio of token probabilities that were clipped on the upper bound of the trust region: ri,t(θ)>1+ϵhighr_{i,t}(\theta) > 1 + \epsilon_\mathrm{high}ri,t​(θ)>1+ϵhigh​. 

##  Customization


###  Speed up training with vLLM-powered generation


Generation is often the main bottleneck that makes training slow with online methods. To accelerate generation, you can use vLLM, a library that enables fast generation. To enable it, first install the package with


 Copied 

```
pip install trl[vllm]
```


Then, start the vLLM server with the desired model:


 Copied 

```
trl vllm-serve --model <model_name>
```


Then, pass `use_vllm=True` in the training arguments and run the training script:


 Copied 

```
from trl import GRPOConfig

training_args = GRPOConfig(..., use_vllm=True)
```


For more information, see Speeding up training with vLLM.


###  GRPO at scale: train a 70B+ Model on multiple nodes


When training large models like Qwen2.5-72B, you need several key optimizations to make the training efficient and scalable across multiple GPUs and nodes. These include:


- DeepSpeed ZeRO Stage 3: ZeRO leverages data parallelism to distribute model states (weights, gradients, optimizer states) across multiple GPUs and CPUs, reducing memory and compute requirements on each device. Since large models cannot fit on a single GPU, using ZeRO Stage 3 is required for training such model. For more details, see DeepSpeed Integration. 
- Accelerate: Accelerate is a library that simplifies distributed training across multiple GPUs and nodes. It provides a simple API to launch distributed training and handles the complexities of distributed training, such as data parallelism, gradient accumulation, and distributed data loading. For more details, see Distributing Training. 
- vLLM: See the previous section on how to use vLLM to speed up generation. 

Below is an example SLURM script to train a 70B model with GRPO on multiple nodes. This script trains a model on 4 nodes and uses the 5th node for vLLM-powered generation.


 Copied 

```
#!/bin/bash
#SBATCH --nodes=5
#SBATCH --gres=gpu:8

# Get the list of allocated nodes
NODELIST=($(scontrol show hostnames $SLURM_JOB_NODELIST))

# Assign the first 4 nodes for training and the 5th node for vLLM
TRAIN_NODES="${NODELIST[@]:0:4}"  # Nodes 0, 1, 2, 3 for training
VLLM_NODE="${NODELIST[4]}"  # Node 4 for vLLM

# Run training on the first 4 nodes (Group 1)
srun --nodes=4 --ntasks=4 --nodelist="${NODELIST[@]:0:4}" accelerate launch \
     --config_file examples/accelerate_configs/deepspeed_zero3.yaml \
     --num_processes 32 \
     --num_machines 4 \
     --main_process_ip ${NODELIST[0]} \
     --machine_rank $SLURM_PROCID \
     --rdzv_backend c10d \
     train_grpo.py \
     --server_ip $VLLM_NODE &

# Run vLLM server on the 5th node (Group 2)
srun --nodes=1 --ntasks=1 --nodelist="${NODELIST[4]}" trl vllm-serve --model Qwen/Qwen2.5-72B --tensor_parallel_size 8 &

wait
```


 Copied 

```
import argparse

from datasets import load_dataset
from trl import GRPOTrainer, GRPOConfig

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--vllm_server_host", type=str, default="", help="The server IP")
    args = parser.parse_args()

    # Example dataset from TLDR
    dataset = load_dataset("trl-lib/tldr", split="train")

    # Dummy reward function: count the number of unique characters in the completions
    def reward_num_unique_chars(completions, **kwargs):
        return [len(set(c)) for c in completions]

    training_args = GRPOConfig(
        output_dir="Qwen2.5-72B-GRPO",
        per_device_train_batch_size=4,
        bf16=True,
        gradient_checkpointing=True,
        logging_steps=10,
        use_vllm=True,
        vllm_server_host=args.vllm_server_host.replace("ip-", "").replace("-", "."),  # from ip-X-X-X-X to X.X.X.X
    )

    trainer = GRPOTrainer(model="Qwen/Qwen2.5-72B", args=training_args, reward_funcs=reward_num_unique_chars, train_dataset=dataset)
    trainer.train()

if __name__=="__main__":
    main()
```


###  Using a custom reward function


The GRPOTrainer supports using custom reward functions instead of dense reward models. To ensure compatibility, your reward function must satisfy the following requirements:


- 

Input arguments:


- 

The function must accept the following as keyword arguments:


- `prompts` (contains the prompts), 
- `completions` (contains the generated completions), 
- All columns names (but `prompt`) that the dataset may have. For example, if the dataset contains a column named `ground_truth`, the function will be called with `ground_truth` as a keyword argument. 

The easiest way to comply with this requirement is to use `**kwargs` in the function signature.

- 

Depending on the dataset format, the input will vary:


- For standard format, `prompts` and `completions` will be lists of strings. 
- For conversational format, `prompts` and `completions` will be lists of message dictionaries. 
- 

Return value: The function must return a list of floats. Each float represents the reward corresponding to a single completion.


####  Example 1: Reward longer completions


Below is an example of a reward function for a standard format that rewards longer completions:


 Copied 

```
def reward_func(completions, **kwargs):
    """Reward function that gives higher scores to longer completions."""
    return [float(len(completion)) for completion in completions]
```


You can test it as follows:


 Copied 

```
>>> prompts = ["The sky is", "The sun is"]
>>> completions = [" blue.", " in the sky."]
>>> print(reward_func(prompts=prompts, completions=completions))
[6.0, 12.0]
```


####  Example 2: Reward completions with specific format


Below is an example of a reward function that checks if the completion has a specific format. This example is inspired by the format reward function used in the paper DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning.
It is designed for conversational format, where prompts and completions consist of structured messages.


 Copied 

```
import re

def format_reward_func(completions, **kwargs):
    """Reward function that checks if the completion has a specific format."""
    pattern = r"^<think>.*?</think><answer>.*?</answer>$"
    completion_contents = [completion[0]["content"] for completion in completions]
    matches = [re.match(pattern, content) for content in completion_contents]
    return [1.0 if match else 0.0 for match in matches]
```


You can test this function as follows:


 Copied 

```
>>> prompts = [
...     [{"role": "assistant", "content": "What is the result of (1 + 2) * 4?"}],
...     [{"role": "assistant", "content": "What is the result of (3 + 1) * 2?"}],
... ]
>>> completions = [
...     [{"role": "assistant", "content": "<think>The sum of 1 and 2 is 3, which we multiply by 4 to get 12.</think><answer>(1 + 2) * 4 = 12</answer>"}],
...     [{"role": "assistant", "content": "The sum of 3 and 1 is 4, which we multiply by 2 to get 8. So (3 + 1) * 2 = 8."}],
... ]
>>> format_reward_func(prompts=prompts, completions=completions)
[1.0, 0.0]
```


####  Example 3: Reward completions based on a reference


Below is an example of a reward function that checks if the completion is correct. This example is inspired by the accuracy reward function used in the paper DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning.
This example is designed for standard format, where the dataset contains a column named `ground_truth`.


 Copied 

```
import re

def reward_func(completions, ground_truth, **kwargs):
    # Regular expression to capture content inside \boxed{}
    matches = [re.search(r"\\boxed\{(.*?)\}", completion) for completion in completions]
    contents = [match.group(1) if match else "" for match in matches]
    # Reward 1 if the content is the same as the ground truth, 0 otherwise
    return [1.0 if c == gt else 0.0 for c, gt in zip(contents, ground_truth)]
```


You can test this function as follows:


 Copied 

```
>>> prompts = ["Problem: Solve the equation $2x + 3 = 7$. Solution:", "Problem: Solve the equation $3x - 5 = 10$."]
>>> completions = [r" The solution is \boxed{2}.", r" The solution is \boxed{6}."]
>>> ground_truth = ["2", "5"]
>>> reward_func(prompts=prompts, completions=completions, ground_truth=ground_truth)
[1.0, 0.0]
```


####  Example 4: Multi-task reward functions


Below is an example of using multiple reward functions in the GRPOTrainer. In this example, we define two task-specific reward functions: `math_reward_func` and `coding_reward_func`. The `math_reward_func` rewards math problems based on their correctness, while the `coding_reward_func` rewards coding problems based on whether the solution works.


 Copied 

```
from datasets import Dataset
from trl import GRPOTrainer

# Define a dataset that contains both math and coding problems
dataset = Dataset.from_list(
    [
        {"prompt": "What is 2+2?", "task": "math"},
        {"prompt": "Write a function that returns the sum of two numbers.", "task": "code"},
        {"prompt": "What is 3*4?", "task": "math"},
        {"prompt": "Write a function that returns the product of two numbers.", "task": "code"},
    ]
)

# Math-specific reward function
def math_reward_func(prompts, completions, task, **kwargs):
    rewards = []
    for prompt, completion, t in zip(prompts, completions, task):
        if t == "math":
            # Calculate math-specific reward
            correct = check_math_solution(prompt, completion)
            reward = 1.0 if correct else -1.0
            rewards.append(reward)
        else:
            # Return None for non-math tasks
            rewards.append(None)
    return rewards

# Coding-specific reward function
def coding_reward_func(prompts, completions, task, **kwargs):
    rewards = []
    for prompt, completion, t in zip(prompts, completions, task):
        if t == "coding":
            # Calculate coding-specific reward
            works = test_code_solution(prompt, completion)
            reward = 1.0 if works else -1.0
            rewards.append(reward)
        else:
            # Return None for non-coding tasks
            rewards.append(None)
    return rewards

# Use both task-specific reward functions
trainer = GRPOTrainer(
    model="Qwen/Qwen2-0.5B-Instruct",
    reward_funcs=[math_reward_func, coding_reward_func],
    train_dataset=dataset,
)

trainer.train()
```


In this example, the `math_reward_func` and `coding_reward_func` are designed to work with a mixed dataset that contains both math and coding problems. The `task` column in the dataset is used to determine which reward function to apply to each problem. If there is no relevant reward function for a sample in the dataset, the reward function will return `None` and the GRPOTrainer will continue with the valid functions and tasks. This allows the GRPOTrainer to handle multiple reward functions with different applicability.


Note that the GRPOTrainer will ignore the `None` rewards returned by the reward functions and only consider the rewards returned by the relevant functions. This ensures that the model is trained on the relevant tasks and ignores the tasks for which there is no relevant reward function.


####  Passing the reward function to the trainer


To use your custom reward function, pass it to the GRPOTrainer as follows:


 Copied 

```
from trl import GRPOTrainer

trainer = GRPOTrainer(
    reward_funcs=reward_func,
    ...,
)
```


If you have multiple reward functions, you can pass them as a list:


 Copied 

```
from trl import GRPOTrainer

trainer = GRPOTrainer(
    reward_funcs=[reward_func1, reward_func2],
    ...,
)
```


and the reward will be computed as the sum of the rewards from each function, or the weighted sum if `reward_weights` is provided in the config.


Note that GRPOTrainer supports multiple reward functions of different types. See the parameters documentation for more details.


##  GRPOTrainer

 


### class trl.GRPOTrainer
  < source > 

( model: typing.Union[str, transformers.modeling_utils.PreTrainedModel] reward_funcs: typing.Union[str, transformers.modeling_utils.PreTrainedModel, typing.Callable[[list, list], list[float]], list[typing.Union[str, transformers.modeling_utils.PreTrainedModel, typing.Callable[[list, list], list[float]]]]] args: typing.Optional[trl.trainer.grpo_config.GRPOConfig] = None train_dataset: typing.Union[datasets.arrow_dataset.Dataset, datasets.iterable_dataset.IterableDataset, NoneType] = None eval_dataset: typing.Union[datasets.arrow_dataset.Dataset, datasets.iterable_dataset.IterableDataset, dict[str, typing.Union[datasets.arrow_dataset.Dataset, datasets.iterable_dataset.IterableDataset]], NoneType] = None processing_class: typing.Optional[transformers.tokenization_utils_base.PreTrainedTokenizerBase] = None reward_processing_classes: typing.Union[transformers.tokenization_utils_base.PreTrainedTokenizerBase, list[transformers.tokenization_utils_base.PreTrainedTokenizerBase], NoneType] = None callbacks: typing.Optional[list[transformers.trainer_callback.TrainerCallback]] = None optimizers: tuple = (None, None) peft_config: typing.Optional[ForwardRef('PeftConfig')] = None  ) 

 

Parameters 


-  model (`Union[str, PreTrainedModel]`) —
Model to be trained. Can be either:


- A string, being the model id of a pretrained model hosted inside a model repo on huggingface.co, or
a path to a directory containing model weights saved using
save_pretrained, e.g., `'./my_model_directory/'`. The model is
loaded using from_pretrained with the keywork arguments
in `args.model_init_kwargs`.

- A PreTrainedModel object. Only causal language models are supported.

-  reward_funcs (`Union[RewardFunc, list[RewardFunc]]`) —
Reward functions to be used for computing the rewards. To compute the rewards, we call all the reward
functions with the prompts and completions and sum the rewards. Can be either:


- A single reward function, such as:


- A string: The model ID of a pretrained model hosted inside a model repo on huggingface.co, or a
path to a directory containing model weights saved using
save_pretrained, e.g., `'./my_model_directory/'`. The model is loaded
using from_pretrained with `num_labels=1` and the
keyword arguments in `args.model_init_kwargs`.

- A PreTrainedModel object: Only sequence classification models are supported.

- A custom reward function: The function is provided with the prompts and the generated completions,
plus any additional columns in the dataset. It should return a list of rewards. Custom reward
functions can also return None when the reward is not applicable to those samples. This is useful for
multi-task training where different reward functions apply to different types of samples. When a
reward function returns None for a sample, that reward function is excluded from the reward
calculation for that sample. For more details, see
Using a custom reward function.


- A list of reward functions, where each item can independently be any of the above types. Mixing different
types within the list (e.g., a string model ID and a custom reward function) is allowed.

-  args (GRPOConfig, optional, defaults to `None`) —
Configuration for this trainer. If `None`, a default configuration is used.  
-  train_dataset (Dataset or IterableDataset) —
Dataset to use for training. It must include a column `"prompt"`. Any additional columns in the dataset is
ignored. The format of the samples can be either:


- Standard: Each sample contains plain text.

- Conversational: Each sample contains structured messages (e.g., role
and content).

-  eval_dataset (Dataset, IterableDataset or `dict[str, Union[Dataset, IterableDataset]]`) —
Dataset to use for evaluation. It must meet the same requirements as `train_dataset`.  
-  processing_class (PreTrainedTokenizerBase, optional, defaults to `None`) —
Processing class used to process the data. The padding side must be set to “left”. If `None`, the
processing class is loaded from the model’s name with from_pretrained. A
padding token, `processing_class.pad_token`, must be set. If the processing class has not set a padding
token, `processing_class.eos_token` will be used as the default.  
-  reward_processing_classes (`Union[PreTrainedTokenizerBase, list[PreTrainedTokenizerBase]]`, optional, defaults to `None`) —
Processing classes corresponding to the reward functions specified in `reward_funcs`. Can be either:


- A single processing class: Used when `reward_funcs` contains only one reward function.

- A list of processing classes: Must match the order and length of the reward functions in `reward_funcs`.
If set to `None`, or if an element of the list corresponding to a PreTrainedModel is
`None`, the tokenizer for the model is automatically loaded using from_pretrained.
For elements in `reward_funcs` that are custom reward functions (not PreTrainedModel),
the corresponding entries in `reward_processing_classes` are ignored.

-  callbacks (list of TrainerCallback, optional, defaults to `None`) —
List of callbacks to customize the training loop. Will add those to the list of default callbacks
detailed in here.


If you want to remove one of the default callbacks used, use the remove_callback
method.  
-  optimizers (`tuple[torch.optim.Optimizer, torch.optim.lr_scheduler.LambdaLR]`, optional, defaults to `(None, None)`) —
A tuple containing the optimizer and the scheduler to use. Will default to an instance of `AdamW` on your
model and a scheduler given by `get_linear_schedule_with_warmup` controlled by `args`.  
-  peft_config (`~peft.PeftConfig`, optional, defaults to `None`) —
PEFT configuration used to wrap the model. If `None`, the model is not wrapped.    

Trainer for the Group Relative Policy Optimization (GRPO) method. This algorithm was initially proposed in the
paper DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models.

 

Example:


 Copied 

```
from datasets import load_dataset
from trl import GRPOTrainer

dataset = load_dataset("trl-lib/tldr", split="train")

def reward_func(completions, **kwargs):
    # Dummy reward function that rewards completions with more unique letters.
    return [float(len(set(completion))) for completion in completions]

trainer = GRPOTrainer(
    model="Qwen/Qwen2-0.5B-Instruct",
    reward_funcs=reward_func,
    train_dataset=dataset,
)

trainer.train()
```

 


#### create_model_card
  < source > 

( model_name: typing.Optional[str] = None dataset_name: typing.Optional[str] = None tags: typing.Union[str, list[str], NoneType] = None  ) 

 

Parameters 


-  model_name (`str` or `None`, optional, defaults to `None`) —
Name of the model.  
-  dataset_name (`str` or `None`, optional, defaults to `None`) —
Name of the dataset used for training.  
-  tags (`str`, `list[str]` or `None`, optional, defaults to `None`) —
Tags to be associated with the model card.    

Creates a draft of a model card using the information available to the `Trainer`.


##  GRPOConfig

 


### class trl.GRPOConfig
  < source > 

( output_dir: typing.Optional[str] = None overwrite_output_dir: bool = False do_train: bool = False do_eval: bool = False do_predict: bool = False eval_strategy: typing.Union[transformers.trainer_utils.IntervalStrategy, str] = 'no' prediction_loss_only: bool = False per_device_train_batch_size: int = 8 per_device_eval_batch_size: int = 8 per_gpu_train_batch_size: typing.Optional[int] = None per_gpu_eval_batch_size: typing.Optional[int] = None gradient_accumulation_steps: int = 1 eval_accumulation_steps: typing.Optional[int] = None eval_delay: typing.Optional[float] = 0 torch_empty_cache_steps: typing.Optional[int] = None learning_rate: float = 1e-06 weight_decay: float = 0.0 adam_beta1: float = 0.9 adam_beta2: float = 0.999 adam_epsilon: float = 1e-08 max_grad_norm: float = 1.0 num_train_epochs: float = 3.0 max_steps: int = -1 lr_scheduler_type: typing.Union[transformers.trainer_utils.SchedulerType, str] = 'linear' lr_scheduler_kwargs: typing.Union[dict, str, NoneType] = <factory> warmup_ratio: float = 0.0 warmup_steps: int = 0 log_level: typing.Optional[str] = 'passive' log_level_replica: typing.Optional[str] = 'warning' log_on_each_node: bool = True logging_dir: typing.Optional[str] = None logging_strategy: typing.Union[transformers.trainer_utils.IntervalStrategy, str] = 'steps' logging_first_step: bool = False logging_steps: float = 500 logging_nan_inf_filter: bool = True save_strategy: typing.Union[transformers.trainer_utils.SaveStrategy, str] = 'steps' save_steps: float = 500 save_total_limit: typing.Optional[int] = None save_safetensors: typing.Optional[bool] = True save_on_each_node: bool = False save_only_model: bool = False restore_callback_states_from_checkpoint: bool = False no_cuda: bool = False use_cpu: bool = False use_mps_device: bool = False seed: int = 42 data_seed: typing.Optional[int] = None jit_mode_eval: bool = False use_ipex: bool = False bf16: bool = False fp16: bool = False fp16_opt_level: str = 'O1' half_precision_backend: str = 'auto' bf16_full_eval: bool = False fp16_full_eval: bool = False tf32: typing.Optional[bool] = None local_rank: int = -1 ddp_backend: typing.Optional[str] = None tpu_num_cores: typing.Optional[int] = None tpu_metrics_debug: bool = False debug: typing.Union[str, list[transformers.debug_utils.DebugOption]] = '' dataloader_drop_last: bool = False eval_steps: typing.Optional[float] = None dataloader_num_workers: int = 0 dataloader_prefetch_factor: typing.Optional[int] = None past_index: int = -1 run_name: typing.Optional[str] = None disable_tqdm: typing.Optional[bool] = None remove_unused_columns: typing.Optional[bool] = False label_names: typing.Optional[list[str]] = None load_best_model_at_end: typing.Optional[bool] = False metric_for_best_model: typing.Optional[str] = None greater_is_better: typing.Optional[bool] = None ignore_data_skip: bool = False fsdp: typing.Union[list[transformers.trainer_utils.FSDPOption], str, NoneType] = '' fsdp_min_num_params: int = 0 fsdp_config: typing.Union[dict, str, NoneType] = None fsdp_transformer_layer_cls_to_wrap: typing.Optional[str] = None accelerator_config: typing.Union[dict, str, NoneType] = None deepspeed: typing.Union[dict, str, NoneType] = None label_smoothing_factor: float = 0.0 optim: typing.Union[transformers.training_args.OptimizerNames, str] = 'adamw_torch' optim_args: typing.Optional[str] = None adafactor: bool = False group_by_length: bool = False length_column_name: typing.Optional[str] = 'length' report_to: typing.Union[NoneType, str, list[str]] = None ddp_find_unused_parameters: typing.Optional[bool] = None ddp_bucket_cap_mb: typing.Optional[int] = None ddp_broadcast_buffers: typing.Optional[bool] = None dataloader_pin_memory: bool = True dataloader_persistent_workers: bool = False skip_memory_metrics: bool = True use_legacy_prediction_loop: bool = False push_to_hub: bool = False resume_from_checkpoint: typing.Optional[str] = None hub_model_id: typing.Optional[str] = None hub_strategy: typing.Union[transformers.trainer_utils.HubStrategy, str] = 'every_save' hub_token: typing.Optional[str] = None hub_private_repo: typing.Optional[bool] = None hub_always_push: bool = False gradient_checkpointing: bool = False gradient_checkpointing_kwargs: typing.Union[dict, str, NoneType] = None include_inputs_for_metrics: bool = False include_for_metrics: list = <factory> eval_do_concat_batches: bool = True fp16_backend: str = 'auto' push_to_hub_model_id: typing.Optional[str] = None push_to_hub_organization: typing.Optional[str] = None push_to_hub_token: typing.Optional[str] = None mp_parameters: str = '' auto_find_batch_size: bool = False full_determinism: bool = False torchdynamo: typing.Optional[str] = None ray_scope: typing.Optional[str] = 'last' ddp_timeout: typing.Optional[int] = 1800 torch_compile: bool = False torch_compile_backend: typing.Optional[str] = None torch_compile_mode: typing.Optional[str] = None include_tokens_per_second: typing.Optional[bool] = False include_num_input_tokens_seen: typing.Optional[bool] = False neftune_noise_alpha: typing.Optional[float] = None optim_target_modules: typing.Union[NoneType, str, list[str]] = None batch_eval_metrics: bool = False eval_on_start: bool = False use_liger_kernel: typing.Optional[bool] = False eval_use_gather_object: typing.Optional[bool] = False average_tokens_across_devices: typing.Optional[bool] = False model_init_kwargs: typing.Union[dict, str, NoneType] = None disable_dropout: bool = False max_prompt_length: typing.Optional[int] = 512 num_generations: typing.Optional[int] = 8 max_completion_length: typing.Optional[int] = 256 ds3_gather_for_generation: bool = True shuffle_dataset: typing.Optional[bool] = True temperature: float = 0.9 top_p: float = 1.0 top_k: typing.Optional[int] = 50 min_p: typing.Optional[float] = None repetition_penalty: float = 1.0 cache_implementation: typing.Optional[str] = None use_vllm: bool = False vllm_server_host: str = '0.0.0.0' vllm_server_port: int = 8000 vllm_server_timeout: float = 240.0 vllm_guided_decoding_regex: typing.Optional[str] = None beta: float = 0.04 num_iterations: int = 1 epsilon: float = 0.2 epsilon_high: typing.Optional[float] = None reward_weights: typing.Optional[list[float]] = None scale_rewards: bool = True loss_type: str = 'bnpo' mask_truncated_completions: bool = False sync_ref_model: bool = False ref_model_mixup_alpha: float = 0.6 ref_model_sync_steps: int = 512 use_liger_loss: bool = False log_completions: bool = False num_completions_to_print: typing.Optional[int] = None wandb_log_unique_prompts: typing.Optional[bool] = False vllm_device: typing.Optional[str] = None vllm_gpu_memory_utilization: typing.Optional[float] = None vllm_dtype: typing.Optional[str] = None vllm_max_model_len: typing.Optional[int] = None vllm_enable_prefix_caching: typing.Optional[bool] = None  ) 

 

Parameters that control the model and reference model 


-  model_init_kwargs (`str`, `dict[str, Any]` or `None`, optional, defaults to `None`) —
Keyword arguments for from_pretrained, used when the `model`
argument of the GRPOTrainer is provided as a string.  
-  disable_dropout (`bool`, optional, defaults to `False`) —
Whether to disable dropout in the model. This is useful for training with a reference model, as it
prevents the model from generating different logprobs for the same input.   

Parameters that control the data preprocessing 


-  remove_unused_columns (`bool`, optional, defaults to `False`) —
Whether to only keep the column `"prompt"` in the dataset. If you use a custom reward function that
requires any column other than `"prompts"` and `"completions"`, you should keep this to `False`.  
-  max_prompt_length (`int` or `None`, optional, defaults to `512`) —
Maximum length of the prompt. If the prompt is longer than this value, it will be truncated left.  
-  num_generations (`int` or `None`, optional, defaults to `8`) —
Number of generations per prompt to sample. The effective batch size (num_processes 
per_device_batch_size  gradient_accumulation_steps) must be evenly divisible by this value.  
-  max_completion_length (`int` or `None`, optional, defaults to `256`) —
Maximum length of the generated completion.  
-  ds3_gather_for_generation (`bool`, optional, defaults to `True`) —
This setting applies to DeepSpeed ZeRO-3. If enabled, the policy model weights are gathered for generation,
improving generation speed. However, disabling this option allows training models that exceed the VRAM
capacity of a single GPU, albeit at the cost of slower generation. Disabling this option is not compatible
with vLLM generation.  
-  shuffle_dataset (`bool`, optional, defaults to `True`) —
Whether to shuffle the training dataset.   

Parameters that control generation 


-  temperature (`float`, defaults to `0.9`) —
Temperature for sampling. The higher the temperature, the more random the completions.  
-  top_p (`float`, optional, defaults to `1.0`) —
Float that controls the cumulative probability of the top tokens to consider. Must be in (0, 1]. Set to
`1.0` to consider all tokens.  
-  top_k (`int` or `None`, optional, defaults to `50`) —
Number of highest probability vocabulary tokens to keep for top-k-filtering. If `None`, top-k-filtering is
disabled.  
-  min_p (`float` or `None`, optional, defaults to `None`) —
Minimum token probability, which will be scaled by the probability of the most likely token. It must be a
value between `0.0` and `1.0`. Typical values are in the `0.01-0.2` range.  
-  repetition_penalty (`float`, optional, defaults to `1.0`) —
Float that penalizes new tokens based on whether they appear in the prompt and the generated text so far.
Values > `1.0` encourage the model to use new tokens, while values < `1.0` encourage the model to repeat
tokens.  
-  cache_implementation (`str` or `None`, optional, defaults to `None`) —
Implementation of the cache method for faster generation when use_vllm is set to False.   

Parameters that control generation acceleration powered by vLLM 


-  use_vllm (`bool`, optional, defaults to `False`) —
Whether to use vLLM for generating completions. If set to `True`, ensure that a GPU is kept unused for
training, as vLLM will require one for generation. vLLM must be installed (`pip install vllm`).  
-  vllm_server_host (`str`, optional, defaults to `"0.0.0.0"`) —
Host of the vLLM server to connect to.  
-  vllm_server_port (`int`, optional, defaults to `8000`) —
Port of the vLLM server to connect to.  
-  vllm_server_timeout (`float`, optional, defaults to `120.0`) —
Total timeout duration in seconds to wait for the vLLM server to be up. If the server is not up after the
timeout, a `ConnectionError` is raised.  
-  vllm_guided_decoding_regex (`str` or `None`, optional, defaults to `None`) —
Regex for vLLM guided decoding. If `None` (default), guided decoding is disabled.   

Parameters that control the training 


-  learning_rate (`float`, optional, defaults to `1e-6`) —
Initial learning rate for `AdamW` optimizer. The default value replaces that of
TrainingArguments.  
-  beta (`float`, optional, defaults to `0.04`) —
KL coefficient. If `0.0`, the reference model is not loaded, reducing memory usage and improving training
speed, but may be numerically unstable for long training runs.  
-  num_iterations (`int`, optional, defaults to `1`) —
Number of iterations per batch (denoted as μ in the algorithm).  
-  epsilon (`float`, optional, defaults to `0.2`) —
Epsilon value for clipping.  
-  epsilon_high (`float` or `None`, optional, defaults to `None`) —
Upper-bound epsilon value for clipping. If not specified, it defaults to the same value as the lower-bound
specified in argument `epsilon`. Paper DAPO recommends `0.28`.  
-  reward_weights (`list[float]` or `None`, optional, defaults to `None`) —
Weights for each reward function. Must match the number of reward functions. If `None`, all rewards are
weighted equally with weight `1.0`.  
-  scale_rewards (`bool`, optional, defaults to `True`) —
Whether to scale the rewards by dividing them by their standard deviation. If `True` (default), the rewards
are normalized by the standard deviation, ensuring they have unit variance. If `False`, no scaling is
applied. The Dr. GRPO paper recommends not scaling the rewards,
as scaling by the standard deviation introduces a question-level difficulty bias.  
-  loss_type (`str`, optional, defaults to `"bnpo"`) —
Specifies the loss formulation to use. Supported values are:


- `"grpo"`: Aggregates token-level losses by normalizing over sequence length. Not recommended due to
length bias—this approach tends to prefer shorter completions with positive advantages and longer ones
with negative advantages.

- `"bnpo"`: Aggregates token-level losses by normalizing number of active token in the local batch.
Note that normalization is performed over the local batch only, so results may slightly vary depending
on the local batch size, despite a constant effective batch size. When using
`per_device_train_batch_size==1`, the loss is equivalent to the GRPO loss.

- `"dr_grpo"`: Aggregates token-level losses by normalizing with a global constant. This method was
introduced in the Dr. GRPO paper to eliminate length bias.
The value of the constant corresponds to `max_completion_length`.

-  mask_truncated_completions (`bool`, optional, defaults to `False`) —
When enabled, truncated completions are excluded from the loss calculation, preventing them from being
incorrectly penalized and introducing noise during training. According to the
DAPO paper, this is a good practice for training stability.  
-  sync_ref_model (`bool`, optional, defaults to `False`) —
Whether to synchronize the reference model with the active model every `ref_model_sync_steps` steps, using
the `ref_model_mixup_alpha` parameter. This synchronization originites from the
TR-DPO paper.  
-  ref_model_mixup_alpha (`float`, optional, defaults to `0.6`) —
α parameter from the TR-DPO paper, which controls the mix
between the current policy and the previous reference policy during updates. The reference policy is
updated according to the equation: `π_ref = α * π_θ + (1 - α) * π_ref_prev`. To use this parameter, you
must set `sync_ref_model=True`.  
-  ref_model_sync_steps (`int`, optional, defaults to `512`) —
τ parameter from the TR-DPO paper, which determines how
frequently the current policy is synchronized with the reference policy. To use this parameter, you must
set `sync_ref_model=True`.  
-  use_liger_loss (`bool`, optional, defaults to `False`) —
Whether to use the Liger GRPO loss.   

Parameters that control the logging 


-  log_completions (`bool`, optional, defaults to `False`) —
Whether to log a sample of (prompt, completion) pairs every `logging_steps` steps. If `rich` is
installed, it prints the sample. If `wandb` logging is enabled, it logs it to `wandb`.  
-  num_completions_to_print (`int` or `None`, optional, defaults to `None`) —
Number of completions to print with `rich`. If `None`, all completions are logged.  
-  wandb_log_unique_prompts (`bool`, optional, defaults to `False`) —
Whether to log unique prompts in wandb. If `True`, only unique prompts are logged. If `False`, all
prompts are logged.     

Configuration class for the GRPOTrainer.


Only the parameters specific to GRPO training are listed here. For details on other parameters, refer to the
TrainingArguments documentation.


Using HfArgumentParser we can turn this class into
argparse arguments that can be specified on the
command line.
 < > Update on GitHub 


 

 

 


←GKD KTO→ 

GRPO TrainerOverviewQuick startLooking deeper into the GRPO methodGenerating completionsComputing the advantageEstimating the KL divergenceComputing the lossLoss TypesLogged metricsCustomizationSpeed up training with vLLM-powered generationGRPO at scale: train a 70B+ Model on multiple nodesUsing a custom reward functionExample 1: Reward longer completionsExample 2: Reward completions with specific formatExample 3: Reward completions based on a referenceExample 4: Multi-task reward functionsPassing the reward function to the trainerGRPOTrainerGRPOConfig
