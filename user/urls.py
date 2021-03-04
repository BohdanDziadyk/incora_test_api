from django.urls import path
from .views import *

urlpatterns = [
    path('', LogInView.as_view()),
]
