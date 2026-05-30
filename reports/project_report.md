# DriveSafe AI Project Report

## Summary
- Best model: Logistic Regression
- Best accuracy: 0.720
- Best weighted F1: 0.707

## Dataset
- Rows: 5000
- Columns: 20
- Target classes: Safe, Moderate Risk, High Risk

## Model Comparison
              model  accuracy  weighted_f1
Logistic Regression     0.720     0.706989
            XGBoost     0.687     0.669291
      Random Forest     0.687     0.676121

## Generated Artifacts
- Dataset: d:\Driver Risk Score Analysis\data\driver_risk_dataset.csv
- Metrics: d:\Driver Risk Score Analysis\reports\model_metrics.json
- Model: d:\Driver Risk Score Analysis\models\driver_risk_predictor.pkl
- Visuals directory: d:\Driver Risk Score Analysis\visuals