A **Markov Decision Process (MDP)** is the mathematical framework for modelling sequential decision-making problems in reinforcement learning. It formalises an environment in which an agent takes actions to maximise cumulative reward over time.

MDPs extend [[Markov Chains]] by adding actions and rewards, giving the agent control over state transitions.

## Formal Definition
An MDP is defined by a tuple $(S, A, P, R, \gamma)$:

- **$S$**: Set of states (the possible situations the agent can be in)
- **$A$**: Set of actions (choices available to the agent)
- **$P$**: Transition function $P(s' | s, a)$ — probability of reaching state $s'$ after taking action $a$ in state $s$
- **$R$**: Reward function $R(s, a, s')$ or $R(s, a)$ — immediate reward received
- **$\gamma$**: Discount factor $\gamma \in [0, 1]$ — determines how much future rewards are valued

### The Markov Property
The key assumption is that the future depends only on the **current state**, not on the history of how you got there:
$$P(S_{t+1} | S_t, A_t, S_{t-1}, A_{t-1}, \dots) = P(S_{t+1} | S_t, A_t)$$
This is the **Markov property** or "memorylessness". The current state contains all relevant information for decision-making.

## Objective
The agent's goal is to find a **policy** $\pi$ (a mapping from states to actions) that maximises the **expected cumulative discounted reward**:
$$\mathbb{E}\left[\sum_{t=0}^{\infty} \gamma^t R_t \mid \pi\right]$$
where $R_t$ is the reward at time step $t$.
