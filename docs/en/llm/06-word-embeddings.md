---
description: Compare integer encoding, one-hot encoding, and learned word embeddings. Explore how Word2Vec learns useful representations from context.
---

# Representing language as vectors

We have seen how neural networks adjust weights and biases to reduce loss. But a language model takes language as input and produces language as output, while our networks calculate with numbers. We first need a numerical representation of words and sentences.

## Turning words into numbers {#words-as-numbers}

The simplest approach assigns each word a unique number: `cat → 1`, `dog → 2`, `car → 3`. This is **integer encoding**. Encoding means representing information in another form according to a rule.

These numbers are identifiers, not quantities. `2 > 1` does not mean a dog is “larger” than a cat in some linguistic ordering. Feeding raw IDs directly into numerical calculations can introduce relationships that the identifiers were never meant to express.

![Integer encoding assigns identifiers to cat, dog, and car](../assets/images/llm/en/06-integer-encoding.svg){ .neural-network-image .word-embedding-image }

**One-hot encoding** avoids that artificial ordering. Give every vocabulary item a position, place `1` at the selected word’s position, and use `0` everywhere else.

![A one-hot vector highlights only the selected word’s position](../assets/images/llm/en/06-one-hot-encoding.svg){ .neural-network-image .word-embedding-image }

The words are now distinct, but their vectors do not represent meaning. Nothing says that cats and dogs are both animals, or that `cat` is closer in meaning to `dog` than to `car`.

The **dimension also grows with vocabulary size**. A vocabulary of 100,000 words requires 100,000 positions per one-hot vector. Only one is nonzero; storing and calculating with these vectors densely would be wasteful, although sparse representations can avoid storing all those zeros.

## Vectors that capture meaning {#meaningful-vectors}

A **word embedding** assigns a word to a point in a numerical vector space. Its dimension is a design choice, independent of vocabulary size: 100,000 words might each have a 300-component vector.

These **dense, lower-dimensional representations** can also capture relationships between words. Our five-word vocabulary can, for example, use three-dimensional embeddings instead of five-dimensional one-hot vectors.

![Example embeddings represent each word with three numbers](../assets/images/llm/en/06-embedding-values.svg){ .neural-network-image .word-embedding-image }

If learning has captured useful relationships, `cat` and `dog` may point in similar directions, while `car` points elsewhere. We can compare these representations numerically using a [dot product](05-high-dimensional-learning.md#learning-and-vectors), or use cosine similarity to compare directions without the effect of vector length.

![Cat and dog vectors have similar directions, while car points elsewhere](../assets/images/llm/en/06-word-embedding-vectors.svg){ .neural-network-image .coordinate-image }

An individual component does not necessarily mean “animal,” “large,” or “moves.” Meaning is distributed across components. The relationships between whole vectors matter more than interpreting each coordinate separately.

## Learning words from context {#learning-from-context}

Neural networks can learn embeddings from patterns of words appearing together. But how can we teach `cat` to be closer to `dog` than `car` without manually describing every word?

**Context** provides clues. Across many sentences, cats and dogs appear with similar surrounding words—sleeping, playing, eating—while cars appear in different settings, such as roads and engines.

**Word2Vec** uses this idea to learn relationships between words and their contexts. Two common training approaches are CBOW and Skip-gram.

### CBOW {#cbow}

**CBOW (Continuous Bag of Words)** uses surrounding words to predict a center word. “Bag of words” means the context words are pooled without preserving their order; “continuous” refers to their numerical vector representations.

For the phrase “drink coffee daily,” the surrounding words `drink` and `daily` can help predict `coffee`.

![CBOW predicts coffee from the surrounding words drink and daily](../assets/images/llm/en/06-word2vec-cbow.svg){ .neural-network-image .word-embedding-image }

### Skip-gram {#skip-gram}

**Skip-gram** reverses the task: use a center word to predict nearby context words individually. The context can include words a few positions away, rather than only immediate neighbors.

![Skip-gram uses coffee to predict drink and daily](../assets/images/llm/en/06-word2vec-skip-gram.svg){ .neural-network-image .word-embedding-image }

Skip-gram produces several prediction pairs for one center word. This can capture word-context relationships in detail and often helps with less frequent words, at greater computational cost. CBOW pools context to predict one center word, making training comparatively efficient, but pooling can lose distinctions between individual context words.

## Learning useful representations {#representation-learning}

As Word2Vec improves its predictions, it adjusts the word vectors. Words used in similar contexts can acquire related representations, even though nobody supplied a list of semantic attributes such as “animal,” “country,” or “profession.”

**Meaningful relationships emerge from the prediction task.**

![Related differences connect man to woman and king to queen](../assets/images/llm/en/06-word-embedding-analogy.svg){ .neural-network-image .coordinate-image }

Here, `E` denotes an embedding. A dashed arrow represents the difference between two vectors: the direction and distance needed to move from one to the other.

In some learned embedding spaces, `E(man) − E(woman) + E(queen)` is close to `E(king)`. A similar difference may connect `aunt` to `uncle`. These analogies illustrate patterns in training data, not universal facts or guaranteed arithmetic identities.

Letting a model discover useful representations instead of specifying every feature is called **representation learning**. It underlies many deep learning systems for images, speech, and language.

In image classification, earlier layers often respond to simple patterns such as edges or colors, while deeper layers respond to textures, shapes, or object parts. We did not explicitly tell each layer which feature to learn. Training it to classify images encourages useful intermediate representations.

![Deeper image-classification layers respond to progressively more complex features](https://oi.readthedocs.io/en/latest/_images/feature_train_time.png){ .neural-network-image }

<p class="cnn-visualization-credit"><em><a href="https://cs.nyu.edu/~fergus/papers/zeilerECCV2014.pdf">Zeiler & Fergus (2014), Visualizing and Understanding Convolutional Networks</a></em></p>

Representation learning did not begin with Word2Vec. Earlier neural network research, including work in the 1980s, explored how hidden layers learn useful features. Word2Vec is an influential example of applying the principle to words.

!!! info "Yoshua Bengio and representation learning"
    <div class="hinton-profile">
      <div class="hinton-profile__photo">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Yoshua_Bengio_2019_cropped.jpg" alt="Yoshua Bengio">
      </div>
      <div class="hinton-profile__content">
        <p>Yoshua Bengio helped develop methods for learning useful representations. His 2003 neural probabilistic language model was an important foundation for learned word embeddings. He shared the 2018 Turing Award with Geoffrey Hinton and Yann LeCun. The award is one of computer science’s highest honors.</p>
        <p class="hinton-profile__credit">Image: <em><a href="https://commons.wikimedia.org/wiki/File:Yoshua_Bengio_2019_cropped.jpg">Maryse Boyce</a> · CC BY 4.0</em></p>
      </div>
    </div>

## :material-pencil: Exercises {#exercises}

Decide whether each statement is **True** or **False**.

1. One-hot vectors grow in dimension as vocabulary size increases.
2. Word2Vec requires people to assign semantic features to every word.
3. CBOW predicts a center word from surrounding words.
4. Representation learning discovers useful features from data.
5. Differences between embedding vectors can reflect relationships between words.

??? success "Answers and explanations"
    1. **True** — Each vocabulary item receives its own position.
    2. **False** — Useful representations are learned from word-context prediction.
    3. **True** — Context is used to predict the missing center word.
    4. **True** — The model learns representations useful for its task.
    5. **True** — Learned differences can reflect relationships, although not perfectly or universally.
