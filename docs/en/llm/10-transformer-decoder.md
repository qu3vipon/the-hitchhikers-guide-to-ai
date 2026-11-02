---
description: Explore shifted decoder inputs, causal masking, cross-attention, and the logits and probabilities used to predict the next token.
---

# Inside the transformer: the decoder

Now let’s examine the decoder.

![The decoder in Figure 1 of Attention Is All You Need](../assets/images/llm/10-transformer-decoder-overview.png){ .neural-network-image .transformer-decoder-image style="width: min(100%, 22rem);" }

<p style="text-align: center;"><em><a href="https://arxiv.org/html/1706.03762v7">Vaswani et al., *Attention Is All You Need* (2017), Figure 1</a></em></p>

## Output embeddings {#output-embedding}

The decoder also converts tokens to vectors. The encoder receives the source sentence, while the decoder receives the beginning of the target translation.

Suppose “Ich trinke Kaffee” should translate to `I drink coffee`. During training, place a beginning-of-sequence token, `<BOS>`, before the target. The decoder input omits the final `<EOS>` token, while the prediction targets include it.

![Decoder inputs are shifted one position relative to their prediction targets](../assets/images/llm/en/10-decoder-shifted-input.svg){ .neural-network-image .transformer-decoder-image }

This is **shifted-right input**. `<BOS>` predicts `I`; `<BOS> I` predicts `drink`; `<BOS> I drink` predicts `coffee`; and the full prefix predicts `<EOS>`.

Target token IDs select embedding vectors through the **output embedding** table. “Output” refers to the target-language tokens, even though these vectors are inputs to the decoder. Positional encoding supplies order before the vectors reach the blocks.

## Masked multi-head attention {#masked-multi-head-attention}

![The decoder’s masked multi-head attention sublayer](../assets/images/llm/10-transformer-decoder-masked-attention-detail.png){ .neural-network-image .transformer-decoder-image style="width: min(100%, 18rem);" }

The first decoder sublayer uses **masked multi-head self-attention**. It resembles encoder attention, but **a position cannot consult future tokens**.

For `<BOS> I drink coffee`, the `drink` position can consult `<BOS>`, `I`, and itself, but not `coffee`.

Instead of deleting future tokens, a causal mask sets their attention scores to **negative infinity (`−∞`)** before softmax. Their resulting weights become `0`. This preserves the matrix structure while preventing access to future answers.

Attention is followed by Add & Norm, as in the encoder.

## Cross-attention {#cross-attention}

![The decoder attends to encoder outputs through cross-attention](../assets/images/llm/10-transformer-decoder-cross-attention-detail.png){ .neural-network-image .transformer-decoder-image style="width: min(100%, 18rem);" }

**Cross-attention** lets the decoder consult the source representations from the encoder.

Unlike self-attention, its queries and keys/values come from different streams: **Q comes from the decoder; K and V come from the encoder**.

![Decoder representations produce Q, while encoder representations produce K and V](../assets/images/llm/en/10-cross-attention-qkv.svg){ .neural-network-image .transformer-decoder-image }

Learned projections create the vectors. Query-key comparisons determine which source information is useful for the translation so far. While predicting `coffee`, the decoder might place a high weight on the source token `Kaffee`.

Another Add & Norm and the FFN complete the remaining processing, using the same basic principles as the encoder.

## Predicting the next token {#next-token}

![A linear projection and softmax produce next-token probabilities](../assets/images/llm/10-transformer-decoder-prediction-detail.png){ .neural-network-image .transformer-decoder-image style="width: min(100%, 15rem);" }

The final decoder representation at each position predicts the next token. A **linear layer** produces one [logit](07-probabilistic-language-modeling.md#context) per vocabulary item.

For a 37,000-token vocabulary, it produces 37,000 scores: perhaps `coffee: 4.2`, `tea: 2.1`, and `apple: 0.7`. These are not probabilities yet.

**Softmax** converts them to probabilities summing to `1`. Given `<BOS> I drink`, `coffee` might receive a high probability.

At generation time, select a token from this distribution, append it to the decoder input, and repeat. This builds the translation one token at a time.

## The transformer’s versatility {#transformer-versatility}

AI researcher and educator Andrej Karpathy discussed transformers in a [Stanford CS25 lecture](https://www.youtube.com/watch?v=XfpMkf4rD6E). He suggested describing the transformer as a general-purpose, efficient, optimizable computer rather than only an attention-based translation model.

The architecture is **not limited to language**. It has been adapted to images, speech, video, and robotics. Represent information as a suitable sequence, and the core ideas can apply beyond text.

## :material-pencil: Exercises {#exercises}

Decide whether each statement is **True** or **False**.

1. Training decoder inputs begin with `<BOS>` followed by target tokens.
2. Causal attention prevents a position from consulting later tokens.
3. Cross-attention uses decoder queries and encoder keys and values.
4. The linear layer directly outputs probabilities summing to `1`.
5. Transformers can process other kinds of data represented as sequences.

??? success "Answers and explanations"
    1. **True** — Inputs are shifted relative to prediction targets.
    2. **True** — Future attention scores are masked before softmax.
    3. **True** — This lets the decoder consult source information.
    4. **False** — The linear layer produces logits; softmax creates probabilities.
    5. **True** — Appropriate representations extend the architecture beyond language.
