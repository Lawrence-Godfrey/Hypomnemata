The Bag of Words (BoW) model is a simple and fundamental feature extraction technique used in Natural Language Processing (NLP) and Information Retrieval (IR). It represents a piece of text (like a sentence or a document) as an unordered collection of its words, disregarding grammar and even word order, but keeping track of multiplicity.

The main idea is that documents with similar content are semantically similar.
## How it Works
The process of creating a Bag of Words model involves three steps:
1.  **Tokenisation:** Breaking down the text into individual words or tokens.
2.  **Vocabulary Creation:** Building a vocabulary of all unique words in the entire corpus of documents.
3.  **Vectorisation:** For each document, creating a vector that represents the frequency of each word from the vocabulary in that document.

The result is a [[Term-Document Matrix]], where each row represents a document and each column represents a word from the vocabulary.
### Example
Consider the following two sentences:
1.  "The cat sat on the mat."
2.  "The dog sat on the rug."

**1. Tokenisation & Vocabulary Creation:**
The vocabulary would be: `{"The", "cat", "sat", "on", "the", "mat", "dog", "rug"}`.
Unique words: `{"The", "cat", "sat", "on", "mat", "dog", "rug"}`.

**2. Vectorisation:**
Each sentence is represented as a vector of word counts:
-   Sentence 1: `{"The": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1, "dog": 0, "rug": 0}`
-   Sentence 2: `{"The": 2, "cat": 0, "sat": 1, "on": 1, "mat": 0, "dog": 1, "rug": 1}`

These vectors can then be used as input for machine learning algorithms.
## Limitations
-   **Sparsity:** For large vocabularies, the resulting vectors are very long and mostly filled with zeros.
-   **Loss of Context:** The model completely ignores the order of words, which can be crucial for understanding the meaning of the text. For example, "this is good, not bad" and "this is bad, not good" would have very similar representations.
-   **Doesn't handle out-of-vocabulary (OOV) words:** Words not in the vocabulary are ignored.
## Relationship with N-grams

The standard Bag of Words model uses individual words as its features, which is equivalent to using a vocabulary of **unigrams** (1-grams). This approach loses all information about word order.

To capture some local context and word order, the BoW model can be extended to use **[[N-Gram Model|n-grams]]**. Instead of counting single words, the model can count the frequency of sequences of *n* words. For example, a **bigram** (2-gram) model of the sentence "The cat sat on the mat" would count the occurrences of "The cat", "cat sat", "sat on", "on the", and "the mat".

Using n-grams as features in a BoW model helps to preserve more of the original sentence's structure and meaning. However, it also significantly increases the size of the vocabulary, leading to even higher-dimensional and sparser vectors.

## Related Concepts

-   **[[Continuous Bag of Words (CBOW)]]:** A neural network model that learns to predict a word from its surrounding context, creating dense word embeddings.
-   **[[Term-Document Matrix]]:** The matrix representation of the Bag of Words model.
-   **[[Term Frequency-Inverse Document Frequency|TF-IDF]]:** A refinement of the Bag of Words model that gives more weight to words that are frequent in a document but rare across all documents.

