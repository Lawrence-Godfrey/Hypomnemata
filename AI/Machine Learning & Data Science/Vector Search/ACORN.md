[ACORN](https://arxiv.org/pdf/2403.04871) is fundamentally a graph‐based ANN index. It builds on [[HNSW]], extending it to handle predicates. 

In ACORN, search proceeds exactly like HNSW’s multi-level graph search, but **predicate filters** are applied during traversal. Concretely, ACORN **traverses the subgraph of the ACORN index induced by the set of nodes that pass the query predicate**. As a query descends the HNSW hierarchy (see Figure below), any edge leading to a node that fails the predicate is simply skipped; thus only the _predicate-matching_ “subgraph” is explored. 

This strategy yields sublinear search times even with complicated filters, since the index was built to ensure that any such subgraph remains well-connected. (For extremely selective predicates where the subgraph would be disconnected, ACORN falls back to classical pre-filtering, scanning the few matching records directly).

![[Pasted image 20251101151643.png|center]]


ACORN modifies HNSW’s build algorithm to create a _denser_ graph so that any arbitrary predicate subgraph remains “searchable”. During indexing, each node’s neighbuor list is expanded by a factor γ (a parameter) before pruning. 

This neighbour expansion and subsequent **pruning (compression)** step ensure the index has enough redundant links so that removing nodes (via a predicate) still leaves a navigable graph. 

ACORN uses two lookup strategies: a simple filter of the neighbour list, or an expanded “two-hop” lookup (including neighbours of neighbours). It then greedily searches from an entry point down to level 0, exactly as in HNSW except that at each node it filters neighbours by the predicate.