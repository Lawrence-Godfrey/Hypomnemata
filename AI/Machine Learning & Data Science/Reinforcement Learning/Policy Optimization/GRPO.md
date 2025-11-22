GRPO (Group Relative Policy Optimisation) was introduced by Deepseek in the [DeepSeekMath paper](https://arxiv.org/pdf/2402.03300) and popularised by the [Deepseek R1 release](https://api-docs.deepseek.com/news/news250120).

It is a RL method specifically optimized for **Large Language Models (LLMs)**. It improves on [[PPO]] by removing the need for a Value Function (Critic) network.
## The Problem with PPO for LLMs
In standard [[PPO]], we need to calculate the Advantage $A_t$:
$$ A_t = Q(s,a) - V(s) $$
To get $V(s)$, PPO trains a **Critic** network.
- In robotics, the Critic is a tiny MLP.
- In LLMs, the Critic must understand the text as well as the Policy. This means the Critic is usually a copy of the Policy model (e.g., a 7B or 70B parameter transformer).

**The Cost:**
- **Memory:** You need to hold the Policy + the Critic + Gradients for both + Optimizer states for both. This effectively doubles the VRAM requirements.
- **Compute:** You have to run forward/backward passes for both models.
## The Solution: Group Relative Advantage
GRPO eliminates the Critic entirely. Instead of learning a value function $V(s)$ to predict the baseline, it estimates the baseline empirically by sampling multiple outputs for the same input.
### The Algorithm
For each prompt (state) $q$, GRPO samples a group of $G$ outputs $\{o_1, o_2, ..., o_G\}$ from the old policy $\pi_{\theta_{old}}$.

1.  **Sample:** Generate $G$ different completions for the question $q$.
2.  **Score:** Calculate the reward $r_i$ for each completion using the reward model (or rule-based checker).
3.  **Advantage:** Calculate the advantage for each output by normalizing the rewards *within the group*:
    $$ A_i = \frac{r_i - \text{mean}(\{r_1, ..., r_G\})}{\text{std}(\{r_1, ..., r_G\}) + \epsilon} $$

The objective function is then similar to PPO (using the clipped ratio), but using this group-based advantage:
$$ J_{GRPO}(\theta) = \mathbb{E} \left[ \frac{1}{G} \sum_{i=1}^G \min \left( \frac{\pi_\theta(o_i|q)}{\pi_{\theta_{old}}(o_i|q)} A_i, \text{clip}(...) A_i \right) - \beta D_{KL}(\pi_\theta || \pi_{ref}) \right] $$
## Why it works
- **Baseline:** The mean reward of the group acts as the baseline $V(s)$. If an output $o_i$ is better than the group average, it has a positive advantage. If it's worse, it has a negative advantage.
- **Efficiency:** No Critic network is needed. This saves ~50% of memory resources, allowing for training larger models or using larger batch sizes.
## Comparison
| Feature | [[TRPO]] | [[PPO]] | [[GRPO]] |
| :--- | :--- | :--- | :--- |
| **Constraint** | Hard KL Constraint | Clipped Objective | Clipped Objective + KL Penalty |
| **Optimization** | Second-order (Conjugate Gradient) | First-order (Adam) | First-order (Adam) |
| **Critic Required?** | Yes | Yes | **No** |
| **Best For** | Theoretical guarantees | General Purpose RL | **LLM Reasoning / Fine-tuning** |
## When to use GRPO?
GRPO is ideal when:
1.  **The Environment is Resettable:** You can ask the model the same question multiple times (trivial for LLMs).
2.  **The Critic is Expensive:** The model is so large that duplicating it for a Critic is prohibitive.
3.  **Sparse Rewards:** By sampling a group, you are more likely to find at least one successful trajectory to learn from (exploration). 
