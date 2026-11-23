
import mlflow
import pandas as pd

from src.features import one_hot_encoder
from src.feature_engineering import create_features

MODEL_URI = "models:/Employee Attrition/1"
THRESHOLD = 0.35

model = mlflow.sklearn.load_model(MODEL_URI)


def predict(input_data):
    df = pd.DataFrame([input_data])

    df = create_features(df)
    df = one_hot_encoder(df)

    probability = model.predict_proba(df)[0, 1]
    prediction = int(probability >= THRESHOLD)

    return {
        "prediction": "Attrition" if prediction == 1 else "No Attrition",
        "probability": round(float(probability), 4) }
