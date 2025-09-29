"""
flow/urls_api.py
"""
from django.urls import path, include
from rest_framework import routers
# from flow.flow_api.views_api import PageDetailView

router = routers.DefaultRouter()
# router.register(r"content", PageDetailView, basename="contents")

urlpatterns = [
    # path("", include(router.urls), name="api_main_content_keys"),
]

