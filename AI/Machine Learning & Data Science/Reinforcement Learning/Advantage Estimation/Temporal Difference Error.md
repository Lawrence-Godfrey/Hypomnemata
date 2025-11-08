The **Temporal Difference (TD) error** is a one-step bootstrapped estimate of the [[README|advantage function]]. It provides a low-variance alternative to [[Reward-to-Go|reward-to-go]] methods by using the value function to estimate future returns instead of sampling complete trajectories.

## Definition
The TD error at time step $t$ is defined as:
$$
\delta_t = r_t + \gamma V^{\pi}(s_{t+1}) - V^{\pi}(s_t)
$$

Where:
- $r_t$ is the immediate reward at time $t$
- $\gamma$ is the discount factor
- $V^{\pi}(s_{t+1})$ is the value of the next state
- $V^{\pi}(s_t)$ is the value of the current state

## Intuition
The TD error answers the question: "Did I do better or worse than expected?"

Breaking it down:
- $r_t + \gamma V^{\pi}(s_{t+1})$: The **actual** return we got (immediate reward plus estimated future value)
- $V^{\pi}(s_t)$: What we **expected** to get from state $s_t$
- $\delta_t$: The **difference** between actual and expected

If $\delta_t > 0$, things went better than expected. If $\delta_t < 0$, things went worse than expected.

## As an Advantage Estimate
The TD error is an unbiased estimate of the advantage function:
$$
A^{\pi}(s_t, a_t) \approx \delta_t
$$

To see why, recall that:
$$
A^{\pi}(s_t, a_t) = Q^{\pi}(s_t, a_t) - V^{\pi}(s_t)
$$

And the [[Bellman Equation]] tells us:
$$
Q^{\pi}(s_t, a_t) = \mathbb{E}[r_t + \gamma V^{\pi}(s_{t+1})]
$$

Therefore:
$$
A^{\pi}(s_t, a_t) \approx r_t + \gamma V^{\pi}(s_{t+1}) - V^{\pi}(s_t) = \delta_t
$$

## Bias-Variance Tradeoff
**Advantages of TD error**:
- **Low variance**: Only depends on one transition, not an entire trajectory
- **No need for complete episodes**: Can be computed immediately after each step
- **Faster learning**: Lower variance means more stable gradient estimates

**Disadvantages of TD error**:
- **Can be biased**: If $V^{\pi}$ is not accurately estimated (which is common early in training), the advantage estimate will be biased
- **Bootstrap error compounds**: Errors in $V^{\pi}$ affect the estimate

## Comparison with Reward-to-Go
| Aspect | Reward-to-Go | TD Error |
|--------|--------------|----------|
| **Variance** | High | Low |
| **Bias** | Unbiased | Biased if $V^{\pi}$ is inaccurate |
| **Episode requirement** | Complete trajectory | Single step |
| **Sensitivity** | Noisy trajectories | Errors in value function |

## Multi-Step TD Error
We can extend TD error to use $n$ steps before bootstrapping:
$$
\delta_t^{(n)} = r_t + \gamma r_{t+1} + \gamma^2 r_{t+2} + \cdots + \gamma^n V^{\pi}(s_{t+n}) - V^{\pi}(s_t)
$$

- $n=1$: Standard TD error (low variance, higher bias)
- $n=\infty$: Equivalent to reward-to-go (high variance, no bias)
- $n$ intermediate: Balanced tradeoff

This idea is generalized in [[Generalised Advantage Estimation|GAE]], which takes an exponentially-weighted average of all multi-step TD errors.

## Usage in Algorithms
TD error is used in many reinforcement learning algorithms:
- **TD Learning**: Updates value functions using $V(s_t) \leftarrow V(s_t) + \alpha \delta_t$
- **Actor-Critic**: Uses TD error as the advantage estimate for policy updates
- **A3C/A2C**: Asynchronous/synchronous advantage actor-critic methods
- **PPO with GAE**: When $\lambda = 0$, GAE reduces to single-step TD error
