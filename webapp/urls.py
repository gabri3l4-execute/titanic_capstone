from django import views
from django.urls import path
from .views import PredictionFormView 

urlpatterns = [
    path('predict/', PredictionFormView.as_view(), name='predict'),
    path('rate/<int:pk>/', views.submit_rating, name='submit_rating'),

]

