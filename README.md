# HeHAims 4U – Public Experiments

This repository contains small, reproducible experiments testing how grammatical structure affects belief certainty, emotion, and confidence.

The core CMIS / HeHAims engine and formulas live in a private repository. This public repo exists to make specific claims testable and repeatable without exposing protected IP.

## Repository Layout

- `docs/claim.md` — statement of the falsifiable claim and predictions.
- `experiments/modal_certainty/` — first experiment: does modal grammar alone change perceived certainty?
  - `modal_certainty_test.py` — simple console script to collect human ratings.
  - `results.md` — space to log observations.

## Running the modal certainty test

```bash
python experiments/modal_certainty/modal_certainty_test.py
```

You will be prompted to rate how certain each sentence sounds on a 1–10 scale.
