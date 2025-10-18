In supervised learning, loss functions are used to measure the error or deviation between the predicted output and the actual target output.
### Frobenius Norm
The Frobenius norm of a matrix is a measure of the overall magnitude of the matrix. 
$$
\parallel A \parallel_{F} = \sqrt{\sum\limits_{i=1}^{m}\sum\limits_{j=1}^{n}|a_{ij}|^2}
$$
This can be used to calculate the loss between your training data $X$ and your target output $Y$. For example:
$$
Loss = \parallel X\Theta - Y \parallel_F
$$
Where $\Theta$ are the parameters of your model.
Often the loss will be calculated as the square of the Frobenius norm divided by $m$ (the number of examples) which makes calculating the derivative easier. This doesn't change the outcome when minimising the loss. The derivative of the squared Frobenius norm is then:
$$
\frac{d}{d\Theta}Loss = \frac{2}{m}(X^T(X\Theta - Y))
$$
### Cross-Entropy Loss (aka Categorical Cross-Entropy)
For two discrete probability distributions, $p$ (true distribution) and $q$ (predicted distribution), the cross-entropy is defined as: 
$$L=-∑y_{j}​log(\hat{y}​_j​)$$
Cross-entropy loss is commonly used in classification problems in machine learning, especially in neural networks. The true distribution typically has a probability of 1 for the correct class and 0 for all other classes (in the case of one-hot encoded labels), and the predicted distribution is the model's estimated probabilities for each class. The loss measures how well the predicted probabilities match the true labels. 

This derives from [[AI/Machine Learning & Data Science/Probability/Kullback-Leibler Divergence|KL divergence]], which measures the difference between two probability distributions. The reason we assume probability distributions even if the output of the model is a one-hot vector is because a probabilistic interpretation allows us to quantify the uncertainty of predictions.

This essentially only considers the true label and ignores everything else, which is why it's often paired with Softmax Regression for [[AI/Machine Learning & Data Science/Supervised Learning/Logistic Regression#Multi-class Classification|Multi-class Classification]], since the Softmax function first normalises the results. Without this the single logit corresponding to the true label does not have much meaning.
### Binary Cross-Entropy Loss
Binary cross-entropy loss is used for binary classification problems. 
$$L_{BCE}​=−[ylog(\hat{y}​)+(1−y)log(1−\hat{y}​)]$$
Where:
- $y$ is the true label (0 or 1).
- $\hat{y}$​ is the predicted probability that the sample belongs to class 1.
### Symmetric Cross-Entropy Loss
The normal cross-entropy formula calculates the difference between one distribution relative to another. It is inherently asymmetric, meaning that the order in which you compare two distributions will affect the result. Symmetric cross-entropy , on the other hand, calculates the average of two cross-entropy losses in both directions. This can be useful when you're working with complex models where the relationship between variables isn't strictly unidirectional and it's important to consider the impact of each variable on the other.

$$
H(p, q)_{sym} = \frac{1}{2}(H(p, q) + H(q, p)) = -\frac{1}{2}(\sum\limits_{i}p(i) log q(i) + \sum\limits_{i}q(i) log p(i) )
$$
Where $H(p, q)$ is the cross-entropy of $p$ and $q$, and $H(q, p)$ is the cross-entropy of $q$ and $p$.
### Contrastive Loss
Contrastive loss is used for tasks that involve finding similarity or dissimilarity between two instances, for example, in tasks such as face recognition or signature verification. The main idea behind contrastive loss is to minimise the distance between similar instances and maximise the distance between dissimilar instances.

The formula for contrastive loss is
$$
L = yd^{2} + (1-y)Max(0, m-d)^{2}
$$
Where $y$ is the labelled sample, which will be $1$ for the positive example and $0$ for the negative example. So for a positive example we will only consider the first part of the function, meaning your loss is directly correlated to the square of the Euclidean distance. For a negative sample, the loss is square of the distance from the margin $m$ (a hyperparameter which determines how strictly the model enforces the minimum distance between dissimilar pairs). 

We use a margin in contrastive loss for a few reasons:
1. It enforces a minimum distance for separation, rather than some arbitrary distance.
2. It avoids overfitting by reducing the importance of separating the points by some infinitely scaling distance.
3. Creates stability.
4. Allows for flexibility since you can tweak how strict the model is.
#### The Problem with Contrastive Loss
There is an issue with how contrastive loss works, stemming from the fact that it only considers pairs of samples (not triplets). This creates "hard negatives" and "hard positives" ("hard" meaning difficult) which are samples which, despite being labelled as similar or dissimilar, are far or close to each other in the feature space, making is "hard" for the model to distinguish between the positive and negative samples. [[Loss Functions#Triplet Loss|Triplet Loss]] looks at triplets of samples, which improves upon the issues inherent with contrastive loss.
### Triplet Loss
With triplet loss, you still have an anchor, positive sample and negative sample, but the distance considered is now the difference between the distance to the positive sample and the distance to the negative sample. The loss now prioritises the distance between the positive and negative samples, rather than the distance between the anchor and the positive and negative samples. 

![[Pasted image 20250216113159.png|center]]

The loss function becomes
$$
L = Max(0, d_{AP} - d_{AN} + m)
$$
Where
- $d_{AN}$ is the distance between the anchor and negative sample
- $d_{AP}$ is the distance between the anchor and positive sample
- $m$ is the margin which determines the minimum distance that the positive and negative samples should be from each other. If this distance is more than m, the loss will be 0.
#### Triplet Mining
When using triplets, you increase the size of your dataset substantially and it becomes more important to train on meaningful triplets, since a lot of triplets will already satisfy the margin condition and won't influence the model much. Triplet mining aims to choose hard examples, where the negative is close to the anchor, or where the positive is far from the anchor, etc., making the model more robust while using the data more efficiently. 
