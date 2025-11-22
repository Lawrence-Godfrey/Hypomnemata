A [[Frequentists vs Bayesians|Bayesian]] [[Multi-Armed Bandits]] algorithm.
## Algorithm
 - Maintain a posterior distribution over each arm’s reward.
- At each round, sample a reward estimate from each posterior and pick the arm with the max sample.
- Exploration is automatic: more uncertain arms have more posterior spread, so they’re sampled more often.
- Very strong empirical performance, often better than [[Upper Confidence Bound (UCB)]].

