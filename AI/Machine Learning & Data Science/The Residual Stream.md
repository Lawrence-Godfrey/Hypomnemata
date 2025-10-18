The **residual stream** (also called the **residual pathway** or **residual connection**) is a core architectural concept in deep learning, especially in **ResNets** and [[Transformer|Transformers]], that allows information to flow **unchanged** across layers.

In a normal neural network layer, you apply a transformation like:
$$x_{l+1} = f(x_l)$$
where $f$ might be something like a linear layer + non-linearity.

A **residual connection** modifies this to:$$x_{l+1} = x_l + f(x_l)$$
Here, the input $x_l$ is added (“residually”) to the output of the transformation.  
The vector being passed forward ($x_l$) is what we call the **residual stream**.
## Why It Matters
Without a residual stream, deep networks can suffer from:
- **Vanishing gradients** — signal fades as it’s backpropagated.
- **Degradation** — adding more layers can actually worsen training loss.

Residual streams fix this by:
- Providing a **direct gradient path** through the identity connection.
- Allowing layers to learn _refinements_ rather than _complete rewrites_ of representations.
## In Transformers
Each transformer layer looks roughly like this:
$$x_{l+1} = x_l + \text{Attention}(x_l) x_{l+2} = x_{l+1} + \text{MLP}(x_{l+1})$$

- The vector $x$ that flows through (before addition) is the **residual stream**.  
- Each sublayer (attention, then feedforward) writes _updates_ into it.

In interpretability work (e.g. [[Anthropic’s Transformer Circuits]]), the residual stream is treated as the **shared representational space** of the model. Every attention head and MLP reads from and writes to this same stream.
## Geometric Intuition
Think of $x$ as a vector in a high-dimensional feature space representing the model’s current “understanding” of the input.

Each layer doesn’t replace this vector, it **nudges it** in directions corresponding to learned features.

So you can think of the residual stream as:
- A **state vector** carrying the model’s evolving representation.
- With each block adding **directional updates**.

