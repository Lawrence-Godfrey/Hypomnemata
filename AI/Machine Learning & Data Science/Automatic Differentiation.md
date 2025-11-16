Differentiation is fundamental in science and engineering. In machine learning, we need derivatives when using gradient-based optimisation methods like [[Gradient Descent]], where we attempt to minimise an objective function by repeatedly tuning model parameters in the direction of the negative gradient.

Automatic differentiation (autodiff) is a set of techniques that allow efficient computation of derivatives. Understanding autodiff is helped by contrasting it with other methods of computing derivatives.
## Alternative Approaches to Computing Derivatives
### Manual Differentiation
One approach is to manually differentiate functions using basic derivative rules from calculus, then code up the result. However, this becomes tedious for complicated functions and isn't automated.

![[Pasted image 20251115162314.png]]
### Numerical Differentiation
Numerical differentiation uses the method of finite differences to approximate derivatives. The simplest version follows from the limit definition of the derivative.

For a scalar-valued function $f$, the partial derivative with respect to $x_i$ is approximated by:
$$\frac{\partial f}{\partial x_i} \approx \frac{f(x + he_i) - f(x)}{h}$$
where $e_i$ is the unit vector along the $i$-axis and $h$ is a small step size.
#### Issues with Numerical Differentiation
1. **Truncation Error:** We're approximating a limit as $h \to 0$ using a non-zero $h$. We're calculating the slope of a secant line near the tangent line at $x$. As $h$ approaches zero, truncation error decreases.
2. **Rounding Error:** As $h$ gets very small, limited precision of floating-point arithmetic introduces rounding error. There's a careful trade-off between truncation and rounding when selecting step size.
3. **Time Complexity:** We need $O(n)$ evaluations for an $n$-dimensional gradient. This won't work for models with millions of parameters.

![[Pasted image 20251115162355.png]]

![[Pasted image 20251115162423.png]]

Whilst some approximation error may be acceptable in machine learning (after all, stochastic [[Gradient Descent]] uses a noisy estimation of the true gradient), the time complexity is prohibitive.
### Symbolic Differentiation
Symbolic differentiation is automated manual differentiation. A program receives a closed-form function and applies standard derivative rules, transforming the expression into the derivative of interest.

![[Pasted image 20251115162534.png]]

This bypasses numerical differentiation errors, allowing exact computation of derivatives up to numerical precision. However, it has its own difficulties.

**Expression Swell:** Derivative expressions may be exponentially longer than the original function. Some derivative rules (like the product rule) naturally lead to duplicated computation. Any computation shared between $f$ and $f'$ will be executed twice.

**Example: Logistic Map**
Consider this recurrence relation:
$$x_{n+1} = rx_n(1-x_n)$$
For $n=1$ and $n=2$, the derivative expression is simple. But as $n$ increases, the derivative quickly becomes unwieldy. Whilst this example can be simplified to polynomial form, this isn't always possible.

**Example: Soft ReLU**
The soft ReLU activation function is:
$$\text{softReLU}(x) = \log(1 + e^x)$$
Even composing two of these together leads to a fairly involved derivative. Symbolically differentiating through a [[Neural Networks|network]] of many layers is usually not tenable.

**Control Flow Limitations:** Symbolic differentiation requires functions to be expressed in closed form, limiting the use of conditionals, loops, and recursion.
## Automatic Differentiation
Automatic differentiation computes derivatives with the same accuracy as symbolic differentiation, but operates directly on the program rather than producing an expression. It obtains numerical values rather than symbolic expressions.

Autodiff bypasses symbolic inefficiency by leveraging intermediate variables present in the original function's implementation and more easily handles control flow. The key insight is that implemented differentiable functions are composed of primitive operations whose derivatives we know, and the chain rule allows us to compose these together.

There are two main versions: forward mode and reverse mode.
## Forward Mode
Forward autodiff augments each intermediate variable during function evaluation with its derivative. Instead of individual floating-point values flowing through a function, we work with tuples of the original intermediate values (primals) paired with their derivatives (tangents).
### Forward Mode Example
Consider a function with two scalar inputs $x_1$ and $x_2$ and a single scalar output. To compute $\frac{\partial f}{\partial x_1}$ at point $(x_1=1.5, x_2=0.5)$:
1. Initialise input variables with both primal and tangent values
2. For $\frac{\partial}{\partial x_1}$: set $\dot{x_1} = 1$ and $\dot{x_2} = 0$
3. Evaluate intermediate variables, computing both primal and tangent values
4. The final output includes both $f(x_1, x_2)$ and $\frac{\partial f}{\partial x_1}$

A single forward pass produces the original output and the partial derivative of interest.
### Multiple Outputs and Inputs
For functions with multiple scalar outputs, forward mode computes partial derivatives of each output with respect to an input variable in a single forward pass.

However, a separate forward pass is required for each input variable. For general functions from $\mathbb{R}^n \to \mathbb{R}^m$, each pass of forward mode autodiff produces one column of the corresponding Jacobian.

**When to Use Forward Mode:** Preferred when $n \ll m$ (few inputs, many outputs).

### Directional Derivatives and Jacobian-Vector Products
Partial derivatives are the axis-aligned special case of directional derivatives. We can initialise $\dot{x}$ to any unit vector and compute the corresponding directional derivative with a single forward pass.

More generally, we can compute Jacobian-vector products without computing the Jacobian matrix itself. Set $\dot{x}$ to the vector of interest and proceed with forward mode autodiff. This is equivalent to computing the Jacobian of the composition of the original function with one having a single scalar input.
### Implementation
**Operator Overloading:** Create a class with attributes for both primal and tangent values. Overload primitive arithmetic operations to handle derivative computation. For example, addition uses the sum rule for derivatives.

**Source Code Transformation:** Input source code is manipulated to produce a new function. More efficient than operator overloading as it directly exposes logic to the compiler, but more difficult to implement.
## Reverse Mode
Forward mode works well with few inputs, but machine learning typically involves models with many parameters (sometimes billions) and we need the gradient of a scalar loss with respect to these parameters. Reverse mode autodiff handles this efficiently.

Rather than propagating derivatives forward, they're propagated backwards from the output in a two-part process:
### Reverse Mode Process
**Forward Pass:** Evaluate intermediate variables and store the dependencies of the expression tree in memory (but don't compute derivatives yet).

**Backward Pass:** Compute partial derivatives of the output with respect to intermediate variables (adjoints, denoted $\bar{v}$).

To obtain the adjoint $\bar{v_i}$ for a node:
1. Look at each of the node's children
2. Multiply the child's adjoint by $\frac{\partial \text{child}}{\partial v_i}$
3. Sum these products

A node's contribution to the final output is determined both by how each of its children affect the output and how it affects each of its children.

### Characteristics of Reverse Mode

**Efficiency:** The gradient is computed with just a single execution of reverse mode autodiff, making it far better suited to typical optimisation settings in machine learning.

**Backpropagation:** In the context of [[Neural Networks]], the backpropagation algorithm (used to compute derivatives with respect to network weights) is a special case of reverse mode autodiff, where adjoints with respect to intermediate layer activations are propagated backwards through the network.

**Jacobian Computation:** For vector-valued functions, reverse mode produces one row of the Jacobian at a time, making it ideal when we have few outputs relative to inputs.

**Computational Cost:** A single pass takes less than six times the number of operations in the original function (typically only 2-3 times in practice).

**Memory:** More memory-intensive than forward mode. We must store values of intermediate variables and their dependencies in memory.

**Re-materialisation:** A technique where only a subset of intermediate variables are stored, and the remainder are recomputed during the backwards pass, helping reduce memory requirements.

## Hybrid Approaches

Forward and reverse mode are extremes of automatic differentiation. In some settings, hybrid approaches are preferred.

### Hessian-Vector Products

Second-order optimisation methods that use curvature information sometimes need Hessian-vector products. A reverse-on-forward approach efficiently computes this:

1. Use forward mode to compute the directional derivative $\nabla f \cdot v$ by setting $\dot{x} = v$
2. Use reverse mode to differentiate again, resulting in $Hv$ (Hessian times $v$)

As with Jacobian-vector products, we compute the Hessian-vector product without explicitly computing the Hessian matrix.

### Higher-Order Derivatives

We can compute arbitrarily higher-order derivatives by composing multiple executions of autodiff together.

## Summary

Automatic differentiation makes computing derivatives of complicated functions much easier. When we can directly implement a function in code, autodiff allows accurate computation of derivatives with minimal overhead. It has a rich history and ongoing research continues to improve it.

**Key Advantages:**
- Accuracy matching symbolic differentiation
- Avoids expression swell
- Handles control flow
- Efficient computation (especially reverse mode for ML applications)
- Supports higher-order derivatives through composition
