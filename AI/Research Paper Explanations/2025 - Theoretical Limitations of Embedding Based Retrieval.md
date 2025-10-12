https://arxiv.org/pdf/2508.21038
## Goal
Prove theoretically and empirically that **embedding-based (dense) retrieval models** cannot, even in principle, represent all possible query-document relevance relationships, regardless of model size or training data.
### Core Idea
- Embedding models represent both queries and documents as single vectors in a fixed-dimensional space. 
- The paper shows that **the number of distinct top-k retrieval sets that can be represented is fundamentally limited by the embedding dimension**.  
- That is, for an embedding dimension $d$, there exist combinations of relevant documents that **no possible query vector** can retrieve, even with perfect optimisation.
### Empirical Demonstration
1. **Free Embedding Optimisation**  
    They directly optimise document/query embeddings (bypassing language) to find when the model fails to represent all combinations of top-k documents.
    - The “critical-n” (number of documents before failure) grows roughly **cubicly with dimension**.
    - Even 4096-dimensional embeddings fail beyond ~250M documents.
2. **LIMIT Dataset**  
    A synthetic, "realistic" benchmark designed to stress these limits.  
    Example task: “Who likes Apples?” → documents represent people and their liked items.
    - Even SOTA models (e.g. GritLM, Qwen3, Gemini Embeddings) perform poorly: recall@100 < 20%.
    - Lexical models like **BM25** perform much better due to effectively infinite dimensionality.
    - Increasing embedding size helps but doesn’t remove the limitation.

![[Pasted image 20251012162510.png]]
## Key Findings
- **Dimensional bottleneck**: There’s a hard cap on how many distinct top-k relevance sets can be represented given a fixed dimension.
- **Instruction-following retrieval** (where relevance definitions vary arbitrarily) will increasingly hit this wall.
- **Failure is not due to domain shift or training data**, but a theoretical geometric limit.
- Models with multiple vectors (e.g. **ColBERT**, **BM25**) or cross-encoders don’t suffer the same issue.
## Opinion
While this paper is interesting and completely sound, I don't see this having any implications on embedding-based retrieval implementations in reality. The LIMIT dataset is adversarially constructed to prove their point and isn't actually very realistic (users generally don't use logical operators in their queries to search for unrelated things). 

Additionally, dense embeddings by design can't represent all relevant combinations. They are compressed representations of data that has semantic structure (not random data). The fact that the data has semantic structure (which all useful data does) means that it can be represented by some finite embedding space.