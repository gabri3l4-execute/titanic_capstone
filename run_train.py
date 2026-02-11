from ml.pipeline.preprocessing import load_fe_training_data, split_features_target
from ml.pipeline.feature_engineering import apply_feature_engineering
from ml.pipeline.train_test_split import stratified_train_test_split
from ml.pipeline.model_training import build_random_forest, train_random_forest, save_model
from ml.pipeline.evaluation import evaluate_classifier


def run_training():
    # 1. Load data
    df = load_fe_training_data()

    # 2. (Optional) extra feature engineering
    df = apply_feature_engineering(df)

    # 3. Split features/target
    X, y = split_features_target(df, target_col="Survived")

    # 4. Train/test split
    X_train, X_test, y_train, y_test = stratified_train_test_split(X, y)

    # 5. Build and train model
    model = build_random_forest()
    model = train_random_forest(model, X_train, y_train)

    # 6. Evaluate
    metrics = evaluate_classifier(model, X_test, y_test)

    # 7. Save model
    model_path = save_model(model)

    print(f"\nModel saved to: {model_path}")
    print("\nTraining complete.")
    return model, metrics


if __name__ == "__main__":
    run_training()
