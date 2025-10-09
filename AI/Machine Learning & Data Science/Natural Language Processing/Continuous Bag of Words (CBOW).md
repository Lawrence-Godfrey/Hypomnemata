The Continuous Bag of Words (CBOW) model is a [[Word Embeddings|Word Embedding]] model which learns to predict a target word based on its surrounding context words. While it shares part of its name with the [[AI/Machine Learning & Data Science/Natural Language Processing/Bag of Words|Bag of Words (BoW)]] model, its goal is to create dense word embeddings rather than just counting word frequencies. It is said to be a self-supervised model, since it does not require labelled data for training, but instead learns from the structure of the text itself.

![[Pasted image 20231024231616.png]]

To train the model, we provide the context words as input, and use the centre word as the "label", before sliding the window over once and continuing until the end of the corpus.
## Architecture
The CBOW model vectorises the centre word and context words using [[One-hot Word Representation]], and averages the centre words to create a single vector. 

The context vector is fed into a shallow dense [[Neural Networks|neural network]]. The input and output vectors will be of size $V$ in the case of the One-hot vector representation (where $V$ is the size of the vocabulary). The size, $N$, of the single hidden layer can be configured depending on how large you want your word embedding to be. 

The first activation function is a [[ReLU]], while the second is a [[softmax]].

During training, [[Loss Functions|cross entropy loss]] is used to train the model.
## Extracting Embeddings
There are a number of ways to extract word embeddings from your trained model. One way could be to use the weight matrix $W_{1}$ between the input layer and hidden layer. This matrix will have $V$ columns, each column corresponding to a word in your vocabulary. Similarly, the rows of the weight matrix $w_{2}$ between the hidden layer and output layer of the model can be used as word embeddings. You can also average $w_{1}$ and $w_{2}^{T}$ to get your embeddings.

The quality of these embeddings can be evaluated using [[AI/Machine Learning & Data Science/Performance Metrics/Intrinsic and Extrinsic Evaluation|Intrinsic and Extrinsic Evaluation]].