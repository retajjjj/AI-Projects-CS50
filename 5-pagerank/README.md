#  PageRank

> Rank web pages by importance using Google's original PageRank algorithm — implemented two ways.

---

##  Overview

This project replicates the algorithm that made Google, Google. PageRank assigns each web page an importance score based on how many other pages link to it. Implemented using both a **random surfer simulation** (sampling) and an **iterative mathematical formula**.

---

##  AI Concepts Demonstrated

- **Markov Chains:** Each page visit depends only on the current page (memoryless)
- **Probability Distributions:** Modeling a random surfer's behavior
- **Damping Factor:** Simulating the probability a user follows a link vs. jumps randomly
- **Iterative Convergence:** Repeatedly updating values until they stabilize
- **Sampling vs. Iteration:** Two fundamentally different approaches to the same problem

---

##  How It Works

**Method 1 — Random Surfer (Sampling):**
- Simulate a user clicking links randomly across N samples
- With probability `d` (damping factor ≈ 0.85), follow a random link on the page
- With probability `1-d`, jump to any random page
- Count how often each page is visited → that's its rank

**Method 2 — Iterative Formula:**
- Start with equal rank `1/N` for all pages
- Repeatedly apply: `PR(p) = (1-d)/N + d * Σ PR(i)/NumLinks(i)`
- Continue until no rank changes by more than 0.001

---

##  How to Run

```bash
cd 5-pagerank
python pagerank.py corpus0
```

**Sample Output:**
```
PageRank Results from Sampling (n = 10000)
  1.html: 0.2295
  2.html: 0.3703
  3.html: 0.2299
  4.html: 0.1703
PageRank Results from Iteration
  1.html: 0.2316
  2.html: 0.3695
  3.html: 0.2312
  4.html: 0.1725
```

---

##  Files

| File | Description |
|------|-------------|
| `pagerank.py` | Both PageRank implementations |
| `corpus0/`, `corpus1/`, `corpus2/` | Sample web page corpuses |

---
