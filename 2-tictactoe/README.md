#  Tic-Tac-Toe AI

> An unbeatable Tic-Tac-Toe AI using the Minimax algorithm.


---

##  Overview

This project implements an AI agent that plays Tic-Tac-Toe **optimally** — it will never lose. It uses the **Minimax** algorithm to explore the full game tree and always choose the best possible move. The AI plays against a human through a graphical interface built with Pygame.

---

##  AI Concepts Demonstrated

- **Minimax Algorithm:** Recursive adversarial search for zero-sum games
- **Game Tree:** Modeling all possible future states of a game
- **Terminal States:** Win, loss, or draw detection
- **Utility Function:** Assigning scores (+1, -1, 0) to terminal game states

---

##  How It Works

1. The AI represents the game as a tree of possible states
2. Maximizing player (X) picks the move with the highest utility
3. Minimizing player (O) picks the move with the lowest utility
4. With alpha-beta pruning, irrelevant branches are skipped for efficiency
5. The AI always plays the optimal move — best possible outcome is guaranteed

---

##  How to Run

```bash
cd 2-tictactoe
pip install requirements.txt
python runner.py
```

A window will open. Choose to play as X or O, and try to beat the AI — you can't!

---

##  Files

| File | Description |
|------|-------------|
| `tictactoe.py` | Game logic and Minimax implementation |
| `runner.py` | Pygame GUI runner |


