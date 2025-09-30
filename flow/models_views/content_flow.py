"""
models_views/content_flow.py
"""

from django.core.validators import MinValueValidator, MaxLengthValidator, RegexValidator
from django.db import models

# Create your models_views here.

from django.utils.translation import gettext_lazy as _

from flow.models_views.categories import CategoryModel
from flow.models_views.status import StatusModel
from flow.models_views.types import TypeFlowModel


class ContentFlowsModel(models.Model):
    """
    This is model for basic of flow's lines
    """

    type_id = models.ForeignKey(
        TypeFlowModel,
        on_delete=models.CASCADE,
        verbose_name=_("Type"),
        help_text=_("Select type name"),
    )
    category_id = models.ForeignKey(
        CategoryModel,
        on_delete=models.CASCADE,
        verbose_name=_("Category"),
        help_text=_("Select category name"),
    )
    subcategory_id = models.ForeignKey(
        on_delete=models.CASCADE,
        verbose_name=_("Subcategory"),
        help_text=_("Select subcategory name"),
    )

    status_id = models.ForeignKey(
        StatusModel,
        on_delete=models.CASCADE,
        verbose_name=_("Status"),
        help_text=_("Select status name"),
    )
    money = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MinValueValidator(300000)],
        help_text=_("Sum from 1 before 300000"),
    )
    comment = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        validators=[
            MaxLengthValidator(100),
            RegexValidator(
                regex="(^[A-Za-z][A-Za-z_ .,]{1,150}$)",
            ),
        ],
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
