https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf

## Problem
- Labeled data for learning specific tasks is scarce.
	- Textual entailment (T text entails H hypothesis, e.g., **T**: "John bought a car yesterday." **H**: "John owns a vehicle.").
	- Question answering.
	- Semantic similarity.
	- Document classification.
- Large gains on these tasks can be gained through generative pre-training.
- Leveraging more than word-level information from unlabeled text is challenging. 
	- What optimisation object to use? 
		- Language modeling - predicting the next word in a sequence.
		- Machine translation - translating text from one language to another.
		- Discourse coherence - maintaining logical and meaningful flow across sentences or paragraphs in text.
	- No consensus on the most effective way to transfer these learned representations to the target task.
## Goal
 - Semi-supervised approach for language understanding tasks 
	 - Unsupervised pre-training and Supervised fine-tuning.

- Pre-training acts as a regularisation scheme, enabling better generalisation in deep neural networks.
- Unlike the original Transformer, which includes both an encoder and decoder for tasks like machine translation, this model uses only the decoder component, adapted for autoregressive language modeling.
- For fine-tuning, adds a linear output layer for labelled output.

### Pre-training Objective
- $P(u)=softmax(h_{n}​W_{e}^{T}​)$ 
	- $h_n$
		- This is the output of the final Transformer layer.
		- $h_n$ is a vector of hidden states with a dimensionality of 768 (the size of the model’s internal representations).
		- It encodes the contextual information of the input sequence up to the current position.
	- $W_e$
	    - $W_e$ is the token embedding matrix used at the input of the model.
		- It has dimensions $V \times d$, where:
			- $V$ is the size of the vocabulary (e.g., 40,000 tokens with byte-pair encoding in this case),
			- $d = 768$ is the embedding dimension (matching the hidden state size).
		- Each row of $W_e$ corresponds to the embedding vector of a specific token in the vocabulary.
	- $W_e^T$
	    - This is the transpose of the token embedding matrix.
	    - Transposing $W_e$ allows the model to project the hidden state $h_n$​ back into the vocabulary space.
	- $h_n W_e^T$
	    - The result is a $1 \times V$ vector, often called the "logits" or unnormalized scores.
	    - Each element in this vector represents a raw score for a corresponding token in the vocabulary.
	- $L_{1}(U) = \sum_{i} log P(u_{i} |u_{i−k}, . . . , u_{i−1}; Θ)$

### Fine-tuning Objective
- $P(y∣x_{1},…,x_{m})=softmax(h_{l}^{m}​W_{y}​)$
	- Adds layer $W_{y}$
	- $h_{l}^{m}$ is still just the hidden layer output at position $m$ (usually the end of the input sequence).
- $L_{2}(C) = \sum_{(x,y)} log P(y|x_{1} , . . . , x_{m})$
- They then use $L_{3}(C) = L_{2}(C) + λ ∗ L_{1}(C)$
	- Introducing $L_1$ as an auxiliary objective which the found improved generalisation and accelerated convergence.

![[Pasted image 20250406191443.png]]

 - [[Perplexity|Perplexity]] score of 18.4.
 - Uses [[Byte Pair Encoding]] with 40,000 merges.
 - Uses [[GELU Activation]] (Gaussian Error Linear Unit) activation functions for the feedforward network.
 - Uses learned position embeddings instead of the sinusoidal version proposed in [[2017 - Attention Is All You Need]].
### Impact of Transferred Layers
Found that the more layers which are transferred, the better the performance.

![[Pasted image 20250407181702.png]]