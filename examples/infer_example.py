import joblib
import pandas as pd
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parents[1] / 'models' / 'driver_risk_predictor.pkl'

def load_model(path=MODEL_PATH):
    return joblib.load(path)

def example_single_predict(model):
    # Example feature order must match the training `raw_features` used in the notebook
    sample = pd.DataFrame([
        {
            'age': 34,
            'experience_years': 12,
            'avg_speed': 58.0,
            'harsh_braking': 1,
            'sudden_acceleration': 1,
            'mobile_usage_minutes': 18.0,
            'night_driving_hours': 1.5,
            'fatigue_score': 3.0,
            'traffic_violations': 0,
            'seatbelt_compliance': 0.95,
            'weather_risk': 2,
            'weekly_driving_hours': 35.0,
            'accident_history': 0,
        }
    ])
    pred = model.predict(sample)
    print('Sample prediction:', pred[0])

if __name__ == '__main__':
    m = load_model()
    example_single_predict(m)
