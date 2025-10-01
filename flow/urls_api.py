"""
flow/urls_api.py
"""

from django.urls import path, include
from rest_framework import routers

from flow.flow_api.views_api import (
    FlowView,
    StatusView,
    SubСategoryView,
    СategoryView,
    TypeView,
)


router = routers.DefaultRouter()
router.register(r"flow", FlowView, basename="flows")

router.register(r"status", StatusView, basename="statuses")
router.register(r"subcategory", SubСategoryView, basename="subcategories")
router.register(r"category", СategoryView, basename="categories")
router.register(r"type", TypeView, basename="types")

urlpatterns = [
    path("", include(router.urls), name="api_main_flows_keys"),
]
