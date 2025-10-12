The **Gauss-Markov Theorem** is a cornerstone theorem in statistics that provides the theoretical justification for using the [[Ordinary Least Squares]] (OLS) method in linear regression.

The theorem states that if a linear regression model satisfies a specific set of assumptions (the "Gauss-Markov assumptions"), then the OLS estimator for the coefficients is the **Best Linear Unbiased Estimator** (BLUE).

Let's break down what "BLUE" means:
- **Best:** This means it has the minimum possible variance among all linear unbiased estimators. In other words, the OLS estimate is the most precise and reliable one you can get.
- **Linear:** The estimator is a linear combination of the observed dependent variable, $y$.
- **Unbiased:** On average, the estimator will equal the true population parameter. It doesn't systematically overestimate or underestimate the true value.

In short, the theorem tells us: "If your model and data meet these conditions, OLS is the best possible linear method you can use."
## The Gauss-Markov Assumptions
For the theorem to hold, the following assumptions about the model and the error term ($\epsilon$) must be met:
1.  **Linearity:** The model is linear in its parameters. $$y = \beta_0 + \beta_1 x_1 + \dots + \beta_p x_p + \epsilon$$
2.  **Random Sampling:** The data is a random sample from the population.
3.  **No Perfect Multicollinearity:** None of the independent variables is a perfect linear function of any other independent variables. The model should not contain redundant information.
4.  **Exogeneity (Zero Conditional Mean):** The error term has an expected value of zero for any given value of the independent variables. This implies that the independent variables are not correlated with the error term. $$E[\epsilon | X] = 0$$
5.  **Homoscedasticity:** The error term has a constant variance for all observations. The spread of the errors does not change as the values of the independent variables change. $$\text{Var}(\epsilon_i) = \sigma^2$$
6.  **No Autocorrelation:** The error terms are uncorrelated with each other. The error for one observation does not provide any information about the error for another observation. $$\text{Cov}(\epsilon_i, \epsilon_j) = 0 \text{ for } i \neq j$$
## What if the Assumptions are Violated?
If these assumptions are not met, the OLS estimator may no longer be BLUE. For example:
-   If **homoscedasticity** is violated (heteroscedasticity), the OLS estimates are still unbiased, but they are no longer "best" (i.e., they don't have the minimum variance). In this case, methods like Weighted Least Squares might be more appropriate.
-   If **exogeneity** is violated, the OLS estimates will be biased and inconsistent.
