[[Transformer|Transformers]] (Vaswani et al., 2017) process sequences _in parallel_ — unlike RNNs or CNNs, there’s no inherent notion of order.  
The self-attention mechanism is _permutation invariant_: it treats its input as a set, not a sequence.  
So we must inject information about **token order** (position in sequence) directly into the representations.

Formally, given embeddings $x_1,x_2\dots,x_n$​, we need to add or mix in a positional signal $p_i$​ for each position $i$.

## Absolute Sinusoidal Positional Encoding 
In the original Transformers paper they propose encoding absolute positions $i$ as deterministic sinusoids:
$$p_{i,2k} = \sin(i / 10000^{2k/d}), \quad p_{i,2k+1} = \cos(i / 10000^{2k/d})$$
**Why:**
- It gives each position a unique signature.
- Sinusoids with exponentially scaled frequencies allow the model to extrapolate to longer sequences, so unseen positions have embeddings that still fit the pattern.
- No additional parameters to learn.
**Drawbacks:**
- It encodes _absolute_ positions; the model has to _learn_ how to infer relative distances (e.g. “the previous token”).
- Harder to generalise to unseen sequence lengths.
## Learned Absolute Positional Embeddings 
Models like Transformer-XL, BERT (era, 2018–2019) introduce learning positional embeddings.  Instead of sinusoids, make $p_i$​ a learned embedding vector.

**Why:**
- Gives model flexibility. Can learn arbitrary position representations.
- Works fine for fixed context lengths.
**Drawbacks:**
- Doesn’t generalise to longer sequences.
- No explicit notion of relative distance; attention weights depend on position indices seen during training only.

## **Relative positional encodings (Shaw et al., 2018; Transformer-XL, Dai et al., 2019)**

**Core idea:** make attention explicitly _relative_ — the attention score between token iii and jjj depends on their distance j−ij-ij−i, not just absolute positions.

Attn(i,j)=qi⊤(kj+rj−i)\text{Attn}(i,j) = q_i^\top (k_j + r_{j-i})Attn(i,j)=qi⊤​(kj​+rj−i​)

where rj−ir_{j-i}rj−i​ is a learned embedding for each relative distance.

**Why:**

- Better translation and long-context behaviour.
    
- Handles arbitrary shifts (e.g. if a phrase moves in position, relationships remain consistent).
    

**Drawbacks:**

- Memory cost grows with sequence length (need embeddings for all distances).
    
- Implementation more complex.

## **Rotary Positional Embedding (RoPE; Su et al., 2021, published 2024 in _Neurocomputing_)**

**Breakthrough:** rather than adding or biasing, _rotate_ queries and keys in complex space according to position.

For token position mmm:

Rm=[cos⁡(mθ1)−sin⁡(mθ1)…sin⁡(mθ1)cos⁡(mθ1)…]R_m = \begin{bmatrix} \cos(m\theta_1) & -\sin(m\theta_1) & \dots \\ \sin(m\theta_1) & \cos(m\theta_1) & \dots \end{bmatrix}Rm​=[cos(mθ1​)sin(mθ1​)​−sin(mθ1​)cos(mθ1​)​……​]

Attention between mmm and nnn:

Smn=(Rmqm)⊤(Rnkn)=qm⊤Rn−mknS_{mn} = (R_m q_m)^\top (R_n k_n) = q_m^\top R_{n-m} k_nSmn​=(Rm​qm​)⊤(Rn​kn​)=qm⊤​Rn−m​kn​

**Why it mattered:**

- Encodes **relative position** implicitly (depends only on n−mn-mn−m).
    
- Maintains the _rotational symmetry_ that’s friendly to extrapolation.
    
- Parameter-free and simple to integrate.
    
- Became standard in modern LLMs (LLaMA 2/3, Qwen, Mistral, etc.).