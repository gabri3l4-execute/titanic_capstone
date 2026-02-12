from pathlib import Path

from .preprocess import preprocess_data
from .model_definition import build_model
from .evaluate import evaluate
from .utils import save_pickle, save_json
from .config import MODEL_OUTPUT, SCALER_OUTPUT, METRICS_OUTPUT, ARTIFACTS_DIR


def main():
    print("▶ Starting training pipeline...")

    # Ensure artifacts dir exists
    from .utils import ensure_dir
    ensure_dir(Path(ARTIFACTS_DIR))

    # Preprocess
    print("▶ Loading and preprocessing data...")
    X_train, X_test, y_train, y_test, scaler = preprocess_data()

    # Build model
    print("▶ Building model...")
    model = build_model()

    # Train
    print("▶ Training model...")
    model.fit(X_train, y_train)

    # Evaluate
    print("▶ Evaluating model...")
    metrics = evaluate(model, X_test, y_test)
    print("▶ Metrics:", metrics)

    # Save artifacts
    print("▶ Saving artifacts...")
    save_pickle(model, MODEL_OUTPUT)
    save_pickle(scaler, SCALER_OUTPUT)
    save_json(metrics, METRICS_OUTPUT)

    print("✅ Training pipeline complete.")


if __name__ == "__main__":
    main()
