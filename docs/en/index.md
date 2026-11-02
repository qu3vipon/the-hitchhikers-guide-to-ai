# The Hitchhiker’s Guide to AI

AI has become a familiar part of everyday life. It answers questions, writes text, creates images, and sometimes handles tasks for us. Yet many people use AI every day without really understanding how it works.

When we work up the courage to learn about AI, we soon run into a wall. It seems to require specialized knowledge of computers, with complex mathematics and unfamiliar terms at every turn. Understanding AI can start to feel out of reach.

You can drive a car without knowing how its engine works. But understanding what makes it move can deepen your experience of driving—and be interesting in its own right. The same is true of AI. Knowing what happens inside the tools you use can help you use them with greater confidence and enjoyment.

This guide explores AI in **language that anyone can understand**. We trace how key ideas in machine learning and deep learning led to today’s LLMs, then go a step further and build agents that use them.

!!! info "What is an LLM?"
    LLM stands for **large language model**: an AI model trained on vast amounts of text to understand and generate human language. Conversational AI systems such as ChatGPT are familiar examples.

## Who is this guide for? {#target-audience}

This guide is for **anyone who uses AI in everyday life and wants to understand what happens inside it**. You do not need specialized computer knowledge, advanced mathematics, or coding experience. We use accessible explanations and analogies to explore the technologies and research papers that shaped LLMs and understand the ideas behind them.

This guide is especially for you if you want to:

- Use AI tools such as ChatGPT with greater independence and confidence.
- Understand unfamiliar terms you encounter in AI news and conversations.
- Learn how LLMs work and how they developed, without needing a technical background.

For those who want to go beyond understanding AI and build services with LLMs, we also cover practical implementation. If you have learned Python, you can learn to build an LLM-powered agent and make it available as a service.

The technical documentation needed to learn AI agent development is extensive, and the learning paths are often disconnected. FastAPI documentation covers FastAPI, while agent development resources cover agents, leaving you to work out how the pieces fit together. This guide connects the necessary concepts and technologies into one learning path, taking you step by step from building an agent to running it as a service.

!!! info "A first step toward using AI more effectively"
    **If you have not learned to code, the `Understanding LLMs` track is enough on its own.** Understanding what AI can do and where its limits lie helps you use it more appropriately in everyday life and make your own judgments about its output.

!!! warning "Before you begin"
    This is not a course on vibe coding, where AI agents produce results for you quickly. We learn how LLMs work, then use that understanding to build agents ourselves.

## What will you learn? {#learning-topics}

### :material-brain: Understanding LLMs

Follow the **key ideas in AI’s history and the problems that inspired them** to learn the core concepts behind LLMs. Along the way, we meet influential researchers and explore important papers, treating AI’s development as a connected history. Rather than focusing on detailed equations or code, we ask **what problem each discovery set out to solve and how it contributed to today’s LLMs**.

### :material-robot: AI agent development

We cover the core topics needed to develop AI agents in the following order.

1. **FastAPI basics**

    Learn to build the API servers that web services need using the FastAPI web framework.

2. **Asynchronous programming (asyncio)**

    Learn asynchronous programming techniques for handling multiple I/O tasks efficiently.

3. **AI model serving**

    Learn to expose AI models through APIs while accounting for their particular requirements.

4. **LangChain & LangGraph**

    Learn to build LLM applications and agent workflows.

5. **AI agent development**

    Bring everything together to develop and deploy an AI agent.

Each section ends with **short exercises, answers, and explanations**. Put what you have learned into practice and check your understanding before moving on.

Let’s take the first step toward finding our way through the world of AI—and eventually building and working confidently with AI agents of our own.
