from django.urls import path
from .views import Desk

urlpatterns = [
    path('', Desk.as_view()),
]