"""
admins/filters.py
"""

from wagtail.admin.filters import WagtailFilterSet

from flow.models_views.categories import CategoryModel
from flow.models_views.content_flow import ContentFlowsModel
from flow.models_views.status import StatusModel
from flow.models_views.subcategories import SubCategory
from flow.models_views.types import TypeFlowModel


# FLOW
class FlowFilterSet(WagtailFilterSet):
    class Meta:
        model = ContentFlowsModel
        fields = [
            "id",
            "type_id",
            "status_id",
            "money",
            "created_at",
            "updated_at",
        ]


# STATUS
class StatusFilterSet(WagtailFilterSet):
    class Meta:
        model = StatusModel
        fields = [
            "id",
            "name",
        ]


# SUBСATEGORY
class СategoryFilterSet(WagtailFilterSet):
    class Meta:
        model = CategoryModel
        fields = ["id", "name", "subcategories"]


# CATEGORY
class SubСategoryFilterSet(WagtailFilterSet):
    class Meta:
        model = SubCategory
        fields = [
            "id",
            "name",
        ]


# TYPE
class TypeFilterSet(WagtailFilterSet):
    class Meta:
        model = TypeFlowModel
        fields = [
            "id",
            "name",
        ]


#
