---
description: Discover how machine learning differs from hand-written rules. Functions, simple examples, and a cat classifier introduce the basic ideas behind learning from data.
---

# How computers learn

## Computers follow rules {#rule-based-computing}

To understand LLMs, we first need to understand how computers carry out instructions. Let’s start with a familiar example.

Computers are diligent tools: they **execute the instructions they are given quickly and precisely**. Open a calculator app, enter `2 + 3 =`, and it displays `5`. What happens inside?

In a simplified picture, the program reads your input one step at a time. When you enter `2`, it stores the value because it does not yet know which operation to perform. When you enter `+`, it records that it should add the next number. You enter `3`, then press `=`, and the program adds the two stored numbers and displays `5`.

Subtraction, multiplication, and division work through other predefined rules. Building a calculator therefore means specifying what the computer should do in each situation and in what order.

![The calculator stores 2, recognizes addition, reads 3, and displays 5](../assets/images/llm/en/01-calculator-process.svg){ .drawing-diagram }

Traditional programs are built by **having people define the rules and procedures for solving a problem, then express them as instructions a computer can execute**. The situations a program can handle depend on how thoroughly its rules cover both expected and unexpected cases. Anticipating those cases has always been an important part of programming.

!!! info "Where the word computer comes from"
    Before it referred to a machine, a **computer** was a person who performed calculations. The name comes from the verb **compute**.

    ENIAC, built in the 1940s, was one of the earliest general-purpose electronic computers. It was designed to speed up calculations for artillery firing tables. Computers developed in part to **perform calculations that would take people far too long**.

A calculator uses an established rule for addition. But not every problem comes with such a clear rule. Suppose we want a program that tells us whether to take an umbrella when going out. We could define this rule ourselves:

![A decision tree choosing whether to take an umbrella based on forecast rainfall](../assets/images/llm/en/01-umbrella-decision.svg){ .drawing-diagram }

The diagram checks the forecast rainfall per hour. If it is at least 1 mm, take an umbrella; otherwise, leave it behind.

The important point is that **a person chose the threshold in advance**. We might examine past rainfall and umbrella use, or draw on our own experience, to decide that 1 mm per hour is a useful threshold. We then put that decision into code. The computer follows it without judging whether it is a good rule.

As the number of relevant conditions grows, the rules become more complicated and harder to implement. When people must specify every condition themselves, there are limits to how many situations a rule-based program can handle well.

A branching set of decisions like the one above can be drawn as a **decision tree**. It helps us see which conditions lead to which outcomes.

## Inputs and outputs: functions {#functions-turn-inputs-into-outputs}

You may have encountered the idea of a “function machine” in math: put a number into a box, and a rule inside the box produces another number.

Imagine a box that always adds 42. Put in `3` and you get `45`; put in `10` and you get `52`. The value going in is the **input**, and the value coming out is the **output**. A **function** assigns an output to each valid input according to a rule.

![A function machine adds 42 to the input 3 to produce 45](../assets/images/llm/en/01-function-machine.svg){ .function-mapping-image }

A function lets us **apply the same rule to different inputs**. Whether we enter `3` or `10`, the rule remains “add 42.” We do not have to list every possible input-output pair to describe what the box does.

We write this relationship as `y = f(x)`: `x` is the input, `f` is the function, and `y` is the output. Our box is `f(x) = x + 42`, a compact way of saying that it adds 42 to any number you give it.

## Viewing programs as functions {#programs-as-functions}

A program receives inputs and produces outputs by following rules. Viewing that process as a function gives us a simple way to describe it—and prepares us to understand machine learning.

Consider the umbrella program. It takes forecast rainfall as input and outputs either “take an umbrella” or “leave it behind.” If we focus on this input-output relationship, we can treat the program as a function.

![An umbrella program checks an input condition and produces a decision](../assets/images/llm/en/01-umbrella-function.svg){ .drawing-diagram }

We can write it as `umbrella decision = f(forecast hourly rainfall)`. The function `f` represents the decision rule.

For an input `x` of at least 1 mm per hour, it outputs “take an umbrella.” For a smaller value, it outputs “leave it behind.” A program’s decision rules can be expressed as a function too.

![A piecewise function says to take an umbrella when x is at least 1 and leave it behind otherwise](../assets/images/llm/en/01-umbrella-piecewise-function.svg){ .drawing-diagram }

## Can we write every rule in advance? {#can-we-write-every-rule}

The umbrella threshold was chosen by a person. Rule-based programming works well when we can clearly define the decision criteria and the situations a program needs to handle.

But many problems resist that approach. Look at the image below: you recognize a cat almost immediately. Could you write down the rules a computer would need to recognize it too?

It is harder than it sounds. Should pointed ears be enough? How pointed? Before that, how would you tell the computer to find an ear in the image and recognize it as an ear?

![A surprised cat](https://commons.wikimedia.org/wiki/Special:FilePath/Surprised_Cat.jpg){ .cat-dog-image }

<p class="cat-dog-caption"><em><a href="https://commons.wikimedia.org/wiki/File:Surprised_Cat.jpg">Rudi Riet</a> (CC BY-SA 2.0)</em></p>

Instead of writing every rule ourselves, what if we could let a computer **discover useful decision criteria from examples**?

We could show it many cat images and have it learn recurring patterns and features. We would not need to specify exactly how to locate ears or how pointed they must be. The computer could learn features that help distinguish cats, then use them to classify a image it has never seen before.

Making this work is still difficult. But the approach is fundamentally different: **the computer learns patterns from data instead of relying on people to write every decision rule**.

This is **machine learning**: learning patterns from data and applying them to new examples.

## Artificial intelligence {#artificial-intelligence}

The idea of **artificial intelligence (AI)** predates modern machine learning. AI aims to make computers perform intellectual tasks such as reasoning, making decisions, and solving problems.

!!! info "An early milestone in AI"
    The term “artificial intelligence” appeared in the 1955 [proposal for the Dartmouth Summer Research Project](https://www-formal.stanford.edu/jmc/history/dartmouth/dartmouth.html), written by John McCarthy and his colleagues.

Think of JARVIS in the *Iron Man* films. It talks naturally with Tony Stark, analyzes information, and controls his suit and equipment. This fictional assistant sometimes exceeds human capabilities across a broad range of tasks.

AI research asks: **Can we build machines that think, learn, and solve problems as humans do?** Researchers have explored many approaches, and machine learning is one of them. If AI describes the broader ambition, machine learning is one way to pursue it.

Not all AI requires machine learning. Consider Akinator, a guessing game that asks questions and tries to identify the character you are thinking of, much like **Twenty Questions**. It does not solve the broad range of problems JARVIS does, but it illustrates the idea of narrowing down possibilities through questions and answers.

![The Akinator wordmark](../assets/images/llm/01-akinator-logo.svg){ style="display: block; width: min(100%, 16rem); margin: 1rem auto;" }

<p style="text-align: center; font-size: 0.7rem;">Source: <a href="https://commons.wikimedia.org/wiki/File:Akinator.svg">Wikimedia Commons</a></p>

You could build a Twenty Questions–style system using a question-and-answer tree designed entirely by people. That would demonstrate AI without requiring machine learning; it is not a claim about how Akinator itself is implemented. A system need not solve every kind of problem to count as AI. It can imitate aspects of human judgment within a particular task.

AI built for a limited range of tasks is called **narrow AI**. Machine learning is part of AI, but not every AI system uses machine learning.

![Machine learning is a subset of artificial intelligence](../assets/images/llm/en/01-ai-machine-learning-venn.svg){ .ai-ml-venn }

## What does it mean for a computer to learn? {#what-machine-learning-means}

When we say a computer “learns,” what do we mean? Its learning process is different from ours.

People build understanding and memories through experience. Computers do not experience the world in the same way. You have probably heard that computers work with zeros and ones. Text, images, and sound are represented numerically inside a computer.

The key idea is that **once information is represented as numbers, a computer can calculate with it and analyze it**.

![Part of a cat image is enlarged into pixels represented by a grid of numbers](../assets/images/llm/en/01-photo-to-numbers.svg){ .photo-to-numbers-image }

A image consists of many pixels. Represent each pixel’s color numerically, and the entire image becomes an array of numbers.

By analyzing numerical representations of animal images, a computer can learn patterns that help distinguish cats from other animals. That process is what we call learning in machine learning.

Think of it as **representing data numerically and repeating calculations to discover patterns in it**. Computers are good at performing complex calculations quickly and repeatedly. We can use that ability to learn decision criteria from data rather than specifying each one ourselves.

What happens when we give the trained program a new image? It uses what it learned to predict whether the image contains a cat. We can describe that input-output relationship as another function.

![A cat prediction is the output of a function that takes a image as input](../assets/images/llm/en/01-cat-classification-function.svg){ .drawing-diagram }

Real image classifiers are much more complex, but imagine a simplified model of the form `f(x) = ax + b`. Here, `x` stands in for a numerical representation of the image, and `a` and `b` are numbers that determine the output. The model performs a calculation with them, and its output is used to make a prediction.

If the chosen model is suitable for the task and we find appropriate values for its parameters, we can apply it to new examples. In supervised learning, we compare model outputs with known answers and adjust values such as `a` and `b`. A real cat classifier needs a much richer model than this simple illustrative formula.

## How does learning happen? {#how-computers-learn}

In our “add 42” box, the rule was fixed in advance: input `3`, output `45`. In the learning version, we do not tell the computer what number to add. We let it find that value from examples.

![The function machine must discover the missing value from an input of 3 and an output of 45](../assets/images/llm/en/01-function-machine-find-42.svg){ .function-mapping-image }

The computer needs clues. Here, the crucial clue is **showing it inputs together with their correct outputs**.

For example, we provide `3 → 45` and `10 → 52`. The computer compares its calculated outputs with these answers and adjusts the number it adds.

A simple learning procedure looks like this:

1. Start with a trial value for `?`, such as `0`.
2. Compare <code>3 + <span class="learning-value">0</span></code> and <code>10 + <span class="learning-value">0</span></code> with the correct answers, `45` and `52`.
3. Both results are too small, so increase `?`. If the results are too large, decrease it instead.
4. Repeat, reducing the differences between outputs and answers. With suitable adjustments, we can find `42`.

## Three ingredients of learning {#three-elements-of-learning}

The example brings together three ingredients: **data, a model, and a learning method**.

- **Data:** examples pairing an input with its correct answer.
- **Model:** the overall computation that turns an input into an output.
- **Learning method:** a procedure for comparing outputs with correct answers and deciding how to change the model’s internal values.

In the addition example:

- Data: the pairs `3 → 45` and `10 → 52`.
- Model: the function `f(x) = x + ?`.
- Learning method: repeatedly increase or decrease `?` according to whether the outputs are too small or too large.

Machine learning therefore **uses data and a learning procedure to repeatedly adjust a model’s internal values so that it produces useful results**. This example uses correct answers during training; other forms of machine learning use different kinds of feedback.

Values adjusted during training are called **parameters**. The term comes from mathematics: parameters determine a function’s form or behavior. In our illustrative `f(x) = ax + b`, the parameters are `a` and `b`.

!!! info "The data must fit the task"
    If you want to distinguish cats from dogs, collecting thousands of car images will not give you the examples you need. Relevance matters, not just quantity.

## The goal of machine learning {#goal-of-machine-learning}

Machine learning aims to learn patterns from data and make accurate predictions. We use the following terms and symbols to describe the process:

- **x — features:** the input information used to make a prediction.
- **y — target:** the answer we want the model to predict.
- **ŷ — prediction:** the output the model actually produces.

A **feature** is similar to an input in an ordinary program. The word emphasizes that it is an attribute of the data used for prediction.

For an umbrella model, forecast rainfall, humidity, and wind speed could each be a feature. We can also combine or transform existing features. For example, combining temperature and humidity gives a heat index that describes how hot the weather feels.

The **target** is the answer we want to predict. In the umbrella example, it is whether an umbrella is actually needed. With labeled training examples, the model learns a relationship between features and targets.

The **prediction** is what the model outputs after receiving the features. If the target says “take an umbrella” but the model predicts “leave it behind,” the prediction and target differ.

Training adjusts the model to reduce the difference between predictions (`ŷ`) and targets (`y`). But matching training examples is not enough: **the model also needs to make good predictions on data it has not seen before**.

## :material-pencil: Exercises {#exercises}

Decide whether each statement is **True** or **False**.

1. A function connects inputs and outputs according to a defined rule.
2. Every AI system must use machine learning.
3. Machine learning discovers recurring patterns in examples instead of requiring people to write every decision rule.
4. A learning method compares a model’s outputs with the answers and determines how to change its internal values.
5. In the `□ + ?` example, the learned value `42` is the model.

??? success "Answers and explanations"
    1. **True** — A function maps each valid input to an output according to a rule.
    2. **False** — AI can also use rules or decision trees designed by people.
    3. **True** — Machine learning uses patterns in data to develop decision criteria.
    4. **True** — That describes the learning method in our supervised example.
    5. **False** — The model is the full computation, `□ + ?`. The learned value `42` is a parameter within it.
