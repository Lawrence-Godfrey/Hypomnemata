The multivariate Gaussian distribution is a generalisation of the one-dimensional (univariate) [[Normal Distribution]] to higher dimensions. In a multivariate Gaussian distribution, each point in the n-dimensional space is associated with a probability. The distribution is defined by two parameters: a mean vector and a covariance matrix. The mean vector, often represented as μ, is an n-dimensional vector where each element represents the mean of a particular dimension. The covariance matrix, usually denoted as Σ, is an n x n matrix that contains the variances and covariances of the variables in the distribution.

A [[Normal Distribution]] might not work well for certain datasets where the features are not mutually exclusive.
![[Pasted image 20230828172559.png | center]]

Rather model $p(x)$ all at once. $\mu$ is now a matrix in $\mathbb{R}^n$ and $\Sigma$ is a matrix in $\mathbb{R}^{n\times n}$. This automatically captures correlations between features.

#### Notes
 - While labels aren't required to fit a Gaussian model, they are useful for evaluating the performance of the model.
 - If raw dataset is not Gaussian, it can be mapped to a Gaussian distribution![[Pasted image 20230828172228.png | center]]