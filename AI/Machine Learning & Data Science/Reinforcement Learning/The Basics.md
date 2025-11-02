The goal of RL is to select a policy $\pi$ which maximises the expected reward when the agent acts according to it.
$$
\pi^{*}= \arg \max_{\pi} J(\pi)
$$

The expected return of a policy is the expected return over all possible trajectories. 
$$J(\pi) = \int_{\tau} P(\tau | \pi) R(\tau) = E_{\substack{\tau \sim \pi}}[R(\tau)]$$

A trajectory is a series of (action, state) starting from an initial state $s_0$ and following the policy $\pi$:

$$
\tau = (s_0, a_0, s_1, a_1, \ldots, s_T, a_T)
$$

We will model the next state as being stochastic:

$$
s_{t+1} \sim P(s_{t+1} | s_t, a_t)
$$

We can then define the probability of a trajectory given a policy as:

$$ 
P(\tau | \pi) = \rho_0(s_0) \prod_{t=0}^{T} \pi(a_t | s_t) P(s_{t+1} | s_t, a_t)
$$

Where $\rho_0(s_0)$ is the distribution of initial states (the probability distribution over possible starting states).

We will always work with discounted rewards, where future rewards are worth less than immediate rewards. The return of a trajectory is defined as the sum of discounted rewards:

$$
R(\tau) = \sum_{t=0}^{T} \gamma^t r(s_t, a_t)
$$

This is helpful not only for mathematical convergence (ensuring the sum is finite when $T \to \infty$), but also because in many real-world scenarios, immediate rewards are more valuable than future rewards. The discount factor $\gamma$ (where $0 \leq \gamma < 1$) controls how much future rewards are discounted. A $\gamma$ close to 1 means future rewards are valued almost as much as immediate rewards, while a $\gamma$ close to 0 means only immediate rewards matter. 