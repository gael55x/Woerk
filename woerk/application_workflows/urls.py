
from django.urls import path, include
from . import views

app_name = 'application_workflows'

urlpatterns = [
    path("", views.index),
    
]
