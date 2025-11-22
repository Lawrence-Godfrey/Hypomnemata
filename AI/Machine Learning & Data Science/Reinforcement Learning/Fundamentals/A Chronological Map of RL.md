## 1933-1952: Multi-Armed Bandits
- **1933**: [[Thompson Sampling]] was introduced by William R. Thompson as a heuristic for choosing between medical treatments.
   - Addressed the exploration-exploitation dilemma: how to balance trying new treatments (exploration) whilst favouring treatments that appear effective (exploitation).
   - Used Bayesian inference to sample from posterior distributions.
   - Theoretical guarantees for its performance were not established until decades later.
   - (["On the likelihood that one unknown probability exceeds another in view of the evidence of two samples", Thompson, 1933](https://doi.org/10.1093/biomet/25.3-4.285))

- **1952**: Herbert Robbins formally introduced the multi-armed bandit problem as a mathematical framework for sequential decision-making under uncertainty.
   - Modelled scenarios like clinical trials where resources must be allocated efficiently across competing options with unknown rewards.
   - The challenge was balancing learning which options are best with exploiting current knowledge.
   - (["Some aspects of the sequential design of experiments", Robbins, 1952](https://doi.org/10.1090/S0002-9904-1952-09620-8))

- **2002**: [[Upper Confidence Bound (UCB)|UCB]] algorithms and EXP3 provided the first provable regret bounds for bandit problems.
   - Solved the issue of theoretical guarantees that plagued earlier methods.
   - (["Finite-time analysis of the multiarmed bandit problem", Auer et al., 2002](https://homes.di.unimi.it/~cesabian/Pubblicazioni/ml-02.pdf))

## 1950s: Mathematical Foundations

- **1957**: Richard [[Bellman Equation|Bellman]] introduced dynamic programming and formalised [[Markov Decision Processes]] (MDPs) as the mathematical framework for sequential decision-making.
   - Addressed how to find optimal policies for problems where an agent's current state fully determines future possibilities (the Markov property).
   - Bellman's principle of optimality and the Bellman equations provided a way to break down complex sequential decisions into recursive sub-problems.
   - Primary limitation was computational: solving Bellman equations exactly required knowing the full model (transition probabilities and rewards) and was tractable only for small state spaces.
   - (["Dynamic Programming", Bellman, 1957](https://press.princeton.edu/books/paperback/9780691146683/dynamic-programming))

## 1980s: Learning Without Models

- **1988**: [[Temporal Difference Error|Temporal Difference]] (TD) learning was introduced by Richard Sutton, bridging Monte Carlo and dynamic programming methods.
   - Addressed a critical limitation of previous methods: the ability to learn from incomplete episodes without waiting for final outcomes.
   - Enabled learning by bootstrapping from current estimates (like dynamic programming) whilst working without a model of the environment (like Monte Carlo).
   - TD(λ) unified these approaches but struggled with theoretical convergence guarantees and could be unstable with function approximation.
   - (["Learning to predict by the methods of temporal differences", Sutton, 1988](https://link.springer.com/article/10.1007/BF00115009))

## Late 1980s-1990s: Model-Free Control

- **1989**: Q-learning was developed by Chris Watkins in his PhD thesis, providing the first model-free algorithm guaranteed to converge to optimal policies in tabular settings.
   - Solved the credit assignment problem by learning action-value functions (Q-values) directly from experience.
   - Was off-policy (learning about the optimal policy whilst following an exploratory policy), making it sample-efficient.
   - Required tabular representations, limiting it to small, discrete state-action spaces, and convergence could be slow.
   - (["Learning from delayed rewards", Watkins, 1989](http://www.cs.rhul.ac.uk/~chrisw/new_thesis.pdf))

- **1994**: SARSA (State-Action-Reward-State-Action) was introduced by Rummery and Niranjan as an on-policy alternative to Q-learning.
   - Unlike Q-learning, SARSA learned about the policy it was actually following, making it more conservative and better suited for safety-critical applications.
   - The trade-off was that it could be less sample-efficient than Q-learning and couldn't learn optimal policies whilst behaving sub-optimally.
   - (["On-line Q-learning using connectionist systems", Rummery & Niranjan, 1994](https://www.researchgate.net/publication/2500611_On-Line_Q-Learning_Using_Connectionist_Systems))

## 1990s: Direct Policy Optimisation

- **1992**: [[REINFORCE]] was introduced by Ronald Williams as the first practical [[Policy Gradient Optimisation|policy gradient]] method.
   - Addressed a fundamental limitation of value-based methods: the ability to handle continuous action spaces and stochastic policies directly.
   - Optimised policies by following the gradient of expected returns, using the log-likelihood trick to estimate gradients from samples.
   - Major problem was high variance in gradient estimates, requiring many samples and making learning slow and unstable.
   - (["Simple statistical gradient-following algorithms for connectionist reinforcement learning", Williams, 1992](https://link.springer.com/article/10.1007/BF00992696))

- **1999**: [[Actor-Critic Methods]] were formalised by Konda and Tsitsiklis, combining value-based and policy-based approaches.
   - The critic learned a value function to reduce the variance of policy gradient estimates, whilst the actor updated the policy.
   - Addressed REINFORCE's high variance problem but introduced the complexity of learning two interacting components and challenges in balancing their learning rates.
   - (["Actor-critic algorithms", Konda & Tsitsiklis, 1999](https://proceedings.neurips.cc/paper/1999/hash/6449f44a102fde848669bdd9eb6b76fa-Abstract.html))

## 1990s-2015: Stable Policy Updates

- **1998**: Shun-Ichi Amari's work on natural gradients was applied to policy optimisation.
   - Addressed the problem that standard gradient descent treats all parameter changes equally, even though some directions in parameter space have larger effects on the policy distribution.
   - Natural gradients account for the geometry of the policy space by using the Fisher information matrix.

- **2002**: Sham Kakade introduced natural policy gradients specifically for RL.
   - Provided theoretical justification for more stable policy updates.
   - Computing the natural gradient was expensive, requiring second-order information.
   - (["A natural policy gradient", Kakade, 2001](https://repository.upenn.edu/statistics_papers/471/); ["Approximately optimal approximate reinforcement learning", Kakade & Langford, 2002](https://people.eecs.berkeley.edu/~pabbeel/cs287-fa09/readings/KakadeLangford-icml2002.pdf))

- **2015**: [[TRPO]] (Trust Region Policy Optimisation) by Schulman et al. made natural policy gradients practical.
   - Constrained policy updates to a trust region, preventing catastrophically large updates that could collapse performance.
   - Used for continuous control tasks like robotic locomotion.
   - Main limitation was computational cost due to conjugate gradient methods and line searches.
   - (["Trust region policy optimization", Schulman et al., 2015](https://arxiv.org/abs/1502.05477))

## 2013-2015: Deep Reinforcement Learning Breakthrough

- **2013**: DeepMind's initial DQN (Deep Q-Network) work demonstrated that neural networks could learn to play Atari games from raw pixel inputs.
   - Combined Q-learning with deep learning.
   - Addressed the limitation of tabular methods by using function approximation to handle high-dimensional state spaces.
   - (["Playing Atari with deep reinforcement learning", Mnih et al., 2013](https://arxiv.org/abs/1312.5602))

- **2015**: The Nature paper on DQN introduced experience replay and target networks.
   - Experience replay: storing and reusing past transitions.
   - Target networks: stabilising learning by fixing the target Q-values.
   - Solved the instability problems that had plagued neural network-based RL for decades.
   - DQN achieved human-level performance on many Atari games.
   - Limited to discrete action spaces and could be sample-inefficient, requiring millions of environment interactions.
   - (["Human-level control through deep reinforcement learning", Mnih et al., 2015](https://www.nature.com/articles/nature14236))

## 2015-2017: Scaling On-Policy Methods

- **2016**: A3C (Asynchronous Advantage Actor-Critic) by Mnih et al. parallelised actor-critic learning across multiple CPU threads.
   - Each thread had its own environment copy.
   - Addressed the sample efficiency problem by gathering experience faster and stabilised learning through decorrelated updates.
   - Used for both discrete and continuous control tasks but still required substantial computational resources.
   - (["Asynchronous methods for deep reinforcement learning", Mnih et al., 2016](https://arxiv.org/abs/1602.01783))

- **2017**: [[PPO]] (Proximal Policy Optimisation) by Schulman et al. simplified TRPO.
   - Used a clipped objective function instead of constrained optimisation, achieving similar stability with much simpler implementation.
   - Became the workhorse algorithm for continuous control in robotics and was later crucial for [[RLHF]].
   - Main limitation was still requiring substantial on-policy samples, making it less sample-efficient than off-policy methods.
   - (["Proximal policy optimization algorithms", Schulman et al., 2017](https://arxiv.org/abs/1707.06347))

## 2015-2018: Continuous Control and Off-Policy Deep Learning

- **2015**: DDPG (Deep Deterministic Policy Gradient) by Lillicrap et al. extended DQN to continuous action spaces.
   - Combined actor-critic methods with the DQN stability tricks (experience replay and target networks).
   - Designed for continuous control tasks like robotic manipulation.
   - Was brittle, sensitive to hyperparameters, and could be unstable during training.
   - (["Continuous control with deep reinforcement learning", Lillicrap et al., 2015](https://arxiv.org/abs/1509.02971))

- **2018**: SAC (Soft Actor-Critic) by Haarnoja et al. addressed DDPG's brittleness.
   - Incorporated maximum entropy RL, which encourages exploration by maximising both expected return and policy entropy.
   - Was more stable and sample-efficient than DDPG, becoming the go-to algorithm for continuous control.
   - (["Soft actor-critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor", Haarnoja et al., 2018](https://arxiv.org/abs/1801.01290))

- **2018**: TD3 (Twin Delayed DDPG) by Fujimoto et al. also improved DDPG.
   - Used clipped double Q-learning and delayed policy updates.
   - Addressed function approximation errors that lead to overestimated value estimates.
   - (["Addressing function approximation error in actor-critic methods", Fujimoto et al., 2018](https://arxiv.org/abs/1802.09477))

## 2017-2022: Learning from Human Preferences

- **2017**: Christiano et al. introduced deep [[RLHF|reinforcement learning from human feedback]].
   - Addressed the challenge of specifying reward functions for complex tasks.
   - Instead of hand-crafting rewards, humans provided pairwise preferences between trajectory segments, and a reward model was learned from these comparisons.
   - Initially used for simulated robotics tasks but showed that RL could optimise for subjective human preferences.
   - (["Deep reinforcement learning from human preferences", Christiano et al., 2017](https://arxiv.org/abs/1706.03741))

- **2022**: OpenAI applied RLHF to language models, creating InstructGPT and subsequently ChatGPT.
   - Solved the alignment problem of making large language models follow instructions and avoid harmful outputs.
   - The approach fine-tuned pre-trained models using supervised learning on demonstrations, then used PPO to optimise against a reward model trained on human preferences.
   - Key challenges included the cost of human feedback, reward model accuracy, and maintaining model capabilities whilst aligning behaviour.
   - (["Training language models to follow instructions with human feedback", Ouyang et al., 2022](https://arxiv.org/abs/2203.02155))

## 2024: Memory-Efficient Policy Optimisation for LLMs

- **2024**: GRPO (Group Relative Policy Optimisation) was introduced by DeepSeek-AI as a memory-efficient alternative to PPO for training large language models.
   - Addressed PPO's substantial memory overhead by eliminating the value network (critic) entirely.
   - Used group-based advantage estimation where multiple responses are generated for each prompt and their mean reward serves as the baseline.
   - Reduced memory consumption whilst maintaining stable policy updates, making it practical for fine-tuning very large language models on mathematical reasoning and other complex tasks.
   - Successfully applied in DeepSeek-Math and later in DeepSeek-R1, demonstrating that strong reasoning capabilities can emerge from outcome-based RL optimisation.
   - Has since been adopted by other teams (e.g., Qwen) and spawned variants like TR-GRPO (Token-Regulated GRPO) for enhanced stability.
   - (["DeepSeekMath: Pushing the limits of mathematical reasoning in open language models", DeepSeek-AI et al., 2024](https://arxiv.org/abs/2402.03300))

