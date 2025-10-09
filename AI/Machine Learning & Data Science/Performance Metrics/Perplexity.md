# Perplexity

**Tags:** #PerformanceMetric #NLP

Perplexity is the measure of how well a probability distribution or a language model predicts a sample of text. It is one of the most common metrics for evaluating language models.

$$
PP(W) = P(s_{1}, s_{2}, ..., s_{m})^{-\frac{1}{m}}
$$

Where:
-   $W$ is a test set containing $m$ sentences $s$.
-   $s_i$ is the $i$-th sentence in the test set.
-   $m$ is the total number of words in the entire test set $W$.

A lower perplexity score indicates that the language model is better at predicting the sample text. A very accurate model might have a perplexity score close to 1, while a bad model might have a score in the hundreds. Good models often have perplexity scores between 20 and 50.

-   Sometimes **log perplexity** ($logPP$) is used instead.
-   Perplexity should only be used to compare models that have the same vocabulary.
