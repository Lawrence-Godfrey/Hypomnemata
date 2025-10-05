**Inverted File Index / Inverted Index / Inverted File System** is a classic approximate nearest neighbour (ANN) technique widely used in vector search systems (e.g. FAISS). 
- **Two-stage search structure** that partitions the vector space into “coarse cells” and then searches only within a few of those cells, rather than across the entire dataset.
 - The idea is to **avoid exhaustive search** by first grouping similar vectors together, and then for a given query only comparing against vectors in a few relevant groups.
## Algorithm
#### Build
1. **Coarse quantisation (clustering)**
    - Run **k-means** on your dataset to obtain **k centroids**:  
        ${c₁, c₂, ..., c_k}$.
    - Each centroid represents a **coarse cell** (or “inverted list”).
2. **Assign data points to centroids**
    - Each vector $x_i$ is assigned to its nearest centroid $c_j$.
    - You store the residual vector $rᵢ = xᵢ - c_j$  in the inverted list corresponding to centroid $j$.
	    - The centroid already represents the **coarse location** of that region in space.
		- The residual encodes the **local offset** within that region.
    - The inverted list acts like an “index” for that cell.
#### Search 
When querying with vector **q**:
1. **Find the closest n_probe centroids** to q: $nearest cells = argmin_{j} || q - c_j ||$
    (often just the top N centroids by proximity).
2. **Search only in those cells**
    - For each selected centroid $c_j$:
        - Compute the residual: $r_q = q - c_j$
        - Compare $r_q$ to the residuals stored in that cell to find nearest neighbours.
3. **Re-rank** the best candidates globally to return the final top-k.
## Why Store Residuals
Why do we calculate and store residuals $r_i$ instead of the actual vectors? 
- Residuals captures the **fine-grained difference** between the vector and the centroid.
- Why this matters:
	- The centroid already represents the **coarse location** of that region in space.
	- The residual encodes the **local offset** within that region.

- So, instead of storing large, absolute coordinates (which may vary widely across cells), you store compact, small residuals relative to the centroid.
- This is critical when IVF is used **with quantisation**, e.g. **IVF+PQ** (Product Quantisation):
	- PQ learns codebooks to compress these _residuals_, not the original vectors.
	- Because residuals are local, they have **smaller variance**, making compression much more accurate and efficient.

If you’re using **IVF+Flat**, there’s no compression — you could technically skip residuals — but IVF implementations (like FAISS) keep this structure for consistency.
## Implementation Details
IVF can be used alone (IVF+Flat) or with other search algorithms/indexes, for example:
- **IVF+PQ** → stores compressed residuals using Product Quantisation.
- **IVF+HNSW** → uses [[HNSW]] as a coarse quantiser.
## Curse of Dimensionality
High-dimensional spaces make clustering and distance estimation harder — the **curse of dimensionality**.
- Impacts on IVF:
	- **Centroid quality degrades:** k-means struggles to form meaningful clusters because distances between all points become similar.
- **Residuals become noisier:** offsets don’t capture local variation well.
- **Recall drops** unless you increase **nprobe** or **nlist**, which increases compute.
- Mitigation:
	- Apply **dimensionality reduction** (e.g. PCA, OPQ).
	- Use **IVF+PQ or IVF+HNSW hybrid** — quantisation + graph helps correct coarse errors.
## IVF vs HNSW
- **IVF+Flat** → high-throughput, static datasets (e.g. FAISS on GPU).
- **HNSW** → dynamic, low-latency CPU search (e.g. Milvus, Qdrant, Pinecone).
