#  Nim — Reinforcement Learning AI

> Train an AI to master the game of Nim through self-play using Q-Learning.

---

##  Overview

Nim is a mathematical strategy game where players take turns removing objects from piles. The player forced to take the last object loses. This AI learns the optimal strategy entirely through **self-play** — playing 10,000 games against itself and using **Q-Learning** to update its understanding of which moves lead to victory.

---

##  AI Concepts Demonstrated

- **Reinforcement Learning:** Learning through reward and punishment signals
- **Q-Learning:** Updating action-value estimates from experience
- **Exploration vs. Exploitation (ε-greedy):** Balancing trying new moves vs. using known good ones
- **Self-Play:** Generating training data without human labeling
- **State-Action Value (Q-value):** Estimating the long-term value of each (state, action) pair

---

##  How It Works

1. The AI plays 10,000 games against itself
2. Each (state, action) pair encountered is recorded
3. After each game, Q-values are updated:
   - **Win:** Q(state, action) += α * (1 - Q(state, action))
   - **Loss:** Q(state, action) += α * (-1 - Q(state, action))
4. During training, ε-greedy exploration ensures the AI tries suboptimal moves
5. After training, the AI exploits its learned Q-table to play optimally

---

##  How to Run

```bash
cd 9-nim
python play.py
```

The AI will train for 10,000 games, then invite you to play against it. Good luck — you'll need it.

---

##  Files

| File | Description |
|------|-------------|
| `nim.py` | Game logic and Q-Learning AI implementation |
| `play.py` | Training runner and human vs. AI interface |

