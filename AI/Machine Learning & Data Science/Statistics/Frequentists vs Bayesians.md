Frequentists and [[AI/Machine Learning & Data Science/Probability/Bayes' Rule|Bayesians]] represents two broad philosophies within statistics that differ primarily in how they interpret the concept of probability. Frequentists interpret probability as the long-run frequency of events, while Bayesians view it as a measure of belief or confidence in the occurrence of an event.
## Frequentists
1. **Definition of Probability**:
	- Probability is the long-run frequency of events. It is an objective property of the physical world.
    - For example, if a coin is flipped many times, the probability of landing heads is the proportion of heads in a large number of flips.
2. **Parameters**:
    - Parameters are fixed but unknown quantities. They do not have distributions.
    - The goal is to estimate these parameters using data, often through methods like [[Maximum Likelihood Estimation]].
3. **Hypothesis Testing**:
    - Relies on [[p-values]], [[AI/Machine Learning & Data Science/Probability/Confidence Intervals|Confidence Intervals]], and [[significance tests]].
    - A hypothesis is either rejected or not rejected based on the probability of observing the data if the null hypothesis is true.
4. **Interpretation**:
    - A 95% confidence interval means that if we were to repeat the experiment many times, 95% of the intervals would contain the true parameter.
    - P-values indicate the probability of obtaining a result as extreme as, or more extreme than, the observed result under the null hypothesis.
## Bayesians
1. **Definition of Probability**:
    - Probability is a measure of belief or certainty about an event. It is subjective and can vary from person to person.
    - Probability is updated as new information becomes available.
2. **Parameters**:
    - Parameters are treated as [[AI/Machine Learning & Data Science/Probability/Random Variables|Random Variables]] with their own distributions (prior distributions).
    - The goal is to update the belief about these parameters using data, resulting in a posterior distribution.
3. **Hypothesis Testing**:
    - Uses [[AI/Machine Learning & Data Science/Probability/Bayes' Rule|Bayes' Rule]] to update the probability of a hypothesis based on observed data.
    - Hypotheses are evaluated by comparing their posterior probabilities.
4. **Interpretation**:
    - A [[credible interval]] (analogous to a confidence interval) gives a range of values within which the parameter lies with a certain probability.
    - Posterior probabilities provide a direct measure of the plausibility of a hypothesis given the data.

The Bayesian approach can be good if you have limited data, but some prior distribution of the data. However, if this prior is incorrect, your result will be incorrect. The frequentist approach can be good if you have a lot of data, but no prior understanding of the distribution of the data. 