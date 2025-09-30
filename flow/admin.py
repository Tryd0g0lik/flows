from django.contrib import admin

# Register your models_views here.
from django.contrib.admin import SimpleListFilter
from django import forms

from flow.models_views.categories import CategoryModel  # , CategorySubcategory
from flow.models_views.content_flow import ContentFlowsModel
from flow.models_views.status import StatusModel
from flow.models_views.subcategories import SubCategory
from flow.models_views.types import TypeFlowModel


# class ProductAdminForm(forms.ModelForm):
#     sub_category = forms.ModelMultipleChoiceField(
#         queryset=SubCategory.objects.all(),
#         widget=forms.SelectMultiple(attrs={"size": "10"}),  # Размер списка
#         required=False,
#         label="Выберите категории",
#     )

# sub_category = forms.ModelChoiceField(
#     queryset=SubCategory.objects.none(),
#     label='Подкатегория',
#     required=False,
#     empty_label="Сначала выберите основную категорию"
# )
# dynamic_choice = forms.ChoiceField(
#     choices=[],
#     label='Динамический выбор'
# )
# class Meta:
#     model = CategorySubcategory
#     fields = "__all__"
# widgets = {
#     'subcategories': forms.CheckboxSelectMultiple,
# }

# def __init__(self, *args, **kwargs):
#     super().__init__(*args, **kwargs)
#
#     # Динамически заполняем choices
#     recent_products = SubCategory.objects.order_by('-name')[:5]
#     self.fields['dynamic_choice'].choices = [
#         (p.id, p.name) for p in recent_products
#     ] __init__(self, *args, **kwargs):
#     super().__init__(*args, **kwargs)
#
#     # Динамически заполняем choices
#     recent_products = SubCategory.objects.order_by('-name')[:5]
#     self.fields['dynamic_choice'].choices = [
#         (p.id, p.name) for p in recent_products
#     ]
# def __init__(self, *args, **kwargs):
#     super().__init__(*args, **kwargs)
#
#     if 'sub_category' in self.data:
#         try:
#             main_category_id = int(self.data.get('main_category'))
#             self.fields['sub_category'].queryset = SubCategory.objects.filter(
#                 parent_id=main_category_id
#             )
#         except (ValueError, TypeError):
#             pass


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
    # model = CategoryModel

    fields = [
        "id",
        "name",
    ]


@admin.register(TypeFlowModel)
class TypeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
    list_filter = [TitleFilter, "name"]
    search_fields = ["name"]
    inlines = [
        # CategoryModelInLine,
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


# @admin.register(CategorySubcategory)
# class CategorySubcategoryAdmin(admin.ModelAdmin):
# form = ProductAdminForm
# exclude = ["subcategory_id"]
# extra = 1
# list_display = [
#     "id",
#     "name",
# ]
# list_filter = [TitleFilter, "name"]
# search_fields = ["name"]
# # inlines = [SubCategoryInLine] # SubCategoryInLine
#
# ordering = ["name"]

# class Media:
#     js = ('admin/js/jquery.init.js', 'js/chained_selects.js')


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
    list_filter = [TitleFilter, "name"]
    search_fields = ["name"]
    ordering = ["name"]


@admin.register(ContentFlowsModel)
class ContentFlowsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "type_id",
        "status_id",
        "money",
        # "created_at",
        # "updated_at",
    ]
    list_filter = [
        TitleFilter,
        "type_id",
        "money",
    ]  # "created_at", "updated_at"
    inlines = []  # TypeInLine StatusModelInLine
    ordering = [
        "money",
        # "created_at",
    ]
