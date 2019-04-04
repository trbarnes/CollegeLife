from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('suggestions/', views.suggestions_json),
]
