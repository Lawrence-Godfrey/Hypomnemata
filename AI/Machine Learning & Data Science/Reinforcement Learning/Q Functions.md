In reinforcement learning, the Q function (also called the action-value function) represents the expected return of taking a specific action in a specific state, and then following a particular policy thereafter. It is denoted as $Q^{\pi}(s, a)$.
## Definition
The Q function is formally defined as:
$$
Q^{\pi}(s, a) = \mathbb{E}_{\pi} \left[ \sum_{t=0}^{\infty} \gamma^t r_{t} \mid s_0 = s, a_0 = a \right]
$$
Where:
- $s$ is the current state
- $a$ is the action taken
- $\pi$ is the policy being followed after taking action $a$
- $\gamma$ is the discount factor
- $r_t$ is the reward at time step $t$

In words: "If I'm in state $s$ and take action $a$, then follow policy $\pi$ afterwards, what total discounted reward can I expect to receive?"
## Relationship to Value Functions
The Q function is closely related to the state-value function $V^{\pi}(s)$ defined in the [[Bellman Equation]]. While $V^{\pi}(s)$ tells us the expected return from a state following policy $\pi$, $Q^{\pi}(s, a)$ tells us the expected return from taking a specific action first, then following the policy.

The relationship between them is:
$$
V^{\pi}(s) = \mathbb{E}_{a \sim \pi} \left[ Q^{\pi}(s, a) \right]
$$

In other words, the value of a state is the expected Q-value over all actions that the policy might take in that state.

For a deterministic policy, this simplifies to:
$$
V^{\pi}(s) = Q^{\pi}(s, \pi(s))
$$
## The Bellman Equation for Q Functions
Just like value functions, Q functions satisfy their own Bellman equation:
$$
Q^{\pi}(s, a) = \mathbb{E}_{s' \sim P} \left[ r(s, a) + \gamma \mathbb{E}_{a' \sim \pi} \left[ Q^{\pi}(s', a') \right] \right]
$$

Where:
- $r(s, a)$ is the immediate reward for taking action $a$ in state $s$
- $s'$ is the next state
- $a'$ is the next action according to policy $\pi$

In words: "The Q-value of taking action $a$ in state $s$ is the immediate reward plus the discounted expected Q-value of the next state and action."

For the optimal Q function $Q^*(s, a)$, the Bellman optimality equation is:
$$
Q^*(s, a) = \mathbb{E}_{s'} \left[ r(s, a) + \gamma \max_{a'} Q^*(s', a') \right]
$$

This optimal Q function represents the expected return of taking action $a$ in state $s$ and then acting optimally thereafter.
## Why Q Functions Matter
Q functions are fundamental to many reinforcement learning algorithms:

**Q-Learning**: Uses the Bellman optimality equation to iteratively learn $Q^*(s, a)$, enabling the agent to derive an optimal policy by always choosing $\arg\max_a Q^*(s, a)$.

**Deep Q-Networks (DQN)**: Uses neural networks to approximate Q functions in high-dimensional state spaces.

**Actor-Critic Methods**: Use Q functions (or approximations) to evaluate actions taken by the policy, providing lower-variance gradient estimates than methods like [[REINFORCE]].

**[[Advantage Estimation]]**: Q functions are used to compute the advantage $A^{\pi}(s, a) = Q^{\pi}(s, a) - V^{\pi}(s)$, which measures how much better an action is compared to the average action in that state.
## Optimal Policy from Q Functions
Once we know the optimal Q function $Q^*(s, a)$, we can extract the optimal policy trivially:
$$
\pi^*(s) = \arg\max_a Q^*(s, a)
$$
This is one of the key advantages of Q functions: if we can learn $Q^*$, we immediately have the optimal policy without needing to learn the environment's dynamics $P(s' \mid s, a)$.
