**Ordinary Least Squares (OLS)** is the most common method used to estimate the parameters of a [[AI/Machine Learning & Data Science/Supervised Learning/Linear Regression|Linear Regression]] model. It's a fundamental technique in statistics and machine learning for modeling the relationship between a dependent variable and one or more independent variables.

The core idea of OLS is simple: find the line (or hyperplane in multiple dimensions) that **minimises the sum of the squared differences** between the observed values and the values predicted by the linear model.
## Minimising Residuals
Imagine a scatter plot of data points. We want to draw a straight line that best fits the data. For any given line, we can measure the vertical distance from each data point to the line. This distance is called a **residual** or an **error**.
-   A positive residual means the data point is above the line.
-   A negative residual means the data point is below the line.

To find the "best" line, we can't just sum up the residuals, because the positive and negative errors would cancel each other out. Instead, OLS squares each residual and then sums them up.

**The objective of OLS is to find the model parameters (the slope and intercept) that result in the smallest possible Sum of Squared Residuals (SSR).**

$$
\text{SSR} = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

Where:
-   $y_i$ is the actual observed value for the *i*-th data point.
-   $\hat{y}_i$ is the value predicted by the regression line for the *i*-th data point.
-   $(y_i - \hat{y}_i)$ is the residual for the *i*-th data point.


![[Pasted image 20251012184043.png]]

## The Normal Equation
For a linear regression model of the form $Y = X\beta + \epsilon$, the OLS estimate for the coefficient vector $\beta$ can be found analytically using a formula known as the **Normal Equation**:

$$
\hat{\beta} = (X^T X)^{-1} X^T Y
$$

-   $\hat{\beta}$: The vector of estimated coefficients (e.g., slope and intercept).
-   $X$: The matrix of independent variables (with a column of ones for the intercept).
-   $Y$: The vector of the dependent variable.

This equation provides a closed-form solution, meaning we can calculate the optimal coefficients directly from the data without needing an iterative optimisation process like [[Gradient Descent]].
### Assumptions of OLS
For the results of OLS regression to be reliable and for the coefficients to be the Best Linear Unbiased Estimators (BLUE), the [[Gauss-Markov Theorem|Gauss-Markov assumptions]] must be met.


