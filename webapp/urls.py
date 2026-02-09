from django.urls import path
from .views import PredictionFormView 

urlpatterns = [
    path('predict/', PredictionFormView.as_view(), name='predict'),
]