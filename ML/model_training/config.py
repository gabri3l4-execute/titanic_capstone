from pathlib import Path
#python -m ML.model_training.train
# Paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "ML" / "titanic_cleaned_training_data_FE.csv"

ARTIFACTS_DIR = PROJECT_ROOT / "ML" / "model_training" / "artifacts"
MODEL_OUTPUT = ARTIFACTS_DIR / "model.pkl"
SCALER_OUTPUT = ARTIFACTS_DIR / "scaler.pkl"
METRICS_OUTPUT = ARTIFACTS_DIR / "metrics.json"

# Target and features
TARGET = "Survived"

# If you want to be explicit, list features here; otherwise they’ll be inferred.
# FEATURES = ["Pclass", "Sex_male", "Age", "SibSp", "Parch", "Fare", "Embarked_S", "Embarked_C", "Embarked_Q"]
FEATURES = None  # use all non-target columns
FEATURES = ["Pclass",'Sex','Age', 'SibSp', 'Parch', 'Fare', 'Embarked','FamilySize','AgeGroup']
# General settings
RANDOM_STATE = 42
TEST_SIZE = 0.2
