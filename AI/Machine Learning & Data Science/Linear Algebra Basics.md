## Matrix Multiplication Properties
### Commutative Property
$$A \times B \neq B \times A$$
### Associative Property
$$(A \times B ) \times C = A \times (B \times C)$$
### Identity Matrix Properties
The identity matrix, denoted $I$ or $I_{n\times n}$ is a square matrix with ones along the diagonal and zeros everywhere else.

For any matrix A
$$A \cdot I = I \cdot A = A$$
### Inverse
$$A(A^{-1}) = (A^{-1})A = I$$
Note: Not all matrices have an inverse. These are known as "singular" or "degenerate".

### Linearity Test
A function is linear if it satisfies two main properties:
##### Additivity (Superposition): 
$$( f(x + y) = f(x) + f(y) )$$
**Intuition**: This means that the function’s output for the sum of two inputs is the same as the sum of the outputs for each input individually. This property ensures that the function preserves the way inputs combine. If you think of inputs as vectors, this property indicates that the function respects vector addition.
##### Homogeneity (Scalar Multiplication): $$( f(cx) = c f(x) )$$ for any constant $( c )$

Intuition: This means that scaling the input by a constant  c  scales the output by the same constant. This property ensures that the function preserves the relative magnitudes of the input. If you think of inputs as vectors, this property indicates that the function respects scalar multiplication.

