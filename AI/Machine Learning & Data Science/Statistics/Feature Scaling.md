Feature scaling is a technique used to normalise the range of the values of features in a dataset, which ensures that each feature contributes equally to the computation of the objective function. 

## Min-Max Scaling
Scale each feature to a given range, typically $[0, 1]$ or $[-1, 1]$ if negative values are present in the feature.
$$X_{scaled}= \frac{X - X_{min}}{X_{max}- X_{min}}$$
where 
 - $X$ is the original feature vector.
 - $X_{min}$ and $X_{max}$ are vectors of the min and max values of each feature.

## Mean Normalisation
Transforms features to have zero mean.
$$X_{scaled}= \frac{X - \mu}{X_{max}- X_{min}}$$
## Matrix Form
If you want to perform this scaling on the entire dataset at once, i.e., your $X$ is an $m\times n$ matrix where $m$ is the number of samples and $n$ is the number of features, then $X_{min}$ and $X_{max}$ need to be $m \times n$ matrices as well, where the columns will be the same min or max value repeated for a particular feature, and the rows will represent the different min/max values for the different features.
This matrix can be obtained by multiplying the transpose of $X_{min}$ or $X_{max}$ by a column vector of ones $1_m$, for example:
$$1_{n}X^T_{min}$$

## Standardisation
Standardisation, often implemented as `StandardScaler` in libraries like Scikit-learn, rescales features to have a mean of 0 and a standard deviation of 1. This is also known as Z-score normalisation.

$$X_{scaled} = \frac{X - \mu}{\sigma}$$

Where:
-   $\mu$ is the mean of the feature values.
-   $\sigma$ is the standard deviation of the feature values.

**Worked Example:**
Consider a feature with values `[1, 2, 3, 4, 5]`.
-   Mean ($\mu$) = 3
-   Standard Deviation ($\sigma$) ≈ 1.414
-   Scaled values: `[-1.414, -0.707, 0, 0.707, 1.414]`

Useful for algorithms that assume zero-centered or normally distributed data, like PCA, Linear Regression, and Logistic Regression. It's crucial for algorithms that rely on Euclidean distance.
## Normalisation
Normalisation, implemented as `Normalizer`, works differently to standardisation. Instead of scaling each feature (column) independently, it scales each **sample** (row) so that it has a unit norm. The most common norm is the L2 norm (Euclidean length).

$$X_{normalized\_row} = \frac{X_{row}}{\|X_{row}\|_2}$$

Where $\|X_{row}\|_2$ is the Euclidean length (L2 norm) of a single row (sample).

**Worked Example:**
Consider a single sample (row) with features `[3, 4]`.
-   L2 norm = $\sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$
-   Normalized values: `[3/5, 4/5]` = `[0.6, 0.8]`
-   The new L2 norm is $\sqrt{0.6^2 + 0.8^2} = \sqrt{0.36 + 0.64} = \sqrt{1} = 1$.

Useful when the direction of the data vector matters more than its magnitude. Common in text classification and clustering where **Cosine Similarity** is the distance metric.

![[Pasted image 20251010171830.png]]
## Impact on Distance Metrics
How you scale your data has significant implications for distance calculations, which are at the heart of many ML algorithms (like k-NN, SVM, and clustering).
-   **Euclidean Distance:** This metric is sensitive to the scale of the features. If one feature has a much larger range than others (e.g., salary vs. age), it will dominate the distance calculation.
    -   **`StandardScaler` is essential here.** By putting all features on the same scale, it ensures that each feature contributes equally to the Euclidean distance.
-   **Cosine Similarity:** This metric measures the cosine of the angle between two vectors, effectively judging their orientation, not their magnitude.
    -   **`Normalizer` is designed for this.** It scales all sample vectors to have a length of 1, placing them on the surface of a unit hypersphere. When vectors have a unit norm, cosine similarity and Euclidean distance have a direct relationship ($d^2 = 2(1 - \cos(\theta))$), and algorithms that use Euclidean distance will effectively be optimising for angular separation.
