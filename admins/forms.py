"""
admins/forms.py
"""

from django import forms
from flow.models_views.categories import CategoryModel
from flow.models_views.content_flow import ContentFlowsModel
from django.utils.translation import gettext_lazy as _


# For CategoryAdmin from admin.py
class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = "__all__"
        widgets = {
            "categories": forms.SelectMultiple(attrs={"size": "10"}),
        }


# For ContentFlowsAdmin from admin.py
class ContentFlowsModelForm(forms.ModelForm):
    created_at = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        required=False,
        label=_("Date of creation"),
    )

    def __init__(self, *args, **kwargs):
        """
        TODO: Доработать "created_at"  редактирование
        """
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.created_at:
            self.initial["created_at"] = self.instance.created_at

    class Meta:
        model = ContentFlowsModel
        fields = "__all__"
