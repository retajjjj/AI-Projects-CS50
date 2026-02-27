#  Heredity

> Calculate the probability that family members carry a genetic trait using a Bayesian Network.

---

##  Overview

This project models the inheritance of a hearing-impairment gene across a family tree. Given observed traits (who has the impairment) and family relationships, the AI computes the probability that each person has 0, 1, or 2 copies of the gene — using a **Bayesian Network** and **joint probability** calculations.

---

##  AI Concepts Demonstrated

- **Bayesian Networks:** Representing probabilistic dependencies between variables
- **Joint Probability:** Computing the probability of a full assignment of variables
- **Conditional Probability:** P(gene | parents' genes), P(trait | gene count)
- **Normalization:** Converting unnormalized scores into proper probability distributions

---

##  How It Works

1. For each family, load who is observed to have the trait and parent-child relationships
2. Enumerate all possible gene count assignments (0, 1, or 2 copies) for every person
3. Compute the joint probability of each full assignment using:
   - Prior probabilities for individuals with no parents
   - Inheritance probabilities based on parents' gene counts
   - Mutation probability (gene copies can flip)
   - Trait expression probabilities conditioned on gene count
4. Accumulate these across all valid assignments → normalized probability distributions

---

##  How to Run

```bash
cd 6-heredity
python heredity.py data/family0.csv
```

**Sample Output:**
```
Harry:
  Gene:
    2: 0.0092
    1: 0.4557
    0: 0.5351
  Trait:
    True: 0.2665
    False: 0.7335
James:
  Gene:
    2: 0.1976
    1: 0.5106
    0: 0.2918
  Trait:
    True: 1.0000
    False: 0.0000
Lily:
  Gene:
    2: 0.0036
    1: 0.0136
    0: 0.9827
  Trait:
    True: 0.0000
    False: 1.0000
```

---

##  Files

| File | Description |
|------|-------------|
| `heredity.py` | Bayesian inference implementation |
| `data/` | Family CSV files (family0, family1, family2) |

