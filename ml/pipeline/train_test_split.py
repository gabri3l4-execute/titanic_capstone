from sklearn.model_selection import train_test_split
import pandas as pd


def stratified_train_test_split(
    X: pd.DataFrame,
    y,
    test_size: float = 0.2,
    random_state: int = 42
):
    """
    Perform a stratified train/test split.
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )
    return X_train, X_test, y_train, y_test
