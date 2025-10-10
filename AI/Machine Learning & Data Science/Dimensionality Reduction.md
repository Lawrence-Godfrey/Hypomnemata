### Principle Component Analysis (PCA)
**Goal**: Reduce data from $n$ dimensions to $k$ dimensions where $n\gt k$. 
Find $k$ vectors which we can project the data onto to minimise the projection error. 
Can speed up learning and reduce memory requirements.
### PCA is not Linear Regression
![[Pasted image 20230828165021.png | center]]
### Preprocessing
Features should be [[Feature Scaling#Standardisation|standardised]] before running PCA.
### Algorithm
1. Compute "Covariance" matrix $$\Sigma = \frac{1}{m}\sum\limits_{i=1}^{n} (x^{i})(x^i)^{T} $$ where $x^{i}$ is a $n\times 1$ matrix, or simply $$\Sigma = \frac{1}{m}XX^T$$
   **Intuition:** The covariance matrix summarises the relationships between all pairs of features. A large positive value means two features tend to increase together. This matrix mathematically describes the shape and orientation of your data cloud.
2. Compute the eigenvectors of $\Sigma$ (singular value decomposition).
   **Intuition:** The **eigenvectors** are the directions of the axes of your data cloud, ordered by how much they "explain" the data's spread. The first eigenvector points in the direction of maximum variance (the longest axis of the cloud). The second points along the next most important direction, and so on. The **eigenvalues** are simply numbers that tell you *how much* variance is captured by each eigenvector. A high eigenvalue means that axis is very important.
3. Sort the eigenvalues in descending order and rearrange the corresponding eigenvectors. The first principal component corresponds to the eigenvector associated with the largest eigenvalue, the second principal component to the second-largest eigenvalue, and so on.
4. Finally, to transform the original data into the new $k$-dimensional space, use $$X_{new}= XW$$ where $W$ are the chosen eigenvectors.
### Choosing $k$
Choose $k$ to be the smallest value so that 99% of variance is maintained, i.e., the average squared projection error over the total variation in data is $\leq 0.01$ 
### Notes
 - It is possible to reconstruct the data in the original dimensionality if the principle components are kept, although it will obviously be an approximation of the original dataset.
 - PCA should **not** be used to prevent [[Overfitting & Underfitting|overfitting]].
 - Only use PCA if actually needed, not as a standard in your pipeline.
### t-Distributed Stochastic Neighbor Embedding (t-SNE)
- **Non-linear Technique**: t-SNE is a non-linear dimensionality reduction method specifically designed for the visualisation of high-dimensional datasets.
- **Probabilistic Approach**: It works by converting the high-dimensional Euclidean distances between data points into conditional probabilities that represent similarities. The same is done for the low-dimensional counterparts of these data points. The technique then minimizes the divergence between the two distributions using gradient descent.
- **Local Structure**: t-SNE excels at capturing the local structure of the data and revealing clusters. It often produces visually appealing plots where clusters of similar data points are grouped together.
- **Perplexity Parameter**: t-SNE has a tunable parameter called "perplexity," which can have a significant impact on the resulting visualisation. It loosely determines how to balance attention between local and global aspects of the data.
- **Stochastic**: t-SNE is non-deterministic, meaning that running it multiple times on the same data can produce different results. This is because of the random initialisation of the low-dimensional embeddings, though the overall structure should remain similar.
- **Computationally Intensive**: t-SNE can be more computationally demanding than PCA, especially on large datasets.