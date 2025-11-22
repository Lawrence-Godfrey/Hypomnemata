TRPO (Schulman et al., 2015) is a foundational policy gradient method designed to solve the "step size" problem in Reinforcement Learning. Building upon standard [[Policy Gradient Optimisation]] and [[REINFORCE]], it introduces a mechanism to ensure that policy updates are safe and do not degrade performance, providing a theoretical guarantee of monotonic improvement.
## The Problem: Policy Collapse
In standard policy gradient methods (like REINFORCE), we update the policy parameters $\theta$ in the direction of the gradient $\nabla_\theta J(\theta)$.
$$ \theta_{new} = \theta_{old} + \alpha \nabla_\theta J(\theta) $$
The critical issue is choosing the step size $\alpha$:
- **Too small:** Learning is agonizingly slow.
- **Too large:** The policy changes too much, potentially entering a region of the parameter space where performance collapses. Since the data distribution depends on the policy, a bad policy produces bad data, leading to a destructive feedback loop from which the agent cannot recover.
## The Solution: Trust Regions
TRPO avoids this by enforcing a **Trust Region**. Instead of taking a step of fixed size $\alpha$ in the parameter space, we want to take the largest possible step such that the new policy $\pi_{\theta_{new}}$ is not "too different" from the old policy $\pi_{\theta_{old}}$.

We measure "difference" using the **KL Divergence** (Kullback-Leibler divergence).
### The Objective
TRPO maximizes a **surrogate objective** subject to a **hard constraint** on the KL divergence:

$$
\begin{aligned}
\max_\theta \quad & \mathbb{E}_t \left[ \frac{\pi_\theta(a_t|s_t)}{\pi_{\theta_{old}}(a_t|s_t)} A_t \right] \\
\text{subject to} \quad & \mathbb{E}_t \left[ D_{KL}(\pi_{\theta_{old}}(\cdot|s_t) || \pi_\theta(\cdot|s_t)) \right] \le \delta
\end{aligned}
$$

- **Ratio:** $\frac{\pi_\theta}{\pi_{\theta_{old}}}$ is the importance sampling ratio.
- **$A_t$:** The Advantage function (how much better an action is than average).
- **$\delta$:** The step size limit (hyperparameter).
## Implementation Details
Solving this constrained optimization problem exactly is intractable for deep neural networks. TRPO uses two key approximations:
1.  **Linear approximation** of the objective.
2.  **Quadratic approximation** of the KL constraint (using the Fisher Information Matrix).

This results in a step direction calculated using the **Conjugate Gradient** algorithm (to avoid inverting the massive Fisher matrix) and a line search to ensure the constraint is satisfied.
## Why it was necessary
Before TRPO, training deep RL agents was extremely unstable. You had to carefully tune learning rates for every specific problem. TRPO provided a robust, stable method that worked across a wide range of tasks without extensive hyperparameter tuning.
## Limitations
- **Complexity:** Implementing the Conjugate Gradient and Fisher Vector Product is mathematically complex and hard to debug.
- **Computation:** Calculating second-order information (Hessian/Fisher matrix interactions) is computationally expensive compared to simple backpropagation.
- **Incompatibility:** It is difficult to combine with architectures that use noise (like Dropout) or parameter sharing in certain ways.

These limitations led directly to the development of [[PPO]].
