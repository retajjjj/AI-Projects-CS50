#  Minesweeper AI

> An AI agent that plays Minesweeper safely by building a knowledge base and inferring mine locations.


---

##  Overview

This AI agent plays Minesweeper by maintaining a **knowledge base** of logical sentences about the board. As cells are revealed, the AI infers which cells are safe or contain mines — and makes moves accordingly. When no inference is possible, it falls back to a random safe choice.

---

##  AI Concepts Demonstrated

- **Knowledge Base:** Storing and updating facts about the game state
- **Logical Inference:** Deriving new knowledge from existing sentences
- **Sentence Subset Inference:** If `{A,B} = 1` and `{A,B,C} = 2`, then `{C} = 1`
- **Safe vs. Mine Classification:** Acting only on certainties

---

##  How It Works

1. When a cell is revealed, the AI creates a sentence: `{neighbors} = count`
2. The AI checks if any sentence implies all cells are mines or all are safe
3. It uses subset inference to derive new, simpler sentences
4. It marks mines with flags and safely clicks known-safe cells
5. If no safe move is known, it picks randomly from unexplored cells

---

##  How to Run

```bash
cd 4-minesweeper
python runner.py
```

Click **Left Click** to reveal a cell, or **AI MOVE** to watch the AI play or **"Reset"** to start a new game.

---

##  Files

| File | Description |
|------|-------------|
| `minesweeper.py` | Game logic and AI agent implementation |
| `runner.py` | Pygame GUI runner |


