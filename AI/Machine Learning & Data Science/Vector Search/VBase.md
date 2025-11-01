[VBase](https://www.usenix.org/conference/osdi23/presentation/zhang-qianxi) (MSVBASE) is a unified database system that integrates high-dimensional vector similarity search with relational queries by exploiting a property called relaxed monotonicity. It was developed by Microsoft Research and presented at OSDI 2023.
## The Problem
Traditional vector databases and relational databases are fundamentally incompatible because high-dimensional vector indices lack monotonicity, a critical property that conventional database indices rely on for efficient query execution.
### What is Monotonicity in Database Indices?
Monotonicity in database indices refers to the property that values can be traversed in a predictable, ordered manner. Traditional indices like B-trees maintain a sorted order of keys, which enables:
- **Ordered traversal**: Scanning entries in ascending or descending order
- **Early termination**: Stopping the scan once a condition is met (e.g., for `ORDER BY ... LIMIT` queries)
- **Range queries**: Efficiently finding all values between two bounds
- **Merge joins**: Combining sorted results from multiple indices
For example, a B-tree index on ages can be scanned from lowest to highest. When executing `SELECT * FROM users WHERE age > 25 ORDER BY age LIMIT 10`, the database can start at age 26, scan in order, and stop after finding 10 rows. This is possible because the index exhibits monotonicity: as you traverse it, values increase monotonically.
### Why Vector Indices Lack Monotonicity
High-dimensional vector indices don't have a natural ordering. Vectors in 100-dimensional or 1000-dimensional space cannot be sorted into a single linear sequence that preserves similarity relationships. Consider:
- In 1D, numbers have a clear order: 1 < 2 < 3 < 4
- In 2D, you can sort by x-coordinate, then y-coordinate, but points with similar coordinates aren't necessarily close in Euclidean distance
- In high dimensions (e.g., 768D embeddings), there's no meaningful way to create a single sorted order
Vector indices like [[HNSW]] or [[IVF (Inverted File Index)|IVF]] organise vectors by proximity (similarity), not by any sortable attribute. The traversal of these indices doesn't follow a monotonic path—you might visit vectors with distances `[0.2, 0.15, 0.3, 0.18]` in that order, which isn't monotonically increasing or decreasing.
## Relaxed Monotonicity
VBase's key innovation is the discovery that whilst vector indices don't exhibit strict monotonicity, they do exhibit a weaker form called [[Relaxed Monotonicity]]. This property allows the system to:
- Traverse vector indices incrementally, returning candidates as they're discovered
- Terminate early when enough candidates have been found to satisfy the query
- Apply relational predicates during traversal rather than after TopK completion
- Maintain semantic equivalence with TopK-based solutions whilst achieving dramatically better performance
The traversal of scalar indices (used in traditional databases) is a special case of this relaxed monotonicity, meaning both types of indices can be unified under the same interface.
## How It Works
Instead of requiring a fixed TopK result set, VBase returns an iterator that produces candidates incrementally. PostgreSQL (or any query engine) can then:
1. Apply relational predicates (filters, joins) to candidates as they arrive
2. Terminate iteration when the LIMIT clause is satisfied
3. Avoid scanning unnecessary portions of the vector index
This approach circumvents the constraints of the TopK-only interface whilst provably preserving query semantics.
## Integration with PostgreSQL
VBase integrates high-dimensional vector indices directly into PostgreSQL with minimal code modifications. It:
- Supports PostgreSQL syntax and protocol
- Enables vector distance calculations (L2 distance and inner product)
- Allows complex queries mixing vector similarity search with SQL operations
- Maintains compatibility with existing PostgreSQL tools and workflows
## Comparison with Other Vector Search Methods
Unlike [[HNSW]], [[IVF (Inverted File Index)|IVF]], or [[Product Quantisation|PQ]], which focus purely on approximate nearest neighbour search, VBase provides a unified query execution framework that seamlessly combines vector search with relational operations. Traditional vector indices can be used within VBase, but the system's relaxed monotonicity property enables much more efficient execution of complex queries.