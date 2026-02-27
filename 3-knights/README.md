#  Knights and Knaves

> Solve classic logic puzzles using propositional logic and an automated model-checking AI.


---

##  Overview

In the Knights and Knaves puzzles, every character is either a **Knight** (always tells the truth) or a **Knave** (always lies). Given a set of statements made by characters, the AI determines who is a Knight and who is a Knave using **propositional logic** and **model checking**.

---

##  AI Concepts Demonstrated

- **Propositional Logic:** Encoding puzzle rules as logical sentences
- **Model Checking:** Enumerating all possible worlds to find what must be true
- **Logical Connectives:** AND, OR, NOT, Implication, Biconditional
- **Knowledge Base:** Accumulating facts and rules the AI uses to reason
- **Entailment:** Determining if a knowledge base logically implies a query

---

##  How It Works

1. Each puzzle is encoded as a set of logical sentences in a knowledge base
2. Rules like "if a character says X, and they are a Knight, then X is true" are added
3. The model checker tests every possible assignment of Knight/Knave
4. It returns the assignment consistent with all logical constraints

---

##  How to Run

```bash
cd 3-knights
python puzzle.py
```

**Sample Output:**
```
Puzzle 0
    A is a Knave
Puzzle 1
    A is a Knave
    B is a Knight
Puzzle 2
    A is a Knave
    B is a Knight
Puzzle 3
    A is a Knight
    B is a Knave
    C is a Knight
```

---

##  Files

| File | Description |
|------|-------------|
| `logic.py` | Propositional logic classes (And, Or, Not, Implication, etc.) |
| `puzzle.py` | Puzzle definitions and model-checking runner |


