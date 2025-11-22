The **reward-to-go** (also called "return" or "cumulative discounted reward from time t") is the sum of all future rewards from a given time step onward in a trajectory. It is a Monte Carlo estimate of the [[Q Functions|Q function]] $Q^{\pi}(s_t, a_t)$.

## Definition
The reward-to-go at time step $t$ is defined as:
$$
R_t = \sum_{t'=t}^{T} \gamma^{t'-t} r_{t'}
$$

Where:
- $r_{t'}$ is the reward at time step $t'$
- $\gamma$ is the discount factor
- $T$ is the final time step of the trajectory

Without discounting (or when $\gamma = 1$), this simplifies to:
$$
R_t = \sum_{t'=t}^{T} r_{t'}
$$

## Why Reward-to-Go?
In the basic [[REINFORCE]] algorithm, each action at time $t$ is weighted by the total return of the entire trajectory $R(\tau) = \sum_{t'=0}^{T} r_{t'}$. However, this includes rewards from *before* the action was taken, which the action couldn't have influenced.

**Key insight**: An action at time $t$ can only affect rewards from time $t$ onward, not rewards in the past.

By using reward-to-go instead of total trajectory return, we:
1. **Reduce variance**: Remove irrelevant past rewards that add noise to gradient estimates
2. **Maintain correctness**: The gradient estimate remains unbiased
3. **Improve learning**: Lower variance leads to more stable and efficient training

## Usage in Policy Gradients
In [[REINFORCE]], the gradient estimate becomes:
$$
\nabla_\theta J(\pi_\theta) \approx \frac{1}{N} \sum_{i=1}^{N} \left[\sum_{t=0}^{T} \nabla_\theta \log \pi_\theta(a_{i, t} | s_t) \right] \left(\sum_{t'=t}^{T} r(s_{i,t'}, a_{i,t'})\right)
$$

Instead of multiplying by the entire trajectory return, each action is weighted only by the rewards that follow it.

## As a Q Function Estimate
The reward-to-go serves as a Monte Carlo estimate of the action-value function:
$$
Q^{\pi}(s_t, a_t) \approx R_t = \sum_{t'=t}^{T} \gamma^{t'-t} r_{t'}
$$

This estimate:
- **High variance**: Different trajectories from the same state-action pair can yield very different returns
- **No bias**: In expectation, it equals the true Q value (assuming infinite samples)
- **Requires complete trajectories**: Must wait until the episode ends to compute

## Combining with Baselines
Reward-to-go is often combined with a baseline (typically the value function $V^{\pi}(s_t)$) to further reduce variance:
$$
A(s_t, a_t) \approx R_t - V^{\pi}(s_t)
$$

This gives us an estimate of the [[README|advantage function]], which measures how much better the action was compared to the average. This is the foundation of advantage-based methods and [[Actor-Critic Methods|actor-critic]] algorithms.

## Comparison with Other Estimates
- **Total return** $R(\tau)$: Includes irrelevant past rewards, higher variance
- **Reward-to-go** $R_t$: Only future rewards, reduced variance
- **[[Temporal Difference Error|TD error]]**: Single-step bootstrap, even lower variance but can be biased
- **[[Generalised Advantage Estimation|GAE]]**: Interpolates between reward-to-go and TD error using parameter $\lambda$
