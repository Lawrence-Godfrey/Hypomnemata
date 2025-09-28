One of the most basic [[Multi-Armed Bandits]] algorithms. 
## Algorithm
- With prob. ε, choose a random arm (exploration).
- With prob. 1 - ε, choose the arm with the highest estimated mean (exploitation).
- Simple, but wasteful exploration since it doesn’t focus on promising arms.

