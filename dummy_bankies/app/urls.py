from django.urls import path, include
from . import views

urlpatterns = [
    # ex: /app/
    path("", views.IndexView.as_view(), name="index"),
]
