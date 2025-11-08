These are three fundamental mathematical tricks that appear repeatedly in reinforcement learning algorithms. Understanding these tricks is crucial for grasping advanced RL methods.
## 1. The Log-Likelihood Trick (Log-Derivative Trick)
### The Core Identity
$$\nabla_\theta \log f(\theta) = \frac{\nabla_\theta f(\theta)}{f(\theta)}$$
Or equivalently:
$$\nabla_\theta f(\theta) = f(\theta) \nabla_\theta \log f(\theta)$$
### Why It's Useful
This trick transforms a gradient of a probability into an expectation, enabling Monte Carlo estimation:

**Before the trick:**
$$\int_{\tau} \nabla_\theta P(\tau | \pi_\theta) R(\tau) d\tau$$
This is **not an expectation** . There's no probability distribution multiplying a function. You can't sample here because you'd need to sample from $\nabla_\theta P(\tau | \pi_\theta)$, but that's not a probability distribution (it can be negative, doesn't integrate to 1).

**After the trick:**
$$\int_{\tau} P(\tau | \pi_\theta) \nabla_\theta \log P(\tau | \pi_\theta) R(\tau) d\tau = \mathbb{E}_{\tau \sim \pi_\theta}[\nabla_\theta \log P(\tau | \pi_\theta) R(\tau)]$$
This **is an expectation** in the form $\mathbb{E}_{x \sim p}[f(x)]$ where $p = P(\tau | \pi_\theta)$ is the probability distribution you sample from, and $f(\tau) = \nabla_\theta \log P(\tau | \pi_\theta) R(\tau)$ is the function you evaluate.
### Applications
- **[[REINFORCE]]**: Core of the policy gradient derivation
- [[Variational Inference]]: ELBO optimization in [[VAEs]]
- **Any gradient estimation involving probabilities**
## 2. Importance Sampling
### The Core Idea
Estimate $\mathbb{E}_{x \sim p}[f(x)]$ using samples from a different distribution $q(x)$:

$$\mathbb{E}_{x \sim p}[f(x)] = \int p(x) f(x) dx = \int q(x) \frac{p(x)}{q(x)} f(x) dx = \mathbb{E}_{x \sim q}\left[\frac{p(x)}{q(x)} f(x)\right]$$

The ratio $\frac{p(x)}{q(x)}$ is called the **importance weight**.
### Why It's Useful
- **Off-policy learning**: Use data from old policy to update new policy
- **Rare event simulation**: Sample from easier distribution, reweight appropriately
- **Data efficiency**: Reuse collected data instead of collecting new samples
### Applications in RL
- **Off-policy policy gradients**: Estimate gradient for $\pi_\theta$ using data from $\pi_{\text{old}}$
- **[[PPO]]**: Uses importance sampling with clipping
- **Experience replay**: Reuse old transitions for learning
### Example
Want to estimate returns under new policy $\pi_\theta$ using trajectories from old policy $\pi_{\text{old}}$:

$$\mathbb{E}_{\tau \sim \pi_\theta}[R(\tau)] = \mathbb{E}_{\tau \sim \pi_{\text{old}}}\left[\frac{P(\tau | \pi_\theta)}{P(\tau | \pi_{\text{old}})} R(\tau)\right]$$
## 3. Expectation of Score Function is Zero
### The Identity
For any probability distribution $p(x; \theta)$:
$$\mathbb{E}_{x \sim p(x; \theta)}[\nabla_\theta \log p(x; \theta)] = 0$$
### Proof
$$\mathbb{E}_{x \sim p}[\nabla_\theta \log p(x; \theta)] = \int p(x; \theta) \nabla_\theta \log p(x; \theta) dx$$

Using the log-derivative trick:
$$= \int p(x; \theta) \frac{\nabla_\theta p(x; \theta)}{p(x; \theta)} dx = \int \nabla_\theta p(x; \theta) dx$$

$$= \nabla_\theta \int p(x; \theta) dx = \nabla_\theta 1 = 0$$

(Since probabilities integrate to 1)
### Why It's Useful
This property is crucial for:
1. **Variance reduction**: Shows that adding the score function to any estimator doesn't change its expectation (used in control variates)
2. **Natural gradients**: Foundation for natural policy gradient methods
3. **Baseline methods**: Justifies subtracting baselines in REINFORCE without introducing bias
### Applications
**Control Variates in REINFORCE**:
The vanilla REINFORCE gradient has high variance. You can subtract any function $b(s_t)$ that doesn't depend on actions:

$$\nabla_\theta J = \mathbb{E}\left[\sum_t \nabla_\theta \log \pi_\theta(a_t|s_t) (R(\tau) - b(s_t))\right]$$

The baseline $b(s_t)$ doesn't change the expectation because:
$$\mathbb{E}\left[\nabla_\theta \log \pi_\theta(a_t|s_t) b(s_t)\right] = b(s_t) \mathbb{E}[\nabla_\theta \log \pi_\theta(a_t|s_t)] = b(s_t) \cdot 0 = 0$$
## How These Tricks Work Together
Many RL algorithms use combinations of these tricks:
1. **PPO**: Uses log-likelihood trick for policy gradients + importance sampling for off-policy updates
2. **Actor-Critic methods**: Use score function property for baseline/critic without bias
3. **Natural Policy Gradients**: Combine all three tricks for more stable updates

