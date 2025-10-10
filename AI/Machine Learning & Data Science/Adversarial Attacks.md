Adversarial attacks refer to techniques used to manipulate the input data to machine learning models, particularly deep neural networks, in a way that the changes are either imperceptible or very subtle to humans but can cause the model to make incorrect predictions or classifications. The manipulated input data is termed as an "adversarial example."

Adversarial attacks are particularly concerning for many reasons:
1. **Imperceptibility**: The changes made to the input are often so small that humans wouldn't notice them, yet they can drastically alter a model's output.
2. **Transferability**: Adversarial examples generated for one model can sometimes fool other models, even if they have different architectures or were trained on different datasets.
3. **Potential Impact**: The existence of adversarial attacks raises concerns about the robustness and trustworthiness of machine learning models, especially in critical applications like medical imaging, autonomous driving, and security systems.

Types of Adversarial Attacks:
1. **White-box Attacks**: The attacker has full knowledge of the model, including its architecture, weights, training data, and other parameters. With this knowledge, they craft adversarial examples specifically designed to fool the model.
2. **Black-box Attacks**: The attacker has limited knowledge about the model. They might only know the model's input and output but not its internal details. Despite this limited knowledge, they can still generate adversarial examples, often by training surrogate models or utilising transferability.
3. **Targeted Attacks**: The aim is to make the model produce a specific wrong output.
4. **Untargeted Attacks**: The aim is merely to make the model produce any incorrect output.

Methods to Craft Adversarial Examples:
1. **Fast Gradient Sign Method (FGSM)**: This method computes the gradient of the loss concerning the input data, then creates the adversarial example by adding a small fraction of the sign of the gradient to the original input.
2. **DeepFool**: Iteratively perturbs the input to cross the decision boundary.
3. **Jacobians-based Saliency Map Attack (JSMA)**: Focuses on a small subset of input features to modify, determining which ones to perturb based on the Jacobian matrix of the model's output concerning its input.

Defense Mechanisms:
Given the potential risks of adversarial attacks, researchers have proposed various defenses:
1. **Adversarial Training**: Incorporating adversarial examples in the training data, thereby making the model more robust to such inputs.
2. **Model Ensembling**: Using a collection of models for predictions to reduce the impact of adversarial examples.
3. **Input Preprocessing**: Applying transformations like denoising, smoothing, or quantisation to input data to reduce the impact of adversarial perturbations.
4. **Gradient Masking or Obfuscation**: Altering the model or its training process to make it harder for attackers to compute meaningful gradients.

However, the arms race between adversarial attacks and defenses is ongoing. Many proposed defenses have been later shown to be ineffective against more sophisticated or adaptive attacks. The field continues to be an active area of research, balancing between the creation of more powerful attacks and the development of robust defenses.