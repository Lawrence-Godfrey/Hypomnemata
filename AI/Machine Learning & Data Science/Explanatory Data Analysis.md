Exploratory Data Analysis (EDA) is a critical step before you proceed to model building. It helps you understand the structure, trends, and anomalies in the data. Below are common EDA techniques, followed by tips on how to interpret results, which can be particularly useful for multivariate linear regression:
### Common EDA Techniques
1. **Data Summary**
    - Use descriptive statistics (`mean`, `median`, `std`, `min`, `max`, etc.) to summarise each numerical variable.
    - For categorical variables, look at frequency distribution.
2. **Data Cleaning**
    - Check for missing values and decide how to handle them (remove, impute, etc.)
    - Look for outliers and consider removing or transforming them.
3. **Univariate Analysis**
    - Plot histograms or kernel density plots to look at the distribution of each numerical variable.
    - For categorical variables, use bar charts.
4. **Bivariate Analysis**
    - Scatter plots to visualise relationship between numerical variables.
    - Box plots to see how numerical variables are distributed with respect to categories.
    - Correlation matrix to quantitatively check for relationships between numerical variables.
5. **Multivariate Analysis**
    - Pair plots to look at bivariate relationships across multiple numerical variables.
    - Heatmaps to visualise correlations across multiple variables.
6. **Feature Engineering**
    - Create new variables that might better represent the problem you are trying to solve.
