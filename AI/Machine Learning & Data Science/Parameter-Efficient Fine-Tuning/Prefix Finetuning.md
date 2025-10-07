Prefix Finetuning is a **Parameter-Efficient Fine-Tuning (PEFT)** method for adapting large, pre-trained **Transformer-based models** to specific downstream tasks, introduced in [[2021 - Prefix Tuning]]. Instead of updating all the weights of the model (which is computationally expensive), Prefix Finetuning freezes the original model's parameters and only trains a small, continuous, task-specific vector, known as a "prefix."

This prefix is prepended to the input of each layer of the transformer model. The model then attends to this prefix as if it were a set of "virtual tokens," allowing it to learn task-specific behaviour without altering its core knowledge. 
## How it Works
1.  **Freeze Transformer Parameters**: The vast majority of the pre-trained model's weights are not changed.
2.  **Introduce a Prefix**: A small, trainable matrix of parameters (the prefix) is added.
3.  **Prepend to Transformer Layers**: For each layer in the transformer, this prefix is prepended to the sequence of key and value vectors for the multi-head attention mechanism.
4.  **Train Only the Prefix**: During finetuning, only the parameters of the prefix are updated. The model learns to condition its output on this prefix to solve the target task.

![[Pasted image 20251007094355.png]]

## Key Advantages
-   **Parameter Efficiency**: It requires training only a tiny fraction of the parameters (e.g., ~0.1% of the total), drastically reducing memory and storage costs.
-   **No Model Retraining**: Since the base model is frozen, you don't need to store a full copy of the model for each new task. You only need to store the small prefix.
-   **Modularity**: You can train multiple prefixes for different tasks and easily swap them out as needed without affecting the base model.
-   **Comparable Performance**: It has been shown to achieve performance comparable to full finetuning on many tasks, especially with limited data.
### Prefix Finetuning vs. Other Methods
-  **Full Finetuning**: Modifies all model weights. Computationally expensive and requires storing a new model for each task.
-  **[[Prompt Tuning]]**: A simpler version where only a soft prompt (a continuous vector) is prepended to the *input embedding layer*. Prefix Finetuning is more expressive as it adds trainable parameters to *every* layer.
-   **Adapter Tuning**: Inserts small, trainable "adapter" modules between the layers of the pre-trained model.
