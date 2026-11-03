---
description: Explore memory, chain-of-thought prompting, reasoning models, distillation, and multimodal systems. Distinguish memory from training and reasoning from inference.
---

# Modern LLMs {#modern-llms}

Language models have developed beyond basic text completion toward complex tasks and more personalized interactions. Some advances change the model; others change the surrounding service. Let’s distinguish them.

## What happens to information you provide? {#memory}

A chat service may remember preferences or important facts across conversations. This feature is often called **memory**.

Usually, the model does not independently remember every past conversation. The service stores selected information elsewhere and adds relevant entries to a later prompt.

![Stored preferences and a new question are combined into model context](../assets/images/llm/en/14-memory-context.svg){ .neural-network-image .modern-llm-image }

**Memory and training are different.** Training changes weights. A memory feature supplies saved information as context; remembering your name does not require updating model weights during the conversation.

This does not mean that the data you enter is never used to train models. Depending on the service, your input may be stored as conversation history or memory, and some services may use collected data for future model training or performance improvements. Whether your data is used in these ways depends on the service’s policies and your settings.

In other words, the information you enter is not learned in real time during a conversation, but it may be used to train models later. When using an LLM, **avoid entering personal or sensitive information without due care**. In particular, do not enter sensitive personal information such as government identification numbers, passwords, or financial details. Do not enter confidential company documents without first checking your organization’s security policies.

## Working through intermediate steps {#chain-of-thought}

Some tasks, such as arithmetic and coding, benefit from multiple intermediate steps. **Chain-of-thought (CoT) prompting** supplies or encourages intermediate solution steps before the final answer.

A [2022 paper](https://arxiv.org/abs/2201.11903) illustrated how a few worked examples could improve performance on multi-step tasks. Consider a similar problem:

> Roger has 5 tennis balls.  
> He buys 2 more cans, each containing 3 balls.  
> How many balls does he have now?

A worked example could show:

> Two cans add `2 × 3 = 6` balls.  
> Adding the original five gives `5 + 6 = 11`.  
> **Answer: 11 balls.**

Examples containing intermediate calculations can help a model apply a similar pattern to new problems.  
Such generated explanations are not guaranteed to expose the model’s actual internal computation, nor does a longer explanation guarantee correctness.

## The DeepSeek moment {#deepseek-shock}

DeepSeek’s January 2025 release of **DeepSeek-R1** attracted wide attention for its reasoning performance and questions about training efficiency. It challenged assumptions about how resources translate into capabilities.

The announcement also contributed to a sharp reassessment of AI infrastructure expectations in financial markets. The technical lesson is not that advanced AI is free to develop, but that architecture, training choices, and efficiency can matter alongside scale.

### Reasoning models {#reasoning-model}

CoT prompting uses instructions or demonstrations. **Reasoning models** also use training designed to improve performance on problems requiring intermediate work.

The [DeepSeek-R1 report](https://arxiv.org/abs/2501.12948) describes **R1-Zero**, an experiment applying reinforcement learning without first adding supervised reasoning demonstrations to the base model. Rewards based on answer correctness and format encouraged useful problem-solving behavior.

Earlier [RLHF](11-gpt.md#chatgpt) often emphasized a learned model of human preferences. R1-Zero instead highlighted **verifiable outcomes**, such as whether a math answer was correct. This could encourage checking and revising a solution without a person labeling every intermediate step. R1 itself used a broader training pipeline than R1-Zero.

!!! info "Reasoning versus inference"
    - **[Inference](13-after-pretraining.md#inference)** is running a trained model on inputs to obtain outputs.
    - **Reasoning** refers to intermediate calculation or logical work used to solve a problem.

    A reasoning model still performs inference when generating its response. The words describe different aspects of the process, not competing execution modes.

### Distillation {#distillation}

In chemistry, distillation separates and concentrates components of a mixture. In machine learning, **distillation** transfers useful behavior from a larger teacher model to a smaller student.

DeepSeek used generated solutions and answers from its larger model to train smaller models. The student learns problem-solving patterns from those examples.

![A teacher model generates solution data used to train a smaller student](../assets/images/llm/en/14-distillation.svg){ .neural-network-image .modern-llm-image }

This is not a literal copy of every fact in the teacher. It is learning from teacher-produced data, with the aim of retaining useful capabilities at a smaller scale.

## Beyond text {#multi-modal}

**Multimodal** systems work with different forms of information, such as text, images, audio, and video. Each form is a **modality**.

Show a cat image and ask “What animal is this?”, and a suitable multimodal model can connect the visual information with the question. Speech understanding and answering questions about video are other examples.

![A multimodal model combines a cat image with a text question](../assets/images/llm/en/14-multimodal.svg){ .neural-network-image .modern-llm-image }

The broad principle is to **convert different forms of information into vector representations that can interact**.

Text becomes token embeddings. Image and audio encoders extract representations appropriate to those signals. Additional projections or other mechanisms align them with the language model’s inputs. The exact design varies.

Combining these representations lets a model relate an image to a question or sound to text. LLM-based systems can therefore interact with more of the information people see and hear.

## :material-pencil: Exercises {#exercises}

Decide whether each statement is **True** or **False**.

1. Remembering a user preference always requires changing model weights during chat.
2. CoT prompting encourages only an immediate final answer with no intermediate work.
3. Reasoning is problem-solving work; inference is executing the trained model.
4. Distillation can train a smaller model using a larger model’s outputs.
5. Multimodal systems can combine information such as images and text.

??? success "Answers and explanations"
    1. **False** — A service can store preferences and supply them as context.
    2. **False** — CoT uses intermediate solution steps.
    3. **True** — They refer to different aspects of the process.
    4. **True** — Teacher-generated data can convey useful behavior.
    5. **True** — Representations of multiple modalities can be processed together.
