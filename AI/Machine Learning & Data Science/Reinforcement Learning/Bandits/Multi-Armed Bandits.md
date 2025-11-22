You have **K arms** (actions).  
Each arm _i_ has an **unknown reward distribution** with mean reward:
$$μ_i = E[r | choose arm i]$$
Your goal over **T rounds** is to maximise total reward (or equivalently, minimise regret).
### Regret
The standard metric is **regret**:
$$R_T = T * μ* - Σ_{t=1}^T μ_{a_t}$$
where
- $μ*$ = reward of the best arm,
- $a_t$ = arm chosen at round $t$.

So regret measures how much you lost compared to an oracle who always picked the best arm.
## Practical Notes
- **Stationarity matters**:  
	- Classic MAB assumes fixed reward distributions. If your environment is drifting (e.g. user behaviour), use _non-stationary bandits_ (e.g. sliding-window UCB, discounted Thompson sampling).
- **Contextual bandits are often what you need**:  
	- Real-world applications (ads, recommendations, personalisation) rarely operate in a pure MAB setting. Instead, you have context (user features, time of day, etc.). [[Contextual bandits]] extend MAB by conditioning reward models on features.
- **Batching & delayed feedback**:  
	- In production (e.g. online ads), you often log batches of outcomes and only see delayed feedback. Algorithms need to be adapted (e.g. batched Thompson sampling).
- **Offline evaluation is hard**:  
	- Because you only observe rewards for the arms you pulled, counterfactual evaluation is tricky. Common solutions:
	    - Inverse propensity scoring (IPS).
	    - Off-policy evaluation techniques.
- **Exploration budget**:  
	- Companies sometimes limit how much exploration is allowed (e.g. don’t want to serve too many bad ads). Algorithms like _ε-decay_ or _safe exploration_ (optimism + constraints) help.
- **Scaling to large action spaces**:  
    If K is huge (like 1M products), you can’t treat each arm independently. Solutions:
    - Contextual bandits with embeddings.
    - Clustering arms.
    - Generalisation across arms using shared models.

