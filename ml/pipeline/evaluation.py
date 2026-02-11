from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd


def evaluate_classifier(model, X_test, y_test) -> dict:
    """
    Evaluate a classifier on test data and return metrics.
    """
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    report_str = classification_report(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    print("Accuracy:", acc)
    print("\nClassification report:\n", report_str)
    print("\nConfusion matrix:\n", cm)

    metrics = {
        "accuracy": acc,
        "classification_report": report_str,
        "confusion_matrix": pd.DataFrame(
            cm,
            index=["Actual_0", "Actual_1"],
            columns=["Pred_0", "Pred_1"],
        ),
    }
    return metrics