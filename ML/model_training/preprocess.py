import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

from .config import DATA_PATH, TARGET, FEATURES, RANDOM_STATE, TEST_SIZE


def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH)
    return df


def split_features_target(df: pd.DataFrame):
    if FEATURES is None:
        feature_cols = [c for c in df.columns if c != TARGET]
    else:
        feature_cols = FEATURES

    X = df[feature_cols].copy()
    y = df[TARGET].copy()
    return X, y


def preprocess_data():
    df = load_data()
    X, y = split_features_target(df)

    # Identify categorical and numeric columns
    categorical_cols = X.select_dtypes(include=["object"]).columns.tolist()
    numeric_cols = X.select_dtypes(exclude=["object"]).columns.tolist()

    # Preprocessing pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
            ("num", StandardScaler(), numeric_cols),
        ]
    )

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y,
    )

    # Fit on train, transform both
    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)

    return X_train_processed, X_test_processed, y_train, y_test, preprocessor
