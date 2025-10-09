# Term Frequency-Inverse Document Frequency (TF-IDF)

**Tags:** #NLP #FeatureExtraction #InformationRetrieval

Term Frequency-Inverse Document Frequency, or TF-IDF, is a numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus. It is a very common and fundamental technique in information retrieval and text mining.

The TF-IDF value increases proportionally to the number of times a word appears in the document and is offset by the number of documents in the corpus that contain the word, which helps to adjust for the fact that some words appear more frequently in general.

## Calculation

The TF-IDF score is the product of two statistics: Term Frequency and Inverse Document Frequency.

### Term Frequency (TF)

Term Frequency measures how frequently a term occurs in a document. Since every document is different in length, it is possible that a term would appear much more times in long documents than shorter ones. Thus, the term frequency is often normalized:

$$
\text{TF}(t, d) = \frac{\text{Number of times term } t \text{ appears in document } d}{\text{Total number of terms in document } d}
$$

### Inverse Document Frequency (IDF)

Inverse Document Frequency measures how important a term is. While computing TF, all terms are considered equally important. However, it is known that certain terms, such as "is", "of", and "that", may appear a lot of times but have little importance. Thus we need to weigh down the frequent terms while scaling up the rare ones.

$$
\text{IDF}(t, D) = \log\left(\frac{\text{Total number of documents in corpus } D}{\text{Number of documents with term } t \text{ in it}}\right)
$$

### TF-IDF

The TF-IDF score is then the product of these two values:

$$
\text{TF-IDF}(t, d, D) = \text{TF}(t, d) \cdot \text{IDF}(t, D)
$$

## Relationship with Other Models

-   **[[Bag of Words]]:** TF-IDF is a refinement of the Bag of Words model. Instead of just using raw counts, it uses the TF-IDF scores to represent words, which helps to focus on more meaningful terms.
-   **[[AI/Machine Learning & Data Science/Vector Search/BM25|BM25]]:** The BM25 algorithm is a further evolution of TF-IDF. It introduces additional parameters for term frequency saturation and document length normalization, generally providing better ranking results.
