**Generalized Advantage Estimation (GAE)** is a method for estimating the [[README|advantage function]] that provides a tunable bias-variance tradeoff. It was introduced by Schulman et al. in 2016 and has become the standard approach for computing advantages in modern policy gradient algorithms like PPO and TRPO.
## The Problem
When estimating advantages, we face a fundamental tradeoff:
- **[[Reward-to-Go|Reward-to-go]]** (Monte Carlo): High variance, no bias. E.g.,$$\hat{A}(s_t, a_t) = \sum_{t'=t}^{T} \gamma^{t'-t} r_{t'} - V(s_t)$$
- **[[Temporal Difference Error|TD error]]** (one-step): Low variance, can be biased. E.g., $$\hat{A}(s_t, a_t) = r_t + \gamma V(s_{t+1}) - V(s_t)$$
GAE provides a way to smoothly interpolate between these extremes.
## Definition
GAE computes advantages as an exponentially-weighted average of multi-step TD errors:
$$
A^{\text{GAE}(\gamma, \lambda)}(s_t, a_t) = \sum_{l=0}^{\infty} (\gamma \lambda)^l \delta_{t+l}
$$

Where:
- $\delta_t = r_t + \gamma V^{\pi}(s_{t+1}) - V^{\pi}(s_t)$ is the [[Temporal Difference Error|TD error]]
- $\gamma$ is the discount factor for rewards
- $\lambda \in [0, 1]$ is the GAE parameter that controls the bias-variance tradeoff

## Expanded Form
We can write out the first few terms to see the pattern:
$$
\begin{align}
A^{\text{GAE}}(s_t, a_t) &= \delta_t + (\gamma \lambda) \delta_{t+1} + (\gamma \lambda)^2 \delta_{t+2} + \cdots \\
&= (r_t + \gamma V(s_{t+1}) - V(s_t)) \\
&\quad + (\gamma \lambda)(r_{t+1} + \gamma V(s_{t+2}) - V(s_{t+1})) \\
&\quad + (\gamma \lambda)^2(r_{t+2} + \gamma V(s_{t+3}) - V(s_{t+2})) + \cdots
\end{align}
$$

## The Lambda Parameter
The parameter $\lambda$ controls the bias-variance tradeoff:

**$\lambda = 0$**: Pure TD error (one-step)
$$
A^{\text{GAE}(\gamma, 0)} = \delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)
$$
- Lowest variance
- Highest bias (if $V$ is inaccurate)

**$\lambda = 1$**: Pure Monte Carlo (reward-to-go minus baseline)
$$
A^{\text{GAE}(\gamma, 1)} = \sum_{l=0}^{\infty} \gamma^l \delta_{t+l} = \sum_{t'=t}^{\infty} \gamma^{t'-t} r_{t'} - V(s_t)
$$
- Highest variance
- No bias (unbiased estimate)

**$\lambda \in (0, 1)$**: Balanced tradeoff
- Most practical setting (commonly $\lambda = 0.95$ or $0.97$)
- Reduces variance compared to Monte Carlo
- Reduces bias compared to single-step TD

## Intuition
GAE gives more weight to nearby rewards and less weight to distant rewards:
- Recent TD errors ($\delta_t, \delta_{t+1}$) get more weight
- Distant TD errors ($\delta_{t+10}, \delta_{t+20}$) get exponentially less weight

This makes sense because:
1. **Nearby rewards are more relevant**: Actions have more direct influence on immediate consequences
2. **Distant estimates are less reliable**: Compounding errors in $V$ make long-term bootstrapping less trustworthy
3. **Exponential decay is natural**: Matches the discount factor $\gamma$ used in the MDP

## Practical Implementation
In code, GAE is typically computed backwards from the end of a trajectory:

```python
advantages = []
gae = 0

for t in reversed(range(len(trajectory))):
    delta = rewards[t] + gamma * values[t+1] - values[t]
    gae = delta + gamma * lambda * gae
    advantages.insert(0, gae)
```

This backward pass efficiently accumulates the weighted sum of TD errors.

## Why GAE is Popular
GAE has become the standard in modern RL because:
1. **Tunable tradeoff**: Single parameter $\lambda$ lets you adjust bias-variance
2. **Empirically effective**: Works well across diverse tasks with $\lambda \approx 0.95$
3. **Simple to implement**: Just requires value function and trajectory data
4. **Used in SOTA algorithms**: PPO, TRPO, and other top-performing methods use GAE

## Comparison Table

| Method | Variance | Bias | Episode Required? | Formula |
|--------|----------|------|-------------------|---------|
| Reward-to-go | High | None | Yes | $\sum_{t'=t}^{T} \gamma^{t'-t} r_{t'} - V(s_t)$ |
| TD error | Low | If $V$ wrong | No | $r_t + \gamma V(s_{t+1}) - V(s_t)$ |
| GAE ($\lambda=0.95$) | Medium | Small | Yes | $\sum_{l=0}^{\infty} (\gamma \lambda)^l \delta_{t+l}$ |

## Connection to n-Step Returns
GAE can be viewed as an exponentially-weighted average of all n-step advantage estimates:
- 1-step: $\delta_t$
- 2-step: $\delta_t + \gamma \delta_{t+1}$
- 3-step: $\delta_t + \gamma \delta_{t+1} + \gamma^2 \delta_{t+2}$
- ...

GAE combines all of these with exponentially decaying weights $(1-\lambda)\lambda^n$, giving a principled way to balance short-term and long-term estimates.
