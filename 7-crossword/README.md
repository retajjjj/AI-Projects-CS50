#  Crossword Puzzle Generator

> Generate complete crossword puzzles automatically using Constraint Satisfaction Problem (CSP) techniques.

---

##  Overview

Given a crossword grid structure and a vocabulary list, this AI fills in the crossword so every word fits its slot and overlapping letters are consistent. It models the puzzle as a **Constraint Satisfaction Problem** and solves it using backtracking search with intelligent heuristics.

---

##  AI Concepts Demonstrated

- **Constraint Satisfaction Problem (CSP):** Variables, domains, and constraints
- **Arc Consistency (AC-3):** Preprocessing to shrink domains before search
- **Backtracking Search:** Systematically trying assignments and undoing failures
- **Degree Heuristic:** Break ties by choosing the variable with the most constraints
- **Least Constraining Value (LCV):** Pick the value that rules out the fewest options

---

##  How It Works

1. Load a grid structure (which cells are blank, which are blocked)
2. Identify all word slots (across and down) and their overlap positions
3. Assign each slot a domain (all valid words of correct length)
4. Apply AC-3 to enforce arc consistency — narrow domains before search
5. Use backtracking with MRV and LCV heuristics to find a valid assignment
6. Output the completed crossword

---

##  How to Run

```bash
cd 7-crossword
python generate.py data/structure1.txt data/words1.txt output.png
```

This generates a PNG image of the solved crossword.

---

##  Files

| File | Description |
|------|-------------|
| `generate.py` | CSP solver with backtracking and heuristics |
| `crossword.py` | Crossword and Variable class definitions |
| `data/` | Grid structures and word lists |

