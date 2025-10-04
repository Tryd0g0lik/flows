"""
flow/admin.py
https://docs.wagtail.org/en/stable/reference/viewsets.html#wagtail.admin.viewsets.model.ModelViewSet.list_filter
"""

from datetime import datetime
from time import localtime
from django.contrib import admin
from django.utils.formats import date_format
from wagtail.admin.ui.tables import BaseColumn

from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.ui.tables import UpdatedAtColumn

from admins.filters import (
    FlowFilterSet,
    СategoryFilterSet,
    StatusFilterSet,
    SubСategoryFilterSet,
    TypeFilterSet,
)

from flow.models_views.categories import CategoryModel

from flow.models_views.content_flow import ContentFlowsModel


from flow.models_views.status import StatusModel
from flow.models_views.subcategories import SubCategory
from flow.models_views.types import TypeFlowModel


class CustomCreatedAtColumn(BaseColumn):
    def __init__(self, *args, **kwargs):
        kwargs["sort_key"] = "created_at"  # Указываем поле для сортировки
        super().__init__("created_at", *args, **kwargs)

    def get_value(self, instance):
        return instance.created_at

    def render_value(self, instance, parent_context):
        created_at = self.get_value(instance)
        if created_at:
            return date_format(
                localtime(created_at), format="DATETIME_FORMAT", use_l10n=True
            )
        return ""


class CustomUpdatedAtColumn(BaseColumn):
    def __init__(self, *args, **kwargs):
        kwargs["sort_key"] = "updated_at"  # Указываем поле для сортировки
        super().__init__(*args, **kwargs)

    def get_value(self, instance):
        return instance.updated_at

    def render_value(self, instance, parent_context):
        updated_at = self.get_value(instance)
        if updated_at:
            return date_format(
                localtime(updated_at), format="DATETIME_FORMAT", use_l10n=True
            )
        return ""


class BasicInline(admin.StackedInline):
    extra = 1
    ordering = ["name"]
    fields = "__all__"


# class TypeAdmin(admin.ModelAdmin):
@register_snippet
class TypeAdmin(SnippetViewSet):
    model = TypeFlowModel
    list_display = [
        "id",
        "name",
        "category",
    ]
    list_filter = ["id", "name", CustomCreatedAtColumn(label="created_at")]
    search_fields = ["name"]
    ordering = ["name"]
    list_per_page = 25
    filterset_class = TypeFilterSet
    base_url_path = "internal/type"

    def categories_count(self, obj):
        return obj.categories.count()


@register_snippet
class StatusAdmin(SnippetViewSet):
    model = StatusModel
    list_display = ["id", "name", UpdatedAtColumn()]
    list_filter = [
        "name",
    ]
    search_fields = ["name"]
    ordering = ["name"]
    list_per_page = 25
    base_url_path = "internal/status"
    filterset_class = StatusFilterSet


@register_snippet
class CategoryAdmin(SnippetViewSet):
    model = CategoryModel
    list_display = ["name", "slug", UpdatedAtColumn()]
    search_fields = [
        "name",
    ]
    ordering = ["name"]
    list_per_page = 25
    base_url_path = "internal/category"
    filterset_class = СategoryFilterSet


@register_snippet
class SubCategoryAdmin(SnippetViewSet):
    model = SubCategory
    exclude = ["id"]
    search_fields = ["name"]
    ordering = ["name"]
    list_display = ["name", UpdatedAtColumn()]
    list_per_page = 25
    admin_url_namespace = "SubCategory_views"
    base_url_path = "internal/member"
    filterset_class = SubСategoryFilterSet


@register_snippet
class ContentFlowsAdmin(SnippetViewSet):
    model = ContentFlowsModel
    list_display = [
        "type_id",
        "status_id",
        "money",
        "created_at",
        "updated_at",
        UpdatedAtColumn(),
        "slug",
    ]
    readonly_fields = ["updated_at"]
    search_fields = ["money"]
    inlines = []
    list_per_page = 25
    filterset_class = FlowFilterSet

    base_url_path = "internal/flow"

    def save_model(self, request, obj, form, change):
        form_created_at = form.cleaned_data.get("created_at")
        if change:
            if form_created_at:
                obj.created_at = form_created_at
        else:
            if form_created_at:
                obj.created_at = form_created_at
            else:
                obj.created_at = datetime.now()
        super().save_model(request, obj, form, change)
