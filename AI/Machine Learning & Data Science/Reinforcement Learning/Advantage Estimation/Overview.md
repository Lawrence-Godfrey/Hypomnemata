The advantage function measures how much better (or worse) a particular action is compared to the average action in a given state. It is a fundamental concept in modern policy gradient methods like A2C, A3C, PPO, and TRPO.

## Definition
The advantage function is defined as:
$$
A^{\pi}(s, a) = Q^{\pi}(s, a) - V^{\pi}(s)
$$

Where:
- $Q^{\pi}(s, a)$ is the [[Q Functions|Q function]] (action-value function)
- $V^{\pi}(s)$ is the [[Bellman Equation#Value Functions|value function]] (state-value function)
- $\pi$ is the policy

In words: "How much better is taking action $a$ in state $s$ compared to the average action I would take in that state under policy $\pi$?"

## Intuition
The advantage function answers a crucial question: "Should I take this action more or less often?"
- **Positive advantage** $A^{\pi}(s, a) > 0$: Action $a$ is better than average in state $s$. The policy should increase the probability of taking this action.
- **Zero advantage** $A^{\pi}(s, a) = 0$: Action $a$ is exactly as good as the average. No change needed.
- **Negative advantage** $A^{\pi}(s, a) < 0$: Action $a$ is worse than average in state $s$. The policy should decrease the probability of taking this action.

This is particularly useful because it provides a relative measure rather than an absolute one, which helps reduce variance in gradient estimates.

## Why Use Advantages in Policy Gradients?
In policy gradient methods like [[REINFORCE]], we estimate gradients of the form:
$$
\nabla_\theta J(\pi_\theta) \approx \frac{1}{N} \sum_{i=1}^{N} \sum_{t=0}^{T} \nabla_\theta \log \pi_\theta(a_t | s_t) R_t
$$
Where $R_t$ is typically the [[Reward-to-Go|reward-to-go]]. However, this can have high variance because returns can vary widely across trajectories.

By using the advantage function instead:
$$
\nabla_\theta J(\pi_\theta) \approx \frac{1}{N} \sum_{i=1}^{N} \sum_{t=0}^{T} \nabla_\theta \log \pi_\theta(a_t | s_t) A^{\pi}(s_t, a_t)
$$
We get several benefits:
1. **Reduced variance**: By subtracting the baseline $V^{\pi}(s)$, we reduce the variance of gradient estimates
2. **Unbiased gradients**: The gradient remains unbiased because $\mathbb{E}_{a \sim \pi}[A^{\pi}(s, a)] = 0$
3. **Faster learning**: Lower variance means more stable and efficient learning

## Practical Estimation Methods
In practice, we rarely have access to the true $Q^{\pi}(s, a)$ and $V^{\pi}(s)$. Instead, we estimate advantages using various methods:

- **[[Reward-to-Go]]**: Uses Monte Carlo returns as Q estimates
- **[[Temporal Difference Error]]**: Single-step bootstrapped estimates
- **[[Generalised Advantage Estimation]]**: Exponentially-weighted average of TD errors

## Actor-Critic Architecture
Advantage estimation is central to [[Actor-Critic Methods|actor-critic methods]]:
- **Actor**: The policy $\pi_\theta(a \mid s)$ that selects actions
- **Critic**: The value function $V^{\pi}(s)$ that estimates state values

The critic is used to compute advantages, which then guide the actor's updates. This architecture is used in algorithms like:
- **A2C/A3C** (Advantage Actor-Critic)
- **PPO** (Proximal Policy Optimisation)
- **TRPO** (Trust Region Policy Optimisation)
- **SAC** (Soft Actor-Critic)
