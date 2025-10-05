## **Motivation**
 - Suppose you have millions of d-dimensional vectors (say $d = 128$), and you want to store them compactly while still supporting approximate nearest-neighbour search.
- You could use **k-means quantisation** directly:  
	- Find a large codebook of $k$ centroids and store each vector by the index of its closest centroid.  
	- But that would require an enormous codebook — e.g. for 128-D data, even $k = 10^6$ might not be enough resolution.

**Product Quantisation (PQ)** solves this by _factorising the space_ into smaller parts.
## Algorithm
Instead of quantising the whole vector at once, PQ **splits each vector into sub-vectors**, and quantises each sub-vector separately.
- For a vector $x \in \mathbb{R}^d$:
	- Split $x$ into $m$ equal parts: $x = [x_1, x_2, ..., x_m]$
	  where each $x_i \in \mathbb{R}^{d/m}$.
- For each subspace $i$, learn a small **codebook** using k-means:
    - $C_i = { c_{i1}, c_{i2}, ..., c_{iK} }$
     where $K$ is typically 256 (so each subvector can be stored in **1 byte**).
- Quantise each subvector by storing the index of its closest centroid:
    $q_i(x_i) = argmin_j || x_i - c_{ij} ||^2$
- The overall quantised vector is then represented by:
    $q(x) = [ q_1(x_1), q_2(x_2), ..., q_m(x_m) ]$
    i.e., a sequence of _m_ small indices.

![[Pasted image 20251005083234.png | center]]

This is why it’s called **Product** Quantisation, you’re effectively forming a Cartesian product of smaller codebooks $C = C_1 × C_2 × ... × C_m$ which yields an **exponentially large implicit codebook** (size $K^m$) without having to store it explicitly.

![[Pasted image 20251005084715.png|center]]
## Distance computation
(ADC — Asymmetric Distance Computation)
When querying, you don’t decompress all vectors, that would defeat the purpose.
Instead:
- For a query vector $q$, split it into the same $m$ parts $q = [q_1, ..., q_m]$.
- Precompute a **distance table** for each subspace: $$D_i[j] = || q_i - c_{ij} ||^2$$
- For a database vector with PQ code $[k₁, k₂, ..., kₘ]$, estimate the distance as: $$|| q - x ||^2 ≈ Σ_{i=1}^{m} D_i[k_i]$$
This avoids ever reconstructing the full vector and gives fast approximate distances.
## Dimensionality Reduction VS Quantisation
Dimensionality reduction aims to produce a new set of lower dimensional vectors with the same scope **S** (e.g., 32-bits), while quantisation reduces the scope while maintaining the dimensionality **D**. 

![[Pasted image 20251005082807.png|center]]


![[Pasted image 20251005082736.png| center]]

## PQ + IVF
PQ alone gives _compact_ representations, but you’d still have to search the entire dataset.
By combining it with [[IVF (Inverted File Index)]]:
1. IVF clusters the space into _coarse cells_.
2. Within each cell, PQ encodes only the **residuals** (fine detail) relative to the centroid: $$$r_i = x_i - c_j$$
3. At query time, you probe a few cells (nprobe), then use PQ to compute approximate distances.
