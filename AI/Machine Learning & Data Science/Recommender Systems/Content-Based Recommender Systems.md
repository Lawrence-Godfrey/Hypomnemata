Content-based recommender systems provide personalised recommendations by leveraging features of the items themselves, as well as the interactions or preferences of the users with those items.

Each user has a "profile", i.e., a set of parameters $\theta^j$ and each item has a feature vector $x^i$. Some users have rated some items. $r(i,j) = 1$ if user $j$ has rated item $i$. A prediction can then be made on item $i$ by user $j$: $$p = (\theta^{j})^{T}(x^{i})$$The intuition here is that $\theta^{j}$ has been learnt so that the features of the item which the user prefers are prioritised.
## Optimisation Objective
To learn the parameters for each user, we want to minimise the cost function $$J(\theta^{j}) = \frac{1}{2}\sum\limits_{i:r(i,j)=1}((\theta^{j})^{T}(x^{i}) - y^{i,j})^2$$
I.e., go through all the items that the user has rated and sum the difference between our prediction and the actual rating. We would need to do this for each user. [[Gradient Descent]] with regularisation can be used to fit the parameters for a particular user.
## Advantages
- **No Cold Start**: Content-based systems do not require other users to have interacted with an item to recommend it.
- **Personalised**: Recommendations are tailored to individual users based on their own behaviour.
## Disadvantages
- **Limited Scope**: Can only recommend items similar to those the user has already interacted with, potentially resulting in a lack of diversity.
- **Feature Engineering**: Requires meaningful feature representation of items, which can be challenging.