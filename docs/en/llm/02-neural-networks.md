---
description: Explore the ideas connecting biological neurons to artificial neural networks. Illustrations and matrix examples explain weights, weighted sums, and multiple inputs and outputs.
---

# The invention of neural networks

## Neurons and weights {#neurons-and-weights}

In machine learning, a computer learns decision criteria from examples. But how does it process the data and learn those criteria? Researchers have proposed many mathematical and statistical models. One of the most influential is the **artificial neural network**, inspired by the **neurons** in our brains. The idea was to represent aspects of how connected neurons process information using computations and connections inside a computer.

![A neuron showing dendrites, the cell body, the axon, and axon terminals](../assets/images/llm/en/02-neuron-anatomy.svg){ .drawing-diagram style="width: min(100%, 30rem);" }

!!! info "The parts of a neuron"
    A simplified neuron has **dendrites**, a **cell body (soma)**, an **axon**, and **axon terminals**.

    - **Dendrites** receive signals from other neurons.
    - **The cell body** integrates incoming signals and maintains the cell’s functions.
    - **The axon** carries electrical signals toward the terminals.
    - **Axon terminals** release neurotransmitters to pass signals to other neurons.

    In this simplified picture, a neuron receives signals, combines them, carries a signal along its axon, and passes it onward.

    We can summarize the flow as **input → integration → transmission → output**. This information-processing pattern helped inspire artificial neural networks.

Countless neurons exchange signals to support sensation, movement, and other functions. Imagine touching a hot pan. Sensory receptors in your skin detect the heat, and signals travel through neurons. Signals reaching the muscles in your hand and arm cause them to contract, pulling your hand away.

![A simplified signal pathway from a sensory neuron through intermediate neurons to a motor neuron](../assets/images/llm/en/02-neuron-signal-flow.svg){ .neuron-signal-flow-image }

What matters is **how the neurons are connected**. Some circuits are involved in moving your hand; others process sounds or visual information. Repeated experience can strengthen connections between neurons that are frequently active together.

Artificial neural networks borrow this idea. A number called a **weight** describes the influence of a connection. You can think of it as indicating **how strongly one neuron’s signal contributes to the next neuron’s calculation**.

![Two layers of artificial neurons connected by weights](../assets/images/llm/en/02-neural-network-3x3.svg){ .neural-network-image }

In this diagram, darker lines represent larger positive weights and therefore stronger contributions. A neuron can connect to several others with different weights and receive input from several neurons at once.

## Weighted sums {#weighted-sum}

![Three input neurons connected to one output neuron](../assets/images/llm/en/02-neural-network-3x1.svg){ .neural-network-image }

Here is how weights enter the calculation. The value inside each input neuron represents its **signal strength**. The receiving neuron multiplies each signal by its connection weight, then adds the results:

`(0.2 × 0.8) + (0.4 × 0.4) + (0.5 × 0.2) = 0.42`

This calculation is called a **weighted sum**.

Imagine comparing applicants using their English, science, and math scores. If math matters more for this particular program, we could multiply the English and science scores by `1` and the math score by `2`. Math would then contribute twice as much per point to the final score.

![Applicants A and B have equal raw totals, but doubling the math score gives weighted totals of 320 and 340](../assets/images/llm/en/02-applicant-weighted-sum.svg){ .drawing-diagram style="width: 100%;" }

Both applicants have a raw total of `250`. After giving math a larger weight, applicant B, who has the higher math score, receives the higher weighted total. A weighted sum **lets different inputs contribute different amounts to the result**.

## Neural networks as functions {#neural-networks-as-functions}

We can also describe these connections using [functions](01-machine-learning.md#functions-turn-inputs-into-outputs). In chapter 1, we saw that a function connects inputs to outputs according to a rule. Let the incoming neuron values be inputs `x` and the receiving neuron’s result be output `y`. A function `f` can describe the calculation connecting them.

For three inputs producing one output, we write `y = f(x₁, x₂, x₃)`. This means that `f` takes `x₁`, `x₂`, and `x₃` and calculates `y`.

![Inputs x₁, x₂, and x₃ pass through weighted connections to produce y](../assets/images/llm/en/02-neural-network-3x1-variables.svg){ .neural-network-image }

Inside the function, each input is multiplied by a weight that determines its contribution. For the network above:

⇒ <code>f(x₁, x₂, x₃) = (<span class="weight-value">0.8</span>x₁) + (<span class="weight-value">0.4</span>x₂) + (<span class="weight-value">0.2</span>x₃)</code>

!!! tip "Reading the formula"
    - `f(x₁, x₂, x₃)` is a function that takes three inputs and produces one result.
    - `0.8x₁`, `0.4x₂`, and `0.2x₃` multiply each input by its connection weight.
    - `+` adds those weighted contributions together.

![Three inputs connect to outputs y₁, y₂, and y₃ calculated by functions f₁, f₂, and f₃](../assets/images/llm/en/02-neural-network-3x3-variables.svg){ .neural-network-image }

Now increase the number of output neurons to three. Each output neuron calculates its value using the inputs and the weights of its own incoming connections. We can therefore describe the network with three functions, one per output.

The functions `f₁`, `f₂`, and `f₃` are **different** even though they receive the same inputs. Each output neuron has its own set of weights.

For example, the functions might be:

![Three functions apply different weights to the same inputs](../assets/images/llm/en/02-three-function-formulas.svg){ .drawing-diagram }

## Expanding the network {#expanding-neural-networks}

The nervous system contains vast numbers of connected neurons. Our examples have been small, but artificial neural networks can also contain many more units and connections.

Let’s expand our example to <code><span class="weight-input-index">n</span></code> input neurons and <code><span class="weight-output-index">m</span></code> output neurons.

Neurons at the same stage of a network form a **layer**. The **input layer** receives the initial signals, and the **output layer** produces the results.

![A network with n inputs and m outputs](../assets/images/llm/en/02-neural-network-nxm.svg){ .neural-network-image }

We can still express these connections as functions. We use `x` for inputs and `w` for connection weights.

![Generalized weighted-sum formulas for n inputs and m outputs](../assets/images/llm/en/02-generalized-function-formulas.svg){ .drawing-diagram }

With <code><span class="weight-input-index">n</span></code> inputs, each output neuron calculates a result from <code><span class="weight-input-index">n</span></code> values. With <code><span class="weight-output-index">m</span></code> output neurons, we have <code><span class="weight-output-index">m</span></code> functions, one for each result.

![The same n inputs are passed to m functions](../assets/images/llm/en/02-function-overview.svg){ .drawing-diagram }

The network turns <span class="weight-input-index">n</span> inputs into <code><span class="weight-output-index">m</span></code> outputs.

The weight <code>w<sub><span class="weight-output-index">i</span><span class="weight-input-index">j</span></sub></code> determines how input <code>x<sub><span class="weight-input-index">j</span></sub></code> contributes to output <code>y<sub><span class="weight-output-index">i</span></sub></code>. The first index, <code><span class="weight-output-index">i</span></code>, identifies the output neuron. The second, <code><span class="weight-input-index">j</span></code>, identifies the input neuron.

For example, <code>w<sub><span class="weight-output-index">2</span><span class="weight-input-index">1</span></sub></code> is the weight connecting the first input <code>x<sub><span class="weight-input-index">1</span></sub></code> to the second output <code>y<sub><span class="weight-output-index">2</span></sub></code>.

![The weight w₂₁ connecting input x₁ to output y₂ is highlighted](../assets/images/llm/en/02-weight-w21.svg){ .neural-network-image }

Writing out all <code><span class="weight-output-index">m</span></code> functions, each with <code><span class="weight-input-index">n</span></code> inputs, would take a lot of space. We can shorten one function to:

![The weighted sum written as f(x) = w · x](../assets/images/llm/en/02-weighted-sum-formula.svg){ .drawing-diagram }

Here, `x` groups the inputs `x₁`, `x₂`, …, `xₙ`, and `w` groups their weights. The dot `·` means **multiply each input by its corresponding weight, then add the products**. The expression `f(x) = w · x` is a compact way to write the weighted sum for one output neuron. The notation is shorter, but the calculation is unchanged.

For <code><span class="weight-output-index">m</span></code> output neurons, each function has a different weight vector: `w₁`, `w₂`, …, `wₘ`. Stack them into a **matrix `W`**, and we can express all the outputs `y₁`, `y₂`, …, `yₘ` in a single equation:

![The output vector y equals the weight matrix W multiplied by the input vector x](../assets/images/llm/en/02-matrix-vector-product.svg){ .drawing-diagram }

Multiplying the input vector `x` by `W` produces the output vector `y`. Thus, `y = Wx` describes **how the weighted connections between two layers transform multiple inputs into multiple outputs**.

To calculate `y₂`, use the second row of `W`: multiply each weight in that row by its corresponding input, then add the products. Matrix notation packages the same weighted-sum calculation into a more convenient form.

!!! info "Matrices"
    A **matrix** arranges numbers in rows and columns. Each row of `W` contains the weights for one output function.

    The weights of `f₁`, `f₂`, and `f₃` form this matrix:

    <div class="matrix-example" aria-label="Weight matrix W containing the weights for three functions"><code>W = ⎡ 0.4   0.8   0.1 ⎤
        ⎢ 0.9   0.3   0.7 ⎥
        ⎣ 0.8   0.4   0.2 ⎦</code></div>

    The first row, `0.4`, `0.8`, and `0.1`, contains the weights for `f₁`. The second and third rows contain the weights for `f₂` and `f₃`.

    For now, we are focusing on weighted sums. Later chapters add other parts of a neuron’s calculation, such as biases and activation functions.

## :material-pencil: Exercises {#exercises}

Decide whether each statement is **True** or **False**.

1. A weight describes how a connection between two neurons contributes to the result.
2. A larger weight means the neuron itself is always more active.
3. The group of neurons that first receives external inputs is called the output layer.
4. `w₂₁` is the weight connecting the first input `x₁` to the second output `y₂`.
5. `y = Wx` can represent the weighted-sum calculation of a neural network layer with multiple inputs and outputs.

??? success "Answers and explanations"
    1. **True** — A weight belongs to a connection and determines its contribution, rather than being a property of one neuron alone.
    2. **False** — A weight describes the connection, not the neuron’s own activity level.
    3. **False** — The first group is the input layer.
    4. **True** — The first index identifies output 2, and the second identifies input 1.
    5. **True** — `W` collects the connection weights, and the matrix multiplication calculates the weighted sums together.
