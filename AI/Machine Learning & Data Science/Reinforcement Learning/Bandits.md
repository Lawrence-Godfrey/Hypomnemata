In reinforcement learning, **bandits** (short for _multi-armed bandits_) are the simplest possible setting for sequential decision-making under uncertainty.

The idea comes from a gambler at a row of slot machines (“one-armed bandits”). Each machine (or “arm”) has an unknown probability distribution of rewards. The gambler’s task is to decide which machine to pull each turn, in order to maximise cumulative reward over time.

![[Pasted image 20250928091600.png | center]]

### Core characteristics of bandits:
- **No state transitions**: Unlike general RL, bandits don’t have environments with states that evolve. Every round is independent.
- **Arms (actions)**: Each action has a fixed but unknown reward distribution.
- **Objective**: Learn to choose arms that maximise total expected reward (or minimise regret).
- **Exploration vs. exploitation**: The central challenge. You must:
    - _Explore_ to learn which arms are good.
    - _Exploit_ by repeatedly pulling the best arm once you’ve learned it.
### Variants:
1. [[Multi-Armed Bandits]]: Finite set of arms, stationary reward distributions.
2. [[Contextual bandits]]: You observe some context (features) before choosing an arm. This is like supervised learning with a feedback limitation—you only see the reward for the action you picked.
3. **Non-stationary bandits**: Reward distributions change over time, so you must keep adapting.