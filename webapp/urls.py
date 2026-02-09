from django.urls import path
from .views import HomePageView, PredictionFormView, PredictionListView

urlpatterns = [
    path('predict/', PredictionFormView.as_view(), name='predict'),
]