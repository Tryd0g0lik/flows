"""
flow/flow_api/views_api.py
"""

import logging
from adrf import viewsets

from flow.flow_api.serializers import (
    FlowSerializer,
    StatusSerializer,
    SubCategorySerializer,
    CategorySerializer,
    TypeFlowSerializer,
)
from flow.models_views.categories import CategoryModel
from flow.models_views.content_flow import ContentFlowsModel
from flow.models_views.status import StatusModel
from flow.models_views.subcategories import SubCategory
from flow.models_views.types import TypeFlowModel
from logs import configure_logging

# log
log = logging.getLogger(__name__)
configure_logging(logging.INFO)


# FLOW
class FlowView(viewsets.ModelViewSet):
    queryset = ContentFlowsModel.objects.all()
    serializer_class = FlowSerializer


# STATUS
class StatusView(viewsets.ModelViewSet):
    queryset = StatusModel.objects.all()
    serializer_class = StatusSerializer


# SUBСATEGORY
class СategoryView(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


# CATEGORY
class SubСategoryView(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


# TYPE
class TypeView(viewsets.ModelViewSet):
    queryset = TypeFlowModel.objects.all()
    serializer_class = TypeFlowSerializer


#
