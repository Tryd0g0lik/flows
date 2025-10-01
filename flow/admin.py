from datetime import datetime
from django.contrib import admin

from admins.filters import TitleFilter
from admins.forms import ProductAdminForm, ContentFlowsModelForm
from flow.models_views.categories import CategoryModel
from flow.models_views.content_flow import ContentFlowsModel
from flow.models_views.status import StatusModel
from flow.models_views.subcategories import SubCategory
from flow.models_views.types import TypeFlowModel


class BasicInline(admin.StackedInline):
    extra = 1
    ordering = ["name"]
    fields = "__all__"


@admin.register(TypeFlowModel)
class TypeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "category",
    ]
    list_filter = [TitleFilter, "name"]
    search_fields = ["name"]
    ordering = ["name"]


@admin.register(StatusModel)
class StatusAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
    list_filter = [
        TitleFilter,
    ]
    search_fields = ["name"]
    ordering = ["name"]


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_filter = [
        TitleFilter,
    ]
    exclude = ["id"]
    search_fields = ["name"]
    ordering = ["name"]


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    exclude = ["id"]
    list_filter = [TitleFilter, "name"]
    search_fields = ["name"]
    ordering = ["name"]

    def categories_count(self, obj):
        return obj.categories.count()

    categories_count.short_description = "Кол-во категорий"


@admin.register(ContentFlowsModel)
class ContentFlowsAdmin(admin.ModelAdmin):
    form = ContentFlowsModelForm
    list_display = [
        "type_id",
        "status_id",
        "money",
        "formatted_created_at",
        "updated_at",
    ]
    readonly_fields = ["updated_at"]
    list_filter = [
        "type_id",
        "status_id",
        "created_at",
        "updated_at",
    ]
    inlines = []
    ordering = [
        "money",
    ]
    empty_value_display = "-empty-"
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "slug",
                    (
                        "created_at",
                        "updated_at",
                    ),
                    ("type_id", "status_id"),
                    "money",
                    "comment",
                ],
            },
        ),
        ("Системная информация", {"fields": [], "classes": ["collapse"]}),
    ]

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

    def formatted_created_at(self, obj):
        return obj.created_at.strftime("%d.%m.%Y %H:%M") if obj.created_at else "-"

    formatted_created_at.short_description = "Создан"
    formatted_created_at.admin_order_field = "created_at"
