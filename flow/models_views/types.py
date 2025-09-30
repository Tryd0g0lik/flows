"""
models_views/type.py
"""

from django.db import models

# Create your models_views here.
from django.core import validators
from django.utils.translation import gettext_lazy as _

from flow.models_views.categories import CategoryModel
from project.settings import TYPE_OF_FLOW


class TypeFlowModel(models.Model):
    category_id = models.ForeignKey(
        CategoryModel,
        on_delete=models.CASCADE,
        related_name="typename",
        verbose_name=_("Type"),
    )
    name = models.CharField(
        max_length=50,
        # choices=TYPE_OF_FLOW,
        # default=TYPE_OF_FLOW[0][0],
        help_text="50 is MAX length of name.",
        verbose_name=_("Name of type"),
        unique=True,
        validators=[
            validators.RegexValidator(
                regex="(^[A-Za-z][A-Za-z0-9_]{1,50}$)",
                message="Check valid a name.",
            ),
            validators.MaxLengthValidator(50),
        ],
    )

    class Meta:
        verbose_name = _("Type")
        verbose_name_plural = _("Types")
        unique_together = ["category", "name"]
        ordering = ["category", "name"]

    def __str__(self):
        return self.name
