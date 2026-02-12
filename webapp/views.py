import pandas as pd
import pickle
from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import FormView, ListView, DetailView
from django.urls import reverse_lazy
from django.conf import settings
from .forms import PredictionForm
from .models import PredictionRecord
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

        # Convert form data into a DataFrame for the ML pipeline
        data = {
            "Pclass": prediction.pclass,
            "Sex": prediction.sex,
            "Age": prediction.age,
            "SibSp": prediction.sibsp,
            "Parch": prediction.parch,
            "Fare": float(prediction.fare) if prediction.fare is not None else 0.0,
            "Embarked": prediction.embarked,
        }

        df = pd.DataFrame([data])

        # Preprocess using your saved pipeline
        X_processed = preprocessor.transform(df)

        # Predict
        pred_value = int(model.predict(X_processed)[0])
        pred_proba = float(model.predict_proba(X_processed)[0][1])

        # Save results into the Django model
        prediction.survived_prediction = bool(pred_value)
        prediction.probability = pred_proba

        prediction.save()
        return redirect('prediction_result', pk=prediction.pk)
    

def submit_rating(request, pk):
        if request.method == 'POST':
          prediction = get_object_or_404(PredictionRecord, pk=pk)
          rating = request.POST.get('rating')
          if rating:
            prediction.rating = int(rating)
            prediction.save()
        return redirect('prediction_result', pk=pk)



class PredictionResultView(DetailView):
    model = PredictionRecord
    template_name = 'webapp/result.html'
    context_object_name = 'prediction'



class PredictionListView(ListView):
    model = PredictionRecord
    template_name = "webapp/prediction_list.html"
    context_object_name = "predictions"
    ordering = ["-created_at"]  # newest first
    paginate_by = 20  # optional
