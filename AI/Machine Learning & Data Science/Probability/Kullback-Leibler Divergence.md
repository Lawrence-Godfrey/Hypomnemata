**Kullback-Leibler (KL) Divergence**, also known as **relative entropy**, is a measure of how one probability distribution is different from a second, reference probability distribution. It originated in information theory, but it is now a cornerstone concept in machine learning for measuring the distance between probability distributions.
### The Intuitive Idea
Imagine you have a "true" distribution, $P$, that perfectly describes some data. You then create a model that generates an "approximating" distribution, $Q$. KL Divergence quantifies the "information loss" or "surprise" you experience when you use your approximation $Q$ instead of the true distribution $P$.
-   If $Q$ is a perfect approximation of $P$, the KL Divergence is **0**.
-   The more $Q$ differs from $P$, the higher the KL Divergence.

It's important to note that KL Divergence is **not a true [[Definition of a Metric|distance metric]]** because it is **asymmetric**:
$$D_{KL}(P || Q) \neq D_{KL}(Q || P)$$
The divergence of $Q$ from $P$ is not the same as the divergence of $P$ from $Q$.

![[Pasted image 20251012191751.png]]
### The Formula
For discrete probability distributions $P$ and $Q$, the KL Divergence of $Q$ from $P$ is defined as:
$$
D_{KL}(P || Q) = \sum_{x \in \mathcal{X}} P(x) \log\left(\frac{P(x)}{Q(x)}\right)
$$
Let's break this down:
-   The sum is over all possible events $x$.
-   $P(x)$ is the true probability of event $x$.
-   $Q(x)$ is the probability of event $x$ according to your model.
-   $\frac{P(x)}{Q(x)}$: This ratio is key. If your model $Q$ assigns a lower probability to an event than the true distribution $P$, this ratio will be large, and the log of it will contribute a large amount to the divergence.
### Relationship with Cross-Entropy
The KL Divergence formula can be rewritten to reveal its close relationship with [[Loss Functions|Cross-Entropy]]:
$$
D_{KL}(P || Q) = \sum P(x) \log(P(x)) - \sum P(x) \log(Q(x))
$$
$$
D_{KL}(P || Q) = -H(P) + H(P, Q)
$$

Where:
-   $H(P)$ is the **entropy** of the true distribution $P$.
-   $H(P, Q)$ is the **cross-entropy** between $P$ and $Q$.

In many machine learning applications, the true distribution $P$ is fixed (it's the ground truth from the dataset). This means its entropy, $H(P)$, is a constant. Therefore, **minimising the KL Divergence between your model's predictions $Q$ and the true data $P$ is equivalent to minimising the cross-entropy between them.** This is why cross-entropy is such a common loss function for classification tasks.
## Applications in Machine Learning
1.  **Loss Functions:** As explained above, minimising KL Divergence is often the goal in classification models, which is achieved by minimising the cross-entropy loss.
2.  **Variational Autoencoders (VAEs):** VAEs use KL Divergence in their loss function to force the learned latent space (the encoded representation) to follow a simple distribution, like a standard [[AI/Machine Learning & Data Science/Probability/Distributions/Normal Distribution|normal distribution]]. This regularises the model and ensures the latent space is smooth and well-structured.
3.  **Reinforcement Learning:** Some advanced RL algorithms use KL Divergence to constrain policy updates, ensuring that the new policy doesn't stray too far from the old one in a single update step, which helps to stabilise training.
