---
description: Follow the path from recurrent networks to attention and transformers. Learn how queries, keys, and values create context-aware token representations.
---

# Connecting context with transformers

In 2017, researchers at Google published [*Attention Is All You Need*](https://arxiv.org/pdf/1706.03762), introducing the **transformer**. Its attention-centered architecture helped overcome limitations of earlier sequence models and became a foundation for modern LLMs.

## Reading in sequence: RNNs {#rnn}

Before transformers, **recurrent neural networks (RNNs)** were widely used to analyze and generate text. A recurrent connection carries information from one processing step to the next.

At each step, the network combines the current token with information from previous steps, creates a new hidden state, and passes it onward.

![An RNN passes its hidden state from one time step to the next](../assets/images/llm/en/08-rnn-overview.svg){ .neural-network-image .transformer-image }

We index steps by `t`. The current input `x⁽ᵗ⁾` and previous hidden state `h⁽ᵗ⁻¹⁾` determine the new state `h⁽ᵗ⁾`, which summarizes information read so far.

For a simple translation example, take the German sentence **“Ich trinke Kaffee”** (“I drink coffee”). Treating words as tokens for illustration, the RNN updates its state three times:

![The RNN reads Ich, trinke, and Kaffee sequentially](../assets/images/llm/en/08-rnn-three-steps.svg){ .neural-network-image .transformer-image }

Early translation systems often paired two RNNs. The **encoder** read the source and compressed it into a final **context vector**. The **decoder** used that summary and previously generated words to produce a translation.

![An RNN encoder summarizes German input and a decoder generates an English translation](../assets/images/llm/en/08-rnn-encoder-decoder.svg){ .neural-network-image .transformer-image }

`<sos>` and `<eos>` mark the start and end of a sequence. Tokens above the decoder are its inputs; those below are its predicted outputs.

Using the context vector and `<sos>`, the decoder predicts `I`. Feeding `I` into the next step leads to `drink`, then `coffee`, and finally `<eos>`. It generates the translation sequentially, using information carried from the source.

## RNN limitations {#rnn-limitations}

Three limitations matter here:

- **Long-term dependencies:** repeated state updates can weaken information from much earlier tokens, making distant relationships difficult to learn.
- **A vector bottleneck:** compressing an entire source sentence into one fixed-size summary can lose details, especially for long inputs.
- **Limited parallelism within a sequence:** a step depends on the previous hidden state, so it cannot simply be calculated simultaneously with all other steps. Large-scale training becomes slower and more expensive.

## Attention Is All You Need {#attention-is-all-you-need}

The transformer paper did not invent attention. In 2014, Dzmitry Bahdanau and colleagues proposed attention for neural translation in [*Neural Machine Translation by Jointly Learning to Align and Translate*](https://arxiv.org/pdf/1409.0473).

The transformer’s key contribution was to **remove recurrence and organize the network around attention**.

### Attention {#attention}

**Attention** calculates which available information is most relevant at a particular step and combines it accordingly.

An intuitive analogy is translating a sentence: you focus on different source words as you produce different parts of the translation. Bahdanau has described language-learning experience as an inspiration for this perspective.

Instead of relying on one fixed source summary, an attention-equipped decoder consults **different encoder states with different weights at each output step**.

![Attention lets a translation decoder consult the encoder’s individual states](../assets/images/llm/en/08-rnn-attention.svg){ .neural-network-image .transformer-image }

When generating `coffee`, for example, the decoder can emphasize the encoder state for `Kaffee`. It scores the encoder states against its current state, then normalizes the scores into weights summing to `1`.

With illustrative weights `0.1`, `0.7`, and `0.2`, the middle source token `trinke` contributes most to that particular weighted combination. The numbers illustrate the calculation rather than a required translation alignment. In a real trained model, the weights depend on the learned representations and current output step.

![A context vector is the weighted sum of encoder hidden states](../assets/images/llm/en/08-attention-weighted-context.svg){ .neural-network-image .transformer-image }

### Self-attention {#self-attention}

Attention relieved the fixed-vector bottleneck, but an RNN encoder still processed its input sequentially.

What if tokens within the same sequence could consult one another directly? **Self-attention** does exactly that, including allowing a token to consult itself.

Each token gathers information from other tokens according to their relevance and forms a new, contextual representation. Distant tokens can interact directly rather than through many recurrent updates. Multiple positions can also be processed in parallel when their inputs are available.

### Queries, keys, and values {#query-key-value}

To understand this calculation, we need **queries, keys, and values (Q, K, V)**.

Consider `bank` in “I withdrew money from the bank” and “We sat on the river bank.” The surrounding words distinguish a financial institution from the edge of a river.

![Money and river context give bank different meanings](../assets/images/llm/en/08-bank-context.svg){ .neural-network-image .transformer-image }

Self-attention decides **which information to consult and how much of it to gather**. It transforms each input vector into three representations:

![Queries identify what is sought, keys enable matching, and values carry information](../assets/images/llm/en/08-qkv-roles.svg){ .neural-network-image .transformer-image }

Multiplication by three learned matrices, `W_Q`, `W_K`, and `W_V`, creates the query, key, and value. One token plays all three roles, using **different vectors for each role**.

![A token vector is projected into query, key, and value vectors](../assets/images/llm/en/08-qkv-projection.svg){ .neural-network-image .transformer-image }

For each query, compute [dot products](05-high-dimensional-learning.md#learning-and-vectors) with the keys. Divide by `√dₖ`, where `dₖ` is key dimension, to moderate score scale. Apply [softmax](07-probabilistic-language-modeling.md#context) to obtain attention weights summing to `1`.

![Scaled dot-product attention applies softmax weights to the values](../assets/images/llm/en/08-attention-formula.svg){ .neural-network-image .transformer-image }

The `T` in `QKᵀ` means **transpose**, exchanging rows and columns. Matrix multiplication calculates the query-key comparisons for all token pairs together.

Consider “Every morning before work I drink coffee.” To update the representation of `drink`, compare its query with all token keys. In the illustration, `coffee` receives the highest weight, while the other tokens contribute smaller amounts.

![Illustrative attention weights from drink to the surrounding tokens](../assets/images/llm/en/08-attention-weights-example.svg){ .neural-network-image .transformer-image }

Multiply each value vector by its attention weight and add them. The result is a new representation of `drink` enriched by relevant context. This context-dependent **transformation** is a defining feature of transformers.

Full self-attention compares `n` tokens against `n` tokens, creating `n²` pairwise scores. Computation and memory therefore grow rapidly with sequence length. Models impose a **context window**, the maximum amount of context they can process in a request under their supported configuration.

![A context window bounds the tokens considered together](../assets/images/llm/en/08-context-window.svg){ .neural-network-image .transformer-image }

A larger window can include more information, but it also has costs. Window sizes and attention implementations vary by model, so practical systems balance context needs with resource use.

We now have the core ideas needed to examine how the transformer’s components fit together.

## :material-pencil: Exercises {#exercises}

Decide whether each statement is **True** or **False**.

1. *Attention Is All You Need* first introduced attention itself.
2. An RNN depends on previous hidden states and therefore processes positions sequentially.
3. Self-attention can include a token’s own information.
4. A larger query-key dot product produces a larger relevance score before normalization.
5. Self-attention can directly compare distant tokens within its allowed context.

??? success "Answers and explanations"
    1. **False** — Earlier work, including Bahdanau’s translation model, used attention.
    2. **True** — Recurrence limits parallel computation within a sequence.
    3. **True** — A position can attend to itself when the mask permits it.
    4. **True** — The dot product is the basis of the score.
    5. **True** — Distance alone does not require intervening recurrent steps.
