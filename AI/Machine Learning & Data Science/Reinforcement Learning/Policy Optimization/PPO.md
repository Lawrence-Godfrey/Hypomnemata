PPO (Schulman et al., 2017) is currently the default standard reinforcement learning algorithm for many domains, including OpenAI's GPT training (RLHF). It was designed to achieve the stability and reliability of its predecessor, [[TRPO]], but with the simplicity of a first-order method (like standard SGD).
## The Problem with TRPO
While [[TRPO]] solved the stability issue, it was:
1.  **Complex:** Required calculating second-order derivatives (Fisher Information Matrix) and using Conjugate Gradient.
2.  **Slow:** The optimization step was computationally heavy.
3.  **Restrictive:** Hard to use with architectures like RNNs or Dropout.
## The Solution: Clipped Surrogate Objective
PPO removes the complex KL-constraint optimization. Instead, it includes the constraint **directly in the objective function** via clipping.

It asks: *"How can we penalize the policy for changing too much, using only first-order derivatives?"*
### The Algorithm
PPO maintains the ratio between the new and old policy:
$$ r_t(\theta) = \frac{\pi_\theta(a_t|s_t)}{\pi_{\theta_{old}}(a_t|s_t)} $$

The objective function is:
$$ L^{CLIP}(\theta) = \mathbb{E}_t \left[ \min(r_t(\theta) A_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) A_t) \right] $$

![[Pasted image 20251122085929.png]]
### How it works
1.  **Unclipped Part ($r_t A_t$):** This is the standard TRPO surrogate objective. It pushes the policy to increase the probability of good actions ($A_t > 0$).
2.  **Clipped Part:** The function $\text{clip}(r_t, 1-\epsilon, 1+\epsilon)$ limits the ratio to be between $[0.8, 1.2]$ (if $\epsilon=0.2$).
3.  **Min Operator:**
    - If the action was **good** ($A_t > 0$): The objective increases as $r_t$ increases, but *stops increasing* once $r_t > 1+\epsilon$. This prevents the update from being too greedy.
    - If the action was **bad** ($A_t < 0$): The objective decreases as $r_t$ increases, but *stops decreasing* (penalty is capped) if $r_t < 1-\epsilon$. This prevents the policy from being destroyed by a single bad sample.
## Why it was necessary
PPO democratized Deep RL. It allowed researchers to train stable agents using standard deep learning optimizers (like Adam) without needing to implement complex math like Conjugate Gradient. It strikes a perfect balance between sample complexity, simplicity, and wall-clock time.
## The "Critic" Bottleneck
PPO is an **Actor-Critic** method. It requires training two networks:
1.  **Actor ($\pi_\theta$):** The policy.
2.  **Critic ($V_\phi$):** Estimates the value of a state to compute the Advantage $A_t$.

For standard RL (Atari, Robotics), the Critic is small. But for **Large Language Models**, the Critic must be as smart as the Actor to judge it effectively. This means if you are finetuning a 70B parameter model, you need *another* 70B parameter model just to be the Critic. This doubles memory requirements.

This limitation led to the development of [[GRPO]].
