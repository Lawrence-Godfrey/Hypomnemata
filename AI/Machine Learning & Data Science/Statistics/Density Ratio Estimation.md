# Density Ratio Estimation

**Tags:** #Statistics #MachineLearning #UnsupervisedLearning

**Density Ratio Estimation** is a statistical method used to estimate the ratio of two probability density functions, $p(x)$ and $q(x)$, using only samples drawn from each distribution. The goal is to find a function $r(x)$ that approximates this ratio:

$$
r(x) = \frac{p(x)}{q(x)}
$$

This is a powerful technique in unsupervised machine learning because it allows us to compare and relate two distributions without ever needing to explicitly model or estimate the individual densities $p(x)$ and $q(x)$, which can be a very difficult task, especially in high-dimensional spaces.

### The Core Idea: The "Density Ratio Trick"

The fundamental insight, often called the "density ratio trick," is that many important statistical divergences and measures can be calculated or optimized by using the density ratio, bypassing the need for direct density estimation.

Instead of a two-step process (1. estimate $p(x)$, 2. estimate $q(x)$, 3. compute the ratio), density ratio estimation formulates a single objective function that allows a model to learn the ratio $r(x)$ directly. This is often framed as a binary classification problem where the model tries to distinguish between samples from $p(x)$ and samples from $q(x)$.

### Connection to KL Divergence

Density ratio estimation is deeply connected to the [[Kullback-Leibler Divergence|Kullback-Leibler (KL) Divergence]]. The KL divergence from $q$ to $p$ is defined as:

$$
D_{KL}(p || q) = \int p(x) \log\left(\frac{p(x)}{q(x)}\right) dx = \mathbb{E}_{x \sim p(x)}[\log r(x)]
$$

This equation shows that if we can accurately estimate the density ratio $r(x)$, we can approximate the KL divergence by simply taking the average of the log-ratio over samples drawn from the distribution $p(x)$. This is a key application and one of the primary motivations for developing density ratio estimation techniques.

### Common Methods

Several algorithms have been developed to perform density ratio estimation, including:
-   **KLIEP (Kullback-Leibler Importance Estimation Procedure):** This method directly minimizes the KL divergence to find the optimal density ratio.
-   **Logistic Regression:** A simple probabilistic logistic regression classifier can be trained to distinguish between samples from $p(x)$ (labeled as 1) and $q(x)$ (labeled as 0). The learned odds from this classifier are directly related to the density ratio.
-   **uLSIF (unconstrained Least-Squares Importance Fitting):** This method uses a squared loss objective to match the density ratio, which often has a convenient closed-form solution.

### Applications in Machine Learning

Density ratio estimation is a versatile tool with many applications:
1.  **Covariate Shift Adaptation:** When the training data distribution is different from the test data distribution, density ratios can be used as importance weights to correct the model's learning process.
2.  **Anomaly/Outlier Detection:** If $p(x)$ is the distribution of normal data and $q(x)$ is a new data point, a very high or low density ratio can indicate that the new point is an outlier.
3.  **Mutual Information Estimation:** The mutual information between two variables can be expressed in terms of the ratio between their joint density and the product of their marginal densities.
4.  **Two-Sample Tests:** It can be used to test the hypothesis of whether two sets of samples are drawn from the same distribution.
