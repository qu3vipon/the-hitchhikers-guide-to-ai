---
description: Learn how language models predict words using logits, softmax, and cross-entropy. Explore tokens and why text is not always processed one word at a time.
---

# Language follows probabilistic patterns

## Rules and patterns in natural language {#patterns-in-natural-language}

Languages that develop through everyday use, such as English and Korean, are called **natural languages**. They differ from deliberately specified programming languages.

Words do not follow one another randomly. In “I drink ___ every morning,” `coffee` fits naturally, while `cars` usually does not. Context changes which words are likely.

Grammar creates patterns too. “I drink coffee every morning” is natural, while “Drink morning I every coffee” is not. Word order and grammatical forms matter.

Early language-processing systems often encoded grammar and meaning through hand-written rules: identify a subject and verb, assign a word sense, and so on.

But expressions have exceptions, and meanings depend on context. In “The bat flew out of the cave,” `bat` is an animal. In “She swung the bat,” it is sports equipment. Defining every possibility by hand is difficult.

![The word bat refers to an animal or sports equipment depending on context](../assets/images/llm/en/07-context-meaning.svg){ .neural-network-image .language-modeling-image }

People do not wait to learn every grammatical rule before speaking. We hear and use many sentences, gradually learning which expressions sound natural and which words appear together. Grammar describes many of these regularities.

Language contains **probabilistic patterns**: a context may allow many continuations, but some occur much more often. Language models learn these patterns from text instead of relying entirely on hand-written grammar rules.

## Predicting from context {#context}

[Word2Vec](06-word-embeddings.md#learning-from-context) predicts words from context, but it does not immediately choose an answer such as `coffee`. A full-vocabulary formulation first scores every candidate in its **vocabulary**, the list of words it handles. A basic word-level model cannot directly predict words outside that list.

With 10,000 vocabulary items, a full-vocabulary output layer has 10,000 outputs, one per word. Practical Word2Vec training can use more efficient objectives, but the full-vocabulary view is useful here.

![A Word2Vec output layer assigns scores to vocabulary candidates](../assets/images/llm/en/07-word2vec-output-layer.svg){ .neural-network-image .language-modeling-image }

Consider predicting the missing word in “drink ___ daily.” Each output is a **logit**, a score indicating how well a candidate fits this context.

Logits are unrestricted scores, not probabilities. To obtain a probability distribution, apply **softmax**. It transforms all the scores together into positive values that sum to `1`, assigning larger probabilities to higher-scoring candidates. If `coffee` receives probability `0.68`, it is the most likely candidate in this example.

!!! info "How softmax creates probabilities"
    <div class="hinton-profile">
      <div class="hinton-profile__photo">
        <img class="language-modeling-image" src="../assets/images/llm/en/07-softmax-transformation.svg" alt="Exponentiation helps convert logits into probabilities">
      </div>
      <div class="hinton-profile__content">
        <p>Softmax exponentiates each logit <code>z<sub>i</sub></code> to obtain <code>e<sup>z<sub>i</sub></sup></code>, then divides by the sum of all exponentiated logits: <code>p<sub>i</sub> = e<sup>z<sub>i</sub></sup> / Σe<sup>z<sub>j</sub></sup></code>. Exponentials are positive, and normalization makes the probabilities sum to <code>1</code>. Larger logits receive larger probabilities.</p>
      </div>
    </div>

How does the model learn? It uses words that actually occur in sentences as targets. A collection of text used for analysis or training is called a **corpus**.

Because the training sentence already exists, we know which word appeared between `drink` and `daily`. We compare the predicted distribution with that target using a [loss function](03-perceptron.md#learning-goal).

A common choice is **cross-entropy**. For a single correct target, it penalizes the model for assigning that target a low probability. Higher target probability means lower loss.

Adjusting the embeddings and other trainable weights to reduce this loss improves prediction and captures patterns in the corpus.

## Splitting words into pieces {#tokens}

Real language models process **tokens**, not necessarily whole words. A token may be a word, a word fragment, punctuation, or another text unit. For example, a tokenizer might represent `playing` as `[play] [ing]`. These examples are conceptual; the actual split depends on the tokenizer.

A whole-word vocabulary can become huge because words have many forms and new words keep appearing. Instead of giving `playing`, `played`, and `playful` unrelated entries, a subword scheme can reuse `play` and represent the remaining pieces separately.

![Related words reuse the token piece play](../assets/images/llm/en/07-shared-token-pieces.svg){ .neural-network-image .language-modeling-image }

Tokenization helps **limit vocabulary size while representing many expressions**. This matters because vocabulary size also affects a full-vocabulary output layer’s size and computation.

Spaces do not uniquely determine token boundaries. Languages differ in their writing systems and grammatical structure, and even the same English sentence can be split differently by different tokenizers.

For illustration, one scheme could split “I drank coffee” into `[I] [dr] [ank] [cof] [fee]`, while another uses `[I] [drank] [coffee]`. Neither example is a claim about a particular model’s tokenizer.

![Two illustrative tokenizers split the same three-word sentence into five or three tokens](../assets/images/llm/en/07-korean-english-tokens.svg){ .neural-network-image .language-modeling-image }

In modern language models, embeddings, vocabularies, logits, and probability distributions refer to tokens rather than necessarily words. The overall flow is:

![Text passes through tokenization, embedding, model computation, and next-token prediction](../assets/images/llm/en/07-language-modeling-flow.svg){ .neural-network-image .language-modeling-image }

## Word2Vec’s legacy {#word2vec-significance}

Modern LLMs do not normally use Word2Vec as a component. Its importance is showing how useful word relationships can be learned as vectors.

Later methods went beyond one fixed vector per word. **Contextual representations** let the same token acquire different vectors depending on its surroundings. This is central to the transformer-based language models we will explore next.

## :material-pencil: Exercises {#exercises}

Decide whether each statement is **True** or **False**.

1. The next expression in natural language is completely random.
2. A full-vocabulary Word2Vec output layer calculates one logit per candidate.
3. Softmax probabilities sum to `1`.
4. A word always corresponds to exactly one token.
5. Cross-entropy measures how the predicted distribution differs from the target.

??? success "Answers and explanations"
    1. **False** — Context makes some expressions more likely than others.
    2. **True** — In the full-vocabulary formulation, each candidate receives a score.
    3. **True** — Softmax normalizes the scores into a distribution.
    4. **False** — Words can be split into fragments, and tokens can also represent punctuation or whitespace.
    5. **True** — Giving the correct target a low probability produces a higher loss.
