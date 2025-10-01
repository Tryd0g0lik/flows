from django.contrib import admin

from django.contrib.admin import SimpleListFilter
from django import forms

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
            return queryset.filter(name__icontains=self.value())
        return queryset


class BasicInline(admin.StackedInline):
    extra = 1
    ordering = ["name"]
    fields = "__all__"


class TypeInLine(BasicInline):
    model = TypeFlowModel
    fields = [
        "id",
        "name",
    ]


class StatusModelInLine(BasicInline):
    model = StatusModel
    fields = [
        "id",
        "name",
    ]


class SubCategoryInLine(BasicInline):
    model = SubCategory
    fields = [
        "id",
        "name",
    ]


class CategoryModelInLine(BasicInline):
    fields = ["id", "name", "subcategories"]


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


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = "__all__"
        widgets = {
            "categories": forms.SelectMultiple(attrs={"size": "10"}),
        }


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
    list_display = [
        "type_id",
        "status_id",
        "money",
        "created_at",
        "updated_at",
    ]

    list_filter = [
        "money",
        "created_at",
        "updated_at",
    ]  # "created_at", "updated_at"
    inlines = []  # TypeInLine StatusModelInLine
    ordering = [
        "money",
    ]
