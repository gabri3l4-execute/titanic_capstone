import joblib
import pandas as pd
from pathlib import Path

MODEL_PATH = Path("ml/models/random_forest.pkl")


def load_model(path: Path = MODEL_PATH):
    """
    Load a trained model from disk.
    """
    model = joblib.load(path)
    return model


def predict_single(model, input_dict: dict):
    """
    Predict for a single passenger represented as a dict of features.
    """
    df = pd.DataFrame([input_dict])
    pred = model.predict(df)[0]
    return int(pred)