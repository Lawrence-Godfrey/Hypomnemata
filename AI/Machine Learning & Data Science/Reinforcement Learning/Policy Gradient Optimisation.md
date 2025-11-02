Imagine that we have a policy $\pi_\theta(a|s)$ parameterised by $\theta$.
We want to change the parameters of the policy such that we maximise the expected return $J(\pi_\theta)$ when using the policy. 
That is, we want to maximise:
$$
J(\pi_\theta) = \mathbb{E}_{\tau \sim \pi_\theta}[R(\tau)]
$$

When we have a deep neural network, our goal is to change the parameters of the network iteratively such that we maximise a loss function. 

This is a typical use case for Stochastic Gradient Descent (SGD). In our case we want to maximise a function:

$$
\theta_{k+1} = \theta_k + \alpha \nabla_\theta J(\pi_\theta) \big|_{\theta=\theta_k} 
$$

The gradient of the policy is known as the **policy gradient** and the methods that use this gradient to update the policy parameters are known as **policy gradient methods**.

The problem is that to calculate the policy gradient, we need to evaluate it over all possible trajectories, which is computationally intractable unless we have a very small state space. 

There are two main ways to estimate the policy gradient: 
1. **[[REINFORCE]] algorithm**: This is a Monte Carlo method that estimates the policy gradient using complete trajectories sampled from the policy.
2. **Actor-Critic methods**: These methods use a value function (the critic) to estimate the expected return, which reduces the variance of the policy gradient estimate. The actor updates the policy parameters using the critic's estimates. The gradient is estimated as:


