from sklearn.ensemble import RandomForestClassifier
import joblib
from pathlib import Path


MODELS_DIR = Path("ml/models")
MODELS_DIR.mkdir(parents=True, exist_ok=True)

DEFAULT_MODEL_PATH = MODELS_DIR / "random_forest.pkl"


def build_random_forest(
    n_estimators: int = 300,
    random_state: int = 42,
    n_jobs: int = -1
) -> RandomForestClassifier:
    """
    Create an untrained RandomForestClassifier with sensible defaults.
    """
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        random_state=random_state,
        n_jobs=n_jobs
    )
    return model


def train_random_forest(model, X_train, y_train):
    """
    Fit the RandomForest model.
    """
    model.fit(X_train, y_train)
    return model


def save_model(model, path: Path = DEFAULT_MODEL_PATH):
    """
    Persist the trained model to disk.
    """
    joblib.dump(model, path)
    return path