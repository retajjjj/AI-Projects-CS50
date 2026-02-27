#  Sentence Parser

> Parse English sentences and extract noun phrase chunks using Context-Free Grammar (CFG).
---

##  Overview

This project implements a natural language parser that determines the syntactic structure of English sentences. Using a handcrafted **Context-Free Grammar**, the AI generates parse trees and identifies all **noun phrase chunks** — a critical component of information extraction in NLP.

---

##  AI Concepts Demonstrated

- **Context-Free Grammar (CFG):** Production rules that define valid sentence structures
- **Parsing:** Building a syntactic tree from a sequence of words
- **Noun Phrase Chunking:** Extracting meaningful subject/object phrases from text
- **Terminals & Non-terminals:** Words vs. grammatical categories (NP, VP, S, etc.)

---

##  How It Works

1. Define a CFG with rules covering sentences, noun phrases, verb phrases, adjectives, prepositions, etc.
2. Tokenize and lowercase the input sentence
3. Use NLTK's `ChartParser` to generate all valid parse trees
4. Print each tree structure
5. Extract and display all noun phrase chunks (NPs with no other NPs inside)

---

##  How to Run

```bash
cd 10-parser
pip install requirements.txt
python parser.py sentences/10.txt
```

Or run interactively:
```bash
python parser.py
```

**Sample Output:**
```
Sentence: Holmes sat.
        S
   _____|___
  NP        VP
  |         |
  N         V
  |         |
holmes     sat

Noun Phrase Chunks
holmes
```

---

##  Files

| File | Description |
|------|-------------|
| `parser.py` | CFG definition and parsing logic |
| `sentences/` | 10 sample English sentences |


