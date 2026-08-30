# Third Order Audit

Structural auditing framework for research papers.

This project evaluates:

1. Falsification conditions
2. External checkability
3. Revision patterns

It does NOT assess whether claims are true.

---

## Installation

```bash
pip install -r requirements.txt
```

Set API key:

```bash
export OPENAI_API_KEY="YOUR_KEY"
```

Run:

```bash
python app.py
```

Paste a paper and terminate with:

```text
END
```

---

## Output

### Order 1

- Claims
- Falsification conditions

### Order 2

- External checkability analysis

### Order 3

- Revision classifications
- Ratio calculations

### Summary

- Pass/Fail overview
