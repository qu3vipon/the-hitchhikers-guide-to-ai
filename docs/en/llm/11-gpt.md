---
description: Explore decoder-only GPT models, autoregressive generation, GPT-2 blocks, and the supervised fine-tuning and human feedback behind early ChatGPT.
---

# Transformers in conversation

We now know the original transformer’s components. Let’s connect them to the large language models we use today.

## A decoder-based language model: GPT {#gpt}

The original transformer used an encoder and decoder for translation. Researchers also applied transformers to **language modeling**, including predicting the next token from preceding tokens. Repeating that prediction generates new text.

!!! info "Translation and language modeling"
    **Translation** conditions on a source and the target prefix: `Ich trinke Kaffee + I drink` → `coffee`. The original transformer uses an encoder for the source and a decoder for the target.

    A **decoder-only language model** predicts from a text prefix: `I drink` → `coffee`. It does not require a separate encoder for a source sentence.

A prominent decoder-only family is **GPT: Generative Pre-trained Transformer**. It is pretrained on large amounts of text and uses that learning to generate continuations.

Beginning with OpenAI’s first GPT in 2018, GPT-2 and GPT-3 increased scale and capabilities. Many later generative LLMs share the decoder-only, next-token-prediction foundation, despite differences in their details.

We will use **GPT-2** as a concrete architectural example. The left of the diagram shows the complete flow; the right expands a repeated block.

![The GPT architecture from input tokens through transformer blocks to next-token prediction](../assets/images/llm/en/11-gpt-architecture-overview.svg){ .neural-network-image .chatgpt-image style="width: min(100%, 34rem);" }

<p style="text-align: center;"><em><a href="https://en.wikipedia.org/wiki/File:Full_GPT_architecture.svg">Full GPT architecture, CC0</a></em></p>

There is no separate encoder and therefore no encoder-decoder cross-attention. But GPT certainly has inputs: **the text prefix goes directly into its decoder stack**. User text and generated text become part of the continuing token sequence, with role or boundary tokens where the model’s format requires them.

For example, `Every morning I drink` might generate `coffee`. Append that token, then predict the next one. Generating each new token from the prefix and earlier generated tokens is **autoregressive generation**.

## GPT’s transformer blocks {#gpt-transformer-block}

GPT blocks resemble the original decoder’s masked-attention and FFN components, with several important details.

### Dropout {#dropout}

![Dropout in the GPT architecture](../assets/images/llm/en/11-gpt-dropout-detail.svg){ .neural-network-image .chatgpt-image style="width: min(100%, 18rem);" }

**Dropout** also appeared in the original transformer implementation, even where the architecture drawing did not show it explicitly.

A model can fit training-specific patterns too closely and perform worse on unseen examples. This is **overfitting**.

Dropout randomly sets some intermediate outputs to `0` **during training**, discouraging dependence on a particular set of units. Think of a soccer player practicing with their weaker foot instead of always relying on their stronger one. The analogy illustrates varied practice, not a literal model of learning. Dropout is normally disabled during inference.

### Pre-LN {#pre-ln}

<div style="display: flex; align-items: center; justify-content: center; gap: 1rem; margin: 1.5rem auto; max-width: 37rem;">
  <img src="../assets/images/llm/en/11-gpt-pre-ln-detail.svg" alt="Layer normalization before attention, with the residual path" style="width: calc(50% - 0.5rem); height: auto;" />
  <img src="../assets/images/llm/en/11-gpt-pre-ln-ffn-detail.svg" alt="Layer normalization before the linear-GELU-linear feed-forward network" style="width: calc(50% - 0.5rem); height: auto;" />
</div>

**LayerNorm** is the layer normalization operation we saw in Add & Norm. GPT-2 changes its placement.

The original transformer normalizes after adding a sublayer output to its input. GPT-2 normally applies LayerNorm **before** attention or the FFN, then adds the sublayer output to the original input. This is **pre-layer normalization (Pre-LN)**.

The FFN’s `Linear → GELU → Linear` sequence follows the same pattern. A direct residual path lets the original representation bypass normalization and the sublayer.

![The Pre-LN residual path bypasses normalization and the computation block](../assets/images/llm/en/11-pre-ln-residual-connection.svg){ .neural-network-image .chatgpt-image style="width: min(100%, 34rem);" }

During backpropagation, this path also supports relatively direct gradient flow toward earlier layers, helping deeper stacks train stably.

### MatMul {#matmul}

![A matrix multiplication operation in GPT](../assets/images/llm/en/11-gpt-matmul-detail.svg){ .neural-network-image .chatgpt-image style="width: min(100%, 18rem);" }

**MatMul** means **matrix multiplication**. Q, K, and V projections are examples. Packing multiple token vectors into a matrix lets hardware calculate many operations together rather than processing each vector separately.

!!! info "GPUs"
    A **CPU (Central Processing Unit)** handles general computation. A **GPU (Graphics Processing Unit)** is particularly effective for large amounts of suitable parallel arithmetic. Originally developed for graphics, GPUs became central to deep learning because operations such as matrix multiplication map well onto their hardware.

### GELU {#gelu}

![GELU in GPT’s feed-forward sublayer](../assets/images/llm/en/11-gpt-gelu-detail.svg){ .neural-network-image .chatgpt-image style="width: min(100%, 18rem);" }

GPT-2 uses **GELU (Gaussian Error Linear Unit)** rather than the original transformer’s ReLU. GELU smoothly modulates inputs instead of cutting all negative values to zero. Some negative outputs remain, and the function changes smoothly.

![ReLU and GELU compared](../assets/images/llm/en/11-gelu-activation-function.svg){ .neural-network-image .chatgpt-image }

## ChatGPT {#chatgpt}

Pretraining teaches GPT to continue text. Making it **follow instructions and hold useful conversations** takes additional training.

**InstructGPT** adapted GPT-3 using **supervised fine-tuning (SFT)** and **reinforcement learning from human feedback (RLHF)**.

SFT supplies examples of desirable responses. For instance, pair “What is the capital of France?” with “The capital of France is Paris.” Training on instruction-answer pairs teaches the model response patterns.

![Supervised fine-tuning uses examples of good answers](../assets/images/llm/en/11-sft-learning.svg){ .neural-network-image .chatgpt-image }

But many answers can be acceptable, and some are more useful than others. RLHF incorporates **human preferences between responses**.

People compare model-generated answers. Their rankings train a **reward model** that predicts preferred responses. Reinforcement learning then adjusts the language model toward higher reward, usually with constraints discouraging excessive departure from the starting model.

![Human response preferences train a reward model used for reinforcement learning](../assets/images/llm/en/11-rlhf-learning.svg){ .neural-network-image .chatgpt-image }

SFT says, “Here is an example of a good response.” Preference-based training adds, “This response is better than that one.” Neither guarantees that every output is correct.

Released in 2022, early **ChatGPT** used a GPT-3.5-series model, dialogue demonstrations written by human trainers, and RLHF. This adapted next-token prediction to following requests and using conversation context.

GPT and early ChatGPT’s underlying models therefore share the decoder-only foundation. Additional training makes the model more suitable for dialogue; it does not replace autoregressive generation.

## How LLMs emerged {#llm}

LLMs did not appear in one sudden invention. They combine advances in architecture, training, large datasets, and computation.

Recall the [three ingredients](01-machine-learning.md#three-elements-of-learning): **data, a model, and a learning method**. Transformers supplied a powerful architecture; pretraining, fine-tuning, and preference-based learning supplied training methods; large text collections supplied data.

Their interaction helped produce today’s language models.

![Data, model architecture, and learning methods combine to produce an LLM](../assets/images/llm/en/11-llm-three-elements.svg){ .neural-network-image .chatgpt-image }

## :material-pencil: Exercises {#exercises}

Decide whether each statement is **True** or **False**.

1. GPT adds generated tokens to its prefix when predicting subsequent tokens.
2. Standard decoder-only GPT uses encoder-decoder cross-attention.
3. Pre-LN applies normalization before attention or the FFN.
4. SFT can use human-written instruction-answer pairs.
5. RLHF incorporates feedback about which answers people prefer.

??? success "Answers and explanations"
    1. **True** — This is autoregressive generation.
    2. **False** — There is no separate source encoder in this architecture.
    3. **True** — Normalization precedes each main sublayer.
    4. **True** — Demonstrations teach desired response behavior.
    5. **True** — Preferences guide additional training.
