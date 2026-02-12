from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, ListView
from django.urls import reverse_lazy
from .models import Passenger, PredictionRecord
from .forms import PredictionForm

import joblib
import pandas as pd

import pickle
import pandas as pd
from django.conf import settings
from pathlib import Path

# This loads our ML artifacts once at server startup. Efficient and clean.
MODEL_PATH = Path(settings.BASE_DIR) / "ML" / "model_training" / "artifacts" / "model.pkl"
PREPROCESSOR_PATH = Path(settings.BASE_DIR) / "ML" / "model_training" / "artifacts" / "scaler.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(PREPROCESSOR_PATH, "rb") as f:
    preprocessor = pickle.load(f)


def home(request):
    return render(request, "webapp/home.html", {"title": "home"})


class PredictionFormView(FormView):
    """
    View for the prediction form with SibSp dropdown
    """

    template_name = "webapp/prediction_form.html"
    form_class = PredictionForm
    success_url = reverse_lazy("prediction_list")

    def form_valid(self, form):
        # Save the form data to database
        prediction = form.save(commit=False)

        # TODO: Integrate with ML model here
        # For now, set mock prediction values
        prediction.survived_prediction = prediction.sex == "female"  # Mock logic
        prediction.probability = 0.72 if prediction.sex == "female" else 0.18

        prediction.save()
        return super().form_valid(form)


def predict_view(request):
    if request.method == "POST":
        # Extract form data
        data = {
            "Pclass": int(request.POST["pclass"]),
            "Sex": request.POST["sex"],
            "Age": float(request.POST["age"]),
            "SibSp": int(request.POST["sibsp"]),
            "Parch": int(request.POST["parch"]),
            "Fare": float(request.POST["fare"]),
            "Embarked": request.POST["embarked"],
        }

        # Convert to DataFrame
        df = pd.DataFrame([data])

        # Preprocess
        X_processed = preprocessor.transform(df)

        # Predict
        prediction = int(model.predict(X_processed)[0])
        probability = float(model.predict_proba(X_processed)[0][1])

        # Save to DB
        record = PredictionRecord.objects.create(
            pclass=data["Pclass"],
            sex=data["Sex"],
            age=data["Age"],
            sibsp=data["SibSp"],
            parch=data["Parch"],
            fare=data["Fare"],
            embarked=data["Embarked"],
            prediction=prediction,
            probability=probability,
        )

        return render(request, "webapp/prediction_form.html", {
            "prediction": prediction,
            "probability": round(probability, 3),
            "record_id": record.id,
        })

    return render(request, "webapp/prediction_form.html")
