from django.contrib import admin

# Register your models_views here.
from django.contrib.admin import SimpleListFilter

from flow.models_views.categories import CategoryModel
from flow.models_views.content_flow import ContentFlowsModel
from flow.models_views.status import StatusModel
from flow.models_views.subcategories import SubCategory
from flow.models_views.types import TypeFlowModel


class TitleFilter(SimpleListFilter):
    title = "Заголовок начинается с:"
    parameter_name = "title_start"

    def lookups(self, request, model_admin):
        return [
            ("a", "A"),
            ("b", "B"),
            ("c", "C"),
            ("d", "D"),
            ("e", "E"),
            ("f", "F"),
            ("g", "G"),
            ("h", "H"),
            ("i", "I"),
            ("j", "J"),
            ("k", "K"),
            ("l", "L"),
            ("m", "M"),
            ("n", "N"),
            ("o", "O"),
            ("p", "P"),
            ("q", "Q"),
            ("r", "R"),
            ("s", "S"),
            ("t", "T"),
            ("v", "V"),
            ("w", "W"),
            ("x", "X"),
            ("y", "Y"),
            ("z", "Z"),
        ]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(tname__icontains=self.value())
        return queryset


class BasicInline(admin.StackedInline):
    extra = 1
    ordering = ["name"]
    fields = "__all__"


class TypeInLine(BasicInline):
    model = TypeFlowModel


class StatusModelInLine(BasicInline):
    model = StatusModel


class CategoryModelInLine(BasicInline):
    model = CategoryModel


class SubCategoryInLine(BasicInline):
    model = SubCategory


@admin.register(TypeFlowModel)
class TypeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "category_id",
        "name",
    ]
    list_filter = [TitleFilter, "name"]
    search_fields = ["name"]
    inlines = [
        CategoryModelInLine,
    ]
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
    list_display = [
        "id",
        "name",
    ]
    list_filter = [TitleFilter, "name"]
    search_fields = ["name"]

    ordering = ["name"]


@admin.register(CategoryModel)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "category_id",
        "name",
    ]
    list_filter = [TitleFilter, "category_id", "name"]
    search_fields = ["name"]
    inlines = [
        CategoryModelInLine,
    ]
    ordering = ["name"]


@admin.register(ContentFlowsModel)
class ContentFlowsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "type_id",
        "category_id",
        "subcategory_id",
        "status_id",
        "money",
        "created_at",
        "updated_at",
    ]
    list_filter = [TitleFilter, "type_id", "money", "created_at", "updated_at"]
    inlines = [CategoryModelInLine, SubCategoryInLine, TypeInLine, StatusModelInLine]
    ordering = [
        "money",
        "created_at",
    ]
