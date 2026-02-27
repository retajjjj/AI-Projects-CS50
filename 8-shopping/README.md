#  Shopping Intent Classifier

> Predict whether an online shopper will complete a purchase using k-Nearest Neighbors classification.

---

##  Overview

Using real e-commerce session data (12,000+ records), this project trains a **k-Nearest Neighbors** classifier to predict whether a user will make a purchase before leaving the site. Features include pages visited, time spent, bounce rates, and more.

---

##  AI Concepts Demonstrated

- **Supervised Learning:** Training on labeled historical data
- **k-Nearest Neighbors (k-NN):** Classifying based on similarity to k closest training points
- **Feature Engineering:** Encoding categorical data (month, visitor type) as numeric
- **Train/Test Split:** Evaluating model on unseen data
- **Sensitivity & Specificity:** Measuring true positive and true negative rates separately

---

##  How It Works

1. Load and parse the `shopping.csv` dataset (17 features per session)
2. Encode categorical variables (months → integers, returning visitor → boolean)
3. Split data 60/40 into training and test sets
4. Train a k-NN classifier (`k=1`) using scikit-learn
5. Evaluate on test set: report sensitivity (recall for buyers) and specificity (recall for non-buyers)

---

##  How to Run

```bash
cd 8-shopping
pip install scikit-learn
python shopping.py shopping.csv
```

**Sample Output:**
```
Correct: 4072
Incorrect: 860
True Positive Rate: 38.40%
True Negative Rate: 90.65%

```

---

##  Files

| File | Description |
|------|-------------|
| `shopping.py` | Data loading, model training, and evaluation |
| `shopping.csv` | Online shoppers intention dataset |

---

##  Dataset Features

The dataset includes: `Administrative`, `Informational`, `ProductRelated` pages visited, time spent on each, `BounceRates`, `ExitRates`, `PageValues`, `SpecialDay`, `Month`, `OperatingSystems`, `Browser`, `Region`, `TrafficType`, `VisitorType`, `Weekend`, and target `Revenue`.

