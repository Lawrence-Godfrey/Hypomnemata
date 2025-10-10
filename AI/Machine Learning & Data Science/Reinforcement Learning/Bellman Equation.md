The Bellman Equation, named after its creator Richard Bellman, is a fundamental concept in Reinforcement Learning and dynamic programming. It provides a recursive definition for the **value** of being in a particular state, breaking it down into two key components: the immediate reward you get from your next action and the discounted value of the state you end up in.

At its core, the Bellman Equation formalises the intuitive idea that the value of your current situation is determined by the immediate benefit you can get, plus the value of the situation you'll be in next.
## Value Functions
In reinforcement learning, we want to learn a **policy** (a strategy for choosing actions) that maximises the total future reward. This can be a [[Deterministic vs Stochastic Policies|deterministic or stochastic policy]]. To do this, we define **value functions** that estimate how good it is to be in a particular state.
-   **State-Value Function, V(s):** The expected total reward an agent can get starting from state *s* and following a specific policy.
-   **Action-Value Function, Q(s, a):** The expected total reward an agent can get by taking action *a* in state *s* and then following a specific policy thereafter.

The Bellman Equation provides a way to calculate these values.
## The Bellman Expectation Equation
This equation calculates the value of a state *s* under a specific policy $\pi$. It states that the value of your current state is the immediate reward you expect to get, plus the discounted value of the state you'll likely be in next.

The equation for the state-value function $V^\pi(s)$ is:
$$
V^\pi(s) = \mathbb{E}_\pi [R_{t+1} + \gamma V^\pi(S_{t+1}) | S_t = s]
$$
Let's break it down:
-   $V^\pi(s)$: The value of being in state *s* while following policy $\pi$.
-   $\mathbb{E}_\pi[\dots]$: The expected value, assuming the agent follows policy $\pi$.
-   $R_{t+1}$: The immediate reward received at the next time step.
-   $\gamma$ (gamma): The **discount factor** (a number between 0 and 1). It determines how much we value future rewards. A $\gamma$ of 0 means we only care about the immediate reward, while a $\gamma$ close to 1 means we value future rewards highly.
-   $V^\pi(S_{t+1})$: The value of the *next* state, $S_{t+1}$.

In simple terms: **The value of a state today is the immediate reward plus the discounted value of the state tomorrow.**
## The Bellman Optimality Equation
While the expectation equation is for a *given* policy, the **Bellman Optimality Equation** is about finding the *best* possible value. It says that the value of a state under an optimal policy must be equal to the expected return for the best action taken from that state.

For the optimal state-value function $V^*(s)$:
$$
V^*(s) = \max_a \mathbb{E}[R_{t+1} + \gamma V^*(S_{t+1}) | S_t = s, A_t = a]
$$
The only difference is the $\max_a$ operator. It means we don't just follow a policy; we choose the action *a* that maximises the expected future reward. This equation is the foundation for many RL algorithms like [[Q-learning]] and [[Value Iteration]], which aim to solve this equation to find the optimal policy.

## Expectation vs Optimality

| Aspect                  | Bellman Expectation Equation                                                     | Bellman Optimality Equation                          |
| :---------------------- | :------------------------------------------------------------------------------- | :--------------------------------------------------- |
| **Purpose**             | To **evaluate** a given policy ($\pi$).                                          | To define the **best possible** performance.         |
| **Question it Answers** | "How good is my current strategy?"                                               | "What is the value of acting perfectly?"             |
| **Action Selection**    | Averages over the actions defined by the policy $\pi$.                           | Chooses the single best action (`max`) at each step. |
| **Result**              | The value of a state under a specific, possibly sub-optimal, policy ($V^{\pi}$). | The maximum possible value of a state ($V^∗$).       |

In short, the **Expectation** equation is for _policy evaluation_, while the **Optimality** equation defines the _target_ for finding the perfect policy. Reinforcement learning algorithms often iterate between using the expectation equation to see how good their current policy is, and then using the optimality principle to improve it.