#  Degrees of Separation

> Find the shortest path between any two Hollywood actors using the "Six Degrees of Kevin Bacon" concept.

---

##  Overview

This project implements **Breadth-First Search (BFS)** to find the shortest connection between two actors through shared movie appearances. It mirrors the real-world "Six Degrees of Separation" theory and is a classic application of graph traversal in AI.

---

##  AI Concepts Demonstrated

- **Breadth-First Search (BFS):** Guarantees the shortest path in an unweighted graph
- **Graph Representation:** Actors as nodes, movies as edges
- **Frontier & Explored Sets:** Core components of uninformed search
- **State Space Search:** Modeling a real-world problem as a search problem

---

##  How It Works

1. Load a dataset of actors and movies
2. Build a graph where actors are connected if they share a movie
3. Use BFS to find the minimum number of "hops" between two actors
4. Output the path of movies and co-stars connecting them

---

##  How to Run

```bash
cd 1-degrees
python degrees.py large
```

**Example:**
```
Name: Emma Watson
Name: Jennifer Lawrence
3 degrees of separation.
1: Emma Watson and Brendan Gleeson starred in Harry Potter and the Order of the Phoenix
2: Brendan Gleeson and Michael Fassbender starred in Trespass Against Us
3: Michael Fassbender and Jennifer Lawrence starred in X-Men: First Class
```

---

##  Files

| File | Description |
|------|-------------|
| `degrees.py` | Main program with BFS implementation |
| `util.py` | Node, StackFrontier, QueueFrontier classes |
| `large/` | Full dataset (actors, movies, stars) |
| `small/` | Smaller dataset for quick testing |

