from django.urls import path
from .views import home, PredictionFormView, PredictionListView

urlpatterns = [
    path("", home, name="home"),
    path("predict/", PredictionFormView.as_view(), name="predict"),
    path("predictions/", PredictionListView.as_view(), name="prediction_list"),
]
