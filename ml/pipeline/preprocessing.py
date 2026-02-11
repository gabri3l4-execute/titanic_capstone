import pandas as pd
from pathlib import Path

DATA_DIR = Path("ml/data")
PROCESSED_DIR = DATA_DIR / "processed"  # platform-correct Path pointing at the processed folder 


def load_fe_training_data(
    filename: str = "fe_training_clean.csv"
) -> pd.DataFrame:
    """
    Load feature-engineered training data from processed folder.
    """
    path = PROCESSED_DIR / filename
    df = pd.read_csv(path)
    return df


def split_features_target(
    df: pd.DataFrame,
    target_col: str = "Survived"
):
    """
    Split a dataframe into X (features) and y (target).
    """
    X = df.drop(columns=[target_col])
    y = df[target_col]
    return X, y
