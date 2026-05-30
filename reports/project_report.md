# DriveSafe AI Project Report

## Summary

- Best model: Random Forest
- Best accuracy: 0.928
- Best weighted F1: 0.9276

## Dataset

- Rows: 5000
- Columns: 15 (final cleaned)
- Target classes: Safe, Moderate Risk, High Risk

## Generation Parameters

- `separation_factor`: 1.18
- `noise_level`: 0.12
- `label_noise`: 0.07

## Model Comparison (final run)

| Model | Accuracy | Weighted F1 |
| --- | ---: | ---: |
| Logistic Regression | 0.913 | 0.9124 |
| Random Forest | 0.928 | 0.9276 |
| XGBoost | 0.927 | (see metrics file) |

## Generated Artifacts

- Dataset: data/driver_risk_dataset.csv
- Metrics: reports/model_metrics.json
- Model: models/driver_risk_predictor.pkl
- Visuals directory: visuals/

## Notes

- The dataset is synthetic and tuned to produce a realistic classification task with controlled overlap between classes. Label noise and feature noise were introduced to avoid deterministic separability.
- The notebook `notebooks/drivesafe_analysis.ipynb` includes the full pipeline to reproduce these results.