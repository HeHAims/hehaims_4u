# CMIS-AIHK Demo (public)

This demo notebook (`docs/cmis-aiahk-demo.ipynb`) is a streamlined view of the CMIS-AIHK pipeline:
- Load local ULMFI-style train/test CSVs.
- Walk through CMIS framing, feature engineering, and CMIS-guided model training.
- Run a quick hybrid reasoning test (CMIS + Aristotle/Hume/Kahneman).

## Run instructions
1) Requirements: Python 3.9+ with `pandas`, `numpy`, `scikit-learn`, `matplotlib`. Install with:
   ```bash
   pip install pandas numpy scikit-learn matplotlib
   ```
2) Data: place `train.csv` and `test.csv` under `./data/ulmfi_competition/` (relative to the repo root), or edit the data-load cell to point to your CSVs.
3) Open `docs/cmis-aiahk-demo.ipynb` and run top-to-bottom. The notebook prints guidance and will error if the CSVs are missing.

## Notes
- Patent/medical artifact cells were intentionally omitted; the full experimental sandbox remains private.
- Streamlit UI is not bundled here; this repo keeps the notebook-focused demo only.
- Public demo only; no production claims.
