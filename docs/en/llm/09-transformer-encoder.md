---
description: Explore transformer encoder embeddings, positional encoding, multi-head attention, residual connections, layer normalization, and feed-forward networks.
---

# Inside the transformer: the encoder

Self-attention gives each token a contextual representation by consulting other tokens. A full transformer combines it with several other components. Let’s examine their roles.

## Transformer architecture {#transformer-architecture}

![The original transformer architecture from Attention Is All You Need, Figure 1](../assets/images/llm/09-transformer-architecture-overview.png){ .neural-network-image .transformer-encoder-image style="width: min(100%, 22rem);" }

<p style="text-align: center;"><em><a href="https://arxiv.org/html/1706.03762v7">Vaswani et al., *Attention Is All You Need* (2017), Figure 1</a></em></p>

The original transformer has an **encoder** on the left and a **decoder** on the right. The encoder builds contextual representations of the source tokens. The decoder uses them and the target tokens seen so far to predict the next target token.

The boxed sections are **encoder blocks** and **decoder blocks**. `N×` means that each block is repeated `N` times. The original paper evaluated this design on English–German and English–French translation.

We will start with the encoder.

## Input embeddings {#input-embedding}

![A token ID selects its vector from an embedding table](../assets/images/llm/en/09-token-id-to-embedding.svg){ .neural-network-image .transformer-encoder-image }

The model has a [vocabulary](07-probabilistic-language-modeling.md#context) of tokens, each assigned a unique **token ID**. An ID identifies a token; its numerical size does not express its meaning.

An **embedding table** maps each ID to a learned vector. In the original English–German model, a vocabulary of approximately 37,000 tokens used 512-dimensional embeddings.

Thus, even a token such as `apple` is represented by 512 numbers:

![An illustrative 512-component embedding for apple](../assets/images/llm/en/09-apple-embedding-vector.svg){ .neural-network-image .transformer-encoder-image }

Converting input tokens into these [embedding vectors](06-word-embeddings.md#meaningful-vectors) is the **input embedding** step.

## Input representations {#input-representation}

![Positional encoding is added to input embeddings](../assets/images/llm/en/09-transformer-input-embedding-balanced.svg){ .neural-network-image .transformer-encoder-image style="width: min(100%, 18rem);" }

A token embedding alone does not specify the token’s position. Self-attention needs positional information to distinguish ordering.

The original transformer adds a **positional encoding** to each embedding. “Dog bites man” and “Man bites dog” use the same words but mean different things. Position information helps the model distinguish them.

The embedding plus positional encoding forms the **input representation** passed to the encoder blocks.

## Multi-head attention {#multi-head-attention}

![The encoder’s multi-head attention sublayer](../assets/images/llm/09-transformer-encoder-attention-detail.png){ .neural-network-image .transformer-encoder-image style="width: min(100%, 18rem);" }

**Multi-head attention** performs several attention calculations in parallel, each using its own learned Q, K, and V projections. A **head** can learn different relationships: grammatical structure, reference, or long-range associations, for example. These are possibilities, not fixed roles assigned by the designer.

The attention output then reaches **Add & Norm**. A bypass path carries the sublayer’s original input there too: the **residual connection**.

A residual connection **adds a sublayer’s input to its output**. It preserves a direct route for information and gradients, helping deeper networks train effectively.

In the original transformer, Add & Norm first performs this addition, then applies **layer normalization**. For each token, normalization centers and scales its feature values using their mean and variance, with a small numerical stabilizer. Learned scale and shift parameters then adjust them. The operation helps stabilize training.

## Feed-forward networks {#feed-forward-network}

![The encoder’s feed-forward sublayer](../assets/images/llm/09-transformer-encoder-ffn-detail.png){ .neural-network-image .transformer-encoder-image style="width: min(100%, 18rem);" }

The next component is a **feed-forward network (FFN)**, a small [multilayer network](04-multilayer-perceptron.md#stacking-perceptrons).

Attention exchanges information between tokens. The FFN then transforms each contextual token vector **individually**, using the same learned network at every position. It does not consult other positions again in that sublayer.

!!! info "Why feed-forward?"
    Information travels through its layers toward the output without recurrent connections feeding a previous time step back into the calculation.

The FFN applies a **nonlinear transformation**, allowing richer representations than a stack of linear maps alone. The original model used [ReLU](03-perceptron.md#mechanical-decision-making), which maps negative values to `0` and passes nonnegative ones through.

Without nonlinear activations, any number of linear layers collapses into one linear map. Including biases gives one affine map. In one dimension, a linear map is a line through the origin; adding a bias can shift that line.

![A small feed-forward network with two inputs and two hidden units](../assets/images/llm/en/09-ffn-mlp-2x2.svg){ .neural-network-image .transformer-encoder-image }

For inputs `4` and `2`, expanding the calculations illustrates this collapse:

![Products of weights combine into a single effective linear transformation](../assets/images/llm/en/09-ffn-linear-formulas.svg){ .neural-network-image .transformer-encoder-image }

The coefficient ① `w₁w₅ + w₂w₆` multiplies `4`, so call it `W₁`. Similarly, ② `w₃w₅ + w₄w₆` multiplies `2`, so call it `W₂`. The entire computation becomes `y = 4W₁ + 2W₂`.

**Extra linear layers alone do not create a more expressive nonlinear function.** Activations such as ReLU prevent this collapse.

![Nonlinear activations let several simple boundaries combine into a more complex decision region](../assets/images/llm/en/09-linear-vs-nonlinear-decision-boundary.svg){ .neural-network-image .transformer-encoder-image }

An individual unit can define a simple straight boundary. Combining several units through nonlinear activations can create boundaries no single line could represent. The FFN uses this principle to further transform information gathered by attention.

The FFN output passes through another Add & Norm: add the FFN input through its residual path, then normalize.

Multi-head self-attention, the FFN, and their residual and normalization operations make one **encoder block**. The original transformer stacked six such blocks.

## :material-pencil: Exercises {#exercises}

Decide whether each statement is **True** or **False**.

1. An embedding’s dimension is the number of components representing one token.
2. Positional encoding helps distinguish sequences with the same tokens in different orders.
3. All attention heads share the same Q, K, and V projection weights.
4. A residual connection adds the original input to the transformed result.
5. Stacking linear layers without activations still produces one linear map.

??? success "Answers and explanations"
    1. **True** — A 512-dimensional vector contains 512 numbers.
    2. **True** — It supplies information about token position.
    3. **False** — Heads learn different projections.
    4. **True** — The bypass supports information and gradient flow.
    5. **True** — Biases make the combined map affine, but do not add nonlinearity.
