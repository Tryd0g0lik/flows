from django.urls import path, include
from flow.views import main

urlpatterns = [
    path("", main),
]
