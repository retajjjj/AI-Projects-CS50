#  Attention — Visualizing BERT's Self-Attention

> Visualize how BERT's transformer attention heads focus on different words to understand language context.
---

##  Overview

This project dives into the internals of **BERT** (Bidirectional Encoder Representations from Transformers) — one of the most influential language models ever built. By extracting and visualizing attention weights from BERT's 144 attention heads (12 layers × 12 heads), we gain intuition for what the model "pays attention to" when processing language.

---

##  AI Concepts Demonstrated

- **Transformer Architecture:** Encoder-based deep learning for NLP
- **Self-Attention Mechanism:** How tokens attend to each other in context
- **Multi-Head Attention:** 12 heads per layer, each learning different relationships
- **BERT (Masked Language Model):** Pre-trained bidirectional context understanding
- **Attention Visualization:** Generating diagrams to interpret neural network behavior
- **[MASK] Prediction:** Using BERT to predict masked words in context

---

##  How It Works

1. Tokenize an input sentence using BERT's WordPiece tokenizer
2. Run the sentence through the pre-trained BERT model (`bert-base-uncased`)
3. Extract attention weights from all 12 layers × 12 heads = 144 attention matrices
4. Generate diagrams showing which tokens each token attends to
5. Use BERT to predict a `[MASK]` token and show the top predictions

---

##  How to Run

```bash
cd 11-attention
pip install requirements.txt
python mask.py
```

**Input:** `"We turned down a narrow lane and passed through a small [MASK]."`

**Sample Output:**
```
We turned down a narrow lane and passed through a small field.
We turned down a narrow lane and passed through a small clearing.
We turned down a narrow lane and passed through a small park.
```

Attention diagrams are saved as `attention_layerX_headY.png` files.

---

##  Files

| File | Description |
|------|-------------|
| `mask.py` | BERT inference and attention diagram generation |

