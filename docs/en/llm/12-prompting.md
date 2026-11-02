---
description: Understand prompts, message roles, conversation context, few-shot examples, structured prompts, and prompt chaining.
---

# Giving instructions to LLMs {#prompting}

## Prompts {#prompt}

An LLM predicts tokens from its context. The same model can produce very different answers depending on what you provide and how you present it.

That input is the **prompt**. It may contain a question, background material, a task, constraints, and an expected output format.

These details affect the next-token distribution. **Which information and conditions you supply** can therefore change both an answer’s content and its form.

![A prompt provides context for the model’s next-token prediction](../assets/images/llm/en/12-prompt-role.svg){ .neural-network-image }

## Types of messages {#prompt-types}

Chat models commonly distinguish messages by **role**, including system, user, and assistant. The role is part of the model’s input format, so the same text can be treated differently depending on where it appears. Exact roles and conventions vary by service.

![System, user, and assistant messages have different roles](../assets/images/llm/en/12-message-roles.svg){ .neural-network-image }

### System prompts {#system-prompt}

A system prompt sets **the model’s role and overall behavior**. Examples include “Answer in clear English” or “Use respectful language.”

The service developer usually supplies these instructions. Users do not need to repeat them with every question, and they may not see the system prompt directly.

### User prompts {#user-prompt}

A user prompt is **the user’s question or request**. It can specify a task—“Summarize this in three sentences”—and supply source material or constraints. Clear instructions help communicate the desired result.

### Assistant messages {#assistant-message}

Assistant messages are **the model’s responses**. A chat service can include earlier user and assistant messages in later requests, allowing the model to continue the conversation.

### A conversation example {#chat-example}

These roles work together. The user might enter:

<div class="chat-user-message-wrap">
  <div class="chat-user-message" aria-label="Example user input"><span class="chat-user-message__role">User</span>What is machine learning?</div>
</div>

The service may also provide a system prompt. The model uses both when generating its response.

<div class="chat-exchange" aria-label="Example system instruction, user question, and assistant response">
  <div class="chat-exchange__system"><div class="chat-exchange__system-content"><span class="chat-exchange__role">System</span>Answer in clear English. Use respectful language.</div></div>
  <div class="chat-exchange__message chat-exchange__message--user"><span class="chat-exchange__role">User</span>What is machine learning?</div>
  <div class="chat-exchange__message chat-exchange__message--assistant"><span class="chat-exchange__role">Assistant</span>It is a way for computers to learn patterns from data.</div>
</div>

## Conversation context {#context}

Suppose you are planning a trip with a friend and ask, “What about Saturday?” Earlier messages tell your friend that you mean a travel date.

**Context** is the information needed to interpret a message. For an LLM, it is the material available when generating the current response.

After “What is machine learning?”, a request such as “Explain it more simply” makes sense because **earlier messages are included again with the new request**. The model can then identify what “it” refers to.

<div class="context-input-flow" aria-label="Conversation history and a new message form the model input; the answer becomes part of later context">
  <div class="context-input-flow__sources">
    <div class="context-input-flow__history">
      <span class="context-input-flow__title">Conversation history</span>
      <div class="context-input-flow__message context-input-flow__message--system"><b>System</b>Answer in clear English.</div>
      <div class="context-input-flow__message context-input-flow__message--user"><b>User</b>What is machine learning?</div>
      <div class="context-input-flow__message context-input-flow__message--assistant"><b>Assistant</b>Learning patterns from data.</div>
    </div>
    <div class="context-input-flow__plus">+</div>
    <div class="context-input-flow__current">
      <span class="context-input-flow__title">New user message</span>
      <div class="context-input-flow__message context-input-flow__message--user"><b>User</b>Explain it more simply.</div>
    </div>
  </div>
  <div class="context-input-flow__arrow">↓</div>
  <div class="context-input-flow__input"><b>LLM</b></div>
  <div class="context-input-flow__arrow">↓</div>
  <div class="context-input-flow__new-answer">
    <span class="context-input-flow__title">New response</span>
    <div class="context-input-flow__answer"><b>Assistant</b>A computer learns useful rules by looking at examples.</div>
  </div>
</div>

Context can also include documents, user-provided material, and information retrieved by tools. Missing relevant facts can reduce answer quality; excessive irrelevant material can distract from what matters.

Selecting, organizing, and retaining useful information is **context management**. As a task or conversation grows, the service must decide what to preserve, omit, or summarize. Some services compress older conversation into a summary.

Context size also affects processing time and cost. Good management aims to improve **both answer quality and efficiency**.

## Common prompting techniques {#prompting-techniques}

Useful prompting involves choosing not just what to ask, but which information, examples, and constraints to include.

### Few-shot prompting {#few-shot-prompting}

**Few-shot prompting** supplies a few examples of the desired input-output pattern.

For example, ask for marketing copy from keywords:

> Use the examples to write a short tagline for the final set of keywords.

> **Keywords:** coffee, morning, energy\
> **Tagline:** Wake up to a brighter morning.
>
> **Keywords:** travel, freedom, discovery\
> **Tagline:** Leave the familiar. Find something new.
>
> **Keywords:** exercise, health, habit\
> **Tagline:**

Examples communicate style, length, and how to combine the inputs. Choose examples that resemble the real task; different demonstrations can produce different results.

### Structured prompting {#structured-prompting}

A **structured prompt** separates elements such as role, goal, background, constraints, and output format.

A short instruction may suffice for a simple task. For a complex one, structure makes requirements easier for both the model and the person writing the prompt to inspect.

> **Role:** Travel planner<br>
> **Goal:** Plan a three-day trip to Edinburgh<br>
> **Travelers:** A family of four, including two older adults<br>
> **Constraints:** Visit no more than three attractions per day and minimize travel time<br>
> **Output:** A table with morning, afternoon, and evening activities for each day

There is no mandatory template. The purpose is to make the task and its requirements clear.

### Prompt chaining {#prompt-chaining}

**Prompt chaining** divides a complex task into stages and uses earlier outputs in later prompts.

For a report based on long source material:

1. Extract key points.
2. Build an outline from those points.
3. Draft the sections.
4. Review and revise the report.

> Prompt 1 + `source material` → `key points`<br>
> Prompt 2 + `key points` → `outline`<br>
> Prompt 3 + `key points` + `outline` → `draft`<br>
> Prompt 4 + `draft` → review and revision

Intermediate results can be checked and corrected before continuing. However, multiple calls add complexity, latency, and cost, so chaining is most useful when the task genuinely benefits from stages.

## :material-pencil: Exercises {#exercises}

Decide whether each statement is **True** or **False**.

1. A prompt supplies input context for a generative LLM’s next-token prediction.
2. System prompts can set an overall role and behavior.
3. Earlier assistant messages can never be used to generate the next answer.
4. Few-shot prompting supplies examples of the desired task.
5. Structured prompting means putting every requirement into one uninterrupted sentence.

??? success "Answers and explanations"
    1. **True** — The input conditions the model’s generation.
    2. **True** — These instructions establish general guidance.
    3. **False** — Conversation history can be included in subsequent requests.
    4. **True** — Demonstrations communicate the intended pattern.
    5. **False** — Structure separates requirements into clear elements.
