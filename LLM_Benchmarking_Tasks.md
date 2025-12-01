# LLM Benchmarking Tasks for Terminal-Based Evaluation

## Introduction

This document outlines a comprehensive set of tasks designed for terminal-based benchmarking of Large Language Models (LLMs). These tasks aim to evaluate various capabilities of LLMs, ranging from fundamental language understanding and generation to complex reasoning, code comprehension, and long-context processing.

Each task is presented with clear instructions for the LLM, specific test cases, and detailed evaluation criteria or potential solution strategies for human evaluators. The focus is on providing a structured approach to assess LLM performance in a rigorous, reproducible, and terminal-friendly manner.

The benchmarks are crafted with the discerning eye of top-tier technology leaders in mind, emphasizing practical applicability, depth of insight, and clear performance differentiation across diverse LLM architectures and capabilities.

## Table of Contents

1.  [Code Generation & Refinement](#1---code-generation--refinement)
    *   [1.1 - Python Function Generation](#11---python-function-generation)
    *   [1.2 - Bug Fixing in Python](#12---bug-fixing-in-python)
    *   [1.3 - Code Explanation](#13---code-explanation)
2.  [Text Generation & Manipulation](#2---text-generation--manipulation)
    *   [2.1 - Creative Writing: Short Story](#21---creative-writing-short-story)
    *   [2.2 - Summarization of a Technical Article](#22---summarization-of-a-technical-article)
    *   [2.3 - Paraphrasing for Tone Adjustment](#23---paraphrasing-for-tone-adjustment)
3.  [Reasoning & Logic](#3---reasoning--logic)
    *   [3.1 - Mathematical Problem Solving](#31---mathematical-problem-solving)
    *   [3.2 - Logical Deduction Puzzle](#32---logical-deduction-puzzle)
    *   [3.3 - Common Sense Reasoning](#33---common-sense-reasoning)
4.  [Information Retrieval & Question Answering](#4---information-retrieval--question-answering)
    *   [4.1 - Fact Retrieval (General Knowledge)](#41---fact-retrieval-general-knowledge)
    *   [4.2 - Contextual Q&A from Provided Text](#42---contextual-qa-from-provided-text)
5.  [Language Understanding & NLU](#5---language-understanding--nlu)
    *   [5.1 - Sentiment Analysis](#51---sentiment-analysis)
    *   [5.2 - Named Entity Recognition](#52---named-entity-recognition)
    *   [5.3 - Language Translation (English to French)](#53---language-translation-english-to-french)
6.  [Long-Context Understanding](#6---long-context-understanding)
    *   [6.1 - Summarization of a Long Document](#61---summarization-of-a-long-document)
    *   [6.2 - Answering Complex Questions from Long Context](#62---answering-complex-questions-from-long-context)

---

## 1 - Code Generation & Refinement

### 1.1 - Python Function Generation

**Objective:** Assess the LLM's ability to generate functional and idiomatic Python code based on a natural language description.

**Instructions:**
Generate a Python function that takes a list of integers and returns a new list containing only the prime numbers from the input list.

**Test Cases:**

#### Test Case 1: Standard List
**Input:**
```
Generate a Python function `get_primes(numbers)` that takes a list of integers `numbers` and returns a new list containing only the prime numbers.
```
**Expected Output / Evaluation Criteria:**
The function should correctly identify prime numbers. It should handle edge cases like 0, 1, and negative numbers (prime numbers are typically defined as integers greater than 1). The code should be syntactically correct Python, readable, and reasonably efficient.

#### Test Case 2: List with Zeros, Ones, and Negatives
**Input:**
```
Generate a Python function `get_primes(numbers)` that takes a list of integers `numbers` and returns a new list containing only the prime numbers. Ensure it correctly handles 0, 1, and negative numbers according to standard prime number definitions.
```
**Expected Output / Evaluation Criteria:**
The function `get_primes([0, 1, 2, 3, 4, 5, -7, 11, 13])` should return `[2, 3, 5, 11, 13]`. The implementation of the primality test should be correct.

**Potential Solution Strategy (for human evaluators):**
A common approach is to implement a helper function `is_prime(n)` that checks for primality by iterating from 2 up to the square root of `n`. The main `get_primes` function then filters the input list using this helper.

### 1.2 - Bug Fixing in Python

**Objective:** Evaluate the LLM's capability to identify and correct bugs in provided Python code.

**Instructions:**
Identify the bug(s) in the following Python function and provide the corrected version. Explain your reasoning for the fix.

**Test Cases:**

#### Test Case 1: Simple Logic Error
**Input:**
```python
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers - 1) # Bug here
```
**Expected Output / Evaluation Criteria:**
The LLM should identify that `len(numbers - 1)` is incorrect and should be `len(numbers)`. The corrected code should return the correct average. The explanation should clearly state the type of error (e.g., TypeError or incorrect indexing logic).

#### Test Case 2: Off-by-one Error
**Input:**
```python
def find_max_index(arr):
    if not arr:
        return -1
    max_val = arr[0]
    max_idx = 0
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            max_idx = i - 1 # Bug here
    return max_idx
```
**Expected Output / Evaluation Criteria:**
The LLM should identify the off-by-one error (`i - 1`) and correct it to `i`. The corrected function should return the correct index of the maximum value. The explanation should describe the off-by-one nature of the bug.

**Potential Solution Strategy (for human evaluators):**
Careful tracing of the loop and variable assignments can reveal these types of bugs. Understanding common error patterns like TypeErrors and off-by-one errors is key.

### 1.3 - Code Explanation

**Objective:** Assess the LLM's ability to understand and clearly explain existing code.

**Instructions:**
Explain the purpose and functionality of the following Python code snippet. Break down the explanation into what the code does, why it's written this way, and its potential applications.

**Test Cases:**

#### Test Case 1: Recursive Function
**Input:**
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```
**Expected Output / Evaluation Criteria:**
The explanation should correctly describe recursion, the base case, and the recursive step. It should mention that it calculates the factorial of a non-negative integer. Potential applications (e.g., permutations, combinations) would be a plus. The explanation should be clear, concise, and easy to understand for someone with basic programming knowledge.

#### Test Case 2: Class with Special Methods
**Input:**
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"
```
**Expected Output / Evaluation Criteria:**
The LLM should explain object-oriented programming concepts (class, instance, attributes). It must correctly identify the `__init__` (constructor), `__add__` (operator overloading for addition), and `__str__` (string representation) special methods, explaining their purpose and how they enable intuitive usage of `Vector` objects.

**Potential Solution Strategy (for human evaluators):**
Identify key programming constructs (recursion, classes, special methods). Explain each part in simple terms and then synthesize how they work together to achieve the overall functionality.

## 2 - Text Generation & Manipulation

### 2.1 - Creative Writing: Short Story

**Objective:** Evaluate the LLM's creative writing capabilities, including narrative coherence, descriptive language, and adherence to a prompt.

**Instructions:**
Write a very short story (around 150-200 words) about a lonely astronaut discovering a vibrant, hidden ecosystem on a supposedly barren moon.

**Test Cases:**

#### Test Case 1: Standard Prompt
**Input:**
```
Write a very short story (150-200 words) about a lonely astronaut discovering a vibrant, hidden ecosystem on a supposedly barren moon.
```
**Expected Output / Evaluation Criteria:**
The story should have a clear beginning, middle, and end. It should evoke a sense of wonder and loneliness. The language should be descriptive. Word count should be roughly within the specified range. Check for grammatical correctness and spelling.

**Potential Solution Strategy (for human evaluators):**
Look for engaging narrative, emotional depth (loneliness, surprise, wonder), vivid descriptions of the ecosystem, and a concise resolution.

### 2.2 - Summarization of a Technical Article

**Objective:** Assess the LLM's ability to extract key information from a technical text and present it concisely without losing essential meaning.

**Instructions:**
Summarize the following technical abstract in 2-3 sentences, highlighting the main problem, method, and key finding.

**Test Cases:**

#### Test Case 1: AI/ML Abstract
**Input:**
```
"Recent advancements in deep learning have significantly improved image recognition capabilities. However, deploying these complex models on resource-constrained edge devices remains a challenge due to high computational and memory requirements. This paper proposes a novel quantization-aware training scheme that adaptively prunes redundant connections in convolutional neural networks while maintaining accuracy. Our experiments demonstrate a 75% reduction in model size and a 60% increase in inference speed on embedded platforms with only a 1% drop in classification accuracy on the ImageNet dataset, paving the way for efficient on-device AI."
```
**Expected Output / Evaluation Criteria:**
The summary should capture:
1.  Problem: Deploying deep learning models on edge devices due to resource constraints.
2.  Method: Novel quantization-aware training with adaptive pruning.
3.  Finding: Significant model size reduction (75%) and inference speed increase (60%) with minimal accuracy loss (1%).
The summary should be 2-3 sentences and grammatically correct.

**Potential Solution Strategy (for human evaluators):**
Identify the core components of an abstract: introduction of problem, proposed solution/methodology, and results/implications. Condense these into succinct phrases.

### 2.3 - Paraphrasing for Tone Adjustment

**Objective:** Evaluate the LLM's understanding of tone and its ability to rephrase text to match a specified emotional or professional register.

**Instructions:**
Paraphrase the following informal sentence into a highly formal and professional tone.

**Test Cases:**

#### Test Case 1: Informal to Formal
**Input:**
```
"Hey team, gotta bounce early today, got some urgent stuff to handle. Catch ya later!"
```
**Expected Output / Evaluation Criteria:**
The paraphrased sentence should convey the same core message (leaving early due to urgency) but in a formal business context. It should avoid slang and informal contractions.
Example: "Dear team, I must depart earlier than planned today due to an unforeseen urgent matter. I will reconnect with you at a later time."

#### Test Case 2: Casual to Professional
**Input:**
```
"I messed up the data entry, so the numbers are all whack. Gotta fix it ASAP."
```
**Expected Output / Evaluation Criteria:**
The output should acknowledge the error professionally, state the need for correction, and maintain a professional demeanor.
Example: "An error occurred during data entry, which has impacted the accuracy of the figures. I will prioritize its immediate rectification."

**Potential Solution Strategy (for human evaluators):**
Replace informal vocabulary with formal synonyms, restructure sentences to be less colloquial, and adopt a respectful and objective stance.

## 3 - Reasoning & Logic

### 3.1 - Mathematical Problem Solving

**Objective:** Assess the LLM's ability to perform calculations and apply mathematical reasoning to solve word problems.

**Instructions:**
Solve the following word problem. Show your steps clearly.

**Test Cases:**

#### Test Case 1: Simple Algebra
**Input:**
```
A train travels at a constant speed. It covers 300 miles in 5 hours. How long will it take to cover 420 miles at the same speed?
```
**Expected Output / Evaluation Criteria:**
The LLM should first calculate the speed (300 miles / 5 hours = 60 mph). Then, it should use this speed to calculate the time for 420 miles (420 miles / 60 mph = 7 hours). Both steps and the final answer must be correct.

#### Test Case 2: Percentage Calculation
**Input:**
```
A product originally costs $150. It is first discounted by 20%, and then an additional 10% discount is applied to the discounted price. What is the final price of the product?
```
**Expected Output / Evaluation Criteria:**
Step 1: Calculate the price after the first discount ($150 * 0.80 = $120).
Step 2: Calculate the price after the second discount ($120 * 0.90 = $108).
The steps should be clear, and the final answer ($108) must be correct.

**Potential Solution Strategy (for human evaluators):**
Break down the problem into smaller, sequential mathematical operations. Identify relevant formulas (speed=distance/time, discount calculation). Execute calculations accurately.

### 3.2 - Logical Deduction Puzzle

**Objective:** Evaluate the LLM's ability to process a set of rules and deduce a correct conclusion.

**Instructions:**
Read the following statements and answer the question.

**Test Cases:**

#### Test Case 1: Simple Deductive Logic
**Input:**
```
Statements:
1. All birds can fly.
2. A penguin is a bird.
Question: Can a penguin fly?
```
**Expected Output / Evaluation Criteria:**
The LLM should identify that the first statement is a false premise in the real world, but *based solely on the provided statements*, the logical deduction is that "Yes, according to the given statements, a penguin can fly." This tests adherence to provided premises, even if they contradict general knowledge.

#### Test Case 2: Multi-step Deduction
**Input:**
```
Statements:
1. John is older than Mary.
2. Mary is older than Tom.
3. Tom is younger than Alice.
Question: Is John older than Alice? (Answer "Yes", "No", or "Cannot be determined")
```
**Expected Output / Evaluation Criteria:**
The LLM should correctly deduce that the relationship between John and Alice cannot be determined from the given statements. It can establish John > Mary > Tom, and Alice > Tom, but no direct or indirect comparison between John and Alice is provided. The answer "Cannot be determined" is correct.

**Potential Solution Strategy (for human evaluators):**
Represent the relationships symbolically (e.g., J > M, M > T). Attempt to chain the relationships. If a direct chain cannot be formed, the relationship is undetermined.

### 3.3 - Common Sense Reasoning

**Objective:** Assess the LLM's ability to apply real-world common sense knowledge to answer questions.

**Instructions:**
Answer the following common sense question.

**Test Cases:**

#### Test Case 1: Basic Action/Consequence
**Input:**
```
Why do people typically carry an umbrella when it's cloudy and dark outside?
```
**Expected Output / Evaluation Criteria:**
The LLM should connect "cloudy and dark" with the likelihood of rain. The answer should be something like "Because cloudy and dark skies often indicate that it might rain, and an umbrella protects from rain."

#### Test Case 2: Object Functionality
**Input:**
```
You find a small, smooth, flat, rectangular object in your pocket. It has a magnetic stripe on one side and a chip on the other. What is it most likely used for?
```
**Expected Output / Evaluation Criteria:**
The LLM should identify the object as a credit card, debit card, or similar payment/access card. The explanation should relate to its use for transactions or identification.

**Potential Solution Strategy (for human evaluators):**
Draw upon implicit knowledge about how the world works, the functions of common objects, and typical human behaviors.

## 4 - Information Retrieval & Question Answering

### 4.1 - Fact Retrieval (General Knowledge)

**Objective:** Evaluate the LLM's ability to access and retrieve factual information from its training data.

**Instructions:**
Answer the following factual question directly and concisely.

**Test Cases:**

#### Test Case 1: Science Fact
**Input:**
```
What is the chemical symbol for gold?
```
**Expected Output / Evaluation Criteria:**
The answer should be "Au".

#### Test Case 2: Geography Fact
**Input:**
```
Which city is known as the "Eternal City"?
```
**Expected Output / Evaluation Criteria:**
The answer should be "Rome".

**Potential Solution Strategy (for human evaluators):**
Direct recall of common general knowledge facts.

### 4.2 - Contextual Q&A from Provided Text

**Objective:** Assess the LLM's ability to read and understand a given text, and then accurately answer questions based *only* on that provided text.

**Instructions:**
Read the following paragraph carefully. Then, answer the question based solely on the information provided in the paragraph. Do not use outside knowledge.

**Test Cases:**

#### Test Case 1: Direct Answer
**Input:**
```
Paragraph: "The Amazon rainforest is the largest tropical rainforest in the world, covering an area of about 5.5 million square kilometers. It is home to an incredible diversity of wildlife, including jaguars, tapirs, and countless species of insects. The rainforest plays a crucial role in regulating the Earth's climate by absorbing vast amounts of carbon dioxide."
Question: What is the primary role of the Amazon rainforest in regulating the Earth's climate?
```
**Expected Output / Evaluation Criteria:**
The answer should directly state: "The Amazon rainforest plays a crucial role in regulating the Earth's climate by absorbing vast amounts of carbon dioxide."

#### Test Case 2: Inferential Answer within Context
**Input:**
```
Paragraph: "The Mars Rover Perseverance landed in Jezero Crater on February 18, 2021. Its mission objectives include searching for signs of ancient microbial life, collecting rock and soil samples, and testing technologies for future human exploration. The crater was chosen because scientists believe it once contained a lake."
Question: Why was Jezero Crater selected as the landing site for Perseverance?
```
**Expected Output / Evaluation Criteria:**
The answer should be: "Jezero Crater was chosen because scientists believe it once contained a lake."

**Potential Solution Strategy (for human evaluators):**
Scan the text for keywords from the question. Locate the relevant sentence(s) or phrase(s) and extract the answer directly or with minimal rephrasing, ensuring no outside information is introduced.

## 5 - Language Understanding & NLU

### 5.1 - Sentiment Analysis

**Objective:** Evaluate the LLM's ability to determine the emotional tone or sentiment of a given text.

**Instructions:**
Determine the sentiment (Positive, Negative, or Neutral) of the following sentence. Provide a brief justification.

**Test Cases:**

#### Test Case 1: Positive Sentiment
**Input:**
```
"The new software update dramatically improved performance and user experience."
```
**Expected Output / Evaluation Criteria:**
Sentiment: Positive.
Justification: The sentence uses positive descriptors like "dramatically improved performance" and "user experience."

#### Test Case 2: Negative Sentiment
**Input:**
```
"Despite numerous attempts, the system consistently failed to process the request, leading to significant frustration."
```
**Expected Output / Evaluation Criteria:**
Sentiment: Negative.
Justification: Phrases like "consistently failed," "significant frustration" indicate a negative sentiment.

#### Test Case 3: Neutral Sentiment
**Input:**
```
"The report details the quarterly sales figures for the electronics division."
```
**Expected Output / Evaluation Criteria:**
Sentiment: Neutral.
Justification: The sentence presents factual information without expressing any strong positive or negative emotion.

**Potential Solution Strategy (for human evaluators):**
Identify sentiment-bearing words or phrases (adjectives, adverbs, verbs that imply emotion or judgment). Consider the overall context and subject matter.

### 5.2 - Named Entity Recognition

**Objective:** Assess the LLM's ability to identify and categorize named entities (e.g., persons, organizations, locations) within a text.

**Instructions:**
Identify all Named Entities (Person, Organization, Location, Date) in the following text. List them in a structured format.

**Test Cases:**

#### Test Case 1: Mixed Entities
**Input:**
```
"Dr. Anya Sharma, CEO of InnovateTech, announced a new research facility in Berlin, Germany, on October 26, 2023."
```
**Expected Output / Evaluation Criteria:**
*   **Person:** Dr. Anya Sharma
*   **Organization:** InnovateTech
*   **Location:** Berlin, Germany
*   **Date:** October 26, 2023

#### Test Case 2: Multiple Occurrences and Ambiguity
**Input:**
```
"Apple Inc. is headquartered in Cupertino, California. Tim Cook is the CEO. They released the iPhone 15 last September."
```
**Expected Output / Evaluation Criteria:**
*   **Organization:** Apple Inc.
*   **Location:** Cupertino, California
*   **Person:** Tim Cook
*   **Date:** last September (or September, if LLM interprets 'last' as contextual)

**Potential Solution Strategy (for human evaluators):**
Read through the text and highlight each proper noun or specific temporal/locational phrase. Categorize each highlighted item based on standard NER labels.

### 5.3 - Language Translation (English to French)

**Objective:** Evaluate the LLM's proficiency in translating text between specified languages.

**Instructions:**
Translate the following English sentence into French.

**Test Cases:**

#### Test Case 1: Simple Sentence
**Input:**
```
"The quick brown fox jumps over the lazy dog."
```
**Expected Output / Evaluation Criteria:**
The translation should be grammatically correct and convey the exact meaning.
Example: "Le rapide renard brun saute par-dessus le chien paresseux."

#### Test Case 2: Complex Sentence with Idiom
**Input:**
```
"It's raining cats and dogs, so we should stay indoors."
```
**Expected Output / Evaluation Criteria:**
The translation should correctly handle the idiom, or provide an equivalent French idiom if applicable, while maintaining the overall meaning.
Example: "Il pleut des cordes, donc nous devrions rester à l'intérieur." (Literally "It's raining ropes," a common French idiom for heavy rain).

**Potential Solution Strategy (for human evaluators):**
Assess grammatical accuracy, idiomatic expression handling, and fidelity to the original meaning.

## 6 - Long-Context Understanding

### 6.1 - Summarization of a Long Document

**Objective:** Evaluate the LLM's ability to process and synthesize information from a significantly longer piece of text (beyond a few paragraphs) into a concise summary.

**Instructions:**
Summarize the following lengthy text (provided as placeholder) in 3-5 key bullet points. Focus on the main arguments and conclusions.

**Test Cases:**

#### Test Case 1: Fictional Policy Document Excerpt
**Input:**
(Imagine a 1000-word excerpt about a new city planning policy, detailing zoning changes, public transport initiatives, and environmental regulations.)
```
[Placeholder for a long text, e.g., a detailed report on climate change impacts, a policy proposal, or a lengthy article. For terminal testing, this would be a large block of text pasted as input.]
```
**Expected Output / Evaluation Criteria:**
The summary should condense the core information into 3-5 bullet points. Each point should represent a significant aspect of the original text. Accuracy, conciseness, and comprehensiveness of the summary are key. The LLM should not hallucinate information not present in the original text.

**Potential Solution Strategy (for human evaluators):**
Read the document for main ideas. Identify topic sentences, conclusions, and repeated themes. Filter out verbose details and combine related concepts into succinct bullet points.

### 6.2 - Answering Complex Questions from Long Context

**Objective:** Assess the LLM's capability to navigate a long document, identify scattered information, synthesize it, and answer multi-faceted questions based *only* on that context.

**Instructions:**
Read the following lengthy text (provided as placeholder). Then, answer the complex question below, citing sections or sentences if possible. Base your answer *strictly* on the provided text.

**Test Cases:**

#### Test Case 1: Synthesizing Information
**Input:**
(Imagine a 1500-word report discussing the challenges of renewable energy adoption, including economic barriers, grid integration issues, and public perception hurdles. It might also detail proposed solutions for each.)
```
[Placeholder for a long text, e.g., a research paper, an annual report, or a comprehensive market analysis. For terminal testing, this would be a large block of text pasted as input.]

Question: According to the document, what are the primary economic and technical challenges hindering the widespread adoption of solar energy, and what solutions are suggested for each?
```
**Expected Output / Evaluation Criteria:**
The answer should identify both economic and technical challenges mentioned in the text. For each challenge, it should also list corresponding solutions provided *within the text*. The answer should be structured (e.g., bullet points or distinct paragraphs for each challenge/solution) and accurate. Hallucinations or reliance on outside knowledge are unacceptable.

**Potential Solution Strategy (for human evaluators):**
Scan the document for keywords related to "economic challenges," "technical challenges," "solar energy adoption," and "solutions." Systematically extract and organize the relevant information, ensuring all parts of the question are addressed using only the provided text.

