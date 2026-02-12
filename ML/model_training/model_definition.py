from sklearn.linear_model import LogisticRegression


def build_model():
    model = LogisticRegression(
        penalty="l2",
        C=1.0,
        solver="liblinear",
        max_iter=1000,
    )
    return model
