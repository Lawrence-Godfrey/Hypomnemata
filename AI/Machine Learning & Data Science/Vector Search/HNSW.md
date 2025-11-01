HNSW (Hierarchical Navigable Small World graphs) is an ANN (Approximate Nearest Neighbour) search algorithm based on multi-layer graph structure. 
- Each layer is a proximity graph where nodes are connected to neighbours by similarity.
- Search proceeds top-down:
    - Start at a high, sparse layer with long-range links → quickly get near the target region.
    - Descend into denser layers for finer search.
- Graph is "navigable": greedy search through neighbours converges rapidly to good candidates.

![[Pasted image 20250928085610.png|center]]
## Algorithm
1. **Index construction**
	- Each new vector is assigned a **maximum layer**.
    - The layer is sampled from an exponential distribution (so most points only appear in the lower layers, while a few are "hubs" at higher layers).
    - This creates a hierarchy: sparse top layers for long jumps, dense bottom layers for local precision.
	- For each layer (from top down):
	    1. **Greedy search** is used to find entry points close to the new vector.
	    2. The new vector is connected to its **M nearest neighbours** within that layer (subject to pruning rules).
	    3. Connections are bidirectional, ensuring graph connectivity.
2. **Search procedure**
	-  **Entry point**: Start at the topmost layer, at some node (usually the last inserted point at max layer).
	-  **Greedy descent**:    
	    - At each layer, perform greedy search — hop from the current node to its closest neighbour if it’s nearer to the query.
	    - When no improvement is possible, drop down a layer.
	2. **Fine search at layer 0**:
	    - Run a **beam search** (best-first) with candidate list size `efSearch`.
	    - Return the closest results from the candidate set.
## Hyperparameters
1. **M (max neighbours per node)**
    - Controls how many connections each node has (except possibly fewer at higher layers).
    - Larger `M` → denser graph → better recall but higher memory usage and build time.
2. **efConstruction (size of candidate list during index build)**
    - Higher means more exhaustive search when connecting new points.
    - Larger values improve index quality (higher recall later), but index build is slower.
3. **efSearch (size of candidate list during query)**
    - Controls recall/speed trade-off at search time.
    - Higher `efSearch` → more thorough search → higher recall but slower query.
    - You can adjust this dynamically at query time.
## HNSW vs [[IVF (Inverted File Index)|IVF]] (Inverted File Index, e.g. FAISS IVF)
- IVF clusters vectors (typically via k-means), then search probes a subset of clusters.
- IVF scales well to billions of vectors but may require careful tuning of cluster size/probe count.
- HNSW usually gives higher recall out of the box, but memory overhead is larger.
## HNSW vs [[Product Quantisation|PQ]] (Product Quantisation) / Compressed indexes
- PQ compresses vectors for memory savings and speed at cost of precision.
- HNSW typically stores full vectors (unless combined with PQ).
- For memory-constrained environments, PQ or IVF-PQ is preferable. For raw speed + recall, HNSW dominates.
## Strengths
- **Excellent recall-speed trade-off**: among the best performing ANN methods in benchmarks.
- **Scales to high dimensions**: works well for 100–2000+ dimensional embeddings (e.g. modern text/image embeddings).
- **Dynamic index**: supports insertion of new vectors without full rebuild (unlike IVF/PQ which often require re-training).
- **Deterministic quality**: performance is stable across many workloads, unlike LSH or trees that can degrade heavily.
## Weaknesses
- **Disjoint Communities**: Performance can degrade when you have extreme clustering, since pointer may get stuck in the wrong cluster at a high level and it can be hard to get out of that cluster.
- **Greedy Search**: can get stuck in local minima if the graph is not well connected, an issue known as "early stopping".
- **Memory-hungry**: stores multiple layers of graph connections, overhead can be ~5–10× the raw vector size.
- **Index build time** is relatively high (graph construction is expensive). Not ideal if you need frequent full rebuilds.
- **Deletion** is not natively supported (requires lazy deletion or rebuild).
- Struggles at **very large scale (>1B vectors)** unless combined with sharding or hybrid methods.


