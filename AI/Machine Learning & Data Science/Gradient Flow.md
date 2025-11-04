## **The Chain Rule is Everything**
When we say "gradients flow," we mean **backpropagation applies the chain rule** to compute derivatives. 
### Example 1: Simple Chain

```python
# Forward pass
x = 2.0          # Input
w = 3.0          # Weight (trainable parameter)
y = x * w        # y = 6.0
loss = y ** 2    # loss = 36.0
```

**Computational graph:**

```
x=2 ──┐
      ↓ [multiply]
w=3 ──→ y=6 ──→ [square] ──→ loss=36
      ↑                         ↑
   PARAMETER              MINIMIZE THIS
```

**Backward pass (gradient flow):**
We want $\frac{\partial \text{loss}}{\partial w}$ to update $w$ via gradient descent.

By chain rule: $$\frac{\partial \text{loss}}{\partial w} = \frac{\partial \text{loss}}{\partial y} \times \frac{\partial y}{\partial w}$$
Step-by-step:
1. **At loss node:** $\frac{\partial \text{loss}}{\partial y} = 2y = 2 \times 6 = 12$
2. **At multiply node:** $\frac{\partial y}{\partial w} = x = 2$
3. **Combine:** $\frac{\partial \text{loss}}{\partial w} = 12 \times 2 = 24$

**"The gradient flows through y"** means:
- The gradient **enters** the $y$ node from the loss: $\frac{\partial \text{loss}}{\partial y} = 12$
- It **flows backward** through the multiply operation
- It **arrives** at $w$ as: $\frac{\partial \text{loss}}{\partial w} = 24$
### Example 2: Blocked Gradient Flow
What if we **stop** the gradient?

```python
# Forward pass
x = 2.0
w = 3.0
y = x * w
y_stopped = y.detach()  # STOPS GRADIENTS HERE
loss = y_stopped ** 2

# Backward pass
loss.backward()
print(w.grad)  # None! No gradient reached w
```

**Why?** `.detach()` breaks the computational graph:

```
x=2 ──┐
      ↓ [multiply]
w=3 ──→ y=6 ──❌ DETACH ❌──→ y_stopped=6 ──→ loss=36
      ↑          ↑
   PARAMETER   GRADIENT FLOW STOPS HERE
```

The gradient computed at `y_stopped` **cannot flow backward** through the broken link to `w`. We say "the gradient is blocked" or "gradients don't flow through the detached operation."

