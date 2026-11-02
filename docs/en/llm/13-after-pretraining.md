---
description: Compare full fine-tuning, LoRA, retrieval-augmented generation, and inference. Learn how prefill, decoding, and KV caching support model serving.
---

# After pretraining {#after-pretraining}

Pretraining gives an LLM broad language patterns and knowledge, but it does not automatically optimize the model for every task or give it access to newly published or private information. Additional training and external information can help.

## Fine-tuning {#fine-tuning}

Suppose you want consistent analysis of contracts, identifying clauses that deserve legal review. A general model may attempt this from a prompt, but examples of your specific review criteria could improve consistency.

**Fine-tuning** continues training a pretrained model on additional data for a particular purpose. It generally requires less data and computation than starting from scratch.

For the contract task, training examples could pair documents with annotated clauses. The model adjusts its weights to reflect patterns in those demonstrations.

![Annotated contract-review examples are used to fine-tune a model](../assets/images/llm/en/13-fine-tuning-example.svg){ .neural-network-image .after-pretraining-image }

Fine-tuning can adapt task behavior, domain language, response style, or output format. Its benefit still needs to be evaluated on relevant held-out examples.

### Full fine-tuning {#full-fine-tuning}

**Full fine-tuning** updates all the model’s weights. This offers broad flexibility, but large models require substantial GPU memory and computation. Storing a complete model for every task also consumes space.

### LoRA {#low-rank-adaptation}

**Parameter-efficient fine-tuning (PEFT)** trains a smaller set of parameters while leaving most of the pretrained model unchanged.

A prominent method is **LoRA (Low-Rank Adaptation)**. It freezes the original weights and learns an update represented by two smaller matrices.

![LoRA freezes pretrained weights and learns matrices A and B](../assets/images/llm/13-lora-figure1.png){ .neural-network-image .after-pretraining-image style="width: min(100%, 25rem);" }

<p style="text-align: center;"><em><a href="https://arxiv.org/abs/2106.09685">LoRA: Low-Rank Adaptation of Large Language Models, Figure 1</a></em></p>

In the diagram, the original weight path stays fixed. Matrices `A` and `B` form the trainable update path. For a square projection, `A` maps dimension `d` to a smaller dimension `r`, and `B` maps back to `d`. More generally, projections may have different input and output dimensions.

The **rank setting `r`** is normally much smaller than the original dimensions. A `1000 × 1000` update has one million entries. Two factors of sizes `1000 × 8` and `8 × 1000` contain just 16,000 entries.

![A low-rank update requires far fewer trainable values than a full update](../assets/images/llm/en/13-lora-parameter-comparison.svg){ .neural-network-image .after-pretraining-image }

The model combines its original output with the learned update’s contribution. We can save just the **LoRA adapter weights**, keeping one base model rather than a full copy for every task.

For example, separate adapters can support contract review, customer support, and summarization:

![Task-specific LoRA adapters share one frozen base model](../assets/images/llm/en/13-lora-task-adapters.svg){ .neural-network-image .after-pretraining-image }

## Retrieval-augmented generation {#retrieval-augmented-generation}

A model’s internal knowledge has limitations:

1. **It may be outdated.** Events after training are not automatically incorporated into frozen weights.
2. **It may not include private material.** Internal documents and organization-specific information may never have appeared in training.
3. **It may hallucinate.** Plausible text is not a guarantee of factual accuracy.

A model can accept a false premise and invent supporting details. Here is a deliberately fictional example, rather than a quotation of a documented model response:

<div class="hallucination-example" aria-label="Illustrative fabricated answer to an impossible historical question">
<p class="hallucination-example__notice">Illustrative hallucination</p>
  <div class="hallucination-example__message hallucination-example__message--user"><b>👤 User</b>Tell me about Shakespeare’s famous incident involving a broken laptop.</div>
  <div class="hallucination-example__message hallucination-example__message--assistant"><b>🤖 AI</b>Shakespeare broke his laptop while revising Hamlet, delaying the play’s first performance.</div>
</div>

Laptops did not exist in Shakespeare’s lifetime. Fluent wording can still describe an impossible event.

Instead of relying only on internal weights, we can **retrieve relevant external information and provide it as context**. This is **retrieval-augmented generation (RAG)**.

The main stages are **retrieval** and **generation**. Search external documents for information related to the question, then send the question and retrieved material to the LLM.

For an employee asking about leave policy:

![A RAG system retrieves relevant company documents and supplies them with the question](../assets/images/llm/en/13-rag-retrieval-flow.svg){ .neural-network-image .after-pretraining-image style="width: min(100%, 48rem);" }

The model can use current or private sources without retraining its weights. Good retrieval and grounded generation can improve reliability, but RAG does not eliminate hallucination or guarantee that the retrieved information is correct.

## Using a trained model {#inference}

Trained weights are stored in files. Their numbers collectively encode learned patterns, but reading them is not like reading ordinary source code. Knowledge is distributed across many interacting values.

A rough analogy is that looking at a brain does not directly reveal a person’s thoughts. Individual weights rarely correspond neatly to one understandable fact.

A serving system loads weights onto suitable hardware and runs the model on new inputs. This execution is **inference**.

![A trained model is loaded onto a computer to process prompts and generate responses](../assets/images/llm/en/13-inference-model-loading.svg){ .neural-network-image .after-pretraining-image }

For comparable computations, inference avoids backpropagation and parameter updates, so it is lighter than training. But a large service generates enormous numbers of tokens for many users; total inference demand can still be substantial.

A [September 2026 analysis by Epoch AI](https://epoch.ai/latest/introducing-the-ai-chip-users-explorer) estimated that OpenAI’s 2025 compute use was divided roughly evenly between R&D and inference. It illustrates that serving existing models can require resources on a scale comparable to developing them; it is an estimate, not a disclosed internal accounting.

## From prompt to response {#prefill-decoding}

Why can a long prompt take time before the first token appears, while the answer then streams out gradually? Standard autoregressive inference has two stages: **prefill** and **decoding**.

During **prefill**, the model processes the prompt tokens: embeddings, attention, and other layer operations. Positions can be processed in parallel within each layer because the prompt is already available, while causal masks still restrict which positions can consult which others.

Longer prompts require more work, which can increase time to the first generated token.

During **decoding**, the model generates a token, incorporates it, and predicts the next. Future output tokens are not available in advance, so standard generation proceeds sequentially.

![Prefill processes the available prompt, while decoding generates tokens sequentially](../assets/images/llm/en/13-prefill-decoding.svg){ .neural-network-image .after-pretraining-image }

Repeating every previous token’s key and value calculations would be wasteful. A **KV cache** stores those vectors and reuses them.

In [self-attention](08-transformer.md#self-attention), a new query consults keys and values from allowed previous positions. Prefill builds the prompt’s cache; subsequent decoding steps use it and append the newly processed token’s keys and values.

![Cached keys and values are reused, and new token entries are appended](../assets/images/llm/en/13-kv-cache.svg){ .neural-network-image .after-pretraining-image }

Caching avoids recomputing the earlier keys and values, although attending over an increasing cache still requires work and memory.

## :material-pencil: Exercises {#exercises}

Decide whether each statement is **True** or **False**.

1. Full fine-tuning updates all the pretrained model’s weights.
2. LoRA learns a small added parameter set while keeping base weights frozen.
3. RAG can supply retrieved information without retraining the language model.
4. Ordinary inference updates model weights through backpropagation for every answer.
5. A KV cache reuses previously calculated keys and values.

??? success "Answers and explanations"
    1. **True** — Full fine-tuning adapts the entire parameter set.
    2. **True** — Low-rank factors represent the weight update.
    3. **True** — Retrieved material becomes context.
    4. **False** — Ordinary inference uses fixed weights and forward computation.
    5. **True** — Reuse reduces repeated work during generation.
