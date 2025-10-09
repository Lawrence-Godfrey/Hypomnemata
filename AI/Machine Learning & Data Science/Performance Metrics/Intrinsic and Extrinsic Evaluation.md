# Intrinsic and Extrinsic Evaluation

**Tags:** #Evaluation #NLP #WordEmbeddings

When evaluating word embeddings, there are two main approaches: intrinsic and extrinsic evaluation.

## Intrinsic Evaluation

Intrinsic evaluation assesses word embeddings based on their internal properties and characteristics, without considering their performance on a specific downstream task. This method focuses on analyzing the quality of the embeddings themselves.

Examples of intrinsic evaluation include:
-   **Word Similarity:** Measuring the semantic similarity between words (e.g., "king" and "queen") and comparing it to human judgments.
-   **Word Analogies:** Testing for relationships like "king" is to "queen" as "man" is to "woman". The famous `king - man + woman = queen` is an example of this.
-   **Clustering:** Evaluating how well the embeddings group similar words together.

Intrinsic evaluations are useful for understanding the syntactic and semantic information captured by the embeddings.

## Extrinsic Evaluation

Extrinsic evaluation assesses word embeddings based on their performance in a specific external task or application. The embeddings are used as input features to a downstream model, and the performance of that model is used to judge the quality of the embeddings.

Examples of extrinsic evaluation tasks include:
-   **Named Entity Recognition (NER)**
-   **Part-of-Speech (POS) Tagging**
-   **Sentiment Analysis**
-   **Text Classification**

Extrinsic evaluation provides a more practical measure of how useful the embeddings are for real-world applications. The downside is that performance can be influenced by the downstream model's architecture and hyperparameters, not just the quality of the embeddings.
