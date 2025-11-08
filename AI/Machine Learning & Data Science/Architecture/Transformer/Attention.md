## Overview
The Attention mechanism is a critical advancement in the field of neural networks, especially in the domain of sequence-to-sequence ([[Seq2Seq]]) models. It was developed to enhance the capability of these models by allowing them to focus on different parts of the input sequence for each step of the output sequence. This mechanism is particularly advantageous in improving the handling of long sequences and retaining context more effectively compared to the basic Seq2Seq models.
## Types of Attention
There are primarily two types of attention mechanisms: Global (or Soft) Attention and Local (or Hard) Attention. Global Attention considers all hidden states of the encoder when generating each word of the decoder. While this approach is computationally intensive, it offers a thorough analysis of the input sequence. On the other hand, Local Attention focuses only on a subset of the encoder's hidden states, making it more efficient but potentially less accurate in certain contexts.
## Keys, Values and Queries
The idea of keys and queries in attention is essentially used to create a linear transformation of the input embedding to a space which we can do attention on more effectively. In the image below, the keys and queries (green and purple) transform the input embeddings so that they have a lower similarity.
![[Pasted image 20231226102652.png]]

The values matrix is used to transform this new embedding used for finding similarity to one used to find the next word:
![[Pasted image 20231226103123.png]]

### Scaled dot-product Self-Attention
In scaled dot-product self-attention, the first MatMul block is performing the dot-product on the keys and queries matrix to find the similarity embeddings:
![[Pasted image 20231226103356.png|center]]

The three blocks after that scale the embeddings in such a way that they take into account their own context (for example, think of the word "apple" in two different sentences: "I ate the apple" and "I love my apple phone". The embedding for "apple" will be scaled differently). 
the final MatMul is the dot product with the values matrix, which scales the embeddings onto a plane which is more effective for a [[Transformer]] to predict the next word in.
### Multi-head Attention
Multi-head attention uses a number of key, query and value matrices. These matrices are essentially doing the same thing as in the self-attention case, but in this case you will have a number of them producing different embeddings, which are then concatenated to produce embeddings in much higher dimensions. A linear step then scales the output embeddings of the different heads, essentially choosing the output which produced the best embeddings.
![[Pasted image 20231226104135.png|center]]

## Challenges
Despite its advantages, the Attention mechanism comes with its own set of challenges. The most significant of these is the Computational Complexity, especially in the case of global attention, due to the need to process all encoder states for each decoder step. Additionally, the memory requirements are high for long sequences, as attention mechanisms need to store and process all encoder states.
## Evolution
One of the most notable evolutions in the field of attention-based models is the [[Transformer]] Model. This architecture relies entirely on attention mechanisms, dispensing with recurrent layers. This shift has led to significant improvements in training efficiency and overall performance of neural network models in handling sequence-based tasks.
