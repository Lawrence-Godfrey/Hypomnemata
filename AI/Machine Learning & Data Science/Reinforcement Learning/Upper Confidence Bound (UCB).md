A core [[Multi-Armed Bandits]] algorithm, probably the most widely used.

## Algorithm
- For each arm i, estimate mean reward plus an uncertainty bonus:
$$UCB_i(t) = μ̂_i + sqrt((2 ln t) / n_i)$$
where $n_i$ = times arm i has been pulled.

- Always pick the arm with the highest UCB.
- Exploration happens naturally because under-explored arms have high uncertainty terms.    
- **Good theoretical guarantees**: regret ~ $O(log T)$.

