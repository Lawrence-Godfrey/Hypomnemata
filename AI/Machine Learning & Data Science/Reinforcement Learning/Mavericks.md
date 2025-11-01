A "Maverick" agent deliberately pursues atypical exploratory or strategic behaviours that depart from canonical exploitation-exploration schedules to surface hidden reward structure, uncover novel state abstractions, or shift collective dynamics in multi-agent settings.

"Maverick" is not (yet) a standardised formal term in RL literature; we use it as a conceptual lens for studying purposeful deviation from mainstream heuristics when those heuristics underperform in sparse, deceptive, risk-sensitive, or socially coupled environments.
## Motivation
Traditional exploration strategies (see [[ε-Greedy MAB Algorithm]], [[Upper Confidence Bound (UCB)]], [[Thompson Sampling]]) trade off short-term reward accumulation against information gain. In complex domains (long horizons, sparse/delayed rewards, partial observability, nonstationary opponents, coordination demands) conventional schedules can collapse into:
- Premature exploitation (locking into suboptimal basins)
- Myopic uncertainty reduction (ignoring structural novelty)
- Herding in multi-agent systems (agents converge to mutually reinforcing but globally poor equilibria)

A Maverick agent purposefully injects structured atypicality to break those failure modes.
