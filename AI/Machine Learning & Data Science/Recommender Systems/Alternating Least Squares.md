Alternating Least Squares (ALS) is an optimisation algorithm commonly used for matrix factorisation in [[Collaborative Filtering]] recommender systems. ALS decomposes a user-item rating matrix into two lower-dimensional matrices representing user and item features, enabling predictions for missing ratings.
## How ALS Works
ALS solves the matrix factorisation problem by alternating between optimising user features and item features:
- Decompose rating matrix $R$ (users × items) into $U$ (users × factors) and $V$ (items × factors) such that $R ≈ UV^T$
- **Alternating Optimisation**: 
	- Fix $V$, solve for $U$ using least squares
	- Fix $U$, solve for $V$ using least squares  
	- Repeat until convergence
- **Least Squares Solution**: Each step has a closed-form solution, making it computationally efficient

![[Pasted image 20251006075106.png]]

## Mathematical Formulation
The objective function minimises:
$$J = \sum_{(i,j) \in observed} (r_{ij} - u_i^T v_j)^2 + \lambda(\sum_i ||u_i||^2 + \sum_j ||v_j||^2)$$

Where:
- $r_{ij}$ = observed rating from user $i$ for item $j$
- $u_i$ = feature vector for user $i$
- $v_j$ = feature vector for item $j$  
- $\lambda$ = regularisation parameter
## Key Properties
- **Handles Sparsity**: Works well with sparse rating matrices (most entries missing)
- **Scalable**: Can be parallelised across users/items during alternating steps
- **Regularised**: Built-in regularisation prevents overfitting
- **Non-convex**: Overall problem is non-convex but each alternating step is convex
## Simple Worked Example
Consider a 3×3 rating matrix with 2 latent factors:

**Original Rating Matrix R:**
```
     Item1  Item2  Item3
User1   5     3     ?
User2   4     ?     1  
User3   ?     2     5
```

**Step 1**: Initialise $U$ and $V$ randomly (rows=number of users/items, columns=latent factors)
```
U = [[0.1, 0.2],    V = [[0.3, 0.1],
     [0.3, 0.1],         [0.2, 0.4], 
     [0.2, 0.4]]         [0.1, 0.3]]
```

**Step 2**: Fix $V$, solve for $U$ using least squares for each user:
- For User1: Minimise $(5 - u_1^T v_1)^2 + (3 - u_1^T v_2)^2 + \lambda||u_1||^2$
- This is the equivalent of solving $u_1 = (V_{observed}^T V_{observed} + \lambda I)^{-1} V_{observed}^T r_1$ 
	- Where $V_{observed} = \begin{bmatrix} 0.3 & 0.1 \\ 0.2 & 0.4 \end{bmatrix}$ (items 1&2 that User1 rated) and $r_1 = \begin{bmatrix} 5 \\ 3 \end{bmatrix}$
**Step 3**: Fix updated $U$, solve for $V$ using least squares for each item

**Step 4**: Repeat until convergence

**Final Prediction**: Missing rating = $u_1^T v_3$ (User1, Item3)
