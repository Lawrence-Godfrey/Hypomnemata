**Actor-Critic methods** are a family of reinforcement learning algorithms that combine two components:
- **Actor**: A policy network that decides which actions to take
- **Critic**: A value function that evaluates how good states (or state-action pairs) are

This architecture addresses key limitations of pure policy gradient methods (like [[REINFORCE]]) and pure value-based methods (like Q-learning).

## Architecture

### The Actor
The actor is a policy $\pi_\theta(a|s)$ parameterized by $\theta$ that maps states to actions (or action probabilities). It is updated using policy gradients:
$$
\nabla_\theta J(\pi_\theta) \approx \frac{1}{N} \sum_{i=1}^{N} \sum_{t=0}^{T} \nabla_\theta \log \pi_\theta(a_t | s_t) A(s_t, a_t)
$$

The actor's job is to **act** - to decide what to do in each state.

### The Critic
The critic is a value function $V^{\pi}(s)$ (or sometimes [[Q Functions|Q function]] $Q^{\pi}(s,a)$) that estimates expected returns. It is trained using temporal difference learning or Monte Carlo methods.

The critic's job is to **critique** - to evaluate how good the actor's decisions are by estimating advantages:
$$
A(s_t, a_t) \approx r_t + \gamma V(s_{t+1}) - V(s_t)
$$

## Why Actor-Critic?
Actor-critic methods solve problems with earlier approaches:

### Problems with Pure Policy Gradients (REINFORCE)
- **High variance**: Gradient estimates vary wildly between trajectories
- **Sample inefficiency**: Requires many episodes to get stable gradients
- **Slow learning**: High variance means slow convergence

**Actor-critic solution**: Use the critic's value estimates to compute [[README|advantages]], which have much lower variance than raw trajectory returns.

### Problems with Pure Value-Based Methods (DQN, Q-learning)
- **Can't handle continuous actions**: Must discretize action space
- **Can't learn stochastic policies**: Only learns deterministic argmax policy
- **Exploration challenges**: Requires epsilon-greedy or other exploration hacks

**Actor-critic solution**: The actor directly parameterizes a stochastic policy that can naturally handle continuous actions and exploration.

## How They Work Together

1. **Actor takes action**: Sample $a_t \sim \pi_\theta(a|s_t)$
2. **Environment responds**: Observe reward $r_t$ and next state $s_{t+1}$
3. **Critic evaluates**: Compute advantage estimate (e.g., TD error)
   $$A(s_t, a_t) = r_t + \gamma V(s_{t+1}) - V(s_t)$$
4. **Both learn**:
   - **Critic update**: Minimize value function error
     $$\mathcal{L}_{\text{critic}} = (V(s_t) - \text{target})^2$$
   - **Actor update**: Maximize expected return using advantage
     $$\nabla_\theta J(\pi_\theta) \propto \nabla_\theta \log \pi_\theta(a_t | s_t) \cdot A(s_t, a_t)$$

## Types of Critics

### State-Value Critic
Estimates $V^{\pi}(s)$, used to compute advantages via [[Temporal Difference Error|TD errors]]:
$$A(s_t, a_t) = r_t + \gamma V(s_{t+1}) - V(s_t)$$

**Examples**: A2C, A3C, PPO

### Action-Value Critic  
Estimates [[Q Functions|Q function]] $Q^{\pi}(s,a)$, can directly provide action values:
$$A(s_t, a_t) = Q(s_t, a_t) - V(s_t)$$

**Examples**: DDPG, TD3, SAC

## Common Actor-Critic Algorithms

### A2C/A3C (Advantage Actor-Critic)
- Uses state-value critic $V(s)$
- Computes advantages using [[Temporal Difference Error|TD error]] or [[Generalised Advantage Estimation|GAE]]
- A3C is asynchronous version with multiple parallel workers

### PPO (Proximal Policy Optimization)
- Actor-critic with clipped objective to prevent large policy updates
- Uses [[Generalised Advantage Estimation|GAE]] for advantage estimation
- One of the most popular modern RL algorithms

### TRPO (Trust Region Policy Optimization)
- Constrains policy updates to a "trust region" using KL divergence
- Theoretically principled but computationally expensive
- PPO is a simpler approximation of TRPO

### DDPG/TD3 (Deep Deterministic Policy Gradient)
- For continuous action spaces
- Uses Q-function critic
- Deterministic policy with noise for exploration

### SAC (Soft Actor-Critic)
- Entropy-regularized actor-critic
- Encourages exploration through maximum entropy objective
- State-of-the-art for many continuous control tasks

## Advantages and Disadvantages

**Advantages**:
- **Lower variance** than pure policy gradient methods
- **Handles continuous actions** unlike pure value-based methods
- **More sample efficient** than REINFORCE
- **Can learn stochastic policies** naturally

**Disadvantages**:
- **More complex**: Two networks to train instead of one
- **Can be unstable**: Critic errors can destabilize actor training
- **Hyperparameter sensitive**: Learning rates, advantage estimation method, etc.
- **Training challenges**: Need to balance actor and critic learning

## Key Design Choices

When implementing actor-critic methods, you must decide:
1. **Advantage estimation**: TD error, n-step, or [[Generalised Advantage Estimation|GAE]]?
2. **Network architecture**: Shared or separate networks for actor and critic?
3. **Update frequency**: Update every step, or batch updates?
4. **On-policy vs off-policy**: A2C/PPO (on-policy) or DDPG/SAC (off-policy)?
5. **Entropy regularization**: Add entropy bonus to encourage exploration?
