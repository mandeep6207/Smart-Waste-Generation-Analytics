# DriveSafe AI

Driver Risk Score Analytics System

DriveSafe AI is a lightweight, notebook-centric transportation analytics project that builds a synthetic driver-risk classification workflow end to end. The project focuses on practical driver safety analytics rather than application scaffolding, so the complete implementation lives in a single notebook: [notebooks/drivesafe_analysis.ipynb](notebooks/drivesafe_analysis.ipynb).

## Project Overview

The notebook generates a realistic synthetic dataset, explores the data, engineers safety-oriented features, trains multiple machine learning models, compares their performance, and exports the best model together with metrics and visualizations.

## Transportation Analytics Context

Driver risk scoring is a core transportation analytics problem. Operational teams use it to identify unsafe driving patterns, prioritize coaching, and reduce incident exposure. This project models those behaviors with interpretable features such as speed, braking, fatigue, phone usage, weather exposure, and history of violations.

## Dataset Overview

- File: [data/driver_risk_dataset.csv](data/driver_risk_dataset.csv)
- Rows: 5,000
- Target classes: `Safe`, `Moderate Risk`, `High Risk`
- Features include age, driving experience, average speed, harsh braking, sudden acceleration, mobile use, night driving, fatigue, violations, seatbelt compliance, weather risk, weekly hours, and accident history.

## Workflow

1. Generate the synthetic dataset inside the notebook.
2. Load and profile the data.
3. Analyze missing values and clean the table.
4. Engineer behavior-focused risk features.
5. Produce EDA summaries and visualizations.
6. Split the data and train Logistic Regression, Random Forest, and XGBoost.
7. Compare the models and export the best one.
8. Save metrics and a written project report.

## Visualizations

The notebook writes figures into [visuals/](visuals/), including:

- [visuals/risk_distribution.png](visuals/risk_distribution.png)
- [visuals/driver_behavior_heatmap.png](visuals/driver_behavior_heatmap.png)
- [visuals/speed_analysis.png](visuals/speed_analysis.png)
- [visuals/feature_importance.png](visuals/feature_importance.png)

## Model Comparison

Final evaluated results saved by the notebook (after dataset tuning):

| Model | Accuracy | Weighted F1 |
| --- | ---: | ---: |
| Logistic Regression | 0.913 | 0.912 |
| Random Forest | 0.928 | 0.928 |
| XGBoost | 0.927 | (see `reports/model_metrics.json`) |

The exported best model is [models/driver_risk_predictor.pkl](models/driver_risk_predictor.pkl).

## Results

- Best model: Random Forest
- Best accuracy: 92.8%
- Best weighted F1: 0.928

## Installation

Install the Python dependencies from [requirements.txt](requirements.txt):

```bash
pip install -r requirements.txt
```

## Usage

1. Open [notebooks/drivesafe_analysis.ipynb](notebooks/drivesafe_analysis.ipynb).
2. Run the notebook from top to bottom.
3. Review the generated dataset, visualizations, metrics, report, and model artifact.

## Outputs

- [models/driver_risk_predictor.pkl](models/driver_risk_predictor.pkl)
- [reports/model_metrics.json](reports/model_metrics.json)
- [reports/project_report.md](reports/project_report.md)
- [visuals/](visuals/)

## Notes

- The project is intentionally lightweight and notebook-centric.
- All core logic lives in the notebook rather than a separate application or package structure.
- The dataset is synthetic and designed to be realistic enough for transportation analytics practice.

## Reproducibility

- Final dataset generation parameters are recorded in [reports/model_metrics.json](reports/model_metrics.json). Example:

```
{
	"separation_factor": 1.18,
	"noise_level": 0.12,
	"label_noise": 0.07
}
```
