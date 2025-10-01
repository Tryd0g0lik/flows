from adrf import serializers

from flow.models_views.categories import CategoryModel
from flow.models_views.content_flow import ContentFlowsModel
from flow.models_views.status import StatusModel
from flow.models_views.subcategories import SubCategory
from flow.models_views.types import TypeFlowModel


# FLOW
class FlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentFlowsModel
        fields = "__all__"
        read_only_fields = ("id", "updated_at")


# STATUS
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusModel
        fields = "__all__"
        read_only_fields = ("id",)


# CATEGORY
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"
        read_only_fields = ("id",)


# SubCATEGORY
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"
        read_only_fields = ("id",)


# TYPE
class TypeFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeFlowModel
        fields = "__all__"
        read_only_fields = ("id",)
