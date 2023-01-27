from django.urls import path
from . import views

urlpatterns = [
    path('sectors/', views.getSectors, name='sectors'),
    path('inputs/', views.createInput, name='inputs')
]