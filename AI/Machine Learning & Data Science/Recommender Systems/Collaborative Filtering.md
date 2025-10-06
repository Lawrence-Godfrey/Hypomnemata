Collaborative Filtering is one of the most commonly used techniques in recommender systems and focuses on finding patterns in user-item interactions rather than using feature-based representations of items or users. The main idea is that users who have agreed in the past tend to agree again in the future.

The idea is to initialise your user parameters and item features randomly, and then minimise the cost function with respect to both your parameters and features. The intuition behind this is that users who rate the same items similarly will probably continue to do so.
## Advantages
- **Highly Personalised**: Recommendations are tailored based on user interactions.
- **No Need for Feature Engineering**: Collaborative filtering doesn't require item or user features.
## Disadvantages
- **Cold Start**: Struggles to recommend items to new users or to recommend new items that have not been interacted with.
- **Scalability**: Calculating similarities can be computationally expensive for large datasets.
